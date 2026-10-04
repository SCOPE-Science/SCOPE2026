# Exact k-limited domination of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite simple complete multipartite graph with \(r\ge2\), with positive part sizes ordered as \(1\le n_1\le\cdots\le n_r\), and put \(N=\sum_{i=1}^r n_i\). A set \(D\subseteq V(G)\) is \(k\)-limited dominating when it dominates every vertex outside \(D\) and every vertex of \(D\) has at most \(k\) neighbors outside \(D\). For \(1\le k<\Delta(G)=N-n_1\), define
\[
T_k(G)=\max\left\{t\in\mathbb Z_{\ge0}:t\le N-k-2,\ t<n_{r-1},\ \sum_{i=1}^r\min\{n_i,t\}\le k+t\right\}.
\]
Then
\[
\gamma_k^{\mathrm L}(G)=N-k-T_k(G).
\]
The set defining \(T_k(G)\) is nonempty because \(t=0\) always satisfies its conditions. For the balanced complete \(r\)-partite graph with all part sizes equal to \(m\), this reduces to
\[
\gamma_k^{\mathrm L}(K_{m,\ldots,m})=rm-k-\left\lfloor\frac{k}{r-1}\right\rfloor,
\qquad 1\le k<(r-1)m.
\]

## Assumptions and scope
Graphs are finite, simple, and undirected. The theorem concerns connected complete multipartite graphs, hence \(r\ge2\), and the nontrivial range \(1\le k<\Delta(G)\) used in the initiating paper. The boundary cases are standard: \(k=0\) forces \(D=V(G)\), while \(k\ge\Delta(G)\) removes the capacity restriction and returns ordinary domination. The main formula does not claim results for arbitrary non-multipartite graphs.

## Proof
Fix a \(k\)-limited dominating set \(D\), let \(X=V(G)\setminus D\), write \(q=|X|\), and put \(d_i=|D\cap V_i|\), \(x_i=|X\cap V_i|=n_i-d_i\). Choosing \(N-k\) vertices that meet at least two parts gives a \(k\)-limited dominating set: its complement has size \(k\), so every selected vertex has at most \(k\) outside neighbors. Hence a minimum set has \(|D|\le N-k\), so \(q\ge k\). Write \(t=q-k\ge0\). Since \(k<\Delta(G)\), no one-vertex set can be \(k\)-limited dominating: a singleton dominator would have to be universal and would then have \(N-1>k\) external neighbors. Hence \(|D|=N-k-t\ge2\), giving \(t\le N-k-2\).

If \(d_i>0\), take \(u\in D\cap V_i\). Its neighbors outside \(D\) are exactly the vertices of \(X\setminus V_i\), so
\[
|N(u)\setminus D|=q-x_i\le k.
\]
Thus \(x_i\ge q-k=t\), equivalently \(d_i\le n_i-t\). Therefore a part that meets \(D\) must satisfy \(n_i>t\). If \(t>0\), domination forces \(D\) to meet at least two parts; when \(t=0\), the inequality \(t<n_{r-1}\) is automatic. Hence in all cases relevant to a minimum set, \(t<n_{r-1}\). Summing the bounds on \(d_i\) yields
\[
N-k-t=|D|=\sum_i d_i\le\sum_i\max\{n_i-t,0\}=N-\sum_i\min\{n_i,t\},
\]
which is equivalent to
\[
\sum_i\min\{n_i,t\}\le k+t.
\]
Thus every minimum \(k\)-limited dominating set produces a feasible \(t\), and consequently \(|D|\ge N-k-T_k(G)\).

Conversely, let \(t\) satisfy the three defining conditions for \(T_k(G)\), and set \(d=N-k-t\). There are at least two indices with \(n_i>t\), and
\[
\sum_i\max\{n_i-t,0\}=N-\sum_i\min\{n_i,t\}\ge d.
\]
Because \(d\ge2\), choose integers \(d_i\) with \(0\le d_i\le\max\{n_i-t,0\}\), total \(\sum_i d_i=d\), and positive values in at least two parts. Choose \(d_i\) vertices from each \(V_i\) to form \(D\). Meeting at least two parts makes \(D\) dominating. Moreover, if \(d_i>0\), then \(x_i=n_i-d_i\ge t\), and with \(q=k+t\),
\[
|N(u)\setminus D|=q-x_i\le k
\]
for every \(u\in D\cap V_i\). Thus \(D\) is \(k\)-limited dominating and has size \(N-k-t\). Taking \(t=T_k(G)\) gives the reverse inequality and proves the formula.

For equal parts \(n_i=m\), every feasible \(t\) satisfies \(t<m\), so the sum condition becomes \((r-1)t\le k\). Therefore the largest feasible value is \(\lfloor k/(r-1)\rfloor\); the assumption \(k<(r-1)m\) guarantees this is at most \(m-1\), and the size bound is also satisfied. The balanced formula follows.

## Verification
The bundled `verify.py` does not use the proof criterion to decide whether a subset is feasible. It explicitly constructs complete multipartite graphs from their part sizes, enumerates every subset, tests domination and the external-neighbor capacity directly, and compares the resulting optimum with the formula. It checks every complete-multipartite isomorphism type through order \(11\), for every nontrivial \(k\), and separately checks both the published complete-bipartite specialization and the balanced closed form.

## Relationship to prior work
Božović, Radić, Kovijanić-Vukićević, and Tepeh introduced \(k\)-limited domination and first made their preprint public on 2026-06-21. Their Proposition 1 gives exact values for paths, stars, complete graphs, and complete bipartite graphs. In the complete bipartite case \(K_{m,n}\), \(2\le m\le n\), they prove
\[
\gamma_k^{\mathrm L}(K_{m,n})=
\begin{cases}
1+n-k,&m\le k,\\
m+n-2k,&k<m,
\end{cases}
\qquad 1\le k<n.
\]
The formula above recovers this exactly: with two parts, feasibility reduces to \(t<m\) and \(t\le k\), hence \(T_k=\min\{m-1,k\}\). The same paper explicitly names determination on additional graph families as a future direction. It also notes that \(k\)-limited domination is the \((0,k)\)-pitchfork special case and that the pitchfork literature had concentrated on \((1,2)\), not this zero-lower-bound case.

Targeted searches under \(k\)-limited domination, \((0,k)\)-pitchfork domination, complete multipartite graphs, Turán graphs, and the exact feasibility expression did not locate a published or indexed statement implying this complete-multipartite formula. The closest semantic-index records concern different domination or complete-multipartite invariants and do not imply the claim.

## Limitations
The theorem does not address general graph classes, algorithmic complexity, graph products, or the enumeration of all minimum \(k\)-limited dominating sets. The exhaustive computation is a finite stress test through order \(11\), not a substitute for the universal proof. An unindexed older treatment of the \((0,k)\)-pitchfork special case remains a residual literature risk, although the 2026 initiating paper explicitly reports that this case had not been studied in that literature.

## References
1. D. Božović, G. Radić, Ž. Kovijanić-Vukićević, and A. Tepeh, “On \(k\)-limited domination in graphs,” arXiv:2606.22422, first public 2026-06-21; later published in *Computational and Applied Mathematics*, DOI:10.1007/s40314-026-03902-2.
2. M. N. Al-Harere and M. A. Abdlhusein, “Pitchfork domination in graphs,” *Discrete Mathematics, Algorithms and Applications* 12 (2020), 2050025, DOI:10.1142/S1793830920500251.
