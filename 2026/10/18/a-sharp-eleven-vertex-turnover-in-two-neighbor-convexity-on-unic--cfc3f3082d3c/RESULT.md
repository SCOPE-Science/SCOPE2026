# A sharp eleven-vertex turnover in two-neighbor convexity on unicyclic graphs

## Finding
For every finite connected simple unicyclic graph \(G\), write \(N(G)\) for the number of vertex sets \(S\subseteq V(G)\) such that each vertex outside \(S\) has at most one neighbor in \(S\). For every integer \(3\le n\le10\), the simple cycle \(C_n\) is the **unique**, up to isomorphism, \(n\)-vertex connected unicyclic graph maximizing \(N(G)\). For every integer \(n\ge11\), the cycle \(C_n\) is **not** a maximizer: the graph \(Q_n\) formed from \(C_4\) by adjoining \(n-4\) leaves at one cycle vertex satisfies
\[
N(Q_n)=2^{n-2}+2n-2>N(C_n).
\]
In particular, \(n=11\) is the **first order at which the cycle ceases to maximize** the number of \(P_3\)-convex sets among connected unicyclic graphs. This does not assert that \(Q_n\) is a global maximizer for any \(n\ge11\).

## Assumptions and scope
Graphs are finite, undirected and simple. Unicyclic means connected with exactly one cycle, equivalently \(|E(G)|=|V(G)|\). For every \(n\ge3\), the cycle \(C_n\) has exactly \(n\) vertices. A set is \(P_3\)-convex if it includes the middle vertex of every three-vertex path whose endpoints it contains; this is equivalent to the external-neighbor condition in the finding. The counting invariant includes the empty and full vertex sets.

## Proof
**1. Finite sharp portion.** Every connected unicyclic graph with \(n\) vertices is obtained by adding one missing edge to an \(n\)-vertex tree: delete any edge of its unique cycle. Every unrooted tree is represented by a rooted tree, and every rooted tree is uniquely determined by the multiset of its rooted child trees. The executable `certify.py` inductively generates **every** such rooted multiset of total size \(n-1\), using all smaller rooted trees. It then forgets the root, identifying duplicates by a canonical center decomposition: repeatedly delete all leaves until one center or two adjacent centers remain; recursively sort the rooted branch encodings. This is a complete and collision-free tree isomorphism invariant, because the center(s) are canonical and recursively sorted rooted branches characterize rooted trees up to isomorphism. Thus the program lists exactly one representative of each unrooted tree and, by adding each missing edge, **covers** all connected unicyclic graphs. Duplicates among resulting unicyclic graphs do not affect the maximum or uniqueness assessment; in these sizes the program finds one cycle representation and no noncycle tie.

For each graph, the program tests all \(2^n\) vertex subsets by the defining external-neighbor condition, using integer bit masks. Its exact integer table is:

| \(n\) | Unrooted trees | Tree plus nonedge cases | \(N(C_n)\) | Maximum | Cases tying cycle |
|---:|---:|---:|---:|---:|---:|
|3|1|1|5|5|1|
|4|2|6|10|10|1|
|5|3|18|17|17|1|
|6|6|60|29|29|1|
|7|11|165|51|51|1|
|8|23|483|90|90|1|
|9|47|1316|158|158|1|
|10|106|3816|277|277|1|

The enumerator and each vertex-subset test are finite, exhaustive and deterministic. The coverage argument shows that the table proves unique extremality of the cycle for \(3\le n\le10\). This is an exact finite proof with executable enumeration; no sampled or timed-out search is treated as exhaustive.

