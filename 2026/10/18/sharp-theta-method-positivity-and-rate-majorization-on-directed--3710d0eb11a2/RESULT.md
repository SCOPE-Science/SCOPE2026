# Strict rate majorization of the theta-method positivity horizon on a directed cycle

## Finding

Let \(n\ge3\), let \(r_i>0\), and let \(Q(r)\) be the row-convention generator whose only nonzero entries in row \(i\) are \(Q_{ii}=-r_i\) and \(Q_{i,i+1}=r_i\), with indices modulo \(n\). For \(0\le\theta\le1\) define \(H_\theta(r)\) as the supremum of the timesteps \(h\ge0\) for which
\[
M_\theta(h;r)=(I-\theta hQ(r))^{-1}(I+(1-\theta)hQ(r))
\]
is entrywise nonnegative. The known cycle horizon criterion ensures that the admissible steps form a single initial interval, with a finite upper endpoint included.

**Rate comparison.** Fix \(0<\theta<1\). If \(r\) majorizes \(u\) (equal totals and every descending partial sum of \(r\) at least that of \(u\)), then \(H_\theta(r)\le H_\theta(u)\). If \(r\) and \(u\) are not permutations and \(H_\theta(u)<\infty\), the inequality is strict. In particular, the comparison can be strict even when the fastest rate is unchanged. For example, \((4,3,1)\) majorizes \((4,2,2)\), both horizons are finite at \(\theta=1/2\), and the first horizon is smaller although both fastest rates are 4.

**Fixed-budget design.** For any total \(B>0\), the uniform vector with rates \(\rho=B/n\) uniquely maximizes the horizon over the positive rate simplex exactly for \(0\le\theta\le(n-1)/n\). At the critical value, the uniform horizon is infinite but every nonuniform horizon remains finite. Above the critical value, infinitely many nonuniform vectors also have infinite horizons. For \(0<\theta<(n-1)/n\), the uniform optimum is
\[
H_\theta^{\max}=\frac{t}{\theta\rho(1-t)},\qquad
t\in(0,1),\quad t=\theta+(1-\theta)t^n.
\]
Here the root in \((0,1)\) is unique. At \(\theta=0\), the uniform optimum is \(1/\rho\).

## Assumptions and scope

The graph is a single one-way cycle with strictly positive rates, and the comparison concerns entrywise nonnegativity of the end-step matrix, or equivalently preservation of all nonnegative row vectors. It does not concern internal stages, more general directed graphs, or kinetic stability. The weak majorization conclusion allows infinite horizons; the stated strict conclusion is conditional on the horizon of the more balanced vector being finite. Uniform uniqueness above the critical value is false.

## Proof

### Known background: the heterogeneous-cycle horizon

The exact cycle criterion and stationary-mass transition are established in *A stationary-mass threshold for positivity of the theta method on directed cycles* [1]; a broader one-interval result for finite irreducible Markov generators is given in [2]. Here is a derivation of the cycle facts used in the comparison. For \(0<\theta<1\) and \(h>0\), write \(s=\theta h\), \(t_i=sr_i/(1+sr_i)\), \(t_*=\max_i t_i\), and \(P=\prod_i t_i\). If \(S\) is the cyclic successor matrix and \(T=\operatorname{diag}(t_i)S\), then \(I-sQ=\operatorname{diag}(1+sr_i)(I-T)\) and \(T^n=PI\). The finite geometric sum for \((I-T)^{-1}\) shows that \(R_s=(I-sQ)^{-1}\) has positive entries and \((R_s)_{ii}=(1-t_i)/(1-P)\). In \(M_\theta=R_s/\theta-(1-\theta)I/\theta\), all off-diagonal entries are therefore positive and the least diagonal condition is at a fastest vertex. Equivalently the criterion is
\[
t_*\le\theta+(1-\theta)P.
\]

