# Terminal atoms exactly classify leaders of heterogeneous product samples
## Finding
Consider independent, identically distributed observations
\[
Z_k=(Z_{k1},\ldots,Z_{kd}),\qquad k\ge1,
\]
where \(d\ge2\) and the coordinates in each vector are independent but may have different laws:
\[
\mathcal L(Z_k)=F_1\otimes\cdots\otimes F_d.
\]
Call a sampled vector a *leader* if it is componentwise at least every other sampled vector. Denote the probability of a leader among the first \(n\) observations by
\[
a_n=\Pr\left\{\exists k\le n:\ Z_{kj}\ge Z_{ij}
\text{ for all }i\le n\text{ and all }j\le d\right\}.
\tag{1}
\]
For each marginal, let
\[
s_j=\operatorname{ess\,sup}F_j\in\mathbb R\cup\{+\infty\},
\]
and let \(p_j=\Pr(Z_{1j}=s_j)\) if \(s_j\) is finite; set \(p_j=0\) when \(s_j=+\infty\). Thus \(p_j>0\) means that the marginal has an attained, positive-mass upper endpoint.

**Theorem (exact classification).** For every collection of arbitrary probability laws \(F_1,\ldots,F_d\) on \(\mathbb R\),
\[
\boxed{\liminf_{n\to\infty}a_n>0
\quad\Longleftrightarrow\quad
\#\{j:p_j=0\}\le1.}
\tag{2}
\]
The following are quantitative parts of the same classification.

If all \(p_j>0\), then
\[
a_n\ge 1-\left(1-\prod_{j=1}^dp_j\right)^n
\longrightarrow1.
\tag{3}
\]
If exactly one marginal, say \(F_j\), has \(p_j=0\), put
\[
p_*=\prod_{i\ne j}p_i>0.
\]
For every integer \(n\ge1\),
\[
a_n\ge p_*.
\tag{4}
\]
If that exceptional marginal is atomless, then more precisely
\[
p_*\le a_n\le p_*+\sum_{i\ne j}(1-p_i)^n,
\tag{5}
\]
so \(a_n\to p_*\). This bound is sharp: if \(d=2\), the first marginal is atomless, and the second is Bernoulli with success probability \(p\in(0,1)\), then
\[
a_n=p+(1-p)^n
\quad\text{for every }n\ge1.
\tag{6}
\]
Finally, if two or more marginals have \(p_j=0\), then
\[
\liminf_{n\to\infty}a_n=0.
\tag{7}
\]
The full limit in (7) is not asserted to exist.

## Assumptions and scope
The observations are iid as vectors, and the coordinate laws form a product distribution. No smoothness, moment, regular-variation, continuity, finite-support, or monotone-atom assumption is made. Atoms and ties are permitted. The essential supremum may be finite and unattained, or infinite. The dimension \(d\) is any fixed integer at least two.

The order is componentwise, not lexicographic, and a leader need not be unique when sampled vectors tie. The *leader property* means the strictly positive lower limit in (2), as in the motivating paper; it does not merely mean positive probability for one fixed sample size.

## Proof
**Case 1: every marginal has a top atom.** The top vector
\[
s=(s_1,\ldots,s_d)
\]
has strictly positive point mass
\[
p=\prod_{j=1}^dp_j.
\]
Whenever any of the first \(n\) observations equals \(s\), that observation dominates all sampled vectors. The probability of at least one such occurrence is \(1-(1-p)^n\), proving (3).

**Case 2: exactly one marginal lacks a top atom.** Let that coordinate be \(j\). For each sample size, select
\[
I_n=\min\{k\le n:Z_{kj}=\max_{1\le i\le n}Z_{ij}\}.
\]
This is a measurable function of the \(j\)-coordinate sample alone. Product independence implies that \(I_n\) is independent of all samples of the remaining coordinates. Thus
\[
\Pr\{Z_{I_n,i}=s_i\text{ for all }i\ne j\}
=\prod_{i\ne j}p_i=p_*.
\]
On this event, the selected observation dominates every coordinate sample, hence is a leader. This proves (4), including when the exceptional marginal has ties.

When \(F_j\) is atomless, its sample maximum has a unique index almost surely. Let \(B_n\) denote the event that each of the other coordinates attains its respective upper endpoint somewhere among the \(n\) observations. On \(B_n\), a leader can exist only at index \(I_n\), and that index must equal the top value in every other coordinate. Therefore the leader event differs from the event used for (4) only on \(B_n^c\). A union bound gives
\[
\Pr(B_n^c)\le\sum_{i\ne j}(1-p_i)^n.
\]
This yields (5). In dimension two, with atomless first coordinate and Bernoulli second coordinate, a leader exists precisely if the index of the first-coordinate maximum has Bernoulli value \(1\), or all second-coordinate values equal \(0\). These disjoint events have probabilities \(p\) and \((1-p)^n\), proving (6).

**Case 3: at least two marginals have no top atom.** Projecting to any two such coordinates can only enlarge the leader event: a leader of the full sample would also be a leader of the projected sample. It suffices to handle a two-coordinate product law \(F_X\otimes F_Y\) whose marginals lack attained positive-mass upper endpoints.

Let \(F_Y(y)=\Pr(Y\le y)\), and for \(n\ge1\) define
\[
g_Y(n)=\Pr\{Y_1=\max_{1\le i\le n}Y_i\}
=\mathbb E[F_Y(Y_1)^{n-1}].
\tag{8}
\]
Because \(F_Y\) has no top atom, \(F_Y(Y_1)<1\) almost surely. Dominated convergence applied to (8) gives
\[
g_Y(n)\longrightarrow0.
\tag{9}
\]
Choose any real threshold \(t\) with \(q=\Pr(X>t)>0\). If at least one sample \(X_i\) exceeds \(t\) and a two-dimensional leader exists, then some index attaining the global \(Y\)-maximum must also have \(X_i>t\). Taking a union bound over indices, and using independence of the complete \(X\)-sample and \(Y\)-sample, gives the key estimate
\[
a_n\le (1-q)^n+nq\,g_Y(n).
\tag{10}
\]
For each integer \(k\ge2\), choose \(N_k\ge k\) large enough that
\[
g_Y(n)\le k^{-2}\qquad(n\ge N_k).
\]
The absence of a top atom in \(F_X\) means that its positive upper-tail probabilities can be arbitrarily small. Hence choose a threshold \(t_k\) with
\[
0<q_k=\Pr(X>t_k)<\min\{k^{-1},\ k/N_k\}.
\]
Set
\[
n_k=\left\lceil k/q_k\right\rceil.
\]
Then \(n_k\ge N_k\), and \(k\le n_kq_k\le k+q_k\). Inserting these choices into (10),
\[
0\le a_{n_k}
\le e^{-k}+\frac{k+q_k}{k^2}
\longrightarrow0.
\tag{11}
\]
Since \(n_k\to\infty\), this proves \(\liminf_na_n=0\) in the two-dimensional projection and hence in the original \(d\)-dimensional product sample. Combining the three cases gives the equivalence (2). \(\square\)

## Verification
Run the bundled standalone Python 3 script `verify.py` with the standard library only. It exactly enumerates iid finite-product samples of sizes \(1\) through \(4\), checks the lower bounds (3)–(4), and checks the universal two-dimensional threshold inequality (10) for a concrete rational finite law. It then uses exact rational binomial identities to replay (6) for sample sizes \(1\) through \(19\). The terminal message is

`VERIFY_OK exact_finite_rows=4 sharp_bernoulli_limit=2/7 all_top_product=3/40`

These exact finite checks do not establish asymptotics. Equations (8)–(11) provide the infinite-distribution argument, with dominated convergence and a constructed unbounded subsequence. No approximation of an infinite support is treated as exhaustive.

## Relationship to prior work
Răducan, Rădulescu, Rădulescu and Zbăganu (2022) introduce the leader property through a positive lower limit of the sample-leader probability and explicitly ask about products of independent marginals with infinitely many possible values and about products where all but one marginal are finitely supported. They provide sufficient criteria and special cases, including a finite-support block paired with a continuous coordinate. The present theorem answers the distribution-level product question using **upper-endpoint atoms rather than support cardinalities**, for arbitrary heterogeneous marginals and every finite dimension.

The cardinality-only assertion suggested by one of the original questions is false without an unboundedness or top-atom exclusion assumption: for any \(p\in(0,1)\), the infinitely supported law
\[
H=p\,\delta_1+(1-p)\sum_{r=1}^\infty2^{-r}\delta_{1-1/r}
\]
has a positive top atom. Every product of finitely many independent copies of \(H\) satisfies \(a_n\to1\) by (3). In contrast, if two marginals are unbounded above, neither has a top atom, and (7) holds without any tail regularity. The theorem also confirms that finite upper supports in all but one coordinate guarantee the leader property, even when the exceptional marginal is discrete, unbounded and highly irregular.

The 2022 follow-up on quasi-unidimensional laws studies a functional-dependence structure rather than arbitrary independent-coordinate products. The 2025 follow-up on computing extremes emphasizes geometric mappings and irregular limiting behavior; its accessible abstract does not supply this classification.

The theorem does not assert that the leader probability converges whenever two top atoms are absent. Its conclusion is deliberately the lower-limit criterion posed in the original definition.

## Limitations
Independence **between coordinates** is essential to the selection and union-bound factorizations; dependence may support leaders without any marginal upper atom. The dimension is fixed as sample size increases. The result decides the existence of a positive lower limit but does not classify all cluster points of \(a_n\) when at least two marginals lack top atoms. For a single exceptional marginal with ties, (4) is valid but convergence to the lower bound is not asserted without uniqueness of the coordinate maximum.

A bibliographic risk remains that the terminal-atom criterion is implicit in broader work on argmax intersections, occupancy, or multivariate maxima under terminology different from the motivating leader-property literature.

## References
1. A. M. Răducan, C. Z. Rădulescu, M. Rădulescu and G. Zbăganu, “On the Probability of Finding Extremes in a Random Set,” *Mathematics* 10 (2022), 1623, first public 10 May 2022. DOI: 10.3390/math10101623.
2. A. M. Răducan and G. Zbăganu, “The Leader Property in Quasi Unidimensional Cases,” *Mathematics* 10 (2022), 4199. DOI: 10.3390/math10224199.
3. G. Zbăganu, A. M. Răducan and M. Rădulescu, “Computing Probabilities of Finding Extremes in a Random Set,” *Mathematics* 13 (2025), 3074. DOI: 10.3390/math13193074.
