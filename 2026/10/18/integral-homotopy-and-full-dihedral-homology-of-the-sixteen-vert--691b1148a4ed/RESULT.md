# Integral homotopy and full dihedral homology of the sixteen-vertex Möbius-ladder matching complex

## Finding
Let \(G\) be the sixteen-vertex Möbius ladder with vertex set \(\mathbb Z/16\mathbb Z\), cycle edges \(\{i,i+1\}\) for all \(i\), and eight opposite-vertex edges \(\{i,i+8\}\) for \(0\le i<8\). Let \(K=\mathcal M(G)\) be its **ordinary matching complex**: a simplex is an arbitrary set of pairwise vertex-disjoint graph edges, not a family of complete perfect matchings. Then
\[
K\simeq (S^4\vee S^4)\vee\bigvee^4 S^5.
\]
In particular its only nonzero reduced integral homology groups are \(\widetilde H_4(K;\mathbb Z)\cong\mathbb Z^2\) and \(\widetilde H_5(K;\mathbb Z)\cong\mathbb Z^4\); both are torsion-free.

The entire graph automorphism group is \(D_{16}=\langle r,s\mid r^{16}=s^2=1,\ srs=r^{-1}\rangle\) with \(r(i)=i+1\) and \(s(i)=-i\). Denote by \(L_{\rho,\sigma}\) the rational one-dimensional character on which \(r\) acts as \(\rho\in\{\pm1\}\) and \(s\) as \(\sigma\in\{\pm1\}\). Let \(E\) be the two-dimensional rational module with
\[
r\mapsto\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
s\mapsto\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]
Then
\[
\widetilde H_4(K;\mathbb Q)\cong L_{+,+}\oplus L_{-,-},\qquad
\widetilde H_5(K;\mathbb Q)\cong L_{+,-}\oplus L_{-,+}\oplus E.
\]
Consequently the antipodal half-turn \(r^8\) acts trivially in both homological degrees, but the invariant subspace of the **full** automorphism group has dimension one in degree four and zero in degree five.

## Assumptions and scope
All graph edges are unordered pairs of distinct integers modulo sixteen. Matching-complex simplices are unordered sets of mutually vertex-disjoint edges. Orient a simplex by placing the graph edges in increasing lexicographic order; the simplicial differential is the standard alternating deletion boundary. The assertion is for this particular finite graph, with integral homotopy and rational representation conclusions; it is not an infinite-family classification.

## Proof

**1. Exhaustive face-poset construction and an acyclic discrete-Morse matching.** Enumerate the \(24\) edges lexicographically. Represent any nonempty simplex as a \(24\)-bit integer. The exhaustive matching-independent-set recursion in `verify.py` yields the face counts in dimensions \(0\) through \(7\):
\[
(24,228,1096,2834,3880,2588,696,47).
\]
It visits all faces because it adds only a later-indexed graph edge disjoint from every already-chosen edge; each nonempty matching has exactly one increasing enumeration.

Apply elementary face-poset matching successively along the following zero-based lexicographic graph-edge indices:
`[23,20,5,4,2,14,3,22,13,1,12,17,0,9,7,19,8,11,15,16,6,10,18,21]`.
For each index, pair every currently unpaired face without that edge with its unpaired union with the edge, when available. The procedure produces \(5690\) matched pairs and exactly one critical vertex, five critical four-simplices, and seven critical five-simplices. It is acyclic: reverse each matched cover relation in the face-poset Hasse diagram, direct all other cover relations downwards, and topologically sort the resulting graph. The verifier constructs all relations and consumes every vertex; therefore there are no closed gradient paths. Standard discrete Morse theory gives a CW model with exactly these cells.

**2. Integral cellular attaching degrees.** With critical four-simplices and five-simplices ordered by increasing bitmask, algebraic cancellation along the gradient paths yields the *integer* Morse boundary from seven five-cells to five four-cells, written as seven column vectors:
\[
\begin{array}{rrrrr}
0&0&0&0&0\\
0&1&0&-1&-1\\
0&0&-1&0&1\\
0&0&-1&0&1\\
0&0&0&0&0\\
0&0&-1&0&1\\
0&1&0&1&0
\end{array}.
\]
The \(3\times3\) submatrix in rows \((1,2,4)\) and columns \((1,2,6)\) (zero-based indexing, after transposing the displayed seven-by-five matrix) has determinant \(-1\). Every \(4\times4\) minor vanishes. Hence the integer boundary has rank \(3\) and its three nonzero Smith invariants are all \(1\). Because there are no critical cells in dimensions one, two or three, the four-skeleton is a wedge of five four-spheres. Each five-cell attaching map lands in \(\pi_4(\bigvee^5 S^4)\cong\mathbb Z^5\), and is therefore determined by this cellular degree vector. Integral changes of degree-four and degree-five cellular bases and cancellation of the three unit pairs give a wedge of two four-spheres and four five-spheres. The calculation proves the integral homotopy equivalence, not merely Betti numbers.

