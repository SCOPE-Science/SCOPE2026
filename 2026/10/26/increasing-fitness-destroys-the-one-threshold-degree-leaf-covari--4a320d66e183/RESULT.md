# Increasing fitness destroys the one-threshold degree–leaf covariance profile in recursive trees

## Finding

Let \(n\ge3\). Build a weighted random recursive tree with deterministic weights \(w_1,\ldots,w_n>0\), where the parent of arrival \(k\) is independently chosen among \(j<k\) with probability \(w_j/W_{k-1}\), and \(W_m=\sum_{j=1}^m w_j\). Let \(D_i\) be the number of children of vertex \(i\), and let \(L\) count vertices with no children (the root is excluded automatically when \(n\ge2\)).

**Theorem.** For every strictly positive weight vector, define
\[
p_j=\prod_{t=j+1}^{n}\left(1-\frac{w_j}{W_{t-1}}\right),\quad 2\le j\le n.
\]
For each \(2\le i\le n\), the full exact finite covariance is
\[
\operatorname{Cov}(D_i,L)=\sum_{k=i+1}^{n}\frac{w_i}{W_{k-1}}\left[-p_i+\sum_{\substack{2\le j<k\\j\ne i}}\frac{w_j p_j}{W_{k-1}-w_j}\right]. \tag{1}
\]
For every \(n\ge3\) and every positive weight vector, \(\operatorname{Cov}(D_{n-1},L)<0\); also \(\operatorname{Cov}(D_n,L)=0\).

Even *strictly increasing* weights do not enforce an ordered one-threshold sign profile among the nonroot covariances. At the first possible order \(n=5\), the weights \((1,2,6,7,8)\) give
\[
\big(\operatorname{Cov}(D_2,L),\operatorname{Cov}(D_3,L),\operatorname{Cov}(D_4,L)\big)
=\left(-\frac{2087}{31104},\ \frac{25}{10368},\ -\frac{1225}{6912}\right).\tag{2}
\]
Thus signs in birth order alternate \(-,+,-\), unlike the single-sign-threshold profile for equal weights. For \(n\le4\), there are fewer than three nonroot vertices with potentially nonzero child counts, making this alternating pattern impossible. Since (2) is strict and finite-dimensional covariances depend continuously on positive weights, the phenomenon persists on a nonempty open neighborhood of strictly increasing weight vectors.

## Assumptions and scope

Edges are directed from a younger vertex to its parent only for bookkeeping; \(D_i\) always means the number of *children*, not the parent edge. Parents at successive arrivals are independent. All prescribed weights are finite, deterministic and strictly positive. The root, vertex \(1\), has at least one child at size \(n\ge2\), and \(D_n=0\) deterministically. The theorem is a finite-distribution identity for every \(n\ge3\); it does not average over a distribution of weights.

## Proof

Write \(B_{ki}=\mathbf 1\{\operatorname{parent}(k)=i\}\) for \(i<k\). Then \(D_i=\sum_{k=i+1}^n B_{ki}\). For \(j\ge2\), write \(X_j=\mathbf1\{D_j=0\}\); thus \(L=\sum_{j=2}^n X_j\). Independence of parent choices over arrivals implies \(\mathbb E X_j=p_j\) as given above.

Fix \(2\le i<k\le n\). If \(j\ge k\), the events defining \(X_j\) concern only arrivals after \(j\), so \(\operatorname{Cov}(B_{ki},X_j)=0\). If \(j=i\), then \(B_{ki}X_i=0\) and
\[
\operatorname{Cov}(B_{ki},X_i)=-\frac{w_i}{W_{k-1}}p_i.
\]
If \(2\le j<k\) and \(j\ne i\), the events \(\{\operatorname{parent}(k)=i\}\) and \(\{\operatorname{parent}(k)=j\}\) are disjoint. Conditioning on the first event guarantees that arrival \(k\) did not select \(j\), and all other attachment choices remain independent. Consequently,
\[
\mathbb E[B_{ki}X_j]=\frac{w_i}{W_{k-1}}\frac{p_j}{1-w_j/W_{k-1}},
\quad
\operatorname{Cov}(B_{ki},X_j)=\frac{w_i}{W_{k-1}}\frac{w_jp_j}{W_{k-1}-w_j}.
\]
Every denominator is strictly positive, since the root is present and has positive weight. Summing these identities over \(j\) and \(k\) gives (1).

