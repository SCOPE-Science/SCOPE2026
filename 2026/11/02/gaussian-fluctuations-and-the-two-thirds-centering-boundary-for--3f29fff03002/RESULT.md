# Gaussian fluctuations and the two-thirds centering boundary for critical Zipf quorum times

## Finding
Fix a quorum fraction \(\theta\in(0,1)\). For each integer \(N\ge2\), put
\[
H_N=\sum_{j=1}^N\frac1j,\qquad
q_{i,N}=\frac1{iH_N}\quad(1\le i\le N).
\]
Let \(E_{1,N},\dots,E_{N,N}\) be independent exponential random variables of respective rates \(q_{i,N}\). At time \(t\) the discovered weight is
\[
M_N(t)=\sum_{i=1}^Nq_{i,N}\mathbf1_{\{E_{i,N}\le t\}},
\qquad T_N=\inf\{t\ge0:M_N(t)>\theta\}.
\]
Define the unique \(A_N>0\) solving
\[
S_N(A_N)=\theta H_N,\qquad
S_N(A)=\sum_{i=1}^N\frac{1-e^{-A/i}}i.
\]
Writing \(\gamma\) for Euler's constant and \(c_\theta=e^{(\theta-2)\gamma}\), the following assertions hold jointly for every fixed \(\theta\in(0,1)\):

1. **Exact-mean-centred Gaussian law:**
   \[
   \frac{T_N/H_N-A_N}{\sqrt{A_N}}
   \ \Rightarrow\ \mathcal N(0,1/2).
   \]
   In particular \(A_N\sim c_\theta N^\theta\) and
   \[
   \frac{T_N-H_NA_N}{H_NN^{\theta/2}}
   \ \Rightarrow\ \mathcal N(0,c_\theta/2).
   \]
2. **Sharp deterministic centering correction:**
   \[
   A_N=c_\theta N^\theta+c_\theta^2N^{2\theta-1}
     +O_\theta(1+N^{3\theta-2}).
   \]
3. **The two-thirds boundary for using only first-order centering:** if
   \(Z_N=(T_N/H_N-c_\theta N^\theta)/N^{\theta/2}\), then
   \[
   Z_N\Rightarrow
   \begin{cases}
   \mathcal N(0,c_\theta/2),&0<\theta<2/3,\\
   \mathcal N(c_\theta^2,c_\theta/2),&\theta=2/3,
   \end{cases}
   \]
   whereas \(Z_N\to+\infty\) in probability if \(2/3<\theta<1\).

For independent Poisson clocks with rates \(\lambda q_{i,N}\), \(\lambda>0\), multiply every displayed time \(T_N\) by \(\lambda\) to recover the same limits. The asymptotic normal laws concern the actual random hitting time, not merely the discovered weight at a deterministic time.

## Assumptions and scope
The number \(N\) of coupon types tends to infinity; \(\theta\in(0,1)\) and the global clock multiplier are fixed, not dependent on \(N\). The activity probabilities and the contributed quorum weights coincide and are harmonic (critical aligned Zipf exponent one). First arrival times across types are independent exponential random variables. The stopping inequality is strict; the distinction from a non-strict threshold is asymptotically immaterial because the normalized discovered-weight fluctuation has a continuous Gaussian limit.

The center \(A_N\) is **deterministic and exact**: it is the unique root of the mean discovered-mass equation \(\mathbb E M_N(H_NA_N)=\theta\). There is no assumption that a random empirical center can be substituted for this root.

## Proof
**1. A uniform harmonic-sum expansion.** Introduce
\[
S_\infty(A)=\sum_{j=1}^\infty\frac{1-e^{-A/j}}j.
\]
For \(A>1\) split at \(m=\lfloor A\rfloor\):
\[
S_\infty(A)=H_m-\sum_{j\le m}\frac{e^{-A/j}}j
 +\sum_{j>m}\frac{1-e^{-A/j}}j.
\]
The last two terms are Riemann sums, of mesh \(1/A\), for the integrable bounded-variation functions \(e^{-1/x}/x\) on \((0,1]\) and \((1-e^{-1/x})/x\) on \([1,\infty)\), respectively. Their total integral difference is
\[
\int_0^1\frac{1-e^{-u}}u\,du
 -\int_1^\infty\frac{e^{-u}}u\,du=\gamma.
\]
The bounded-variation Riemann-sum error is \(O(A^{-1})\), including the endpoint shift at \(\lfloor A\rfloor\), while \(H_m=\log A+\gamma+O(A^{-1})\). Hence
\[
S_\infty(A)=\log A+2\gamma+O(A^{-1}). \tag{1}
\]
When \(A=o(N)\), Taylor expansion with a summable remainder gives
\[
\sum_{j>N}\frac{1-e^{-A/j}}j
 =A\sum_{j>N}j^{-2}+O\left(A^2\sum_{j>N}j^{-3}\right)
 =\frac AN+O\left(\frac A{N^2}+\frac{A^2}{N^2}\right).
\]
Combining this with (1), uniformly along \(A\to\infty\), \(A/N\to0\),
\[
S_N(A)=\log A+2\gamma-\frac AN
 +O\left(\frac1A+\frac A{N^2}+\frac{A^2}{N^2}\right). \tag{2}
\]

