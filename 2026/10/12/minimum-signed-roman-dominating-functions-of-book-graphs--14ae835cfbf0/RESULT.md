# Minimum signed Roman dominating functions of book graphs
## Finding
For every integer \(n\ge3\), let \(B_n=K_{1,n}\mathbin{\square}P_2\) be the \(n\)-page book graph. Write its spine vertices as \(u,v\), and for \(1\le i\le n\) write the page pair as \((a_i,b_i)\), so that the edges on page \(i\) are \(ua_i\), \(a_i b_i\), \(b_i v\), together with the common spine edge \(uv\).

A signed Roman dominating function is a map \(f:V(B_n)\to\{-1,1,2\}\) such that every closed-neighborhood sum is at least \(1\), and every vertex labeled \(-1\) has a neighbor labeled \(2\). Its weight is \(w(f)=\sum_{x\in V(B_n)}f(x)\).

Then
\[
\gamma_{sR}(B_n)=4.
\]
Every minimum function is exactly one of the following two types.

**Type I.** The spine labels are \(f(u)=f(v)=2\). Every page pair \((f(a_i),f(b_i))\) is either \((-1,1)\) or \((1,-1)\). If exactly \(k\) pages have the first type, then
\[
|n-2k|\le3.
\]

**Type II.** This occurs only when \(3\le n\le5\). Either \((f(u),f(v))=(1,2)\), exactly one page is labeled \((-1,2)\), and every other page is labeled \((1,-1)\); or, after reflecting the book, \((f(u),f(v))=(2,1)\), exactly one page is labeled \((2,-1)\), and every other page is labeled \((-1,1)\).

Hence the number \(M_n\) of minimum signed Roman dominating functions is
\[
M_n=\sum_{\substack{0\le k\le n\\ |n-2k|\le3}}\binom{n}{k}+2n\mathbf{1}_{3\le n\le5}.
\]
Thus \(M_3=14\), \(M_4=22\), and \(M_5=40\). For even \(n=2m\ge6\),
\[
M_n=\binom{2m}{m}+2\binom{2m}{m-1},
\]
and for odd \(n=2m+1\ge7\),
\[
M_n=2\binom{2m+1}{m}+2\binom{2m+1}{m-1}.
\]

## Assumptions and scope
The graph is the standard book graph \(B_n=K_{1,n}\mathbin{\square}P_2\), namely \(n\) four-cycles sharing the edge \(uv\). The theorem concerns exactly the minimum-weight signed Roman dominating functions for \(n\ge3\). It does not claim the full weight enumerator of all feasible functions.

Put
\[
\alpha=f(u),\qquad \beta=f(v),\qquad x_i=f(a_i),\qquad y_i=f(b_i),\qquad s_i=x_i+y_i.
\]
Then the closed-neighborhood inequalities are
\[
\alpha+\beta+\sum_i x_i\ge1,\qquad
\alpha+\beta+\sum_i y_i\ge1,
\]
and, page by page,
\[
\alpha+s_i\ge1,\qquad \beta+s_i\ge1.
\]
The Roman support condition is imposed separately: every occurrence of \(-1\) must have a neighboring \(2\).

## Proof
Let \(W=w(f)=\alpha+\beta+\sum_i s_i\). The page inequalities give
\[
s_i\ge1-\min\{\alpha,\beta\}.
\]
We first prove \(W\ge4\).

If \(\min\{\alpha,\beta\}=-1\), then every \(s_i\ge2\). Except for the formal boundary \(\alpha=\beta=-1\) and \(n=3\), this already gives \(W>4\). In that boundary case equality in the numerical bound would force every page to have \(s_i=2\), hence every page would be \((1,1)\); then neither spine vertex labeled \(-1\) would have a neighboring \(2\), so equality is impossible.

If \(\alpha=\beta=2\), then \(s_i\ge-1\). Because \(x_i,y_i\in\{-1,1,2\}\), the only page sum below \(0\) is \(-2\), coming from \((-1,-1)\), and that page violates \(2+s_i\ge1\). Hence every \(s_i\ge0\), so \(W\ge4\).

It remains to consider \(\min\{\alpha,\beta\}=1\). If \(\alpha=\beta=1\), a page with sum \(0\) would be either \((-1,1)\) or \((1,-1)\), but in either case its \(-1\)-vertex has no neighboring \(2\). Thus every \(s_i\ge1\), and \(W\ge n+2\ge5\). If, say, \((\alpha,\beta)=(1,2)\), then every \(s_i\ge0\). The only locally feasible page of sum \(0\) is \((1,-1)\): the alternative \((-1,1)\) leaves its \(-1\)-vertex without a neighboring \(2\). Therefore \(W\le3\) would force every page to be \((1,-1)\), making the closed-neighborhood sum at \(v\) equal to \(3-n<1\) for \(n\ge3\), a contradiction. The reflected case is identical. Hence \(W\ge4\) in all cases.

