# Precise stop-loss large deviations for Poisson-binomial sums

## Statement

Let
\[
S_n=\sum_{i=1}^n X_{i,n},\qquad X_{i,n}\sim \operatorname{Bernoulli}(p_{i,n})
\]
be independent, and assume that for some fixed \(\varepsilon,\eta>0\),
\[
\varepsilon\le p_{i,n}\le 1-\varepsilon,\qquad
\varepsilon\le r\le 1-\varepsilon,\qquad
\bar p_n-r\ge \eta,
\]
where
\[
\bar p_n=\frac1n\sum_{i=1}^n p_{i,n}.
\]
Thus \(nr\) is a prescribed center a fixed distance below the mean.

Set
\[
\psi_n(t)=\frac1n\sum_{i=1}^n
\log(1-p_{i,n}+p_{i,n}e^t).
\]
There is a unique \(t_n<0\) satisfying
\[
\psi_n'(t_n)=r.
\]
Define
\[
I_n(r)=rt_n-\psi_n(t_n),\qquad
v_n=\psi_n''(t_n),\qquad
\theta_n=\{nr\}.
\]
Finally, for \(t<0\) and \(0\le\theta<1\), let
\[
C(t,\theta)
=
e^{t\theta}
\left(
\frac{\theta}{1-e^t}
+
\frac{e^t}{(1-e^t)^2}
\right).
\]

### Theorem 1: precise lower stop-loss asymptotics

Uniformly over all arrays satisfying the displayed balance and separation
conditions,
\[
\mathbb E[(nr-S_n)^+]
=
\frac{e^{-nI_n(r)}}{\sqrt{2\pi n v_n}}\,
C(t_n,\theta_n)
\left(1+O(n^{-1/2})\right).
\]

Consequently,
\[
\mathbb E|S_n-nr|
=
n(\bar p_n-r)
+
\frac{2e^{-nI_n(r)}}{\sqrt{2\pi n v_n}}\,
C(t_n,\theta_n)
\left(1+O(n^{-1/2})\right).
\]

The corresponding upper-tail formulas for \(r>\bar p_n\) follow by replacing
\(X_{i,n}\) by \(1-X_{i,n}\) and \(r\) by \(1-r\).

### Theorem 2: profile limit

Suppose in addition that the empirical probability measures
\[
\nu_n=\frac1n\sum_{i=1}^n\delta_{p_{i,n}}
\]
converge weakly to a probability measure \(\nu\) supported in
\([\varepsilon,1-\varepsilon]\), and that
\[
\int x\,d\nu(x)>r.
\]
Let \(t_\nu<0\) be the unique solution of
\[
r=
\int
\frac{xe^{t_\nu}}{1-x+xe^{t_\nu}}
\,d\nu(x).
\]
Then
\[
I_n(r)\longrightarrow
I_\nu(r)
=
rt_\nu-
\int\log(1-x+xe^{t_\nu})\,d\nu(x),
\]
and
\[
v_n\longrightarrow
v_\nu
=
\int q_\nu(x)(1-q_\nu(x))\,d\nu(x),
\qquad
q_\nu(x)=
\frac{xe^{t_\nu}}{1-x+xe^{t_\nu}}.
\]
Along every subsequence for which \(\theta_n\to\theta\),
\[
\sqrt n\,e^{nI_n(r)}
\mathbb E[(nr-S_n)^+]
\longrightarrow
\frac{C(t_\nu,\theta)}{\sqrt{2\pi v_\nu}}.
\]

Thus an arbitrary balanced heterogeneous Bernoulli profile has an explicit
large-deviation rate, Gaussian saddle curvature, and lattice-prefactor limit.

### Theorem 3: an exponential heterogeneity gap

For each \(n\), let \(p=\bar p_n\) and
\[
V_n=\frac1n\sum_{i=1}^n(p_{i,n}-p)^2.
\]
Then for every \(r<p\),
\[
I_n(r)
\ge
D(r\|p)
+
\frac{(p-r)^2}{2p^2(1-r)^2}\,V_n,
\]
where
\[
D(r\|p)
=
r\log\frac rp+
(1-r)\log\frac{1-r}{1-p}.
\]

For \(r>p\), the symmetric statement is
\[
I_n(r)
\ge
D(r\|p)
+
\frac{(r-p)^2}{2r^2(1-p)^2}\,V_n.
\]

In particular, under the same balance and separation conditions, if
\(B_n\sim\operatorname{Bin}(n,\bar p_n)\), then
\[
\frac{\mathbb E[(nr-S_n)^+]}
{\mathbb E[(nr-B_n)^+]}
\le
K\exp\!\left[
-n\,\frac{(\bar p_n-r)^2}
{2\bar p_n^2(1-r)^2}V_n
\right]
\]
for all sufficiently large \(n\), with \(K\) depending only on the fixed
balance and separation constants. Hence persistent heterogeneity,
\(\liminf V_n>0\), makes the lower stop-loss exponentially smaller than in
the equal-probability binomial with the same mean.

