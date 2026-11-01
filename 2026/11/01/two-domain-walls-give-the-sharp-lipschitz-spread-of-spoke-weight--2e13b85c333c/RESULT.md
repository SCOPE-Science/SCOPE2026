# Two domain walls give the sharp Lipschitz spread of spoke-weighted wheels

## Finding

Let \(W_n(t)\), with integer \(n\ge4\) and \(0<t\le1\), be the metric on the \(n+1\) vertices of a wheel: the edges of its rim cycle have length \(1\), and each edge from the hub to a rim vertex has length \(t\). Distances are shortest-path distances. Give every vertex mass \(1/(n+1)\). Write \(N=n+1\) and \(\eta_n=0\) for even \(n\), \(\eta_n=1\) for odd \(n\). Then the exact sharp variance of a real one-Lipschitz observable is

\[
\operatorname{spr}(W_n(t))=
\max_{\operatorname{Lip}(f)\le1}\frac1N\sum_{v}|f(v)-\bar f|^2
=\begin{cases}
\displaystyle \frac{nt^2}{N}-\frac{\eta_n t^2}{N^2},&0<t\le\frac12,\\[6pt]
\displaystyle \frac{(n-2)t^2+2(1-t)^2}{N}-\frac{\eta_n(3t-2)^2}{N^2},&\frac12<t\le1.
\end{cases}
\]

There is a complete equality classification. Normalize the hub value to \(0\). When \(0<t\le1/2\), **all** maximizers assign \(+t\) and \(-t\) to the rim in arbitrary cyclic order, with their multiplicities differing by \(0\) when \(n\) is even, and by \(1\) when \(n\) is odd. When \(1/2<t\le1\), every maximizer has a single nonempty contiguous block of \(+t\), a single nonempty contiguous block of \(-t\), and exactly two intervening rim vertices. Those intervening values have magnitude \(1-t\). For even \(n\), the extreme blocks have equal size \((n-2)/2\) and the intervening values are \(+(1-t)\) and \(-(1-t)\). For odd \(n\), the extreme blocks have sizes \((n-1)/2\) and \((n-3)/2\), and both intervening values have sign opposite to the larger extreme block. At \(t=1\) the intervening vertices are both \(0\), so their signs are immaterial. In every case arbitrary translations are also allowed.

The sharp value is continuous at \(t=1/2\), but its left derivative minus its right derivative is exactly

\[
\operatorname{spr}'_-(W_n(1/2))-\operatorname{spr}'_+(W_n(1/2))
=\begin{cases}\displaystyle \frac4{n+1},&n\text{ even},\\[5pt]
\displaystyle\frac{4n}{(n+1)^2},&n\text{ odd}.
\end{cases}
\]

For fixed \(1/2<t\le1\), the cost of the two domain walls is explicit:
\[
\operatorname{spr}(W_n(t))
=t^2-\frac{t^2+2(2t-1)}{n+1}
-\frac{\eta_n(3t-2)^2}{(n+1)^2}.
\]
In particular the spread converges to \(t^2\) as the rim grows, with a first-order loss reflecting precisely two interfaces.

## Assumptions and scope

All vertices, including the hub, have equal probability mass. Edges carry shortest-path lengths, rather than electrical conductances. Because a rim edge has length \(1\), the direct and hub-mediated routes tie at \(t=1/2\); this is the natural geometric threshold. The metric's one-Lipschitz inequalities are equivalent to edge inequalities. The sharp value and equality statements hold for every integer \(n\ge4\) and every real \(0<t\le1\), including both parameter endpoints.

## Proof

**1. Strict convexity and vertices.** Translate so that the hub has value zero and denote rim values by \(x_1,\ldots,x_n\), with indices modulo \(n\). The feasible polytope is
\[
P_t=\bigl\{x\in\mathbb R^n:|x_i|\le t,\ |x_i-x_{i+1}|\le1\ \text{for every }i\bigr\}.
\]
The objective is
\[
V(x)=\frac1N\sum_i x_i^2-\frac1{N^2}\Bigl(\sum_i x_i\Bigr)^2.
\]
Its Hessian is positive definite: its eigenvalues are \(2/N\) on the orthogonal complement of the all-ones vector and \(2/N^2\) in the all-ones direction. Therefore **every** maximizer is a vertex of \(P_t\).