**2. Existence and expansion of the root.** The continuous function \(S_N\) is strictly increasing, \(S_N(0)=0\), and \(S_N(A)\to H_N\) as \(A\to\infty\); thus \(A_N\) exists uniquely. As \(H_N=\log N+\gamma+O(N^{-1})\), (2) evaluated at a fixed positive multiple of \(N^\theta\) and monotonicity imply
\[
A_N\sim c_\theta N^\theta,
\qquad c_\theta=e^{(\theta-2)\gamma}.
\]
Substituting \(A_N\) into (2) and expanding \(\log(A_N/(c_\theta N^\theta))\) gives
\[
\log\frac{A_N}{c_\theta N^\theta}
 =\frac{A_N}N+O_\theta\left(N^{-\theta}+N^{2\theta-2}+N^{-1}\right).
\]
Exponentiation, followed by one substitution \(A_N=c_\theta N^\theta+o(N^\theta)\) into the leading correction, yields
\[
A_N=c_\theta N^\theta+c_\theta^2N^{2\theta-1}
 +O_\theta(1+N^{3\theta-2}). \tag{3}
\]
For \(\theta>1/2\) the positive second term dominates the constant remainder. Equation (3) is used at and away from the boundary \(\theta=2/3\).

**3. Sharp deterministic-time variance and slope.** Let \(\xi_{i,N}(A)=\mathbf1_{\{E_{i,N}\le H_NA\}}\). These are independent Bernoulli random variables with means \(r_i(A)=1-e^{-A/i}\). Define
\[
R_N(A)=\sum_{i=1}^N\frac{\xi_{i,N}(A)-r_i(A)}i,
\quad V_N(A)=\operatorname{Var}R_N(A)
 =\sum_{i=1}^N\frac{e^{-A/i}(1-e^{-A/i})}{i^2}.
\]
For each deterministic sequence \(A\to\infty\) with \(A/N\to0\), the Riemann sums with \(x=i/A\) yield
\[
A S_N'(A)\longrightarrow
\int_0^\infty\frac{e^{-1/x}}{x^2}\,dx=1,
\qquad
A V_N(A)\longrightarrow
\int_0^\infty\frac{e^{-1/x}(1-e^{-1/x})}{x^2}\,dx=\frac12. \tag{4}
\]
Both integrands are integrable at zero and infinity, so truncating to a compact subinterval first justifies these limits. Equation (4) holds as well for \(A=A_N+u\sqrt{A_N}\), uniformly for fixed bounded \(u\).

**4. A triangular-array Gaussian limit.** For fixed \(u\in\mathbb R\), put \(A_{N,u}=A_N+u\sqrt{A_N}\). The centered weighted array satisfies
\[
\sqrt{A_N}R_N(A_{N,u})\Rightarrow\mathcal N(0,1/2). \tag{5}
\]
To verify Lindeberg rather than merely infer (5) from variance, split the indices at \(i=A_N^{2/3}\). For smaller indices the probability that *any* such type remains undiscovered at \(A_{N,u}\) is bounded by
\[
O\left(A_N^{2/3}\exp(-A_N^{1/3}/2)\right)=o(1).
\]
On the complement their centered, \(\sqrt{A_N}\)-scaled contribution is deterministically \(o(1)\). On larger indices every centered summand is bounded by \(\sqrt{A_N}/i=O(A_N^{-1/6})\); Lindeberg holds directly. Its limiting total variance is \(1/2\) by (4), proving (5).

**5. Inverting the threshold.** By the mean-value theorem and (4),
\[
\sqrt{A_N}\{S_N(A_{N,u})-S_N(A_N)\}\longrightarrow u.
\]
The exact hitting event is \(\{T_N/H_N\le A_{N,u}\}=\{S_N(A_{N,u})+R_N(A_{N,u})>\theta H_N\}\). The strict inequality presents no limiting difficulty because (5) has a continuous limit. Hence
\[
\Pr\left(\frac{T_N/H_N-A_N}{\sqrt{A_N}}\le u\right)
 \longrightarrow\Pr(Z+u>0)=\Phi(\sqrt2\,u),
\quad Z\sim\mathcal N(0,1/2).
\]
This proves the first assertion.

