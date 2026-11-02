# Sharp Nash-welfare price of EF1 with one exceptional good

## Finding

For every integer \(n\ge2\), every integer \(L\ge n-1\), and every real \(H\ge1\), consider a complete division of exactly one good of common value \(H\) and \(L\) distinct goods of common value \(1\), between \(n\) agents having identical additive valuations. Write \(\operatorname{NSW}(A)\) for the geometric mean of their realized utilities and \(\operatorname{NSW}^*\) for the maximum over all complete allocations.

Define \(k=n-1\). For \(r\ge0\), let \(r=kq+j\), where \(q=\lfloor r/k\rfloor\) and \(0\le j<k\), and put
\[
 B_k(r)=q^{k-j}(q+1)^j,\qquad F(t)=(H+t)B_k(L-t),\quad 0\le t\le L.
\]
The convention \(0^0=1\) is used; a zero utility factor makes the product zero. Define the two integers
\[
 a=\max\!\left\{0,\left\lceil\frac{L-(n-1)(\lfloor H\rfloor+1)}n\right\rceil\right\},\qquad b=\left\lfloor\frac Ln\right\rfloor.
\]
Then every EF1 allocation has the exceptional-good recipient holding some \(s\in\{a,a+1,\ldots,b\}\) unit goods, with the other \(n-1\) unit-only bundles balanced to within one good. Conversely, every such choice gives an EF1 allocation. Consequently, the *exact* worst EF1 utility product, optimum utility product, and EF1-to-optimum Nash-welfare ratio are
\[
 P_{\mathrm{worst\ EF1}}=\min\{F(a),F(b)\},\quad
 P^*=\max_{0\le t\le L}F(t),\quad
 \min_{A\ \mathrm{EF1}}\frac{\operatorname{NSW}(A)}{\operatorname{NSW}^*}
 =\left(\frac{\min\{F(a),F(b)\}}{\max_{0\le t\le L}F(t)}\right)^{1/n}.
\]
Moreover, **every EF1 allocation** in this entire family satisfies the sharp uniform estimate
\[
 \boxed{\displaystyle \frac{\operatorname{NSW}(A)}{\operatorname{NSW}^*}\ge
 \left(\frac{n-1}{n}\right)^{(n-1)/n}.}
\]
For each fixed \(n\), no larger constant works uniformly over \(L\) and \(H\).

## Assumptions and scope

All \(L+1\) goods are indivisible, distinct, and allocated exactly once; all agents share the same positive additive valuation. The lower bound \(L\ge n-1\) ensures a strictly positive optimum and a full EF1 division with positive utility for every agent. No monetary transfers, fractional allocation, or heterogeneous valuations are considered. EF1 means that for every ordered pair of distinct agents, removing some *at most one* good from the second bundle eliminates the first agent's envy. The special item's value may be noninteger, and \(\lfloor H\rfloor\) in the exact endpoints is essential.

## Proof

**1. Normal form and the EF1 interval.** Let the exceptional-good owner possess \(s\) unit goods. Write \(\ell_1,\ldots,\ell_k\) for unit-good counts of the other agents, so \(\sum_i\ell_i=L-s\). Comparing any two unit-only agents, EF1 forces \(|\ell_i-\ell_j|\le1\). Hence all their counts equal \(q=\lfloor(L-s)/k\rfloor\) or \(q+1\), proving their utility product is \(B_k(L-s)\). Each unit-only agent must be able to remove the exceptional good from its owner's bundle; as \(H\ge1\), removing that good achieves the smallest remaining value \(s\), so EF1 in this direction requires \(\ell_i\ge s\) for every \(i\). With balanced counts this is exactly \(\lfloor(L-s)/k\rfloor\ge s\), equivalently \(ns\le L\), or \(s\le b\).

In the reverse direction, the exceptional-good owner has value \(H+s\). Removing a unit good from one of the unit-only bundles leaves \(\ell_i-1\) (and removing none is no easier), so EF1 requires \(\max_i\ell_i\le H+s+1\). The left side is integer, while \(s\) is integer. Therefore the inequality is equivalent to
\[
 \left\lceil\frac{L-s}{k}\right\rceil\le s+\lfloor H\rfloor+1,
 \quad\text{or}\quad L\le ns+k(\lfloor H\rfloor+1).
\]
Together with \(s\ge0\), this says \(s\ge a\). Conversely, balancing the unit-only bundles at every integer \(s\in[a,b]\) meets all three types of comparisons. The interval is nonempty because \(s=\lfloor L/n\rfloor\) always works (the lighter bundles receive at least as many unit goods as the special owner, and at most one extra).

**2. Exact products and endpoint minima.** For a fixed exceptional-owner count \(t\), balancing the other \(k\) counts maximizes their product: whenever two counts differ by at least two, moving one good from larger to smaller strictly raises their product. Thus the maximal unrestricted product at that \(t\) is \(F(t)\); maximizing over all \(t=0,\ldots,L\) gives \(P^*\). Within EF1 the unit-only counts are already forced balanced, so the product at every admissible \(s\) is exactly \(F(s)\).

On the positive range, \(B_k(r+1)/B_k(r)=(q+1)/q\), with \(q=\lfloor r/k\rfloor\ge1\), and these ratios are nonincreasing as \(r\) grows. Hence \(B_k\) is log-concave, including the zero-product boundary; reversing its argument preserves this property. The sequence \(H+t\) is also log-concave. Therefore \(F(t)=(H+t)B_k(L-t)\) is log-concave, and its minimum over the integer interval \([a,b]\) occurs at an endpoint: \(\min_{a\le s\le b}F(s)=\min\{F(a),F(b)\}\). The unrestricted maximum is also an exact finite one-variable expression.

