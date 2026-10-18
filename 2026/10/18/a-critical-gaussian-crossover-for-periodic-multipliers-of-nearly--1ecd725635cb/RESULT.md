# A critical Gaussian crossover for periodic multipliers of nearly linear expanding circle maps

## Finding

For each integer \(b\ge 2\), consider the degree-\(b\) circle endomorphism
\[
 f_\varepsilon(x)=bx+\varepsilon\sin(2\pi x)\pmod 1.
\]
Write \(\mathcal P_n(\varepsilon)=\operatorname{Fix}(f_\varepsilon^n)\), and, for \(p\in\mathcal P_n(\varepsilon)\), let
\[
 \Lambda_n(p,\varepsilon)=\log (f_\varepsilon^n)'(p).
\]
Sample \(p\) uniformly from the \(b^n-1\) points of \(\mathcal P_n(\varepsilon)\), including points of shorter least period. For every fixed real \(\tau\), set \(\varepsilon_n=\tau/\sqrt n\). Then
\[
 \Lambda_n(p,\varepsilon_n)-n\log b
 \ \xrightarrow[n\to\infty]{\mathrm{law}}\ 
 \mathcal N\!\left(\frac{\pi^2\tau^2}{b^2},\frac{2\pi^2\tau^2}{b^2}\right).
\]
The convention at \(\tau=0\) is the point mass at zero. Thus the finite limiting variance is exactly twice the positive limiting mean shift.

There is also an exact finite-period perturbation identity. If \(\mathbb E_n^\varepsilon\) is uniform averaging over \(\mathcal P_n(\varepsilon)\), then for every integer \(n\ge3\),
\[
 \left.\frac{d}{d\varepsilon}\mathbb E_n^\varepsilon[\Lambda_n]\right|_{\varepsilon=0}=0,
 \qquad
 \left.\frac{d^2}{d\varepsilon^2}\mathbb E_n^\varepsilon[\Lambda_n]\right|_{\varepsilon=0}
 =\frac{2n\pi^2}{b^2}\frac{b^n+1}{b^n-1},
\]
and
\[
 \operatorname{Var}_{\mathcal P_n(0)}\!\left(
 \left.\partial_\varepsilon\Lambda_n(p,\varepsilon)\right|_{\varepsilon=0}
 \right)=\frac{2n\pi^2}{b^2},
\]
where the derivative in the last display follows the continuation of each periodic point. Both identities are exact, not just asymptotic.

## Assumptions and scope

The phase space is \(\mathbb T=\mathbb R/\mathbb Z\). The integer \(b\ge2\) is fixed while \(n\to\infty\). For all sufficiently small \(|\varepsilon|\), specifically whenever \(b-2\pi|\varepsilon|>1\), the map is uniformly expanding and orientation preserving; its fixed-point sets are well-defined and have cardinality \(b^n-1\). The parameter \(\tau\) is fixed, not allowed to grow with \(n\). A normal law with zero variance denotes a Dirac mass. The perturbation identities use ordinary derivatives of the finite sum obtained by continuing all periodic points smoothly; they are not derivatives of an integral with a fixed sampling measure.

## Proof

**1. A uniform-in-time conjugacy expansion.** Set \(T(x)=bx\pmod1\). A degree-one near-identity conjugacy \(H_\varepsilon(x)=x+w_\varepsilon(x)\pmod1\) solving \(f_\varepsilon\circ H_\varepsilon=H_\varepsilon\circ T\) is obtained by the fixed-point equation
\[
 w_\varepsilon(x)=-\varepsilon\sum_{j=0}^\infty b^{-j-1}
 \sin\bigl(2\pi(b^j x+w_\varepsilon(b^j x))\bigr).
\]
This defines a contraction on real continuous, one-periodic functions when \(2\pi|\varepsilon|/(b-1)<1\). Its unique solution satisfies \(\|w_\varepsilon\|_\infty\le|\varepsilon|/(b-1)\) and depends three times continuously differentiably on \(\varepsilon\) in the uniform norm: the right side is a smooth Nemytskii map on \(C^0(\mathbb T)\) with invertible fixed-point linearization at zero. The induced circle map is a homeomorphism: it has degree one and is surjective; if it identifies two points, their forward \(T\)-orbits remain within \(2\|w_\varepsilon\|_\infty\) of each other, contradicting positive expansivity of \(T\) once \(\varepsilon\) is small enough. Accordingly the conjugacy bijects \(\mathcal P_n(0)\) and \(\mathcal P_n(\varepsilon)\).

