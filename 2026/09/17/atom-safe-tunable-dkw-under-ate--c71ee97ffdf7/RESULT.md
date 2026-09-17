# Atom-safe and tunable DKW bounds under approximate tensorization of entropy

**SCOPE Phase II research record.**  
**Record ID:** SCOPE-20260917-c71ee97ffdf7  
**Publication identity:** 05159106-83b6-4348-88a0-4df6aec0f289

## 1. Setting

Let \(X=(X_1,\ldots,X_n)\sim\nu\) on \(\mathcal X^n\). Assume that \(\nu\) satisfies approximate tensorization of entropy (ATE) with constant \(\kappa\ge 1\). Roth (2026, Theorem 2.4) shows that ATE implies the bounded-differences inequality
\[
\Pr\{f(X)-\mathbb Ef(X)\ge t\}
\le \exp\!\left(-\frac{2t^2}{\kappa\sum_i c_i^2}\right)
\]
whenever changing coordinate \(i\) changes \(f\) by at most \(c_i\). The lower-tail analogue follows by applying the same statement to \(-f\).

For a measurable set \(A\subseteq\mathcal X\), write
\[
P_n(A)=\frac1n\sum_{i=1}^n\mathbf 1\{X_i\in A\},
\qquad
\bar P(A)=\frac1n\sum_{i=1}^n\Pr(X_i\in A).
\]
The observations need not be identically distributed.

## 2. A finite-bracketing inequality under ATE

### Theorem 1
Let \(\mathcal A\) be a class of measurable subsets of \(\mathcal X\). Suppose that for some \(\varepsilon\ge0\) there are \(B<\infty\) pairs \((L_j,U_j)\), \(j=1,\ldots,B\), such that
\[
L_j\subseteq U_j,\qquad \bar P(U_j\setminus L_j)\le\varepsilon,
\]
and every \(A\in\mathcal A\) is bracketed by at least one pair:
\[
L_j\subseteq A\subseteq U_j.
\]
Then, for every \(r>\varepsilon\),
\[
\Pr\!\left\{
\sup_{A\in\mathcal A}|P_n(A)-\bar P(A)|\ge r
\right\}
\le
2B\exp\!\left[-\frac{2n(r-\varepsilon)^2}{\kappa}\right].
\tag{2.1}
\]
If the supremum is not measurable, the same statement holds with outer probability.

### Proof
For every fixed measurable \(C\), \(P_n(C)\) changes by at most \(1/n\) when a single coordinate is changed. Thus ATE bounded differences gives
\[
\Pr\{P_n(C)-\bar P(C)\ge t\}\le e^{-2nt^2/\kappa},
\qquad
\Pr\{\bar P(C)-P_n(C)\ge t\}\le e^{-2nt^2/\kappa}.
\tag{2.2}
\]

If \(L_j\subseteq A\subseteq U_j\), then
\[
P_n(A)-\bar P(A)
\le P_n(U_j)-\bar P(U_j)+\bar P(U_j\setminus A)
\le P_n(U_j)-\bar P(U_j)+\varepsilon,
\]
and similarly
\[
\bar P(A)-P_n(A)
\le \bar P(L_j)-P_n(L_j)+\bar P(A\setminus L_j)
\le \bar P(L_j)-P_n(L_j)+\varepsilon.
\]
Hence a deviation of size at least \(r\) forces one of the \(2B\) one-sided endpoint deviations to be at least \(r-\varepsilon\). Equation (2.1) follows from (2.2) and a union bound. \(\square\)

This theorem is deliberately elementary: the bracketing device is standard empirical-process machinery. Its role here is to expose a direct finite-sample consequence of ATE for uniform empirical-set deviations.

## 3. DKW-type inequality without continuity

Now take \(\mathcal X=\mathbb R\), define
\[
\widehat F_n(x)=\frac1n\sum_{i=1}^n\mathbf 1\{X_i\le x\},
\qquad
\bar F(x)=\mathbb E\widehat F_n(x),
\]
and let
\[
D_n=\sup_{x\in\mathbb R}|\widehat F_n(x)-\bar F(x)|.
\]
Roth (2026, Theorem 4.9) proves, assuming \(\bar F\) is continuous,
\[
\Pr(D_n\ge r)\le \frac4r\exp\!\left(-\frac{nr^2}{2\kappa}\right).
\tag{3.1}
\]
The next result both removes continuity and retains the free discretization parameter that is lost when a particular grid size is selected.

