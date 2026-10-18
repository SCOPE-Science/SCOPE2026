# A weight-independent sharp log-concavity phase boundary for two-shape Gamma mixtures

## Finding

Let \(g_{a,\lambda}(x)=\lambda^a x^{a-1}e^{-\lambda x}/\Gamma(a)\) for \(x>0\), and let
\[
f(x)=(1-w)g_{\alpha,\lambda}(x)+w g_{\beta,\lambda}(x),
\qquad 0<\alpha<\beta,\quad \lambda>0,\quad 0<w<1.
\]
Then the density \(f\) is log-concave on \((0,\infty)\) **if and only if**
\[
\boxed{\alpha\ge1\quad\text{and}\quad
\beta-\alpha\le1+2\sqrt{\alpha-1}.}
\]
Thus the classification is independent of the common rate and of the positive mixture weight. In particular, for any two distinct Erlang shapes \(m<n\), every strictly positive mixture of those two components is log-concave exactly when \(n-m\le1+2\sqrt{m-1}\). The maximal allowable stage gap is therefore of square-root order in the smaller shape.

There is an exact curvature refinement. Write \(d=\beta-\alpha\) and
\[
A=\frac{(1-w)\lambda^\alpha}{\Gamma(\alpha)},\quad
B=\frac{w\lambda^\beta}{\Gamma(\beta)},\quad
t=\frac BA x^d.
\]
For \(d>1\),
\[
\boxed{\sup_{x>0}x^2(\log f)''(x)=\frac{(d-1)^2}{4}-(\alpha-1),}
\]
and the supremum is attained at the unique location
\[
x_* = \left[\frac AB\frac{d-1}{d+1}\right]^{1/d}.
\]
If \(\alpha\ge1\), \(d>1\), and \(\alpha-1<(d-1)^2/4\), then \((\log f)''\) is strictly positive on exactly one nonempty interval and strictly negative outside its closure. At the equality threshold \(\alpha-1=(d-1)^2/4\), the curvature is nonpositive everywhere and vanishes at precisely \(x_*\).

## Assumptions and scope

The Gamma distribution is parameterized by positive shape \(a\) and **rate** \(\lambda\), not scale. Both components have exactly the same rate. The mixture weights are strictly interior, \(0<w<1\); at \(w=0\) or \(w=1\), the corresponding single Gamma density has the familiar log-concavity criterion that its shape is at least one. Log-concavity means concavity of \(\log f\) throughout the open positive half-line, equivalently \((\log f)''\le0\) there because the density is strictly positive and smooth.

## Proof

Factor the density as
\[
f(x)=e^{-\lambda x}x^{\alpha-1}(A+Bx^d),\qquad A,B,d>0.
\]
The linear term in the logarithm makes no contribution to the second derivative. Direct differentiation gives the exact identity
\[
\boxed{
x^2(\log f)''(x)
=-(\alpha-1)+\frac{dt(d-1-t)}{(1+t)^2}.}
\tag{1}
\]
This can also be rewritten without any inequality as the perfect-square identity
\[
\boxed{
x^2(\log f)''(x)
=\frac{(d-1)^2}{4}-(\alpha-1)
-\frac{((d+1)t-(d-1))^2}{4(1+t)^2}.}
\tag{2}
\]
Because \(t=(B/A)x^d\) runs bijectively through \((0,\infty)\), these identities control the curvature at every positive argument, for **all** permitted weights and rates.

If \(0<\alpha<1\), then the limit of the left side of (1) as \(x\downarrow0\) is \(1-\alpha>0\). Therefore the density is not log-concave, independently of \(d\). Suppose henceforth \(\alpha\ge1\). If \(0<d\le1\), the last fraction in (1) is strictly negative for every \(t>0\), and log-concavity follows (indeed the curvature is strictly negative).

Now let \(d>1\). Differentiating the variable portion of (1) gives
\[
\frac{d}{dt}\left[\frac{dt(d-1-t)}{(1+t)^2}\right]
=\frac{d((d-1)-(d+1)t)}{(1+t)^3}.
\]
It has a unique global maximum at \(t_*=(d-1)/(d+1)>0\), with value \((d-1)^2/4\). Equivalently, (2) exhibits the same maximum by a vanishing square. Consequently \((\log f)''\le0\) for every \(x>0\) exactly when \(\alpha-1\ge(d-1)^2/4\). Combining this condition with \(0<d\le1\) yields the announced criterion \(d\le1+2\sqrt{\alpha-1}\), and proves the sharp attained curvature formula.

