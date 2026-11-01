# Full hyperoctahedral top-homology character of the four-cube independence complex

## Finding

Let \(Q_4\) be the sixteen-vertex graph of the four-dimensional cube, and let \(X=\operatorname{Ind}(Q_4)\). The full cube automorphism group is \(B_4=(C_2)^4\rtimes S_4\), of order \(384\). Write \(U_4\) for the three-dimensional augmentation representation of \(S_4\), inflated across the translation subgroup, and \(W_4\) for the defining four-dimensional signed-permutation representation of \(B_4\). Then the complete reduced rational homology representation is

\[
\widetilde H_3(X;\mathbb Q)\cong
(\operatorname{sgn}_{S_4}\otimes U_4)\oplus\bigwedge^3W_4,
\qquad \widetilde H_i(X;\mathbb Q)=0\quad(i\ne3).
\]

The two summands have dimensions three and four and are irreducible over \(\mathbb Q\). In particular, if \(T=(C_2)^4\) is the translation subgroup, the \(T\)-invariant part of degree-three homology is the sign-twisted standard \(S_4\)-representation and has dimension three. The four weight-three Fourier characters of \(T\) each occur once; every other nontrivial translation character occurs zero times. Consequently

\[
\widetilde H_*(|X|/B_4;\mathbb Q)=0,
\qquad \dim_\mathbb Q\widetilde H_3(|X|/T;\mathbb Q)=3.
\]

## Assumptions and scope

Vertices of \(Q_4\) are the bit vectors \(v\in\{0,1\}^4\), represented by integers \(0\le v<16\); two are adjacent exactly when their Hamming distance is one. A simplex in \(X\) is a set of pairwise nonadjacent cube vertices. The cube automorphism associated to \((p,b)\in S_4\times\{0,1\}^4\) sends a vertex \(v\) to \(p(v)\oplus b\). This identifies the entire automorphism group, since the image of a base vertex has 16 choices and the ordered images of its four neighbors have at most 24 choices. The signed-permutation representation is defined on basis vectors \(e_j\) by \(W_4(p,b)e_j=(-1)^{b_{p(j)}}e_{p(j)}\).

The augmentation representation \(U_4\subset\mathbb Q^4\) consists of vectors whose four coordinates sum to zero. Its twist by \(\operatorname{sgn}_{S_4}\) is trivial on \(T\). No integral representation-lattice classification or equivariant homotopy equivalence is asserted. Geometric quotients use the ordinary orbit-space topology, and all homology coefficients appearing in this result are rational.

## Proof

**Homological concentration.** Enumerate the complete set of independent subsets of \(Q_4\) using their 16-bit membership masks. The number of subsets by cardinality \(0,\ldots,8\) is

\[
(1,16,88,208,228,128,56,16,2).
\]

The exact reduced simplicial boundary ranks over \(\mathbb F_2\), with the augmented boundary from vertices to the empty face included, are

\[
(1,15,73,135,86,42,14,2,0)
\]

for the boundaries indexed by subset cardinality \(1,\ldots,9\). Hence reduced mod-two homology has dimension seven in degree three and vanishes otherwise. Every rational Betti number is bounded above by the corresponding mod-two Betti number. The alternating independent-subset count equals \(7\), or equivalently reduced Euler characteristic equals \(-7\). Therefore rational homology is concentrated in degree three and is exactly seven-dimensional.

**Exact character formula.** Let \(p\in S_4\), \(b\in\{0,1\}^4\), and let \(f(p)\) denote the number of fixed coordinate positions. Put \(\epsilon(p)=\operatorname{sgn}(p)\). The degree-three character is

\[
\chi(p,b)=\epsilon(p)\left(f(p)-1+
\sum_{j:p(j)=j}(-1)^{|b|-b_j}\right).
\tag{1}
\]

Here \(|b|\) is the number of ones in \(b\). To calculate the left side directly, apply the augmented simplicial Lefschetz formula. A nonempty invariant simplex contributes the sign of the induced permutation of its vertices, multiplied by the alternating chain sign. Because reduced homology is in odd degree three, its trace equals the signed sum \(\sum_{S=gS}(-1)^{|S|}\operatorname{sgn}(g|_S)\), including the empty simplex. More simply, decompose the 16 vertices into orbits of \(g\). Discard each orbit containing a graph edge, and form the finite conflict graph of the remaining orbits; the trace is its independent-set polynomial evaluated at \(-1\). Selecting an admissible orbit contributes precisely \(-1\), since a cycle on \(t\) selected vertices has permutation sign \((-1)^{t-1}\), which multiplies \((-1)^t\).

