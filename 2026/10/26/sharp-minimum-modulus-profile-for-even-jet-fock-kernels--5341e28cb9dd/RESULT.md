# Sharp minimum-modulus profile for even-jet Fock kernels

## Finding
Fix an even positive integer \(m\), a finite penalty \(\tau\geq0\), and the standard Gaussian Fock Hilbert space with an additional \(m\)-th Taylor jet penalty at the origin. Write
\[
q=\frac{\tau}{1+\tau m!},\qquad
F_{m,\tau}(t)=e^t-q t^m.
\]
Its reproducing kernel is \(K_{m,\tau}(z,w)=F_{m,\tau}(z\overline w)\). For every \(r\geq0\), its exact minimum-modulus profile is
\[
\boxed{\min_{|t|\leq r}|F_{m,\tau}(t)|
=\max\{0,e^{-r}-q r^m\}.}
\]
Equivalently, for every \(\rho\geq0\), the minimum of \(|K_{m,\tau}(z,w)|\) over \(|z|,|w|\leq\rho\) is \(\max\{0,e^{-\rho^2}-q\rho^{2m}\}\). When \(\tau>0\), the zero closest to the origin is uniquely \(t=-R_{m,\tau}\), where
\[
R_{m,\tau}=m W_0\!\left(\frac{q^{-1/m}}m\right),
\qquad e^{-R_{m,\tau}}=qR_{m,\tau}^{m}.
\]
It is simple, and the open observation disk \(|z|,|w|<\rho\) has zero-free kernel precisely when \(\rho^2\le R_{m,\tau}\). When \(\tau=0\), the kernel is zero-free everywhere (write \(R_{m,0}=+\infty\)). The radius valid simultaneously for every finite \(\tau\geq0\) is
\[
R_m^{\mathrm{unif}}=mW_0\!\left(\frac{(m!)^{1/m}}m\right).
\]
This radius is optimal as a uniform bound: any larger squared observation radius has a kernel zero for sufficiently large finite penalty. As \(m\) increases through even integers,
\[
R_m^{\mathrm{unif}}
=m\omega+\frac{\omega}{2(1+\omega)}\log(2\pi m)
+O\!\left(\frac{(\log m)^2}{m}\right),
\qquad \omega=W_0(e^{-1})=0.278464542761\ldots.
\]

## Assumptions and scope
The complex plane carries normalized Gaussian measure \(\pi^{-1}e^{-|z|^2}\,dA(z)\). For the entire function \(f(z)=\sum_{n\geq0}a_nz^n\), define the positive Hilbert norm
\[
\|f\|_{m,\tau}^2=\sum_{n\geq0}n!|a_n|^2+\tau|f^{(m)}(0)|^2.
\]
The penalty is finite, real and nonnegative, and \(m\in\{2,4,6,\ldots\}\). Both kernel variables range over the entire complex plane. We define the standard principal real Lambert branch \(W_0(x)\) on \(x>0\) by \(W_0(x)e^{W_0(x)}=x\) and \(W_0(x)>0\). The infimum on closed observation disks is attained; the assertions about open disks refer to absence of zeros strictly inside.

