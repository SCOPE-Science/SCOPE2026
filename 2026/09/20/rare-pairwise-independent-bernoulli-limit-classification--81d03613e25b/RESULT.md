# Weak-limit classification for rare pairwise-independent Bernoulli sums

## Result

Let, for each row index \(n\),
\[
X_{n,1},\dots,X_{n,m_n}\in\{0,1\}
\]
be pairwise independent Bernoulli variables within the row. Write
\[
p_{n,i}=\Pr(X_{n,i}=1),\qquad S_n=\sum_i X_{n,i}.
\]
Assume the rare-event conditions
\[
\max_i p_{n,i}\to0,
\qquad
\lambda_n:=\sum_i p_{n,i}\to\lambda\in(0,\infty).
\]
Then every weak subsequential limit \(Y\) of \(S_n\) is supported on \(\mathbb Z_{\ge0}\) and satisfies
\[
\boxed{\mathbb EY=\lambda,\qquad \operatorname{Var}(Y)\le\lambda.}
\]

Conversely, these are the only restrictions. For every \(\mathbb Z_{\ge0}\)-valued random variable \(Y\) with
\[
\mathbb EY=\lambda,\qquad \operatorname{Var}(Y)\le\lambda,
\]
there exists a triangular array with exactly \(n\) Bernoulli variables in row \(n\), for all sufficiently large \(n\), such that

- the row is exchangeable and pairwise independent;
- every marginal is exactly \(\operatorname{Bernoulli}(\lambda/n)\); and
- \(S_n\Rightarrow Y\).

Thus the complete class of weak limits of rare pairwise-independent Bernoulli sums is
\[
\boxed{
\left\{\mathcal L(Y):Y\in\mathbb Z_{\ge0},\ \mathbb EY=\lambda,\ \operatorname{Var}(Y)\le\lambda\right\}.
}
\]
The converse is attained inside the much smaller subclass of exchangeable, equal-marginal rows.

This sharply contrasts with the classical law of small numbers: under mutual independence, the same rare-event assumptions force \(S_n\Rightarrow\operatorname{Poisson}(\lambda)\).

## A particularly strong failure of the Poisson limit

For \(\lambda=1\), one can make the count converge to the constant one. For every \(n\ge2\), choose a count \(K_n\in\{0,1,n\}\) with
\[
\Pr(K_n=0)=\frac{n-1}{n^2},\qquad
\Pr(K_n=1)=1-\frac1n,\qquad
\Pr(K_n=n)=\frac1{n^2}.
\]
Conditional on \(K_n=k\), choose uniformly a \(k\)-element subset of \([n]\), and let its membership indicators be \(X_{n,1},\ldots,X_{n,n}\). Then
\[
\Pr(X_{n,i}=1)=\frac1n,
\qquad
\Pr(X_{n,i}=X_{n,j}=1)=\frac1{n^2}\quad(i\ne j),
\]
so the indicators are pairwise independent. Yet
\[
S_n=K_n\xrightarrow{\Pr}1.
\]
Hence rare pairwise-independent events with the same one- and two-coordinate behavior as independent Bernoulli\((1/n)\) variables can produce essentially one occurrence with probability tending to one, rather than a Poisson(1) count.

The mechanism is a vanishing \(n^{-2}\) mass at the extreme count \(n\): it is invisible to weak convergence but carries an order-one contribution to the second moment. This explains how every finite row can have variance asymptotic to \(\lambda\) while the weak limit can have any smaller variance.

## Proof: necessity

Pairwise independence gives
\[
\mathbb ES_n=\lambda_n
\]
and
\[
\operatorname{Var}(S_n)
=\sum_i p_{n,i}(1-p_{n,i})
=\lambda_n-\sum_i p_{n,i}^2.
\]
Because
\[
0\le \sum_i p_{n,i}^2
\le \left(\max_i p_{n,i}\right)\lambda_n\to0,
\]
we have
\[
\mathbb ES_n\to\lambda,
\qquad
\operatorname{Var}(S_n)\to\lambda,
\qquad
\mathbb ES_n^2\to\lambda^2+\lambda.
\]
In particular, \(\sup_n\mathbb ES_n^2<\infty\), so \((S_n)\) is uniformly integrable.

Suppose along a subsequence \(S_n\Rightarrow Y\). Since every \(S_n\) is nonnegative integer-valued, so is \(Y\). Uniform integrability preserves the first moment:
\[
\mathbb EY=\lim_n\mathbb ES_n=\lambda.
\]
For the second moment, lower semicontinuity under weak convergence gives
\[
\mathbb EY^2\le\liminf_n\mathbb ES_n^2=\lambda^2+\lambda.
\]
Consequently
\[
\operatorname{Var}(Y)=\mathbb EY^2-\lambda^2\le\lambda.
\]

