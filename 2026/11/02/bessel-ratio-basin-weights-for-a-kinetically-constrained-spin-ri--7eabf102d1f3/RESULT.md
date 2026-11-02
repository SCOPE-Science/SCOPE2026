# Bessel-ratio basin weights for a kinetically constrained spin ring

## Finding

Consider the continuous-time spin system below, with an arbitrary independent initial density and two positive flip rates. Its all-empty absorption probability has an exact generating function and a sharp exponential finite-size asymptotic. Write \(p\in(0,1)\) for the initial occupied-site probability, \(q=1-p\), and \(\theta=\lambda/\mu>0\) for the activation-to-removal rate ratio. For each cycle length \(L\ge3\), let \(b_L(p,\theta)\) be the probability of ultimately visiting the all-empty configuration.

Set
\[
\alpha=\frac{\theta}{1+\theta},\qquad
\beta=\frac{\theta}{(1+\theta)^2},\qquad
A_{\theta}(z)=
\frac{{}_0F_1(;1+\alpha;-\beta z)}{{}_0F_1(;\alpha;-\beta z)}.
\]
Here \({}_0F_1(;c;z)=\sum_{k\ge0}z^k/[(c)_k k!]\) and \((c)_k\) is the rising factorial. The analytic germ at zero satisfies \(A_{\theta}(0)=1\). The full ring-size generating function is
\[
\boxed{\quad
\sum_{L\ge3}b_L(p,\theta)x^L
=1- x\frac{d}{dx}\log\bigl(1-qx A_{\theta}(pqx^2)\bigr)
+\frac{2pqx^2}{1+\theta}\bigl(A_{\theta}(pqx^2)-1\bigr)
-1-qx-q^2x^2.
\quad}
\]
All equalities are equalities of formal power series and of analytic functions near zero. The subtraction removes the artificial size-zero, size-one and size-two coefficients; the un-subtracted expression has coefficients \(1,q,q^2\) in degrees \(0,1,2\).

There is a unique positive \(R=R(p,\theta)\), before the first positive pole of the Bessel ratio after substitution, satisfying
\[
\boxed{\quad qR A_{\theta}(pqR^2)=1.\quad}
\]
For every fixed \(p\in(0,1)\) and \(\theta>0\) there exists \(r>R\) such that
\[
\boxed{\quad b_L(p,\theta)=R^{-L}+O(r^{-L})\quad (L\to\infty).\quad}
\]
In particular, the exponential basin-weight rate is exactly \(\Lambda(p,\theta)=R(p,\theta)^{-1}\), and the leading amplitude is one rather than an unspecified prefactor. When \(\lambda=\mu\), the ratio reduces to \(A_1(z)=\tan\sqrt z/\sqrt z\), and the general equation becomes the explicit density-dependent law
\[
\boxed{\quad\Lambda(p,1)=\frac{\sqrt{p(1-p)}}{\arctan\sqrt{p/(1-p)}}.\quad}
\]
For instance \(\Lambda(1/2,1)=2/\pi\). This special case is an illustration of the two-parameter result, not its entire statement.

## Assumptions and scope

Each vertex of the labelled cycle \(C_L\), \(L\ge3\), carries \(\eta_i\in\{0,1\}\). Independently, initially \(\Pr(\eta_i=1)=p\). The only permitted transitions, each at the stated **total per-site** rate, are:

- \(1\to0\) at rate \(\mu>0\) when **both** neighboring spins are zero (removal of an isolated excitation).
- \(0\to1\) at rate \(\lambda>0\) when **at least one** neighboring spin is one (facilitated excitation, counted once whether one or two neighbors are excited).

All other flips have zero rate. A pair of adjacent occupied sites is permanently frozen: neither member can be removed, even though other sites might still evolve. Thus visiting all zeros is equivalent to the history having no facilitated excitation at all and eventually removing every original occupied site. The statement concerns absorption probability, not mean absorption time, and allows no thermal leakage or other positive-temperature flips. Divide the generator by \(\mu\) to use removal rate one and activation rate \(\theta\).

The mathematical-physics classification is 82C20: stochastic dynamics and metastability of constrained lattice-spin systems.

## Proof

**1. Alternating-block first-step recurrence.** Any initial adjacent pair of ones makes the target unreachable, so only independent occupied sets contribute. A nonempty independent configuration breaks into maximal alternating blocks \(1,01,\ldots,01\), separated by at least two zeros. For a block with \(m\ge1\) occupied sites and a zero reservoir at each end, let \(a_m\) be the probability that every occupied site is removed before any facilitated activation, with \(a_0=1\). There are \(m\) allowed removals and \(m+1\) distinct zero sites that could activate (the internal \(m-1\) zeros and the two exterior zeros). A removal at occupied site \(j\) creates two independent alternating subblocks with \(j-1\) and \(m-j\) occupied sites, with the removed site and its neighboring zeros serving as separators. The strong Markov property and exponential clocks therefore give
\[
\bigl((1+\theta)m+\theta\bigr)a_m
=\sum_{j=1}^{m}a_{j-1}a_{m-j},\qquad m\ge1.
\]
The same decomposition applies even when multiple blocks are present, because every successful history excludes all activation events and all remaining removal clocks, and activation hazards belong to disjoint blocks. Consequently successful block probabilities multiply. In particular \(a_m>0\), and the coefficients are computed uniquely by this recurrence.