## Proof
The monomials are orthogonal under the Gaussian measure and have squared norms \(n!\). Since \(f^{(m)}(0)=m!a_m\), only the squared norm of \(z^m\) changes: it is \(m!+\tau(m!)^2=m!(1+\tau m!)\). Expanding the inverse squared norms of the monomial basis therefore gives
\[
K_{m,\tau}(z,w)=\sum_{n\ne m}\frac{(z\overline w)^n}{n!}
+\frac{(z\overline w)^m}{m!(1+\tau m!)}
=e^{z\overline w}-\frac{\tau}{1+\tau m!}(z\overline w)^m.
\]
Fix \(q>0\). If \(|t|\le r\), then the reverse triangle inequality and \(\operatorname{Re}t\ge-|t|\) imply
\[
|e^t-qt^m|\ge e^{\operatorname{Re}t}-q|t|^m
\ge e^{-|t|}-q|t|^m
\ge e^{-r}-qr^m.
\]
For \(r\) at most the unique positive solution \(R\) of \(e^{-R}=qR^m\), the right-hand side is nonnegative. Since \(m\) is even, choosing \(t=-r\) gives equality \(|e^{-r}-q(-r)^m|=e^{-r}-qr^m\). For \(r\ge R\), the point \(t=-R\) is a zero contained in the closed disk, so the minimum is zero. This proves the entire minimum-modulus formula and the fact that \(t=-R\) is the sole zero of modulus \(R\): equality in \(\operatorname{Re}t\ge-|t|\) forces \(t\) negative real; strict monotonicity of \(e^{-s}-qs^m\) for \(s\ge0\) fixes \(s=R\). It is simple because
\[
F'_{m,\tau}(-R)=e^{-R}+qmR^{m-1}>0.
\]
The strictly decreasing function \(e^{-s}-qs^m\) has one positive zero. Solving it by taking its positive \(m\)-th root gives \(R e^{R/m}=q^{-1/m}\), hence the Lambert expression. Every complex \(t\) of modulus at most \(\rho^2\) occurs as \(z\overline w\) with \(|z|,|w|\le\rho\), so the scalar and two-variable disk minima coincide. For the open disks the closest zero enters exactly when \(\rho^2>R\); equality is zero-free in the open bidisk.

The deficit coefficient \(q(\tau)=\tau/(1+\tau m!)\) increases continuously from zero toward \(1/m!\) as \(\tau\to\infty\). Consequently \(R\) decreases toward \(mW_0((m!)^{1/m}/m)\), and every squared radius larger than this limit includes a zero at a sufficiently large finite \(\tau\). Finally Stirling's expansion gives
\[
\log\!\left(\frac{(m!)^{1/m}}m\right)
=-1+\frac{\log(2\pi m)}{2m}+O(m^{-2}).
\]
Taylor expansion of \(W_0\) about \(e^{-1}\), using \(W'_0(x)=W_0(x)/(x(1+W_0(x)))\), yields the claimed sharp asymptotic.

## Verification
The standalone `verify.py` computes the exact Lambert equality to high precision for 16 pairs of even derivative order and finite penalty, checks sampled closed disks against the analytic lower bound, verifies sharpness at the negative real extremizer, checks the zero's derivative, and verifies six limiting radii. These finite tests are diagnostic only. Every quantified complex-variable assertion above follows from the inequalities and identities in the proof.

## Relationship to prior work
The standard Gaussian Fock kernel and the monomial-basis reproducing-kernel method are classical. Cho, Choe and Koo (arXiv:1307.2670, first posted 2013-07-10) develop Fock-Sobolev spaces and give monomial and reproducing-kernel formulas for global weights; their Theorem 4.5 concerns fractional-order weighted Fock spaces, not a single coefficient-jet penalty or the exact minimum modulus under bounded observations. The present formula starts from the same classical monomial mechanism but concerns a different finite-rank norm perturbation and determines a sharp two-variable nonvanishing and stability profile. The Lambert function is used only as the standard inverse of \(x\mapsto xe^x\); the novelty claim concerns this particular quantified kernel profile, not the inverse-function identity. Available mathematical-record searches did not reveal an equivalent sharp even-jet profile, but indexing and source-access limitations preclude a global novelty guarantee.

## Limitations
The exact minimum-modulus formula here requires even derivative order and nonnegative real penalty. Odd orders are not classified by this argument because \((-r)^m\) changes sign. The guarantee is about the modulus of individual kernel entries, not positivity of an interpolation Gram determinant or general numerical conditioning of arbitrary multi-point interpolation. Independent mathematical review has not been performed. An undiscovered equivalent characterization could change the originality assessment.

## References
1. H. R. Cho, B. R. Choe and H. Koo, *Fock-Sobolev spaces of fractional order*, arXiv:1307.2670 (first posted 2013-07-10); especially introduction and Theorem 4.5, https://arxiv.org/abs/1307.2670 .
2. The Lambert \(W\) function, classical inverse-function identity \(W(x)e^{W(x)}=x\), used without any novelty claim.
