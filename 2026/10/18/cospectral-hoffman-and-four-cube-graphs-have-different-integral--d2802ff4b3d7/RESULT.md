# Cospectral Hoffman and four-cube graphs have different integral independence-complex homotopy types

## Finding

Let \(H\) denote the sixteen-vertex Hoffman graph and \(Q_4\) the four-dimensional binary cube graph, with the exact conventions below. They have identical adjacency spectra:
\[
\chi_{A(H)}(\lambda)=\chi_{A(Q_4)}(\lambda)
=\lambda^6(\lambda^2-4)^4(\lambda^2-16).
\]
Nevertheless their ordinary independence complexes have different **integral homotopy types**:
\[
\boxed{\operatorname{Ind}(H)\simeq\bigvee^3 S^3,\qquad
\operatorname{Ind}(Q_4)\simeq\bigvee^7 S^3.}
\]
In particular, \(\widetilde H_3(\operatorname{Ind}(H);\mathbb Z)\cong\mathbb Z^3\) and \(\widetilde H_3(\operatorname{Ind}(Q_4);\mathbb Z)\cong\mathbb Z^7\); every other reduced integral homology group of either complex vanishes. The independence polynomials \(I_G(z)=\sum_{S\in\operatorname{Ind}(G)}z^{|S|}\) satisfy the sharper identity
\[
\boxed{I_H(z)-I_{Q_4}(z)=4z^5.}
\]
The preexisting four-cube wedge decomposition and the classical cospectrality are **not** claimed as new. The contribution is the exact integral homotopy type of the Hoffman-graph independence complex and this complete comparison for the distinguished cospectral pair.

## Assumptions and scope

Both graphs are simple and have exactly sixteen vertices. The Hoffman graph \(H\) has bipartition \(\{0,\ldots,7\}\sqcup\{8,\ldots,15\}\) and adjacency matrix \(A(H)=\left(\begin{smallmatrix}0&D\\D^{\mathsf T}&0\end{smallmatrix}\right)\), where
\[
D=\begin{pmatrix}
1&1&1&1&0&0&0&0\\
1&1&1&0&1&0&0&0\\
1&0&0&1&0&1&1&0\\
0&1&0&1&0&1&0&1\\
0&0&1&1&0&0&1&1\\
1&0&0&0&1&1&1&0\\
0&1&0&0&1&1&0&1\\
0&0&1&0&1&0&1&1
\end{pmatrix}.
\]
This is the standard Hoffman graph matrix tabulated in MathWorld [2]. For \(Q_4\), identify vertices with four-bit words (integers \(0,\ldots,15\)); join two words exactly when their Hamming distance is one. The independence complex \(\operatorname{Ind}(G)\) has a simplex for every vertex subset containing no graph edge. All homotopies are of geometric realizations and are nonequivariant. There is no assertion about arbitrary graphs sharing these spectra.

## Proof

**1. The two characteristic polynomials agree.** Construct both symmetric integral adjacency matrices from the definitions. An exact Faddeev–LeVerrier recurrence, working only with integer matrix multiplication, determines every coefficient of each characteristic polynomial. For each graph it returns the coefficient sequence (highest to lowest degree)
\[
(1,0,-32,0,352,0,-1792,0,4352,0,-4096,0,0,0,0,0,0),
\]
which is the expansion of \(\lambda^6(\lambda^2-4)^4(\lambda^2-16)\). The companion verifier recomputes these matrices and coefficients independently from the stated adjacency definitions; the classical spectral coincidence is also documented in [1,2].

**2. Complete face enumeration.** Each vertex subset is uniquely represented by its sixteen-bit membership mask. Visit *all* \(2^{16}\) masks; a mask is admissible precisely if none of its selected vertices has a selected neighbor. The exact counts of masks with \(k=0,1,\ldots,8\) selected vertices are
\[
\begin{array}{c|rrrrrrrrr}
k&0&1&2&3&4&5&6&7&8\\\hline
H&1&16&88&208&228&132&56&16&2\\
Q_4&1&16&88&208&228&128&56&16&2
\end{array}
\]
and no larger independent set exists. Hence \(I_H(z)-I_{Q_4}(z)=4z^5\). This calculation is exhaustive and integer-valued, not a sample.

