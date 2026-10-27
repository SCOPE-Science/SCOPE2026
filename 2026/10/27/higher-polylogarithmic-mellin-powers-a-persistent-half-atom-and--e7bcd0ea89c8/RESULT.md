# Higher polylogarithmic Mellin powers: a persistent half atom and sharp endpoint laws

## Finding

Let \(\eta=(\delta_0+\delta_1)/2\), and let \(\mathcal M_2\) denote the order-two Markov–Krein (Dirichlet-mean) transform. Define \(\mu_1=\eta\) and, for every integer \(k\ge2\), the order-two multiplicative-convolution power \(\mu_k=\eta^{\otimes_2 k}\). Equivalently, \(\mathcal M_2\mu_k\) is the distribution of a product of \(k\) independent uniform random variables on \((0,1)\). Existence and uniqueness of the multiplicative convolution are supplied by the established closure theorem [1].

For every integer \(k\ge3\), the **ordinary Cauchy transform** of \(\mu_k\) is
\[
H_k(z):=\int_{[0,1]}\frac{\mu_k(dx)}{z-x}
=\frac{1}{2z}\left(1+\frac{\operatorname{Li}_{k-2}(1/z)}{\operatorname{Li}_{k-1}(1/z)}\right),\qquad z\in\mathbb C\setminus[0,1],
\]
where the polylogarithms use the branch obtained by analytic continuation from \(z>1\). The measure has **exactly one atom**, of mass \(1/2\) at zero, and is otherwise absolutely continuous on \((0,1)\), with density
\[
h_k(x)=-\frac{1}{2\pi x}\operatorname{Im}\frac{\operatorname{Li}_{k-2}(1/x-\mathrm i0)}{\operatorname{Li}_{k-1}(1/x-\mathrm i0)},\qquad 0<x<1.
\]
There is no atom at one. The second power serves only as a known comparison case, discussed below; the claim assessed here is the all-power classification for \(k\ge3\).

Every higher-power positive component has the sharp left-end asymptotic
\[
h_k(x)\sim\frac{k-1}{2x\log^2(1/x)}\quad(x\downarrow0),\qquad k\ge3.
\]
At the right endpoint the exponent changes with the power:
\[
h_k(x)\sim\frac{[\log(1/x)]^{k-3}}{2(k-3)!\,\zeta(k-1)}\ (k\ge3),\qquad x\uparrow1.
\]
The first two raw moments, for all \(k\ge3\), are exactly
\[
\int x\,\mu_k(dx)=2^{-k},\qquad
\int x^2\,\mu_k(dx)=3^{1-k}-2^{1-2k}.
\]
Thus each finite convolution power retains the same half atom at zero, despite its mean tending to zero as the power grows. The continuous component always has total mass \(1/2\) and changes its endpoint behavior with \(k\).

## Assumptions and scope

The Dirichlet-process concentration parameter is exactly \(2\). The base law \(\eta\) is supported equally at \(0\) and \(1\), and the assessed powers are integers \(k\ge3\). A polylogarithm \(\operatorname{Li}_s(w)\) means the analytic continuation of \(\sum_{n\ge1}w^n/n^s\). Boundary values \(1/x-\mathrm i0\) are approached from the lower half-plane, corresponding to \(z=x+\mathrm i0\). The above support, atoms, densities, and asymptotic statements concern the unique probability laws \(\mu_k\) given by [1], not arbitrary transforms.

## Proof