Hoeffding's classical convex-order theorem already implies the qualitative
finite-\(n\) inequality that the equal-probability binomial maximizes every
convex functional, including stop-loss. The statement above gives a
quantitative large-deviation refinement: it identifies an explicit
exponential penalty in the empirical variance of the Bernoulli
probabilities.

## Proof

### 1. Exponential tilting

For fixed \(n\), define the tilted law \(\mathbb Q_n\) by
\[
\frac{d\mathbb Q_n}{d\mathbb P}
=
\exp\{t_n S_n-n\psi_n(t_n)\}.
\]
Under \(\mathbb Q_n\), the summands remain independent Bernoulli variables
with parameters
\[
q_{i,n}
=
\frac{p_{i,n}e^{t_n}}
{1-p_{i,n}+p_{i,n}e^{t_n}}.
\]
By the saddle equation,
\[
\sum_iq_{i,n}=nr,
\qquad
\sum_iq_{i,n}(1-q_{i,n})=nv_n.
\]

The balance and fixed mean-separation assumptions force \(t_n\) into a
compact subinterval of \(( -\infty,0)\). They also keep all tilted
probabilities \(q_{i,n}\) uniformly away from \(0\) and \(1\); in
particular \(v_n\) is bounded above and below by positive constants.

Let
\[
m_n=\lfloor nr\rfloor=nr-\theta_n.
\]
For \(j\ge0\), change of measure gives the exact identity
\[
\mathbb P(S_n=m_n-j)
=
e^{-nI_n(r)}
e^{t_n(\theta_n+j)}
\mathbb Q_n(S_n=nr-\theta_n-j).
\]
Therefore
\[
\mathbb E[(nr-S_n)^+]
=
e^{-nI_n(r)}e^{t_n\theta_n}
\sum_{j\ge0}
(\theta_n+j)e^{t_nj}
\mathbb Q_n(S_n=nr-\theta_n-j).
\]

### 2. Local central limit evaluation

For triangular arrays of independent Bernoulli variables whose success
probabilities stay uniformly inside \((0,1)\), the lattice local central
limit theorem is uniform at bounded and logarithmic displacements from the
mean. Hence, uniformly for \(0\le j\le A\log n\),
\[
\mathbb Q_n(S_n=nr-\theta_n-j)
=
\frac1{\sqrt{2\pi n v_n}}
\left(1+O(n^{-1/2})\right).
\]
Because \(t_n\) is uniformly bounded above by a negative constant, the
geometric factor \(e^{t_nj}\) makes the contribution of \(j>A\log n\)
smaller than the displayed main term when \(A\) is chosen sufficiently
large.

It remains only to sum
\[
\sum_{j\ge0}(\theta+j)e^{tj}
=
\frac{\theta}{1-e^t}
+
\frac{e^t}{(1-e^t)^2}.
\]
This proves Theorem 1.

The exact identity
\[
\mathbb E|S_n-nr|
=
n(\bar p_n-r)+2\mathbb E[(nr-S_n)^+]
\]
then gives the absolute-deviation expansion.

### 3. Profile convergence

Weak convergence of \(\nu_n\) on the compact interval
\([\varepsilon,1-\varepsilon]\) yields locally uniform convergence of
\[
\psi_n(t)
=
\int\log(1-x+xe^t)\,d\nu_n(x)
\]
and its first two derivatives. Strict convexity and the fixed separation
from the mean imply
\[
t_n\to t_\nu.
\]
Substitution then gives
\[
I_n(r)\to I_\nu(r),\qquad
v_n\to v_\nu.
\]
The first theorem supplies the asserted subsequential lattice-prefactor
limit.

### 4. Quantitative heterogeneity penalty

Fix \(p=\bar p_n\) and \(r<p\), and let
\[
t_0=\log\frac{r(1-p)}{p(1-r)}<0.
\]
Write \(a=1-e^{t_0}>0\). For
\[
h(x)=\log(1-x+xe^{t_0})=\log(1-ax),
\]
one has
\[
h''(x)
=
-\frac{a^2}{(1-ax)^2}
\le -a^2.
\]
Thus \(h\) is \(a^2\)-strongly concave. Since
\(\frac1n\sum_i(p_{i,n}-p)=0\),
\[
\frac1n\sum_i h(p_{i,n})
\le
h(p)-\frac{a^2}{2}V_n.
\]
Evaluating the heterogeneous Legendre transform at the homogeneous saddle
\(t_0\) gives
\[
I_n(r)
=
\sup_t\{rt-\psi_n(t)\}
\ge
rt_0-\frac1n\sum_i h(p_{i,n})
\ge
D(r\|p)+\frac{a^2}{2}V_n.
\]
Finally,
\[
a
=
1-\frac{r(1-p)}{p(1-r)}
=
\frac{p-r}{p(1-r)},
\]
which proves the lower-tail inequality. The upper-tail inequality follows
by complementing every Bernoulli variable.

