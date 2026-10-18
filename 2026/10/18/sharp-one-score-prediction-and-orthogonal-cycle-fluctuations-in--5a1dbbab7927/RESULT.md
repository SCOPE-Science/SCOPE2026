# Sharp one-score prediction and orthogonal cycle fluctuations in random tournaments

## Finding

Let \(T\) be the uniformly random tournament on \(n\ge3\) labeled vertices: each pair is oriented independently and fairly. Write \(S_v\) for the outdegree (number of wins) of vertex \(v\), \(C\) for the number of directed cyclic triangles (one per three-vertex set), and \(m=n-1\). Define the centered quadratic score
\[
Q_v=\left(S_v-\frac m2\right)^2-\frac m4.
\]
Then the exact *pairwise orthogonal score decomposition* is
\[
C-\mathbb EC=-\frac12\sum_{v=1}^n Q_v,
\qquad
\operatorname{Cov}(Q_v,Q_w)=0\quad(v\ne w),
\qquad
\operatorname{Var}(Q_v)=\frac{m(m-1)}8.
\]
In particular, \(\mathbb EC=\binom n3/4\) and \(\operatorname{Var}(C)=n(n-1)(n-2)/32\).

For every fixed vertex \(v\) and each integer \(0\le s\le m\), the exact conditional moments are
\[
\boxed{\ \mathbb E[C\mid S_v=s]=\frac14\binom m3+\frac12s(m-s)
=\mathbb EC-\frac12\left[\left(s-\frac m2\right)^2-\frac m4\right],\ }
\]
\[
\boxed{\ \operatorname{Var}(C\mid S_v=s)
=\frac3{16}\binom m3+\frac14s(m-s).\ }
\]
Consequently the fraction of cyclic-triangle variance explained by observing a single vertex's score is **exactly**
\[
\boxed{\quad\frac{\operatorname{Var}(\mathbb E[C\mid S_v])}{\operatorname{Var}(C)}=\frac1n.\quad}
\]
Equivalently, among all square-integrable real predictors based only on \(S_v\), the unique minimum-mean-square-error predictor is the displayed conditional mean. Its residual mean-square error is \((1-1/n)\operatorname{Var}(C)\). The sharp nonlinear correlation ratio equals \(1/\sqrt n\), attained by the centered quadratic score; in contrast, \(\operatorname{Cov}(C,S_v)=0\). The last statement does **not** imply independence.

## Assumptions and scope

A tournament is an orientation of every unordered pair of distinct labeled vertices. Orientations are mutually independent with probabilities \(1/2\) and \(1/2\); there are no ties or loops. A cyclic triangle is a directed cycle on three distinct vertices; it is counted once, not three times by its starting position. All expectations and variances refer to this finite uniform distribution. The claim holds for all integers \(n\ge3\), all vertices \(v,w\), and all possible integer outdegrees \(s\in\{0,\ldots,n-1\}\). At \(n=2\), the cyclic-triangle variance vanishes and the displayed explained-variance ratio is undefined, hence the explicit lower bound on \(n\).

## Proof

**1. Exact score identity.** Every transitive triple has exactly one vertex that wins against its two companions, whereas no vertex wins against both others in a cyclic triple. Therefore the number of transitive triples is precisely \(\sum_v\binom{S_v}{2}\), and the classical deterministic identity is
\[
C=\binom n3-\sum_v\binom{S_v}{2}.
\]
Each three-set is cyclic with probability \(2/8=1/4\), and \(\sum_v S_v=\binom n2\) deterministically. Centering the identity and completing squares thus gives
\[
C-\mathbb EC=-\frac12\sum_v\left[\left(S_v-\frac m2\right)^2-\frac m4\right].
\]

**2. Quadratic score orthogonality.** For distinct \(v,w\), condition on their common edge. The scores can be written \(S_v=B_v+\delta\) and \(S_w=B_w+(1-\delta)\), where \(\delta\in\{0,1\}\) is fixed by the common edge and \(B_v,B_w\) are independent \(\operatorname{Bin}(m-1,1/2)\) variables, independently of that edge. For either \(\epsilon\in\{0,1\}\),
\[
\mathbb E\left[\left(B_v+\epsilon-\frac m2\right)^2\right]
=\frac{m-1}{4}+\left(\epsilon-\frac12\right)^2=\frac m4.
\]
Thus \(\mathbb E[Q_v\mid\delta]=\mathbb E[Q_w\mid\delta]=0\). Conditional independence implies \(\mathbb E[Q_vQ_w]=0\). Also \(S_v\sim\operatorname{Bin}(m,1/2)\). Writing its centered version as a sum of independent symmetric half-Bernoulli variables gives
\[
\mathbb E\left[\left(S_v-\frac m2\right)^4\right]=\frac{3m^2-2m}{16},
\quad \operatorname{Var}(Q_v)=\frac{m(m-1)}8.
\]
The decomposition now gives \(\operatorname{Var}(C)=\frac14 n\operatorname{Var}(Q_v)=nm(m-1)/32\), with no assumption that the \(Q_v\) are independent.