**1. Product-uniform representation and analytic transform.** The weight at \(1\) of an order-two Dirichlet process with base \(\eta\) is \(\operatorname{Beta}(1,1)\), hence uniform. By multiplicative closure and injectivity [1, Theorem 1.4(ii) and Proposition 1.2], \(\mathcal M_2\mu_k\) is the law of \(P_k=\prod_{j=1}^k U_j\) with independent \(U_j\sim\operatorname{Unif}(0,1)\). The established compact-support lemma [1, Lemma 3.1(i)] puts \(\mu_k\) in \([0,1]\). For \(|z|>1\), expansion of the second-order Cauchy kernel gives
\[
G_k(z):=\mathbb E(z-P_k)^{-2}
=\sum_{n\ge0}\frac{(n+1)\mathbb E P_k^n}{z^{n+2}}
=\sum_{n\ge0}\frac1{(n+1)^{k-1}z^{n+2}}
=\frac{\operatorname{Li}_{k-1}(1/z)}{z},
\]
since \(\mathbb E P_k^n=(n+1)^{-k}\). The Markov–Krein identity [1, Proposition 1.2] states \(G_k(z)=\exp[-2\int\log(z-x)\mu_k(dx)]\). Differentiating yields \(H_k=-G'_k/(2G_k)\). The polylogarithm differentiation rule \(w(\operatorname{Li}_{s})'(w)=\operatorname{Li}_{s-1}(w)\) gives the asserted quotient; analytic continuation extends the identity to the slit plane. The nonvanishing of \(G_k\) away from the real support follows directly from its exponential representation.

**2. Interior density and absence of interior singular mass.** For every integer \(s\ge1\) and real \(r>1\), the lower-side boundary value satisfies \(\operatorname{Im}\operatorname{Li}_s(r-\mathrm i0)=-\pi(\log r)^{s-1}/(s-1)!\). In particular, the denominator \(\operatorname{Li}_{k-1}(r-\mathrm i0)\) never vanishes. The boundary value of \(H_k\) is consequently continuous and real-analytic on every compact subinterval of \((0,1)\). Local Stieltjes inversion identifies the density \(h_k=-\operatorname{Im} H_k(x+\mathrm i0)/\pi\) and precludes singular mass on those intervals.

**3. Endpoint masses.** The atom at zero is \(\lim_{t\downarrow0}[-tH_k(-t)]\). For \(k=2\), \(\operatorname{Li}_0(-1/t)/\operatorname{Li}_1(-1/t)\to0\); for \(k\ge3\), both polylogarithms have large-negative-argument expansions whose quotient is \(O(1/\log(1/t))\). Therefore the atom is exactly \(1/2\). Likewise \(\lim_{t\downarrow0}tH_k(1+t)=0\): for \(k=2\) the possible \(1/t\) pole is divided by a diverging logarithm; for \(k=3\) the quotient grows only logarithmically; for \(k\ge4\) it is bounded. There is no atom at one. Since the interior is absolutely continuous, the stated decomposition is complete.

**4. Comparison with the established second-power density.** Write \(r=1/x>1\) and \(L=\log((1-x)/x)\). As \(\operatorname{Li}_0(r)=1/(x-1)\) and \(\operatorname{Li}_1(r-\mathrm i0)=-L-\mathrm i\pi\), the benchmark density simplifies to \(1/[2x(1-x)(L^2+\pi^2)]\). This benchmark is also obtained by squaring the symmetric additive-convolution distribution in [2] and adding a half atom at zero, so it is not an independently new part of the claim. Substituting \(t=\log((1-x)/x)\) shows that the positive component has mass \(1/2\) and its conditional logit has density \(1/(t^2+\pi^2)\), a Cauchy density of scale \(\pi\).

**5. Endpoint laws.** Let \(y=\log(1/x)\to\infty\). The large-argument polylogarithm expansions, obtainable by integrating \(d\operatorname{Li}_s(e^y)/dy=\operatorname{Li}_{s-1}(e^y)\) from the elementary \(\operatorname{Li}_1\), are
\[
\operatorname{Re}\operatorname{Li}_s(e^y-\mathrm i0)=-\frac{y^s}{s!}+O(y^{s-2}),\quad
\operatorname{Im}\operatorname{Li}_s(e^y-\mathrm i0)=-\frac{\pi y^{s-1}}{(s-1)!},\quad s\ge1,
\]
with the obvious direct treatment of \(s=1\). These imply
\(\operatorname{Im}[\operatorname{Li}_{k-2}/\operatorname{Li}_{k-1}](e^y-\mathrm i0)\sim-\pi(k-1)/y^2\) for \(k\ge3\); the \(k=2\) case follows explicitly. At \(x\uparrow1\), \(\operatorname{Li}_{k-1}(1/x-\mathrm i0)\to\zeta(k-1)>0\) for \(k\ge3\), while the exact imaginary jump of the numerator is \(-\pi[\log(1/x)]^{k-3}/(k-3)!\). The term from the denominator's imaginary jump is of smaller order (including the logarithmically growing numerator when \(k=3\)). The asserted right-end asymptotic follows; \(k=2\) is immediate from its explicit formula.

