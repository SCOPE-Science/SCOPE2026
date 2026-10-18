# An exact pooling-benefit phase boundary and two turning points in beta-correlated medical screening

## Finding
For two-stage Dorfman disease screening with perfectly accurate tests, take a shared latent infection probability \(P\sim\operatorname{Beta}(\alpha,\beta)\), with \(\alpha,\beta>0\); conditional on \(P\), infection indicators are independent Bernoulli variables. A uniform group of \(k\ge2\) specimens is tested once, then every constituent is individually retested only if its pool is positive. The expected number of tests **per specimen** is
\[
 C_k=1+\frac1k-\frac{(\beta)_k}{(\alpha+\beta)_k},\qquad C_1=1,
\]
where \((z)_k=z(z+1)\cdots(z+k-1)\) is the rising factorial. Write \(Q_k=(\beta)_k/(\alpha+\beta)_k\) and \(F_k=kQ_k\). The following is an exact classification over *all* integer pool sizes, without any prescribed upper size limit.

1. If \(0<\alpha<1\), some finite pool always beats individual screening. If \(\alpha=1\), some finite pool beats individual screening if and only if \(\beta>1\).
2. If \(\alpha>1\), set \(K=\max\{1,\lceil\beta/(\alpha-1)\rceil\}\). Some finite pool strictly beats individual screening **if and only if** \(F_K>1\); equality yields no strict savings. Thus this regime admits a one-integer finite test for the feasibility of savings.
3. For the pooled-size cost sequence, put
\[
 H_k=\frac{\alpha k(k+1)Q_k}{\alpha+\beta+k}.
\]
Its adjacent differences have the exact sign \(\operatorname{sgn}(C_{k+1}-C_k)=\operatorname{sgn}(H_k-1)\), for \(k\ge2\). If \(\alpha\le1\), \(H_k\) is strictly increasing; thus pooled costs decrease then increase, apart from a possible adjacent tie, or decrease toward the individual-testing baseline. If \(\alpha>1\), \(H_k\) increases and then decreases, so pooled costs have at most one local minimum followed by at most one local maximum; they can genuinely exhibit both. If pooling strictly beats \(C_1=1\), the *first* local minimum is the global optimal pooled size, apart from a possible adjacent tie.
4. The double-turn behavior occurs already at \((\alpha,\beta)=(3/2,5/2)\). The costs have a strict local minimum at \(k=5\), with \(C_5=10143/10240<1\), and a strict local maximum at \(k=29\). Moreover \(k=5\) is the unique global optimum over every integer \(k\ge1\).

## Assumptions and scope
A pool test returns positive exactly when at least one constituent is infected. The perfect-test assumption excludes dilution, contamination, false negatives, and sample-processing limits. The beta variable is common within a sampling cohort; unlimited pool-size comparisons mean arbitrarily long exchangeable sequences, not a fixed finite population with a maximum capacity. \(C_1=1\) is an individual test, not a group test followed by a redundant retest. Uniform equal-size pooling is compared with individual screening; arbitrary unequal-size partitions and adaptive multistage schemes are not optimized here. The claim is primarily a model-specific mathematical statement about medical screening resource use, not clinical guidance.

## Proof
**Expected cost.** Conditional on \(P\), the pool is negative with probability \((1-P)^k\). Integration under the beta density yields
\[
 Q_k=\mathbb E[(1-P)^k]=\frac{B(\alpha,\beta+k)}{B(\alpha,\beta)}=\frac{(\beta)_k}{(\alpha+\beta)_k}.
\]
There is one initial pool test and \(k\) retests precisely on a positive pool, giving \(C_k\). For \(k\ge2\), strictly fewer than one test per specimen is equivalent to \(Q_k>1/k\), namely \(F_k>1\).

**Global pooling-benefit boundary.** Direct cancellation gives
\[
 \frac{F_{k+1}}{F_k}=\frac{(k+1)(\beta+k)}{k(\alpha+\beta+k)},\qquad
 \operatorname{sgn}(F_{k+1}-F_k)=\operatorname{sgn}(\beta+(1-\alpha)k).
\]
Also \(F_1=\beta/(\alpha+\beta)<1\). The beta-gamma ratio yields \(Q_k\sim\Gamma(\alpha+\beta)k^{-\alpha}/\Gamma(\beta)\), so \(F_k\) diverges for \(\alpha<1\), approaches \(\beta\) for \(\alpha=1\), and approaches zero for \(\alpha>1\). For \(\alpha=1\), the exact formula \(F_k=\beta k/(\beta+k)\) establishes the boundary \(\beta>1\), including equality. For \(\alpha>1\), the ratio says \(F_k\) increases up to \(K=\max\{1,\lceil\beta/(\alpha-1)\rceil\}\) and then decreases; if the turning ratio is exactly one, \(F_K=F_{K+1}\). Therefore \(\sup_{k\ge1}F_k=F_K\), proving the finite feasibility test.

