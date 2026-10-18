# Sharp stability and optimal quartic SOS certificates in a phase-locked cubic flow

## Finding

For real \(a\), \(\gamma>0\), and \(0\le\omega\le\gamma\), consider the fourfold-equivariant homogeneous planar polynomial equation
\[
\dot z=(-a+i\omega)|z|^2z+\gamma\overline z^{\,3},\qquad z=x+iy.
\]
The origin is globally asymptotically stable **if and only if**
\[
a>\sqrt{\gamma^2-\omega^2}.
\]
Whenever this holds, a strictly decreasing quartic polynomial exists for which **both** the Lyapunov function and its negative Lie derivative have explicit positive-definite sum-of-squares (SOS) Gram representations. Furthermore, among all globally positive-definite strict polynomial Lyapunov functions, the smallest total degree is exactly \(4\) when \(\sqrt{\gamma^2-\omega^2}<a\le\gamma\), and exactly \(2\) when \(a>\gamma\). The quartic certificate also yields an explicit algebraic relaxation bound.

## Assumptions and scope

Write \(r=|z|\), \(z=re^{i\theta}\) for \(r>0\). We use the ordinary physical time and define global asymptotic stability to mean forward completeness, Lyapunov stability and convergence of every trajectory to the origin. A **strict polynomial Lyapunov function** is a real polynomial \(V(x,y)\) with \(V(0)=0\), \(V(z)>0\) for every \(z\ne0\), and \(\nabla V(z)\cdot F(z)<0\) for every \(z\ne0\). Thus a merely nonincreasing quadratic functional is not counted as strict. At \(\omega=\gamma\), the angular dynamics has degenerate stationary directions, but the strict quartic theorem still applies for every \(a>0\). The case \(\gamma<\omega\), in which angles rotate instead of locking, is explicitly outside the asserted novelty domain.

## Proof

**1. Sharp necessity.** For \(r>0\), direct separation of real and imaginary parts gives
\[
\dot r=r^3(-a+\gamma\cos4\theta),\qquad
\dot\theta=r^2(\omega-\gamma\sin4\theta).
\]
Since \(0\le\omega\le\gamma\), there is a constant direction \(\theta_+\) satisfying
\[
\sin4\theta_+=\omega/\gamma,\qquad
\cos4\theta_+=\sqrt{1-\omega^2/\gamma^2}.
\]
The ray \(z=re^{i\theta_+}\), \(r>0\), is invariant and obeys
\[
\dot r=(\sqrt{\gamma^2-\omega^2}-a)r^3.
\]
At equality the entire positive ray consists of nonzero equilibria. Below equality, positive-radius solutions on this ray do not approach the origin (indeed they escape in finite forward time for a positive coefficient). Therefore global asymptotic stability forces \(a>\sqrt{\gamma^2-\omega^2}\), which in the given parameter range implies \(a>0\) and \(D:=a^2+\omega^2>\gamma^2\).

**2. A strict quartic on the entire stable region.** Put
\[
A=x^2-y^2,\quad B=2xy,\quad t=-\frac{\gamma\omega}{D},\quad
V=(x^2+y^2)^2+2tAB.
\]
The identities \(A^2+B^2=(x^2+y^2)^2\) and \(2AB=\operatorname{Im}(z^4)\) give
\[
V=\frac{1+t}{2}(A+B)^2+\frac{1-t}{2}(A-B)^2.
\]
Since \(D>\gamma^2\) and \(a>0\), one has \(|t|<1\). This is a positive-definite SOS of quadratic forms. A direct Lie-derivative calculation yields the exact polynomial identity
\[
-\dot V=4(x^2+y^2)\begin{pmatrix}A&B\end{pmatrix}
M\begin{pmatrix}A\\B\end{pmatrix},\qquad
M=\begin{pmatrix}a-(\gamma+t\omega)&at\\at&a+(\gamma+t\omega)\end{pmatrix}.
\]
The two eigenvalues of \(M\) are
\[
\lambda_\pm=a\left(1\pm\frac{\gamma}{\sqrt D}\right),
\]
which are strictly positive. A real Cholesky factorization \(M=L^{\mathsf T}L\) writes \(-\dot V\) explicitly as a sum of squares of the homogeneous cubic polynomials \(2x(L_{j1}A+L_{j2}B)\) and \(2y(L_{j1}A+L_{j2}B)\), with \(j=1,2\). Both \(V\) and \(-\dot V\) are positive definite away from the origin. Properness and strict decay imply forward completeness and global asymptotic stability.

