# Correct tail-sum moments expose the EDBuE light-tail boundary
## Finding
Let \(X\) have the exponentiated discrete Burr–Hatke exponential (EDBuE) distribution with
\[
\alpha>0,\qquad 0<\theta<1.
\]
Put
\[
\lambda=-\log\theta>0,
\qquad
u_k=\frac{\theta^k}{1+\lambda k},
\qquad
G_k=(1-u_k)^\alpha .
\]
The source writes the probability mass function as
\[
p_n=G_{n+1}-G_n,
\qquad n=0,1,2,\ldots .
\]

The exact lattice survival is therefore
\[
\boxed{
\Pr(X\ge k)=1-G_k,
\qquad k\ge1.
}
\]
Since
\[
1-(1-y)^\alpha\sim\alpha y
\qquad(y\downarrow0),
\]
one obtains
\[
\boxed{
\Pr(X\ge k)
\sim
\frac{\alpha}{\lambda}\frac{\theta^k}{k}.
}
\]
The source's own PMF asymptotic is
\[
\boxed{
p_n
\sim
\frac{\alpha(1-\theta)}{\lambda}
\frac{\theta^n}{n}.
}
\]

These equivalents have two structural consequences.

First, the probability generating function has exact radius
\[
\boxed{
R=\frac1\theta,
}
\]
and the ordinary probabilistic moment-generating function has domain
\[
\boxed{
\mathbb E[e^{tX}]<\infty
\quad\Longleftrightarrow\quad
t<-\log\theta.
}
\]
At the boundary \(t=-\log\theta\), its terms are asymptotic to a positive constant divided by \(n\), so the defining series diverges harmonically. Because a positive interval of exponential moments always exists, the EDBuE law is light-tailed for every admissible parameter pair under the standard moment-generating-function definition of heavy tails. The exponentiation parameter \(\alpha\) changes the leading tail constant but not the geometric decay rate.

Second, the moment formulas printed in Section 6.2 require correction. For every positive integer \(r\),
\[
\boxed{
\mathbb E[X^r]
=
\sum_{k=1}^{\infty}
\left\{
k^r-(k-1)^r
\right\}
(1-G_k).
}
\]
All these moments are finite because
\[
\left\{
k^r-(k-1)^r
\right\}
(1-G_k)
=
O(k^{r-2}\theta^k).
\]

By contrast, Eq. (6.4) of the source is
\[
\sum_{k=1}^{\infty}
\left\{
(k-1)^r-k^r
\right\}
G_k.
\]
Since \(G_k\to1\), its summand is asymptotic to
\[
-rk^{r-1},
\]
so the displayed series diverges to \(-\infty\) for every positive integer \(r\). It is not a valid infinite-series rearrangement of the moment.

In particular, the correct mean and second moment are
\[
\boxed{
\mathbb E[X]
=
\sum_{k=1}^{\infty}(1-G_k)
}
\]
and
\[
\boxed{
\mathbb E[X^2]
=
\sum_{k=1}^{\infty}
(2k-1)(1-G_k).
}
\]
Thus
\[
\boxed{
\operatorname{Var}(X)
=
\sum_{k=1}^{\infty}
(2k-1)(1-G_k)
-
\left[
\sum_{k=1}^{\infty}(1-G_k)
\right]^2.
}
\]

The paper's description of selected parameter settings as “heavy-tailed” is therefore an interpretation of finite-range shape or kurtosis, not an asymptotic heavy-tail property.

## Assumptions and scope
The parameter domain is exactly
\[
\alpha>0,\qquad 0<\theta<1,
\]
as stated for the EDBuE model.

“Heavy-tailed” is used in the standard probabilistic sense for nonnegative random variables: a law is heavy-tailed when
\[
\mathbb E[e^{tX}]=\infty
\]
for every \(t>0\). The exact MGF boundary above is stronger than a label: it specifies the complete positive-exponential convergence domain.

The corrected moment identity is stated for positive integer orders because those are the raw moments used by the source for mean, variance, skewness, and kurtosis. No claim is made that the numerical values in the paper's descriptive tables were necessarily computed from the divergent printed formulas; they may have been obtained by a different numerical procedure.

## Proof
For
\[
G_k=(1-u_k)^\alpha,
\qquad
u_k=\frac{\theta^k}{1+\lambda k},
\]
the source's PMF is
\[
p_n=G_{n+1}-G_n.
\]
Hence the CDF is
\[
F(n)=G_{n+1},
\]
and for \(k\ge1\),
\[
\Pr(X\ge k)=1-F(k-1)=1-G_k.
\]

As \(k\to\infty\),
\[
u_k\sim\frac{\theta^k}{\lambda k},
\]
and
\[
1-(1-u_k)^\alpha\sim\alpha u_k.
\]
Therefore
\[
1-G_k
\sim
\frac{\alpha}{\lambda}
\frac{\theta^k}{k}.
\]