Combining this rate gap with Theorem 1 for the heterogeneous array and its
homogeneous binomial specialization yields the stop-loss ratio bound.

## Recovery of the binomial coefficient

If \(p_{i,n}\equiv p\), then
\[
t_n=
\log\frac{r(1-p)}{p(1-r)},\qquad
v_n=r(1-r),\qquad
I_n(r)=D(r\|p).
\]
Writing
\[
\rho=e^{t_n}=\frac{r(1-p)}{(1-r)p},
\]
Theorem 1 becomes
\[
\mathbb E[(nr-S_n)^+]
=
\frac{e^{-nD(r\|p)}}{\sqrt{2\pi n r(1-r)}}
\rho^{\theta_n}
\left[
\frac{\theta_n}{1-\rho}
+
\frac{\rho}{(1-\rho)^2}
\right]
(1+O(n^{-1/2})).
\]
This is exactly the first stop-loss coefficient in the recent closed-form
binomial expansion of Elezović, including the lattice defect.

## Context and originality

Elezović recently gave a complete closed-form large-deviation expansion for
the binomial absolute deviation about a prescribed center, retaining the
lattice defect explicitly. The result above extends its first large-
deviation coefficient from a common Bernoulli probability to balanced
Poisson-binomial triangular arrays and identifies the corresponding
empirical-profile functional.

Strong and local large-deviation theorems of Chaganty and Sethuraman supply
general machinery for sums of non-identically distributed variables.
Saddlepoint approximations for Poisson-binomial tails are also established
in the literature; Madsen, Hobolth, Jensen and Pedersen give conditions
under which a Poisson-binomial saddlepoint approximation has uniform
relative error of order \(O(n^{-1})\). The contribution here is therefore
not a claim to a new general saddlepoint or strong-large-deviation method.

Hoeffding proved in 1956 that, at fixed mean, the equal-probability
binomial maximizes expectations of convex functions among sums of
independent Bernoulli variables. Hence the qualitative stop-loss ordering
is classical. The additional statement here is the explicit rate-function
gap
\[
I_n(r)-D(r\|\bar p_n)
\ge
\frac{(\bar p_n-r)^2}
{2\bar p_n^2(1-r)^2}V_n
\]
(and its upper-tail analogue), which turns heterogeneity into a
quantitative exponential penalty and links that penalty to the precise
stop-loss asymptotic.

To the best of our knowledge, the combination of the explicit
Poisson-binomial stop-loss lattice prefactor, empirical-profile limit, and
variance-of-probabilities exponential gap has not been stated previously.

## Limitations

- The precise asymptotic is proved only in the balanced regime where all
  Bernoulli probabilities stay uniformly away from \(0\) and \(1\), and
  the prescribed center stays a fixed distance from the mean and the
  support boundaries.
- The \(O(n^{-1/2})\) remainder is intentionally conservative. Existing
  saddlepoint theory can yield sharper relative errors under additional
  regularity, but no second-order coefficient is derived here.
- The heterogeneity bound is explicit but is not claimed to be the best
  possible function of \(V_n\).
- The result does not cover sparse Poisson-binomial regimes, moderate
  deviations, dependent Bernoulli variables, or centers approaching the
  mean.
- General strong-large-deviation and saddlepoint theory may imply the first
  asymptotic after specialization. Originality is claimed for the explicit
  stop-loss specialization, profile formulation, and quantitative
  heterogeneity-rate comparison, not for exponential tilting or local
  limit theory.

## References

1. N. Elezović, "Absolute deviations of the binomial about a prescribed centre: the tail expansion in closed form", arXiv:2609.19064 (2026). https://arxiv.org/abs/2609.19064
2. N. R. Chaganty and J. Sethuraman, "Strong Large Deviation and Local Limit Theorems", Annals of Probability 21 (1993), 1671-1690. https://doi.org/10.1214/aop/1176989136
3. N. R. Chaganty and J. Sethuraman, "Large Deviation Local Limit Theorems for Arbitrary Sequences of Random Variables", Annals of Probability 13 (1985), 97-114. https://doi.org/10.1214/aop/1176993069
4. W. Hoeffding, "On the Distribution of the Number of Successes in Independent Trials", Annals of Mathematical Statistics 27 (1956), 713-721. https://doi.org/10.1214/aoms/1177728178
5. T. Madsen, A. Hobolth, J. L. Jensen and J. S. Pedersen, "Significance evaluation in factor graphs", BMC Bioinformatics 18, 199 (2017). https://doi.org/10.1186/s12859-017-1614-z
6. W. Tang and F. Tang, "The Poisson Binomial Distribution - Old & New", Statistical Science 38 (2023), 108-119. https://doi.org/10.1214/22-STS852
7. V. Čekanavičius, "Approximation of the generalized Poisson binomial distribution: Asymptotic expansions", Lithuanian Mathematical Journal 37 (1997), 1-12. https://doi.org/10.1007/BF02465434