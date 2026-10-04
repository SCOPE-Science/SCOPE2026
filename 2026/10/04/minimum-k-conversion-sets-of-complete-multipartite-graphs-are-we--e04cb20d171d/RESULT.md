# Minimum \(k\)-conversion sets of complete multipartite graphs are weighted parking profiles
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a complete multipartite graph with \(r\ge2\) and \(N=\sum_{i=1}^r n_i\). Fix an irreversible uniform \(k\)-threshold process: once active, a vertex remains active, and an inactive vertex activates when at least \(k\) of its neighbors are active.

For \(1\le k<N\), define
\[
D=\{i:N-n_i<k\},\qquad X=\bigcup_{i\in D}V_i,\qquad d=|X|.
\]
The vertices in \(X\) have degree below \(k\), so every \(k\)-conversion set contains \(X\). The minimum size \(\max\{d,k\}\) is known from the complete-multipartite theory. The refinement here classifies every minimum set.

If \(d\ge k\), then \(X\) is the unique minimum \(k\)-conversion set.

Assume \(d<k\). Then a set \(S\subseteq V(G)\) is a minimum \(k\)-conversion set if and only if all three conditions hold:

1. \(X\subseteq S\);
2. \(|S|=k\);
3. for each nondeficient part \(i\notin D\), put \(s_i=|S\cap V_i|\) and \(u_i=n_i-s_i\). Let \(J=\{i\notin D:u_i>0\}\), and order \(J\) so that \(s_{i_1}\le\cdots\le s_{i_q}\). Then
\[
s_{i_t}\le \sum_{h<t}u_{i_h}\qquad(1\le t\le q).
\]
For \(t=1\), the empty sum is \(0\), so at least one incomplete nondeficient part must initially receive no seeds.

Thus the number of minimum \(k\)-conversion sets is exactly
\[
M_k(G)=\sum_{\substack{0\le s_i\le n_i\ (i\notin D)\;\sum_{i\notin D}s_i=k-d\;\text{the ordered inequalities above hold}}}
\prod_{i\notin D}\binom{n_i}{s_i}.
\]
If \(d\ge k\), then \(M_k(G)=1\). If \(k\ge N\), every vertex has degree below \(k\), so \(V(G)\) is the unique minimum set.

## Assumptions and scope
Graphs are finite, simple, undirected, and complete multipartite with at least two nonempty parts. The threshold is uniform across vertices. The result concerns minimum irreversible \(k\)-threshold conversion sets, not arbitrary nonminimum conversion sets and not majority thresholds that vary with degree.

The classification is indexed by the canonical partite classes only through their sizes and seed counts. Parts with \(N-n_i<k\) are called deficient because no unseeded vertex in such a part can ever reach threshold.

## Proof
Every deficient vertex has fewer than \(k\) neighbors in the entire graph, hence must be seeded. This proves \(X\subseteq S\) for every conversion set. Also, if \(|S|<k\) and \(S\ne V(G)\), no initially inactive vertex can have \(k\) active neighbors, so no first activation is possible. These two lower bounds give \(|S|\ge\max\{d,k\}\) when \(k<N\).

When \(d\ge k\), seeding exactly \(X\) activates every vertex outside \(X\) in the next round because each such vertex is adjacent to all \(d\) seeded deficient vertices. Since every minimum set must contain all of \(X\) and already has size at least \(d\), \(X\) is the unique minimum set.

Now suppose \(d<k\) and \(S\) has size \(k\) with \(X\subseteq S\). For a nondeficient part \(V_i\), let \(s_i\) be its number of seeds and \(u_i=n_i-s_i\) its initially inactive vertices. Consider a stage before \(V_i\) has activated, and let \(U\) be the total number of newly activated, originally unseeded vertices in other nondeficient parts. Because \(G\) is complete multipartite, an inactive vertex of \(V_i\) sees exactly
\[
k-s_i+U
\]
active neighbors: all \(k\) initial seeds except the \(s_i\) seeds in its own part, plus the \(U\) newly activated vertices outside its part. Therefore \(V_i\) can activate exactly when
\[
U\ge s_i.
\]
When it does, it contributes exactly \(u_i\) new active vertices to the running total \(U\).

Consequently the vertex process is equivalent, on incomplete nondeficient parts, to the scalar process that starts with \(U=0\) and repeatedly accepts a part \(i\) with \(s_i\le U\), then replaces \(U\) by \(U+u_i\). Such a process succeeds for every incomplete part if and only if, after ordering the parts by nondecreasing \(s_i\), each \(s_{i_t}\) is at most the accumulated \(\sum_{h<t}u_{i_h}\). Necessity follows from the activation order of any successful process. For sufficiency, process the sorted parts in that order; each displayed inequality guarantees the next activation. Fully seeded parts need no activation and are correctly omitted. This proves the classification.

For a fixed feasible seed profile \((s_i)_{i\notin D}\), the choices inside distinct parts are independent, giving exactly \(\prod_{i\notin D}\binom{n_i}{s_i}\) vertex sets. Summing over feasible profiles gives the stated count.

## Verification
The accompanying `verify.py` independently implements the literal irreversible threshold process and the weighted-profile criterion. It exhaustively checks every ordered complete-multipartite part-size composition through order \(8\), every threshold \(1\le k\le N\), every minimum-size vertex subset, the known minimum-size formula, and the profile-count formula. A clean replay gives:

`VERIFY_OK profiles=247 subset_checks=71117 count_checks=1757 max_order=8`

The finite census is a regression test, not the proof of the infinite theorem.

## Relationship to prior work
Dreyer and Roberts developed irreversible \(k\)-threshold processes and determined minimum conversion numbers for several graph families, including complete multipartite graphs. Adams, Brass, Stokes, and Troxell later stated the complete-multipartite minimum in the unified form \(\max\{|X|,k\}\) for \(N>k\), where \(X\) is the set of vertices of degree below \(k\), and supplied a construction of one minimum set.

The present statement does not claim that minimum cardinality formula. It refines the scalar optimum to an if-and-only-if description of every optimum and an exact enumerator. This refinement is nontrivial: in \(K_{1,100,100}\) with \(k=50\), a set containing \(25\) seeds in each large part and none in the singleton has the optimal cardinality \(50\) yet is not a conversion set. The singleton activates first, after which each large part sees only \(26\) active neighbors and the process stalls. The weighted parking inequalities detect exactly this obstruction.

## Limitations
The result does not enumerate nonminimum conversion sets. It does not cover nonuniform threshold functions. The originality search found the prior minimum-value theorem and later general target-set-selection work, but older literature may use alternative language such as irreversible conversion, contagious sets, perfect target sets, or dynamic monopolies. No checked source stated the all-minimum-set parking-profile classification or its exact count.

## References
1. P. A. Dreyer Jr. and F. S. Roberts, “Irreversible \(k\)-threshold processes: Graph-theoretical threshold models of the spread of disease and of opinion,” *Discrete Applied Mathematics* 157 (2009), 1615–1627. DOI: 10.1016/j.dam.2008.09.012.
2. S. S. Adams, Z. Brass, C. Stokes, and D. S. Troxell, “Irreversible \(k\)-threshold and majority conversion processes on complete multipartite graphs and graph products,” arXiv:1102.5361, first posted 2011-02-25; later *Australasian Journal of Combinatorics* 56 (2013), 47–60.
3. P. Dvořák, D. Knop, and T. Toufar, “Target Set Selection in Dense Graph Classes,” *SIAM Journal on Discrete Mathematics* 36 (2022), 536–572, DOI: 10.1137/20M1337624.
