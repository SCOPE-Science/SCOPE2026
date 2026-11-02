# A universal isolate–induced-motif covariance threshold in fixed-edge random graphs

## Finding
Let \(G\sim G(n,m)\), the uniformly selected labeled simple graph with \(n\) vertices and exactly \(m\) edges. Let \(I\) count isolated vertices and \(X_H\) count vertex subsets whose **induced** graph is isomorphic to a specified graph \(H\). Assume \(H\) has \(h\ge3\) vertices, \(e\ge1\) edges, no isolated vertices, and at least one nonedge. Put \(t=\binom h2\), \(r=t-e\ge1\), \(N=\binom n2\), and \(B=\binom{n-1}2\). For all integers \(n>h\) and \(e\le m\le\min(B,N-r)\),
\[
\frac{\operatorname{Cov}(I,X_H)}{\mathbb E I\,\mathbb E X_H}
=\mathcal R_{n,h,e}(m)-1,
\qquad
\mathcal R_{n,h,e}(m)=\frac{n-h}{n}\frac{(N)_{\underline t}}{(B)_{\underline t}}\frac{(B-m)_{\underline r}}{(N-m)_{\underline r}}.
\]
The ratio \(\mathcal R_{n,h,e}(m)\) is nonnegative and strictly decreasing in the integer \(m\) wherever it is positive, and becomes zero if \(B-m<r\). Consequently **the covariance changes sign at most once, from positive to negative, as the fixed edge count increases**. This finite sign law depends only on \((n,h,e,m)\), not the topology of \(H\) within fixed \((h,e)\).

Fix \(h,e\), let \(n\to\infty\) and \(m/\binom n2\to p\in(0,1)\). Then
\[
 n\,\frac{\operatorname{Cov}(I,X_H)}{\mathbb E I\,\mathbb E X_H}
\longrightarrow
\frac{2e-h-h(h-2)p}{1-p}.
\]
Whenever \(2e>h\), the limiting sign therefore changes at the universal density
\[
 p_*(h,e)=\frac{2e-h}{h(h-2)}\in(0,1):
\]
for every fixed \(p<p_*\) the covariance is eventually positive, and for every fixed \(p>p_*\) eventually negative. No limiting sign at equality is asserted. If \(2e\le h\), the covariance is eventually negative at each fixed \(p>0\).

For the induced open wedge \(H=P_3\), this becomes a sharp **all-finite-order threshold**. For every \(n\ge4\) and every integer \(2\le m\le\binom{n-1}2\), define
\[
 M_n=\frac{(n-1)(n^3-3n^2+6n+8)}{2(3n^2-3n-4)}.
\]
Then \(\operatorname{Cov}(I,X_{P_3})\) is strictly positive for \(m<M_n\), zero exactly when \(m=M_n\) is integral, and strictly negative for \(m>M_n\). In all cases \(2<M_n<\binom{n-1}2\). Moreover \(M_n/\binom n2\to1/3\).

## Assumptions and scope
The falling factorial is \((a)_{\underline k}=a(a-1)\cdots(a-k+1)\) for integer \(k\ge0\), with \((a)_{\underline0}=1\) and zero when \(a\) is a nonnegative integer smaller than \(k\). The model \(G(n,m)\) has \(\binom Nm\) equally likely graphs. A copy of \(H\) means an unordered \(h\)-vertex subset inducing an isomorphic graph, counted once per subset; write \(a_H=|\operatorname{Aut}(H)|\). The hypotheses \(n>h\), \(e\le m\le\min(B,N-r)\), and no isolated vertices in \(H\) ensure both expectations in the normalization are strictly positive and allow an isolated vertex to occur only outside a copy of \(H\). The clique case \(r=0\) is excluded from the strict monotonicity theorem, although the displayed conditional-count derivation also applies to it without a sign transition. The theorem concerns covariances, not independence or conditional independence.

## Proof
For any prescribed set of \(e\) present and \(r\) absent edges, where all \(t=e+r\) tested edges are distinct, uniform fixed-size sampling gives probability \((m)_{\underline e}(N-m)_{\underline r}/(N)_{\underline t}\). Therefore
\[
\mathbb E X_H=\frac{(n)_{\underline h}}{a_H}\frac{(m)_{\underline e}(N-m)_{\underline r}}{(N)_{\underline t}}.
\]
For a distinguished vertex \(v\), the event that \(v\) is isolated has probability \(\binom Bm/\binom Nm\); conditioned on that event, all \(m\) edges are uniformly chosen from the \(B\) pairs not incident with \(v\). Because \(H\) has no isolated vertices, no induced copy of \(H\) contains \(v\). Hence
\[
\mathbb E[X_H\mid v\text{ isolated}]
=\frac{(n-1)_{\underline h}}{a_H}
\frac{(m)_{\underline e}(B-m)_{\underline r}}{(B)_{\underline t}}.
\]
Summing \(\operatorname{Cov}(\mathbf1_{\{v\text{ isolated}\}},X_H)\) over \(v\) yields
\[
\operatorname{Cov}(I,X_H)=\mathbb E I\bigl(\mathbb E[X_H\mid v\text{ isolated}]-\mathbb E X_H\bigr),
\qquad \mathbb E I=n\binom Bm/\binom Nm,
\]
and division proves the exact formula. All divisions are by positive quantities in the stated range.

