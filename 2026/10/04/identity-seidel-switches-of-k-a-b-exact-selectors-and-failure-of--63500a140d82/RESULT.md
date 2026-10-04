# Identity Seidel switches of \(K_{a,b}\): exact selectors and failure of subgroup closure
## Finding
Let \(G=K_{a,b}\) with bipartition \(A\cup B\), where \(a,b\ge1\). For a selector \(S\subseteq V(G)\), put \(x=|S\cap A|\) and \(y=|S\cap B|\). Then the Seidel-switched graph is exactly a complete bipartite graph with part sizes \(b+x-y\) and \(a-x+y\). Hence \(S\) is an identity Seidel switch if and only if \(x-y\in\{0,a-b\}\). The number of identity-selector subsets is \(\binom{a+b}{a}\) when \(a=b\), and \(2\binom{a+b}{a}\) when \(a\ne b\). In particular, identity Seidel switches are not in general closed under symmetric difference: in \(K_{2,3}\), if \(b_1\) lies in the part of size three and \(a_1\) lies in the part of size two, then \(\{b_1\}\) and \(\{a_1,b_1\}\) are identity Seidel switches, whereas their symmetric difference \(\{a_1\}\) is not. Therefore the assertion in arXiv:2601.04530v1 that all identity Seidel switches of a fixed graph form a \(2\)-subgroup is false under Definition 4.1 of that preprint.

## Assumptions and scope
All graphs are finite, simple, and undirected. Seidel switching by a selector \(S\subseteq V(G)\) toggles adjacency exactly across the cut \((S,V(G)\setminus S)\). An identity Seidel switch is a selector whose switched graph is isomorphic to the original graph, following Definition 4.1 of arXiv:2601.04530v1. The theorem concerns all complete bipartite graphs \(K_{a,b}\) with \(a,b\ge1\); no assumption of balance or connectedness after switching is made.

## Proof
Let \(A,B\) be the bipartition of \(K_{a,b}\), and put \(x=|S\cap A|\), \(y=|S\cap B|\). Define
\[
A'=(S\cap A)\cup(B\setminus S),\qquad B'=(S\cap B)\cup(A\setminus S).
\]
Pairs with one endpoint in \(A'\) and one in \(B'\) fall into four types. A pair from \((S\cap A,S\cap B)\) or from \((A\setminus S,B\setminus S)\) was an edge and is not switched; a pair from \((S\cap A,A\setminus S)\) or from \((B\setminus S,S\cap B)\) was a non-edge and is switched. Thus every such cross-pair is an edge after switching. Conversely, pairs lying within \(A'\) or within \(B'\) are either original same-part non-edges left unchanged or original cross-part edges toggled off. Hence the switched graph is exactly
\[
K_{|A'|,|B'|}=K_{b+x-y,\,a-x+y}.
\]
Write \(d=x-y\). Since complete bipartite graphs are determined up to isomorphism by the unordered pair of part sizes, the switched graph is isomorphic to \(K_{a,b}\) exactly when
\[
\{b+d,a-d\}=\{a,b\}.
\]
There are exactly two algebraic possibilities: \(d=0\) or \(d=a-b\). Therefore \(S\) is an identity Seidel switch exactly when \(x-y\in\{0,a-b\}\).

For \(x-y=0\), the number of selectors is
\[
\sum_k\binom ak\binom bk=\binom{a+b}a
\]
by Vandermonde's identity. For \(x-y=a-b\), writing \(a-x=b-y=k\) gives the same count. These two selector families coincide exactly when \(a=b\), proving the stated enumeration.

Finally take \(K_{2,3}\) with \(a_1\in A\) and \(b_1\in B\). For \(S=\{b_1\}\), one has \(x-y=-1=a-b\), so \(S\) is an identity switch. For \(T=\{a_1,b_1\}\), one has \(x-y=0\), so \(T\) is an identity switch. But \(S\triangle T=\{a_1\}\) has \(x-y=1\), which is neither \(0\) nor \(-1\), so it is not an identity switch. Thus the identity-switch family need not be closed under symmetric difference.

## Verification
The accompanying `verify.py` constructs each \(K_{a,b}\), performs Seidel switching directly on adjacency sets for every selector, independently recognizes complete bipartite outputs by graph traversal and edge checks, and compares the observed identity condition with the theorem. It exhausts all \(1\le a,b\le6\) with \(a+b\le10\), checking 7,684 selectors, and separately verifies the explicit \(K_{2,3}\) closure counterexample. The finalized replay output is:

`ALL CHECKS PASSED; parameter_cases=33; selectors=7684; iss_selectors=2790; a,b_range=1..6 with a+b<=10`

The finite computation is a stress test only; the theorem and the closure counterexample are proved analytically above.

## Relationship to prior work
Gervacio's 2026 preprint introduces identity Seidel switches and states in its abstract, introduction, and conclusion that the identity switches of a fixed graph form a \(2\)-subgroup under symmetric difference. The same paper gives two ingredients consistent with the present counterexample: vertices in the larger part of \(K_{n,n+1}\) are vertex identity switches (Example 4.3), and every edge of \(K_{m,n}\) is an edge identity switch (Example 5.4). The exact selector classification above shows that these valid examples do not combine to give subgroup closure.

Classical switching literature already records that, on a fixed vertex set, the switching class of the empty graph is precisely the class of complete bipartite graphs. That broader orbit statement does not identify which selectors return a specified \(K_{a,b}\), does not give the selector count, and does not imply subgroup closure. Targeted searches for the exact identity-selector criterion, its binomial enumeration, and a correction or counterexample to the 2026 subgroup assertion found no covering result.

## Limitations
The theorem concerns complete bipartite graphs only. It does not classify identity switches in arbitrary graphs, nor does it propose a replacement algebraic structure for the identity-switch family. The originality conclusion is limited by the possibility that an older switching source contains an equivalent selector-level count under different terminology; no such source was located in the checked literature. The correction applies specifically to the subgroup assertion under Definition 4.1 of arXiv:2601.04530v1.

## References
1. S. V. Gervacio, *On identity Seidel switches*, arXiv:2601.04530v1, submitted 8 January 2026. MSC 2020: 05C50, 05C60.
2. A. Ehrenfeucht, J. Hage, T. Harju, and G. Rozenberg, *Pancyclicity in Switching Classes*, Information Processing Letters 73 (2000), 153--156, DOI:10.1016/S0020-0190(00)00020-X.
3. J. Hage, *Structural Aspects of Switching Classes*, and related switching-class literature recording that the switching class of the empty graph consists of all complete bipartite graphs on the fixed vertex set.
