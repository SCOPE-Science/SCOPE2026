# Rounded proportional allocation can reverse gradient-clustered variance reduction

## Statement

Consider a finite population of vectors partitioned into clusters \(C_1,\dots,C_K\). Write
\[
p_k=\frac{n_k}{N},\qquad
\mu_k=\frac1{n_k}\sum_{i\in C_k}g_i,\qquad
\sigma_k^2=\frac1{n_k}\sum_{i\in C_k}\|g_i-\mu_k\|^2,
\]
and let
\[
\sigma_W^2=\sum_k p_k\sigma_k^2,
\qquad
\sigma_B^2=\sum_k p_k\|\mu_k-G\|^2,
\qquad
G=\sum_kp_k\mu_k.
\]
Suppose cluster \(k\) is sampled independently with replacement \(m_k\ge1\) times and the estimator is
\[
\widehat G_{\rm cl}=\sum_{k=1}^K p_k\frac1{m_k}\sum_{j=1}^{m_k}g_{k,j},
\qquad \sum_km_k=m.
\]
Then
\[
\boxed{\operatorname{Var}(\widehat G_{\rm cl})
=\sum_{k=1}^K\frac{p_k^2\sigma_k^2}{m_k}.}
\]
If \(q_k=m_k/m\), comparison with \(m\) independent uniform population draws gives the exact identity
\[
\boxed{
\operatorname{Var}(\widehat G_{\rm rand})-
\operatorname{Var}(\widehat G_{\rm cl})
=\frac1m\left[
\sigma_B^2-
\sum_kp_k\sigma_k^2\left(\frac{p_k}{q_k}-1\right)
\right].}
\]
Thus exact proportional allocation \(q_k=p_k\) recovers the familiar reduction \(\sigma_B^2/m\), but an integer-rounded allocation need not reduce variance. The sign of the variance gap is governed by the displayed criterion, not by \(\sigma_B^2\) alone.

This distinction applies directly to the gradient-clustered BS sampler of Niknia--Wang (2026). Their theoretical variance identity assumes exact integer proportional counts \(m_k=mn_k/N\), whereas their practical prescription rounds \(mn_k/N\), enforces at least one draw per nonempty cluster, and preserves the total budget. The exact proportional theorem is correct under its stated divisibility assumption; it does not automatically transfer to the rounded sampler.

## Exact counterexample compatible with cosine clustering

Take scalar gradients and two clusters with sizes \(n_1=7\), \(n_2=3\), total \(N=10\), and budget \(m=2\). Let
\[
C_1:\quad
\left\{\frac1{10},\frac1{10},\frac1{10},\frac1{10},\frac1{10},\frac1{10},\frac{67}{5}\right\},
\qquad
C_2:\quad\{-1,-1,-1\}.
\]
All gradients in \(C_1\) normalize to \(+1\), while all gradients in \(C_2\) normalize to \(-1\). Hence this partition is exactly compatible with cosine-similarity clustering of normalized gradients.

The cluster statistics are
\[
p_1=\frac7{10},\quad p_2=\frac3{10},\qquad
\mu_1=2,\quad \mu_2=-1,
\]
\[
\sigma_1^2=\frac{1083}{50},\qquad \sigma_2^2=0,
\]
and therefore
\[
G=\frac{11}{10},\qquad
\sigma_W^2=\frac{7581}{500},\qquad
\sigma_B^2=\frac{189}{100},\qquad
\sigma^2=\frac{4263}{250}.
\]
Nearest-integer proportional allocation gives
\[
mn_1/N=1.4\mapsto m_1=1,\qquad
mn_2/N=0.6\mapsto m_2=1,
\]
so the minimum-one and total-budget constraints are simultaneously satisfied with no further tie-breaking.

For uniform sampling with replacement,
\[
\operatorname{Var}(\widehat G_{\rm rand})
=\frac{\sigma^2}{2}
=\frac{4263}{500}.
\]
For the rounded clustered sampler,
\[
\operatorname{Var}(\widehat G_{\rm cl})
=\left(\frac7{10}\right)^2\frac{1083}{50}
=\frac{53067}{5000}.
\]
Consequently
\[
\boxed{
\operatorname{Var}(\widehat G_{\rm cl})-
\operatorname{Var}(\widehat G_{\rm rand})
=\frac{10437}{5000}>0,}
\]
and
\[
\boxed{
\frac{\operatorname{Var}(\widehat G_{\rm cl})}
{\operatorname{Var}(\widehat G_{\rm rand})}
=\frac{361}{290}\approx1.24483.}
\]
Thus a partition with distinct cluster means and perfect angular separation can yield about \(24.5\%\) *larger* meta-gradient selection variance after the paper's stated rounding rule.

