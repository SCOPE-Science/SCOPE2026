# Same-model review

Same-model review: passed. Cross-model review: not yet performed.

## Correctness

**PASS.**

The change-of-measure identity was checked directly. Under the exponential
tilt at \(t_n\), the Bernoulli parameters become
\[
q_{i,n}=\frac{p_{i,n}e^{t_n}}
{1-p_{i,n}+p_{i,n}e^{t_n}},
\]
their total mean is exactly \(nr\), and their total variance is \(nv_n\).
For \(m_n=\lfloor nr\rfloor=nr-\theta_n\),
\[
\mathbb P(S_n=m_n-j)
=
e^{-nI_n(r)}e^{t_n(\theta_n+j)}
\mathbb Q_n(S_n=nr-\theta_n-j),
\]
so the stop-loss transform reduces to a geometrically weighted local
probability sum.

The balance and fixed-separation assumptions keep both the original and
tilted Bernoulli probabilities uniformly nondegenerate and keep the saddle
inside a compact subset of \(( -\infty,0)\). A uniform lattice local CLT
therefore gives the stated central mass uniformly over logarithmic
displacements, while the geometric tilt controls the remaining sum. The
weighted geometric series evaluates to the displayed coefficient
\(C(t,\theta)\).

The homogeneous specialization was checked algebraically:
\(t=\log[r(1-p)/(p(1-r))]\), \(v=r(1-r)\), and
\(I=D(r\|p)\). Its prefactor agrees with the first coefficient in
Elezović's binomial prescribed-center expansion, including the lattice
defect.

The heterogeneity inequality was checked independently from the asymptotic
argument. For the homogeneous lower-tail saddle \(t_0<0\),
\[
h(x)=\log(1-x+xe^{t_0})
\]
has
\[
h''(x)=-
\frac{(1-e^{t_0})^2}
{(1-(1-e^{t_0})x)^2}
\le -(1-e^{t_0})^2.
\]
Strong concavity and the zero average of \(p_{i,n}-\bar p_n\) yield the
claimed quadratic gap, and complementing Bernoulli variables gives the
upper-tail formula.

## Originality

**PASS, to the best of our knowledge.**

Several nearby results substantially constrain the originality claim.

- Hoeffding's 1956 theorem already shows that, at fixed mean, the
  equal-probability binomial maximizes expectations of convex functions.
  Thus the qualitative stop-loss comparison is classical and is not
  claimed as new.
- Chaganty--Sethuraman strong and local large-deviation theory supplies
  general precise asymptotic machinery for non-identically distributed
  sums. The first theorem may therefore be viewed as an explicit
  specialization rather than a new general method.
- Madsen et al. explicitly study Poisson-binomial saddlepoint tails and
  state that, under mild regularity, their saddlepoint approximation has
  uniform relative error \(O(n^{-1})\). Hence neither Poisson-binomial
  saddlepoint approximation nor its relative accuracy is claimed as new.
- Čekanavičius gives asymptotic expansions for generalized Poisson-binomial
  approximation, and older actuarial work studies stop-loss distances for
  compound-Poisson approximations. These sources reinforce the need for a
  narrow claim.

Searches by `Poisson-binomial stop-loss`, `Poisson-binomial absolute
deviation prescribed center`, `Poisson-binomial large-deviation
majorization`, `heterogeneous Bernoulli stop-loss`, and equivalent
saddlepoint/rate-function wording did not locate a source stating the
specific combination proved here: the explicit prescribed-center
stop-loss lattice coefficient for a heterogeneous Bernoulli profile,
the empirical-profile limit, and the quantitative bound
\[
I_n(r)-D(r\|\bar p_n)
\ge
\frac{(\bar p_n-r)^2}
{2\bar p_n^2(1-r)^2}V_n
\]
with its upper-tail counterpart.

The most significant residual risk is that a general saddlepoint or
actuarial stop-loss theorem, after specialization, could reproduce the
first asymptotic. The detailed supplementary theorem of Madsen et al. was
not separately inspected beyond the main article's statement of its
\(O(n^{-1})\) relative-error result. The subscription-only full text of
Čekanavičius (1997) was not inspected; its abstract and bibliographic
context concern distributional approximation and asymptotic expansions.
Neither accessible description indicates the empirical-profile
heterogeneity exponent proved here, but this remains a scientific
originality risk.

## Value

**PASS.**

The result gives a closed first-order formula for prescribed-center
absolute deviations of balanced Poisson-binomial sums, directly extending
the newly explicit binomial coefficient to heterogeneous trials. More
importantly, it quantifies the effect of heterogeneity at the
large-deviation scale: variance among the success probabilities raises the
rate function by an explicit positive amount. This upgrades the classical
convex-order statement from qualitative domination to an exponential
penalty and supplies a profile-level description useful for triangular
arrays whose Bernoulli probabilities vary systematically.

## Sources inspected

- Elezović, *Absolute deviations of the binomial about a prescribed centre:
  the tail expansion in closed form*, arXiv:2609.19064.
- Hoeffding, *On the Distribution of the Number of Successes in Independent
  Trials*, including the statement that equal probabilities maximize
  strictly convex expectations at fixed mean.
- Chaganty and Sethuraman, 1993 and 1985 strong/local large-deviation
  theorems, at theorem/abstract level and bibliographic descriptions.
- Madsen, Hobolth, Jensen and Pedersen, *Significance evaluation in factor
  graphs*, including its Poisson-binomial saddlepoint section and the
  main-text statement of a uniform \(O(n^{-1})\) relative-error theorem.
- Tang and Tang, *The Poisson Binomial Distribution - Old & New*, as a
  broad literature survey.
- Čekanavičius, 1997, abstract and reference context; full subscription
  text was not inspected.

## Scientific limitations retained

The theorem is confined to uniformly nondegenerate Bernoulli arrays and
fixed large-deviation centers. It gives a conservative first-order error,
not a complete asymptotic expansion. The explicit heterogeneity constant is
not asserted optimal. Sparse, moderate-deviation, dependent, and
near-the-mean regimes remain outside the claim. General saddlepoint theory
may recover part of the first theorem by specialization.