**3. Full acyclic Morse certificates.** On the face poset of *nonempty* independent sets, process pivot vertices \(v=0,1,\ldots,15\). At pivot \(v\), pair every currently unmatched face \(a\) omitting \(v\) with \(a\cup\{v\}\), provided that the latter is also currently unmatched. Each pivot gives disjoint pairs. The successive numbers of pairs are
\[
\begin{aligned}
H:&\quad(177,18,32,22,12,8,6,4,80,6,0,5,0,1,0,0);\\
Q_4:&\quad(176,134,10,4,5,5,13,4,0,3,4,3,3,1,1,1).
\end{aligned}
\]
Thus the respective \(746\) and \(742\) nonempty faces are reduced by \(371\) and \(367\) pairs. The unmatched Hoffman masks are exactly \(1,5888,28928,45312\), one vertex and three four-vertex simplices. The unmatched four-cube masks are exactly \(1,1680,2400,10370,17028,24600,33064,33096\), one vertex and seven four-vertex simplices.

To prove *acyclicity*, orient every Hasse incidence from larger face to smaller face, except reverse each matched incidence. The supplied `morse_certificate.json` gives all \(371+367\) pairs and a complete topological ordering for each resulting directed graph. The independent `verify.py` rebuilds all faces and all incidences from scratch, verifies the matching against the pivot rule, verifies every certificate position, and checks that **every one** of the \(2836\) Hoffman incidences and \(2816\) four-cube incidences points forward. It separately runs a complete directed-acyclicity traversal. Therefore both matchings are acyclic, not merely numerically plausible.

**4. Homotopy consequences.** Forman's acyclic-matching theorem, in the independence-complex formulation of [3], produces a CW complex with exactly one zero-cell and three three-cells for \(H\), and one zero-cell and seven three-cells for \(Q_4\), with no other cells. Each three-cell attaches to a point and so has constant attaching map. These CW complexes are respectively wedges of three and seven three-spheres. The resulting integral homology groups, homotopy types, and their inequivalence follow. An independent calculation of every reduced mod-two simplicial boundary rank is included in the verifier as a redundant check.

## Verification

Execute `python3 verify.py` in a directory containing `morse_certificate.json`. No nonstandard Python package is required. The program independently reconstructs both graphs, enumerates all independent subsets, verifies both full explicit acyclic Morse certificates, calculates every reduced mod-two boundary rank, and computes both integral characteristic polynomials. It terminates with `VERIFY_OK_HOFFMAN_Q4_SPECTRAL_INDEPENDENCE_HOMOTOPY` only after all assertions succeed. The finite case is exhaustively enumerated; no extrapolation to other graph sizes is involved.

## Relationship to prior work

The Hoffman graph was introduced as a spectral mate of \(Q_4\) in Hoffman's 1963 work. Van Dam's primary 2008 treatment [1, §3] analyzes this exact pair as an example of adjacency-cospectral graphs with different distance-regularity. MathWorld [2] supplies the standard exact adjacency matrix. Neither gives a homotopy type for its ordinary independence complex. Bousquet-Mélou, Linusson, and Nevo [3] introduce and apply acyclic matchings to independence complexes of square grids; their main homotopy classification treats open/cylindrical grids, not the Hoffman graph. A separately available exact calculation [4] establishes the \(\bigvee^7 S^3\) homotopy type for \(\operatorname{Ind}(Q_4)\); this antecedent is adopted, not rediscovered. A further known rational symmetry calculation for \(Q_4\) does not determine the Hoffman-graph homotopy type. The new content is precisely the Hoffman result and the comparison of both integral homotopy types at fixed adjacency spectrum.

## Limitations

The theorem is about this one canonical cospectral pair, not a characterization of all cospectral graphs. Its method gives a complete finite certificate, not a general closed expression for independence-complex topology from adjacency eigenvalues. No claim is made about integral automorphism representations or an equivariant homotopy equivalence. Although primary sources and mathematical databases were compared, undiscovered prior presentations of the Hoffman computation remain possible; this study is not an independent scientific audit.

## References

[1] E. R. van Dam, *The spectral excess theorem for distance-regular graphs: a global (over)view*, Electronic Journal of Combinatorics 15 (2008), R129, §3, published 2008-10-13. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v15i1r129/pdf/

[2] E. W. Weisstein, *Hoffman Graph*, MathWorld. https://mathworld.wolfram.com/HoffmanGraph.html

[3] M. Bousquet-Mélou, S. Linusson, E. Nevo, *On the independence complex of square grids*, first posted 2007-01-30, arXiv:math/0701890. https://arxiv.org/abs/math/0701890

[4] *The four-cube independence complex is a wedge of seven three-spheres*, public mathematical result with full proof and finite acyclic-Morse certificate. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-four-cube-independence-complex-is-a-wedge-of-seven-three-sph--9947aaad144c

[5] R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145. https://doi.org/10.1006/aima.1997.1650
