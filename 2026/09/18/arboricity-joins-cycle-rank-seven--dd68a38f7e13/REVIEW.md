# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof was checked against the Nash--Williams characterization in classical-arboricity form.

For nonempty \(A\subseteq V(G)\), \(B\subseteq V(H)\), with \(s=|A|\), \(t=|B|\), the edge count is
\[
|E((G*H)[A\cup B])|=st+s+t-2+c,
\]
where
\[
c=(|E(G[A])|-s+1)+(|E(H[B])|-t+1).
\]
Each summand is bounded above by the cycle rank of its ambient factor, so \(c\le\beta(G)+\beta(H)\). If \(K\) is the full-set ceiling and \(q=K-1\), the required Nash--Williams inequality is exactly
\[
c\le R_q(s,t),\qquad
R_q(s,t)=q^2-q+1-(q-s)(q-t).
\]

For \(q\ge3\), the proof covers separately \(s,t\ge q\), the mixed regime \(s<q\le t\), and \(s,t<q\). The mixed regime is controlled by the hypothesis \(\beta\le q^2-q+1\); the small-small regime follows from the simple-graph bounds
\[
c_G(A)\le (s-1)(s-2)/2,\qquad
c_H(B)\le (t-1)(t-2)/2
\]
and the identity
\[
2R_q(s,t)-[(s-1)(s-2)+(t-1)(t-2)]
=(s+t-1)(2q-s-t+2).
\]
One-sided subsets are not omitted: the bound
\[
e(U)\le\min\{\binom r2,r-1+\beta\}
\]
gives \(e(U)\le(q+1)(r-1)\) after splitting at \(r=2q+2\).

The exceptional \(q=2\) regime was checked directly. Here the stronger constant \(7\) works because
\[
\min\{7,(s-1)(s-2)/2\}\le s+1=R_2(s,1),
\]
while subsets meeting both factors in at least two vertices are controlled by the full-set inequality. The \(q=1\) and \(q=0\) cases follow from the strong restrictions imposed by the full-set ceiling itself.

The sharpness construction was recomputed directly. Its total cycle rank is \(8\); the full join has \(21\) edges on \(8\) vertices, giving ceiling \(3\), while an induced \(7\)-vertex subgraph has \(19\) edges, forcing arboricity \(4\). The ambient \(K_8\) gives the matching upper bound \(4\).

## Originality

The directly relevant 2026 preprint of Kuanyshov--Yeginbay was inspected in full-text HTML. Its Section 3.2 and Theorem 23 give general lower and upper bounds for graph joins, followed by examples including complete bipartite graphs, fan graphs, \(P_4*\overline K_3\), and wheels. It does not state an exact theorem for factors of bounded cycle rank or a criterion expressed through the full-set ceiling.

Literature searches used the equivalent terminology "arboricity of graph joins", "arboricity of the join", "sum of graphs", "cone graph arboricity", and the parameters "cycle rank", "cyclomatic number", "circuit rank", and "corank". These searches found the new Kuanyshov--Yeginbay paper, standard Nash--Williams references, and unrelated join invariants, but no theorem implying the criterion above or the sharp cycle-rank-eight obstruction.

The reference list of the directly relevant preprint contains the standard arboricity source and graph/topology references, but no earlier exact join-arboricity theorem. This is additional evidence, not a proof of novelty.

No specific inaccessible paper was identified as especially likely to contain the same theorem. The main residual originality risk is unindexed or very recent parallel work, because the motivating join-arboricity preprint was submitted on 17 September 2026.

Originality is therefore assessed as PASS **to the best of our knowledge**, not as certainty.

## Value

The result converts newly established general join bounds into an exact formula on a natural structural regime measured by cycle-space dimension. Unlike a fixed small-rank corollary alone, the main criterion allows the admissible cycle rank to grow quadratically with the predicted arboricity. The clean corollary at total cycle rank at most seven is best possible as a uniform bound, with a concrete obstruction already at eight.

## Limitations

- The criterion is sufficient, not necessary.
- The quadratic threshold for each fixed \(K\ge4\) is not claimed optimal.
- No claim is made that the full vertex set maximizes fractional arboricity.
- Originality remains to the best of our knowledge, with residual risk from very recent or unindexed parallel work.
- Independent audit has not been performed.