Put
\[
 u(x)=\left.\partial_\varepsilon w_\varepsilon(x)\right|_0
 =-\sum_{j\ge0}b^{-j-1}\sin(2\pi b^j x).
\]
The series converges uniformly. A Taylor expansion **in the uniform norm** gives
\[
 \log f_\varepsilon'(H_\varepsilon(x))
 =\log b+\varepsilon g(x)+\varepsilon^2h(x)+O_b(|\varepsilon|^3),
\]
with uniform remainder, where
\[
 g(x)=\frac{2\pi}{b}\cos(2\pi x),\qquad
 h(x)=-\frac{4\pi^2}{b}u(x)\sin(2\pi x)
       -\frac{2\pi^2}{b^2}\cos^2(2\pi x).
\]
Thus, uniformly for all \(n\), all \(x\in\mathcal P_n(0)\), and small \(\varepsilon\),
\[
 \Lambda_n(H_\varepsilon x,\varepsilon)-n\log b
 =\varepsilon S_ng(x)+\varepsilon^2S_nh(x)+O_b(n|\varepsilon|^3),
 \quad S_nv(x)=\sum_{j=0}^{n-1}v(T^jx).
\]
Orthogonality of distinct integer Fourier frequencies yields the exact integrals
\[
 \int g\,dx=0,\quad \int g^2\,dx=\frac{2\pi^2}{b^2},\quad
 \int g\,g\circ T^j\,dx=0\ (j\ge1),\quad
 \int u(x)\sin(2\pi x)\,dx=-\frac1{2b}.
\]
In particular \(\int h\,dx=\pi^2/b^2\).

**2. Uniform periodic-word sampling.** Put \(q=b^n-1\). The points in \(\mathcal P_n(0)\) are exactly \(k/q\) modulo one, \(0\le k<q\). Choosing instead one of the \(b^n\) length-\(n\) base-\(b\) words uniformly and repeating it periodically gives those same points, except that \(0\) receives one extra copy (from the word whose digits are all \(b-1\)). The total-variation discrepancy is at most \(b^{-n}\). Thus any limiting probability law under one ensemble holds under the other.

For every continuous \(v\), the law of large numbers \(S_nv/n\to\int v\,dx\) in probability follows directly from the periodic-word representation: approximate \(v\) uniformly by a function of its first \(L\) base-\(b\) digits; the resulting random variables at cyclic shifts at distance at least \(L\) are independent. The variance of their empirical average is \(O(L/n)\), and the expected value equals the Haar integral. Take \(n\to\infty\) for fixed \(L\), then let the approximation error vanish. Applying this to the continuous \(h\) gives \(S_nh/n\to\pi^2/b^2\).

For the central limit theorem for \(g\), choose \(L_n=\lceil3\log_b n\rceil\) and replace each \(g(T^j x)\) by its conditional expectation given the next \(L_n\) digits. The total approximation error in the sum is bounded by \(O_b(nb^{-L_n})=o(1)\). Divide the cyclic digit indices into retained blocks of length \(\lfloor n^{1/3}\rfloor\), separated by discarded gaps of length at least \(L_n\); discard also a closing gap. Retained block sums are independent because their digit windows are disjoint, and each is bounded by \(O(n^{1/3})=o(\sqrt n)\), so the Lindeberg condition holds.

The asymptotic variance is exact rather than inferred from a mixing heuristic. For \(n\ge3\), no integer \(b^i\pm b^j\) with \(0\le i<j<n\) is divisible by \(q\), because \(0< b^j+b^i<q\). Discrete Fourier orthogonality therefore gives
\[
 \mathbb E_{\mathcal P_n(0)}S_ng=0,\qquad
 \mathbb E_{\mathcal P_n(0)}(S_ng)^2=
 \frac{2n\pi^2}{b^2}.
\]
The omitted indices number \(O(n^{2/3}\log n)=o(n)\), and, by the same exact orthogonality, their contribution has variance \(o(n)\); word-ensemble and cylinder-approximation errors are negligible. Therefore the sum of independent retained-block variances divided by \(n\) tends to \(2\pi^2/b^2\). Lindeberg--Feller yields
\[
 \frac{S_ng}{\sqrt n}\ \xrightarrow{\mathrm{law}}\
 \mathcal N\!\left(0,\frac{2\pi^2}{b^2}\right).
\]
For \(\varepsilon_n=\tau/\sqrt n\), the uniform remainder in step 1 is \(O_b(n^{-1/2}|\tau|^3)\). Thus
\[
 \Lambda_n(H_{\varepsilon_n}x,\varepsilon_n)-n\log b
 =\tau\frac{S_ng}{\sqrt n}+\tau^2\frac{S_nh}{n}+o(1).
\]
Slutsky's theorem proves the stated shifted Gaussian law, including the degenerate case \(\tau=0\).