For completeness, the exact failure interval is explicit. In the case \(\alpha\ge1\), \(d>1\), and \(c:=\alpha-1<(d-1)^2/4\), the curvature's numerator after multiplication by the strictly positive \((1+t)^2\) is
\[
-(d+c)t^2+[d(d-1)-2c]t-c.
\]
Its two roots are
\[
t_\pm=\frac{d(d-1)-2c\pm d\sqrt{(d-1)^2-4c}}{2(d+c)},
\quad0\le t_-<t_+,
\]
where \(t_-=0\) only if \(\alpha=1\). The polynomial is strictly positive exactly for \(t_-<t<t_+\), hence \((\log f)''>0\) precisely for
\[
\left(\left[\frac AB t_-\right]^{1/d},
\left[\frac AB t_+\right]^{1/d}\right).
\]
The curvature is strictly negative everywhere else on \((0,\infty)\) outside the two endpoints. When the discriminant vanishes, the roots coincide at \(t_*\), proving the boundary statement.

As an exact instance, a positive common-rate mixture of Gamma shapes \(2\) and \(5\) is log-concave for every mixing weight (boundary equality). For shapes \(2\) and \(6\), take the unique \(x\) with \(t=3/5\); then \(x^2(\log f)''=5/4>0\) for **every** interior mixing weight. The latter failure persists as either weight tends to zero, even though the mixtures converge in total variation to their log-concave endpoint components. This follows directly from the explicit mixture formula and requires no limiting curvature interchange.

## Verification

The included standalone script `check_gamma_mixture.py` uses only Python's standard library and checks the curvature identity in two independently evaluated forms using exact rational arithmetic for a broad family of integer-shape and positive rational parameter instances. It also checks the sharp maximizing relation and three boundary/counterexample cases. Execute with `python3 check_gamma_mixture.py` from the directory containing the extracted files. The observed result was `PASS: 1013 exact-rational checks and three sharp analytic examples`. These finite computations validate algebraic instances, **not** all real parameters; the proof above establishes the universal assertions.

## Relationship to prior work

Li, Lee, and Kottas (2022) build survival-density models from common-scale Erlang components with varying integer shapes and time-dependent hazard-mixture weights; their definition motivates asking exactly when this simple two-component family can satisfy a global log-concavity shape constraint. Their modeling and convergence results do not furnish the sharp shape-gap test here. Mu (2013/2015) proves preservation of log-concavity for certain Beta mixtures when the mixing weights are log-concave, a different component family and a sufficient hypothesis that does not resolve widely separated two-point Erlang shape support. Yu (2009) studies stochastic orders and Gamma **scale** mixtures with fixed shape, not Gamma **shape** mixtures with a fixed rate. None of these statements logically implies the exact weight-independent curvature supremum and if-and-only-if boundary for the present object.

## Limitations

The theorem covers exactly two positive-weight Gamma components sharing a common rate. It does not classify mixtures with more than two components, unequal rates, arbitrary continuous mixing laws, or the hazard monotonicity of non-log-concave mixtures. Log-concavity is a sufficient, not necessary, condition for increasing hazard. The work is a self-contained analytic classification and has not received independent audit. The literature comparison cannot exclude an earlier equivalent identity hidden under a different formulation.

## References

1. Y. Li, J. Lee, and A. Kottas, *Bayesian Nonparametric Erlang Mixture Modeling for Survival Analysis*, arXiv:2211.08652v1, first submitted 2022-11-16. https://arxiv.org/abs/2211.08652
2. X. Mu, *Log-concavity of a Mixture of Beta Distributions*, arXiv:1312.2166v1 (2013); *Statistics & Probability Letters* 99 (2015), 125–130. https://arxiv.org/abs/1312.2166
3. Y. Yu, *Stochastic Ordering of Exponential Family Distributions and Their Mixtures*, *Journal of Applied Probability* 46 (2009), 244–254. https://doi.org/10.1239/jap/1238592127
