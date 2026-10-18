# Zero-forcing polynomial and matching-deletion thresholds in dense bipartite graphs

## Finding

Let \(a,b\ge3\) and \(0\le t\le\min(a,b)\) be integers. Start from \(K_{a,b}\) with disjoint named parts \(A=\{a_1,\dots,a_a\}\) and \(B=\{b_1,\dots,b_b\}\), and remove the matching \(M_t=\{a_ib_i:1\le i\le t\}\). Denote the resulting graph by \(G_{a,b,t}\) and its order by \(N=a+b\). Write

\[
p=\binom{a}{2}-\binom{a-t}{2},\qquad
q=\binom{b}{2}-\binom{b-t}{2},\qquad
r=pq-t(a-t)(b-t)-\binom{t}{2}.
\]

A set \(S\subseteq V(G)\) is *zero forcing* if, after initially coloring exactly \(S\) blue, repeated use of the rule "a blue vertex with exactly one white neighbor colors that neighbor blue" colors the whole graph. Its zero-forcing polynomial is \(\mathcal Z(G;z)=\sum_{S\text{ zero forcing}}z^{|S|}\).

**Theorem.** The polynomial is

\[
\boxed{\mathcal Z(G_{a,b,t};z)=z^N+Nz^{N-1}+(ab+p+q)z^{N-2}+(bp+aq)z^{N-3}+rz^{N-4}.}
\]

Equivalently, all zero-forcing sets are exactly the complements of the white sets \(U\sqcup V\), with \(U\subseteq A\), \(V\subseteq B\), satisfying:

1. \(|U|\le2\) and \(|V|\le2\).
2. If \(|U|=2\), then at least one vertex of \(U\) has index in \(\{1,\ldots,t\}\), and similarly for \(V\).
3. If \(|U|=|V|=2\), let \(I_U=\{i\le t:a_i\in U\}\) and \(I_V=\{i\le t:b_i\in V\}\). Then \(I_U\ne I_V\).

In particular, the minimum size of a zero-forcing set has a three-stage transition:

\[
\boxed{Z(G_{a,b,t})=
\begin{cases}
N-2,&t=0,\\
N-3,&t=1,\\
N-4,&2\le t\le\min(a,b).
\end{cases}}
\]

The coefficient of \(z^{N-4}\) counts *every* minimum zero-forcing set for \(t\ge2\); the coefficient of \(z^{N-3}\) does so for \(t=1\). The theorem includes \(t=\min(a,b)\), in particular all crown graphs \(K_{n,n}-M_n\) for \(n\ge3\).

## Assumptions and scope

All graphs are finite, undirected, simple, with named vertex parts and named removed matching. A binomial coefficient with a zero upper argument has its usual value; the cases \(t=0\) and \(t=1\) require no separate polynomial conventions. The proof applies to every integer \(a,b\ge3\), including the small \(3\times3\) crown graph, with no asymptotics or genericity assumptions. It does not claim the same characterization for a side of size two.

## Proof

Fix an initially white set \(W=U\sqcup V\), with \(U\subseteq A\), \(V\subseteq B\), and write \(u=|U|\), \(v=|V|\). Every vertex of \(B\) has edges to all vertices of \(A\) except possibly its matched partner; the symmetric statement holds in the other direction.

**White-side obstruction.** If \(u\ge3\), then *every* blue vertex of \(B\) has at least \(u-1\ge2\) white neighbors in \(A\). No white vertex in \(A\) can be the first such vertex forced; before the first decrease of \(u\), the same inequality persists. Consequently \(u\ge3\) is incompatible with zero forcing. The same argument with the parts interchanged gives \(v\le2\), while the first argument gives \(u\le2\). This proves condition 1.

If \(u=2\) but neither white vertex is incident to a deleted matching edge, then every vertex of \(B\), blue or white, is adjacent to both vertices of \(U\). Thus no blue vertex can ever force either white vertex of \(A\), unless one had already been forced—a contradiction to the first-forcing argument. Consequently \(I_U\ne\varnothing\) whenever \(u=2\). Similarly \(I_V\ne\varnothing\) whenever \(v=2\). This proves condition 2.

**Completion lemma.** If \(u,v\le1\), the remaining white vertices can be forced: with exactly one white vertex on a side, at least two opposite-side vertices are blue, and at most one of these can be its non-neighbor. Force that vertex, and repeat on the other side. If \(u=2,v=0\) and \(I_U\ne\varnothing\), choose \(a_i\in U\) with \(i\le t\): its blue partner \(b_i\) is adjacent to the *other* white vertex of \(A\) and not to \(a_i\), so it forces the other white vertex. The remaining singleton is forced since \(b\ge3\). The symmetric statement holds for \(u=0,v=2\).

Now assume \(u=2,v=1\) and \(I_U\ne\varnothing\). If some blue vertex of \(A\) is adjacent to the sole white vertex of \(B\), that blue vertex forces it, leaving the already proved \((2,0)\) case. Otherwise every blue vertex of \(A\) is a non-neighbor of the sole white vertex \(b_j\). Since each \(b_j\) has at most one non-neighbor in \(A\), and \(a-2\ge1\), this is only possible when \(a=3\), with sole blue vertex \(a_j\), and \(j\le t\). A matched white vertex \(a_i\in U\) then has \(i\ne j\), so its partner \(b_i\) is blue and forces the *other* vertex of \(U\). We reach \((1,1)\) and finish. The case \(u=1,v=2\) follows by symmetry. Thus every configuration satisfying conditions 1 and 2 with \(\min(u,v)\le1\) is zero forcing.