To prove the penultimate-vertex sign, let \(Y\) be the parent chosen by vertex \(n\), and condition on the existing tree of size \(n-1\). The new leaf replaces the old leaf at \(Y\) if that parent is childless, so
\[
L_n=L_{n-1}+1-\mathbf1\{D_Y(n-1)=0\}.
\]
If \(Y=n-1\), the right side equals \(L_{n-1}\), since the youngest existing vertex is certainly a leaf. If \(Y\ne n-1\), it is at least \(L_{n-1}\), and with strictly positive probability \(Y=1\) it equals \(L_{n-1}+1\), since the root is not a leaf at size \(n-1\ge2\). The choice of \(Y\) is independent of the previous tree. Hence
\(\mathbb E[L_n\mid Y=n-1]<\mathbb E[L_n\mid Y\ne n-1]\).
Both conditioning events have positive probability and \(D_{n-1}=\mathbf1\{Y=n-1\}\); the elementary Bernoulli-covariance identity gives \(\operatorname{Cov}(D_{n-1},L_n)<0\). Finally \(D_n=0\) gives its vanishing covariance.

For \(n=5\), evaluate (1) at weights \((1,2,6,7,8)\), for which \((W_1,W_2,W_3,W_4)=(1,3,9,16)\). Simplification gives the exact fractions (2). Alternatively one can enumerate all \((n-1)!=24\) independent parent-choice combinations, weighting each by \(\prod_{k=2}^5 w_{\operatorname{parent}(k)}/W_{k-1}\); this independently gives (2). At \(n\le4\), only indices \(2,\ldots,n-1\) can have random nonroot child counts, and there are at most two of them, proving minimality for a three-term alternation. Continuity follows because every joint probability is a rational function of positive weights with nonvanishing denominator. This completes the proof.

## Verification

Run `python3 checker.py` with Python's standard library. The code calculates (1) in exact rational arithmetic and separately enumerates all independent parent assignments, without using (1) in its enumeration branch. It verifies the strict-increasing witness, and performs 2,400 exact-rational assertions over systematic small weight families through six vertices. These tests check the calculation, not the unrestricted theorem; the preceding proof establishes the latter.

## Relationship to prior work

Hiesmayr's 2017 study introduced deterministic weighted recursive trees and treated leaf-count moments, particularly for a special weight family where the first several weights are equal and later weights are one. Eslava, Lodewijks and Ortgiese (2021 preprint, 2023 journal article) study high-degree and maximum-degree asymptotics in weighted recursive trees, with vertex weights sampled from a distribution. Neither of the inspected relevant results states the exact fixed-vertex degree–leaf covariance (1) or the strictly-increasing-weight sign reversal (2). Classical equal-weight recursive-tree identities have a one-threshold chronological sign pattern; that special case does not imply the heterogeneous assertion. The contribution claimed here is the exact weighted cross-covariance together with the smallest-order strictly increasing fitness counterexample, not the tree model or existing leaf-count asymptotics.

## Limitations

The counterexample disproves a general chronological sign-threshold law, but it does not classify all weight vectors or all possible sign patterns. The result concerns linear covariance, not conditional dependence, and does not treat preferential attachment by evolving degrees. The fifth vertex's weight is irrelevant to its own arrival and is chosen to maintain strict increase. The independent scientific audit is not performed; an earlier implicit weighted-moment formula remains a priority risk.

## References

1. E. Hiesmayr, *On Asymptotics of Two Non-Uniform Recursive Tree Models*, arXiv:1710.01402 (first posted 2017-10-03), particularly Chapter 4, Section 4.5.
2. L. Eslava, B. Lodewijks and M. Ortgiese, *Fine asymptotics for the maximum degree in weighted recursive trees with bounded random weights*, arXiv:2109.15270 (first posted 2021-09-30), especially Sections 1–2.
