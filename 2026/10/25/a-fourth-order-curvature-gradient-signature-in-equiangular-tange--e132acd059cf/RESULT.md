# A fourth-order curvature-gradient signature in equiangular tangent-polygon approximation

## Finding
Let \(K\subset\mathbb R^2\) be a strictly convex body whose \(2\pi\)-periodic support function \(h\) is \(C^8\) and satisfies \(\rho(\theta):=h(\theta)+h''(\theta)>0\). For every integer \(n\ge3\), set \(\delta=2\pi/n\); choose \(U\) uniformly on \([0,\delta)\); and form the circumscribed \(n\)-gon \(P_{n,U}\) from the supporting lines at normal angles \(U+j\delta\), \(0\le j<n\).

The expected excess area has the two-term expansion
\[
\mathbb E_U\bigl[|P_{n,U}|-|K|\bigr]
=\frac{\delta^2}{24}\int_0^{2\pi}\rho(\theta)^2\,d\theta
+\frac{\delta^4}{720}\int_0^{2\pi}\bigl(3\rho(\theta)^2-\rho'(\theta)^2\bigr)\,d\theta
+O_K(\delta^6).
\]
Its **fourth-order coefficient need not be positive**: the negative curvature-gradient energy can dominate. In particular, the smooth strictly convex family with radius of curvature
\[
\rho_m(\theta)=1+\tfrac12\cos(m\theta),\qquad m\in\{2,3,\ldots\},
\]
has the same perimeter and the same distribution of \(\rho_m\) with respect to uniform normal angle for every \(m\), but its fourth-order coefficient is
\[
B_4(m)=\frac{\pi}{720}\left(6+\tfrac14(3-m^2)\right),
\]
which is positive for \(2\le m\le5\) and negative for \(m\ge6\). Thus the next-order approximation error distinguishes the **angular arrangement** of curvature even when the curvature-radius histogram and leading error are identical.

The result includes an exact, nonasymptotic Fourier identity. Write
\[
h(\theta)=a_0+\sum_{k\ge1}\bigl(a_k\cos(k\theta)+b_k\sin(k\theta)\bigr).
\]
Then for every \(n\ge3\),
\[
\mathbb E_U|P_{n,U}|=
 n a_0^2\tan(\delta/2)
 +\frac{n}{2\sin\delta}\sum_{k\ge1}(a_k^2+b_k^2)
 \bigl(\cos(k\delta)-\cos\delta\bigr).
\]

## Assumptions and scope
The ambient metric is Euclidean. The support function is evaluated against \(u(\theta)=(\cos\theta,\sin\theta)\); \(|\cdot|\) denotes planar area, not perimeter. The condition \(\rho>0\) makes \(K\) an oval with a unique tangent for each outward normal. Each \(P_{n,U}\) is the intersection of the \(n\) supporting halfplanes at the prescribed equally spaced normal angles and contains \(K\). The random phase is **uniform on one normal-angle spacing**, rather than sampling independent random normals. The remainder depends on \(K\), and the limit is taken with \(K\) fixed as \(n\to\infty\).

No optimality of these particular polygons among all circumscribed \(n\)-gons is asserted. The fourth-order sign concerns a coefficient in the expansion, **not** the sign of the total excess area, which is always nonnegative.

## Proof
**1. Exact area of the supporting polygon.** Put \(h_j=h(U+j\delta)\), with cyclic indices. Along the line \(x\cdot u(U+j\delta)=h_j\), the intersections with its adjacent supporting lines have tangential coordinates
\[
\frac{h_{j+1}-h_j\cos\delta}{\sin\delta},\qquad
\frac{h_j\cos\delta-h_{j-1}}{\sin\delta}.
\]
Since \(h+h''>0\), the corresponding supporting lines are all genuine sides. Their lengths are \((h_{j-1}+h_{j+1}-2h_j\cos\delta)/\sin\delta\). The planar divergence theorem, or the support-length formula for polygonal area, gives
\[
|P_{n,U}|=\frac1{\sin\delta}\left(
\sum_{j=0}^{n-1}h_jh_{j+1}-\cos\delta\sum_{j=0}^{n-1}h_j^2\right).
\]
These equations remain valid under translation of the origin: the signed support lengths are used consistently in the area formula.

**2. Remove orientation aliasing exactly.** If \(g\) is \(2\pi\)-periodic and integrable, uniform \(U\) on \([0,\delta)\) satisfies \(\mathbb E\sum_jg(U+j\delta)=\delta^{-1}\int_0^{2\pi}g(\theta)\,d\theta\). Therefore
\[
\mathbb E_U|P_{n,U}|=
\frac1{\delta\sin\delta}\int_0^{2\pi}
 h(\theta)\bigl[h(\theta+\delta)-h(\theta)\cos\delta\bigr]d\theta.
\tag{1}
\]
Orthogonality of trigonometric functions in (1) proves the displayed exact Fourier identity, including the vanishing first-frequency term, for every \(n\ge3\). No bandlimit or assumption that \(n\) avoid resonant Fourier frequencies is necessary.

**3. Fourth-order expansion.** Set \(H_j=\int_0^{2\pi}(h^{(j)}(\theta))^2\,d\theta\), \(j=0,1,2,3\), and \(Q(t)=\int_0^{2\pi}h(\theta)h(\theta+t)\,d\theta\). Periodicity makes \(Q\) even. Repeated integration by parts yields
\[
Q(t)=H_0-\frac{t^2}{2}H_1+\frac{t^4}{24}H_2-\frac{t^6}{720}H_3+O_K(t^8).
\]
The \(C^8\) hypothesis bounds the eighth derivative and controls the remainder. Insert this expansion and the Taylor series of \(\cos t\) and \((t\sin t)^{-1}\) into (1). Using the classical support-function area formula \(|K|=(H_0-H_1)/2\), obtain
\[
\mathbb E_U|P_{n,U}|-|K|
=\frac{\delta^2}{24}(H_0-2H_1+H_2)
 +\frac{\delta^4}{720}(3H_0-7H_1+5H_2-H_3)
 +O_K(\delta^6).
\]
Finally, integration by parts shows \(\int\rho^2=H_0-2H_1+H_2\) and \(\int(\rho')^2=H_1-2H_2+H_3\). This proves the general formula with the advertised derivative energy.

**4. Strictly convex sign-changing examples.** The function
\[
h_m(\theta)=1+\frac{\cos(m\theta)}{2(1-m^2)}
\]
satisfies \(h_m+h_m''=1+\frac12\cos(m\theta)\in[1/2,3/2]\), so it defines a smooth strictly convex oval. Its perimeter is \(\int\rho_m=2\pi\). For every bounded measurable \(F\), substitution over the \(m\) complete periods gives \(\int_0^{2\pi}F(\rho_m(\theta))d\theta=\int_0^{2\pi}F(1+\frac12\cos\theta)d\theta\). Thus all members have the same normal-angle curvature-radius histogram. Direct integration gives \(\int\rho_m^2=\pi(2+1/4)\) and \(\int(\rho_m')^2=\pi m^2/4\). Hence the coefficient \(B_4(m)\) above, with its exact sign threshold. The area of the approximating polygon is in fact independent of the phase for this family whenever \(n>2m\), by the finite Fourier orthogonality in Step 2. This also establishes the displayed signs for a deterministic polygon sequence with sufficiently many sides.

## Verification
The independent coordinate construction in `equiangular_tangent_area_check.py` computes intersections of consecutive support lines and uses the shoelace formula. It is compared against the support-length identity, the full-phase averaged Fourier formula in a deliberately aliasing \(n=8\) case, and high-precision sixth-order residuals in the single-frequency family. Executing `python equiangular_tangent_area_check.py` (Python 3 with `mpmath`) prints `ALL_EQUANGULAR_TANGENT_AREA_CHECKS_OK`. The computer checks are finite corroboration; the analytical identities and estimates in the proof establish the theorem.

## Relationship to prior work
Polygonal approximation and second-order error rates are classical. McClure and Vitale (1975) and Ludwig (1994) investigate **best** polygonal approximations; Ludwig determines a fourth-order correction for best circumscribed polygons in terms of affine curvature. Those optimization statements do not imply a fourth-order coefficient for the prescribed **equispaced normal fan**, its exact uniform-phase Fourier diagonalization, or the contrasting coefficient signs among curves with identical normal-angle curvature-radius distributions. The 2025 study of equiangular circumscribed polygon families by Safarewicz and Zwierzyński focuses on centroid loci and isoperimetric inequalities, not the fixed-normal area defect. Bazarov and Tomskova (2026) analyze a different, **inscribed chordal**, fixed-parameter area approximation to leading order. These are comparisons of claims and constructions, not assertions that title differences alone establish priority.

## Limitations
The smooth strictly convex hypothesis excludes polygons and flat boundary arcs. The asymptotic remainder is for a **fixed** body, not for families whose Fourier frequency grows with \(n\). The counterexample signs apply to the fourth-order coefficient, not to every finite-size residual; and the exact distribution of \(|P_{n,U}|\), beyond its mean, is not determined. Historical priority requires further bibliographic verification, especially older approximation sources unavailable in full text; no independent mathematical audit has been performed.

## References
1. D. E. McClure and R. A. Vitale, *Polygonal approximation of plane convex bodies*, Journal of Mathematical Analysis and Applications **51** (1975), 326–358. DOI: 10.1016/0022-247X(75)90125-0. Historical comparison based on accessible bibliographic and secondary descriptions; original full text not inspected.
2. M. Ludwig, *Asymptotic approximation of convex curves*, Archiv der Mathematik **63** (1994), 377–384. DOI: 10.1007/BF01189576. Original mathematical text inspected, in particular the best-circumscribed Theorem 2. Author-posted full text: https://www.researchgate.net/publication/226972184_Asymptotic_approximation_of_convex_curves .
3. M. F. Safarewicz and M. Zwierzyński, *The k-th Order Preserving Sets and Isoperimetric Type Inequalities for Planar Ovals*, arXiv:2505.08017 (2025; revised 2026). https://arxiv.org/pdf/2505.08017 . Primary paper inspected, especially its setup of equiangular circumscribed polygons and its main results on associated sets.
4. S. Bazarov and A. Tomskova, *Second-Order Polygonal Discretization of the Area Functional and Explicit Error Asymptotics*, Journal of Numerical Analysis and Approximation Theory (online 31 July 2026). https://www.ictp.acad.ro/jnaat/journal/article/view/1710/1631 . Article and proof scope inspected.
