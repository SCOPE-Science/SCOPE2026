# Sharp samplewise positivity frontier for scalar Bernoulli control-variate Gram sketches

## Finding

A variance-reducing control variate can make a positive scalar Galerkin Gram estimator zero or negative. The exact finite-sample support-wise positivity threshold, and the sharp coefficient-contrast threshold for its oracle variance-optimal weight, can both be obtained without asymptotic approximations.

Fix \(m\ge1\), \(0<\eta<1\), and a finite number \(\nu\ge1\) of independently repeated sketches. Let \(p_i>0\) for \(1\le i\le m\), and let independent \(\gamma_i^{(j)}\sim\operatorname{Bernoulli}(\eta)\). Set
\[
 c_i=\frac1\nu\sum_{j=1}^{\nu}\gamma_i^{(j)},\quad
 \overline p=\frac1m\sum_{i=1}^m p_i,\quad
 Z_\beta=\beta+\frac{1}{m\eta}\sum_{i=1}^m c_i(p_i-\beta).
\]

The scalar Galerkin matrix is \(\overline p\), obtained from \(u=m^{-1/2}(1,\ldots,1)^{\mathsf T}\), \(P=\operatorname{diag}(p_i)\), and \(u^{\mathsf T}Pu\). The estimator subtracts a multiple of the sketched known Gram value \(u^{\mathsf T}u=1\). It is unbiased and has
\[
 \operatorname{Var}(Z_\beta)=\frac{1-\eta}{m^2\eta\nu}\sum_i(p_i-\beta)^2,
 \qquad \beta_0=\overline p
\]
as its unique variance-minimizing fixed coefficient.

**Exact all-mask positivity rule.** For sorted \(p_{(1)}\le\cdots\le p_{(m)}\), define
\[
 \beta_{\mathrm{crit}}=\min_{\substack{1\le k\le m\\k>m\eta}}
 \frac{\sum_{i=1}^{k}p_{(i)}}{k-m\eta}.
\]
For fixed \(\beta\in\mathbb R\), all sampling outcomes have \(Z_\beta>0\) if and only if \(0<\beta<\beta_{\mathrm{crit}}\). At \(\beta=\beta_{\mathrm{crit}}\), an outcome with value zero is possible. For \(\beta>\beta_{\mathrm{crit}}\), a negative outcome is possible; for \(\beta\le0\), the all-missing outcome is nonpositive. Every witnessing outcome has positive probability for every finite \(\nu\).

**Variance-optimal positivity rule.** At \(\beta=\overline p\),
\[
 \min_{\mathrm{outcomes}}Z_{\overline p}
 =\overline p-\frac{1}{m\eta}\sum_i(\overline p-p_i)_+.
\]
Therefore strict positivity holds for every outcome if and only if
\[
 \eta>\frac{\sum_i(\overline p-p_i)_+}{m\overline p}.
\]
The equality case admits a zero outcome, and the reverse strict inequality admits a negative outcome.

**Sharp contrast envelope.** Suppose \(0<a\le p_i\le b\), with contrast \(\kappa=b/a\ge1\). The exact infimum across all positive integers \(m\), all admissible coefficient vectors, and all finitely repeated Bernoulli outcomes is
\[
 \boxed{\inf\frac{Z_{\overline p}}{\overline p}
 =1-\frac{\sqrt\kappa-1}{\eta(\sqrt\kappa+1)}.}
\]
Consequently a dimension-independent **strict positive relative margin** exists exactly for
\[
 \boxed{\eta>\frac{\sqrt\kappa-1}{\sqrt\kappa+1}.}
\]
Below the threshold, a finite admissible instance has a negative outcome; at the threshold the infimum is zero. For \(\kappa>1\), when the contrast has rational square root, the zero endpoint is attained by a finite population; for other contrasts an extremal sequence approaches zero and individual finite populations can still be strictly positive at equality. When \(\kappa=1\), the estimate is identically the positive Gram scalar at its oracle coefficient for every admissible \(\eta\). When \(\kappa=1\), the estimate is identically the positive Gram scalar at its oracle coefficient for every admissible \(\eta\). This is a worst-case support statement, not a probability lower bound for failure.

