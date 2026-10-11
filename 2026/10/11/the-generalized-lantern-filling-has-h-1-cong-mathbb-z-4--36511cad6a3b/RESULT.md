# The generalized-lantern filling has \(H_1\cong\mathbb Z/4\)
## Finding
Let \(W_{\mathrm{GL}}\) be the Stein total space of the positive allowable Lefschetz fibration on \(\Sigma_{0,6}\) whose six vanishing cycles are the left-hand factors of Baykur's generalized lantern relation, with homology classes \(e_{23},e_{245},e_{135},e_{14},e_{12},e_{34}\) in Mori's winding-number basis. Then \(H_1(W_{\mathrm{GL}};\mathbb Z)\cong\mathbb Z/4\) and \(H_2(W_{\mathrm{GL}};\mathbb Z)\cong\mathbb Z\). Consequently \(H^2(W_{\mathrm{GL}};\mathbb Z)\cong\mathbb Z\oplus\mathbb Z/4\), and the nonzero order-two first Chern class identified by Mori is exactly the unique order-two element of the torsion summand: \(c_1(W_{\mathrm{GL}})=2\tau\) for either generator \(\tau\) of \(\operatorname{Tor}H^2(W_{\mathrm{GL}};\mathbb Z)\cong\mathbb Z/4\).

Equivalently, the torsion that makes the integral Calabi--Yau criterion fail in this example is not merely known to contain a class of order two: the complete torsion group in degree two is cyclic of order four, and \(c_1\) is its midpoint.

## Assumptions and scope
The page is the six-boundary-component planar surface \(\Sigma_{0,6}\). Baykur's generalized lantern relation has six positive left-hand factors. Mori records their homology classes, in a basis \(e_1,\ldots,e_5\) of \(H_1(\Sigma_{0,6};\mathbb Z)\), as
\[
e_{23},\quad e_{245},\quad e_{135},\quad e_{14},\quad e_{12},\quad e_{34}.
\]
Here \(e_J=\sum_{j\in J}e_j\). The total space \(W_{\mathrm{GL}}\) is the Stein PALF associated to this six-factor positive allowable factorization.

No claim is made about the diffeomorphism type, fundamental group, intersection form, or boundary three-manifold beyond what follows from this handle complex.

## Proof
The standard PALF handle decomposition has one zero-handle, five one-handles, and six two-handles. In the chosen basis, the boundary map \(C_2\to C_1\) is the vanishing-cycle matrix
\[
V=
\begin{pmatrix}
0&0&1&1&1&0\\
1&1&0&0&1&0\\
1&0&1&0&0&1\\
0&1&0&1&0&1\\
0&1&1&0&0&0
\end{pmatrix}.
\]
There are no handles of index greater than two, so
\[
H_2(W_{\mathrm{GL}};\mathbb Z)=\ker V,\qquad
H_1(W_{\mathrm{GL}};\mathbb Z)=\operatorname{coker}V.
\]

The determinantal divisors of \(V\), namely the greatest common divisors of all \(k\times k\) minors for \(1\le k\le5\), are
\[
\Delta_1=\Delta_2=\Delta_3=\Delta_4=1,\qquad \Delta_5=4.
\]
Hence the Smith invariant factors are
\[
1,\ 1,\ 1,\ 1,\ 4.
\]
In particular \(V\) has rank five,
\[
\operatorname{coker}V\cong\mathbb Z/4,
\]
and \(\ker V\) is free of rank one. One generator is
\[
(-1,0,0,-1,1,1),
\]
the negative of the generator recorded by Mori. This proves
\[
H_1(W_{\mathrm{GL}};\mathbb Z)\cong\mathbb Z/4,\qquad
H_2(W_{\mathrm{GL}};\mathbb Z)\cong\mathbb Z.
\]

The corresponding cochain differential is \(V^{\mathsf T}:\mathbb Z^5\to\mathbb Z^6\). Transposition has the same nonzero Smith invariant factors, so
\[
H^2(W_{\mathrm{GL}};\mathbb Z)
=\operatorname{coker}V^{\mathsf T}
\cong\mathbb Z\oplus\mathbb Z/4.
\]

Mori's Calabi--Yau criterion represents the first Chern class by the all-ones cochain \(\mathbf 1_6\) in this cokernel. For
\[
w=(1,1,1,1,0)^{\mathsf T}
\]
one has
\[
V^{\mathsf T}w=2\mathbf 1_6.
\]
Mori also proves that \(\mathbf 1_6\notin\operatorname{im}V^{\mathsf T}\), so \(c_1(W_{\mathrm{GL}})\) is nonzero of order two. Since the torsion subgroup of \(H^2\) is cyclic of order four, it has a unique element of order two. Therefore, for either generator \(\tau\) of that torsion subgroup,
\[
c_1(W_{\mathrm{GL}})=2\tau.
\]

## Verification
An exact integer checker recomputes every determinantal divisor directly from minors, checks the displayed kernel vector, and checks \(V^{\mathsf T}w=2\mathbf 1_6\). It returns

`VERIFY_OK rank=5 determinantal_divisors=1,1,1,1,4 kernel=(-1,0,0,-1,1,1) VTu=(2,2,2,2,2,2)`

The finite computation is a certificate for the explicit integer matrix, not a substitute for the handle-theoretic identification of the chain complex.

As cross-checks, the rank-five result gives \(b_1=0\) and \(b_2=1\). With five one-handles and six two-handles, the Euler characteristic is \(1-5+6=2\), consistent with Mori's general PALF formulas.

## Relationship to prior work
Baykur proves the generalized lantern relation on \(\Sigma_{0,6}\) and uses a different five-factor family to construct infinitely many Stein fillings. In that family, Baykur computes \(H_1\cong\mathbb Z\); the inspected paper does not compute the homology of the six-factor left-hand side of the generalized lantern relation.

Mori uses that six-factor relation as an integrality example. Mori identifies the six homology classes, proves that \(c_1\) is nonzero of order two, and records a generator of \(\ker V\). The inspected text does not state \(\operatorname{coker}V\cong\mathbb Z/4\), the full decomposition of \(H^2\), or the identification of \(c_1\) as twice a generator of cyclic four-torsion.

A nearby published result gives a zero--one length-defect law for competing planar Calabi--Yau factorizations. That statement concerns factorization length and Betti-number excess, not the integral homology or exact torsion structure of this generalized-lantern filling.

## Limitations
The result is specific to the six-factor positive allowable Lefschetz fibration supplied by the generalized lantern relation. It does not classify all Stein fillings of its boundary contact manifold.

The Smith calculation determines the abelian homology groups but not the fundamental group or intersection pairing. The order-two statement for \(c_1\) uses Mori's obstruction calculation; the new computation identifies the ambient torsion group containing that class.

No claim is made that cyclic four-torsion is invariant under replacing this factorization by another positive factorization of the same monodromy.

## References
1. A. Mori, *Planar Contact Structures with Calabi-Yau Fillings and Topological Quantum Computation*, arXiv:2609.30406v1, first posted 2026-09-24; current inspected version v2, 2026-10-01.
2. R. İ. Baykur, *Planar contact 3-manifolds with infinitely many Stein fillings*, arXiv:2607.21303v1, first posted 2026-07-23.
