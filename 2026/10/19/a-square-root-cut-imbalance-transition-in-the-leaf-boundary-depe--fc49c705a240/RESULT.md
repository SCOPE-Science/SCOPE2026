# A square-root cut-imbalance transition in the leaf–boundary dependence of random labeled trees

## Finding

Let \(T\) be a uniformly random labeled tree on \([n]\), where \(n\ge3\). Choose a deterministic nonempty proper subset \(S\subset[n]\), and put \(a=|S|\), \(b=n-a\). Let \(L\) be the total number of degree-one vertices and \(C\) the number of edges of \(T\) with exactly one endpoint in \(S\). Then

\[\operatorname{Cov}(L,C)=0,\qquad \operatorname{Cov}(L,C^2)=\frac{ab}{n(n-1)^2}\left(\frac{n-1}{n}\right)^{n-2}\big((a-b)^2-n+2\big).\]

The second covariance is negative precisely when \(|a-b|<\sqrt{n-2}\), zero precisely when \(|a-b|=\sqrt{n-2}\), and positive precisely when \(|a-b|>\sqrt{n-2}\). In particular, uncorrelated linear leaf and cut counts can exhibit either sign of quadratic dependence, with an exact square-root boundary in the partition imbalance.

## Assumptions and scope

All labels are distinct; every one of the \(n^{n-2}\) Cayley trees is equally likely. The subset \(S\) is fixed before drawing the tree, not sampled or chosen adaptively. Covariances are ordinary centered real covariances. The theorem applies for every integer \(n\ge3\) and all \(1\le a<n\), including singleton sides and the exceptional zero-covariance parameter pairs.

## Proof

Write \(I_e\) for the indicator that an edge \(e\) of the complete graph belongs to \(T\); write \(Y_v\) for the indicator that vertex \(v\) is a leaf. Standard Prüfer counting gives

\[p_n:=\Pr(Y_v=1)=\left(\frac{n-1}{n}\right)^{n-2}.\]

Conditionally on \(Y_v=1\), the unique neighbor of \(v\) is uniform on the other \(n-1\) labels, and deleting \(v\) produces an independent uniform Cayley tree on the remaining \(n-1\) vertices. This follows bijectively: for each fixed neighbor, every Cayley tree on the remaining labels has exactly one such leaf extension.

For a fixed edge \(e\), \(\Pr(I_e=1)=2/n\). If \(v\) is an endpoint of \(e\), the leaf-conditioned inclusion probability is \(1/(n-1)\); otherwise it is \(2/(n-1)\). Consequently, summing over all possible leaf vertices gives

\[\mathbb E[L I_e]=p_n\frac{2+2(n-2)}{n-1}=2p_n=\mathbb E[L]\,\mathbb E[I_e].\]

Thus each edge indicator is uncorrelated with \(L\), establishing the first claim after summing over cut edges.

For distinct edges \(e,f\), there are two isomorphism types. The ordinary Cayley forest-extension formula, or contraction of the prescribed forest, gives

\[\Pr(I_eI_f=1)=\begin{cases}3/n^2,&e,f\text{ share a vertex},\\4/n^2,&e,f\text{ are disjoint}.\end{cases}\]

For adjacent edges, a leaf cannot lie at their common endpoint. Each of the other two endpoints contributes \(2p_n/(n-1)^2\) to \(\mathbb E[L I_eI_f]\), and each of the remaining \(n-3\) vertices contributes \(3p_n/(n-1)^2\). For disjoint edges, each of their four endpoints contributes \(2p_n/(n-1)^2\), while each of the other \(n-4\) vertices contributes \(4p_n/(n-1)^2\). Therefore

\[\operatorname{Cov}(L,I_eI_f)=\frac{p_n}{n(n-1)^2}\begin{cases}n-3,&e,f\text{ adjacent},\\-4,&e,f\text{ disjoint}.\end{cases}\]

For \(n=3\), only the adjacent case occurs; the disjoint-edge calculation is needed only for \(n\ge4\).

There are \(ab\) possible edges crossing the fixed cut. Among unordered pairs of distinct crossing edges, exactly \(ab(n-2)/2\) pairs share an endpoint and \(ab(a-1)(b-1)/2\) pairs are disjoint. Since

\[C^2=C+2\sum_{\{e,f\}\subseteq\delta(S)} I_eI_f,\]

and \(\operatorname{Cov}(L,C)=0\), we obtain

\[\operatorname{Cov}(L,C^2)=\frac{ab p_n}{n(n-1)^2}\big((n-2)(n-3)-4(a-1)(b-1)\big).\]

Using \(a+b=n\), the parenthesis simplifies exactly to \((a-b)^2-n+2\). Every other prefactor is strictly positive, so the stated exhaustive sign classification follows. This completes the proof.

## Verification

The accompanying independent standard-library script `verify_leaf_cut.py` enumerates every Prüfer word and computes exact rational covariances for every fixed-cut size, for each \(3\le n\le8\). The complete check covers \(280391\) labeled trees and \(27\) parameter pairs, verifying both the zero linear covariance and the exact quadratic formula. It is finite corroboration only; the proof above is valid without a finite cutoff.

## Relationship to prior work

Lyons' determinantal treatment of uniform spanning trees provides general edge-inclusion dependence and forest methods. Goyal–Rademacher–Vempala study cut expansion for random spanning trees. The present formula asks a different question: how the total number of leaves co-varies with a *quadratic* fixed-cut boundary statistic, including an exact sign transition as the cut becomes imbalanced. The general edge determinantal law and classical Prüfer encoding are used as background, not claimed as new. Existing formulas might permit this covariance to be derived implicitly, so historical uniqueness remains unverified.

## Limitations

The uniform complete-graph spanning-tree model is essential for the symmetry used here. No analogous sign theorem is claimed for weighted spanning trees, noncomplete host graphs, or adaptively selected cuts. The result is a covariance identity, not stochastic-order monotonicity or a characterization of the full joint distribution. No independent priority or proof audit has been performed.

## References

1. Russell Lyons, *Determinantal probability measures*, arXiv:math/0204325 (first public version 2002-04-26), https://arxiv.org/abs/math/0204325.
2. Navin Goyal, Luis Rademacher, and Santosh Vempala, *Expanders via Random Spanning Trees*, arXiv:0807.1496 (first public version 2008-07-09), https://arxiv.org/abs/0807.1496.
3. David Aldous, *The Random Walk Construction of Uniform Spanning Trees and Uniform Labelled Trees*, SIAM Journal on Discrete Mathematics (1990), foundational random-tree context.