**3. Full graph symmetry and equivariant homology.** A graph rim edge is contained in exactly one four-cycle, while a rung is contained in two. Thus any graph automorphism preserves the rim edges, which form a sixteen-cycle; it must be one of its \(32\) dihedral automorphisms. All those rotations/reflections preserve the rungs, so the full automorphism group is precisely \(D_{16}\).

For every graph automorphism, the verifier computes the signed permutation of simplex orientations. An independent signed simplicial Lefschetz calculation, over all \(11{,}393\) faces, finds the unreduced alternating trace \(L(r^a)\) to be \(-1,1,3,1\) for \(a\equiv0,1,2,3\pmod4\), and \(L(r^a s)=1\) when \(a\) is even and \(5\) when \(a\) is odd. By the integral result, reduced homology lies only in degrees four and five; thus \(L(g)=1+\operatorname{tr}(g\mid H_4)-\operatorname{tr}(g\mid H_5)\).

To separate the degrees, compute the equivariant boundary complexes in rotation eigenspaces over \(\mathbb F_{97}\), using the primitive sixteenth root \(8\), and in reflection eigenspaces over \(\mathbb F_{101}\). The only rotation weights for degree four are \(k=0,8\), each once, and for degree five are \(k=0,4,8,12\), each once. Reflections \(s\) and \(rs\) have respectively \((H_4^+,H_4^-;H_5^+,H_5^-)=(1,1;2,2)\) and \((2,0;1,3)\). Both characteristics are coprime to \(|D_{16}|=32\), the integral homology is torsion-free, and the group algebras are semisimple. The multiplicities therefore determine the characteristic-zero dihedral modules. Rotation weights \(0,8\) correspond to the one-dimensional lines \(r=+1,-1\), and weights \(4,12\) together form \(E\). The reflection eigenmultiplicities fix the signs of the four lines, giving exactly the displayed decomposition. The signed Lefschetz values for all \(32\) elements provide a separate consistency test.

## Verification
Run `python3 verify.py` with a standard Python 3 interpreter; no external dependencies or data files are required. It reconstructs the graph, all simplices and their oriented boundaries; verifies complete mod-two ranks; checks the acyclic matching by topological sort; recomputes the *integer* Morse boundary and its unit minor and rank bound; checks signed Lefschetz traces of all dihedral elements; and independently recomputes the two primes' equivariant homology multiplicities. Its final line is `VERIFY_OK_MOBIUS16_ORDINARY_MATCHING_COMPLEX`. The mod-two calculation alone is not used to infer integral torsion-freeness or a homotopy equivalence: those follow from the integral Morse complex.

## Relationship to prior work
Björner, Lovász, Vrećica and Živaljević (1994) developed foundational chessboard and matching-complex topology; that publication supplies the archival historical framework. Matsushita (2018/2019) studies the ordinary matching complexes of small **open** grid graphs via line-graph complexes. Agarwal and Basak (2026, arXiv:2608.30601) determine the homotopy types of **independence** and **perfect-matching** complexes for Möbius and circular ladders. A perfect-matching complex is a different simplicial object from the ordinary matching complex of *all* matchings used here: for the present graph their reported perfect-matching homotopy type is \(S^3\vee S^3\), not the two-degree wedge above. The present graph and complex are also different from matching complexes of the Möbius–Kantor generalized Petersen graph and the Wagner graph. No theorem inspected in those sources gives the above ordinary-complex homotopy and complete dihedral homology module.

## Limitations
The result is specific to sixteen vertices; no assertion is made for all Möbius ladders or about minimal supports of homology classes. The proof is exact and reproducible but computationally intensive in its full acyclic-matching and dihedral verification. Existing results under alternate terminology or in unindexed sources could potentially overlap the conclusion; publication priority is not guaranteed. No independent audit is asserted.

## References
- A. Björner, L. Lovász, S. T. Vrećica, R. T. Živaljević, *Chessboard Complexes and Matching Complexes*, J. London Math. Soc. **49** (1994), 25–39. DOI: 10.1112/jlms/49.1.25 (publicly published 1994-02-01).
- T. Matsushita, *Matching complexes of small grids*, arXiv:1812.11000 (submitted 2018-12-28), Electron. J. Combin. **26** (2019), P3.1. DOI: 10.37236/8480.
- A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601 (2026).
