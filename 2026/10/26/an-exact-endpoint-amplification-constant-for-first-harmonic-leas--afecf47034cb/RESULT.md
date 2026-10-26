# An exact endpoint amplification constant for first-harmonic least squares on a semicircle

## Finding
Let \(\mu(d\theta)=d\theta/\pi\) on \([0,\pi]\), and let \(P\) be the \(L^2(\mu)\)-orthogonal projector onto
\[\mathcal{A}=\operatorname{span}_{\mathbb R}\{1,\cos\theta,\sin\theta\}.\]
Then its **sharp** endpoint norms coincide:
\[\boxed{\|P\|_{L^1(\mu)\to L^1(\mu)}=\|P\|_{L^\infty(\mu)\to L^\infty(\mu)}=\Lambda_{\mathrm{semi}}},\]
where, with
\[D=\pi^2-8,\quad R=2\sqrt{D^2+4\pi^2},\quad \beta=\arccos(\pi^2/R),\]
\[\boxed{\Lambda_{\mathrm{semi}}=1+\frac{4}{\pi D}\left(\sqrt{3\pi^4-48\pi^2+256}-\pi^2\beta\right)=2.0480992714794347668\ldots>2.}\]
Every maximizing evaluation of the absolute-kernel integral occurs at one of the two arc endpoints \(\theta=0,\pi\), and no interior evaluation is maximizing. Sharp input functions are the signs of the endpoint projection kernels (and their negatives). For the full circle, by contrast, the corresponding first-harmonic projector has norm \(1/3+2\sqrt3/\pi=1.43599\ldots\); restricting to a semicircle therefore changes the worst-case amplification quantitatively.

## Assumptions and scope
All functions are real measurable functions modulo \(\mu\)-null sets. The underlying geometry is a semicircular arc of unit radius, sampled by **continuous uniform arclength**, not a finite point cloud and not the filled half-disk. The approximation space consists of restrictions of affine functions in the two Cartesian coordinates (equivalently, the constant and the first sine/cosine harmonics). The \(L^\infty\) norm is the essential supremum, and the endpoint evaluation of \(Pf\) uses the continuous representative in \(\mathcal A\). The operator is bounded on both \(L^1\) and \(L^\infty\) because its kernel is continuous.

## Proof
**1. Kernel.** Under \(\mu\), \(\mathbb E[\cos\theta]=0\), \(\mathbb E[\sin\theta]=m=2/\pi\), \(\mathbb E[\cos^2\theta]=1/2\), and \(\operatorname{Var}(\sin\theta)=v=1/2-m^2>0\). The centered coordinate features are orthogonal. The projection kernel is therefore
\[K(\theta,\varphi)=1+2\cos\theta\cos\varphi+\frac{(\sin\theta-m)(\sin\varphi-m)}{v},\quad Pf(\theta)=\frac1\pi\int_0^\pi K(\theta,\varphi)f(\varphi)\,d\varphi.\]
It is symmetric and reproduces constants. Hence \(\|P\|_{\infty\to\infty}=\max_{\theta\in[0,\pi]} F(\theta)\), with \(F(\theta)=\pi^{-1}\int_0^\pi|K(\theta,\varphi)|\,d\varphi\); symmetry of \(K\) gives the equality of the \(L^1\) and \(L^\infty\) norms.

**2. Endpoint localization, analytically for the entire continuum.** Reflection \(\varphi\mapsto\pi-\varphi\) and the identity \(|a+b|+|a-b|=2\max\{|a|,|b|\}\) give, on setting \(t=\sin\theta\),
\[F(\theta)=\frac2\pi\int_0^{\pi/2}\max\left\{\left|1+\frac{(t-m)(\sin\varphi-m)}v\right|,\ 2\sqrt{1-t^2}\cos\varphi\right\}\,d\varphi.\]
Thus \(F\) depends only on \(t\in[0,1]\). Put \(s=\sin\varphi\), \(a(t,s)=1+(t-m)(s-m)/v\) and \(b(t,s)=2\sqrt{1-t^2}\sqrt{1-s^2}\).

For \(0\le t\le1/3\) and \(s\le m\), \(a\ge1\) and both \(a\) and \(b\) are nonincreasing in \(t\). For \(s>m\), \(a\) increases with \(t\), so its negative part \((-a)_+\) decreases. We claim that whenever \(a\ge0\), \(b\ge a\). In fact the positive interval in \(s\) is \([m,s_0]\), where \(s_0=m+v/(m-t)\le1\). The last inequality is equivalent to \(t\le(m-1/2)/(1-m)\), and this threshold is larger than \(1/3\), because \(m>5/8\). The function \(s\mapsto b(t,s)-a(t,s)\) is concave on \([m,s_0]\); it is nonnegative at \(s_0\), and at \(m\) it equals \(2\sqrt{1-t^2}\sqrt{1-m^2}-1>0\). Hence \(\max\{|a|,b\}=\max\{(-a)_+,b\}\) for \(s>m\), and this expression too is nonincreasing in \(t\). Pointwise comparison under the integral proves
\[F(\theta)\le F(0)\quad\text{whenever }0\le\sin\theta\le1/3.\]
Strictness away from \(t=0\) follows on a positive-measure range \(s<m\), where the winning positive branch strictly decreases.