For \(0\le m\le B-r\), write
\[
\frac{(B-m)_{\underline r}}{(N-m)_{\underline r}}
=\prod_{j=0}^{r-1}\frac{B-m-j}{N-m-j}.
\]
Every factor is positive (apart from an allowed zero endpoint) and strictly decreasing as a function of \(m\), because \(B<N\). Thus the product is strictly decreasing while positive. For \(m>B-r\), the numerator is zero, completing the one-transition conclusion.

For fixed \(h,e\) and \(m/N\to p\in(0,1)\), expansion of the three terms in the ratio gives
\[
\frac{n-h}{n}=1-\frac hn,
\quad \frac{(N)_{\underline t}}{(B)_{\underline t}}=1+\frac{2t}{n}+O(n^{-2}),
\quad \frac{(B-m)_{\underline r}}{(N-m)_{\underline r}}=1-\frac{2r}{n(1-p)}+o(n^{-1}).
\]
Their product equals \(1+n^{-1}[2t-h-2r/(1-p)]+o(n^{-1})\). Use \(r=t-e\) and \(2t-h=h(h-2)\) to obtain the asserted limit. Since \(r\ge1\) and \(2e>h\), the threshold is strictly between zero and one; strict sign conclusions follow from the nonzero limiting coefficient.

For \(P_3\), substitute \(h=3\), \(e=2\), \(t=3\), \(r=1\) into \(\mathcal R\). Solving \(\mathcal R_{n,3,2}(m)=1\) for real \(m\) yields exactly \(M_n\). The denominator \(3n^2-3n-4\) is positive for \(n\ge4\), and
\[
M_n-2=\frac{(n^2-3n-2)(n^2-n-4)}{2(3n^2-3n-4)}>0,
\quad
B-M_n=\frac{n(n-1)(n^2-3n-2)}{3n^2-3n-4}>0.
\]
Strict monotonicity gives the sign classification. The leading terms of \(M_n\) and \(N\) are \(n^2/6\) and \(n^2/2\), respectively, proving the density limit.

## Verification
An independent standard-library Python enumerator `verify_induced_motifs.py` constructs every labeled simple graph on four, five and six vertices, groups graphs by exact edge count, directly counts isolated vertices and induced wedges, and checks all three exact first and mixed moments against the formulas. The same enumerator separately checks induced four-cycles and induced four-vertex paths on all five-vertex graphs. It completes \(168\) exact rational moment/covariance assertions over \(34{,}880\) enumerated labeled graphs across these test families. For replay: `python3 verify_induced_motifs.py`. Finite enumeration is corroboration, not the proof of the theorem for unbounded \(n\); the proof above is symbolic.

## Relationship to prior work
Sah and Sawhney [1] develop central and local limit theory for (possibly induced) subgraph counts in both \(G(n,m)\) and \(G(n,p)\). The original complete public preprint, particularly its introduction and Section 4.2, addresses univariate local limits, exceptional densities for those limits, and graph-factor expansions. The present result is instead an exact mixed covariance with isolated vertices, including a topology-invariant sign rule and a different explicitly computed density threshold. The density \(p_*\) here is not identified with their exceptional-density set.

The usual hypergeometric fixed-edge sampling identity is used openly and is not claimed as new. Analogous noninduced-motif covariance expressions are simpler and can be independent of \(m\) even in their sign; the required absent edges in the induced case cause the new monotone dependence on \(m\). In the independent-edge model \(G(n,p)\), the same no-isolated-vertex condition in \(H\) gives \(\operatorname{Cov}(I,X_H)=-(h/n)\mathbb E I\,\mathbb E X_H<0\), so the positive fixed-edge regime is genuinely model-specific.

## Limitations
Historical priority is not settled: a general occupancy calculation or unpublished covariance table could imply this result without using the same terminology. The inspected primary reference gives stronger results for some univariate distributions but does not state this mixed-covariance sign classification. The formula excludes motifs with isolated vertices and requires a nonempty induced-motif probability. No quantitative central limit theorem, nonlinear conditional dependence statement, or finite-dimensional joint limit is proved. The limit coefficient vanishes exactly at \(p=p_*\); the behavior for density sequences approaching that boundary requires the exact formula rather than a sign claim from the first-order expansion. No independent audit is claimed.

## References
[1] A. Sah and M. Sawhney, *Local limit theorems for subgraph counts*, arXiv:2006.11369v1 (public June 19, 2020), https://arxiv.org/html/2006.11369v1; later *Journal of the London Mathematical Society* **105** (2022), 950–1011, https://doi.org/10.1112/jlms.12523.