The inequality can be strict because bounded second moments of \(S_n\) do not imply uniform integrability of \(S_n^2\).

## Proof: converse

### 1. Exchangeable rows reduce pairwise independence to two count moments

Let \(K_n\) be any random variable supported on \(\{0,1,\dots,n\}\). Conditional on \(K_n=k\), choose uniformly a \(k\)-subset of \([n]\), and let \(X_{n,i}\) be its membership indicators. The row is exchangeable and
\[
\Pr(X_{n,i}=1)=\frac{\mathbb EK_n}{n},
\]
while for \(i\ne j\),
\[
\Pr(X_{n,i}=X_{n,j}=1)
=\frac{\mathbb E[K_n(K_n-1)]}{n(n-1)}.
\]
Therefore the row has marginal \(\lambda/n\) and is pairwise independent exactly when
\[
\boxed{
\mathbb EK_n=\lambda,
\qquad
\mathbb E[K_n(K_n-1)]
=\left(1-\frac1n\right)\lambda^2.
}
\]
It remains to approximate any admissible target law by count laws satisfying these two equations exactly.

### 2. Finite-support targets with variance strictly below \(\lambda\)

Let \(Q\) be supported on \(\{0,\dots,M\}\), with
\[
\mathbb EQ=\lambda,
\qquad
v:=\operatorname{Var}(Q)<\lambda.
\]
Set \(d=\lambda-v>0\). Then
\[
\mathbb E[Q(Q-1)]=\lambda^2-d.
\]
Choose an atom \(j\ge1\) with \(q_j:=\Pr(Q=j)>0\). For all sufficiently large \(n>M\), define
\[
\Delta_n=d-\frac{\lambda^2}{n}>0,
\qquad
\varepsilon_n=\frac{\Delta_n}{j(n-j)}.
\]
For large \(n\), \(\varepsilon_n<q_j\). Modify the law of \(Q\) by removing mass \(\varepsilon_n\) at \(j\) and adding
\[
\varepsilon_n\left(1-\frac jn\right)
\quad\text{at }0,
\qquad
\varepsilon_n\frac jn
\quad\text{at }n.
\]
Call the resulting count \(K_n\). Total mass and the mean are unchanged. Its second factorial moment increases by
\[
\varepsilon_n\bigl(j(n-1)-j(j-1)\bigr)
=\varepsilon_n j(n-j)=\Delta_n,
\]
so
\[
\mathbb E[K_n(K_n-1)]
=(\lambda^2-d)+\Delta_n
=\left(1-\frac1n\right)\lambda^2.
\]
Also \(\varepsilon_n=O(n^{-1})\), hence \(K_n\to Q\) in total variation.

### 3. Finite-support targets with variance exactly \(\lambda\)

Let \(Q\) have finite support, mean \(\lambda\), and variance \(\lambda\), so
\[
\mathbb E[Q(Q-1)]=\lambda^2.
\]
Let \(Z\) be the two-point integer distribution on
\(\{\lfloor\lambda\rfloor,\lceil\lambda\rceil\}\) with mean \(\lambda\). Its variance \(v_Z\) is strictly less than \(\lambda\), so put \(d_Z=\lambda-v_Z>0\).

For sufficiently large \(n\), set
\[
\eta_n=\frac{\lambda^2}{n d_Z}
\]
and let
\[
K_n\sim(1-\eta_n)Q+\eta_n Z.
\]
The mean remains \(\lambda\), while
\[
\mathbb E[K_n(K_n-1)]
=\lambda^2-\eta_n d_Z
=\left(1-\frac1n\right)\lambda^2.
\]
Since \(\eta_n\to0\), \(K_n\to Q\) in total variation.

### 4. Arbitrary admissible targets

Now let \(Y\) be any nonnegative integer-valued law with mean \(\lambda\) and variance at most \(\lambda\). For an integer cutoff \(M\), retain the law of \(Y\) on \(\{0,\dots,M\}\). Replace the conditional tail law \(Y\mid Y>M\) by the two adjacent integers bracketing its conditional mean, with weights chosen to preserve that mean.

Call the resulting finite-support law \(Q_M\). Then
\[
\mathbb EQ_M=\lambda.
\]
Among integer-valued laws with a fixed mean, the distribution on the two adjacent bracketing integers minimizes the second moment, so
\[
\operatorname{Var}(Q_M)\le\operatorname{Var}(Y)\le\lambda.
\]
Moreover
\[
d_{\rm TV}(Q_M,Y)\le\Pr(Y>M)\to0.
\]
Thus \(Q_M\Rightarrow Y\).

