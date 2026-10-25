# Contact-order transition in the conditioning of jittered planar observability

## Finding

Fix integers \(a,b\ge1\), write \(m=a+b\), and choose \(0<\delta<\pi/12\) and \(-\delta<\Delta<\delta\). For a planar rotation observed in one fixed coordinate at \(m\) independent random phases, take \(a\) phases uniformly on \([-2\delta,0]\) and \(b\) uniformly on \([\Delta,\Delta+2\delta]\). Let \(H\) be the resulting \(m\)-by-\(2\) observation matrix, each row being \((\cos\theta_i,\sin\theta_i)\), and let \(s=\sigma_{\min}(H)\).

Put \(P=I_m-\mathbf1\mathbf1^{\mathsf T}/m\), \(v_k=\pi^{k/2}/\Gamma(k/2+1)\), and
\[
V_{a,b}=\operatorname{Vol}_m\{z:\ z_i\le0\ (1\le i\le a),\ z_j\ge0\ (a<j\le m),\ \|Pz\|_2<1\}.
\]
This is a finite, strictly positive constant. The three exact regimes are
\[
\begin{array}{ll}
-\delta<\Delta<0:&\displaystyle\Pr(s<t)\sim\frac{\sqrt m\,v_{m-1}(-\Delta)}{(2\delta)^m}\,t^{m-1},\\[4pt]
\Delta=0:&\displaystyle\Pr(s<t)\sim\frac{V_{a,b}}{(2\delta)^m}\,t^{m},\\[4pt]
0<\Delta<\delta:&\displaystyle s\ge\sqrt{1-\cos\Delta}\quad\text{for every realization}.
\end{array}
\]
For every \(p>0\), the negative moments of \(s\) and of the spectral condition number \(\kappa_2(H)\) are finite precisely when \(p<m-1\) in the overlap regime, precisely when \(p<m\) at contact, and for every \(p>0\) in the separated regime. Equality in either finite-moment threshold gives divergence.

The constants at contact are explicit geometric integrals, with \(V_{1,1}=1\) and \(V_{1,2}=V_{2,1}=\sqrt{2/3}\). Hence three observations divided into one and two touching phase windows have finite expected least-squares squared error under independent finite-variance measurement noise, whereas three observations with overlapping windows have infinite expected squared error. Four observations suffice in the overlap regime.

## Assumptions and scope

The dynamical system is \(\dot x=\omega Jx\), \(\omega>0\), with \(J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\); one observes \(e_1^{\mathsf T}x(t)\). A change of sign in the second state coordinate identifies its observation rows with those used above. Sampling phases mean \(\omega t\) modulo \(\pi\), with independent uniform choices in the specified intervals. The stated phases can be realized at nonnegative sampling times by adding sufficiently large multiples of \(\pi/\omega\), which does not affect any singular value. The results concern fixed \(m,a,b,\delta,\Delta\) and \(t\downarrow0\); they are not dimension-uniform estimates. The strict restriction on \(\delta,\Delta\) ensures every pairwise phase difference has magnitude less than \(\pi/2\), so no additional projective aliasing occurs.

## Proof

**Exact spectrum.** For arbitrary phases, let \(S=\sum_{i=1}^{m}e^{2\mathrm i\theta_i}\). Directly expanding \(H^{\mathsf T}H\) gives its two eigenvalues
\[
\lambda_\pm=\tfrac12(m\pm|S|).
\]
Hence \(s=\sqrt{(m-|S|)/2}\). Since all phases occupy an interval of length at most \(\Delta+4\delta<5\delta<\pi/2\), the only possible rank-one configurations have all phases equal (as ordinary real numbers). Such configurations have joint probability zero, and \(H\) has rank two almost surely.

**Uniform local normal form.** Near the rank-one diagonal write \(\theta=\mu\mathbf1+w\), with \(\mathbf1^{\mathsf T}w=0\). Taylor expansion of \(\sum e^{2\mathrm i w_i}\), using \(\sum w_i=0\), yields
\[
\tfrac12(m-|S|)=\|w\|_2^2+O(\|w\|_2^4),
\qquad s=\|w\|_2(1+O(\|w\|_2^2)).
\]
The bounds are uniform on a fixed neighborhood of the diagonal. The orthogonal-coordinate volume element is \(d\theta=\sqrt m\,d\mu\,dw\) when \(dw\) is Euclidean \((m-1)\)-dimensional measure on \(\mathbf1^\perp\).

**Overlapping windows.** For \(\Delta<0\), the diagonal intersected with the phase rectangle is precisely \(\{\mu\mathbf1:\Delta\le\mu\le0\}\), of length \(\sqrt m(-\Delta)\). Away from its endpoints, \(s<t\) forms a normal \((m-1)\)-ball of radius \(t(1+O(t^2))\). Endpoint sections contribute \(O(t^m)\). Since the joint density equals \((2\delta)^{-m}\), its leading volume is \(\sqrt m(-\Delta)v_{m-1}t^{m-1}\), proving the first line.

**Touching windows.** At \(\Delta=0\), the only rank-one point in the support rectangle is the origin. For sufficiently small \(t\), any \(\theta\) with \(s<t\) has \(\|P\theta\|=O(t)\) by the local normal form. Because the phase rectangle contains both a nonpositive and a nonnegative coordinate, this forces every coordinate to be \(O(t)\). Scale \(\theta=tz\). Its rescaled support tends to the mixed-sign orthant, and \(s(tz)/t\to\|Pz\|\) uniformly on bounded sets. The admissible rescaled sets are uniformly bounded: \(|z_i-z_j|\le\sqrt2\|Pz\|\), and an oppositely signed pair bounds all coordinates. The bounded-convergence theorem therefore gives the volume \(V_{a,b}t^m+o(t^m)\), proving the second line. The same argument shows \(0<V_{a,b}<\infty\).

