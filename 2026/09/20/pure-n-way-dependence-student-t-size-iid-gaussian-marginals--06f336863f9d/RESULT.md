# Pure n-way dependence can double Student t size despite iid Gaussian proper marginals

**Same-model review: passed. Independent audit: not yet performed.**

## Result

Let \(\phi\) be the standard normal density. For \(n\ge2\) and
\(\theta\in[-1,1]\), define an absolutely continuous distribution on
\(\mathbb R^n\) by
\[
f_\theta(x_1,\ldots,x_n)
=
\prod_{i=1}^n \phi(x_i)
\left(
1+\theta\prod_{i=1}^n \operatorname{sgn}(x_i)
\right).
\]
(The value of \(\operatorname{sgn}(0)\) is immaterial.)

Every proper subvector of \((X_1,\ldots,X_n)\) is a vector of mutually
independent \(N(0,1)\) variables. In particular, the observations are
\((n-1)\)-wise independent and each marginal is exactly standard normal.
Nevertheless the ordinary one-sample Student statistic
\[
T_n=\frac{\sqrt n\,\bar X}{S},
\qquad
S^2=\frac{1}{n-1}\sum_{i=1}^n(X_i-\bar X)^2,
\]
need not have its usual \(t_{n-1}\) distribution.

Write
\[
q_\nu(c)=\Pr(t_\nu>c).
\]
For every \(c\ge n-1\),
\[
\boxed{\Pr_\theta(T_n>c)=(1+\theta)q_{n-1}(c)}
\]
and
\[
\boxed{\Pr_\theta(T_n<-c)=\left(1+(-1)^n\theta\right)q_{n-1}(c).}
\]
Hence, for even \(n\),
\[
\boxed{\Pr_\theta(|T_n|>c)=2(1+\theta)q_{n-1}(c),\qquad c\ge n-1.}
\]

The threshold \(n-1\) is sharp for the deterministic sign implication used
below: for every \(c<n-1\) there are samples with at least one nonpositive
coordinate and \(T_n>c\).

### A conventional 5% test with four observations

Take \(n=4\). Since
\[
2\Pr(t_3>3)
=
\frac13-\frac{\sqrt3}{2\pi}
=
0.057668885622\ldots>0.05,
\]
the usual two-sided 5% critical value \(t_{3,0.975}=3.182446\ldots\)
lies above the threshold \(3\). Therefore the conventional two-sided
one-sample t-test has exact null rejection probability
\[
\boxed{\Pr_\theta\!\left(|T_4|>t_{3,0.975}\right)=0.05(1+\theta).}
\]
As \(\theta\) ranges over \([-1,1]\), the actual size ranges continuously
from \(0\) to \(0.10\), even though every triple among the four
observations is exactly an iid \(N(0,1)\) sample.

Equivalently, the usual 95% t confidence interval for the mean can have
coverage anywhere from \(90\%\) to \(100\%\) within this family, while
every proper subsample has exactly the classical iid Gaussian law.

More generally, for even \(n\), if a two-sided nominal level \(\alpha\)
satisfies
\[
\alpha\le 2\Pr(t_{n-1}>n-1),
\]
then its exact size in this family is \((1+\theta)\alpha\). For an upper
one-sided test, for any \(n\), the same statement holds with the condition
\[
\alpha\le \Pr(t_{n-1}>n-1).
\]

## Proof

### 1. Every proper marginal is iid standard normal

The density is nonnegative for \(|\theta|\le1\). Also
\[
\int_{\mathbb R}\phi(x)\operatorname{sgn}(x)\,dx=0,
\]
so \(f_\theta\) integrates to one.

Now integrate out any coordinate, say \(x_j\). The interaction term
contains the factor
\[
\int_{\mathbb R}\phi(x_j)\operatorname{sgn}(x_j)\,dx_j=0,
\]
and therefore disappears. The remaining marginal density is exactly the
product of the corresponding standard normal densities. Repeating this
argument shows that every subvector of size at most \(n-1\) is mutually
independent and standard normal.

### 2. A sharp geometric threshold for the Student statistic

Consider deterministic observations \(x_1,\ldots,x_n\) with mean
\(m>0\). Suppose at least one coordinate is nonpositive. Subject to the
fixed-sum constraint \(\sum_i x_i=nm\) and the condition \(x_j\le0\),
the squared deviation
\[
Q=\sum_{i=1}^n(x_i-m)^2
\]
is minimized when \(x_j=0\) and all other coordinates equal
\(nm/(n-1)\). Thus
\[
Q\ge m^2+(n-1)\left(\frac{m}{n-1}\right)^2
=\frac{n}{n-1}m^2.
\]
Consequently,
\[
S^2=\frac{Q}{n-1}\ge\frac{n}{(n-1)^2}m^2
\]
and hence
\[
T_n=\frac{\sqrt n\,m}{S}\le n-1.
\]
Therefore
\[
\{T_n>n-1\}\subset\{X_1>0,\ldots,X_n>0\}.
\]
By sign reversal,
\[
\{T_n<-(n-1)\}\subset\{X_1<0,\ldots,X_n<0\}.
\]