For \(t\le1/2\), the rim constraints are redundant and \(P_t=[-t,t]^n\). Its vertices assign signs to all rim positions. The objective is largest precisely when the signed sum has least absolute value: \(0\) for even \(n\), and \(t\) for odd \(n\). This proves the first branch and all its equality cases.

**2. Four allowed levels in the open weighted regime.** Assume \(1/2<t<1\), and put \(a=1-t\) and \(d=2t-1=t^2-a^2>0\). Form a graph from all tight rim inequalities \(|x_i-x_{i+1}|=1\). Every connected component must contain a vertex with \(|x_i|=t\); otherwise its entire component can be shifted slightly without violating any inequality, contradicting extremality. Along a tight rim path all values differ by integers. Starting from \(+t\), the only values in \([-t,t]\) obtainable by integer shifts are \(+t\) and \(-a\). Starting from \(-t\), they are \(-t\) and \(+a\). Thus every polytope vertex uses only the four levels \(\{-t,-a,+a,+t\}\). If only \(+t\) or only \(-t\) is present, the allowed levels reduce to \(\{+t,-a\}\) or its sign-reversal. If both signs of extreme level occur, a cyclic rim must contain at least two smaller-magnitude bridging vertices, since \(+t\) and \(-t\) cannot be adjacent.

**3. Exclude vertices with only one extreme sign.** Suppose the rim has \(p\) copies of \(+t\) and \(q=n-p\) copies of \(-a\). The pairwise-variance identity, including the hub at \(0\), gives
\[
N^2V=pq+pt^2+qa^2.
\]
This concave quadratic in the integer \(p\) is maximized at \(p=n/2\) when \(n=2h\), and at \(p=(n+1)/2\) when \(n=2h+1\) (the restriction \(1\le p\le n\) does not enlarge the maximum). The two-domain-wall candidate from Step 4 strictly exceeds these maxima. The difference in numerators \(N^2V\) is, respectively,
\[
(2t-1)(2h^2t+h^2-3h-2),\qquad n=2h\ge4,
\]
\[
(2t-1)(2h^2t+h^2+2ht-2h-4t),\qquad n=2h+1\ge5.
\]
Both expressions are strictly positive on \(1/2<t<1\). For the even expression, the bracket at \(t=1/2\) equals \((2h+1)(h-2)\) and its slope is positive. For the odd expression, its value at \(t=1/2\) equals \(2h^2-h-2>0\) and its slope \(2h^2+2h-4\) is positive.

**4. Two interfaces and their parity imbalance.** Let \(r\) be the number of vertices taking the small levels \(\pm a\), and let \(S=\sum_i x_i\). When both extreme signs occur, \(r\ge2\) and
\[
N^2V=N\bigl(nt^2-rd\bigr)-S^2.
\]
For even \(n\), this is bounded above by \(N[(n-2)t^2+2a^2]\). Equality requires precisely two bridges and \(S=0\), forcing equally many \(+t\) and \(-t\) and opposite bridge values. Such a cyclic assignment is feasible, establishing the claimed even formula and all its optimizers.

For odd \(n\), first consider \(r=2\). The extreme signed count is odd, and the two bridge signs have even signed count. Consequently \(|S|\ge|t-2a|=|3t-2|\); equality is achieved exactly by extreme block counts differing by one and both bridges opposing the majority, up to global sign. This gives the odd candidate.

