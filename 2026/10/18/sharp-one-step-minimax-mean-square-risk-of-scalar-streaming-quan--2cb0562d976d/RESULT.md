# Sharp one-step minimax mean-square risk of scalar streaming quantile Kaczmarz under Massart corruption

## Finding

A scalar specialization of streaming quantile randomized Kaczmarz has an exact minimax mean-square error factor under bounded, jointly adversarial Massart corruption. It has a sharp quarter-corruption boundary and a two-term logarithmic calibration-batch law.

Fix a current nonzero scalar error \(e=x-x^*\), a calibration-batch size \(D\geq1\), a quantile proportion \(0<q<1\), an independent per-row corruption probability \(0<\beta<1\), and a corruption-amplitude ratio \(B\geq2\). Put \(k=\max\{1,\lfloor qD\rfloor\}\) and \(J\sim\operatorname{Bin}(D,\beta)\). The exact worst-case conditional mean-square factor is

\[
\boxed{\mathcal R_D(\beta,q,B)
=(1-\beta)\Pr(J\geq k)+4\beta
 +\beta(B^2-4)\Pr(J>D-k).}
\]

Specifically, the supremum over admissible joint adversarial choices of corruption values of \(\mathbb E[|x^+-x^*|^2\mid x]\) equals \(\mathcal R_D(\beta,q,B)|e|^2\). The supremum is attained by explicitly described conditional choices; it is not merely an upper estimate.

For every fixed finite \(B\geq2\), **there exist** \(q\in(0,1)\) and \(D\in\mathbb N\) with \(\mathcal R_D<1\) **if and only if** \(\beta<1/4\). If \(0<\beta<1/4\) and \(q\) is fixed in \((\beta,1-\beta)\), define

\[
I=D_{\mathrm{KL}}(1-q\,\|\,\beta)
=(1-q)\log\frac{1-q}{\beta}
+q\log\frac{q}{1-\beta}>0.
\]

Let \(D_{\min}(B)=\min\{D\geq1:\mathcal R_D(\beta,q,B)<1\}\). As \(B\to\infty\),

\[
\boxed{D_{\min}(B)=\frac{2}{I}\log B
 -\frac{1}{2I}\log\log B+O(1).}
\]

For each finite \(D\) and \(\beta>0\), \(\mathcal R_D\to\infty\) as \(B\to\infty\). Hence no fixed finite batch provides a uniform unconditional mean-square contraction across **unbounded** adversarial corruption amplitudes. This conclusion does not contradict high-probability guarantees which exclude sufficiently rare catastrophic batches.

## Assumptions and scope

The scalar measurement row \(a_j\) equals \(1\) or \(-1\), independently with equal probabilities. Measurements obey \(b_j=a_j x^*+\xi_j\epsilon_j\), where \(\xi_0,\xi_1,\ldots,\xi_D\) are independent \(\operatorname{Bernoulli}(\beta)\), independent of rows and of the current iterate. The value of \(\epsilon_j\) on any corrupted row may depend jointly on the entire batch, including all indicators and the current iterate. For this theorem the relative amplitude condition is \(|\epsilon_j|\leq B|e|\). There is no additive noise on uncorrupted rows.

Compute the \(k\)-th smallest absolute residual among rows indexed \(1,\ldots,D\); call this \(Q\). On the independent update row indexed \(0\), apply the exact unit-relaxation Kaczmarz projection if and only if its absolute residual is at most \(Q\). Otherwise retain the current iterate. Ties **are accepted**. This is the scalar, normalized-row version of the streaming quantile rule; it is **not** an assertion that the motivating paper's dimension-\(n\geq2\) theorem applies at dimension one.

The supremum is over adversarial corruption values at a **single fixed nonzero iterate**. The relative amplitude condition is state-dependent, not a generic absolute-noise assumption. The adversary's ability to choose corruption values **jointly after observing the corruption indicators**, as allowed by the Massart model, is essential for simultaneous sharpness of the two conditional cases.

## Proof