A second exact representation, useful for evaluation, is
\[
V_{a,b}=\sqrt m\int_{\substack{w\in\mathbf1^\perp\\ \|w\|<1}}
\left(\min_{j>a}w_j-\max_{i\le a}w_i\right)_+\,dw.
\]
For \(a=b=1\), direct integration over the two-dimensional wedge gives \(V_{1,1}=1\). For \(a=1,b=2\), use \(u=z_2-z_1\), \(v=z_3-z_1\); the allowable length of \(z_1\) is \(\min(u,v)\), while \(\|Pz\|^2=2(u^2+v^2-uv)/3\). Thus
\[
V_{1,2}=\int_{u,v\ge0\atop u^2+v^2-uv<3/2}\min(u,v)\,du\,dv
=\int_0^{\sqrt{3/2}}u\left(\sqrt{6-3u^2}-u\right)du
=\sqrt{2/3}.
\]
Interchanging the group labels gives \(V_{2,1}=V_{1,2}\).

**Separated windows.** If \(\Delta>0\), choose any row from each group; their phase difference lies in \([\Delta,\Delta+4\delta]\subset(0,\pi/2)\). The two-row Gram matrix has least eigenvalue \(1-\cos(\theta_B-\theta_A)\ge1-\cos\Delta\). Adding the other observation rows adds positive-semidefinite terms to the Gramian, proving the deterministic bound.

**Inverse moments and estimation risk.** If \(\Pr(s<t)\sim c t^q\) with \(c,q>0\), the layer-cake formula for \(s^{-p}\) shows \(\mathbb E s^{-p}<\infty\) exactly for \(p<q\), with logarithmic divergence at \(p=q\). Since \(\lambda_++\lambda_-=m\), \(\sqrt{m/2}\le\sigma_{\max}(H)\le\sqrt m\), so \(\kappa_2(H)\) is bounded above and below by positive multiples of \(s^{-1}\). For independent zero-mean measurement errors with common variance \(\tau^2>0\), conditional least-squares mean squared state error is \(\tau^2\operatorname{tr}(H^{\mathsf T}H)^{-1}=\tau^2(s^{-2}+\sigma_{\max}^{-2})\); the stated sample-count consequences follow with \(p=2\).

## Verification

The accompanying `verify.py` checks the exact Gram-spectrum formula against a direct \(2\)-by-\(2\) eigenvalue calculation for \(2100\) seeded phase samples; the exact two-observation triangular-density formulas at overlap and contact; the closed three-observation cone integral \(V_{1,2}=\sqrt{2/3}\) by Simpson quadrature; and the separated-window lower bound on \(4000\) seeded draws. Run with `python3 verify.py`; no external packages are required. The universal asymptotics and moment endpoints are established analytically above, not by sampling or quadrature.

## Relationship to prior work

Krauss, Lopez, and Müller, *Sample-based observability of linear discrete-time systems*, arXiv:2204.06451, analyze pathological sampling and qualitative rank recovery. Their original version was publicly posted April 13, 2022. Their second-order sampling conditions do not give a probability law, contact-order singular-value exponent, or inverse-moment criterion under independent interval jitter. Bass and Gröchenig, *Random Sampling of Multivariate Trigonometric Polynomials*, study the conditioning of random trigonometric sampling matrices; their work is particularly relevant to the common-interior regime, and should not be conflated with a priority claim for generic random-frame small-ball reasoning. The distinguishing asserted result here is the three-way fixed-horizon support-contact transition, with exact mixed-sign cone coefficient and least-squares risk consequences. Koltchinskii and Mendelson provide non-asymptotic singular-value bounds for independent random rows under different assumptions, rather than this fixed-dimensional endpoint geometry. Earlier nonuniform sampling literature gives observability criteria but does not, in accessible material, determine the contact coefficient.

## Limitations

Only planar rotations, one fixed observation coordinate, independent uniform phase jitter in two equal-width interval families, and the specified small-arc range are covered. The derived bound in the separated regime is sufficient but is not asserted optimal for more than two rows. The asymptotic coefficients are for fixed parameters, not uniform as \(\Delta\to0\). The volume \(V_{a,b}\) is a finite integral, not an elementary closed form for every group size. The result does not give noise-filtering bounds for nonlinear, damped, or process-noise-driven systems. A relevant historical trigonometric random-sampling paper was inaccessible in full, leaving residual priority risk.

## References

1. I. Krauss, V. G. Lopez, M. A. Müller, *Sample-based observability of linear discrete-time systems*, arXiv:2204.06451 (first posted 2022-04-13), https://arxiv.org/html/2204.06451v3.
2. R. F. Bass, K. Gröchenig, *Random Sampling of Multivariate Trigonometric Polynomials*, SIAM J. Math. Anal. 36 (2004/05), 773–795, DOI:10.1137/S0036141003432316.
3. V. Koltchinskii, S. Mendelson, *Bounding the Smallest Singular Value of a Random Matrix Without Concentration*, arXiv:1312.3580 (2013), https://arxiv.org/html/1312.3580v1.
4. W. M. Brown, *Sampling with Random Jitter*, J. SIAM 11 (1963), 460–473, DOI:10.1137/0111033.
5. A. Fúster-Sabater, J. M. Guillén, *Characterisation of observability and controllability for nonuniformly sampled discrete systems*, arXiv:1006.4288 (2010).
