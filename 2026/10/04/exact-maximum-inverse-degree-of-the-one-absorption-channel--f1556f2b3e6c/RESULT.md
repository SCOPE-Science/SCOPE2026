# Exact maximum inverse degree of the one-absorption channel
## Finding
For every integer \(q\ge 2\) and \(n\ge 2\), put \(\Sigma_q=\{0,1,\ldots,q-1\}\) and \(a\oplus b=\min\{a+b,q-1\}\). For a received word \(y\in\Sigma_q^{n-1}\), define
\[
P_{q,n}(y)=\{x\in\Sigma_q^n: y\text{ is obtained from }x\text{ by exactly one absorption}\},
\]
where an absorption either replaces adjacent \(a,b\) by \(a\oplus b\) or removes the terminal symbol, as in Ye--Elishco. Then
\[
\max_{y\in\Sigma_q^{n-1}} |P_{q,n}(y)|=q+(n-1)\binom{q}{2}.
\]
The constant saturated word \(y=(q-1)^{n-1}\) attains this maximum.

## Assumptions and scope
The claim concerns exactly one absorption and the finite alphabet \(\Sigma_q\) with the saturated-sum operation above. The terminal-loss case is included because it is part of the source channel definition. The quantity is an inverse-ball size: it counts possible transmitted parents of one fixed received word. It is not the forward absorption-ball size \(|B^{ab}_1(x)|\), and it does not determine an optimal correcting-code cardinality by itself.

## Proof
Let \(m=n-1\). Write \(I(y)\) for the ordinary one-symbol insertion sphere of \(y\): all length-\(m+1\) words obtained by inserting one alphabet symbol in one of the \(m+1\) gaps. A canonical first-difference description gives
\[
|I(y)|=q+m(q-1).
\]
Indeed, if an inserted word differs from \(y\) before its final position, let \(j\in\{1,\ldots,m\}\) be the first differing coordinate. The inserted symbol at \(j\) can be any of the \(q-1\) symbols different from \(y_j\), and this canonical pair determines the supersequence uniquely. If there is no difference among the first \(m\) coordinates, the word is \(ya\) for one of \(q\) terminal symbols \(a\).

Consider now a parent \(x\in P_{q,n}(y)\). If the terminal symbol is lost, then \(x\in I(y)\). Otherwise some symbol \(c=y_i\) arose by absorbing a pair \((a,b)\) with \(a\oplus b=c\). If \(a=c\) or \(b=c\), then \(x\) is again an ordinary one-symbol insertion supersequence of \(y\). The only remaining parents are genuine splits, for which \(a\ne c\) and \(b\ne c\).

Let \(g_q(c)\) be the number of genuine ordered splits of \(c\). If \(c<q-1\), then \(a+b=c\), and requiring both \(a\ne c\) and \(b\ne c\) leaves
\[
g_q(c)=\max\{c-1,0\}.
\]
For \(c=q-1\), genuine splits have \(0\le a,b\le q-2\) and \(a+b\ge q-1\), hence
\[
g_q(q-1)=\binom{q-1}{2}.
\]
Thus \(g_q(c)\le\binom{q-1}{2}\) for every \(c\). Counting insertion parents once and then bounding genuine splits position by position gives
\[
|P_{q,n}(y)|
\le q+m(q-1)+m\binom{q-1}{2}
=q+m\binom{q}{2}.
\]

For \(y=(q-1)^m\), every word in \(I(y)\) is a parent: an inserted symbol can be absorbed into an adjacent saturated symbol, while a terminal insertion can be removed by the terminal-loss rule. In addition, at each of the \(m\) positions every genuine split \((a,b)\) with \(a,b\ne q-1\) and \(a+b\ge q-1\) is a parent. These genuine-split words have two adjacent nonsaturated symbols, whereas an insertion into \((q-1)^m\) has at most one nonsaturated symbol, so the two families are disjoint. Genuine splits at different positions or with different ordered pairs are also distinct. Therefore
\[
|P_{q,n}((q-1)^m)|=q+m(q-1)+m\binom{q-1}{2}=q+m\binom{q}{2},
\]
which matches the upper bound.

## Verification
The bundled `verify.py` implements the source channel forward from every source word and, independently, generates parents by inverse pair expansion. It checks equality of the two parent sets for all received words in a finite multi-parameter test range, verifies the insertion-plus-genuine-split decomposition, and confirms the closed-form maximum and the saturated-word witness. These finite checks corroborate the proof; the universal statement rests on the counting argument above.

## Relationship to prior work
Ye and Elishco introduced the absorption channel and its one-error balls in arXiv:2302.09842v1. Their conclusion explicitly identifies estimating the *forward* one-absorption ball \(|B^{ab}_1(x)|\) as a difficult open ingredient for sharper code-size upper bounds; the present invariant instead fixes a received word and counts its possible parents. Their Section V uses a hypergraph only after restricting to zero-deletion correction and does not state the inverse-degree formula above. A 2024 follow-up by Nguyen, Cai, Quek, and Immink improves code constructions and redundancy bounds; the accessible abstract does not state an inverse-ball or received-word-degree result.

Targeted searches were made for inverse balls, preimages, list size, received-word degree, incidence-hypergraph degree, and the displayed formula, both in the published-results database and the public literature. No inspected source stated or implied the exact maximum \(q+(n-1)\binom{q}{2}\). This is evidence of noncoverage, not a proof that no differently phrased or unindexed result exists.

## Limitations
The result concerns one absorption only. It gives a worst-case inverse degree, not the full distribution of inverse degrees, not a forward-ball formula, and not an optimal code-size theorem. The 2024 follow-up was available only through bibliographic/abstract material under the bounded access available, so an unadvertised inverse-degree statement in inaccessible full text remains a residual originality risk.

## References
1. Z. Ye and O. Elishco, “Codes Over Absorption Channels,” arXiv:2302.09842v1, first public 20 February 2023; later IEEE Transactions on Information Theory, DOI 10.1109/TIT.2023.3346882.
2. T. T. Nguyen, K. Cai, T. Q. S. Quek, and K. A. Schouhamer Immink, “Efficient Constructions of Non-Binary Codes over Absorption Channels,” ISIT 2024, DOI 10.1109/ISIT57864.2024.10619179.