For each fixed \(M\), Steps 2--3 construct, for every sufficiently large \(n\), an exact pairwise-independent exchangeable Bernoulli row whose count law is arbitrarily close to \(Q_M\). Choose a nondecreasing cutoff \(M=M(n)\to\infty\) slowly enough that the corresponding finite-support construction is valid. A diagonal argument gives
\[
S_n\Rightarrow Y.
\]
This proves sufficiency.

## Consequences

1. **Poisson is only one boundary member.** The Poisson law has mean and variance \(\lambda\), so it is attainable, but it is not selected by pairwise independence.

2. **Arbitrarily strong underdispersion is possible.** If \(\lambda=m\) is an integer, the deterministic law \(Y\equiv m\) is attainable. For noninteger \(\lambda=m+\theta\), the minimum-variance integer law \(m+\operatorname{Bernoulli}(\theta)\) is attainable.

3. **The limiting variance can lose mass.** Every row in the rare-event regime has \(\operatorname{Var}(S_n)\to\lambda\), yet any limit variance in the feasible interval can occur. The missing variance is carried by events whose probabilities vanish while their count magnitudes diverge.

4. **Two-coordinate diagnostics cannot certify a Poisson law of small numbers.** Even exact pairwise independence and equal marginals \(\lambda/n\) leave the weak limit essentially unconstrained beyond mean and the variance upper bound.

## Relation to prior literature

The mutually independent law of small numbers is classical; Le Cam's 1960 theorem gives a total-variation Poisson approximation for sums of independent rare Bernoulli variables.

The finite-dimensional pairwise-independent Bernoulli problem is also classical. Boros and Prékopa (1989) studied sharp probability bounds from the first two binomial moments. Ramachandra and Natarajan (2023) developed tight finite-\(n\) probability bounds for pairwise-independent Bernoulli sums and, for identical marginals, explicitly connect the problem to the first-two-binomial-moment linear program. These finite moment formulations contain an important ingredient used here: for a symmetric Bernoulli row, pairwise independence is encoded by the first two factorial moments of the count.

Gupta, Hu, Kehne, and Levin (2025/2026) give, for a different contention-resolution purpose, an explicit symmetric pairwise-independent example with marginal \(1/n\) and count probabilities tending to \(\tfrac12\delta_0+\tfrac12\delta_2\). Thus non-Poisson rare-event limits under pairwise independence are not new in themselves.

The claim here is narrower and more structural: **to the best of our knowledge, the exact weak-limit classification by \(\mathbb EY=\lambda\) and \(\operatorname{Var}(Y)\le\lambda\), together with an exchangeable equal-marginal realization of every admissible law, has not previously been stated.** The construction also isolates the second-moment escape mechanism needed to realize underdispersed limits.

## Limitations

- The result classifies scalar count limits, not point-process limits or locations of the rare events.
- Only pairwise independence is treated. Higher \(k\)-wise independence imposes higher factorial-moment constraints and leads to a different moment problem.
- The theorem is existential. It does not minimize support size, entropy, or randomness required to sample the realizing rows.
- The originality claim is to the best of our knowledge. Older discrete moment, Bonferroni, finite-exchangeability, orthogonal-array, or limited-independence literature could contain an equivalent asymptotic classification under different terminology.

## References

1. L. Le Cam, “An approximation theorem for the Poisson binomial distribution,” *Pacific Journal of Mathematics* 10 (1960), 1181–1197. https://doi.org/10.2140/pjm.1960.10.1181
2. E. Boros and A. Prékopa, “Closed Form Two-Sided Bounds for Probabilities that At Least r and Exactly r Out of n Events Occur,” *Mathematics of Operations Research* 14(2) (1989), 317–342. https://doi.org/10.1287/moor.14.2.317
3. A. K. Ramachandra and K. Natarajan, “Tight Probability Bounds with Pairwise Independence,” *SIAM Journal on Discrete Mathematics* 37 (2023). https://doi.org/10.1137/21M1408294
4. A. Gupta, J. Hu, G. Kehne, and R. Levin, “Pairwise-independent contention resolution,” *Mathematical Programming* 216 (2026), 295–338; version of record published 2025. https://doi.org/10.1007/s10107-025-02253-w
5. J. P. Schmidt, A. Siegel, and A. Srinivasan, “Chernoff–Hoeffding Bounds for Applications with Limited Independence,” *SIAM Journal on Discrete Mathematics* 8(2) (1995), 223–250. https://doi.org/10.1137/S089548019223872X

**Same-model review: passed. Independent audit: not yet performed.**
