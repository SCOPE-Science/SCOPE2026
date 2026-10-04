# Commuting conjugacy class graphs of finite Heisenberg groups are symplectic clique blow-ups

## Finding

Let \(q\) be a prime power and \(n\ge2\). Define
\[
H_n(q)=\mathbf F_q^n\times\mathbf F_q^n\times\mathbf F_q
\]
by
\[
(x,y,z)(x',y',z')=(x+x',y+y',z+z'+x\cdot y').
\]
On
\[
V=\mathbf F_q^{2n}
\]
use the alternating form
\[
B((x,y),(x',y'))=x\cdot y'-x'\cdot y.
\]

Let \(\mathcal C(H_n(q))\) be the commuting conjugacy class graph: its vertices are the noncentral conjugacy classes, and two distinct classes are adjacent when they contain commuting representatives. With the Tang--Wan convention that \(\operatorname{Sp}(2n,q)\) has projective one-spaces as vertices and joins two of them when their symplectic product is nonzero,
\[
\boxed{\mathcal C(H_n(q))\cong\overline{\operatorname{Sp}(2n,q)}[K_{q-1}].}
\]

Therefore
\[
|V(\mathcal C(H_n(q)))|=q^{2n}-1,\qquad
\deg=q^{2n-1}-2,
\]
\[
\operatorname{diam}=2,\qquad
\omega=q^n-1.
\]

The adjacency spectrum is
\[
\boxed{
\begin{array}{c|c}
q^{2n-1}-2&1\\
(q-1)q^{n-1}-1&
\dfrac{(q+q^n)(q^n-1)}{2(q-1)}\\[2mm]
-(q-1)q^{n-1}-1&
\dfrac{(q^n-q)(q^n+1)}{2(q-1)}\\[2mm]
-1&
\dfrac{(q^{2n}-1)(q-2)}{q-1}
\end{array}}
\]
so the graph is adjacency-integral; regularity also makes its Laplacian and signless-Laplacian spectra integral.

For \(q=2\) it is strongly regular with parameters
\[
\boxed{(2^{2n}-1,\ 2^{2n-1}-2,\ 2^{2n-2}-3,\ 2^{2n-2}-1).}
\]
For every \(q>2\) it is not strongly regular. Two adjacent vertices on one projective line have
\[
q^{2n-1}-3
\]
common neighbors, while adjacent vertices on distinct orthogonal projective lines have
\[
q^{2n-2}-3.
\]

At the boundary \(n=1\),
\[
\mathcal C(H_1(q))\cong(q+1)K_{q-1}.
\]
For \(q=p\) prime, this agrees with the known center-index-\(p^2\) formula.

## Assumptions and scope

The graph uses noncentral conjugacy classes, not individual group elements. The convention for \(\operatorname{Sp}(2n,q)\) matters: Tang and Wan join projective points having nonzero symplectic product, so the orthogonality graph is its complement.

The theorem is stated for \(n\ge2\). The case \(n=1\) is only a boundary comparison and is not part of the originality claim in the prime-field case.

## Proof

For
\[
g=(x,y,z),\qquad h=(x',y',z'),
\]
direct multiplication gives
\[
[g,h]=(0,0,B((x,y),(x',y'))).
\]
Hence
\[
Z(H_n(q))=\{(0,0,z):z\in\mathbf F_q\}.
\]

Write \(v=(x,y)\). For \(v\ne0\), conjugation changes only the last coordinate, and the possible changes are the values of
\[
u\longmapsto B(u,v).
\]
This is a nonzero linear functional and is therefore surjective. Thus every noncentral conjugacy class is
\[
C_v=\{(v,z):z\in\mathbf F_q\}
\]
for a unique nonzero \(v\in V\). Moreover,
\[
C_v\sim C_w\quad\Longleftrightarrow\quad B(v,w)=0.
\]

Partition \(V\setminus\{0\}\) into one-dimensional subspaces. Each projective point contributes \(q-1\) nonzero vectors, all pairwise orthogonal, so it contributes \(K_{q-1}\). For two different projective points either every cross-pair is orthogonal or no cross-pair is. By the Tang--Wan convention, the former is exactly nonadjacency in \(\operatorname{Sp}(2n,q)\). This proves
\[
\mathcal C(H_n(q))\cong\overline{\operatorname{Sp}(2n,q)}[K_{q-1}].
\]

For a fixed nonzero \(v\), \(v^\perp\) has \(q^{2n-1}\) vectors. Removing \(0\) and \(v\) gives degree
\[
q^{2n-1}-2.
\]
If \(B(v,w)\ne0\), then
\[
v^\perp\cap w^\perp
\]
has dimension \(2n-2\), so for \(n\ge2\) it contains a nonzero common neighbor. Thus the diameter is \(2\).

Any clique spans a totally isotropic subspace, whose dimension is at most \(n\), so it has at most \(q^n-1\) vertices. A Lagrangian \(n\)-subspace attains this bound.

Tang and Wan give the projective graph \(\operatorname{Sp}(2n,q)\) degree
\[
q^{2n-1}
\]
and nontrivial eigenvalues
\[
q^{n-1},\qquad -q^{n-1}.
\]
Writing
\[
N=\frac{q^{2n}-1}{q-1},
\]
the complement has degree \(N-1-q^{2n-1}\), eigenvalues
\[
q^{n-1}-1,\qquad -q^{n-1}-1,
\]
and multiplicities
\[
\frac{(q+q^n)(q^n-1)}{2(q-1)},\qquad
\frac{(q^n-q)(q^n+1)}{2(q-1)}.
\]
For a graph eigenvalue \(\theta\), the lexicographic blow-up by \(K_{q-1}\) gives
\[
(q-1)\theta+q-2,
\]
and contributes \(-1\) with multiplicity \(N(q-2)\). Substitution yields the displayed spectrum.

If \(q>2\), distinct scalar multiples \(v,w\) satisfy \(v^\perp=w^\perp\), so they have \(q^{2n-1}-3\) common neighbors. Independent orthogonal \(v,w\) have a common orthogonal space of dimension \(2n-2\), and therefore \(q^{2n-2}-3\) common neighbors after deleting \(0,v,w\). These counts differ. If \(q=2\), the scalar-multiple type is absent; every adjacent pair has \(2^{2n-2}-3\) common neighbors and every nonadjacent pair has \(2^{2n-2}-1\), proving the stated strongly regular parameters.

When \(n=1\), the orthogonal complement of a projective point is the point itself. Hence distinct projective points contribute no cross-edges and
\[
\mathcal C(H_1(q))\cong(q+1)K_{q-1}.
\]

## Verification

The included replay directly constructs the group for
\[
(n,q)=(1,4),(2,2),(2,3),(2,4),(3,2).
\]
It verifies the center, every predicted conjugacy orbit, every commuting-class adjacency, the projective clique blocks, the degree and diameter formulas, a Lagrangian clique of size \(q^n-1\), the common-neighbor formulas, and the spectral multiplicities and first two spectral moments.

The \(\mathbf F_4\) arithmetic uses
\[
\mathbf F_4=\mathbf F_2[t]/(t^2+t+1).
\]
The replay returns `VERIFY_OK`.

Finite enumeration is not used to prove the theorem.

## Relationship to prior work

Bhowal's 2021 paper studies spectra and energies of commuting conjugacy class graphs. It proves that a nonabelian \(p\)-group of order \(p^N\) with center of order \(p^{N-2}\) has commuting conjugacy class graph
\[
(p+1)K_{p^{N-3}(p-1)}.
\]
For \(H_1(p)\) this gives the prime-field boundary above. For \(n\ge2\), however,
\[
|H_n(q)/Z(H_n(q))|=q^{2n},
\]
so that center-index-\(p^2\) theorem does not apply.

Earlier work of Bhowal and Nath treats the same graph for several explicit finite-group families, including dihedral and quaternion-type groups, but the inspected scope does not include higher-dimensional Heisenberg groups.

Tang and Wan determine the projective symplectic graph and its spectrum. Their vertices are projective points. The new group-theoretic step here identifies each noncentral Heisenberg conjugacy class with a nonzero symplectic vector, so every projective point expands to a \(q-1\) clique. That distinction produces the displayed Heisenberg graph, its multiplicities, its clique number, and the \(q=2\) versus \(q>2\) strong-regularity transition.

Targeted searches using commuting-conjugacy-class, Heisenberg, unitriangular, extraspecial, symplectic, lexicographic-product, and spectrum terminology did not locate this higher-rank Heisenberg statement.

## Limitations

The theorem concerns the standard finite Heisenberg group with one-dimensional center. More general class-two groups can have vector-valued commutator maps.

The projective symplectic graph spectrum is prior finite-geometry work and is not claimed as new. The originality claim is the exact Heisenberg conjugacy-class realization as its complementary clique blow-up and the stated group-graph consequences.

The \(n=1\), \(q=p\) prime boundary is already covered by the center-index-\(p^2\) theorem.

An equivalent result may exist under class-two, extraspecial, or commuting-class terminology not captured by the searches.

## References

1. P. Bhowal, “Spectrum and energies of a graph,” *Journal of Mathematics and Computer Science* 11 (2021), no. 2, 1355–1363, published 5 February 2021, DOI 10.28919/jmcs/5370.
2. P. Bhowal and R. K. Nath, “Spectral aspects of commuting conjugacy class graph of finite groups,” arXiv:2003.05762v1, first public version 12 March 2020.
3. Z. Tang and Z.-X. Wan, “Symplectic graphs and their automorphisms,” finite-geometry treatment of the projective symplectic graph and its spectrum.
