# Leaf-conditioned convex ordering of a marked degree in uniform Cayley trees

## Finding

For every integer \(n\ge4\), let \(T\) be uniform among the \(n^{n-2}\) labeled trees on \([n]\). Write \(L\) for the number of leaves and \(D\) for the degree of any one predetermined labeled vertex. For each \(2\le k<\ell\le n-1\),

\[
D\mid(L=k)\ <_{\mathrm{cx}}\ D\mid(L=\ell),
\]

where strict convex ordering means equality of means, inequality of expectations for every convex real function on the finite degree range, and strict inequality for every strictly convex such function. Nevertheless, the conditional mean is constant:

\[
\mathbb E[D\mid L=k]=2-\frac2n.
\]

More precisely, let \(m=n-2\), \(q=n-k\), \(J=D-1\), and \(S(a,b)\) denote a Stirling number of the second kind, with \(S(0,0)=1\) and zero outside its combinatorial range. Then

\[
\Pr(J=0\mid L=k)=\frac{k}{n},\qquad
\Pr(J=j\mid L=k)=\frac1n\binom mj\frac{S(m-j,q-1)}{S(m,q)}\quad(1\le j\le m).
\tag{1}
\]

For every pair \(k<\ell\), the difference of conditional degree-tail probabilities, as an integer threshold \(d\) rises, changes sign **exactly once** in the weak sense: it is negative at \(d=2\), may vanish at intermediate thresholds, and is strictly positive at \(d=k+1\); it never returns to negative after becoming positive. Equivalently, the positive-count probability-mass difference undergoes one transition from negative to positive. In particular,

\[
\operatorname{Cov}(h(L),D)=0
\]

for any real function \(h\), while \(\operatorname{Cov}(h(L),D^2)>0\) for every strictly increasing \(h\) on the possible leaf counts. The exact conditional variance is

\[
\operatorname{Var}(D\mid L=k)=\frac mn-\frac{m^2}{n^2}
+\frac{m(m-1)}n\frac{S(m-1,q)}{S(m,q)},
\tag{2}
\]

and it strictly increases with the number of leaves.

## Assumptions and scope

The tree is uniformly sampled from all labeled, unrooted, simple trees of order \(n\); the marked vertex is fixed independently of the random tree. No asymptotic approximation is involved. Each conditioning event \(L=k\) has positive probability precisely for \(2\le k\le n-1\). The convex-order assertion concerns the one-dimensional degree of one fixed vertex; it does not assert multivariate convex ordering of whole degree sequences. Strict convexity is understood on the interval of possible integer degrees.

The notation \(X\le_{\mathrm{cx}}Y\) means \(\mathbb E\phi(X)\le\mathbb E\phi(Y)\) for every convex \(\phi\), with equal finite means. The strict symbol in the finding asserts a strict inequality whenever \(\phi\) is strictly convex. All boundary cases, including a star with \(n-1\) leaves, are included.

## Proof