## Assumptions and scope

The model is real, exactly arithmetic, scalar (one Galerkin basis vector), and has equal leverage scores. Row inclusion is independent across indices and repeated sketches, with common Bernoulli probability strictly between zero and one. Coefficients are strictly positive and fixed before sampling. The control coefficient \(\beta\) is deterministic, and the term *variance-optimal* refers to the **oracle** choice \(\overline p\); computing that oracle value exactly generally requires the same full sum being estimated. The theorem does not promise that a practical sample-estimated coefficient is optimal, nor that higher-dimensional corrected Gram matrices remain positive definite.

## Proof

**1. Variance and the oracle weight.** Since \(\mathbb E[c_i]=\eta\) and \(\operatorname{Var}(c_i)=\eta(1-\eta)/\nu\), independence across indices yields \(\mathbb E[Z_\beta]=\overline p\) and the stated variance. The quadratic in \(\beta\) has second derivative \(2m(1-\eta)/(m^2\eta\nu)>0\), so its unique minimizer is \(\beta_0=\overline p\).

**2. Complete support characterization.** Every vertex \(c_i\in\{0,1\}\) occurs with positive probability: require the same indicator value in all \(\nu\) repetitions. The minimum of an affine function over the cube \([0,1]^m\) occurs at a vertex, so these vertices determine exact positivity over the entire discrete support. For a selected set \(S\) of cardinality \(k\),
\[
 m\eta\,Z_\beta=(m\eta-k)\beta+\sum_{i\in S}p_i.
\]
If \(\beta>0\) and \(k\le m\eta\), this is positive. For each integer \(k>m\eta\), positivity for every selected set of size \(k\) holds exactly when \(\beta<\sum_{i=1}^{k}p_{(i)}/(k-m\eta)\). Taking the minimum proves the claimed necessary and sufficient interval. Equality and strict violation give zero and negative witnesses, respectively. The all-missing mask shows that \(\beta\le0\) cannot be strictly positive on the entire support.

**3. The oracle minimum.** For \(\beta=\overline p\), the adverse vertex selects precisely indices with \(p_i<\overline p\) and omits those with \(p_i>\overline p\); ties are arbitrary. Thus
\[
 \min Z_{\overline p}=\overline p-\frac{\sum_i(\overline p-p_i)_+}{m\eta}.
\]
The strict criterion, zero boundary, and negative side follow immediately.

**4. Exact coefficient-contrast optimization.** Let \(r\) entries lie below \(\overline p\); if no entries do, the deficit is zero. Write \(A\) for their sum, \(B\) for the sum of all remaining coefficients. The normalized downward mean deviation is
\[
 R=\frac{\sum_i(\overline p-p_i)_+}{m\overline p}
 =\frac rm-\frac{A}{A+B}.
\]
At fixed \(r\), this expression decreases with \(A\) and increases with \(B\). The constraints \(A\ge ra\), \(B\le(m-r)b\) therefore imply
\[
 R\le\frac{r(m-r)(\kappa-1)}{m[r+(m-r)\kappa]}.
\]
Equality is attained by exactly \(r\) coefficients equal to \(a\) and \(m-r\) coefficients equal to \(b\). With \(q=r/m\), the right-hand side becomes
\[
 F_\kappa(q)=\frac{(\kappa-1)q(1-q)}{q+(1-q)\kappa},\quad 0\le q\le1.
\]
Elementary differentiation (or completing a square after the substitution \(s=\sqrt\kappa\)) shows its unique maximum when \(\kappa>1\) is at \(q=s/(1+s)\), with value \((s-1)/(s+1)\). Finite rational fractions \(r/m\) are dense, proving the global infimum. For \(\kappa=1\), all coefficients coincide and the normalized deficit is zero. If \(s\) is rational, choose integers \(r,m\) with \(r/m=s/(1+s)\) to attain the endpoint; otherwise it is approached but not attained at finite \(m\).

