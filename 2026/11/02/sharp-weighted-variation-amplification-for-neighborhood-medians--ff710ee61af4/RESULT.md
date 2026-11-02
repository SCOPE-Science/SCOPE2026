# Sharp weighted-variation amplification for neighborhood medians on complete bipartite graphs

## Finding

Let \(X=\{x_1,\ldots,x_p\}\) and \(Y=\{y_1,\ldots,y_q\}\) with integers \(p,q\ge1\), and give every edge of the complete bipartite graph \(K_{p,q}\) a strictly positive weight \(w_{ij}\). Let \(T\) replace each vertex's value with the lower median of the values at **its neighbors, excluding that vertex**. Then the following is the exact, attained *one-input* weighted edge-variation gain:

\[
K_w:=\sup_{J_w(f)>0}\frac{J_w(Tf)}{J_w(f)}=\frac{W}{c_w},\qquad W=\sum_{i=1}^p\sum_{j=1}^q w_{ij},
\]
where \(c_w\) is the minimum weighted cut value over bipartite binary labelings for which the strict-majority labels of the two vertex parts disagree. Writing the high-labeled sets as \(A\subseteq X\) and \(B\subseteq Y\), this means

\[
c_w=\min_{\substack{A\subseteq X,\,B\subseteq Y\\ (|A|>p/2)\ \mathrm{xor}\ (|B|>q/2)}}\left(\sum_{i\in A,j\notin B}w_{ij}+\sum_{i\notin A,j\in B}w_{ij}\right).
\]
In particular, for **unit edge weights**,

\[
K_{p,q}=\begin{cases}\dfrac{2pq}{pq+1},&p\text{ and }q\text{ both odd},\\[4pt]2,&\text{otherwise}.\end{cases}
\]
The sole variation-nonexpansive member with strictly positive edge weights is \(K_{1,1}\). For example, on \(K_{2,2}\), weights \(w_{i1}=R\ge1\) and \(w_{i2}=1\) for both \(i\) yield \(c_w=2\), \(W=2R+2\), and the exact factor \(R+1\), which is unbounded as \(R\to\infty\). All gains are attained by binary vertex signals. After the first step, the output is constant on each vertex part; further steps merely exchange those two constants, so the edge variation thereafter stays fixed.

## Assumptions and scope

Here \(f: X\cup Y\to\mathbb R\), \(J_w(f)=\sum_{i,j}w_{ij}|f(x_i)-f(y_j)|\), and the lower median of a list of length \(r\) means its \(\lceil r/2\rceil\)-th smallest entry. Thus when \(r\) is even, the **lower** of the two middle entries is selected. Every vertex uses its **open** neighborhood, not its value together with its neighbors. The operators and weights are finite, real, undirected, and strictly positive. No additional vertex or observation weights enter the definition. The ratio omits constant inputs, where \(J_w(f)=0\).

## Proof

Write \(u=\operatorname{med}_{\mathrm{low}}(f|_Y)\) and \(v=\operatorname{med}_{\mathrm{low}}(f|_X)\). Every vertex in \(X\) is updated to \(u\), and every vertex in \(Y\) to \(v\). Therefore \(J_w(Tf)=W|u-v|\). A second update exchanges the two constants, proving the iteration assertion.

For each real threshold \(t\), set \(A_t=\{x\in X:f(x)>t\}\) and \(B_t=\{y\in Y:f(y)>t\}\). For all thresholds except finitely many signal values, the lower median exceeds \(t\) exactly when *strictly more than half* of the input values exceed \(t\). In particular, the binary lower median is \(m_r(S)=\mathbf1_{|S|>r/2}\). The layer-cake identity \(|a-b|=\int_\mathbb R|\mathbf1_{a>t}-\mathbf1_{b>t}|\,dt\) gives the exact coarea formulas

\[
J_w(f)=\int_\mathbb R\operatorname{cut}_w(A_t,B_t)\,dt,\quad
J_w(Tf)=W\int_\mathbb R|m_p(A_t)-m_q(B_t)|\,dt.
\]
Whenever the integrand in the latter expression is \(1\), the cut in the former is at least \(c_w\) by definition; otherwise the output integrand is zero. Integrating yields \(J_w(Tf)\le (W/c_w)J_w(f)\). The minimum \(c_w\) is strictly positive, since a zero cut in a complete graph with positive edge weights forces the binary signal to be constant, contradicting opposing majority labels. Choose a minimizing cut \((A,B)\) and put \(f=\mathbf1_{A\cup B}\). Its input variation is \(c_w\), while its two updated part constants are opposite binary values; its output variation is \(W\). This proves attainability.