A weight-\(4\) function always exists. Set \(\alpha=\beta=2\), choose each page as \((-1,1)\) or \((1,-1)\), and let \(k\) be the number of pages of the first type. Then the two page-side sums are \(n-2k\) and \(2k-n\). The two spine inequalities are therefore equivalent to \(|n-2k|\le3\). Such a \(k\) exists for every \(n\ge3\), and the two spine vertices labeled \(2\) support every \(-1\). Thus \(\gamma_{sR}(B_n)=4\).

For the equality classification, the preceding lower-bound analysis leaves only \((\alpha,\beta)=(2,2)\), \((1,2)\), or \((2,1)\). In the first case, weight \(4\) forces every \(s_i=0\), so every page is exactly \((-1,1)\) or \((1,-1)\), and the spine inequalities give \(|n-2k|\le3\). This is Type I.

Now take \((\alpha,\beta)=(1,2)\). Weight \(4\) forces \(\sum_i s_i=1\). The only feasible sum-\(0\) page is \((1,-1)\), while the sum-\(1\) pages are \((-1,2)\) and \((2,-1)\). Hence exactly one page has sum \(1\). If it is \((2,-1)\), the \(v\)-side sum is \(-n\), so the closed-neighborhood condition at \(v\) fails for every \(n\ge3\). If the exceptional page is \((-1,2)\), the \(v\)-side sum is \(3-n\), and the condition at \(v\) is \(3+(3-n)\ge1\), equivalently \(n\le5\). This gives the first Type II family. Reflection gives the second family.

Counting Type I functions gives the binomial sum in the statement. Type II contributes exactly \(2n\) functions for \(3\le n\le5\). The parity formulas follow by listing the central binomial layers satisfying \(|n-2k|\le3\).

## Verification
The proof above is symbolic and covers every \(n\ge3\). The accompanying program `verify.py` is only a finite consistency check. It independently tests the signed Roman conditions on every labeling for \(n=3,4,5\), confirming both the minimum weight and the complete equality classification. It also performs a page-state dynamic enumeration for \(3\le n\le12\) and checks the minimum count against the closed formula.

The replayed output is:

`VERIFY_OK brute_n=3..5 labelings=597051 dp_n=3..12 minimum_functions_summed=5604`

## Relationship to prior work
Ahangar, Henning, Löwenstein, Zhao, and Samodivkin introduced and studied signed Roman domination, including general bounds and special bipartite cases. Their framework supplies the definition used here but does not state the book-graph classification.

Behtoei, Vatandoost, and Azizi Rajol Abad study signed Roman domination for joins and explicitly determine values for wheels, fans, friendship graphs, and joins of cycles. Their paper was first publicly posted as arXiv:1411.7208 on 2014-11-26 and lists primary MSC 05C69. The full text describes a fan as \(K_1\vee P_n\), a wheel as \(K_1\vee C_n\), and a friendship graph as \(K_1\vee(mK_2)\); the book graph \(K_{1,n}\mathbin{\square}P_2\) is a different Cartesian-product family and is not one of the families treated there.

A semantic search of published published-finding corpus findings returned the signed-Roman weight enumerator for complete multipartite graphs as the closest same-invariant item. For \(n\ge2\), the book graph is not complete multipartite, so that result does not imply the theorem here. Searches using the aliases “book graph”, “square book graph”, and \(K_{1,n}\mathbin{\square}P_2\) did not produce a same-object signed-Roman theorem. Previously published findings available for comparison include other book-graph invariants and a signed-Roman complete-multipartite enumerator, but no signed-Roman book-graph claim.

## Limitations
The theorem classifies only minimum-weight signed Roman dominating functions; it does not give the full weight distribution. The cases \(n=1,2\) are excluded and behave differently. Finite computation was used only to check small cases and the counting formula; it is not used as evidence for the infinite statement. Bibliographic searches cannot prove absolute nonexistence of an unindexed earlier result, so a residual literature risk remains, but no decisive overlapping source was found.

## References
1. H. Abdollahzadeh Ahangar, M. A. Henning, C. Löwenstein, Y. Zhao, and V. Samodivkin, “Signed Roman domination in graphs,” *Journal of Combinatorial Optimization* 27 (2014), 241–255. DOI: 10.1007/s10878-012-9500-0.
2. A. Behtoei, E. Vatandoost, and F. Azizi Rajol Abad, “Signed Roman Domination Number and Join of Graphs,” arXiv:1411.7208 (first posted 2014-11-26); *Journal of Algebraic Systems* 4 (2016), 65–77. DOI: 10.22044/jas.2016.729.
