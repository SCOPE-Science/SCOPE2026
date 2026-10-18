# Exact cherry–Sackin covariance in Yule phylogenetic trees

## Finding

**Theorem.** Generate a rooted binary phylogenetic tree with \(n\) leaves by starting from one leaf and repeatedly replacing one uniformly selected extant leaf by two children; assign any distinct leaf labels after growth. Let \(C_n\) count *cherries* (internal vertices with two leaf children) and let \(S_n\) be the *Sackin index* (sum of the numbers of edges from the root to every leaf). Then, for every integer \(n\geq3\),

\[
\operatorname{Cov}(C_n,S_n)=-\frac{n}{9}+\frac{2}{3(n-1)}=\frac{6-n(n-1)}{9(n-1)}.
\]

The covariance vanishes at \(n=3\) and is strictly negative for all \(n\geq4\). Thus \(\operatorname{Cov}(C_n,S_n)/n\to-1/9\). At \(n=2\) both indices are deterministic, so their covariance is zero (the displayed formula is not applied at \(n=2\)).

For every \(n\geq5\), the variance of the cherry count is \(2n/45\), and hence the exact least-squares slope of Sackin on cherries is

\[
\frac{\operatorname{Cov}(C_n,S_n)}{\operatorname{Var}(C_n)}=-\frac52+\frac{15}{n(n-1)}.
\]

Write \(H_n=\sum_{j=1}^n1/j\) and \(H_n^{(2)}=\sum_{j=1}^n1/j^2\). Combining the covariance with the established Yule variance of Sackin [2] gives, for \(n\geq5\),

\[
\operatorname{Corr}(C_n,S_n)=
\frac{-n/9+2/[3(n-1)]}
{\sqrt{(2n/45)\{7n^2-4n^2H_n^{(2)}-2nH_n-n\}}},
\]

and its explicit first-order decay is

\[
\lim_{n\to\infty}\sqrt n\,\operatorname{Corr}(C_n,S_n)
=-\frac19\sqrt{\frac{45}{2(7-2\pi^2/3)}}
\approx-0.812994847.
\]

This separates two effects: the unscaled cross-covariance grows linearly in magnitude while the Pearson correlation vanishes at the square-root rate.

## Assumptions and scope

The model is the rooted Yule–Harding–Kingman equal-rate leaf-splitting law, not the uniform/PDA law on labeled tree topologies. Children are unordered in the mathematical tree; using an ordered representation in a verifier only records growth histories with their correct weights. Root-to-leaf distances count edges, not branch lengths or elapsed speciation time. There are no extinct lineages, polytomies, or conditioned branch lengths. All statements are exact for the stated finite integer ranges; no claims concerning full joint distributions or Gaussian limits are made.

## Proof

**1. Root decomposition and means.** An ordered designation of the two root subtrees has leaf counts \(K\) and \(n-K\), where \(K\) is uniform on \(\{1,\ldots,n-1\}\); conditional on \(K\), the two subtrees are independent Yule trees. This is the standard root-split representation of the specified equal-rate process [2,3]. For \(n\geq3\),

\[
C_n=C_K+C'_{n-K},\qquad S_n=S_K+S'_{n-K}+n.
\]

Here the primes indicate an independent subtree. The special two-leaf tree consists of one cherry, so \(C_1=0\), \(C_2=1\), \(S_1=0\), and \(S_2=2\); the recursive cherry formula is used only for \(n\geq3\). Writing \(c_j=\mathbb EC_j\) and \(s_j=\mathbb ES_j\), the expectation recursions yield

\[
c_j=\frac j3\quad(j\geq3),\qquad s_j=2j(H_j-1)\quad(j\geq1).
\]

For completeness, \(c_3=1\), and, if the cherry expectation formula holds below \(n\geq4\), its deviation from \(j/3\) is \(-1/3\) at \(j=1\), \(+1/3\) at \(j=2\), and zero otherwise. These deviations sum to zero, so the uniform-root-split recursion gives \(c_n=n/3\). Similarly, the recurrence for \(s_n\), together with the elementary harmonic-sum identity \(\sum_{j=1}^{n-1}jH_j=n(n-1)H_{n-1}/2-(n-1)(n-2)/4\) after appropriate reindexing, or direct telescoping of successive means, proves the displayed Sackin expectation. (In fact the exact identity used below is \(s_{m+1}-s_m=2H_m\).)

**2. Covariance recurrence.** Let \(v_n=\operatorname{Cov}(C_n,S_n)\) and \(\delta_j=c_j-j/3\). Define the two conditional means \(g_k=c_k+c_{n-k}\) and \(h_k=s_k+s_{n-k}+n\). Independence of the two root subtrees and the law of total covariance give

\[
 v_n=\frac2{n-1}\sum_{j=1}^{n-1}v_j+F_n,
 \qquad F_n=\operatorname{Cov}(g_K,h_K),\qquad n\geq3.
\]

Since \(\delta_1=-1/3\), \(\delta_2=1/3\), and all later \(\delta_j\) vanish, the conditional cherry mean is \(g_k=n/3+\delta_k+\delta_{n-k}\). Its average is \(n/3\), and symmetry of the uniform split yields

\[
\begin{aligned}
F_n&=\frac{2}{n-1}\sum_{k=1}^{n-1}\delta_k(s_k+s_{n-k})\\
&=\frac2{3(n-1)}\big[(s_2+s_{n-2})-(s_1+s_{n-1})\big]\\
&=\frac{4(1-H_{n-2})}{3(n-1)}.
\end{aligned}
\]