For unit weights, let \(a=|A|\), \(b=|B|\). The cut has size \(a(q-b)+(p-a)b\). In the orientation \(m_p(A)=1\), \(m_q(B)=0\), the minimum occurs at \(a=\lfloor p/2\rfloor+1\) and \(b=\lfloor q/2\rfloor\): increasing \(a\) cannot help since \(q-2b\ge0\), and at the minimum \(a\) the cut decreases as \(b\) increases. The opposite orientation similarly uses \(a=\lfloor p/2\rfloor\) and \(b=\lfloor q/2\rfloor+1\). Direct evaluation of these two endpoints gives \(c_w=(pq+1)/2\) if both sizes are odd and \(c_w=pq/2\) otherwise; this proves the parity formula even when a part has size one.

For \(q\ge2\), take \(A=X\) and let \(B\subseteq Y\) be nonempty with \(|B|\le\lfloor q/2\rfloor\). Then the two part majorities oppose, but all weights on edges incident to \(B\) remain uncut, so the cut has weight strictly less than \(W\); hence \(K_w>1\). When \(q=1\) and \(p\ge2\), reverse the roles of the parts. For \(p=q=1\), the filter merely exchanges endpoint values and \(K_w=1\). Finally, on \(K_{2,2}\) with the stated weights, the strict-majority-disagreeing binary patterns have minimum cut \(2\) for \(R\ge1\); thus \(K_w=R+1\).

## Verification

The self-contained Python 3 script `verification/check_medians.py` checks exhaustive binary signals and binary cut minima for every part-size pair through \(7\) in the unit-weight case, exhaustive binary tests for positive integer-weight samples through size \(5\), exact integer real-signal inequalities, two-step dynamics, and sharp witnesses. It uses only Python's standard library and exact integer/rational arithmetic. Run `python3 verification/check_medians.py`. The recorded successful comparison totals were 64,516 unweighted binary inequalities; 26,908 weighted binary inequalities; 12,250 real-signal inequalities; 12,250 two-step dynamics checks; and 224 sharpness witnesses. These finite checks are not a proof for all sizes and all real weights; that role is served by the coarea proof above.

## Relationship to prior work

Arias-Castro and Donoho analyze statistical edge preservation and risk of spatial median filtering; those results do not calculate the sharp weighted edge-variation ratio for a graph neighborhood median. Sandryhaila and Moura develop general graph-signal filtering primarily through linear graph-shift operators. Benjamini and collaborators, and the earlier theorem of Goles and Olivos, address period-two behavior of majority/threshold dynamics: the **periodicity consequence is not claimed novel**. Prior unweighted majority-median tree results cover certain star cases of a different closed-neighborhood tie convention; they do not yield the positive-weighted formula on cyclic complete bipartite graphs. The principal new assertion here is the attained weighted cut constant and its exact parity consequences. A related 2016 conference contribution on center-weighted graph medians could be inspected only at the abstract level; implicit prior coverage of part of the bound cannot be excluded.

## Limitations

The result concerns a *one-input* quotient \(J_w(Tf)/J_w(f)\), not the two-input difference quotient \(J_w(Tf-Tg)/J_w(f-g)\). The filter uses lower medians of open neighborhoods; switching to upper medians or adding the central sample changes the hypothesis. Weighted edges enter only the **variation measure**, not the order statistic. The graph is complete bipartite, and the positive weighted cut minimum is a finite characterization, not a claimed efficient closed form for arbitrary weights. Although prior-work comparison found no covering exact formula, exhaustive novelty is not established, and the related 2016 graph-median article was unavailable in full.

## References

1. E. Arias-Castro and D. L. Donoho, *Does median filtering truly preserve edges better than linear filtering?*, arXiv:math/0612422v1, posted 2006-12-14, https://arxiv.org/abs/math/0612422.
2. A. Sandryhaila and J. M. F. Moura, *Discrete Signal Processing on Graphs*, arXiv:1210.4752v1, posted 2012-10-17, https://arxiv.org/abs/1210.4752.
3. I. Benjamini et al., *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1, posted 2014-05-11, https://arxiv.org/abs/1405.2486.
4. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, https://doi.org/10.1016/0012-365X(80)90121-1.
5. S. Segarra et al., *Center-weighted median graph filters*, GlobalSIP 2016, https://doi.org/10.1109/GlobalSIP.2016.7905859 (abstract consulted; full text inaccessible).
