# Joint recovery of resetting, pinning and noise strength in a fluctuating interface

## Finding

Consider the one-dimensional, harmonically pinned Edwards–Wilkinson field whose **entire profile** is returned to zero at the event times of one common Poisson clock. At stationarity, measure the height variance \(V\) at one point, the normalized covariance \(R\) at a fixed nonzero spatial separation \(\ell\), and the standardized excess kurtosis \(K\) at one point. If the diffusivity \(\nu>0\) and separation \(\ell>0\) are known, these three measurements identify **all three unknown positive parameters**: uniform pinning \(\mu\), resetting rate \(r\), and noise strength \(D\).

Indeed, the image of the map \((\mu,r,D)\mapsto(V,R,K)\) is **exactly**
\[
V>0,\qquad 0<R<1,\qquad 0<K<\frac{12}{\pi}-3.
\]
Every triple satisfying these inequalities has exactly one preimage, given explicitly below. Thus the kurtosis separates two mechanisms—pinning and resetting—that enter the stationary two-point covariance only through their sum.

## Assumptions and scope

On the entire line \(x\in\mathbb R\), between resets the real field solves the linear stochastic heat equation in mild form,
\[
\partial_t h=\nu\partial_{xx}h-\mu h+\sqrt{2D}\,\xi,
\]
where \(\nu,\mu,D>0\), \(\xi\) is normalized space-time Gaussian white noise, and the flat initial condition after each reset is \(h(x,0)=0\) at every \(x\). A spatially global Poisson clock of rate \(r>0\), independent of the noise, resets the *whole* field, rather than resetting individual spatial points independently. The same noise convention applies across the line, with independent increments after a reset. In one spatial dimension, each point evaluation has finite variance. All observables concern the unique regenerative stationary one-time law; \(\ell>0\) is a known physical distance.

Define
\[
V=\mathbb E[h(0)^2],\quad
R=\frac{\mathbb E[h(0)h(\ell)]}{V},\quad
K=\frac{\mathbb E[h(0)^4]}{V^2}-3.
\]
Here \(\mathbb E[h(0)]=0\). Put \(s=r+2\mu\) and \(y=\sqrt{s/(2\mu)}=\sqrt{1+r/(2\mu)}>1\). The complete forward formulas are
\[
V=\frac{D}{\sqrt{2\nu s}},\quad
R=\exp\!\left[-\ell\sqrt{\frac{s}{2\nu}}\right],\quad
K=\frac{12}{\pi}y\arctan\!\frac1y-3.
\]

The inverse is as follows. From a valid observed triple set
\[
q=-\frac{\log R}{\ell}>0,\quad s=2\nu q^2.
\]
There is exactly one \(y>1\) satisfying
\[
\frac{12}{\pi}y\arctan(1/y)-3=K.
\]
Then necessarily and sufficiently,
\[
\boxed{\mu=\frac{s}{2y^2},\qquad
r=s\left(1-\frac1{y^2}\right),\qquad
D=V\sqrt{2\nu s}.}
\]

## Proof

**1. Stationary covariance.** The stochastic heat kernel after a reset is
\[
G_t(x)=e^{-\mu t}(4\pi\nu t)^{-1/2}\exp[-x^2/(4\nu t)].
\]
For age \(a>0\), the centered conditional Gaussian field has covariance
\[
C_a(z)=2D\int_0^a e^{-2\mu u}
 (8\pi\nu u)^{-1/2}\exp[-z^2/(8\nu u)]\,du.
\]
Regeneration at a homogeneous Poisson clock gives the stationary age \(A\sim\mathrm{Exp}(r)\). Tonelli's theorem (nonnegative heat kernels) yields
\[
C(z)=\mathbb E[C_A(z)]
=2D\int_0^\infty e^{-(r+2\mu)u}
 (8\pi\nu u)^{-1/2}\exp[-z^2/(8\nu u)]\,du.
\]
Using the one-dimensional heat-resolvent identity (or its Fourier transform) gives
\[
C(z)=\frac{D}{\sqrt{2\nu(r+2\mu)}}
\exp\!\left[-|z|\sqrt{\frac{r+2\mu}{2\nu}}\right].
\]
Both covariance statements for \(V=C(0)\) and \(R=C(\ell)/C(0)\) follow. They determine \(s=r+2\mu\) but by themselves do not separate \(r\) and \(\mu\).