**5. No finite-averaging repair.** The extremal vertex in step 3 is obtained by demanding, for each row, the same selected or omitted Bernoulli value in all \(\nu\) repeats. Its probability is \(\eta^{\nu r}(1-\eta)^{\nu(m-r)}>0\). Thus adding any finite number of independent repetitions changes this probability and the variance, but not the support-wise minimum.

**Concrete exact witness.** Set \(m=4\), \((p_1,p_2,p_3,p_4)=(1,1,1,9)\), \(\eta=2/5\), and \(\beta_0=3\). If the first three rows are always selected and the fourth always omitted, then \(Z_{\beta_0}=-3/4\), even though the exact Gram is \(3>0\). Here \(\beta_{\mathrm{crit}}=15/7\). At \(\eta=1/2\) the same outcome gives exactly zero, realizing the sharp contrast threshold \((\sqrt9-1)/(\sqrt9+1)=1/2\).

## Verification

Run the standalone Python 3 standard-library program with `python verify.py`. It checks exact-rational affine-mask minima and the all-mask positivity interval for 1,364 parameter populations (up to five rows), totaling 449,376 tested mask configurations across boundary variants; it also checks nine square-contrast equality instances. The recorded execution output is:

```text
VERIFY_OK coefficient_arrays= 1364  mask_tests= 449376  positivity_threshold_tests= 5456  square_contrast_equalities= 9
```

These finite checks verify selected algebraic instances only. The proof above, not enumeration, establishes the unbounded-dimension and finite-arbitrary-repetition statements.

## Relationship to prior work

Polydorides, Noori, Vandierendonck, and Woods (2025) establish parameter-oblivious Bernoulli Gram sketching and an elementwise control-variate correction; their equations (13)–(18) analyze variance and explicitly warn that corrected positive-definite Gram estimators can become singular or ill-conditioned, suggesting damping the correction. The present result accepts their mechanism as known and solves a narrower, distinct **all-mask positivity design problem** with an exact data-dependent interval, sharp contrast envelope, equality construction, and finite-averaging statement in the scalar equal-leverage specialization.

The later preprint by Polydorides, Wu, Noori, Vandierendonck, and Woods (2026) extends low-variance sketches and sketch fusion. Its abstract was examined; its full text was unavailable for complete comparison. Nothing here asserts its uninspected body lacks an equivalent bound. Classical elementary facts about Bernoulli sums, control variates, finite affine minima, and bounded mean deviation are used without novelty claims.

## Limitations

The coefficients of the variance-optimal rule are oracle quantities, not free online input. The cutoff \(\beta_{\mathrm{crit}}\) also depends on the full coefficient population; its main utility is a sharp classification and a benchmark for positivity safeguards. The contrast envelope is universal over the scalar equal-leverage family, not a statement about arbitrary trial spaces. A negative outcome may have exponentially small probability in \(\nu\); the theorem does not claim poor typical performance. No finite-precision, nonuniform-inclusion, matrix-valued, or fused-inverse estimator theorem is proved. An exact equivalent in older positivity-preserving control-variate literature or the inaccessible full 2026 paper cannot be excluded without further independent literature inspection.

## References

1. N. Polydorides, H. Noori, H. Vandierendonck, and R. Woods, *Randomised sketching of parametric linear systems*, IEEE Statistical Signal Processing Workshop (2025), pp. 186–190, DOI `10.1109/SSP64130.2025.11073388`. Lawful full peer-reviewed manuscript: `https://www.pure.ed.ac.uk/ws/files/516680657/IEEE_ssp_5_pager-19.pdf`.
2. N. Polydorides, Y. Wu, H. Noori, H. Vandierendonck, and R. Woods, *Low-Variance Randomised Numerical Linear Algebra for Finite Element Simulation*, arXiv `2606.08817`, first submitted June 7, 2026: `https://arxiv.org/abs/2606.08817`.
