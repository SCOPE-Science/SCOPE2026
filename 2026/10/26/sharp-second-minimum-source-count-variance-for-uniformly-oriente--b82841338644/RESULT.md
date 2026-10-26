# Sharp second-minimum source-count variance for uniformly oriented trees

## Finding

Let \(T\) be any finite tree of order \(n\ge4\). Independently orient each edge in either direction with probability \(1/2\), and let \(S(T)\) denote the number of vertices with indegree zero. For the path \(P_n\),
\[
\operatorname{Var}(S(P_n))=\frac n{16}.
\]
For every nonpath tree,
\[
\boxed{\operatorname{Var}(S(T))\ge\frac n{16}+\frac3{64}.}
\]
Equality holds if and only if \(T\) has precisely one degree-three vertex, all its other vertices have degree one or two, and all three arms from the degree-three vertex to the leaves contain at least two edges. Equivalently, \(T\) is a subdivided claw with arm lengths \(a,b,c\ge2\). Thus, for every \(n\ge7\), the second-smallest possible source-count variance among all trees of order \(n\) equals \(n/16+3/64\), with the complete equality classification above. For \(4\le n\le6\), the inequality is strict. By reversing all edge orientations, the same theorem holds for the number of sinks.

## Assumptions and scope

All graphs are finite, simple, undirected trees prior to orientation. Each edge independently selects its direction by an unbiased fair coin. A source has no incoming edges. A tree arm length is the number of edges between the unique degree-three center and a leaf. No independence is asserted between source indicators at adjacent vertices. The theorem is not asserted for biased orientations or graphs with cycles.

## Proof

**Exact variance identity.** Write \(d_v\) for the degree of a vertex \(v\), \(a_v=2^{-d_v}\), and \(X_v\) for its source indicator. Then \(\mathbb E X_v=a_v\). For nonadjacent vertices their incident edge sets are disjoint, so the indicators are independent. For adjacent vertices, the shared edge cannot point outward from both, and therefore \(X_uX_v=0\). Hence
\[
\operatorname{Var}\!\left(\sum_v X_v\right)
=\sum_v(a_v-a_v^2)-2\sum_{uv\in E(T)}a_ua_v.
\tag{1}
\]
Set \(b(d)=(2^d-d-1)4^{-d}\). Expanding the edge squares in the following formula recovers (1):
\[
\boxed{\operatorname{Var}(S(T))
=\sum_{uv\in E(T)}(a_u-a_v)^2+\sum_v b(d_v).}
\tag{2}
\]
Every term is nonnegative. The local values are \(b(1)=0\), \(b(2)=b(3)=1/16\). A path has precisely two degree-one vertices, \(n-2\) degree-two vertices and two edges of squared \(a\)-difference \(1/16\), so (2) gives \(\operatorname{Var}(S(P_n))=n/16\).

