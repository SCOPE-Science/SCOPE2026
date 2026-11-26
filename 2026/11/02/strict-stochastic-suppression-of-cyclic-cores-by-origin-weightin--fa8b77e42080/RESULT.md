# Strict stochastic suppression of cyclic cores by origin weighting in random mappings

## Finding

Let \(F:[n]\to[n]\) be a map on \(n\ge2\) labeled vertices, allowing loops. Let \(C(F)\) count the vertices lying on directed cycles and let \(L(F)\) count vertices of indegree zero (origins). For finite \(t\ge1\), give each map probability proportional to \(t^{L(F)}\) and write \(C_{n,t}\) for its cyclic-vertex count. For every \(1\le s<t<\infty\) and every \(2\le k\le n\),

\[
\Pr(C_{n,t}\ge k)<\Pr(C_{n,s}\ge k).
\]

The comparison follows from a positive mixture. With \(a_{n,r}=\binom nr(1-r/n)^n\), \(W_n(t)=\sum_{r=0}^{n-1}a_{n,r}(t-1)^r\), and \(h_{m,k}=(m)_{\underline k}/m^k\) if \(k\le m\) and zero otherwise, one has
\[
\Pr(C_{n,t}\ge k)=\frac{1}{W_n(t)}\sum_{r=0}^{n-1}a_{n,r}(t-1)^r h_{n-r,k},\qquad 1\le k\le n.
\]
At \(t=1\) the sole term is \(r=0\).

## Assumptions and scope

The state space is all \(n^n\) functions, with arrows \(v\to F(v)\). A cyclic vertex is counted once, irrespective of cycle length. This is an all-size, cross-weight comparison on the indicated range, not a statement about the number of cycles, the law below weight one, or the always-satisfied tail at \(k=1\). Uniform-law covariance, its asymptotics and conditional origin-count laws are not claimed as contributions here.

## Proof

**Positive mixture.** Under the uniform map law, the event that a prescribed set \(S\) of \(r\le n-1\) labels consists of origins has probability \(((n-r)/n)^n\): each of the \(n\) independent arrows must avoid \(S\). Conditional on this event, the restriction to the complement is a uniform self-map there and contains every cycle. In particular for any test function \(g\), summing over \(S\) gives
\[
\mathbb E\left[\binom{L(F)}r g(C(F))\right]=a_{n,r}\,\mathbb E[g(C_{n-r,1})].
\]
The case of all \(n\) labels being origins is impossible. Expand \(t^{L(F)}=(1+(t-1))^{L(F)}\) and divide the resulting weighted expectation by \(\mathbb E[t^{L(F)}]=W_n(t)>0\). This expresses the tilted law as the mixture of the uniform laws at sizes \(n-r\), with weights \(a_{n,r}(t-1)^r/W_n(t)\).

**Uniform tail.** In an \(m\)-label map with exactly \(j\) cyclic vertices, choose their labels, permute them, and attach a directed forest rooted at the chosen vertices. For \(1\le j<m\), the rooted-forest count is \(j m^{m-j-1}\): the relevant directed matrix-tree minor on the nonroot labels is \(mI-J\), with eigenvalues \(j,m,\ldots,m\), where \(J\) is the all-ones matrix of size \(m-j\). At \(j=m\) the forest count is one. Thus
\[
\Pr(C_{m,1}=j)=\frac{j(m)_{\underline j}}{m^{j+1}}=h_{m,j}-h_{m,j+1},
\]
which gives the stated tail by telescoping.

**Strict ordering.** For each \(k\ge2\), \(h_{m,k}\) is zero for \(m<k\), positive at \(m=k\), and strictly increasing thereafter by the product \(\prod_{i=0}^{k-1}(1-i/m)\). Thus \(H(r)=h_{n-r,k}\) is nonincreasing, with \(H(0)>H(1)\). For \(1<s<t\), every index has positive mixture weight at \(s\), and the ratio of the new weight to the old weight is a strictly increasing function \(R(r)\) proportional to \(((t-1)/(s-1))^r\). The difference of the two tail probabilities is the covariance of \(H\) and \(R\) under the \(s\)-weights, since \(\mathbb E_s R=1\). The independent-copy covariance formula has nonpositive summands \((H(r)-H(r'))(R(r)-R(r'))/2\), and the pair \(0,1\) contributes strictly negatively. For \(s=1\), the initial weight is concentrated at \(r=0\); the distribution at \(t>1\) assigns positive weight to \(r=1\) and averages a nonincreasing \(H\). This proves strictness including that endpoint.

## Verification

The accompanying, unchanged `verify.py` enumerates all maps for \(2\le n\le7\) and checks the weighted tails and the positive mixture at tested rational weights. As a separate small exact diagnostic, enumerating the \(4^4\) maps gives total weight \(680\) at \(t=2\) and weighted tails \((57,21,3)/85\) at \(k=2,3,4\), respectively, against \((3/4,3/8,3/32)\) at \(t=1\). These finite checks complement the proof and do not establish its universal quantifiers.

## Relationship to prior work and limitations

Arney and Bender studied origin weighting and constraints and asymptotic cyclic-element statistics; their §7 equation (7.1) marks cycles, not cyclic vertices. The broad cyclic-vertex distribution in Theorem 1 of Hansen and Jaworski (2006) already applies at each fixed weight: use the exchangeable indegree law proportional to \((n!/\prod_i d_i!)t^{\#\{i:d_i=0\}}\) on vectors with sum \(n\). What is compared here is the strict order across weights at every finite size and threshold, using the positive mixture in uniform mapping sizes. The existence of a fixed-weight distribution formula does not supply that monotonicity. This proof gives no unconditional historical-priority statement, no extension to weights less than one, and no comparison for a conditioned number of components.

## References

- J. Arney and E. A. Bender, “Random mappings with constraints on coalescence and number of origins,” *Pacific Journal of Mathematics* 103 (1982), 269–294, https://doi.org/10.2140/pjm.1982.103.269.
- J. Hansen and J. Jaworski, “A new random mapping model,” https://arxiv.org/abs/math/0603529, §§2–3.
