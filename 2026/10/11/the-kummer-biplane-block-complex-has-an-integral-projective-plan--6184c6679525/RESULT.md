# The Kummer biplane block complex has an integral projective-plane summand

## Finding

Let \(P=\{0,1,2,3\}^{2}\) and for every \((i,j)\in P\) let
\[
B_{ij}=\{(i,k):k\ne j\}\cup\{(k,j):k\ne i\}.
\]
Let \(K\) be the abstract simplicial complex on \(P\) whose faces are **all** subsets of the sixteen six-point blocks \(B_{ij}\), together with the empty face. This is the block simplicial complex of the classical Kummer biplane, a symmetric \(2\)-\((16,6,2)\) design.

**Theorem.** There is an integral homotopy equivalence
\[
\boxed{K\simeq\mathbb{RP}^{2}\vee\bigvee^{55}S^{2}.}
\]
In particular \(\pi_1(K)\cong\mathbb Z/2\), \(\widetilde H_1(K;\mathbb Z)\cong\mathbb Z/2\), \(\widetilde H_2(K;\mathbb Z)\cong\mathbb Z^{55}\), and all other reduced integral homology groups vanish. The same simplicial complex is \(\mathcal N(R)\), the open Lovász neighborhood complex of the \(4\times4\) rook graph \(R=K_4\square K_4\), and is simplicially isomorphic to \(\mathcal N(S)\) for the Shrikhande graph \(S\). In fact the asserted homotopy type holds for these two specific graphs; it is not a claim about the other two nonisomorphic biplanes with the same parameters.

## Assumptions and scope

The underlying grid is a labeled sixteen-point set. Adjacency in \(R\) means distinct cells share a row or column. Adjacency in \(S\) is on \((\mathbb Z/4)^2\) with six differences \((\pm1,0),(0,\pm1),(1,1),(-1,-1)\). All graph neighborhoods are *open*, so the center vertex is excluded. For every graph \(G\), the neighborhood complex \(\mathcal N(G)\) has as faces the subsets of some common open neighborhood, irrespective of whether the common neighbor belongs to the subset. A simplicial complex includes the empty face; the face-count and Morse matching below concern nonempty faces only. Homotopy type refers to geometric realization.

## Proof

**1. Explicit finite model and isomorphism.** Encode \((i,j)\) by \(4i+j\), with indices from zero to fifteen. The full sixteen blocks are exactly the open neighborhoods of the rook graph; every block has six elements and any two distinct blocks meet in two elements. In the above Cayley model of \(S\), the open-neighborhood blocks are carried to those of \(R\) by the following point permutation, listed as images of the indices \(0,1,\ldots,15\):

`(0,8,2,10,7,3,5,1,14,6,12,4,9,13,11,15)`.

Their block-center labels are sent by the independent permutation

`(11,1,9,3,2,4,0,6,5,15,7,13,12,10,14,8)`.

Direct substitution verifies all sixteen block images. These explicit maps prove simplicial isomorphism of the two neighborhood complexes. No claim is made that the graphs themselves are isomorphic.

**2. Exact face enumeration and discrete-Morse matching.** Enumerate every nonempty subset of the sixteen size-six blocks, deduplicating subsets of intersecting blocks. This exhausts the finite face set because these sixteen blocks are all maximal faces. It gives \(808\) nonempty faces, with face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(16,120,320,240,96,16).
\]
For either graph, start with every nonempty face unmatched. For each vertex index \(v=0,1,\ldots,15\) in that order, traverse the currently unmatched face masks in increasing numeric order and pair any face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\), provided both are still unmatched. Remove both faces immediately; never match the empty face. The algorithm produces exactly \(375\) pairs and \(58\) critical faces: one vertex, one edge, and fifty-six triangles. The independent directed-Hasse test orients matched incidences from lower to upper and all other codimension-one incidences from upper to lower. A topological sort visits all \(808\) faces along all \(2736\) such incidences. Hence there is no directed cycle, and the matching is acyclic.

By Forman's discrete Morse theorem, \(K\) has a homotopy-equivalent two-dimensional CW model with one \(0\)-cell, one \(1\)-cell, and fifty-six \(2\)-cells; there are no higher critical cells. The one-cell attaches at its endpoints to the unique vertex, giving a circle. Every two-cell attaching map is thus classified up to homotopy by its integral winding degree around that circle.

