# Inverse-prevalence optimal pools for positively correlated disease screening

## Finding

Consider two-stage Dorfman disease screening with perfect pooled and individual assays and groups of equal integer size \(k\ge2\). For each group, conditional on its unobserved infection probability \(\Theta\), the infection indicators are independent Bernoulli variables, where \(\Theta\sim\operatorname{Beta}(a,\tau-a)\), \(\tau>0\), and \(0<a<\min\{1,\tau\}\). The marginal prevalence is \(p=a/\tau\), and the within-group pairwise infection correlation is \(1/(\tau+1)\). The expected number of assays per individual is

\[
 C_k(a,\tau)=\frac1k+1-Q_k(a,\tau),\qquad
 Q_k(a,\tau)=\prod_{j=0}^{k-1}\frac{\tau-a+j}{\tau+j}.
\]

**Theorem.** For every \(\tau>0\) and \(0<a<\min\{1,\tau\}\), the sequence \((C_k)_{k\ge2}\) decreases to its minimum and then increases, with at most two adjacent minimizing integers. In particular, the exact comparison between successive group sizes is

\[
 C_{k+1}-C_k=\frac{R_k-1}{k(k+1)},\qquad
 R_k=\frac{a k(k+1)Q_k}{\tau+k},\qquad
 \frac{R_{k+1}}{R_k}=1+\frac{(1-a)k+2(\tau-a)}{k(\tau+k+1)}>1.
\]

Fix \(\tau>0\). As \(p\downarrow0\), **every** optimal integer group size \(k_*(p)\) satisfies the sharp law

\[
 \boxed{\tau p\,k_*(p)\longrightarrow1}.
\]

Its minimum cost has the two-term asymptotic expansion

\[
 \boxed{\min_{k\ge2} C_k(\tau p,\tau)
 =\tau p\Bigl[\log\frac1{\tau p}+1-\psi(\tau)\Bigr]+o(p)},
\]

