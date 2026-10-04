# Connected dom-k-forcing of complete multipartite graphs
## Finding
Let \(G=K_{{n_1,\ldots,n_r}}\) be a finite simple complete multipartite graph with \(r\ge2\), let \(N=\sum_i n_i\), and assume \(1\le k\le\Delta(G)\). Put
\[
W_k(G)=\max_{{1\le i\le r}}\left(\min\{{k,n_i-1\}}+\min\{{k,N-n_i-1\}}\right).
\]
Then
\[
F_{{cdk}}(G)=
\begin{{cases}}
1,&\min_i n_i=1\text{{ and }}k=N-1,\\
N-W_k(G),&\text{{otherwise}}.
\end{{cases}}
\]
Thus the parameter is determined exactly by the part sizes and \(k\).

## Assumptions and scope
The graph is finite, simple, and has at least two nonempty partite sets. The connected dom-\(k\)-forcing number follows the definition in Susanth, Dominic, and Premodkumar: the initial set must dominate the graph, induce a connected subgraph, and under the rule that a colored vertex with at most \(k\) uncolored neighbors colors all of them, eventually color the whole graph. The range is \(1\le k\le\Delta(G)\).

## Proof
Write \(V_1,\ldots,V_r\) for the partite sets and let \(D\) be an initial connected dom-\(k\)-forcing set. Let \(U=V(G)\setminus D\), let \(w_i=|U\cap V_i|\), and let \(W=|U|\).

First suppose \(|D|=1\). A one-vertex dominating set in a complete multipartite graph must be a universal vertex, so its part has size one. Such a vertex has \(N-1\) uncolored neighbors initially, hence it can start the process exactly when \(k\ge N-1\). Since \(k\le\Delta(G)\le N-1\), this is exactly the exceptional case \(k=N-1\) with a singleton part. Conversely, the universal vertex is then a connected dominating set and forces all other vertices in one step.

Now assume \(|D|\ge2\). Because the induced subgraph on \(D\) is connected and no two vertices in one part are adjacent, \(D\) meets at least two parts. If \(U=\varnothing\), the claimed lower bound is immediate. Otherwise consider the first nonempty force, made by a black vertex in some part \(V_i\). Before any nonempty force occurs, that vertex has exactly \(W-w_i\) white neighbors, all outside \(V_i\), so
\[
W-w_i\le k.
\]
The force colors every white vertex outside \(V_i\). The only possible white vertices left are the \(w_i\) vertices in \(V_i\). Since \(D\) meets another part, at least one black vertex lies outside \(V_i\). Every such black vertex is adjacent to all \(w_i\) remaining white vertices. If \(w_i>k\), none can force, while vertices of \(V_i\) have no neighbors inside their own part; the process would stall. Hence \(w_i\le k\).

Because the forcing vertex itself is initially black in \(V_i\), \(w_i\le n_i-1\). Because \(D\) also has an initially black vertex outside \(V_i\), \(W-w_i\le N-n_i-1\). Combining the four bounds gives
\[
W\le\min\{k,n_i-1\}+\min\{k,N-n_i-1\}\le W_k(G).
\]
Therefore \(|D|=N-W\ge N-W_k(G)\).

For the reverse inequality choose an index \(i\) attaining \(W_k(G)\), and set
\[
a=\min\{k,n_i-1\},\qquad b=\min\{k,N-n_i-1\}.
\]
Leave exactly \(a\) vertices of \(V_i\) white and exactly \(b\) vertices outside \(V_i\) white; color every other vertex initially. The inequalities \(a\le n_i-1\) and \(b\le N-n_i-1\) leave at least one black vertex both in \(V_i\) and outside it. Hence the initial black set meets at least two parts, so it is connected and dominating. If \(b>0\), a black vertex of \(V_i\) forces all \(b\) outside white vertices; if \(b=0\), skip this empty step. Then, if \(a>0\), any black vertex outside \(V_i\) forces all \(a\) remaining white vertices. Thus this is a connected dom-\(k\)-forcing set of size \(N-a-b=N-W_k(G)\), completing the proof.

## Verification
A standalone verifier reconstructs every complete multipartite graph type through order nine, enumerates every candidate initial set, checks domination and induced connectivity directly, simulates the \(k\)-forcing process for every \(1\le k\le\Delta(G)\), and compares the brute-force optimum with the displayed formula. It reports:

`ALL CHECKS PASSED; multipartite_types=87; parameter_cases=524; max_order=9`

This finite computation is a stress test, not the proof of the universal statement.

## Relationship to prior work
Susanth, Dominic, and Premodkumar introduced connected dom-\(k\)-forcing and proved exact values for several graph families. Their paper gives \(F_{{cdk}}(K_N)=\max\{{N-k,1\}}\) for complete graphs, and for \(m,n\ge3\) gives \(F_{{cd2}}(K_{{m,n}})=m+n-4\). The formula above recovers both results and extends the second from two parts and \(k=2\) to arbitrary part profiles and all admissible \(k\).

For the boundary \(k=1\), the earlier connected dom-forcing paper gives \(F_{{cd}}(K_{{m,n}})=m+n-2\) for \(m,n\ge2\), again matching the specialization here. Earlier connected \(k\)-forcing work, which does not impose domination, gives the complete-bipartite connected zero-forcing value and the all-\(k\) star value, but does not state the present connected-domination formula for arbitrary complete multipartite graphs. Searches under connected dom-\(k\)-forcing, connected \(k\)-forcing, complete multipartite, complete bipartite, and part-size formulations did not locate a statement covering the theorem above.

## Limitations
The result concerns complete multipartite graphs and the connected dom-\(k\)-forcing rule exactly as defined above. It does not classify all minimum initial sets, forcing times, or analogous parameters on multipartite graphs with missing cross-edges. The literature comparison cannot exclude an equivalent result published under terminology not surfaced by the checked sources; this remains the principal originality risk.

## References
1. P. Susanth, Charles Dominic, and K. P. Premodkumar, “Connected Dom-k-forcing Sets in Graphs,” Journal of Advances in Mathematics and Computer Science 41(2) (2026), 15–27. DOI: 10.9734/jamcs/2026/v41i22096.
2. P. Susanth, Charles Dominic, and K. P. Premodkumar, “Connected Dom-forcing Sets in Graphs,” Advances and Applications in Discrete Mathematics 42(7) (2025), 713–736. DOI: 10.17654/0974165825046.
3. K. P. Premodkmuar, Charles Dominic, and Baby Chacko, “Connected k-forcing sets of graphs and splitting graphs,” Journal of Mathematics and Computer Science 10(3) (2020), 656–680. DOI: 10.28919/jmcs/4446.
4. David Amos, Yair Caro, Randy Davila, and Ryan Pepper, “Upper bounds on the k-forcing number of a graph,” Discrete Applied Mathematics 181 (2015), 1–10; arXiv:1401.6206.