**6. The centering transition.** Divide (3) by \(N^{\theta/2}\). The leading deterministic shift is
\[
\frac{A_N-c_\theta N^\theta}{N^{\theta/2}}
 \sim c_\theta^2N^{3\theta/2-1}
 \quad\text{for }\theta>1/2.
\]
It vanishes for \(\theta<2/3\), tends to \(c_\theta^2\) at \(\theta=2/3\), and diverges positively for \(\theta>2/3\); when \(\theta\le1/2\), (3) also makes the shift vanish. Slutsky's theorem completes the three cases. The effect is a finite-population bias from indices beyond \(N\), not a change of the Gaussian fluctuation mechanism.

## Verification
A self-contained Python 3 verifier (`checker.py`) accompanies this result, together with its recorded output (`checker_output.txt`). Execute `python3 checker.py` in the directory containing these files. Its 72 finite/computational assertions include independently enumerated exact-rational Bernoulli moment identities and numerical evaluations of the exact centering root, normalized slope, variance, and finite-population correction for three system sizes and three quorum fractions. The numerical evidence is consistent with (3)–(5), but does **not** prove the limits; those depend on the analytical arguments above.

The quoted asymptotic constants may also be checked without randomness: solve \(S_N(A)=\theta H_N\) by bisection, then evaluate \(A\sum_i e^{-A/i}/i^2\) and \(A\sum_i e^{-A/i}(1-e^{-A/i})/i^2\); the two values approach \(1\) and \(1/2\), respectively.

## Relationship to prior work
Müller and Šebek, *Weighted-threshold Coupon Collection* (first public July 9, 2026, arXiv:2607.08551v1), establish the critical aligned-Zipf first-order scale and constant \(c_\theta\) (their Theorem 6.3), a variance upper bound (Lemma 6.2), and a concentration-based deterministic comparison. The first-order law and its constant are **not** claimed as new here. The present statement adds the fluctuation law around the exact mean root and the sharp shift/phase boundary for the leading centering; neither conclusion appears in the inspected Section 6.

Chebunin and Zuyev, *Functional Central Limit Theorems for Occupancies and Missing Mass Process in Infinite Urn Models*, Journal of Theoretical Probability (published online 2020), give Gaussian limits for fixed infinite occupancy-frequency sequences satisfying regular-variation conditions. These furnish nearby central-limit theory, but their fixed, summable infinite frequency law is not the present \(N\)-dependent harmonic normalization, and their theorem does not state the finite-population cutoff bias or the inverse-quorum transition. Ordinary triangular-array Lindeberg theory is used and acknowledged, rather than claimed as new.

Baake and Baake, *A multiple coupon collection process and its Markov embedding structure* (2026), analyze Markov semigroup embeddability for multiple-coupon sampling. Their inspected principal theorem concerns a different question and does not imply the displayed asymptotic. Broader uninspected occupancy and inversion results may still contain a relevant equivalent; historical novelty is not independently certified.

## Limitations
The theorem is about independent Poissonized first discoveries, fixed \(\theta\), aligned harmonic rates and weights, and a single threshold crossing. It does not provide rates in probability metrics, a functional central limit theorem in \(\theta\), extensions to other Zipf exponents, or fixed-draw de-Poissonized error bounds. The exact-mean-root Gaussian limit holds in every \(0<\theta<1\); the centering transition only concerns replacing the root with the leading explicit constant. External historical-priority review and independent mathematical validation have not been performed.

## References
1. Sebastian Müller and Stjepan Šebek, *Weighted-threshold Coupon Collection*, arXiv:2607.08551v1 (July 9, 2026), https://arxiv.org/abs/2607.08551 . Sections 2, 3 and 6.
2. Mikhail Chebunin and Sergei Zuyev, *Functional Central Limit Theorems for Occupancies and Missing Mass Process in Infinite Urn Models*, Journal of Theoretical Probability 35 (2022), 1–19; published online November 23, 2020. https://doi.org/10.1007/s10959-020-01053-6 . Introduction and Theorem 1.
3. Ellen Baake and Michael Baake, *A multiple coupon collection process and its Markov embedding structure*, Monatshefte für Mathematik 209 (2026), 357–381. https://doi.org/10.1007/s00605-026-02153-x . Sections 1, 3 and 6.