### Theorem 2
No continuity assumption on \(\bar F\) is needed. For every integer \(N\ge2\) and every \(r>1/N\),
\[
\boxed{
\Pr(D_n\ge r)
\le
2(N-1)\exp\!\left[-\frac{2n(r-1/N)^2}{\kappa}\right].
}
\tag{3.2}
\]
Consequently,
\[
\Pr(D_n\ge r)
\le
\min\!\left\{1,
\inf_{\substack{N\ge2\\1/N<r}}
2(N-1)\exp\!\left[-\frac{2n(r-1/N)^2}{\kappa}\right]
\right\}.
\tag{3.3}
\]

### Proof
Fix \(N\ge2\). For \(j=1,\ldots,N-1\), let
\[
q_j=\inf\{x\in\mathbb R:\bar F(x)\ge j/N\}
\]
be generalized quantiles. Repeated values are allowed. Let the distinct values among the \(q_j\)'s be
\[
b_1<\cdots<b_m,
\qquad m\le N-1,
\]
and put \(b_0=-\infty\), \(b_{m+1}=+\infty\).

The generalized-quantile identities imply the atom-safe gap bound
\[
\bar F(b_{k+1}-)-\bar F(b_k)\le\frac1N,
\qquad k=0,\ldots,m,
\tag{3.4}
\]
where \(\bar F(-\infty)=0\) and \(\bar F(+\infty-)=1\). Indeed, if \(b_k\) is the quantile value for the last level \(c/N\) in its repeated block, then
\(\bar F(b_k)\ge c/N\), while the next distinct quantile satisfies
\(\bar F(b_{k+1}-)\le(c+1)/N\). The two endpoint cases are identical.

Introduce the strict empirical CDF
\[
\widehat F_n^{<}(b)=\frac1n\sum_{i=1}^n\mathbf 1\{X_i<b\},
\qquad
\mathbb E\widehat F_n^{<}(b)=\bar F(b-).
\]
For \(x\in[b_k,b_{k+1})\), monotonicity and (3.4) give
\[
\widehat F_n(x)-\bar F(x)
\le
\widehat F_n^{<}(b_{k+1})-\bar F(b_{k+1}-)+\frac1N,
\tag{3.5}
\]
while
\[
\bar F(x)-\widehat F_n(x)
\le
\bar F(b_k)-\widehat F_n(b_k)+\frac1N.
\tag{3.6}
\]
The upper endpoint at \(+\infty\) and lower endpoint at \(-\infty\) are deterministic, so only \(m\) strict upper-tail terms and \(m\) non-strict lower-tail terms remain. Every one is an empirical average of indicators and therefore obeys the one-sided bound (2.2). If \(D_n\ge r\), (3.5)--(3.6) force one of those terms to be at least \(r-1/N\). Hence
\[
\Pr(D_n\ge r)
\le2m\exp\!\left[-\frac{2n(r-1/N)^2}{\kappa}\right]
\le2(N-1)\exp\!\left[-\frac{2n(r-1/N)^2}{\kappa}\right].
\]
This proves (3.2), and taking the infimum proves (3.3). \(\square\)

### Recovery and sharpening of the stated Roth bound
For \(0<r\le1\), choose \(N=\lceil2/r\rceil\). Then \(1/N\le r/2\) and \(N-1<2/r\), so (3.2) gives exactly the same displayed guarantee as (3.1), now for arbitrary \(\bar F\):
\[
\Pr(D_n\ge r)
\le \frac4r\exp\!\left(-\frac{nr^2}{2\kappa}\right).
\tag{3.7}
\]
For \(r>1\), the event is empty.

Keeping \(N\) tunable can be much sharper. For example, whenever \(r>1/n\), taking \(N=n\) gives
\[
\Pr(D_n\ge r)
\le2(n-1)\exp\!\left[-\frac{2n(r-1/n)^2}{\kappa}\right].
\tag{3.8}
\]
Thus, for fixed \(r\in(0,1)\) and a sequence of ATE laws with a common constant \(\kappa\),
\[
\limsup_{n\to\infty}\frac1n\log\Pr(D_n\ge r)
\le-\frac{2r^2}{\kappa}.
\tag{3.9}
\]
The stated bound (3.1) has exponential rate \(-r^2/(2\kappa)\). Hence retaining and optimizing the bracketing resolution improves the fixed-deviation exponential rate by a factor of four within this argument. For \(\kappa=1\), (3.9) matches the classical i.i.d. DKW exponent, although the finite-sample prefactor here is not Massart-sharp.