**1. Reduction to a uniform occupancy scheme.** Under the Prüfer bijection, the tree corresponds to a uniformly chosen word of length \(m=n-2\) over \([n]\). Let \(J_v\) count appearances of label \(v\). Then \(\deg_T(v)=1+J_v\) and \(L=n-\#\{v:J_v>0\}\). Conditioning on \(L=k\) is conditioning the word to have exactly \(q=n-k\) distinct symbols. There are \(\binom nq q!S(m,q)\) such words. By exchangeability, the marked symbol is missing with probability \((n-q)/n=k/n\). To force it to appear \(j\ge1\) times, select its \(j\) positions and partition the other positions among exactly \(q-1\) used labels: the number is \(\binom mj\binom{n-1}{q-1}(q-1)!S(m-j,q-1)\). Division by the total gives (1). Exchangeability and \(\sum_vJ_v=m\) imply \(\mathbb E[J\mid L=k]=m/n\), independent of \(k\).

**2. A needed strict ratio lemma.** For every integer \(t\ge2\), the ratio

\[
R_t(N)=\frac{S(N,t-1)}{S(N,t)}
\]

is strictly decreasing for integers \(N\ge t\). To prove the requisite row log-concavity without appealing to a numerical table, set \(B_N(z)=\sum_{r=0}^NS(N,r)z^r\). The Stirling recurrence yields \(B_{N+1}(z)=z(B_N(z)+B_N'(z))\), starting at \(B_1(z)=z\). If \(B_N\) has simple nonpositive real roots, then \(B_N+B_N'\) has one simple negative root in each interval between consecutive roots and one to their left, because \(1+B_N'/B_N=1+\sum_i(z-r_i)^{-1}\) is strictly decreasing between its poles and has the requisite opposite endpoint signs. The additional factor \(z\) gives the next simple zero root. Induction proves simple nonpositive real-rootedness, hence log-concavity of all positive coefficient rows:

\[
S(N,t-1)^2\ge S(N,t-2)S(N,t).
\]

Writing \(A=S(N,t-1)>0\), \(B=S(N,t-2)\), \(C=S(N,t)>0\), the recurrence gives

\[
R_t(N+1)=\frac{(t-1)A+B}{tC+A}<\frac AC=R_t(N)
\]

because the strict inequality is equivalent to \(BC<AC+A^2\), which follows from \(BC\le A^2\) and \(AC>0\). This includes \(t=2\), with the usual zero-column convention.

**3. Single crossing of the conditional mass laws.** Let \(p_k(j)=\Pr(J=j\mid L=k)\). For neighboring leaf strata, \(q=n-k\ge3\), formula (1) gives on the common positive support

\[
\frac{p_{k+1}(j)}{p_k(j)}
=\frac{S(m,q)}{S(m,q-1)}
\frac{S(m-j,q-2)}{S(m-j,q-1)}.
\tag{3}
\]

The last factor is strictly increasing in \(j\) by step 2; the distribution with one more leaf also has a new strictly positive top cell. When \(q=2\), the next stratum has only \(j=m\) as a positive count, and the same single-crossing conclusion is immediate. Multiplying the adjacent likelihood ratios yields the corresponding nondecreasing ratio for any pair \(k<\ell\) on their common positive support, with an enlarged right endpoint. Since \(p_\ell(0)-p_k(0)=(\ell-k)/n>0\) but both total masses are one, some positive-cell difference is negative. Since the upper support is larger in the higher-leaf stratum, some positive-cell difference is strictly positive. The monotone ratios imply precisely one weak sign transition from negative to positive among the positive cells.

**4. Tail sign and convex order.** Define \(\Delta_j=p_\ell(j)-p_k(j)\) and \(H_t=\sum_{j\ge t}\Delta_j\) for integer \(t\ge1\). We have \(H_1=-(\ell-k)/n<0\). By step 3 the \(\Delta_j\) for positive \(j\) are initially negative and thereafter positive, so the right tails \(H_t\) cross from negative to positive at most once. At threshold \(t=k\), the smaller-leaf stratum has no mass (its positive \(J\)-support ends at \(k-1\)), whereas the larger-leaf stratum has positive mass, so \(H_k>0\). Thus the tail crossing is unique, apart from possibly zero ties.

The constant conditional mean gives \(\sum_{t=1}^mH_t=\mathbb E[J\mid L=\ell]-\mathbb E[J\mid L=k]=0\). Consequently for every integer \(r\ge0\),

\[
\mathbb E[(J-r)_+\mid L=\ell]-\mathbb E[(J-r)_+\mid L=k]
=\sum_{t=r+1}^mH_t\ge0.
\]

For \(1\le r\le\ell-2\) the inequality is strict; for \(r=0\) it is equality by the mean identity. The stop-loss characterization of convex order now proves the theorem, because every convex function on the finite integer range is an affine function plus a nonnegative linear combination of the hinge functions \((x-r)_+\). A strictly convex function gives positive weight to at least one nontrivial hinge, giving strictness. Translation by one transfers the statement from \(J\) to \(D\).

**5. Variance and dependence consequences.** Given exactly \(q\) used word symbols, merging the first two positions shows \(\Pr(W_1=W_2\mid q)=S(m-1,q)/S(m,q)\), where \(W_i\) is the symbol in position \(i\). By symmetry, \(\Pr(W_1=W_2=v\mid q)\) is one \(n\)-th of that probability. Therefore

\[
\mathbb E[J(J-1)\mid L=k]
=\frac{m(m-1)}n\frac{S(m-1,q)}{S(m,q)}.
\]

Together with the fixed mean this proves (2). Strict convex order implies that the conditional second moment, and hence the variance, strictly increases with \(k\). The conditional mean identity yields zero covariance of \(D\) against any function of \(L\). The strict monotonicity of \(\mathbb E[D^2\mid L=k]\) yields positive covariance with every strictly increasing function of \(L\), by the independent-copy identity \(2\operatorname{Cov}(U,V)=\mathbb E[(U-U')(V-V')]\).

## Verification

The accompanying standalone standard-library program `artifacts/verify.py` recomputes all formulas using exact integer and rational arithmetic. It exhaustively enumerates every Prüfer word for \(4\le n\le8\), then checks probability normalization, the conditional mean, factorial moments, pairwise convex stop-loss inequalities and likelihood-ratio/tail sign comparisons for \(4\le n\le33\). It reports 448491 exact assertions passed. Enumeration checks are finite tests; they are not the proof of the statements for arbitrary \(n\). The general result follows from steps 1–5 above.

To run after extracting the files, execute `python3 artifacts/verify.py` from the directory containing `artifacts`.

## Relationship to prior work

Remmel and Williamson's 2010 preprint classifies and constructs uniformly random labeled trees with prescribed leaves via functions and ordered set partitions. Its exact leaf-count and degree-sequence counts supply the familiar combinatorial starting point for (1); the new assertion here is the strict leaf-conditioned **convex order and unique degree-tail sign crossing**, which require comparison across distinct leaf strata and are not direct restatements of its counts. Wagner's 2012 and 2014/2015 work develops asymptotic central limit results for additive parameters of random trees, including leaves; these do not give the finite-size one-vertex conditional ordering. A published one-switch law for unconditional covariance of occupancy richness with frequency counts concerns a different assertion: it does not provide a conditional distributional order of a fixed labeled box across exact richness levels. Aldous's work supplies probabilistic random-tree background. No priority claim is made for the classical Prüfer encoding, the Stirling-number counts, or row real-rootedness.

## Limitations

The ordering applies only to uniform **labeled Cayley** trees and a single predetermined marked vertex. It does not assert analogous statements for nonuniform trees, joint ordered degree vectors, or a fixed degree when the marked vertex itself depends on the tree. The exact conditional mass law follows from established counting tools; originality is assessed only for the all-leaf-strata convex ordering, sharp tail crossing, and dependence implications. Literature coverage is not exhaustive: older occupancy total-positivity or random-tree literature could contain equivalent formulations. No independent validation has been performed.

## References

1. J. B. Remmel and S. G. Williamson, *Ranking and unranking trees with a given number or a given set of leaves*, arXiv:1009.2060, first posted 2010-09-10. https://arxiv.org/abs/1009.2060
2. S. Wagner, *Additive tree functionals with small toll functions and subtrees of random trees*, DMTCS Proceedings AQ, 2012, DOI:10.46298/dmtcs.2984. https://dmtcs.episciences.org/en/articles/2984
3. S. Wagner, *Central limit theorems for additive tree parameters with small toll functions*, *Combinatorics, Probability and Computing* 24 (2015), 329–353; first published online 2014-09-08, DOI:10.1017/S0963548314000443. https://doi.org/10.1017/S0963548314000443
4. D. J. Aldous, *The random walk construction of uniform spanning trees and uniform labelled trees*, *SIAM Journal on Discrete Mathematics* 3 (1990), DOI:10.1137/0403039. https://doi.org/10.1137/0403039
