# A wedge-only conditional-variance law for triangles under partial graph revelation

## Finding

Let \(G\sim G(n,p)\), fix a set \(S\subseteq[n]\) of size \(h\), and observe **all** edges and nonedges of the induced graph \(G[S]=H\). Write \(N=n-h\), \(e=e(H)\), \(t=t(H)\) for its number of triangles, and
\[
w=w(H)=\sum_{v\in S}\binom{d_H(v)}2\]
for its number of (not necessarily induced) two-edge wedges. Let \(T\) count all unordered three-vertex sets spanning triangles in \(G\). For every integer \(n\ge h\ge2\) and every real \(0\le p\le1\),
\[
\begin{aligned}
\operatorname{Var}(T\mid G[S]=H)
={}&\left(\binom N3+h\binom N2\right)(p^3-p^6)
 +eN(p^2-p^4)\\
&+2\binom N2\left(\binom{N-2}2+2h(N-2)+\binom h2\right)p^5(1-p)\\
&+4eN(N-1)p^4(1-p)+2Nw\,p^3(1-p).
\end{aligned}
\tag{1}
\]
A product of \(\binom N2\) and the bracketed expression in (1) is defined to be zero when \(N<2\); all binomial coefficients with out-of-range nonnegative arguments are zero. In particular, for fixed \(n,h,p\), the entire conditional variance depends on \(H\) **only** through \(e(H)\) and \(w(H)\), not through its triangle count or higher graph structure.

Consequently, for any two observed graphs \(H_1,H_2\) on the same \(h\)-vertex set with \(e(H_1)=e(H_2)\),
\[
\operatorname{Var}(T\mid H_1)-\operatorname{Var}(T\mid H_2)
=2(n-h)\bigl(w(H_1)-w(H_2)\bigr)p^3(1-p).
\tag{2}
\]
This yields a strict **wedge-ordering** of the conditional variances whenever \(n>h\) and \(0<p<1\), with equality exactly when the wedge counts agree.

For the four-vertex claw \(K_{1,3}\) and four-vertex path \(P_4\), both have three edges and no triangles but wedge counts three and two. Therefore, for every \(n\ge5\),
\[
\operatorname{Var}(T\mid K_{1,3})-\operatorname{Var}(T\mid P_4)
=2(n-4)p^3(1-p)>0 \qquad(0<p<1),
\tag{3}
\]
even though the conditional expected triangle counts coincide. At \(n=5\), \(p=1/2\), both means equal \(3/4\), whereas their respective variances are \(15/16\) and \(13/16\). The extra-vertex boundary \(n=h+1\) is sharp: at \(n=h\), the triangle count is deterministic.

## Assumptions and scope

The graph is simple, undirected, and labeled. The conditioning event specifies *both* present and absent edges among the chosen \(h\) vertices; it has positive probability when \(0<p<1\). At \(p=0\) or \(p=1\), formula (1) is understood algebraically for the uniquely possible observed graph, and the variance vanishes. The remaining \(\binom n2-\binom h2\) edges are mutually independent Bernoulli-\(p\) variables after conditioning. Triangle copies are unordered; wedges are unordered pairs of incident edges, including wedges contained in triangles. Nothing is conditioned on the number of total graph edges.

The companion first-moment identity is
\[
\mathbb E[T\mid G[S]=H]
=t+eNp^2+\left(\binom N3+h\binom N2\right)p^3.
\tag{4}
\]
Unlike the variance law, the conditional mean retains the deterministic internal triangle count \(t\); this elementary mean formula is background, not an independent priority claim. To illustrate the distinction, the triangular prism and \(K_{3,3}\) both have six vertices, nine edges, and eighteen wedges. Their internal triangle counts are respectively two and zero, so their conditional means differ by two, while their conditional variances agree for every \(n\ge6\), \(p\).

## Proof

Condition on \(G[S]=H\), and partition the triangle indicators according to the number of their vertices outside \(S\). Class \(A_0\) consists of triangles entirely outside \(S\) (there are \(\binom N3\), each requiring three random edges); class \(A_1\) has exactly one vertex inside \(S\) (there are \(h\binom N2\), requiring three random edges); class \(A_2\) has two vertices inside \(S\) (there are \(eN\) possible nonzero indicators, each requiring two random cross-edges); class \(A_3\) has all three vertices inside \(S\) and contributes the deterministic count \(t\). This proves (4) and gives the two diagonal variance contributions in the first line of (1).

Distinct nonzero triangle indicators are independent unless their required **random** edge sets intersect. Any two distinct triangles share at most one edge; if the common edge is random and their respective random-edge requirements have sizes \(r\) and \(s\), their covariance is exactly
\[
p^{r+s-1}(1-p).
\tag{5}
\]
The complete list of unordered dependent pairs is as follows; in each line the same covariance factor applies to all pairs:

