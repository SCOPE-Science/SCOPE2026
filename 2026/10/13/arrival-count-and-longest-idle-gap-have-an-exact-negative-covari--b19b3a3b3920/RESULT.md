# Arrival count and longest idle gap have an exact negative covariance
## Finding
Let
\[
(N(s))_{s\ge0}
\]
be a homogeneous Poisson process of rate
\[
\lambda>0,
\]
and fix
\[
t>0.
\]
Write
\[
\mu=\lambda t.
\]

Let
\[
0=T_0<T_1<\cdots<T_{N(t)}
\]
be the arrival epochs before time \(t\). Include the terminal censoring point
\[
T_{N(t)+1}=t,
\]
and define the longest observed gap by
\[
L_t=\max_{1\le j\le N(t)+1}(T_j-T_{j-1}).
\]

Define the entire exponential integral
\[
\operatorname{Ein}(x)
=
\int_0^x\frac{1-e^{-u}}u\,du.
\]

Then, for every integer \(n\ge0\),
\[
\boxed{
\mathbb E[L_t\mid N(t)=n]
=
t\frac{H_{n+1}}{n+1},
}
\]
where
\[
H_m=\sum_{j=1}^m\frac1j.
\]
Consequently,
\[
\boxed{
\mathbb E L_t
=
t\frac{\operatorname{Ein}(\mu)}{\mu}.
}
\]

The exact arrival-count/longest-gap covariance is
\[
\boxed{
\operatorname{Cov}(N(t),L_t)
=
\frac{t}{\mu}
\left(
1-e^{-\mu}-\operatorname{Ein}(\mu)
\right).
}
\]
It is strictly negative for every
\[
\mu>0.
\]

For small expected count,
\[
\operatorname{Cov}(N(t),L_t)
=
-\frac{\lambda t^2}{4}
+O(\lambda^2t^3).
\]
For large expected count,
\[
\boxed{
\operatorname{Cov}(N(t),L_t)
=
-\frac1\lambda
\left(
\log(\lambda t)+\gamma-1+o(1)
\right),
}
\]
where \(\gamma\) is Euler's constant.

Thus the longest idle interval becomes shorter as the realized count rises, and the exact mixed moment is governed by a single classical entire function.

## Assumptions and scope
The process is homogeneous Poisson with constant rate \(\lambda\). The statistic \(L_t\) includes both boundary gaps, so when \(N(t)=0\),
\[
L_t=t.
\]

The result concerns the fixed observation window \([0,t]\). It is not a statement about the longest completed interarrival interval before \(t\) when the terminal censored gap is excluded.

No independence between \(N(t)\) and \(L_t\) is asserted. Their dependence is exactly the object quantified above.

## Proof
Conditional on
\[
N(t)=n,
\]
the \(n\) arrival times are distributed as the order statistics of \(n\) independent uniform points on \([0,t]\). Therefore the \(n+1\) normalized gaps
\[
\left(
\frac{T_1-T_0}{t},
\ldots,
\frac{T_{n+1}-T_n}{t}
\right)
\]
are uniform on the probability simplex, equivalently
\[
\operatorname{Dirichlet}(1,\ldots,1).
\]

Put
\[
m=n+1
\]
and let
\[
M_m=\max(D_1,\ldots,D_m)
\]
for a uniform simplex vector. Inclusion-exclusion gives, for \(0\le x\le1\),
\[
\Pr(M_m>x)
=
\sum_{j=1}^m
(-1)^{j+1}
\binom mj
(1-jx)_+^{m-1}.
\]
Integrating the tail,
\[
\begin{aligned}
\mathbb E M_m
&=
\sum_{j=1}^m
(-1)^{j+1}
\binom mj
\int_0^{1/j}(1-jx)^{m-1}\,dx\\
&=
\frac1m
\sum_{j=1}^m
(-1)^{j+1}
\binom mj\frac1j.
\end{aligned}
\]
The binomial-harmonic identity
\[
\sum_{j=1}^m
(-1)^{j+1}
\binom mj\frac1j
=
H_m
\]
follows by integrating
\[
\frac{1-(1-z)^m}{z}
\]
over \(0\le z\le1\). Hence
\[
\mathbb E[L_t\mid N(t)=n]
=
t\frac{H_{n+1}}{n+1}.
\]