Normalize \(e\) to \(1\) by scalar homogeneity and change signs with the measurement rows. On each corrupted row, let \(v_j=\epsilon_j/(a_j e)\), so \(|v_j|\leq B\). Uncorrupted calibration residuals are exactly \(1\); corrupted calibration residuals are \(|1-v_j|\). After an accepted corrupted update the new error is \(v_0e\), while an accepted clean update produces error zero and any rejected update leaves error \(e\).

**Clean update.** Conditional on \(\xi_0=0\) and exactly \(J\) corrupted calibration samples, if \(J<k\), at most \(J\) residuals can be strictly below \(1\), so \(Q\geq1\) and the clean update is accepted. The squared-error ratio is zero. If \(J\geq k\), set every corrupted calibration value \(v_j=1\), making at least \(k\) residuals zero; then \(Q=0\), the clean residual \(1\) is rejected, and the squared-error ratio is one. Thus the sharp conditional ratio is \(\mathbf1_{\{J\geq k\}}\).

**Corrupted update.** Conditional on \(\xi_0=1\) and \(J\leq D-k\), at least \(k\) clean calibration residuals equal \(1\), so \(Q\leq1\). If a corrupted update is accepted, \(|1-v_0|\leq1\), and therefore \(0\leq v_0\leq2\). Its squared-error ratio is at most four; rejection gives ratio one. Equality at four is attained by setting every corrupted calibration value \(v_j=2\), so \(Q=1\), and choosing \(v_0=2\); ties are accepted. If \(J>D-k\), at most \(D-J<k\) calibration observations are clean. The general amplitude bound gives squared-error ratio at most \(B^2\) if accepted (and one if rejected). Set all corrupted calibration values to \(v_j=B\) and the update corruption to \(v_0=B\). Then \(Q=B-1\) because \(B\geq2\), and equality at \(B^2\) is attained. Thus the sharp conditional ratio is \(4+(B^2-4)\mathbf1_{\{J>D-k\}}\).

The update indicator is independent of \(J\), and conditional strategies above can be selected as functions of the indicators (admissible joint Massart selection). Averaging proves the exact formula.

For \(\beta\geq1/4\), its nonnegative terms give \(\mathcal R_D\geq4\beta\geq1\) at every \(D,q,B\). For \(0<\beta<1/4\), choose any fixed \(q\in(\beta,1-\beta)\). Binomial laws of large numbers yield \(\Pr(J\geq k)\to0\) and \(\Pr(J>D-k)\to0\) as \(D\to\infty\), so \(\mathcal R_D\to4\beta<1\). This proves both directions of the sharp boundary.

For the batch law, write \(a=1-q>\beta\), \(I=D_{\mathrm{KL}}(a\|\beta)\), and \(r_D=D-k+1\). For every sufficiently large \(D\), \(r_D=aD+O(1)\), where the integer offset stays in a fixed bounded interval. Stirling's formula gives

\[
\Pr(J=r_D)=\Theta\bigl(D^{-1/2}e^{-DI}\bigr).
\]

Indeed, the derivative of the binary relative entropy is finite at the interior \(a\), so shifting its binomial argument by \(O(1)\) affects only a bounded multiplicative constant. The ratio of successive binomial masses starting at \(r_D\) tends to \(\rho=\beta(1-a)/[a(1-\beta)]<1\); it is decreasing in the upper tail. Summing the geometric bounds therefore gives

\[
\boxed{\Pr(J>D-k)=\Theta\bigl(D^{-1/2}e^{-DI}\bigr)}
\qquad(D\to\infty).
\]

For \(q>\beta\), the other tail \(\Pr(J\geq k)\) decays exponentially in \(D\). Thus the strict inequality \(\mathcal R_D<1\) near its first solution is governed by the positive term \(\beta(B^2-4)\Theta(D^{-1/2}e^{-DI})\) crossing the fixed gap \(1-4\beta>0\). The upper and lower geometric-tail bounds hold **uniformly for every sufficiently large integer** \(D\); smaller fixed \(D\) are excluded as \(B\to\infty\) because the catastrophic-tail probability is positive. Taking logarithms and solving the two-sided inequalities yields