## 4. Finite-support corollary

If the average marginal distribution is supported on exactly \(M<\infty\) points, then every marginal is supported on the same finite set. The empirical and average CDFs are constant between support points, and deviations at the empty and full support endpoints vanish. Therefore, for every \(r>0\),
\[
\boxed{
\Pr(D_n\ge r)
\le2(M-1)\exp\!\left(-\frac{2nr^2}{\kappa}\right).
}
\tag{4.1}
\]
For fixed finite support this removes the bracketing loss entirely. This is particularly relevant to discrete spin-system settings, where ATE is a standard weak-dependence condition.

## 5. Relation to prior work

- **Roth (2026).** Theorem 4.9 assumes a continuous average marginal CDF and chooses \(N=\lceil2/r\rceil\) in a standard bracketing proof. Theorem 2 above replaces equal-mass continuous anchors by generalized quantiles together with strict/non-strict threshold brackets, so atoms and repeated quantiles cause no problem. It also records the stronger free-\(N\) bound implicit in the bracketing strategy rather than fixing the resolution.
- **Bobkov--Götze (2010).** Their dependent empirical-CDF results use Poincare/log-Sobolev assumptions and, in the comparison quoted by Roth, a Lipschitz average CDF. The present statement is instead driven by ATE and handles arbitrary atoms.
- **Kontorovich--Weiss (2014)** and **Jerison (2026)** give DKW-type bounds under Markov/regenerative structures. Those assumptions encode a different dependence mechanism and do not subsume arbitrary \(\kappa\)-ATE laws.
- **Classical i.i.d. DKW--Massart.** Continuity is not required for validity of the classical two-sided DKW inequality. The contribution here is not an atom extension in the i.i.d. theory; it is the removal of Roth's continuity restriction under ATE, together with the tunable finite-sample bound and the general bracketing formulation.
- **Discrete ATE literature.** Caputo--Menz--Tetali (2015) and subsequent entropy-factorization work establish ATE in discrete weakly dependent systems, so an ATE empirical-CDF theorem that permits atoms covers a substantial part of the natural ATE setting excluded by a continuity hypothesis.

## 6. Limitations

1. The bounds use only bounded differences plus finite bracketing. They do not exploit variance, local mass, or finer dependence information, and they do not recover the sharp finite-sample Massart constant in the i.i.d. case.
2. The factor \(\kappa\) enters through ATE McDiarmid concentration; no claim is made that its dependence is minimax optimal for uniform empirical-CDF deviations.
3. The general bracketing theorem is a direct combination of standard bracketing with ATE bounded differences. The originality claim is restricted to the located ATE formulation, the atom-safe DKW consequence, and the retained/optimized resolution bound, not to bracketing as a method.
4. Originality is to the best of our knowledge. Broad empirical-process and dependent-concentration literatures remain a residual source of equivalent formulations under different functional-inequality assumptions.

## References

1. V. Roth, *On McDiarmid's Inequality under Dependence via Approximate Tensorization of Entropy*, arXiv:2606.12720 (2026).
2. S. G. Bobkov and F. Götze, *Concentration of empirical distribution functions with applications to non-i.i.d. models*, Bernoulli 16 (2010), 1385--1414, DOI: 10.3150/10-BEJ254.
3. A. Kontorovich and R. Weiss, *Uniform Chernoff and Dvoretzky--Kiefer--Wolfowitz-type inequalities for Markov chains and related processes*, Journal of Applied Probability 51 (2014), 1100--1113, DOI: 10.1239/jap/1421763330.
4. P. Caputo, G. Menz and P. Tetali, *Approximate tensorization of entropy at high temperature*, Ann. Fac. Sci. Toulouse 24 (2015), 691--716, arXiv:1405.0608.
5. D. Jerison, *A data-dependent DKW inequality for regenerative Markov chains*, arXiv:2606.30866 (2026).
6. P. Massart, *The tight constant in the Dvoretzky--Kiefer--Wolfowitz inequality*, Annals of Probability 18 (1990), 1269--1283, DOI: 10.1214/aop/1176990746.