For \(1/3\le t\le1\), Cauchy--Schwarz and the reproducing identity imply
\[F(\theta)^2\le\int|K(\theta,\varphi)|^2\,d\mu(\varphi)=K(\theta,\theta)=1+2(1-t^2)+\frac{(t-m)^2}{v}.\]
The right-hand side is a strictly convex quadratic in \(t\), so its maximum on \([1/3,1]\) is attained at an endpoint. Direct elementary bounds \(3.14159<\pi<3.14160\) give both endpoint values strictly smaller than \(4\). Consequently \(F(\theta)<2\) throughout this interval. The next step proves \(F(0)>2\). Therefore the only maximizing evaluation parameters are \(t=0\), corresponding exactly to \(\theta=0,\pi\).

**3. Exact endpoint integral.** At \(\theta=0\),
\[K(0,\varphi)=\frac{\pi^2+2D\cos\varphi-4\pi\sin\varphi}{D}.\]
Write \(\delta=\arctan(2\pi/D)\). The numerator is \(\pi^2+R\cos(\varphi+\delta)\). It is positive at \(\varphi=0,\pi\) but negative at \(\varphi=\pi/2\), so has exactly two interior zeros, \(\varphi_\pm=\pi-\delta\pm\beta\). The negative-region integral, evaluated by one antiderivative, equals
\[\int_{\varphi_-}^{\varphi_+}K(0,\varphi)\,d\varphi=\frac2D(\pi^2\beta-R\sin\beta).\]
Because \(\pi^{-1}\int K(0,\varphi)\,d\varphi=1\), the absolute-kernel integral is \(1-2/\pi\) times this negative integral. This gives the stated formula using \(R\sin\beta=\sqrt{R^2-\pi^4}=\sqrt{3\pi^4-48\pi^2+256}\).

To prove \(\Lambda_{\mathrm{semi}}>2\) without relying on a decimal approximation, integrate \(K(0,\varphi)\) on the fixed interval \([\pi/3,5\pi/6]\). Its integral is less than \(-\pi/2\) precisely when
\[\pi(\pi^2-6-2\sqrt3)+(\pi^2-8)(1-\sqrt3)<0.\]
The inequality follows, for example, from the rational enclosures \(3.14159<\pi<3.14160\) and \(1.73205<\sqrt3<1.73206\): an explicit rational upper bound for the left-hand side is \(-0.09437\ldots\). Since the signed integral of the negative part is no greater than the signed integral over any selected interval, this implies \(F(0)>2\). Finally, choosing \(f(\varphi)=\operatorname{sgn}K(0,\varphi)\) gives \(\|f\|_\infty=1\) and \(Pf(0)=\Lambda_{\mathrm{semi}}\). No finite discretization is used for sharpness.

## Verification
Run `python verify.py` with Python 3 and `mpmath`. The standalone checker tests five decisive inequalities with rational arithmetic, locates the two analytic sign zeros to high precision, independently integrates the split projection kernel, checks the moment identity, and compares 35 nonendpoint evaluations numerically. It reports 48 checks passed. The grid samples corroborate the result but are not part of the global extremizer proof; the proof in the preceding section covers all real \(\theta\in[0,\pi]\).

## Relationship to prior work
Huybrechs, *On the Fourier Extension of Nonperiodic Functions* (public journal version dated January 27, 2010, DOI 10.1137/090752456; an earlier technical report is dated only by month), studies the corresponding half-range trigonometric approximation geometry, its orthogonal-polynomial structure and numerical stability. The inspected full text does not give the present sharp degree-one \(L^\infty\)-norm, its exact radical--inverse-trigonometric value, or the endpoint-maximization proof. Hangelbroek--Narcowich--Sun--Ward, arXiv:1005.2424 (first posted May 13, 2010), prove uniform \(L^p\) bounds for kernel-based least-squares projectors under structural hypotheses rather than a sharp number for this elementary arc space. A known three-frequency cyclic Fourier-projection calculation concerns a **finite uniform group on a full circle**; it does not imply the continuous nonperiodic semicircle result, whose Gram matrix and kernel differ. These statements concern mathematical implication rather than title similarity.

## Limitations
The result is for the first harmonic and one specific, natural semicircular arc. It does not give a degree-uniform bound, a formula for arbitrary arc opening angles, or sharp norms for higher harmonics. Published-priority research cannot prove absolute uniqueness: full-text inspection of Huybrechs and Hangelbroek plus targeted literature searches found no covering claim, but specialist non-indexed Fourier-extension sources remain a residual risk. This is a self-review, not independent verification.

## References
1. D. Huybrechs, *On the Fourier Extension of Nonperiodic Functions*, SIAM J. Numer. Anal. **47** (2010), 4326--4355, DOI: 10.1137/090752456, full text: https://people.cs.kuleuven.be/~daan.huybrechs/research/sinum_fourierextension.pdf (public electronic date January 27, 2010; earlier institutional technical report is month-dated January 2009).
2. T. Hangelbroek, F. J. Narcowich, X. Sun, J. D. Ward, *Kernel Approximation on Manifolds II: The \(L^\infty\)-norm of the \(L^2\)-projector*, arXiv:1005.2424, first posted May 13, 2010, https://arxiv.org/abs/1005.2424.
3. *Exact three-frequency Fourier projection norm on every cyclic group*, publicly accessible statement: https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-three-frequency-fourier-projection-norm-on-every-cyclic-gr--b176a6018242 (finite-group comparison, not a source of the semicircle formula).