The constant is best possible. Equality in the variance bound occurs at
\[
(0,nm/(n-1),\ldots,nm/(n-1)),
\]
for which \(T_n=n-1\). A small negative perturbation of the zero coordinate,
followed by a compensating adjustment of the others, gives mixed-sign samples
with \(T_n\) arbitrarily close to \(n-1\) from below.

### 3. Exact tail rescaling

Under \(\theta=0\), the observations are iid \(N(0,1)\), so
\(T_n\sim t_{n-1}\).

On the event \(\{T_n>c\}\) with \(c\ge n-1\), all coordinates are positive,
and therefore
\[
\prod_{i=1}^n\operatorname{sgn}(X_i)=1.
\]
On this entire event the density \(f_\theta\) is exactly
\((1+\theta)f_0\). Hence
\[
\Pr_\theta(T_n>c)
=(1+\theta)\Pr_0(T_n>c)
=(1+\theta)q_{n-1}(c).
\]

Similarly, on \(\{T_n<-c\}\), all coordinates are negative, so the sign
product is \((-1)^n\). Therefore
\[
\Pr_\theta(T_n<-c)
=
\left(1+(-1)^n\theta\right)q_{n-1}(c).
\]
Adding the two tails gives the even-\(n\) formula. For odd \(n\), the two
corrections cancel in the two-sided high-threshold tail.

For \(n=4\), the \(t_3\) density integrates to
\[
F_{t_3}(x)
=
\frac12+\frac1\pi\arctan\!\left(\frac{x}{\sqrt3}\right)
+\frac{\sqrt3\,x}{\pi(x^2+3)}.
\]
Substituting \(x=3\) yields
\[
2\Pr(t_3>3)=\frac13-\frac{\sqrt3}{2\pi}>0.05,
\]
which proves the stated 5% example.

## Relation to prior literature

Student's 1908 derivation establishes the classical small-sample
studentization law for samples from a normal population and explicitly
uses the behavior of the sample mean and sample standard deviation.
The present construction keeps every proper subsample exactly iid normal
but changes the full \(n\)-way law.

The multiplicative density used here is a pure highest-order member of the
Sarmanov family: Sarmanov-type models use product marginal densities
multiplied by centered interaction kernels, and multivariate extensions
allow higher-order interaction terms. Thus the dependence family itself is
not claimed as new.

Limited-independence parity phenomena are also established independently
of this problem. Natarajan, Ramachandra and Tan (2023) characterize
probability measures for \(n\) events under \((n-1)\)-wise independence.
Schaufele (1975) gives an earlier statistical example in which pairwise but
not joint independence changes exact error probabilities in a stepwise
regression problem.

The contribution here is the explicit connection to the one-sample
Student statistic: the sharp geometric threshold \(n-1\), the exact tail
multipliers above that threshold, and in particular the four-observation
example where every triple is iid \(N(0,1)\) but the conventional
two-sided 5% t-test can have any size from \(0\) to \(10\%\).

## Limitations

The result gives an explicit family and exact distortion formulas; it does
not claim that the displayed factors are global extrema over all
\((n-1)\)-wise independent standard-normal vectors. The clean two-sided
formula above the threshold \(n-1\) depends on parity: for odd \(n\), this
particular sign interaction cancels between the two tails.

The literature search did not locate an earlier statement of these exact
Student-tail formulas or the \(n=4\) 5%-to-10% example. However, equivalent
formulations may exist in older work on multivariate Sarmanov
distributions, exact robustness of Student statistics, or higher-order
interaction models under different terminology. Only claims supported by
the sources inspected are made here.

## Reproducibility

`artifacts/check_student_t.py` uses only the Python standard library. It
checks the exact proper sign marginals for the endpoint interactions,
stress-tests the deterministic threshold implication on a finite grid,
computes the closed-form \(t_3\) tail at \(3\), and obtains the usual 5%
two-sided \(t_3\) critical value by bisection of its closed-form CDF.

`artifacts/verification_output.txt` records the successful output.

## References

- Student [W. S. Gosset] (1908). *The Probable Error of a Mean*.
  Biometrika 6(1), 1-25.
  https://doi.org/10.1093/biomet/6.1.1
- Lee, M.-L. T. (1996). *Properties and applications of the Sarmanov
  family of bivariate distributions*. Communications in Statistics -
  Theory and Methods 25(6), 1207-1222.
  https://doi.org/10.1080/03610929608831759
- Schaufele, R. A. (1975). *An Application of Pairwise Independence of
  Random Variables to Regression Analysis*. Canadian Mathematical
  Bulletin 18(3), 397-404.
  https://doi.org/10.4153/CMB-1975-073-5
- Natarajan, K., Ramachandra, A. K., and Tan, C. (2023).
  *Probability bounds for n random events under (n-1)-wise independence*.
  Operations Research Letters 51(1), 116-122.
  https://doi.org/10.1016/j.orl.2023.01.004
- *Rank-Based Multivariate Sarmanov for Modeling Dependence between Loss
  Reserves* (2023), for an explicit modern presentation of the
  multivariate Sarmanov interaction form.
  https://www.mdpi.com/2227-9091/11/11/187