To see the initial-interval conclusion, order the product factors as \(t_*,t_2,\ldots,t_n\) just for the next identity. Telescoping gives
\[
\frac{1-P}{1-t_*}=1+\sum_{j=2}^n\left(t_*\prod_{k=2}^{j-1} t_k\right)\frac{1-t_j}{1-t_*}.
\]
Each product in parentheses is positive and strictly increasing for \(s>0\); each final ratio equals \((1+sr_{\max})/(1+sr_j)\) and is nondecreasing. Thus the minimum resolvent diagonal, the reciprocal on the left, decreases strictly from 1 to \(\pi_{\min}=1/(r_{\max}\sum_j1/r_j)\) (the last limit also follows termwise in the displayed sum). For \(0<\theta<1\) the finite cutoff is consequently the unique positive crossing of the criterion at equality when \(\theta<1-\pi_{\min}\); otherwise the horizon is infinite. For \(\theta=0\), direct inspection of \(I+hQ\) gives \(1/r_{\max}\); for \(\theta=1\) the update is the nonnegative resolvent and the horizon is infinite.

### Strict comparison of the horizons

At any fixed \(s>0\), let \(f_s(x)=\log(sx/(1+sx))\). Its second derivative is
\[
f_s''(x)=-\frac{1+2sx}{x^2(1+sx)^2}<0.
\]
If \(r\) majorizes \(u\) and they are not permutations, strict Karamata yields \(\sum_j f_s(r_j)<\sum_j f_s(u_j)\), and hence \(P_r(s)<P_u(s)\). Also \(r_{\max}\ge u_{\max}\), so \(t_*(r,s)\ge t_*(u,s)\). Thus the right side of the positivity criterion is strictly smaller for \(r\) and the left side is no smaller, even for equal fastest rates. If \(H_\theta(u)\) is finite then it is positive and its criterion is saturated there. The criterion for \(r\) fails at that step, and interval structure with a closed finite endpoint implies \(H_\theta(r)<H_\theta(u)\). When \(H_\theta(u)=\infty\) the weak comparison holds automatically. Permutations leave the criterion unchanged.

### Budget transition

Every positive rate vector of total \(B\) majorizes the uniform vector. For \(0<\theta<(n-1)/n\) the uniform horizon is finite, so strict comparison makes it the unique optimum. At \(\theta=0\), minimizing \(r_{\max}\) at fixed sum likewise uniquely selects uniformity. At \(\theta=(n-1)/n\) the uniform stationary masses equal \(1/n\); for a nonuniform vector \(r_{\max}\sum_j 1/r_j>n\), so \(\pi_{\min}<1/n\), forcing a finite horizon. For \((n-1)/n<\theta<1\), the stationary-mass criterion remains satisfied on a neighborhood of the uniform vector by continuity, so infinitely many nonuniform rates share its infinite horizon. At \(\theta=1\) every rate vector has infinite horizon. In the finite uniform regime, substituting \(t_i=t\) in the equality criterion gives the stated root and step length; uniqueness in \((0,1)\) follows from the unique finite crossing and the strictly increasing bijection \(s\mapsto s\rho/(1+s\rho)\).

## Verification

The all-rate comparison is analytical: strict concavity controls the cycle product while the maximal rate moves in the opposite direction in the admissibility inequality. The unchanged standard-library `verify.py` in the accompanying package may be run with Python 3.9 or newer. It checks the cycle identities by exact rational matrix inversion and includes 55 strict product comparisons at fixed budgets, with expected final line `VERIFY_OK exact_checks= 1065`. Those checks are finite corroboration, not a proof of majorization or an originality certificate.

## Relationship to prior work and limitations

The new claim considered here is the strict fixed-sum rate comparison on this cycle, together with its optimal-allocation consequences. The exact heterogeneous-cycle horizon and its stationary-mass threshold are credited to [1]; the general Markov-chain one-interval law and the reversible Crank–Nicolson resolvent test are not claims of this note. Karamata's inequality is standard. The periodic centered-advection theta discretizations in [3] have a different signed spatial operator, so their thresholds do not settle the rate comparison for this positive one-way generator. The formulas here are specific to positive rates and a single directed cycle. No publication priority is asserted.

## References

1. *A stationary-mass threshold for positivity of the theta method on directed cycles*, Resultary record `eb886aea6d4c`.
2. *Stationary-mass positivity frontier for the theta method on finite Markov generators*, Resultary record `e98f7c7419d6`.
3. Y. Hadjimichael, D. I. Ketcheson, and L. Lóczi, *Positivity Preservation of Implicit Discretizations of the Advection Equation*, arXiv:2105.07403.