For comparison, if the same population is sampled with budget \(m=10\), exact proportional counts are \((m_1,m_2)=(7,3)\). Then
\[
\operatorname{Var}(\widehat G_{\rm cl})=\frac{7581}{5000},\qquad
\operatorname{Var}(\widehat G_{\rm rand})=\frac{4263}{2500},
\]
and their difference is exactly \(\sigma_B^2/10=189/1000>0\), as the source theorem predicts. The reversal is therefore caused by the allocation mismatch, not by a failure of the ANOVA identity.

## Corrected criterion and repair

For arbitrary positive integer counts \(m_k\), the exact necessary-and-sufficient condition for clustered sampling to beat uniform sampling under the same with-replacement model is
\[
\boxed{
\sigma_B^2\ge
\sum_kp_k\sigma_k^2\left(\frac{p_k}{q_k}-1\right),
\qquad q_k=m_k/m.}
\]
A convergence argument that uses the BS-selection second moment should therefore substitute
\[
V_{\rm sel}=\sum_k\frac{p_k^2\sigma_k^2}{m_k}
\]
for the selection-variance term of the actual rounded sampler, rather than \(\sigma_W^2/m\) unless exact proportionality holds.

Two standard repairs are available. First, evaluate the displayed variance criterion after integer allocation and fall back to uniform sampling whenever it fails. Second, when within-cluster variances are available, choose counts by variance-aware stratified allocation instead of size-only rounding. In the continuous relaxation, minimizing \(\sum_kp_k^2\sigma_k^2/m_k\) subject to \(\sum_km_k=m\) gives the classical Neyman rule
\[
m_k\propto p_k\sigma_k,
\]
with integer-constrained exact allocation handled by established stratified-sampling methods. These repairs preserve the source paper's useful stratification idea while removing the unsupported transfer from exact proportional counts to rounded counts.

## Relation to the source paper

Niknia and Wang define a practical clustered sampler that rounds \(m n_k/N\) to integer counts while requiring at least one sample from each cluster. Their convergence analysis later assumes that \(m n_k/N\) is already a positive integer and proves
\[
\operatorname{Var}(\widehat G_{\rm cl})=\sigma_W^2/m,
\qquad
\operatorname{Var}(\widehat G_{\rm rand})-\operatorname{Var}(\widehat G_{\rm cl})=\sigma_B^2/m.
\]
The paper also states that the result is exact and universal and that stale clustering can never make clustered sampling worse than random. Those claims are correct for the exact proportional sampler analyzed in the theorem, but the counterexample above shows that they do not extend to the rounded practical sampler without an additional allocation condition.

The paper's experiments use \(N=60\) training BSs, \(K=6\) clusters, and budget \(m=10\). Exact proportional integer allocation would require each cluster size \(n_k\) to make \(n_k/6\) an integer. The published text does not report the realized cluster sizes, so this record does **not** claim that the reported experiment encountered the counterexample or violated the exact-proportional condition. It only identifies the missing guarantee for the stated practical rule.

## Limitations

This result does not contradict the source paper's Theorem 3 when its exact proportional integer-allocation assumption is satisfied. It does not evaluate the reported learning curves, does not claim that rounded allocation usually increases variance, and does not analyze sampling without replacement. The counterexample concerns the BS-selection variance under the same independent-with-replacement model used in the source analysis. The optimal-allocation observation is classical stratified-sampling theory; the new contribution claimed here is the paper-specific exact criterion, explicit cosine-compatible reversal, and the resulting correction to the practical variance/convergence guarantee.

## Reproducibility

`artifacts/verify_rounding_counterexample.py` uses exact rational arithmetic to verify all cluster moments, both variances, their ratio, and the exact-proportional comparison. `artifacts/verified_output.txt` contains its executed output.

## References

1. F. Niknia and P. Wang, *Fast-Convergent Meta-RL via Gradient-Clustered BS Sampling for Edge Caching*, arXiv:2609.16370v1 (2026). https://arxiv.org/abs/2609.16370v1
2. T. Wright, *Two Optimal Exact Sample Allocation Algorithms: Sampling Variance Decomposition is Key*, U.S. Census Bureau Statistical Research Report RRS2016-03 (2016). https://www.census.gov/library/working-papers/2016/adrm/rrs2016-03.html
3. T. Wright, *The Equivalence of Neyman Optimum Allocation for Sampling and Equal Proportions for Apportioning the U.S. House of Representatives*, The American Statistician 66(4), 217--224 (2012). https://doi.org/10.1080/00031305.2012.733679
