# Integral homology of the five-point parabolic very-stable surface
## Finding
Let \(X\subset\mathbf P^4\) be the smooth intersection of two quadrics in the \(n=2\) case of Bhattacharya--Matsubara, let \(W\subset X\) be the wobbly locus, and put
\[
Y=X\setminus W.
\]
Then \(X\) is a degree-\(4\) del Pezzo surface and \(W\) is the union of its sixteen \((-1)\)-curves. The complete integral homology of the very-stable locus is
\[
H_k(Y,\mathbf Z)\cong
\begin{cases}
\mathbf Z,&k=0,\\
\mathbf Z^{10},&k=1,\\
\mathbf Z^{25},&k=2,\\
0,&k\ge3.
\end{cases}
\]
Consequently
\[
\chi(Y)=16
\]
and its integral Poincare polynomial is
\[
P_Y(t)=1+10t+25t^2.
\]

Bhattacharya--Matsubara compute
\[
H_2(\pi_1(Y),\mathbf Z)\cong\mathbf Z^{25}.
\]
For this actual complement, the Hopf map
\[
H_2(Y,\mathbf Z)\longrightarrow H_2(\pi_1(Y),\mathbf Z)
\]
is an isomorphism. Hence the Hurewicz image of \(\pi_2(Y)\) in \(H_2(Y,\mathbf Z)\) is zero. This does not assert that \(\pi_2(Y)\) itself vanishes.

## Assumptions and scope
The ground field is \(\mathbf C\), and homology is singular homology of the classical analytic space. The result is specific to the surface case \(n=2\). It concerns ordinary homology, not intersection homology or compactly supported cohomology.

A degree-\(4\) del Pezzo surface is the blow-up of \(\mathbf P^2\) at five points in general position. In the standard basis \(H,E_1,\ldots,E_5\) of its Picard group, the sixteen \((-1)\)-curves are
\[
E_i,\qquad H-E_i-E_j\quad(i<j),\qquad 2H-E_1-\cdots-E_5.
\]

## Proof
The initiating paper gives two inputs in the surface case: \(W\) is the union of all sixteen \((-1)\)-curves, and
\[
H_1(Y,\mathbf Z)\cong\mathbf Z^{10}.
\]
It also realizes \(Y\) as the inverse image of the complement of the discriminant under the finite squaring map. For \(n=2\), the discriminant in \(\operatorname{Sym}^2(\mathbf P^1)\cong\mathbf P^2\) is a conic. Its complement is affine, and a finite inverse image of an affine variety is affine. Thus \(Y\) is a smooth affine complex surface.

We first compute its Euler characteristic. In the basis above, the intersection form is
\[
H^2=1,\qquad E_i^2=-1,\qquad H\cdot E_i=0,\qquad E_i\cdot E_j=0\quad(i\ne j).
\]
A direct calculation with the sixteen displayed classes shows that every \((-1)\)-curve meets exactly five of the other fifteen, each such intersection has multiplicity one, and the resulting incidence graph has no triangles. Therefore there are exactly
\[
\frac{16\cdot5}{2}=40
\]
distinct pairwise intersection points and no triple intersection points.

Each component of \(W\) is a copy of \(\mathbf P^1\), so inclusion--exclusion gives
\[
\chi(W)=16\chi(\mathbf P^1)-40=32-40=-8.
\]
The surface \(X\) is the blow-up of \(\mathbf P^2\) at five points, hence
\[
\chi(X)=3+5=8.
\]
By additivity,
\[
\chi(Y)=\chi(X)-\chi(W)=8-(-8)=16.
\]

A smooth affine complex surface has the homotopy type of a finite CW complex of real dimension at most \(2\) by the Andreotti--Frankel--Hamm theorem. Consequently
\[
H_k(Y,\mathbf Z)=0\qquad(k\ge3),
\]
and \(H_2(Y,\mathbf Z)\) is free abelian because it is the kernel of the cellular boundary from the top-dimensional free cellular chain group. Since \(Y\) is connected and \(H_1(Y,\mathbf Z)\cong\mathbf Z^{10}\), the Euler characteristic identity becomes
\[
16=1-10+\operatorname{rank}H_2(Y,\mathbf Z).
\]
Thus
\[
H_2(Y,\mathbf Z)\cong\mathbf Z^{25}.
\]

Finally, Hopf's exact sequence gives a surjection
\[
H_2(Y,\mathbf Z)\twoheadrightarrow H_2(\pi_1(Y),\mathbf Z).
\]
The source and target are both free abelian of rank \(25\), the latter by Bhattacharya--Matsubara. A surjection between free abelian groups of the same finite rank is an isomorphism. Exactness then says that the image of \(\pi_2(Y)\to H_2(Y,\mathbf Z)\) is zero.

## Verification
The accompanying `verify.py` reconstructs the sixteen divisor classes in the blow-up basis and computes all pairwise intersections exactly. It verifies that the incidence graph is \(5\)-regular, has \(40\) edges and no triangles. It then checks
\[
\chi(W)=-8,\qquad \chi(X)=8,\qquad \chi(Y)=16,
\]
and the Betti-number identity giving \(b_2(Y)=25\).

The script is a finite check of the incidence and arithmetic only. It does not replace the geometric inputs that \(W\) is the sixteen-curve wobbly locus, that \(H_1(Y,\mathbf Z)\cong\mathbf Z^{10}\), or the Andreotti--Frankel--Hamm theorem for smooth affine surfaces. The saved replay output ends in `VERIFY_OK`.

## Relationship to prior work
Bhattacharya--Matsubara compute \(H_1(Y,\mathbf Z)\cong\mathbf Z^{10}\) and, separately, the group homology
\[
H_2(\pi_1(Y),\mathbf Z)\cong\mathbf Z^{25}.
\]
Their proof of the latter uses a minimal presentation and Hopf's formula for group homology; it does not identify this group with the ordinary second homology of the geometric complement. The ordinary homology computation above requires the del Pezzo incidence arrangement, Euler additivity, and the affine CW-dimension bound.

Donagi--Pantev had previously identified the surface wobbly divisor with the sixteen \((-1)\)-curves. Standard degree-\(4\) del Pezzo geometry gives the blow-up description and the sixteen divisor classes used in the incidence calculation.

Targeted searches for the ordinary homology group \(H_2(Y,\mathbf Z)\), the Poincare polynomial \(1+10t+25t^2\), the Euler characteristic \(16\), and the Hopf-map isomorphism for this very-stable locus did not locate a covering statement.

## Limitations
The result does not prove that \(Y\) is aspherical and does not determine \(\pi_2(Y)\). The vanishing conclusion concerns only the Hurewicz image of \(\pi_2(Y)\) in ordinary second homology.

The argument is specific to \(n=2\). For higher-dimensional intersections of two quadrics, the wobbly divisor has different geometry and this sixteen-curve incidence calculation does not apply.

The ordinary homology ranks are forced by established geometric inputs plus standard topology once the incidence calculation is made. An older unindexed computation of the same complement remains a residual originality risk.

## References
1. S. Bhattacharya and Y. Matsubara, *Fundamental groups of complements of wobbly divisors in intersections of two quadrics*, arXiv:2609.31421v1, 2026.
2. R. Donagi and T. Pantev, *Parabolic Hecke eigensheaves*, Asterisque 435 (2022).
3. A. Andreotti and T. Frankel, *The Lefschetz theorem on hyperplane sections*, Annals of Mathematics 69 (1959), 713--717.