**Number and placement of turning points.** For every \(k\ge2\),
\[
 C_{k+1}-C_k=-\frac{1}{k(k+1)}+\frac{\alpha Q_k}{\alpha+\beta+k}=
 \frac{H_k-1}{k(k+1)}.
\]
The ratio
\[
 \frac{H_{k+1}}{H_k}=\frac{(k+2)(\beta+k)}{k(\alpha+\beta+k+1)}
\]
is above, equal to, or below one according as \(2\beta+(1-\alpha)k\) is positive, zero, or negative. Thus for \(\alpha\le1\), \(H_k\) is strictly increasing, and for \(\alpha>1\) it rises until \(2\beta/(\alpha-1)\) and then falls. Moreover \(H_1=2\alpha\beta/[(\alpha+\beta)(\alpha+\beta+1)]<1\). Hence the difference signs can only follow the patterns negative–positive or negative–positive–negative (allowing equality at boundary indices). In the second pattern, the descending tail tends to \(C_k\to1\) and for \(\alpha>1\) eventually \(C_k>1\) because \(Q_k=o(k^{-1})\). Therefore the descending tail cannot beat any strict pooling advantage \(C_k<1\). The only candidate for a global pooled minimum is the first local minimum, with at most two neighboring tied sizes if its change is zero. In the \(\alpha\le1\) regime there is at most one minimum directly. This proves item 3, with the caveat that for \(\alpha>1\) there may be no cost below individual testing.

**Sharp two-turn example.** At \((\alpha,\beta)=(3/2,5/2)\), the ratio of \(H\)'s rises through index \(k=10\), then falls. Exact evaluations give
\[
 H_4=\frac{495}{512}<1<H_5=\frac{2145}{2048},\qquad
 H_{28}=\frac{145207923735888321}{144115188075855872}>1>H_{29}=\frac{575174243369427765}{576460752303423488}.
\]
By unimodality these are the only crossings; therefore \(C_5\) is a strict local minimum and \(C_{29}\) is a strict local maximum. The exact value \(C_5=10143/10240<1\), plus the tail bound just proved, certifies that \(k=5\) is the unique global minimizer, not merely the best size observed numerically.

## Verification
Run `python3 check_exact.py` (Python 3 standard library only). The program checks the beta-binomial mass sum and its zero-positive-cell probability independently of the recurrence, the exact expected test-cost formula, both adjacent-ratio identities, and the strict witness inequalities. It performs 14,520 exact-rational identity tests over a rational parameter grid and then checks 1,000 candidate pool costs for the witness. These are finite consistency tests; the universal classifications are established by the preceding algebraic proof and the beta-gamma asymptotic.

## Relationship to prior work
Dorfman's 1943 procedure is the classical two-stage testing protocol. Lendle, Hudgens and Qaqish (online 2011) study correlated-response disease screening, including the efficiency of hierarchical pooling. Basso and coauthors (2021) use precisely beta-binomial correlated screening and derive expected test use, correlation comparisons and a comparison of optimal beta-binomial versus binomial pool sizes (their Propositions 1–2 and Appendix). Landolfi and Lall (arXiv 2023) give an algorithmic treatment of optimal Dorfman partitions for arbitrary exchangeable distributions. Those works cover the underlying model, probability of a negative pool, and general computational formulation. The distinct statement established here is an exact all-integer beta-parameter *phase criterion* for strict resource savings, the complete bound of two cost turning points, and a low-index double-turn witness; it is not a new model or an assertion that the general partitioning algorithms were unknown.

## Limitations
The relevance of the two-turn phenomenon to actual diagnostics is limited by finite pool-size caps and dilution; no sensitivity or specificity effects are modeled. The full 2011 paper could not be reobtained through the available download methods; its accessible abstract and relevant indexed manuscript passages were examined, but overlooked equivalent detail remains a bibliographic risk. The 2021 and 2023 primary PDFs were materially inspected; further specialist review of correlated group-testing optimization is warranted. The exact parameter regimes do not optimize mixtures of pool sizes for a finite nondivisible cohort.

## References
- Dorfman, R. (1943), *The Detection of Defective Members of Large Populations*, Annals of Mathematical Statistics 14:436–440.
- Lendle, S. D., Hudgens, M. G., Qaqish, B. F. (2011), *Group Testing for Case Identification with Correlated Responses*, Biometrics, DOI 10.1111/j.1541-0420.2011.01674.x, first online 2011-09-27.
- Basso, L. J., Salinas, V., Sauré, D., Thraves, C., Yankovic, N. (2021), *The effect of correlation and false negatives in pool testing strategies for COVID-19*, DOI 10.1007/s10729-021-09578-w (online 2021-08-28).
- Landolfi, N. C., Lall, S. (2023), *Optimal Dorfman Group Testing for Symmetric Distributions*, arXiv:2308.11050 (first posted 2023-08-21).
- Wan, J., Zhang, Y., Frazier, P. I. (2021), *Correlation Improves Group Testing: Capturing the Dilution Effect*, arXiv:2111.07517 (first posted 2021-11-15).