\[
DI=2\log B-\tfrac12\log D+O(1).
\]

The first-order consequence is \(D=\frac{2}{I}\log B+O(\log\log B)\). Substituting this in the logarithmic term gives the stated \(-\frac1{2I}\log\log B\) correction and an \(O(1)\) remainder, including the possible integer-rounding oscillation. This derivation concerns the **first** successful integer \(D\) and does not assume monotonicity of the quantile rule as \(D\) changes. Finally, \(\Pr(J>D-k)\geq\Pr(J=D)=\beta^D>0\), proving divergence for fixed \(D\) as \(B\to\infty\).

## Verification

Run `python3 CHECK.py` alongside this document. The standalone standard-library program enumerates the conditional corruption values at all endpoints and residual kinks in 72 finite configurations (batch sizes from one to six), checks the exact expectation against the binomial formula, tests the quarter threshold numerically, verifies scaled binomial tails, and computes representative minimum batch sizes for growing amplitude bounds. It is an independent finite check of the formulas, **not** a proof of the asymptotic or universal claims.

For example, with \(\beta=0.1\), \(q=0.5\), \(B=8\), the exact minimax one-step ratio at \(D=8\) is approximately \(0.407112\), dropping toward \(0.4\) for larger batches. The formula and its boundary prove the universal conclusions.

## Relationship to prior work

Battaglia, Cai, Chen, Ma, Needell, and Wu (2026), *Quantile Randomized Kaczmarz for Streaming Linear Systems with Massart Noise* (arXiv:2608.27968, initially public 2026-08-28), introduce the independent calibration/update streaming rule, permit jointly chosen adversarial Massart corruption values, and analyze high-probability convergence in dimensions at least two. The present scalar specialization keeps the **same quantile and tie-acceptance mechanisms** but asks the different question of **exact unconditional worst-case one-step squared risk with a relative amplitude envelope**. It does not improve or replace their dimension-at-least-two guarantees.

Cai and collaborators, *On the Subsample Size of Quantile-Based Randomized Kaczmarz* (arXiv:2507.15185), prove high-probability logarithmic-in-horizon subsample requirements and catastrophic failure under certain insufficient batches in a finite-system model. This already demonstrates the danger of rare bad batches; the present result **does not claim that observation as novel**. It instead provides the exact scalar finite-batch minimax factor, the sharp quarter-corruption feasibility boundary, and the two-term amplitude-dependent batch law. Earlier quantile Kaczmarz literature, including arXiv:2009.08089, studies different full-sample settings.

## Limitations

The theorem applies only to the normalized **scalar** streaming rule, independent Bernoulli corruption indicators, jointly adaptive Massart corruption values, exact Kaczmarz projection, acceptance of ties, and the state-relative envelope \(|\epsilon_j|\leq B|e|\). It gives no uniform higher-dimensional corruption threshold and no claim about absolute-noise amplitudes, adaptive reuse of calibration samples, or floating-point implementation. The asymptotic batch formula holds for fixed \(q\in(\beta,1-\beta)\) and fixed \(\beta\in(0,1/4)\) as \(B\to\infty\); it is not an optimum over quantile levels. The possible existence of equivalent calculations in unindexed robust-iteration literature is an originality risk. Independent scientific validation has not been performed.

## References

1. Battaglia, Cai, Chen, Ma, Needell, and Wu (2026), *Quantile Randomized Kaczmarz for Streaming Linear Systems with Massart Noise*, arXiv:2608.27968, https://arxiv.org/abs/2608.27968.
2. Cai et al., *On the Subsample Size of Quantile-Based Randomized Kaczmarz*, arXiv:2507.15185, https://arxiv.org/abs/2507.15185.
3. *Quantile-based random Kaczmarz for corrupted linear systems of equations*, arXiv:2009.08089, https://arxiv.org/abs/2009.08089.