**2. Fourth moment of a common-age mixture.** At a fixed point, conditional on age \(A=a\), the field is centered normal with variance
\[
v(a)=\frac{D}{2\sqrt{\nu\mu}}
\operatorname{erf}(\sqrt{2\mu a}).
\]
Put \(z=r/(2\mu)>0\) and \(T=2\mu A\sim\mathrm{Exp}(z)\). By integration by parts and the elementary Gaussian integral,
\[
\mathbb E[\operatorname{erf}(\sqrt T)]=\frac1{\sqrt{1+z}},
\]
\[
\mathbb E[\operatorname{erf}(\sqrt T)^2]
=\frac4{\pi\sqrt{1+z}}\arctan\!\frac1{\sqrt{1+z}}.
\]
For completeness, integration by parts in the second identity gives
\(\frac4{\sqrt\pi}\int_0^\infty e^{-(1+z)u^2}\operatorname{erf}(u)\,du\). Differentiating the same integral with \(\operatorname{erf}(bu)\) in the auxiliary parameter \(b\), then integrating from \(b=0\) to \(1\), evaluates it as stated. Since a centered normal with variance \(v\) has fourth moment \(3v^2\),
\[
K=3\left(\frac{\mathbb E[v(A)^2]}{\mathbb E[v(A)]^2}-1\right)
=\frac{12}{\pi}\sqrt{1+z}\arctan\!\frac1{\sqrt{1+z}}-3.
\]
The same global Poisson age appears at both points: treating resets at separate points as independent would invalidate this non-Gaussian mixture formula.

**3. Strict range and inverse.** Let \(f(y)=y\arctan(1/y)\) for \(y\ge1\). Then
\[
f'(y)=\arctan(1/y)-\frac{y}{1+y^2}>0,
\]
because \(\arctan u>u/(1+u^2)\) for every \(u>0\) (their difference has positive derivative \(2u^2/(1+u^2)^2\) and vanishes at zero). Moreover \(f(1)=\pi/4\) and \(\lim_{y\to\infty}f(y)=1\). Therefore \(K\) increases continuously and strictly from \(0\) to \(12/\pi-3\) as \(r/(2\mu)\) ranges through \((0,\infty)\). From \(V,R,K\), the displayed inverse gives positive \(\mu,r,D\) uniquely. Conversely, every positive parameter triple produces the three strict observable inequalities, proving both necessity and sufficiency.

## Verification

The accompanying `verify.py` directly integrates (i) the exponential age mixture of the conditional Gaussian second and fourth moments and (ii) the spatial heat-kernel covariance, without using the arctangent or exponential closed forms in those integrations. Five parameter tuples spanning small and large resetting-to-pinning ratios were checked against the analytic forward formulas; each independently reconstructed the original \(\mu,r,D\). Run with `python3 verify.py` using SciPy. The proof is analytic; these finite tests corroborate its normalization and inverse implementation but do not establish global strict monotonicity.

## Relationship to prior work

Gupta, Majumdar and Schehr (arXiv:1312.5954, first posted 20 December 2013) establish the global-reset renewal representation and the non-Gaussian stationary distribution of the **massless** one-dimensional Edwards–Wilkinson interface. Gupta, Rosso and Texier (arXiv:1308.0284, first posted 1 August 2013) study Gaussian relaxation and **localized elastic pinning** in a Rouse/Edwards–Wilkinson chain, without this uniform-mass/global-reset inverse problem. Olsen (arXiv:2310.04840, first posted 7 October 2023) studies a moment approach to resetting of a **single** harmonically confined particle, including resetting to a distribution. These forward frameworks motivate the present problem but do not, in their inspected parts, state the complete observable image and simultaneous recovery of uniform pinning, resetting and driving noise for the spatial field.

A prior finite-band **massless** interface result characterizes cutoff-dependent one-point kurtosis; another finite-mode result analyzes common-reset OU fourth-cumulant matrices. Neither is the same inverse map: this theorem uses an **unbounded spatial Fourier spectrum, nonzero uniform pinning, and a separated-point covariance** to determine absolute time and noise scales. The mass and reset effects are indistinguishable from second-order data alone but are exactly separable by the fourth moment. General renewal identities by themselves supply a representation, not the strict global inverse statement above.

## Limitations

The theorem assumes exact ensemble moments, spatially global instantaneous resetting, white noise, infinite-line geometry, strictly positive uniform pinning, and known \(\nu\) and \(\ell\). It does not assert statistical stability under finite samples or measurement noise. At the excluded boundaries \(r\downarrow0\) and \(\mu\downarrow0\), the kurtosis approaches \(0\) and \(12/\pi-3\), respectively; the boundary values cannot arise with both rates strictly positive. Unknown spatial calibration or additional noise correlations require separate analysis. Specialized unpublished or differently worded prior inverse results remain a priority risk.

## References

1. S. Gupta, A. Rosso, and C. Texier, *Dynamics of a Tagged Monomer: Effects of Elastic Pinning and Harmonic Absorption*, arXiv:1308.0284 (first posted 1 August 2013), https://arxiv.org/abs/1308.0284.
2. S. Gupta, S. N. Majumdar, and G. Schehr, *Fluctuating Interfaces Subject to Stochastic Resetting*, arXiv:1312.5954 (first posted 20 December 2013), Phys. Rev. Lett. 112, 220601 (2014), https://arxiv.org/abs/1312.5954.
3. K. S. Olsen, *Steady-state moments under resetting to a distribution*, arXiv:2310.04840 (first posted 7 October 2023), Phys. Rev. E 108, 044120 (2023), https://arxiv.org/abs/2310.04840.