| Classes of the two distinct triangles | Number of unordered dependent pairs | Covariance per pair |
|---|---:|---:|
| \(A_0,A_0\) | \(\binom N2\binom{N-2}2\) | \(p^5(1-p)\) |
| \(A_0,A_1\) | \(h\binom N2(N-2)\) | \(p^5(1-p)\) |
| \(A_1,A_1\), same inside vertex | \(h\binom N2(N-2)\) | \(p^5(1-p)\) |
| \(A_1,A_1\), different inside vertices | \(\binom h2\binom N2\) | \(p^5(1-p)\) |
| \(A_1,A_2\) | \(2eN(N-1)\) | \(p^4(1-p)\) |
| \(A_2,A_2\) | \(Nw\) | \(p^3(1-p)\) |

For the last line, two \(A_2\)-triangles share a random edge precisely when they use the same outside vertex and their two internal \(H\)-edges share an endpoint. The number of these pairs per outside vertex is \(\sum_v\binom{d_H(v)}2=w\). In the penultimate line, choose an edge of \(H\), its outside endpoint, which of its two inside endpoints lies in the \(A_1\)-triangle, and the second outside vertex. The other counts follow by choosing the common outer edge or cross-edge. No unlisted distinct pair shares a random edge, and pairs sharing merely a deterministic internal edge have zero covariance. The variance of the sum is the sum of the diagonal variances plus twice the six displayed pairwise covariance sums, yielding (1). Subtraction for equal-edge graphs gives (2); since \(p^3(1-p)>0\) for interior \(p\), this proves strictness and the equality condition. For (3), the claw's degree sequence is \((3,1,1,1)\) and the path's is \((2,2,1,1)\); each has three edges, zero triangles, but wedge counts three and two respectively.

## Verification

The companion standalone standard-library script `verify.py` independently enumerates all free-edge configurations and uses exact integer weights and rational arithmetic to compute the conditional first and second moments. Its separate implementation checks all observed graphs with two through four vertices in the indicated small domains, selected five-vertex observed graphs, the claimed claw-versus-path gap through \(n=49\), and equal-degree prism-versus-bipartite examples. Running `python3 verify.py` reports `PASS: 612 exact independent checks; no external files or packages required.` A direct exhaustive check at \(n=5,h=4,p=1/2\) gives the displayed \(13/16\) and \(15/16\) variances. Finite checks validate examples but are not the all-size proof; the complete pair classification above supplies that proof.

## Relationship to prior work

Ellis and Ferry derive general unconditional Erdős–Rényi subgraph-count variance formulas using copy overlaps; their model and overlap principle are relevant but their published formula concerns variance *without conditioning on a prescribed complete induced graph*. Kunegis gives an exact unconditional triangle-count variance and general computational overlap method; the inspected discussion does not characterize the conditional wedge-only graph fingerprint or the strict same-edge wedge ordering (2). Ginoza and Mugler study motif-count correlations under network randomization, motivating attention to dependencies but using a different randomization mechanism. The conditional **mean** response to observed edges is already an elementary consequence of independence; the contribution assessed here is the structural conditional **variance** statement, including exact separation of equal-edge observed graphs. These comparisons do not establish absolute historical novelty; general conditional overlap formulas might imply (1) without spelling it out.

## Limitations

The theorem assumes independent Bernoulli edges outside a fully revealed induced set. It is not asserted for fixed-total-edge \(G(n,m)\), degree-preserving randomization, random regular graphs, or conditioning only on \(e(H)\) without revealing the graph. The variance statistic does not identify all aspects of \(H\), and the first two conditional moments do not determine the entire triangle-count law. No hypothesis-testing power, optimal detector, or asymptotic distribution theorem is proved. Although full texts of the especially relevant 2009–2014 accessible sources were compared, priority may be implicit in older general overlap or conditional exposure literature; independent external review remains outstanding.

## References

- R. B. Ellis and J. P. Ferry, *Variance of the subgraph count for sparse Erdős–Rényi graphs*, Discrete Applied Mathematics 158 (2010), 649–658, DOI: https://doi.org/10.1016/j.dam.2009.11.012.
- J. Kunegis, *Polcovar: Software for Computing the Mean and Variance of Subgraph Counts in Random Graphs*, arXiv:1402.5835v1 (first posted 2014-02-24), https://arxiv.org/abs/1402.5835.
- R. Ginoza and A. Mugler, *Network motifs come in sets: correlations in the randomization process*, arXiv:0907.4680v1 (first posted 2009-07-27), https://arxiv.org/abs/0907.4680.
