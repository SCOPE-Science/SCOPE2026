# Two-term large-flattening Lyapunov law for planar-trapped ellipsoidal billiards

## Finding

For an open billiard outside at least three flattened ellipsoids, the transverse curvature controls not just separation of the two positive exponents but an explicit two-term asymptotic. For each fixed ergodic Gibbs measure \(\mu\) of the trapped itinerary shift, the top exponent *per billiard collision* satisfies
\[
\lambda_1(\beta)=2\log\beta+C_0(\mu)+\beta^{-2}C_1(\mu)+R_\beta(\mu),\qquad
|R_\beta(\mu)|\le \frac{3}{\beta^4 a_*^2d_*^2},
\]
for sufficiently large \(\beta\). The coefficients are explicit geometric averages:
\[
C_0(\mu)=\int\log(a(x)d(x))\,d\mu(x),\qquad
C_1(\mu)=\int\frac{a(x)^{-1}+a(B^{-1}x)^{-1}}{d(x)}\,d\mu(x).
\]
The estimate is uniform over the Gibbs measures under discussion; neither coefficient requires computing a separate unstable direction.

## Assumptions and scope

Fix \(k\ge3\) obstacles in \(\mathbb R^3\), with planar centres \((X_i,Y_i,0)\) and equations
\[
K_i(\beta)=\{(x,y,z):(x-X_i)^2+(y-Y_i)^2+\beta^2z^2\le r_i^2\},\qquad\beta>1.
\]
Assume the no-eclipse condition, radii small relative to centre separations, and the uniform positive angle of incidence from the cited open-billiard construction. Its trapped/nonwandering ball-map system \(B\) lies in the plane \(z=0\) and is symbolically conjugate to the fixed two-sided subshift of obstacle labels, independent of \(\beta\). Let \(\mu\) be any fixed ergodic Gibbs probability for that shift (identified with its planar trapped set). For a collision \(x\) at obstacle \(i\), let \(\nu(x)\) be the outward normal and \(v_{\mathrm{out}}(x)\) the outgoing unit ray; define \(a(x)=2\langle\nu(x),v_{\mathrm{out}}(x)\rangle/r_i\). Let \(d(x)=\|q(x)-q(B^{-1}x)\|\). Fix global bounds \(a(x)\ge a_*>0\), \(d(x)\ge d_*>0\). In the source's symbols one may take \(a_*=2c_1/r_0\) and \(d_*=d_0-2r_0\). All Lyapunov exponents here are per *billiard-ball-map iteration*, not per unit flow time. The dominant normal exponent is denoted \(\lambda_\perp\), the in-plane exponent \(\lambda_\parallel\).

## Proof

**1. Physical equatorial curvature.** Put \(F_i=(x-X_i)^2+(y-Y_i)^2+\beta^2z^2-r_i^2\). At any equatorial impact, \(\|\nabla F_i\|=2r_i\) and the normal is in the plane. For the transverse unit tangent \(e_z\), the derivative of the unit outward normal is
\[
D\nu_i(e_z)=\frac{\operatorname{Hess}F_i(e_z)}{\|\nabla F_i\|}=\frac{\beta^2}{r_i}e_z.
\]
The equatorial in-plane principal curvature remains \(1/r_i\). Consequently, the reflected normal-coordinate forcing in the standard open-billiard Poincaré matrix is \(Q a_i\), where \(Q=\beta^2\) and \(a_i=a(B^ix)\). The tangent/normal projections in this planar orbit fix \(e_z\), so there is no extra incidence factor beyond \(2\langle\nu_i,v_i\rangle\).

**2. Exact positive matrix recurrence.** Let \(d_i=d(B^ix)\). The transverse block of the linearized billiard map, using the Poincaré coordinates of the two cited primary works, is
\[
M_i(Q)=\begin{pmatrix}1&d_i\\Qa_i&1+Qa_i d_i\end{pmatrix}.
\]
For a vector starting with positive coordinates \(U_0=V_0=1\), write \((U_i,V_i)^\top=M_i(Q)\cdots M_1(Q)(1,1)^\top\). Then
\[
U_i=U_{i-1}+d_i V_{i-1},\qquad
V_i=V_{i-1}+Qa_iU_i.
\]
The positivity of every factor and the standard billiard unstable-bundle identification imply \(\lambda_\perp=\lim_{n\to\infty}n^{-1}\log V_n\) for \(\mu\)-almost every itinerary, as in the recurrence/corollary of the motivating paper; the initial positive vector affects the logarithm by a bounded additive quantity only.