Now use
\[
N(t)\sim\operatorname{Poisson}(\mu).
\]
Then
\[
\begin{aligned}
\mathbb E L_t
&=
te^{-\mu}
\sum_{n=0}^{\infty}
\frac{\mu^n}{n!}
\frac{H_{n+1}}{n+1}\\
&=
\frac{t e^{-\mu}}{\mu}
\sum_{m=1}^{\infty}
H_m\frac{\mu^m}{m!}.
\end{aligned}
\]
The exponential generating function
\[
\sum_{m=1}^{\infty}
H_m\frac{x^m}{m!}
=
e^x\operatorname{Ein}(x)
\]
therefore gives
\[
\mathbb E L_t
=
t\frac{\operatorname{Ein}(\mu)}{\mu}.
\]

For any function \(g\) not depending on \(\mu\), if
\[
N\sim\operatorname{Poisson}(\mu),
\]
then differentiation of the Poisson mass function gives
\[
\operatorname{Cov}(N,g(N))
=
\mu\frac{d}{d\mu}\mathbb E[g(N)].
\]
Since \(N(t)\) is fixed under conditioning,
\[
\operatorname{Cov}(N(t),L_t)
=
\operatorname{Cov}\!\left(
N(t),
\mathbb E[L_t\mid N(t)]
\right).
\]
Thus
\[
\begin{aligned}
\operatorname{Cov}(N(t),L_t)
&=
\mu\frac{d}{d\mu}
\left(
t\frac{\operatorname{Ein}(\mu)}{\mu}
\right)\\
&=
\frac{t}{\mu}
\left(
1-e^{-\mu}-\operatorname{Ein}(\mu)
\right),
\end{aligned}
\]
because
\[
\operatorname{Ein}'(\mu)
=
\frac{1-e^{-\mu}}{\mu}.
\]

To determine the sign, set
\[
h(\mu)
=
\operatorname{Ein}(\mu)-(1-e^{-\mu}).
\]
Then
\[
h(0)=0
\]
and
\[
h'(\mu)
=
\frac{1-(1+\mu)e^{-\mu}}{\mu}
>0
\]
for every \(\mu>0\), since
\[
e^\mu>1+\mu.
\]
Therefore
\[
h(\mu)>0,
\]
which proves the strict negative covariance.

Finally,
\[
\operatorname{Ein}(\mu)
=
\mu-\frac{\mu^2}{4}+O(\mu^3)
\]
as \(\mu\downarrow0\), while
\[
\operatorname{Ein}(\mu)
=
\log\mu+\gamma+o(1)
\]
as \(\mu\to\infty\). Substitution proves the two asymptotic formulas.

## Verification
The accompanying `checker.py` uses exact rational arithmetic to verify the finite binomial-harmonic identity for many simplex dimensions and independently checks the coefficient identity
\[
e^{-x}
\sum_{m\ge1}H_m\frac{x^m}{m!}
=
\operatorname{Ein}(x)
\]
through a long exact power-series truncation.

It also verifies, coefficient by coefficient, that differentiating the expected-longest-gap series produces the stated covariance series. These finite algebraic checks supplement the all-parameter analytic proof.

## Relationship to prior work
Onn and Weissman study a vector uniformly distributed on the probability simplex, identify it with uniform spacings, and derive the exact first moment of its largest coordinate. That supplies the conditional mean used here.

Omwonylee studies the longest gap in a homogeneous Poisson process and explicitly connects it with Poissonized maximal uniform spacing. The paper develops exact distributional estimates and large-deviation asymptotics for the longest gap.

The present result asks a different joint question: how the longest gap covaries with the realized arrival count in the same observation window. The conditional simplex mean, followed by the Poisson score identity, yields the exact covariance and its strict sign. Targeted searches did not locate this mixed moment or the equivalent derivative formula.

## Limitations
The terminal boundary gap is included. Excluding it changes the conditional spacing problem and the formula.

Homogeneity is essential to the uniform-order-statistic conditioning. For an inhomogeneous Poisson process, conditioning on the count gives independent samples from the normalized cumulative intensity rather than uniform time spacings, so the longest time gap no longer has the same simplex law.

Older random-division, maximal-spacing, or Poisson-gap literature may contain the same mixed moment under another notation. The inspected sources establish the marginal and conditional ingredients but do not state the count-gap covariance.

## References
1. S. Onn and I. Weissman, “Generating uniform random vectors over a simplex with implications to the volume of a certain polytope and to multivariate extremes,” *Annals of Operations Research* 189 (2011), 331–342. DOI: 10.1007/s10479-009-0567-7. First published online 2009-05-19.
2. J. O. Omwonylee, “Large Deviations for the Longest Gap in Poisson Processes,” *Bulletin of the Australian Mathematical Society* 101 (2020), 146–156. DOI: 10.1017/S0004972719000972. First published online 2019-10-16.
