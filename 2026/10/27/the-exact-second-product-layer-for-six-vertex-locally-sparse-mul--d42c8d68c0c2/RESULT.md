# The exact second product layer for six-vertex locally sparse multigraphs

## Finding

For every integer \(a\ge1\), among all nonnegative-integer edge-weighted \(K_6\) in which every five-vertex set has total edge weight at most \(10a+4\), the largest product strictly below the maximum is
\[
 a^{10}(a+1)^4(a+2).
\]
Up to vertex relabeling, it is attained uniquely by one edge of weight \(a+2\), a disjoint \(4\)-cycle whose four edges have weight \(a+1\), and the remaining ten edges of weight \(a\). The maximum product is \(a^9(a+1)^6\), so the ratio of the second product to the maximum is exactly \(1-1/(a+1)^2\).

## Assumptions and scope

An edge-weighted \(K_6\) assigns a nonnegative integer \(w(e)\) to each of its fifteen edges. It is admissible when every five-vertex set \(X\) satisfies \(\sum_{e\in E(K_6[X])}w(e)\le10a+4\). Its product is \(P(G)=\prod_{e\in E(K_6)}w(e)\). The parameter \(a\) is any integer at least one. “Second product” means the largest product strictly smaller than the maximum, excluding every maximum-product graph.

## Proof

Write \(S=\sum_e w(e)\), and for a vertex \(v\) write \(d_w(v)=\sum_{e\ni v}w(e)\). The five-set obtained by deleting \(v\) has weight \(S-d_w(v)\le10a+4\). Summing this inequality over the six vertices counts every edge weight exactly four times, so
\[
4S\le6(10a+4),\qquad S\le15a+6.
\]

If \(S\le15a+5\), increasing some weights until their sum is \(15a+5\) cannot decrease the product. The integer arithmetic-geometric mean bound at that sum is \(a^{10}(a+1)^5\), which is strictly smaller than \(a^{10}(a+1)^4(a+2)\). It remains to consider \(S=15a+6\).

For fifteen nonnegative integers with this sum, the unique balanced multiset is nine copies of \(a\) and six copies of \(a+1\), with product \(a^9(a+1)^6\). To bound the largest product below it, consider a product-maximizing unbalanced multiset of the same sum. It has positive entries. If two entries \(x<y-1\) occur, replacing them by \(x+1\) and \(y-1\) preserves the sum and strictly increases the product, since
\[
(x+1)(y-1)-xy=y-x-1>0.
\]
Thus, in a largest unbalanced multiset, every such smoothing must lead to the balanced multiset. The only possible predecessor multisets are obtained from the balanced one by replacing the indicated pair:

- replace two copies of \(a\) by \(a-1,a+1\), giving \((a-1)a^7(a+1)^7\);
- replace two copies of \(a+1\) by \(a,a+2\), giving \(a^{10}(a+1)^4(a+2)\);
- replace one copy each of \(a,a+1\) by \(a-1,a+2\), giving \((a-1)a^8(a+1)^5(a+2)\).

The second product is strictly larger than the first and third: the first-to-second ratio is \((a-1)(a+1)^3/[a^3(a+2)]<1\), and the third-to-second ratio is \((a-1)(a+1)/a^2<1\). Hence every nonmaximum product with sum \(15a+6\) is at most \(a^{10}(a+1)^4(a+2)\). The earlier bound for smaller sums proves the same upper bound for every nonmaximum admissible graph.

It remains to attain the bound and identify equality. Give one edge weight \(a+2\), give the four edges of a \(4\)-cycle on the other four vertices weight \(a+1\), and give every other edge weight \(a\). The total weight is \(15a+6\), and every vertex is incident to total excess weight \(2\) above the baseline \(a\). Therefore every five-set has weight \(15a+6-(5a+2)=10a+4\), and the product is \(a^{10}(a+1)^4(a+2)\).

Finally, any graph attaining this second product must have that unique edge-weight multiset and total weight \(15a+6\). Since the sum of the six five-set weights is \(4S=6(10a+4)\), all six constraints are tight. Each vertex must therefore have excess degree exactly \(2\). The edge of excess weight \(2\) already supplies the full excess degree at its two endpoints, so the four excess-weight-one edges lie on the remaining four vertices and give each degree two. A simple graph on four vertices with four edges and every degree two is a \(4\)-cycle. This proves uniqueness up to relabeling.

## Verification

The argument uses exact integer inequalities only. The key checks are the fourfold edge count in the sum over deleted-vertex constraints, the integer smoothing identity, the two strict product comparisons, and the excess-degree characterization of equality. The proposed weighted graph directly attains every five-set bound. No computational enumeration is used or needed.

## Relationship to prior work

Day, Falgas-Ravry, and Treglown encode this constraint value as \(q=\Sigma_{2,2}(a,5)=10a+4\) in their conjectured maximum-product construction. Gu and Wang explicitly identify that equivalence and prove the maximum product for six vertices, exhibiting a six-cycle of edges of weight \(a+1\) as a maximizer. The result here concerns the next distinct product below that maximum and its unique weighted structure; neither paper states this finite second-product layer. Falgas-Ravry’s later theorem concerns a different asymptotic parameter family.

## Limitations

The result is specific to six vertices, five-vertex constraints, and the bound \(10a+4\). It does not classify the second product for larger vertex sets or other constraint values, and it makes no claim about a general stability theorem for locally sparse multigraphs.

## References

1. R. Gu and S. Wang, “On extremal problems on multigraphs,” arXiv:2301.10430, first posted 2023-01-25; see the definition of \((n,s,q)\)-graphs and the six-vertex case in the proof of Theorem 1.
2. A. N. Day, V. Falgas-Ravry, and A. Treglown, “Extremal problems for multigraphs,” arXiv:2011.01626, first posted 2020-11-03; see Construction 3.1 and Conjecture 3.2.
3. V. Falgas-Ravry, “On an extremal problem for locally sparse multigraphs,” arXiv:2101.03056, first posted 2021-01-08; see Theorem 1.6 and its parameter range.