where \(\psi=\Gamma'/\Gamma\) is the digamma function. Direct individual screening costs one assay per individual and is suboptimal for all sufficiently small \(p\). By comparison, with independent Bernoulli infection indicators of prevalence \(p\), the same two-stage protocol has optimal group size asymptotic to \(p^{-1/2}\) and minimum cost asymptotic to \(2\sqrt p\). Thus fixed positive within-pool correlation changes both rare-prevalence scaling exponents.

## Assumptions and scope

Each tested pool is formed from a cluster of \(k\) exchangeable individuals with the stated beta-mixture law. The concentration \(\tau\), hence correlation, remains constant while \(p\) tends to zero. A new latent \(\Theta\) may be drawn independently for different pools; dependence across pools does not affect the expectation for one pool. The pool assay returns positive exactly when at least one individual is infected. A negative pool is cleared; every member of a positive pool receives an individual assay. The cost counts pooled and reflex individual assays, with equal costs and no dilution, false positives, false negatives, or fixed upper bound on \(k\). Large enough clusters must be available to support growing optimal sizes. Individual testing (without a redundant retest) is represented separately by cost \(1\).

The exact unimodality conclusion assumes \(0<a<1\); this holds automatically for all sufficiently small \(p\) at any fixed \(\tau\). The theorem does not assert this unimodality for arbitrary larger beta shape parameters.

## Proof

**Negative-pool probability.** Conditional on \(\Theta\), all \(k\) specimens are negative with probability \((1-\Theta)^k\). Integrating against the beta density yields

\[
 Q_k=\frac{B(a,\tau-a+k)}{B(a,\tau-a)}
 =\frac{(\tau-a)_k}{(\tau)_k}.
\]

A pool uses one first-stage test and either zero or \(k\) second-stage tests, so its expected cost divided by \(k\) is exactly \(C_k=1/k+1-Q_k\). Since \(Q_{k+1}=Q_k(\tau-a+k)/(\tau+k)\), subtraction gives

\[
 C_{k+1}-C_k=-\frac1{k(k+1)}+\frac{a Q_k}{\tau+k}.
\]

**Exact location and uniqueness.** Define \(R_k\) as in the finding. Direct cancellation in its product gives

\[
 \frac{R_{k+1}}{R_k}=
 \frac{(k+2)(\tau-a+k)}{k(\tau+k+1)}
 =1+\frac{k(1-a)+2(\tau-a)}{k(\tau+k+1)}.
\]

All extra numerator terms are strictly positive under \(0<a<\min\{1,\tau\}\). Thus \(R_k\) is strictly increasing. Moreover, the gamma-ratio asymptotic

\[
 Q_k=\frac{\Gamma(\tau)}{\Gamma(\tau-a)}
 \frac{\Gamma(k+\tau-a)}{\Gamma(k+\tau)}
 \sim\frac{\Gamma(\tau)}{\Gamma(\tau-a)}k^{-a}
\]

implies \(R_k\sim a\Gamma(\tau)k^{1-a}/\Gamma(\tau-a)\to\infty\) because \(a<1\). Hence the signs of consecutive differences are initially negative, if any, then may be zero at one index, and thereafter are positive. The minimizing integers are either one integer or two consecutive integers. This includes the boundary possibility of a minimum at \(k=2\).

**Rare-prevalence position.** Now hold \(\tau\) fixed and send \(a=\tau p\downarrow0\). For any fixed \(c>0\), let \(k=\lfloor c/a\rfloor\). For small \(a\), uniformly in all positive integers \(k\), Taylor expansion of the logarithm gives

\[
 \log Q_k=-a\sum_{j=0}^{k-1}\frac1{\tau+j}+O_\tau(a^2),
\]

because \(\sum_{j\ge0}(\tau+j)^{-2}<\infty\). For \(k\asymp1/a\), the harmonic sum equals \(\log k-\psi(\tau)+o(1)\), so \(Q_k=1+o(1)\). Consequently

\[
 R_{\lfloor c/a\rfloor}
 =a\lfloor c/a\rfloor\,
 \frac{\lfloor c/a\rfloor+1}{\tau+\lfloor c/a\rfloor}
 Q_{\lfloor c/a\rfloor}\longrightarrow c.
\]

For any \(0<c_-<1<c_+\), strict increase of \(R_k\) implies, for sufficiently small \(a\), that every minimizing \(k_*\) lies between \(\lfloor c_-/a\rfloor\) and \(\lceil c_+/a\rceil+1\). Letting \(c_-\uparrow1\) and \(c_+\downarrow1\) proves \(a k_*\to1\).

**Cost constant.** At every minimizing index, \(k_*\sim1/a\). The same uniform logarithmic expansion and the digamma identity yield

\[
 \sum_{j=0}^{k_*-1}\frac1{\tau+j}
 =\psi(\tau+k_*)-\psi(\tau)
 =\log\frac1a-\psi(\tau)+o(1).
\]

Since \(a\log(1/a)\to0\), the exponential remainder satisfies

\[
 1-Q_{k_*}
 =a\Bigl[\log\frac1a-\psi(\tau)\Bigr]+o(a).
\]

Also \(1/k_*=a+o(a)\), giving the stated two-term expansion. In particular the cost tends to zero, so it eventually improves upon direct individual testing.

**Independence comparison.** If infection indicators are independent Bernoulli with prevalence \(p\), then \(C_k^{\mathrm{iid}}=1/k+1-(1-p)^k\). Choosing \(k=\lfloor p^{-1/2}\rfloor\) shows the minimum is at most \(2\sqrt p+o(\sqrt p)\). For an optimizing \(k\), the inequalities \(1/k\le C_k^{\mathrm{iid}}\) and \(1-(1-p)^k\le C_k^{\mathrm{iid}}\) force \(k=\Theta(p^{-1/2})\). Expanding uniformly on this scale gives

\[
 \frac{C_k^{\mathrm{iid}}}{\sqrt p}=
 \frac1{k\sqrt p}+k\sqrt p+o(1).
\]

The unique minimum of \(x^{-1}+x\) on \((0,\infty)\) is \(2\) at \(x=1\), proving both independent-model limits.

## Verification

The self-contained Python 3 program `verify.py` uses exact rational arithmetic to independently test the negative-pool probability recurrence, the adjacent-cost identity, and the monotonic-ratio identity in 168 configurations spanning six beta parameter choices. Its additional numerical calculations exhibit the approach of \(a k_*\) to one at fixed \(\tau=1\) and contrast the independent scaling. The script was executed against its actual distributed content. These finite tests check algebra and sample cases only; the infinite asymptotic follows from the preceding proof.

For illustration, at \(\tau=1\), marginal prevalence \(p=1/20\), \(1/100\), and \(1/1000\), the exact adjacent-sign computation places the minima at integer pool sizes \(25\), \(106\), and \(1008\), respectively (the limiting scale is \(1/p\)).

## Relationship to prior work

Lendle, Hudgens, and Qaqish (2010 technical report; online 2011; Biometrics 2012) study precisely the beta-binomial exchangeability mechanism and calculate the efficiency of grouped hierarchical and matrix disease screening. Their underlying probability model and the fact that correlation can help pooling are **not** new claims here. The contribution here is the exact integer adjacent-comparison threshold for the unlimited-pool two-stage case and, especially, the sharp fixed-correlation rare-prevalence asymptotics, including the constant in the minimum expected assay count.

Augenblick, Kolstad, Obermeyer, and Wang (2020) explicitly explain and numerically exhibit that intrapool correlation leads to larger efficient groups and fewer tests. Their correlated-risk examples do not state or establish the beta-mixture fixed-concentration \(p\downarrow0\) limit here. Landolfi and Lall (2023 preprint) derive a general optimization framework for exchangeable binary specimens; its exact finite-pool objective specializes to the present model, but an algorithm for optimizing finite partitions is not, by itself, the proved asymptotic coefficient, exponent transition, or unique adjacent-threshold law. The specializations and containment risks are explicitly acknowledged rather than dismissed on differing terminology.

An inaccessible but very closely related primary source is Lendle et al.'s full manuscript: an authorized preprint download was unavailable and a lawful institutional request did not supply its text. Its abstract, specified beta-binomial model, and subsequent descriptions were considered. The possibility that its unretrieved appendix already derives the asserted asymptotic remains a material originality risk. Searches and the inspected full-text primary works did not establish such prior coverage; absence of an accessible match is not a proof of historical novelty.

## Limitations

The theorem optimizes **expected assay count**, not detection sensitivity, prevalence-estimation precision, time to screening, or infections prevented. It assumes error-free nondiluting assays, equal assay costs, homogeneous exchangeable pools, fixed beta concentration, and no laboratory or cluster-size constraint. With an upper cap on pool size independent of \(p\), the inverse-prevalence asymptotic is not implementable. If the correlation decreases along with prevalence, another scaling regime may arise and is not classified here. The uninspected Lendle full text leaves a genuine prior-coverage uncertainty. Independent scientific audit has not been performed.

## References

1. S. D. Lendle, M. G. Hudgens, and B. F. Qaqish, *Group Testing for Case Identification with Correlated Responses*, University of North Carolina technical report (2010); *Biometrics* 68 (2012), 532–540, first journal online September 27, 2011. DOI: 10.1111/j.1541-0420.2011.01674.x.
2. N. Augenblick, J. T. Kolstad, Z. Obermeyer, and A. Wang, *Group Testing in a Pandemic: The Role of Frequent Testing, Correlated Risk, and Machine Learning*, NBER Working Paper 27457 (July 2020). DOI: 10.3386/w27457.
3. N. C. Landolfi and S. Lall, *Optimal Dorfman Group Testing for Symmetric Distributions*, arXiv:2308.11050 (2023).
4. J. Montesinos-López et al., *Estimating a Proportion Based on Group Testing for Correlated Binary Response* (2014). DOI: 10.4172/2155-6180.1000185. This concerns estimating prevalence rather than minimizing Dorfman case-identification tests.