These two exact, independent methods were exhaustively compared with the closed right side of (1) for **all 384 group elements**. The universe is exhaustive because \(24\cdot16=384\), not sampled. The standalone program reconstructs every face and every orbit and executes all three evaluations; each equality is asserted, and it also checks constancy on all 20 signed-cycle conjugacy classes. This is an exact finite proof of (1) for the whole finite group, not an infinite extrapolation.

**Irreducible decomposition.** The trace of \(\operatorname{sgn}_{S_4}\otimes U_4\) is \(\epsilon(p)(f(p)-1)\). The exterior-cube character of a four-dimensional invertible representation satisfies

\[
\operatorname{tr}(\bigwedge^3W_4(g))
=\det(W_4(g))\operatorname{tr}(W_4(g)^{-1}).
\]

Since a signed permutation matrix is orthogonal, \(\operatorname{tr}(W_4(g)^{-1})=\operatorname{tr}(W_4(g))=\sum_{j:p(j)=j}(-1)^{b_j}\), while \(\det W_4(g)=\epsilon(p)(-1)^{|b|}\). Their sum is exactly formula (1). Equality of all finite-group rational characters implies isomorphism of the representations.

The three-dimensional summand is the sign twist of the irreducible augmentation representation of \(S_4\). The four-dimensional summand is irreducible under \(B_4\): the translation subgroup acts diagonally on the four exterior-basis elements by the four distinct Fourier weights of cardinality three, and \(S_4\) acts transitively on those weights. The same observation proves the claimed translation-character multiplicities. The characters are inequivalent because one is trivial on \(T\) and the other has no \(T\)-fixed vectors. Averaging the traces over \(T\) yields \(\chi^{T}(p)=\epsilon(p)(f(p)-1)\), while averaging over \(B_4\) gives zero since the standard \(S_4\)-module has no invariants. Finite-group rational transfer identifies the rational homology of the geometric quotients with the corresponding invariant homology, proving the consequences.

## Verification

Run `python3 verify_q4_symmetry.py` using Python 3 and only its standard library. The script reconstructs all 743 faces including the empty set, the augmented mod-two boundary ranks, all 384 cube automorphisms, all 20 conjugacy classes, and the independent fixed-face/orbit and closed-form character calculations. The complete successful log is `verification_output.txt`, beginning with the exact marker `Q4_INDEPENDENCE_SYMMETRY_VERIFIED`. The Fourier decomposition and the weight-three stabilizer action are checked separately. The finite signed-character identity and mod-two boundary computations are independently reconstructible from this code without reliance on stored matrices.

## Relationship to prior work

Bousquet-Mélou, Linusson and Nevo [1] treat independence complexes of square grids and explain why the toroidal case is topologically different from their open and cylindrical cases. The identification \(Q_4\cong C_4\mathbin\square C_4\) places the graph inside the historical periodic-grid setting. Barmak [2] gives general tools for independence complexes of triangle-free graphs. A previously available exact finite calculation of the same \(Q_4\) complex establishes its nonequivariant homotopy type \(\bigvee^7 S^3\), which fixes the homology rank but leaves the full automorphism action unclassified. Neither ordinary Betti numbers nor a nonequivariant sphere-wedge equivalence determines the two irreducible summands or the translation-quotient character above.

The calculation is distinct from the scale-three Čech nerve on the same cube (which has nonzero homology in two dimensions), and from the total-three-cut complex of the open 4-by-4 grid (a different graph and complex). These different-complex representation calculations do not imply the present result. The source comparisons do not establish absolute publication priority.

## Limitations

The result concerns exactly the 16-vertex graph \(Q_4\), rational coefficients and the full signed-coordinate automorphism group. It does not classify integral equivariant homology lattices, equivariant homotopy decompositions, higher-dimensional cubes, other filtrations or the integral topology of the symmetry quotients. The finite certificate has been checked by the same mathematical analysis that derived it; no independent mathematical audit was performed. An equivalent unindexed computation might exist.

## References

[1] M. Bousquet-Mélou, S. Linusson and E. Nevo, *On the independence complex of square grids*, arXiv:math/0701890, first public 2007-01-30; https://arxiv.org/abs/math/0701890 .

[2] J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418, first public 2010-07-02; https://arxiv.org/abs/1007.0418 .
