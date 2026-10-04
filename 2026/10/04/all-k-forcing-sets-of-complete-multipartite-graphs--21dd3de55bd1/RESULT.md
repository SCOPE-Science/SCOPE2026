# All k-forcing sets of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite connected complete multipartite graph with \(r\ge2\), partite sets \(V_1,\ldots,V_r\), and \(N=\sum_i n_i\), where \(n_i=|V_i|\). Fix \(k\ge1\). For an initial black set \(S\subseteq V(G)\), let
\[
w_i=|V_i\setminus S|,\qquad W=\sum_{i=1}^r w_i.
\]
Then \(S\) is a \(k\)-forcing set if and only if either \(W=0\), or there is an index \(i\) such that
\[
n_i-w_i>0,\qquad 1\le W-w_i\le k,\qquad w_i\le k.
\]
Thus an arbitrary initial set is decided by one possible first forcing part and the two white capacities on that part and its complement.

Put
\[
a_i=\min\{k,n_i-1\},\qquad c_i=\min\{k,N-n_i\},\qquad M_i=a_i+c_i,
\]
and \(M=\max_i M_i\). Then
\[
F_k(G)=N-M.
\]
If \(I=\{i:M_i=M\}\), the number of minimum \(k\)-forcing sets is
\[
m_k(G)=\sum_{\varnothing\ne J\subseteq I}(-1)^{|J|+1}
\left(\prod_{i\in J}\binom{n_i}{a_i}\right)
\binom{N-\sum_{i\in J}n_i}{M-\sum_{i\in J}a_i},
\]
where an out-of-range binomial coefficient is interpreted as zero.

## Assumptions and scope
The graph is finite, simple, connected, and complete multipartite with at least two nonempty parts. The \(k\)-forcing rule is the standard rule: a black vertex having at least one and at most \(k\) white neighbors colors all of those white neighbors black. The integer \(k\) is positive. The theorem classifies every initial set, then derives the minimum size and the exact number of minimum sets.

For \(k=1\), the theorem specializes to ordinary zero forcing. In particular, when every part has size at least two, it recovers the known formula \(Z(G)=N-2\) and the known count \(\sum_{i<j}n_i n_j\) of minimum zero-forcing sets. That special case is prior work and is not part of the originality claim.

## Proof
Assume first that \(W>0\) and that \(S\) is \(k\)-forcing. Consider the first force in any successful forcing sequence, and suppose its forcing vertex lies in \(V_i\). Before this first force no color has changed, so that vertex has exactly \(W-w_i\) white neighbors: every white vertex outside \(V_i\), and no white vertex inside \(V_i\). Hence \(1\le W-w_i\le k\). The forcing vertex is initially black, so \(n_i-w_i>0\). Its force colors every white vertex outside \(V_i\), leaving exactly the \(w_i\) white vertices of \(V_i\). Every vertex outside \(V_i\) then sees all of these remaining white vertices. If \(w_i>k\), no later force is possible, contradicting success. Therefore \(w_i\le k\).

Conversely, suppose an index \(i\) satisfies the three displayed inequalities. An initially black vertex of \(V_i\) has exactly \(W-w_i\) white neighbors, so it forces all white vertices outside \(V_i\). If \(w_i=0\), the graph is fully black. If \(w_i>0\), every vertex outside \(V_i\) is now black and sees exactly the \(w_i\le k\) remaining white vertices, so any such vertex forces all of them. Thus \(S\) is \(k\)-forcing. The case \(W=0\) is immediate.

For a witnessing part \(V_i\), the number of white vertices in that part is at most both \(k\) and \(n_i-1\), while the number outside it is at most both \(k\) and \(N-n_i\). Therefore
\[
W\le a_i+c_i=M_i.
\]
Conversely, choose exactly \(a_i\) white vertices in \(V_i\) and exactly \(c_i\) white vertices outside it. Because \(r\ge2\), one has \(c_i\ge1\), and the characterization shows this white profile is feasible. Hence the largest possible number of initially white vertices is \(M=\max_iM_i\), proving \(F_k(G)=N-M\).

It remains to count minimum sets. Fix \(i\in I\). A minimum set has \(W=M=M_i=a_i+c_i\). It is witnessed by \(i\) exactly when \(w_i=a_i\): necessity follows from \(w_i\le a_i\) and \(W-w_i\le c_i\), and sufficiency follows from the characterization. Let \(E_i\) be this event among white sets of size \(M\). For nonempty \(J\subseteq I\), the intersection \(\bigcap_{i\in J}E_i\) fixes \(a_i\) white vertices in each \(V_i\), leaving \(M-\sum_{i\in J}a_i\) whites to choose outside those parts. Its size is therefore
\[
\left(\prod_{i\in J}\binom{n_i}{a_i}\right)
\binom{N-\sum_{i\in J}n_i}{M-\sum_{i\in J}a_i}.
\]
Inclusion-exclusion over the events \(E_i\) gives the displayed formula for \(m_k(G)\).

## Verification
A standalone verifier independently implements the literal \(k\)-forcing dynamics and compares it with the structural criterion, the formula for \(F_k(G)\), and the inclusion-exclusion count of minimum sets. It exhaustively checks every ordered positive part-size profile of total order from \(2\) through \(9\), every admissible number of parts, every \(k\) from \(1\) through \(\min\{4,N\}\), and every initial vertex subset. The replay result is `VERIFY_OK profiles=502 parameter_checks=2003 subset_checks=694928 count_checks=2003 max_order=9 k_max=4`.

This finite computation is a regression check, not the proof of the theorem. The infinite statement is established by the first-force argument and inclusion-exclusion above.

## Relationship to prior work
Amos, Caro, Davila, and Pepper introduced the standard \(k\)-forcing number and proved general upper bounds. Their foundational paper supplies the propagation rule used here. Boyer et al. later introduced the zero-forcing polynomial and proved the complete-multipartite formula for ordinary zero forcing when all part sizes are at least two; this is exactly the \(k=1\) covered slice acknowledged above.

A later study of \(k\)-forcing automata treats complete bipartite graphs and records minimum-set behavior in that two-part setting. Those results do not give the arbitrary complete-multipartite all-set criterion or the inclusion-exclusion formula for the number of minimum \(k\)-forcing sets. Searches under the aliases generalized forcing, zero forcing, connected \(k\)-forcing, oriented \(k\)-forcing, and \(q\)-zero forcing were also compared; the latter variants use different rules or additional restrictions.

## Limitations
The theorem concerns the standard undirected \(k\)-forcing rule on complete multipartite graphs; it does not apply automatically to connected, oriented, positive-semidefinite, skew, probabilistic, or game variants of zero forcing. The finite verifier reaches order \(9\) and \(k\le4\), so it is not an exhaustive certificate for the infinite family. The literature comparison leaves a residual possibility that an older, poorly indexed source using alternate terminology contains an equivalent arbitrary-multipartite statement; no such source was found in the targeted full-text and semantic searches performed.

## References
1. D. Amos, Y. Caro, R. Davila, and R. Pepper, *Upper bounds on the k-forcing number of a graph*, arXiv:1401.6206v1; Discrete Applied Mathematics 181 (2015), 1–10, DOI:10.1016/j.dam.2014.08.029.
2. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, and C. Reinhart, *The zero forcing polynomial of a graph*, arXiv:1801.08910v1; Discrete Applied Mathematics 258 (2019), 35–48, DOI:10.1016/j.dam.2018.11.033.
3. *Recognizable Languages of k-Forcing Automata*, Mathematical and Computational Applications 29 (2024), article 32, DOI:10.3390/mca29030032.