**3. The exact finite-period curvature.** Differentiating the uniform expansion in step 1 along the continued periodic points gives first derivative \(S_ng\) and second derivative \(2S_nh\). The finite-grid average of \(g\) is zero. For \(x=k/q\), the differentiated conjugacy equation also gives
\[
 u(Tx)-bu(x)=\sin(2\pi x),\qquad
 u(x)=-\frac1q\sum_{j=0}^{n-1} b^{n-1-j}\sin(2\pi b^j x).
\]
With \(n\ge3\), finite cyclic Fourier orthogonality implies
\[
 \mathbb E_{\mathcal P_n(0)}\cos^2(2\pi x)=\frac12,\qquad
 \mathbb E_{\mathcal P_n(0)}u(x)\sin(2\pi x)=-\frac{b^{n-1}}{2q}.
\]
Hence \(\mathbb E_{\mathcal P_n(0)}h=\pi^2(b^n+1)/(b^2q)\), because \(2b^n-q=b^n+1\). By invariance of the periodic grid under \(T\), \(\mathbb E S_nh=n\mathbb E h\). This yields the exact second-derivative formula. The exact first-derivative variance is the Fourier identity in step 2.

## Verification

A standalone script, `verify.py`, tests finite-grid Fourier nonresonance and the resulting curvature formula for 35 integer pairs \((b,n)\), with \(2\le b\le6\) and \(3\le n\le9\). For nine additional pairs, it continues all actual periodic points at two small perturbations by Newton iteration, computes their logarithmic derivative sums directly, and compares central finite differences with the exact curvature. The script passes these finite diagnostics. Its numerical step, finite ranges, and double-precision calculation do not establish the infinite Gaussian limit; that limit follows from the uniform conjugacy expansion, cyclic-word blocking and law of large numbers proved above.

## Relationship to prior work

Drach, Fu, Kaloshin, Li, and Liverani establish a central limit theorem for periodic Lyapunov exponents of a *fixed* smooth expanding circle map not smoothly conjugate to its linear model [1]. Their theorem centers at the map-dependent maximal-entropy Lyapunov exponent, normalizes by a strictly positive map-dependent variance, and does not give a uniform statement as the perturbation tends to zero. The present joint limit has \(\varepsilon=\tau/\sqrt n\) and an explicit uncentered Gaussian shift and variance, with the linear map as its limiting boundary.

De la Llave, Shub, and Simó already study the **same sinusoidally perturbed circle-map family**, including Lyapunov/entropy expansions for its absolutely continuous invariant measure and rotational averages [2]. Their results are not periodic-multiplier distributions for the maximal-entropy ensemble and do not imply the stated critical joint law by direct substitution. Parameter response of periodic-orbit formulas and transfer operators has substantial earlier literature, including Jézéquel [3] and Pollicott--Vytnova [4]. The exact curvature and crossover should therefore not be construed as inventing perturbative linear response or the fixed-map CLT.

## Limitations

The theorem is restricted to integer degrees, the specified sine perturbation, uniform sampling of **all** period-dividing-\(n\) fixed points, and fixed \(\tau\). It does not quantify convergence rates in the triangular-array CLT, extend uniformity to \(b\to\infty\), or establish the same explicit coefficients for arbitrary perturbing observables. A previously published equivalent critical-scaling limit formulated in thermodynamic formalism or local asymptotic normality cannot be ruled out solely by these searches; bibliographic priority requires independent checking. Neither the accompanying finite verifier nor the available bibliographic search constitutes external certification.

## References

[1] K. Drach, Z. Fu, V. Kaloshin, Z. Li, and C. Liverani, *Normal distribution of Lyapunov exponents of periodic orbits for expanding circle maps*, arXiv:2511.15662 (first publicly available 2025-11-19), https://arxiv.org/abs/2511.15662 .

[2] R. de la Llave, M. Shub, and C. Simó, *Entropy estimates for a family of expanding maps of the circle*, Discrete and Continuous Dynamical Systems B 10 (2008), 597--608, doi:10.3934/dcdsb.2008.10.597. An author-hosted manuscript is available at https://shub.ccny.cuny.edu/articles/2008-Entropy_estimates_for_a_family_of_expanding_maps_of_the_circle.pdf .

[3] M. Jézéquel, *Parameter regularity of dynamical determinants of expanding maps of the circle and an application to linear response*, Discrete and Continuous Dynamical Systems 39 (2019), 927--958, doi:10.3934/dcds.2019039.

[4] M. Pollicott and P. Vytnova, *Linear response and periodic points*, Nonlinearity 29 (2016), 3047--3069, https://wrap.warwick.ac.uk/id/eprint/81577/ .