**3. Signed attaching-degree certificate.** Orient each simplex by increasing vertex index. If \(\tau\) is obtained from \(\sigma\) by deleting its \(j\)-th vertex, write the simplicial incidence number as \([\sigma:\tau]=(-1)^j\), indexing from zero. Define a projection \(E(e)\) from each simplicial edge \(e\) to the single critical edge as follows: it is \(1\) for the critical edge, \(0\) for any edge that is an upper member of a matched vertex–edge pair, and for an edge \(e\) matched upward to a triangle \(t\),
\[
E(e)=-[t:e]\sum_{e'\subset t,\ e'\ne e}[t:e']E(e').
\]
Acyclicity makes the recursion terminating. The integer attaching degree of a critical triangle \(c\) is
\[
d(c)=\sum_{e\subset c}[c:e]E(e).
\]
The standalone verifier recomputes these integer coefficients directly from the full matched face poset. On the Shrikhande labeling, among the fifty-six critical triangles there are four degrees \(-2\), thirty-nine degrees \(0\), and thirteen degrees \(2\). On the rook labeling, there are nine degrees \(-2\), thirty-eight degrees \(0\), and nine degrees \(2\). In both cases the list contains a degree of absolute value two and every degree belongs to \(\{-2,0,2\}\).

Attach one degree-two cell first; attaching a disk to a circle by degree two yields \(\mathbb{RP}^2\). Every remaining attaching loop has degree \(0\) or \(\pm2\), hence becomes null-homotopic after that first attachment since \(\pi_1(\mathbb{RP}^2)=\mathbb Z/2\). Attaching a \(2\)-cell by a null-homotopic map wedges on an \(S^2\). There are fifty-five remaining cells. Thus the claimed homotopy equivalence follows, including the integral two-torsion and the full fundamental group.

## Verification

The self-contained standard-library programs `artifacts/verify_morse.py` and `artifacts/verify_chains.py` reconstruct both graph families without referring to external data. Run `python3 artifacts/verify_morse.py` followed by `python3 artifacts/verify_chains.py`. The former verifies all blocks, faces, the point/block permutation, each matching, acyclicity, signed gradient-path incidences and degree multisets. The latter independently constructs every simplicial boundary matrix and checks ranks over \(\mathbb F_2\), \(\mathbb F_3\) and \(\mathbb F_5\). In particular, the mod-two reduced Betti numbers are \((0,1,56,0,0,0)\) in dimensions zero through five, while the mod-three and mod-five Betti numbers are \((0,0,55,0,0,0)\); these are cross-checks, not replacements for the integral homotopy proof. Expected and observed deterministic output is stored in `artifacts/verification_output.txt`.

## Relationship to prior work

The construction of the classical Kummer biplane by sixteen six-point row/column blocks, and its distinction from other \(2\)-\((16,6,2)\) biplanes, are classical. White's *Modelling biplanes on surfaces* treats a surface embedding of this design, not the geometric realization of the high-dimensional abstract block simplicial complex studied here. These should not be confused. Matsushita's *Fundamental groups of neighborhood complexes* gives general graph-theoretic fundamental-group theory but does not state the present exact \(2\)-torsion computation or the wedge decomposition. Shukla's classification applies to graphs with maximal degree at most three and to certain four-regular circulants; the two graphs here are six-regular. The related higher-degree integral homology/quotient description for general rook-graph neighborhood complexes does not determine the degree-one and degree-two attaching maps or the total homotopy type here. The point/block isomorphism alone is not asserted as a new result; the integral homotopy calculation is the additional contribution.

## Limitations

The proof concerns this explicitly constructed Kummer biplane and these two graph presentations only. The sixteen-block enumeration is exhaustive in this finite domain, but does not classify the other nonisomorphic biplanes or general symmetric designs. Literature searches and checked statements cannot exclude an unindexed equivalent homotopy computation. The supplied verifiers independently check algebraic consequences to several characteristics, while the full homotopy conclusion rests on the verified acyclic matching and signed integer attaching degrees.

## References

1. T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803v1 (first public 2012-10-10); J. Math. Sci. Univ. Tokyo 24 (2017), 321–353. https://arxiv.org/abs/1210.2803 ; https://www.ms.u-tokyo.ac.jp/journal/abstract_e/jms240302_e.html
2. A. T. White, *Modelling biplanes on surfaces*, European Journal of Combinatorics 25 (2004), 899–909. https://doi.org/10.1016/j.ejc.2003.05.004
3. S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, Electronic Journal of Combinatorics 26 (2019), P2.4. https://arxiv.org/abs/1802.04526
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145. https://doi.org/10.1006/aima.1997.1650