**3. Conditional mean and sharp prediction.** Given \(S_v=s\), the orientation of an edge between \(v\) and another vertex \(w\) may be biased, but the other \(m-1\) edges incident to \(w\) remain independent fair coin flips. The preceding squared-mean calculation shows \(\mathbb E[Q_w\mid S_v=s]=0\) for every \(w\ne v\), irrespective of which way the edge \(vw\) is oriented. Conditional expectation of the centered score decomposition yields
\[
\mathbb E[C\mid S_v=s]=\mathbb EC-\frac12\left[\left(s-\frac m2\right)^2-\frac m4\right].
\]
Simplification gives the first displayed conditional formula. Since the centered conditional mean is \(-Q_v/2\), its variance is \(m(m-1)/32\); dividing by \(\operatorname{Var}(C)=nm(m-1)/32\) proves the exact \(1/n\) ratio. For every square-integrable \(h(S_v)\), conditional expectation is the orthogonal projection in \(L^2\), hence
\[
\mathbb E[(C-h(S_v))^2]
=\mathbb E[\operatorname{Var}(C\mid S_v)]
+\mathbb E[(\mathbb E[C\mid S_v]-h(S_v))^2].
\]
Equality in the optimal nonlinear correlation bound is attained exactly by nonzero affine transformations of \(Q_v\); the optimal predictor itself is uniquely the conditional expectation (almost surely). Because the binomial distribution is symmetric about \(m/2\), the centered quadratic \(Q_v\) is uncorrelated with \(S_v\), giving \(\operatorname{Cov}(C,S_v)=0\).

**4. Conditional variance.** Fix \(S_v=s\), and condition further on the *identity* of the \(s\) vertices beaten by \(v\), a set \(A\). Let \(B\) be the other \(m-s\) vertices. The induced tournament on \(A\cup B\) remains an independent fair tournament; let its cyclic-triangle count be \(C_0\). A triangle containing \(v\) is cyclic exactly when its other two vertices are \(a\in A\), \(b\in B\), and the remaining edge points from \(a\) to \(b\). The count \(C_v\) of these triangles therefore has the \(\operatorname{Bin}(s(m-s),1/2)\) law.

For any fixed edge among the \(m\) remaining vertices, the conditional expectation of \(C_0\), given either orientation of that edge, remains \(\binom m3/4\): each triangle using that edge is cyclic with conditional probability \(1/4\), and other triangles are unaffected. Since \(C_v\) is a sum of cross-edge orientation indicators, linearity implies \(\operatorname{Cov}(C_0,C_v\mid A)=0\). Likewise, the indicators of cyclic triangles in a uniform tournament are pairwise independent: triangles with disjoint edge sets are independent, and for two triangles sharing one edge, conditioning on it gives independent indicators each with conditional probability \(1/4\). Hence
\[
\operatorname{Var}(C_0\mid A)=\frac3{16}\binom m3,
\qquad \operatorname{Var}(C_v\mid A)=\frac14s(m-s).
\]
The sum is the asserted conditional variance, independent of the identities in \(A\), and therefore also valid given only \(S_v=s\).

## Verification

The standalone standard-library script `verify.py` exhaustively enumerates all labeled tournaments for \(3\le n\le6\) (respectively \(8,64,1024,32768\) orientations) using exact rational arithmetic. It independently counts cyclic triangles by directed-edge tests and compares: the deterministic score identity; unconditional cycle variance; orthogonality of every pair of quadratic vertex scores; zero linear score covariance; all conditional means and variances at every feasible score; and the sharp explained-variance ratio. Run `python3 verify.py`. The script's finite checks complement, but do not replace, the arguments above for all \(n\).

## Relationship to prior work

The deterministic fact that cyclic-triangle counts are determined by the tournament score sequence is classical; it is explicitly acknowledged in the introduction of Grzesik, Kráľ, Lovász and Volec (arXiv:2008.06577). The stochastic score-vector viewpoint is developed by Kolesnik and Sanchez (arXiv:2009.09322), whose geometric results address realizable mean scores rather than the conditional fluctuation laws here. The present point is the finite-sample *orthogonality of local quadratic score fluctuations*, the complete conditional first and second moments given a single score, and the exact optimal one-score variance fraction. These are not claimed as a new identity for deterministic tournament score sequences.

## Limitations

The theorem assumes independent fair orientations; it does not treat biased or correlated paired comparisons, and it makes no asymptotic normality assertion. Pairwise uncorrelated quadratic scores need not be jointly independent. Conditional moment identities do not specify the complete conditional distribution of the cyclic-triangle count. The classical deterministic score identity makes some deductions short, and undiscovered earlier probabilistic derivations of the same conditional formulas remain a historical-priority possibility.

## References

1. A. Grzesik, D. Kráľ, L. M. Lovász and J. Volec, *Cycles of a given length in tournaments*, first public arXiv version dated 2020-08-14, arXiv:2008.06577, https://arxiv.org/abs/2008.06577.
2. B. Kolesnik and M. Sanchez, *The geometry of random tournaments*, first public arXiv version dated 2020-09-19, arXiv:2009.09322, https://arxiv.org/abs/2009.09322.
3. Classical deterministic score-sequence identity, as attributed in the introduction of reference 1 to earlier tournament literature (including the 1959 reference cited there).