**6. Moments.** The Laurent expansion of \(H_k=-G'_k/(2G_k)\) at infinity gives the first moment \(2^{-k}\). Its next coefficient equals \(3\mathbb E P_k^2-2(\mathbb E P_k)^2=3^{1-k}-2^{1-2k}\), proving the two moment identities.

## Verification

The accompanying standalone program `verify.py` (dependency stated in `requirements.txt`) was executed against the exact formulas. It passed 45 deterministic high-precision checks: ordinary Cauchy transform against direct integration for the second power at three exterior points; its first three exact moments; positive values of the proposed densities at 30 points; five left-end and four right-end asymptotic comparisons. These finite evaluations are consistency tests only. The analytic arguments above establish the statements for every integer power.

## Relationship to prior work

Mergny [1] proves general existence, uniqueness, support control, and the logarithmic-derivative method for order-\(c\) multiplicative convolution; those ingredients are not new here. The contribution assessed here is the **whole higher-power hierarchy \(k\ge3\)**: closed polylogarithmic inversions, an exactly persistent half atom, and the exponent-changing edge classification. Crucially, the logistic–Cauchy formula for \(k=2\) is **already implied by** Mergny's 2022 **additive** Bernoulli self-convolution [2]. Indeed, if \(V\) has the even density given in [2, Eq. (12)] at parameter \(c=2\), then squaring yields density \(1/[x(1-x)(\log^2((1-x)/x)+\pi^2)]\); the earlier benchmark \(\mu_2\) equals \(\tfrac12\delta_0+\tfrac12\mathcal L(V^2)\). That known special case is not claimed new, nor does the additive two-fold calculation supply the \(k\ge3\) quotient family or the changing endpoint exponents. James [3] proves beta-scaling identities for Dirichlet means; such identities provide alternative representations of products with beta factors but do not state the all-power polylogarithmic measure and endpoint law here. Lijoi and Regazzini [4] provide the foundational Markov–Krein inversion rather than this specific hierarchy. As in all explicit examples derived from a general transform theorem, an unnoticed earlier evaluation through alternative special-function identities remains possible.

## Limitations

The assessed higher-power result does not address noninteger powers, unequal Bernoulli weights, orders other than \(2\), or random-matrix realizations of the multiplicative operation. The terminology 'high-temperature' refers solely to the established transform-based convolution, without claiming its proposed random-matrix interpretation is proven. The program requires `mpmath` and checks finite samples only.

## References

[1] P. Mergny, *Stability of the Markov-Krein Transform Under Classical Convolutions*, arXiv:2610.18436v1 (first public 2026-10-13), https://arxiv.org/abs/2610.18436 . Theorem 1.4(ii), Proposition 1.2, Lemma 3.1 and Equation (3.3).

[2] P. Mergny, *An explicit example for the high temperature convolution: crossover between the binomial law B(2,1/2) and the arcsine law*, arXiv:2204.07744 (2022), https://arxiv.org/abs/2204.07744 .

[3] L. F. James, *Dirichlet mean identities and laws of a class of subordinators*, Bernoulli 16 (2010), arXiv:1010.1639, https://arxiv.org/abs/1010.1639 . Section 2, beta-scaling identities.

[4] A. Lijoi and E. Regazzini, *Means of a Dirichlet process and multiple hypergeometric functions*, Annals of Probability 32 (2004), arXiv:math/0410151, https://arxiv.org/abs/math/0410151 .