Likewise,
\[
p_n
=
G_{n+1}-G_n
\sim
\alpha(u_n-u_{n+1}).
\]
A direct calculation gives
\[
u_n-u_{n+1}
=
\frac{\theta^n}{1+\lambda n}
-
\frac{\theta^{n+1}}{1+\lambda(n+1)}
\sim
\frac{1-\theta}{\lambda}
\frac{\theta^n}{n},
\]
which proves the PMF equivalent.

The root test now gives the PGF radius
\[
R=1/\theta.
\]
Equivalently, for real \(t\),
\[
e^{tn}p_n
\sim
\frac{\alpha(1-\theta)}{\lambda}
\frac{(\theta e^t)^n}{n}.
\]
The series converges for
\[
\theta e^t<1,
\]
diverges harmonically when
\[
\theta e^t=1,
\]
and has terms that fail to approach zero when
\[
\theta e^t>1.
\]
This proves the exact MGF domain.

For the raw moments, use the pointwise identity
\[
x^r
=
\sum_{k=1}^{x}
\left\{
k^r-(k-1)^r
\right\}.
\]
All summands are nonnegative, so Tonelli's theorem gives
\[
\mathbb E[X^r]
=
\sum_{k=1}^{\infty}
\left\{
k^r-(k-1)^r
\right\}
\Pr(X\ge k),
\]
which is the corrected formula.

Finally,
\[
k^r-(k-1)^r
\sim
rk^{r-1}
\]
and
\[
1-G_k
\sim
\frac{\alpha}{\lambda}\frac{\theta^k}{k},
\]
so the corrected moment series is dominated by a polynomial times a geometric sequence and converges for every fixed positive integer \(r\).

For the source's Eq. (6.4),
\[
\left\{
(k-1)^r-k^r
\right\}
G_k
\sim
-rk^{r-1},
\]
because \(G_k\to1\). Its terms therefore do not even approach zero for \(r=1\), and grow in magnitude for \(r>1\). The displayed infinite series cannot equal a finite raw moment.

## Verification
The accompanying checker evaluates the exact EDBuE \(G_k\), survival, and PMF for representative parameter pairs.

It verifies three independent facts:
\[
\frac{1-G_k}
{(\alpha/\lambda)\theta^k/k}
\to1,
\]
\[
\frac{p_k}
{[\alpha(1-\theta)/\lambda]\theta^k/k}
\to1,
\]
and direct PMF moment sums agree with the corrected tail-sum moments.

The checker also shows that the partial sums of the printed Eq. (6.4) decrease without stabilization, while the corrected mean and variance sums converge. Finally, it compares MGF partial sums below and at the exact boundary \(t=-\log\theta\).

These finite computations are consistency checks only. The convergence and divergence statements follow analytically from the asymptotics above.

## Relationship to prior work
Eliwa, Shahen, and El-Morshedy introduce the EDBuE distribution and derive the same geometric-with-\(1/n\)-correction PMF asymptotic used here. They also prove that the discrete hazard tends to
\[
1-\theta,
\]
which is consistent with a geometric-type light tail.

The same article later describes the model as capable of both light- and heavy-tailed behavior, labels the simulation setting
\[
\alpha=0.5,\qquad\theta=0.8
\]
as heavy-tailed, and interprets kurtosis as evidence of heavy tails. Those descriptions conflict with the paper's own tail asymptotic: for every fixed \(0<\theta<1\), the exponential decay rate is \(-\log\theta>0\).

Section 6.2 presents raw-moment Eq. (6.4), a mean formula in Eq. (6.6), and a variance formula in Eq. (6.7). The first of these is an invalid infinite reindexing because the intermediate \(G_k\) terms tend to one rather than zero. The corrected tail-sum identity avoids that divergent cancellation.

Focused searches using the exact DOI, EDBuE name, moment-equation aliases, MGF convergence, heavy-tail terminology, and tail-sum formulas did not locate a published correction of these statements.

## Limitations
This finding establishes mathematical convergence domains and corrected population-moment formulas. It does not determine how the source's numerical tables were computed, and therefore does not assert that every reported numerical moment is wrong.

Finite-range histograms with high kurtosis can look more extreme than competing models even when the asymptotic tail is light. The correction concerns the asymptotic probabilistic meaning of “heavy-tailed.”

The result does not reassess the paper's likelihood estimation, censoring analysis, actuarial risk calculations, or empirical goodness-of-fit comparisons.

## References
1. M. S. Eliwa, H. S. Shahen, and M. El-Morshedy, “The generalized discrete Burr–Hatke exponential distribution: Mathematical characterization, reliability analysis, and applications to censored actuarial, clinical, and agricultural data,” AIMS Mathematics 11 (2026), 11437–11472. DOI: 10.3934/math.2026471.
2. J. Nair, A. Wierman, and B. Zwart, The Fundamentals of Heavy Tails: Properties, Emergence, and Estimation, Cambridge University Press, 2022.