The last equality uses \(s_{m+1}-s_m=2H_m\); it includes the boundary \(n=3\) exactly. The initial covariances \(v_1=v_2=v_3=0\). Suppose that \(v_j=-j/9+2/[3(j-1)]\) for \(3\leq j<n\). Then

\[
\frac2{n-1}\sum_{j=1}^{n-1}v_j
=-\frac n9+\frac2{3(n-1)}+\frac{4(H_{n-2}-1)}{3(n-1)}.
\]

Adding the derived \(F_n\) cancels the harmonic term and proves the covariance formula by induction. Negativity for \(n\geq4\) follows from \(n(n-1)>6\). The linear asymptotic follows immediately.

**3. Cherry variance and least-squares slope.** Let \(w_n=\operatorname{Var}(C_n)\). Total variance gives \(w_n=2\sum_{j<n}w_j/(n-1)+G_n\), where \(G_n=\operatorname{Var}(g_K)\). The same four boundary split positions with deviations \(\pm1/3\) imply \(G_n=4/[9(n-1)]\) for every \(n\geq5\). Direct evaluation gives \(w_1=w_2=w_3=0\), \(w_4=2/9\), \(w_5=2/9\). Induction on the recurrence establishes \(w_n=2n/45\) for \(n\geq5\). Divide the proven covariance by this variance to obtain the regression slope. This cherry-variance formula is also established in the pre-existing cherry-count literature [1,3]; it is not asserted to be novel here.

**4. Correlation.** The previously proved exact Yule Sackin variance [2] is

\[
\operatorname{Var}(S_n)=7n^2-4n^2H_n^{(2)}-2nH_n-n.
\]

It is independently reproduced by applying total variance to the root decomposition and matching the initial conditions; the accompanying checker tests this identity separately through \(n=120\). Substitution gives the exact displayed Pearson correlation. Since \(H_n^{(2)}\to\pi^2/6\) and \(H_n/n\to0\), its stated square-root asymptotic follows. The constant \(7-2\pi^2/3\) is positive.

## Verification

Run the supplied standalone Python file `verify.py` with a standard Python 3 interpreter. It performs **754 exact-rational assertions**. One computation enumerates all uniform leaf-splitting histories through nine leaves, using integer history multiplicities without the root-split moment recurrence. An independent computation applies exact rational root-split moment recursions through 120 leaves, checking both means, the claimed covariance, the cherry variance, the prior Sackin variance, and the regression identity. Both checks print `VERIFICATION_OK`. Enumeration alone is not the proof for all tree sizes; the induction above provides that proof.

## Relationship to prior work

The cherry/pitchfork distribution results of Choi, Thompson and Wu [1] and earlier Wu–Choi results [3] determine important cherry statistics under Yule and PDA laws, but their inspected full text concerns cherries jointly with pitchforks, not with Sackin. Cardona, Mir and Rosselló [2] establish the Yule Sackin variance and its covariance with the total cophenetic index; the \(C\) in that paper denotes **Colless imbalance**, not cherry count. Their general recursive-shape-index moment machinery supplies an applicable method, but its results do not state or algebraically evaluate the cherry–Sackin covariance. Coronado and collaborators [4] address the Sackin index and leaf-depth variance, not this cherry–Sackin cross-moment. Janzen and Etienne [5] study model-dependent correlations between tree statistics empirically and numerically, motivating an exact Yule calibration rather than directly implying it. The new contribution claimed here is the evaluated finite covariance, its strict sign, and the resulting exact regression and asymptotic correlation formulas, not a new tree-generating model or a general moment recursion.

## Limitations

The covariance law is specific to the Yule leaf-splitting model and to the stated rooted cherry and edge-depth conventions. The Pearson correlation uses published Sackin second moments and does not show a joint central limit theorem, stochastic ordering, or causal relation between metrics. No exact covariance under the PDA model is claimed. Earlier general recursive-index methods can in principle be specialized to evaluate cross-moments; an uncatalogued prior specialization is a residual historical-priority risk. The result has not undergone independent validation.

## References

1. K. P. Choi, A. Thompson and T. Wu, *On cherry and pitchfork distributions of random rooted and unrooted phylogenetic trees*, arXiv:2002.12643 (first posted 2020-02-28), *Theoretical Population Biology* 132 (2020), 92–104. https://arxiv.org/abs/2002.12643 ; https://doi.org/10.1016/j.tpb.2020.02.001
2. G. Cardona, A. Mir and F. Rosselló, *Exact formulas for the variance of several balance indices under the Yule model*, arXiv:1202.6573 (first posted 2012-02-29), *Journal of Mathematical Biology* 67 (2013), 1833–1846. https://arxiv.org/abs/1202.6573 ; https://doi.org/10.1007/s00285-012-0615-9
3. T. Wu and K. P. Choi, *On joint subtree distributions under two evolutionary models*, *Theoretical Population Biology* 108 (2016), 13–23. https://doi.org/10.1016/j.tpb.2015.11.004
4. T. M. Coronado, A. Mir, F. Rosselló and L. Rotger, *On Sackin’s original proposal: the variance of the leaves’ depths as a phylogenetic balance index*, *BMC Bioinformatics* 21 (2020), 154. https://doi.org/10.1186/s12859-020-3405-1
5. T. Janzen and R. S. Etienne, *Phylogenetic tree statistics: A systematic overview using the new R package ‘treestats’*, *Molecular Phylogenetics and Evolution* 200 (2024), 108168 (first available 2024-08-06). https://doi.org/10.1016/j.ympev.2024.108168
