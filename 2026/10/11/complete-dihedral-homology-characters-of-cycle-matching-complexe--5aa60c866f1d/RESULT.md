# Complete dihedral homology characters of cycle matching complexes

## Finding
For every integer \(n\ge 3\), let \(X_n=\mathcal M(C_n)\) be the ordinary matching complex of a simple cycle with edges indexed by \(\mathbb Z/n\mathbb Z\). Its dihedral symmetry group \(D_n=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle\) acts by \(r(i)=i+1\) and \(s(i)=-i\) on the edge indices. Let \(d_n\) be the unique degree with nonzero reduced rational homology:
\[
d_n=\begin{cases}m-1,&n=3m,\\m-1,&n=3m+1,\\m,&n=3m+2.\end{cases}
\]
The \(D_n\)-character \(\chi_n\) on \(\widetilde H_{d_n}(X_n;\mathbb Q)\) is completely determined as follows. Define the integer sequence \(a_0=1\), \(a_1=0\), and \(a_j=a_{j-1}-a_{j-2}\) for \(j\ge2\), and define \(b_h=2\cos(\pi h/3)\) for integers \(h\ge1\). Then for all integers \(0\le k<n\):
\[
\boxed{\chi_n(r^k)=(-1)^{d_n+1}b_{\gcd(n,k)},\quad
\chi_n(r^ks)=(-1)^{d_n+1}a_{\ell(n,k)},}
\]
where
\[
\ell(n,k)=\begin{cases}
(n-1)/2,&n\text{ odd},\\
n/2+1,&n\text{ even and }k\text{ even},\\
n/2-2,&n\text{ even and }k\text{ odd}.
\end{cases}
\]
In particular, when \(3\mid n\), the two-dimensional rational homology representation is irreducible, with the rotation generator having eigenvalues of order three if \(n/3\) is odd and order six if \(n/3\) is even; every reflection has trace zero. When \(3\nmid n\), the representation is one-dimensional, with \(r\) acting by \((-1)^{n+1}\). The full \(D_n\)-fixed rational homology has dimension one exactly when \(n\equiv1,11\pmod{12}\), and is zero otherwise.

## Assumptions and scope
The graph \(C_n\) is the simple cycle on \(n\ge3\) vertices and edges. A matching is a subset of pairwise vertex-disjoint edges. Index its \(n\) edges consecutively by residues \(i\pmod n\): two indexed edges conflict precisely when their indices differ by \(1\pmod n\). Thus \(X_n\) is simplicially isomorphic to \(\operatorname{Ind}(C_n)\), the independence complex of the cycle on these edge indices. Group actions are simplicial; homology and traces are over \(\mathbb Q\). The earlier nonequivariant homotopy theorem is used, but no equivariant homotopy equivalence is assumed. The empty face is included in the augmented simplicial chain complex for reduced homology. The formula specifies the complete character, not a canonical integral module isomorphism or an equivariant homotopy type.

## Proof
**Homology concentration.** The established cycle matching-complex theorem, proved again in Donovan--Scoville, Proposition 26 (arXiv:2207.13780v1; journal version Proposition 5.4), gives
\[
X_{3m}\simeq S^{m-1}\vee S^{m-1},\qquad
X_{3m+1}\simeq S^{m-1},\qquad
X_{3m+2}\simeq S^m.
\]
Consequently all reduced rational homology is in degree \(d_n\), of dimension two or one as indicated. These homotopy equivalences need not preserve the group action; only the homology concentration is used below.

**Signed equivariant Lefschetz formula.** For any permutation \(g\) of the edge indices induced by a dihedral symmetry, the trace on the augmented simplicial chains is
\[
\widetilde L(g)=\sum_{S\in X_n,\,gS=S}(-1)^{|S|-1}\operatorname{sgn}(g|_S).
\]
For the empty face the term is \(-1\). A nonempty setwise-fixed face is a union of \(q\) distinct orbits of \(g\) on edge indices. Because the sign of the restricted permutation is \((-1)^{|S|-q}\), its contribution to the preceding sum is \((-1)^{q-1}\). Discard any orbit containing two adjacent indices; among the remaining orbits make a conflict graph \(B_g\), with an edge whenever an index in one orbit is adjacent to an index in the other. The admissible unions are precisely the independent sets of \(B_g\). Therefore
\[
\widetilde L(g)=-I(B_g,-1),\qquad
I(B,z)=\sum_{J\in\operatorname{Ind}(B)}z^{|J|}.
\]
The alternating trace identity and homology concentration imply
\[
(-1)^{d_n}\chi_n(g)=\widetilde L(g)=-I(B_g,-1).
\]
This identity does not rely on an equivariant choice of Morse matching.

**Rotation orbit graph.** For \(g=r^k\), set \(h=\gcd(n,k)\). Its index orbits are the residue classes modulo \(h\). For \(h=1\), the sole orbit contains adjacent indices, so \(B_g\) is empty and \(I(B_g,-1)=1=b_1\). For \(h=2\), the two admissible orbits conflict and \(B_g=K_2\), giving \(I(B_g,-1)=-1=b_2\). For \(h\ge3\), the graph of conflicting residue classes is \(C_h\), so \(I(B_g,-1)=I(C_h,-1)\). The independence-polynomial deletion recurrence, or the path recurrence below, yields \(I(C_h,-1)=2\cos(\pi h/3)=b_h\). This proves the rotation formula, including the identity case \(k=0\), where \(h=n\).