**Two whites in both parts.** Suppose \(u=v=2\), with \(I_U,I_V\ne\varnothing\). A blue vertex \(b_i\) can initially force a vertex of \(U\) precisely when \(i\in I_U\setminus I_V\); the reason is that it misses the matched white vertex \(a_i\) and sees the other. Likewise a blue vertex \(a_j\) can initially force a vertex of \(V\) precisely when \(j\in I_V\setminus I_U\). Hence an initial move exists if and only if \(I_U\ne I_V\). If none exists, the initial configuration is stalled. If one exists, it leaves white sizes \((1,2)\) or \((2,1)\) with the size-two class still containing a matched endpoint; the completion lemma then finishes. This proves condition 3 and the all-set classification.

**Enumeration.** A two-subset of \(A\) includes a matched endpoint in exactly \(p\) ways, and likewise the count for \(B\) is \(q\). There is one empty white set; \(N\) singleton white sets; \(ab+p+q\) allowable size-two white sets (one in each part or an allowable pair within one part); and \(bp+aq\) allowable size-three sets (an allowable pair on one side and a singleton on the other). For four whites, there are initially \(pq\) pairs of allowable two-subsets. The forbidden pairs satisfy \(I_U=I_V\ne\varnothing\). When their common matched-index set has size one, choose its index in \(t\) ways and the remaining unmatched vertices in \((a-t)(b-t)\) ways. When it has size two, choose the same two matched indices in \(\binom t2\) ways. These cases are disjoint and exhaustive, leaving the stated coefficient \(r\). No larger white set can be forced, so the polynomial follows.

For \(t=0\), only the coefficients down to degree \(N-2\) are positive. For \(t=1\), \(p=a-1\), \(q=b-1\), \(r=0\), and \(bp+aq>0\). For \(t=2\), choose \(U=\{a_1,a_2\}\), \(V=\{b_1,b_3\}\): both sides have two whites with matched-index sets \(\{1,2\}\) and \(\{1\}\), so \(r>0\) (\(b\ge3\)). For \(t\ge3\), choose \(U=\{a_1,a_2\}\), \(V=\{b_2,b_3\}\), again giving \(r>0\). The zero-forcing-number cases follow. \(\square\)

## Verification

The standalone program `verify.py` constructs graph adjacency masks from the defining deleted matching and independently simulates the blue-vertex/unique-white-neighbor rule for each initial white set. It checks the structural characterization and compares all five polynomial coefficients with the closed formulas. Running `python3 verify.py` checks every vertex subset for all \(3\le a,b\le7\) and \(0\le t\le\min(a,b)\), covering 130 parameter profiles and 407040 subsets. It also checks all omitted configurations with at most two whites per side for twelve larger parameter profiles on \((8,9)\), \((10,11)\), and \((13,14)\), covering 60824 additional sets. Output is in `verification_output.txt`. These finite tests corroborate, but do not establish, the universal theorem.

## Relationship to prior work

Boyer, Brimkov, English, Ferrero, Keller, Kirsch, Phillips, and Reinhart introduced the zero-forcing polynomial [1]. In its Section 4 and later examples, that paper gives the formula \(\mathcal Z(K_{a,b};z)=z^N+Nz^{N-1}+abz^{N-2}\), precisely the \(t=0\) specialization, and its Theorem 1 determines the general second-from-top coefficient. Therefore neither the \(t=0\) formula nor the upper two coefficients are presented as new. The present result handles positive matching deletion, including the non-chain case \(t\ge2\), identifies the possible two-whites-per-side deadlock, and determines the new third/fourth lower coefficients and the matching-count phase transition.

Fallat and collaborators [2, Section 4.2] study the scalar \(q\)-analogue of zero forcing on *undeleted* complete bipartite graphs and related Cartesian products; they do not enumerate all initial sets on \(K_{a,b}-M_t\). Related published database findings about chain-graph zero forcing, complete-multipartite \(k\)-forcing, and other crown-graph invariants concern different hypotheses or outputs; the comparisons are documented in `AUDIT.json`.

## Limitations

The result concerns ordinary zero forcing, not positive-semidefinite, skew, or game-variant forcing. The condition \(a,b\ge3\) is necessary for the stated uniform completion proof: sides of order two can have exceptional forcing behavior. While inspected sources show no implication covering the positive-matching-deletion formula, exhaustive bibliographic uniqueness and independent review are not claimed.

## References

[1] K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, C. Reinhart, “The zero forcing polynomial of a graph,” arXiv:1801.08910v1 (first public 2018-01-26), subsequently *Discrete Applied Mathematics* 258 (2019), 35–48. Full text: https://arxiv.org/html/1801.08910v1 .

[2] S. Fallat, N. Joshi, R. Maleki, K. Meagher, S. A. Mojallal, S. Nasserasr, M. N. Shirazi, A. S. Razafimahatratra, B. Stevens, “The \(q\)-Analogue of Zero Forcing for Certain Families of Graphs,” arXiv:2306.01138v1 (first public 2023-06-01). Full text: https://arxiv.org/html/2306.01138v1 .
