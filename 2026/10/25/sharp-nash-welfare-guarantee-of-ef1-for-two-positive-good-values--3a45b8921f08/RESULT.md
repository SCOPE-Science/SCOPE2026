# Sharp Nash-welfare guarantee of EF1 for two positive good values

## Finding
For any integer \(n\ge2\), any finite set of \(m\ge n\) indivisible goods, and any **identical additive** valuation assigning each good either \(a\) or \(2a\), where \(a>0\), every complete EF1 allocation \(A\) obeys
\[
\frac{\operatorname{NSW}(A)}{\operatorname{NSW}(A^*)}\ge
\left(\frac34\right)^{\lfloor n/2\rfloor/n}.
\]
Here \(A^*\) maximizes Nash social welfare over **all** complete allocations, with \(\operatorname{NSW}\) the geometric mean of the agents' utilities. For every \(n\ge2\) the bound is attained, so its dependence on the agent count is sharp. There is no restriction on the number or relative frequencies of the two item types beyond the stated inventory requirement.

## Assumptions and scope
The valuation \(v\) is common to all \(n\) agents and additive: \(v(S)=\sum_{g\in S}v(g)\), with \(v(g)\in\{a,2a\}\). A complete allocation partitions all goods into \(n\) labeled bundles. EF1 means that, for all agents \(i,j\), either \(v(A_i)\ge v(A_j)\), or some good \(g\in A_j\) satisfies \(v(A_i)\ge v(A_j\setminus\{g\})\). The unrestricted optimum \(A^*\) uses precisely the same goods and agents but need not be EF1. Positive-valued goods, \(m\ge n\), and identical valuations are essential to the argument. The result is a sharp **worst-case guarantee for every EF1 allocation**, not an algorithmic complexity statement.

## Proof
First scale by \(a\), so each good has integer value \(1\) or \(2\). Every EF1 allocation has nonempty bundles. Indeed, if an agent received no good, then because \(m\ge n\) at least one other agent would have two or more positive-valued goods; removing just one would leave positive utility, contradicting EF1 for the empty agent.

Write \(x_i=v(A_i)/a\) and \(S=\sum_i x_i\). Thus every \(x_i\) is a positive integer. Taking an agent of minimum bundle value and one of maximum bundle value, EF1 requires
\[
\max_i x_i-\min_i x_i\le 2,
\]
since removing any single good decreases utility by at most \(2\).

Define \(B(S,n)\) as the largest product of \(n\) **nonnegative integer** coordinates with sum \(S\). By pairwise smoothing, this maximum is achieved exactly when all coordinates differ by at most \(1\): if \(u\le v-2\), replacing \((u,v)\) with \((u+1,v-1)\) changes their product by \(v-u-1>0\). Every feasible allocation yields such an integer vector, hence the unrestricted optimal allocation satisfies
\[
\prod_{i=1}^n\frac{v(A_i^*)}{a}\le B(S,n).
\]

If the minimum and maximum of \((x_i)\) differ by at most \(1\), its product is already \(B(S,n)\). Otherwise, let the minimum be \(L\ge1\) and the maximum be \(L+2\). Replace *one coordinate of each extreme* by two coordinates equal to \(L+1\). This operation is performed on the **numerical load vector only**, not asserted to be an implementable item transfer. It preserves the sum and multiplies the product by
\[
\frac{(L+1)^2}{L(L+2)}
=1+\frac1{L(L+2)}\le\frac43.
\]
Because the original coordinates are confined to \(L,L+1,L+2\), repeating this replacement exhausts at least one of the two extreme values after at most \(\lfloor n/2\rfloor\) steps. The final vector differs by at most one, so its product is \(B(S,n)\). Therefore
\[
 B(S,n)\le\left(\frac43\right)^{\lfloor n/2\rfloor}\prod_{i=1}^n x_i.
\]
Combining with the unrestricted-optimum bound and taking \(n\)-th roots establishes the claimed Nash-social-welfare inequality.

To prove sharpness, put \(q=\lfloor n/2\rfloor\) and \(r=n-2q\in\{0,1\}\). Construct \(2q\) goods of value \(a\) and \(q+r\) goods of value \(2a\), for a total of \(3q+r\ge n\) goods. Give \(q\) agents one \(a\)-good each, \(q\) agents a bundle consisting of one \(a\)-good and one \(2a\)-good, and (if \(r=1\)) the remaining agent one \(2a\)-good. The resulting utility vector is \((a,\ldots,a,3a,\ldots,3a,2a\text{ if }r=1)\). This allocation is EF1: a lower-valued agent comparing with a \(3a\)-bundle can remove the \(2a\)-good, leaving value \(a\), while all other comparisons are easier. Its product is \(a^{2q+r}3^q2^r\).

Another allocation gives utility exactly \(2a\) to everyone: use the \(q+r\) high-valued goods as singleton bundles, and combine the \(2q\) low-valued goods into \(q\) pairs. Its product is \((2a)^n\), globally maximal by arithmetic–geometric mean because total value is \(2an\). The EF1-to-optimum geometric-mean ratio of the first allocation equals \((3/4)^{q/n}\). Hence the bound cannot be increased for any fixed \(n\).

## Verification
The standalone `CHECK.py` enumerates all allocations up to indistinguishability of equal-valued goods for \(2\le n\le5\) and \(n\le m\le10\), with all feasible counts of the two item types. It checks EF1 directly from the count-vector definition, compares each allocation's Nash product with the true maximum over all such allocations, and verifies the claimed bound using exact rational arithmetic. In this finite domain it checked 6,497 EF1 allocation count vectors without violation; equality examples occur for every tested agent count. The construction and universal bound above are proved symbolically and do not rely on finite enumeration. Run with Python 3: `python3 CHECK.py`.

## Relationship to prior work
Yang, Chen, Kuan, Wu, Lin, and Chen, *EF1-Constrained Nash Social Welfare with Identical Additive Valuations: Complexity, Guarantees, and Experiments* (first publicly posted 2026-09-03, arXiv:2609.03846), prove exact optimality under **uniform** goods and an explicit general lower bound when all items are sufficiently small relative to the mean load. Their general EF1 spread bound motivates this question. The contribution here is the **sharp finite-agent, inventory-independent bound for the natural two-positive-value alphabet**, together with equality examples for every agent count; it does not claim the basic spread property or general EF1 welfare lower bounds as new. Barman, Krishnamurthy, and Vaish's earlier *Finding Fair and Efficient Allocations* supplies broader fair-allocation and Nash-welfare context but not this exact two-positive-value ratio in the inspected material.

## Limitations
This result does not cover zero-valued goods, goods taking arbitrary positive values, heterogeneous agents, fewer goods than agents, or allocation constraints. The proof is an unconditional mathematical argument; a mathematically equivalent result outside inspected, indexed literature remains a priority risk. The finite enumeration is not a general computational proof.

## References
1. Zih-Sian Yang, Yi-Hao Chen, Yu-Te Kuan, Cheng-Jui Wu, Chuang-Chieh Lin, Po-An Chen (2026), *EF1-Constrained Nash Social Welfare with Identical Additive Valuations: Complexity, Guarantees, and Experiments*, arXiv:2609.03846, https://arxiv.org/abs/2609.03846 (first posted 2026-09-03).
2. Siddharth Barman, Sanath Kumar Krishnamurthy, Rohit Vaish (2018), *Finding Fair and Efficient Allocations*, https://rohitvaish.in/Publications/%5BBarman%2B%5D%20Finding%20Fair%20and%20Efficient%20Allocations.pdf.