**Reflection orbit graph.** Write \(g=r^ks\), acting by \(i\mapsto k-i\). If \(n\) is odd, it fixes one index and exchanges the others in mirror pairs. Exactly one exchanged pair consists of adjacent indices and must be discarded. The remaining orbit classes, read from the fixed index toward this omitted end pair, form a path of \((n-1)/2\) vertices, with adjacency only between successive orbit classes. If \(n\) is even and \(k\) is even, the reflection fixes two opposite indices. The consecutive orbit classes from one fixed index to the other form a path of \(n/2+1\) vertices, none discarded. If \(n\) is even and \(k\) is odd, the reflection axis passes between two opposite pairs of neighboring indices; each such pair is internally conflicting and must be discarded. The remaining \(n/2-2\) orbit classes form a path (including the empty path when \(n=4\)). Thus in every case \(B_g=P_{\ell(n,k)}\).

Let \(a_t=I(P_t,-1)\), where \(P_0\) is the empty graph. Splitting independent sets according to whether the last vertex of the path is selected gives \(a_0=1\), \(a_1=0\), \(a_t=a_{t-1}-a_{t-2}\), and proves the reflection formula.

**Representation and invariants.** For \(n=3m\), the rotation generator has trace \((-1)^m\) on a two-dimensional space and every reflection has trace zero. The generator has determinant one: finite order implies determinant \(\pm1\), while determinant \(-1\) would force the real eigenvalues \(1\) and \(-1\), hence trace zero, contrary to the computed trace \(\pm1\). Its characteristic polynomial is \(t^2-(-1)^mt+1\). Its roots are primitive third roots when \(m\) is odd and primitive sixth roots when \(m\) is even. Both polynomials are irreducible over \(\mathbb Q\), proving irreducibility. For \(3\nmid n\) the homology has dimension one, and the rotation formula gives \(\chi_n(r)=(-1)^{n+1}\). If \(n\) is even this is negative, so there is no group-fixed vector. If \(n\) is odd and \(3\nmid n\), then \(r\) acts trivially and a fixed vector exists exactly when the reflection acts positively. The six-periodic path recurrence gives positive reflection trace exactly for \(n\equiv1,11\pmod{12}\) (among odd numbers not divisible by three). For \(3\mid n\), the rotation has no eigenvalue one. These cases give the asserted invariant dimension.

## Verification
The reproducibility program `dihedral_cycle_verify.py` independently enumerates all independent simplices and their signed fixed-face traces for every dihedral element for \(3\le n\le18\). It compares the resulting reduced Lefschetz sums with the closed formulas in all \(336\) cases. It separately computes all augmented mod-two boundary ranks for \(3\le n\le15\), verifying the expected homology concentration and Betti numbers in thirteen exact finite cases. Running `python3 dihedral_cycle_verify.py` prints `VERIFY_OK signed-traces= 336 GF2-homology= 13`. These finite calculations check conventions and arithmetic; the preceding orbit argument and cited homology theorem prove the formulas for every \(n\ge3\).

## Relationship to prior work
Donovan--Scoville, arXiv:2207.13780, Proposition 26 (journal Proposition 5.4), and earlier results of Kozlov establish the nonequivariant wedge-of-spheres homotopy types of the cycle matching complexes. Adamaszek, arXiv:1106.6250, proves broader nonequivariant independence-complex splitting results for powers of cycles. These results determine the homology degrees and dimensions, but the displayed nonequivariant equivalences alone do not fix the induced dihedral representation: they do not specify the signs of reflections or the eigenvalues of rotations. The present formulas use signed fixed-simplex traces to obtain the entire rational character. No new claim is made about the already-known wedge counts, the elementary character theory of dihedral groups, or higher graph powers.

## Limitations
The theorem classifies ordinary reduced rational homology representations, not integral \(\mathbb Z[D_n]\)-lattices, chain homotopy types, fixed-point subcomplexes, or Borel-equivariant cohomology. An equivalent equivariant computation could remain unindexed or occur in literature not recovered by the searches; the literature comparison is not a proof of priority. The code verifies only the specified finite parameter range and is not itself an infinite proof. The nonequivariant homotopy concentration is invoked from the cited primary theorem, not independently reconstructed for every size.

## References
1. C. Donovan and N. A. Scoville, *Star clusters in the Matching, Morse, and Generalized Morse complex*, arXiv:2207.13780v1, public 2022-07-27, Proposition 26, https://arxiv.org/abs/2207.13780.
2. C. Donovan and N. A. Scoville, *Star clusters in the matching, Morse, and generalized complex of discrete Morse functions*, New York Journal of Mathematics **29** (2023), 1393–1412, Proposition 5.4, https://nyjm.albany.edu/j/2023/29-54v.pdf.
3. M. Adamaszek, *Splittings of independence complexes and the powers of cycles*, Journal of Combinatorial Theory, Series A **119** (2012), 1196–1211; arXiv:1106.6250v4, https://arxiv.org/abs/1106.6250.