**2. Counts for cycles.** Represent each subset of \(C_n\) by its cyclic binary indicator word, with \(1\) meaning membership. Such a word is convex precisely when it avoids cyclic consecutive pattern \(101\), as the middle \(0\) would have two \(1\)-neighbors. The transition matrix on ordered two-bit states \(00,01,10,11\), admitting transitions that do not form \(101\), is
\[
A=\begin{pmatrix}1&1&0&0\\0&0&1&1\\1&0&0&0\\0&0&1&1\end{pmatrix}.
\]
The trace \(\operatorname{tr}(A^n)\) counts cyclic words with distinguished labeled positions, hence \(c_n:=N(C_n)=\operatorname{tr}(A^n)\). Direct determinant expansion gives
\[
\det(\lambda I-A)=\lambda(\lambda^3-2\lambda^2+\lambda-1).
\]
Cayley–Hamilton, with \(c_3=5\), \(c_4=10\), \(c_5=17\), yields
\[
c_{n}=2c_{n-1}-c_{n-2}+c_{n-3}\qquad(n\ge6).
\]
It follows inductively that \(c_{n+1}>c_n>0\) and \(c_{n+1}<2c_n\) for all \(n\ge5\): if three consecutive counts are increasing, the recurrence gives \(c_{n+1}-c_n=(c_n-c_{n-1})+c_{n-2}>0\), while \(2c_n-c_{n+1}=c_{n-1}-c_{n-2}>0\).

**3. Explicit noncycle witness.** Set \(t=n-4\). In \(Q_n\), let \(v\) be the vertex of \(C_4\) carrying the \(t\) new leaves. If \(v\) belongs to a convex set, there are precisely four permissible membership patterns on the four cycle vertices and the \(t\) leaves are arbitrary, giving \(4\cdot2^t\) sets. If \(v\) does not belong, at most one of its \(t+2\) neighbors belongs, and the opposite cycle vertex may be chosen independently; this gives \(2(t+3)\) sets. Therefore
\[
p_n:=N(Q_n)=4\cdot 2^t+2(t+3)=2^{n-2}+2n-2.
\]
The recurrence above gives \(c_{11}=486\), whereas \(p_{11}=532\). For \(n\ge11\), suppose \(q_n:=p_n-c_n\ge2n\), which holds at \(n=11\) because \(q_{11}=46\). Since \(p_{n+1}=2p_n-(2n-4)\) and \(c_{n+1}<2c_n\),
\[
q_{n+1}>2q_n-(2n-4)\ge2n+4>2(n+1).
\]
Thus \(q_n>0\) for every \(n\ge11\), proving the sharp threshold with the finite portion.

## Verification
Run `python3 certify.py` with Python 3.10 or later. The program has no third-party dependencies. It constructs all unrooted trees through size ten via a rooted multiset generator and center-canonical deduplication, adds all nonedges, and exhaustively tests all subsets. It checks the eight maxima and uniqueness counts from the displayed table and directly checks \(N(C_{11})=486\) and \(N(Q_{11})=532\). Its final successful line is `VERIFIED`. The transfer-matrix identity and the inequality for arbitrarily large \(n\) are mathematical arguments above; finite enumerations alone do not prove them.

## Relationship to prior work
Dourado, Grippo, Lin and Protti (2026) introduce a comprehensive counting study of \(P_3\)-convex sets. Their Lemma 5 shows that a unicyclic graph has fewer such sets than every spanning tree, and their Theorem 3 provides an efficient counting algorithm for trees. These results do **not** compare distinct unicyclic graphs, locate the first failure of cycle extremality, or give the infinite family of larger witnesses established here. Their path recurrence has the same characteristic cubic as the cycle trace, but does not imply the sharp finite extremal statement. Earlier work on the Helly number of \(P_3\)-convexity investigates a different invariant.

## Limitations
This theorem does not identify actual extremal unicyclic graphs for \(n\ge11\), nor determine the optimal maximum value beyond the range \(3\le n\le10\). The exact finite portion is justified by a transparent executable enumeration and its coverage proof, rather than a short case-free analytic classification. As with any literature comparison, an unindexed equivalent statement remains possible; no independent external audit is claimed here.

## References
Dourado, M. C., Grippo, L. N., Lin, M. C., and Protti, F. (2026), *Counting \(P_3\)-convex sets in graphs*, arXiv:2603.04706v1 (first posted March 5, 2026), https://arxiv.org/html/2603.04706 .

Carvalho, M. T., Dourado, M. C., and Szwarcfiter, J. L., *On the Helly Number in \(P_3\)-Convexity in Graphs*, Matemática Contemporânea 45 (2017), 106–114; abstract and bibliographic record at https://mc.sbm.org.br/wp-content/uploads/sites/9/sites/9/2021/12/45-12.pdf .