**3. Uniform projective estimate.** Put \(h=Q^{-1}=\beta^{-2}\) and \(u_i=U_i/V_i\). Exact division gives
\[
u_i=\frac{u_{i-1}+d_i}{1+Qa_i(u_{i-1}+d_i)}.
\]
For every \(i\ge1\), \(0<u_i\le h/a_i\), and exact subtraction gives
\[
0\le \frac{h}{a_i}-u_i=\frac{h/a_i}{1+Qa_i(u_{i-1}+d_i)}
\le \frac{h^2}{a_*^2d_*}.
\]
For \(i\ge2\), the second recurrence yields
\[
\log\frac{V_i}{V_{i-1}}=\log Q+\log(a_i d_i)
+\log\left(1+\frac{u_{i-1}+h/a_i}{d_i}\right).
\]
Set \(z_i=(u_{i-1}+h/a_i)/d_i\); then \(0\le z_i\le 2h/(a_*d_*)\). Combining \(0\le z-\log(1+z)\le z^2/2\) with the preceding estimate gives the uniform **one-step** bound
\[
\left|\log\frac{V_i}{V_{i-1}}-\log Q-\log(a_i d_i)-
 h\frac{a_{i-1}^{-1}+a_i^{-1}}{d_i}\right|
\le\frac{3h^2}{a_*^2d_*^2}\quad (i\ge2).
\]
The first step contributes only a finite \(\beta\)-dependent additive transient, negligible after division by \(n\).

**4. Invariant-measure limit and branch selection.** Apply Birkhoff to the bounded continuous cylinder-coding observables \(\log(ad)\) and \((a^{-1}+a^{-1}\circ B^{-1})/d\). Summing the one-step bound and taking \(n\to\infty\) gives
\[
\left|\lambda_\perp-\log Q-C_0(\mu)-hC_1(\mu)\right|
\le\frac{3h^2}{a_*^2d_*^2}.
\]
The planar linearized block is independent of \(\beta\) and has a uniform bounded per-step norm, so \(\lambda_\parallel\le\log P\) for some finite \(P\) depending only on the fixed obstacle configuration. Positivity of the normal block also gives \(\lambda_\perp\ge\log(Q a_*d_*)\). Hence \(\lambda_\perp>\lambda_\parallel\) for all \(\beta\) sufficiently large (uniformly over \(\mu\)), proving \(\lambda_1=\lambda_\perp\) and the stated expansion.

## Verification

The proof uses exact differentiation of a quadratic defining function, exact positive matrix multiplication, an elementary algebraic projective bound, and Birkhoff's theorem. Every hypothesis needed for denominators is explicit: \(a_*>0\), \(d_*>0\), \(\beta>1\). The bound holds for all \(h>0\) in the transverse calculation; only identification with the **top** exponent requires a sufficiently large flattening parameter. The elementary scalar constant-case check sets \(a_i=a\), \(d_i=d\): the matrix has trace \(2+Qad\), determinant \(1\), and its expanding eigenvalue has logarithm \(\log(Qad)+2/(Qad)+O(Q^{-2})\), agreeing with \(C_1=2/(ad)\). This check illustrates but does not replace the general proof.

## Relationship to prior work

Al Dowais and Stoyanov, arXiv:2610.03004v1, introduce the flattened ellipsoidal family and prove separation of positive exponents via positive polynomial recurrences; they do not give these measure-dependent large-flattening coefficients. Their presentation writes the transverse curvature proportional to \(\beta/r_i\), while direct differentiation of the displayed ellipsoid equation gives \(\beta^2/r_i\). The asymptotic here uses the **stated physical ellipsoid geometry**, so its leading logarithmic slope is \(2\), not \(1\). The earlier spherical-obstacle paper arXiv:2306.03611 establishes the Poincaré matrix representation, and Al Dowais (2023), DOI 10.3390/math11224633, discusses differentiability under small obstacle deformations rather than the present singular large-flattening limit. No universality independent of the invariant measure is asserted for \(C_0\) or \(C_1\).

## Limitations

The theorem does not address finite \(\beta\) beyond eventual spectral domination; the exact threshold is not optimized. It applies to trapped *planar* orbits and fixed ergodic Gibbs measures, not to generic escaping rays, nonplanar trapped families, or exponents normalized per unit flow time. The \(O(\beta^{-4})\) remainder is an explicit bound but no claim of sharpness is made. A related general positive-matrix asymptotic could exist under another name; targeted searches did not uncover an implication-equivalent spectral expansion.

## References

1. A. Al Dowais and L. Stoyanov, *Some open billiards with distinct top Lyapunov exponents*, arXiv:2610.03004v1, first public 2026-10-02, https://arxiv.org/pdf/2610.03004v1 (especially geometry, §3, formulas (3.1)–(3.9)).
2. A. Al Dowais and L. Stoyanov, *Lyapunov exponents for open billiards in the exterior of balls*, arXiv:2306.03611, https://arxiv.org/pdf/2306.03611 (especially §3, billiard differential and Poincaré matrices).
3. A. Al Dowais, *Differentiability of the Largest Lyapunov Exponent for Non-Planar Open Billiards*, Mathematics 11 (2023), 4633, DOI:10.3390/math11224633 (small-deformation comparison).