**2. The Bessel-ratio generating function.** Write \(A(z)=\sum_{m\ge0}a_m z^m\). Multiplying the recurrence by \(z^m\) and summing gives the Riccati equation
\[
(1+\theta)zA'(z)+\theta(A(z)-1)=zA(z)^2,
\qquad A(0)=1.
\]
Let \(F(z)={}_0F_1(;\alpha;-\beta z)\). Its hypergeometric differential equation is \(zF''+\alpha F'+\beta F=0\); termwise differentiation gives \(F'=-(1+\theta)^{-1}{}_0F_1(;1+\alpha;-\beta z)\). Hence \(A=-(1+\theta)F'/F\) satisfies that Riccati equation and has constant term one. Coefficient uniqueness proves the claimed formula for \(A_{\theta}\).

**3. Exact cyclic enumeration, including the exceptional alternating ring.** For an alternating block with \(m\ge1\) occupied sites, the Bernoulli-weighted word has length \(2m-1\) and weight \(p^mq^{m-1}a_m\). Its word generating function is
\[
C(x)=\sum_{m\ge1}p^m q^{m-1}a_m x^{2m-1}
=\frac{A(pqx^2)-1}{qx}.
\]
A gap of at least two zero sites has generating function \(G(x)=(qx)^2/(1-qx)\). On a labelled cyclic word containing \(j\ge1\) alternating blocks, division by \(j\) accounts for which block is marked, and \(x\,d/dx\) restores the distinguished labelled starting site. Thus all nonempty independent cyclic words containing a two-zero gap contribute
\[
-x\frac{d}{dx}\log(1-C(x)G(x)).
\]
Together with the all-zero words, whose contribution is \(1/(1-qx)\), use \(1-CG=(1-qx A(pqx^2))/(1-qx)\) to reduce the sum to
\[
1-x\frac{d}{dx}\log(1-qx A(pqx^2)).
\]
The only independent cyclic configurations without a two-zero gap are the two strictly alternating configurations on an even cycle \(L=2m\) with \(m\ge2\). Their first event must be one of \(m\) removals before any of \(m\) possible activations, with probability \(1/(1+\theta)\). Afterward an ordinary alternating block of \(m-1\) occupied sites remains; its success probability is \(a_{m-1}\). Their total contribution is
\[
\sum_{m\ge2}\frac{2(pq)^m a_{m-1}x^{2m}}{1+\theta}
=\frac{2pqx^2}{1+\theta}\bigl(A(pqx^2)-1\bigr).
\]
Remove the artificial coefficients in sizes zero, one and two to obtain the displayed formula for all \(L\ge3\). No infinite-size or independence approximation is used here.

**4. A unique dominant pole and its coefficient.** Let \(\alpha\in(0,1)\) and \(\beta>0\) as above. The standard identity
\[
{}_0F_1(;\alpha;-\beta z)
=\Gamma(\alpha)(\beta z)^{(1-\alpha)/2}
J_{\alpha-1}(2\sqrt{\beta z})
\]
shows that \(F\) has a first strictly positive simple zero \(s_0\); the positive zeros are \(j_{\alpha-1,k}^2/(4\beta)\). The standard real-zero theorem for \(J_\nu\) with \(\nu>-1\) ensures these are the nearest complex zeros as well. Since \(F'=-{}_0F_1(;1+\alpha;-\beta z)/(1+\theta)\) and \(F'\ne0\) at a simple zero, \(A\) has a positive simple pole at \(s_0\). Its Taylor coefficients are strictly positive. Therefore \(f(x)=qx A(pqx^2)\) is strictly increasing from zero to infinity for \(0<x<\sqrt{s_0/(pq)}\), giving a unique \(R\) there with \(f(R)=1\).

The coefficients of \(f\) at powers one and three are strictly positive. If \(|z|=R\) and \(f(z)=1\), then \(1=|f(z)|\le f(R)=1\). Equality forces every nonzero monomial of \(f(z)\) to have phase zero; the positive first-degree coefficient forces \(z=R\). Consequently the logarithmic derivative has exactly one singularity on its circle of convergence. Since \(f'(R)>0\),
\[
\frac{xf'(x)}{1-f(x)}=\frac{1}{1-x/R}+O(1)
\]
near \(x=R\). The correction \(A(pqx^2)\) is analytic there. Isolated meromorphic singularities and the strict circle argument permit some \(r>R\) for which subtraction of \(1/(1-x/R)\) leaves a function analytic throughout \(|x|<r\). Cauchy's coefficient estimate yields \(b_L=R^{-L}+O(r^{-L})\), proving both the rate and unit amplitude.

**5. Equal-rate specialization.** At \(\theta=1\) we have \(\alpha=1/2\) and \(\beta=1/4\), so the two hypergeometric functions are \(\sin\sqrt z/\sqrt z\) and \(\cos\sqrt z\). Thus \(A_1(z)=\tan\sqrt z/\sqrt z\). On the interval before the first tangent pole, the root equation becomes \(\tan(\sqrt{pq}R)=\sqrt{p/q}\), giving \(R=\arctan\sqrt{p/q}/\sqrt{pq}\), as asserted.

## Verification

A standalone standard-library Python program, `VERIFY.py`, derives finite-size probabilities independently from the full \(2^L\)-state first-step absorption equations and compares them **exactly as rational numbers** with coefficients of the claimed generating function. Five pairs of rational \((p,\theta)\) were checked at cycle sizes \(L=3,\ldots,10\), for 40 exact finite-state equalities; 90 exact alternating-block Riccati-coefficient identities and 40 probability bounds were also tested, along with four equal-rate exponent bounds: 174 checks in total. Run `python VERIFY.py` in the same directory. The analytic proof—not the finite checks—establishes the theorem for arbitrary positive parameters and all lengths.

Independent high-precision evaluations of the Bessel-ratio root produced \(\Lambda(1/2,1)\approx0.63661977236758\), \(\Lambda(2/5,2/3)\approx0.74294297389243\), and \(\Lambda(3/4,3/2)\approx0.38264245528358\). These are supplementary numerical cross-checks, not interval certificates.

## Relationship to prior work

Marić, Garrahan and Zadnik (2026) study metastable time-scale hierarchies and excitation-facilitated single-spin-flip generators in the East and Fredrickson–Andersen chains. Their general setting motivates a quantitative finite-size question about constrained kinetic basins, but their detailed-balance models and relaxation observables do not identify the two-rate irreversible all-empty basin probability computed here. Krapivsky and Luck (2022/2023), and the earlier Godrèche–Luck (2004) review, rigorously develop attractor statistics in constrained Ising chains, including descending dynamics with isolated spins of both signs flipping and a random-sequential-adsorption representation. Those dynamics, target observable and enumeration differ: here an activation of any zero adjacent to a one creates a permanent occupied pair and rules out all-empty absorption. A subsequently released special-case analysis by Cao, Jiang and Zhang (arXiv:2610.36829v1, first made public on 2026-10-27) evaluates the unbiased, equal-flip-rate exponent \(2/\pi\) in a corresponding kinetic sector using Euler zigzag numbers. That particular exponent is therefore **prior work**, not asserted to be new. Its Appendix B does not give the two-variable Bernoulli-density/rate-ratio Bessel generating function, unique-pole equation or all-length probability law stated here. The result is not an inference from the existence of metastable plateaus or the older adsorption formulas; the stated exact finite-cycle identity and its Bessel pole are derived specifically for this two-rate generator.

## Limitations

This classification is restricted to the specified irreversible generator and independent Bernoulli initial configurations on labelled cycles of length at least three; it does not describe other kinetic spin constraints, finite-temperature leakage, characteristic absorption times, the whole blocked-state distribution, or an infinite-volume interacting-particle evolution. The unique leading singularity result uses the usual real-zero theorem for Bessel functions of real order greater than minus one. An independently conducted mathematical audit and a definitive global publication-priority assessment have not been performed; potential coverage by a broader stochastic-adsorption theorem remains a research risk. The numerical tests are finite, not a proof of the infinite-size asymptotic.

## References

1. V. Marić, J. P. Garrahan and L. Zadnik, *Hierarchy of time scales in kinetically constrained models via stochastic-generator expansion*, arXiv:2609.18882v1 (first submitted 2026-09-16), https://arxiv.org/abs/2609.18882 .
2. P. L. Krapivsky and J. M. Luck, *Jamming and metastability in one dimension: from the kinetically constrained Ising chain to the Riviera model*, arXiv:2211.12815v1 (2022), https://arxiv.org/html/2211.12815v1 .
3. C. Godrèche and J. M. Luck, *Metastability in zero-temperature dynamics: Statistics of attractors*, arXiv:cond-mat/0412077v1 (2004), https://arxiv.org/pdf/cond-mat/0412077 .
4. D. Cao, W. Jiang and Y. Zhang, *Kinetic Sectors and Nonequilibrium Dynamics in the \(\delta\)-Ising Model*, arXiv:2610.36829v1 (first submitted 2026-10-27), https://arxiv.org/abs/2610.36829 .
5. NIST Digital Library of Mathematical Functions, §10.21 (zeros of Bessel and Hankel functions) and §16.2 (generalized hypergeometric functions), https://dlmf.nist.gov/10.21 and https://dlmf.nist.gov/16.2 .