**3. Sharp price bound.** Fix any EF1 allocation with special-owner count \(s\). Its other counts satisfy \(\ell_i\ge s\). Compare any unrestricted count \(t\).

If \(t\ge s\), set \(M=\lceil(L-s)/k\rceil\). Provided the next product is positive,
\[
 \frac{F(s+1)}{F(s)}=\frac{H+s+1}{H+s}\frac{M-1}{M}\le1,
\]
because EF1 gives \(M\le H+s+1\). If the next product vanishes the conclusion is immediate. Log-concavity then implies \(F(t)\le F(s)\) for all \(t\ge s\).

If \(t<s\), necessarily \(s\ge1\). Starting with the balanced light counts \(\ell_i\) at \(s\), redistribute the \(s-t\) unit goods removed from the exceptional owner to the light agents, always incrementing a smallest current count. This produces balanced counts \(\ell_i+d_i\), with each \(d_i\ge0\) and \(\sum_i d_i=s-t\); their product is \(B_k(L-t)\). Therefore, by \(H+t\le H+s\), \(\ell_i\ge s\), and the arithmetic-geometric mean inequality,
\[
 \frac{F(t)}{F(s)}=\frac{H+t}{H+s}\prod_{i=1}^{k}\left(1+\frac{d_i}{\ell_i}\right)
 \le\prod_{i=1}^k\left(1+\frac{d_i}{s}\right)
 \le\left(1+\frac{s-t}{ks}\right)^k
 \le\left(\frac{k+1}{k}\right)^k.
\]
Combining the two cases proves \(P^*/F(s)\le(n/(n-1))^{n-1}\), hence the claimed Nash-welfare bound.

**4. Sharpness.** Fix \(n\), set \(L=n(n-1)\), and consider EF1 allocation with the exceptional-good owner holding \(n-1\) unit goods and each other agent holding \(n-1\) unit goods. Every count is \(n-1\), so the normal-form inequalities verify EF1. Its utility product is \((H+n-1)(n-1)^{n-1}\). The unrestricted optimum, for all sufficiently large \(H\), gives the exceptional good alone to its owner and exactly \(n\) unit goods to every other agent; its product is \(Hn^{n-1}\). (Indeed any positive special-owner count sacrifices at least one unit from the balanced light product and is eventually worse as \(H\to\infty\).) The ratio of geometric means tends to \(((n-1)/n)^{(n-1)/n}\), proving optimality of the constant.

## Verification

The standalone Python script `verify_one_spike.py` enumerates every integer composition of the \(L\) unit goods among \(n\) agents, with the exceptional good fixed at the first agent. Using exact rational arithmetic it independently tests EF1 from all ordered agent comparisons, calculates the actual minimum EF1 product and unrestricted maximum product, and compares them against the interval and product formulas. It checks all \(228\) parameter combinations with \(n=2,3,4,5\), \(n-1\le L\le11\), and \(H\in\{1,3/2,2,7/2,10,1000\}\). It also tests the universal \(n\)-dependent lower bound. The verification program checks a finite sample; the proof above establishes the claims for all prescribed \(n,L,H\).

## Relationship to prior work

Yang et al. (2026), arXiv:2609.03846, study the same general EF1-constrained Nash-welfare objective with identical additive valuations. Their uniform-goods case gives optimality for all EF1 allocations, and their more general improved bound requires each item to be sufficiently small relative to the mean. Here one exceptional good may be arbitrarily large; we give an exact EF1 feasibility/product classification and a sharp \(n\)-specific guarantee for that family. Their general lower bound \(e^{-1/e}\) is acknowledged rather than reproved.

Barman, Krishnamurthy, and Vaish (2017), arXiv:1707.04731, provide a general EF1-to-NSW approximation guarantee under identical additive valuations. Their 2018 greedy-NSW work, arXiv:1801.09046, concerns constructing efficient allocations; the present assertion instead covers *every* EF1 allocation and identifies the worst admissible one. These general results do not state the exact one-exceptional-good phase interval or sharp \(n\)-dependent constant. Some earlier unindexed specialization could exist.

## Limitations

The classification assumes precisely one exceptional good and all other goods identical and positive; it does not imply the same bound for several exceptional goods, heterogeneous valuations, weighted agents, or online prefix EF1. The worst-NSW constant is an infimum attained in the limit \(H\to\infty\), not generally at a fixed finite \(H\). The finite verification does not replace the general algebraic proof. Literature priority is not independently certified; unindexed earlier equivalent statements remain possible. No independent external mathematical audit has been performed.

## References

1. Z.-S. Yang et al., *EF1-Constrained Nash Social Welfare with Identical Additive Valuations: Complexity, Guarantees, and Experiments*, first publicly posted September 3, 2026. https://arxiv.org/abs/2609.03846
2. S. Barman, S. K. Krishnamurthy, R. Vaish, *Finding Fair and Efficient Allocations*, first publicly posted July 15, 2017. https://arxiv.org/abs/1707.04731
3. S. Barman, S. K. Krishnamurthy, R. Vaish, *Greedy Algorithms for Maximizing Nash Social Welfare*, first publicly posted January 27, 2018. https://arxiv.org/abs/1801.09046