For a quantitative consequence, let \(c=4a(1-\gamma/\sqrt D)/(1+|t|)^{3/2}>0\). The Gram bound implies
\[
\dot V\le -cV^{3/2},\qquad
V(t_0+s)\le\left(V(t_0)^{-1/2}+\tfrac12cs\right)^{-2}
\]
for \(V(t_0)>0\), \(s\ge0\). In particular, the radius has a uniform algebraic upper bound and satisfies \(r(t)=O(t^{-1/2})\) for every nonzero initial state. This is an upper decay-rate bound, not a universal asymptotic equivalence.

**3. Optimal degree.** If \(a>\gamma\), the quadratic \(W=x^2+y^2\) is a strict Lyapunov function because
\[
\dot W=2r^4(-a+\gamma\cos4\theta)<0\quad(r>0).
\]
Conversely, suppose a positive-definite strict quadratic polynomial exists. Its constant is zero, and positive definiteness at the origin forces the linear part to vanish. Average its homogeneous quadratic form over the four quarter-turns \(z\mapsto i^kz\). Equivariance of the vector field preserves strict negativity of the averaged Lie derivative; the average is a positive multiple of \(x^2+y^2\). Therefore strict negativity would force \(a>\gamma\), contradicting \(a\le\gamma\). Globally positive-definite polynomials cannot have odd total degree, because their odd leading form changes sign along opposite rays. Hence degrees below four are impossible when \(a\le\gamma\), and the exhibited quartic is optimal.

## Verification

The companion `verify.py` reconstructs the Cartesian cubic field, differentiates the quartic symbolically, verifies the exact matrix Gram identity and determinant, verifies the quartic SOS decomposition, and checks the rational locked-direction example \((a,\omega,\gamma)=(4/5,4/5,1)\). In that example \(t=-5/8\), the Gram matrix is
\[
M=\begin{pmatrix}3/10&-1/2\\-1/2&13/10\end{pmatrix},
\qquad\det M=7/50>0,
\]
while the ordinary radial energy initially **increases** at angle zero, since \(-a+\gamma=1/5>0\). The verifier also runs 120 rational diagnostic substitutions; those finite tests are not offered as proofs of the parameter-uniform theorem.

## Relationship to prior work

Shevchenko, Liu and Liu (2026) establish an angular invariant-average criterion for global asymptotic stability of homogeneous vector fields and undecidability in sufficiently large fixed dimension. That general criterion is prior work; it does not supply an explicit sharp fixed-degree SOS representation for this angular-locked fourfold normal form. Ahmadi and Parrilo (2017/2018) establish existence of some SOS Lyapunov certificate under suitable prior polynomial-Lyapunov assumptions, without guaranteeing degree four or determining a degree-two/four boundary. Liu and Fitzsimmons (2026) demonstrate that general stable planar homogeneous cubics need not possess polynomial Lyapunov functions at all, emphasizing why an explicit uniform low-degree result needs a restricted class. A previous theorem for this same normal form treated only the strictly rotating sector \(\gamma<\omega\); the present theorem concerns the disjoint angular-locked range \(0\le\omega\le\gamma\), with a new sharp stability boundary and a different quartic certificate.

## Limitations

This is a theorem for a three-real-parameter homogeneous planar cubic family only. It is not a converse SOS result for general planar cubics, does not classify rates of escape on every unstable trajectory, and does not assert a strict quadratic Lyapunov function at \(a=\gamma\): in that case a nonstrict quadratic may exist even though no strict one does. Priority uncertainty remains for older treatments of special equivariant planar cubic normal forms, especially general homogeneous-flow classification literature. No independent external validation has been performed.

## References

1. I. O. Shevchenko, J. Liu and X. Liu, *Global asymptotic stability of homogeneous polynomial vector fields is undecidable*, arXiv:2610.12434v1, first public version 2026-10-08, Sections 1 and 3. URL: https://arxiv.org/html/2610.12434v1.
2. A. A. Ahmadi and P. A. Parrilo, *Sum of squares certificates for stability of planar, homogeneous, and switched systems*, arXiv:1801.00070v1 (2017), especially Theorems 3.3 and 3.5. URL: https://arxiv.org/pdf/1801.00070.
3. J. Liu and M. Fitzsimmons, *A Globally Asymptotically Stable Planar Homogeneous Polynomial Vector Field With No Polynomial Lyapunov Function*, arXiv:2607.16171v1 (2026); abstract inspected, not full text. URL: https://arxiv.org/abs/2607.16171.