**Branching budget.** Suppose \(T\) is not a path and put \(H=\{v:d_v\ge3\}\), \(L=\#\{v:d_v=1\}\), and \(U=\#\{v:d_v=2\}\). The handshaking identity gives
\[
L=2+\sum_{v\in H}(d_v-2),\qquad n=L+U+|H|.
\tag{3}
\]
Suppress every degree-two vertex. Every original leaf now belongs to a unique maximal path, called a leaf arm, ending at a branching vertex; let \(t_v\) count leaf arms ending at \(v\in H\). Then \(\sum_{v\in H}t_v=L\). Every such arm of branch degree \(d\) contributes at least
\[
\frac1{16}+g(d)\quad\text{to}\quad\sum_{uv\in E(T)}(a_u-a_v)^2,
\qquad g(d)=\left(\frac14-2^{-d}\right)^2.
\tag{4}
\]
Indeed, if the arm has a degree-two vertex, its first edge from the leaf contributes \(1/16\), its last edge into the branching vertex contributes \(g(d)\), and any intervening edges contribute zero. If the arm consists of a single edge directly joining a leaf to its branch vertex, its contribution is
\[
\left(\frac12-2^{-d}\right)^2
=\frac1{16}+g(d)+\frac12\left(\frac14-2^{-d}\right)
>\frac1{16}+g(d).
\tag{5}
\]
Every remaining edge has nonnegative squared contribution. Since \(b(1)=0\) and \(b(2)=1/16\), combining (2)--(4) with (3) gives
\[
\operatorname{Var}(S(T))-\frac n{16}
\ge\sum_{v\in H}\bigl(t_v g(d_v)-\delta(d_v)\bigr),
\qquad\delta(d)=\frac1{16}-b(d).
\tag{6}
\]

**Degree inequalities.** For every integer \(d\ge3\),
\[
g(d)\ge g(3)=\frac1{64},\qquad
\delta(d)\le\frac{d-2}{64}.
\tag{7}
\]
The first statement follows from the monotonicity of \(1/4-2^{-d}\). For the second, equality at \(d=3\) holds because \(\delta(3)=0\). Direct substitution gives \(\delta(4)=5/256<2/64\) and \(\delta(5)=38/1024<3/64\). For \(d\ge6\), the inequality follows from \(\delta(d)\le1/16\le(d-2)/64\). Also, for \(d\ge4\),
\[
g(d)\ge g(4)=\frac9{256}.
\tag{8}
\]
If at least one branching vertex has degree three, substitute (7) in (6), then use (3):
\[
\operatorname{Var}(S(T))-\frac n{16}
\ge\frac{L}{64}-\sum_{v\in H}\delta(d_v)
=\frac2{64}+\sum_{v\in H}\left(\frac{d_v-2}{64}-\delta(d_v)\right)
\ge\frac3{64}.
\tag{9}
\]
The last step uses the contribution \(1/64\) of at least one degree-three vertex. Equality requires *exactly one* branching vertex, of degree three, because every additional branching vertex contributes strictly positively (for degree three, \(1/64\); for degrees at least four, strictness in (7)). With this sole degree-three center, equality in (4) requires that no arm be a direct leaf-center edge, i.e. all three arms have length at least two. Conversely, those trees have exactly three \(g(3)=1/64\) arm contributions and no other excess, proving equality.

If instead every branching degree is at least four, then \(L\ge4\), and (3), (6)--(8) yield
\[
\operatorname{Var}(S(T))-\frac n{16}
\ge \frac{9L}{256}-\frac{L-2}{64}
=\frac{5L+8}{256}\ge\frac{28}{256}>\frac3{64}.
\tag{10}
\]
These cases exhaust nonpaths. Finally, three arms of lengths at least two require \(n\ge7\), and such trees exist for every \(n\ge7\). This proves all assertions.

## Verification

A standalone exact-arithmetic verifier, `verify.py`, independently constructs every labeled tree using Prüfer codes for orders \(4\) through \(7\), checks the gap and the equality characterization, and directly enumerates all edge-orientation configurations for every labeled tree through order \(6\). It tests the degree inequalities numerically for many integer degrees; the proof of those inequalities is algebraic and unrestricted. Run using `python verify.py` (Python 3 standard library only). The finite checks supplement rather than replace the proof.

## Relationship to prior work

Source statistics in directed random graphs and reachability correlation in independently oriented fixed graphs provide nearby motivation. Bienvenu's arXiv:1711.08815, §§1--2, addresses positive association of *reachability events from a specified source set*, rather than indegree-zero source-count variance. Ralaivaosaona, DOI 10.4230/LIPIcs.AofA.2022.17, Theorems 1--2, studies the number of sources of a random sparse DAG with a random edge set rather than varying a fixed underlying tree. Conte et al., DOI 10.1016/j.dam.2017.08.002, investigate algorithms that enumerate orientations under source restrictions rather than the sharp tree variance gap. The present contribution is the global sharp positive gap above the path variance and its exact second-minimizer classification, not the routine first/second moment identity by itself.

## Limitations

No statement is claimed for unequal direction probabilities, higher moments, connected graphs containing cycles, or arbitrary source-count distribution order. The second-moment identity is elementary and may be known; historical precedence for the extremal gap should be checked independently before asserting priority. This is a self-review, not independent validation.

## References

1. François Bienvenu, *Positive association of the oriented percolation cluster in randomly oriented graphs*, arXiv:1711.08815 (initial public version 2017-11-23), especially §§1--2.
2. Dimbinaina Ralaivaosaona, *The Number of Sources and Isolated Vertices in Random Directed Acyclic Graphs*, LIPIcs AofA 2022, DOI:10.4230/LIPIcs.AofA.2022.17, especially §1 and Theorems 1--2.
3. Alessio Conte, Roberto Grossi, Andrea Marino and Romeo Rizzi, *Efficient enumeration of graph orientations with sources*, Discrete Applied Mathematics 246 (2018), DOI:10.1016/j.dam.2017.08.002.