To rule out **every** \(r\ge3\) for odd \(n\), it suffices to prove
\[
N(r-2)d+S^2>(3t-2)^2.
\]
If \(Nd\ge1\), this follows immediately from \(|3t-2|<1\). Otherwise write \(t=1/2+\varepsilon\) with \(0<\varepsilon<1/(2N)\). Every rim level equals a sign times either \(1/2+\varepsilon\) or \(1/2-\varepsilon\); hence \(S=k/2+\varepsilon\ell\), where \(k\) is odd and \(|\ell|\le n\). If \(|k|\ge3\), then \(|S|\ge3/2-n\varepsilon>1\), so the inequality follows. If \(|k|=1\), let \(u\) be the signed count of the \(r\) small-level vertices. Then \(\ell=k-2u\), so \(|\ell|\le2r+1\). If \((2r+1)\varepsilon\ge1/2\), the first term on the left exceeds \(N(r-2)/(2r+1)\ge N/7>1/4\), whereas \((3t-2)^2<1/4\). Otherwise \(|S|\ge1/2-(2r+1)\varepsilon\); since \(|3t-2|=1/2-3\varepsilon\),
\[
(3t-2)^2-S^2\le2(r-1)\varepsilon
<2N(r-2)\varepsilon=N(r-2)d.
\]
This proves the strict exclusion of all additional bridges, and hence the odd formula and equality classification.

**5. Boundary and derivative.** At \(t=1\), the value follows from the interior formula by a quantitative continuity comparison: for \(0<t<1\), \(tP_1\subseteq P_t\subseteq P_1\), and the variance is quadratic, so \(t^2\operatorname{spr}(W_n(1))\le\operatorname{spr}(W_n(t))\le\operatorname{spr}(W_n(1))\). To classify maximizers directly, the tight-component argument yields levels \(\{-1,0,+1\}\). Vertices having both \(\pm1\) require at least two zeros. Three or more zeros strictly lose against the two-zero construction (even case by the square sum; odd case because the one-vertex loss exceeds the possible unit squared-mean gain). Single-sign configurations are strictly suboptimal by the expressions in Step 3 evaluated at \(t=1\). Thus the stated optimizer patterns persist. The two displayed branches agree at \(t=1/2\); differentiating the two polynomial expressions gives the exact one-sided derivative jump. Rewriting the second branch yields the finite-size domain-wall cost.

## Verification

The standalone `verify_weighted_wheel_spread.py` uses only Python's exact rational arithmetic. It checks all feasible four-level rim configurations for \(n=4,\ldots,8\) at nine rational spoke lengths; the four-level reduction is proved in Step 2. It also compares all possible signed extremal counts in the additional-interface bound for \(4\le n\le30\) across nine rational parameters, and checks the one-sided derivative and parity identities for \(4\le n\le100\). The finite tests independently detect mistakes in formulas and equality assertions, but the universal results rely on the proof above, not the enumeration.

## Relationship to prior work

Alon, Boppana and Spencer introduced the sharp finite-metric Lipschitz variance (spread) and proved the general integer-extremizer structure for unweighted graph metrics [1]. Addario-Berry, Janson and McDiarmid studied spread, including random edge lengths [2]. Yancey studied extremal graph Lipschitz observables and cycles [3]. These results provide context and related extreme-point machinery but do not state the deterministic one-parameter weighted-wheel formula or its two-interface classification in the relevant sections inspected. The weighted result is not obtained from the unweighted integrality theorem because its optimal bridge levels are generally nonintegral. The possible existence of an equivalent treatment under other terminology remains an originality limitation.

## Limitations

The result assumes equal vertex masses and uniform rim-edge lengths. It treats \(n\ge4\) and \(0<t\le1\); it does not extend automatically to the four-vertex wheel with a triangular rim (\(n=3\)), heavier spokes \(t>1\), heterogeneous spokes, or higher centered moments. The literature comparison is not proof of global priority, and the analytical proof has not undergone independent peer review.

## References

[1] N. Alon, R. Boppana, J. Spencer, *An Asymptotic Isoperimetric Inequality*, Geometric and Functional Analysis **8** (1998), 411–436. DOI: 10.1007/s000390050062. Author-hosted full text: https://web.math.princeton.edu/~nalon/PDFS/iso7.pdf.

[2] L. Addario-Berry, S. Janson, C. McDiarmid, *On the Spread of Random Graphs*, arXiv:0902.1156 (first public posting 2009-02-06), later Combinatorics, Probability and Computing **23** (2014), 477–504. https://arxiv.org/pdf/0902.1156.

[3] M. P. Yancey, *Probabilistic and Geometrical Applications to Graph Theory*, arXiv:1705.09725 (first posting 2017-05-26), especially the variance-extremizer and cycle sections. https://arxiv.org/pdf/1705.09725.
