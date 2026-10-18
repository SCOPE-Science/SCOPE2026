# Super-domination polynomial of bicliques with a deleted matching

## Finding

Let \(a,b\geq3\), let \(0\leq t\leq\min\{a,b\}\), and let \(G_{a,b,t}\) be the graph obtained from the complete bipartite graph \(K_{a,b}\) by deleting \(t\) pairwise vertex-disjoint edges. A vertex set \(S\) is *super dominating* when every \(u\notin S\) has a vertex \(v\in S\) with \(N(v)\cap(V\setminus S)=\{u\}\). Define the omitted-vertex enumerator
\[
Q_{a,b,t}(u)=\sum_{S\text{ super dominating}}u^{|V(G_{a,b,t})\setminus S|}.
\]
Writing \(N=a+b\), and setting \(\binom tk=0\) for \(k>t\), we prove the complete formula
\[
\boxed{Q_{a,b,t}(u)=1+Nu+\left(ab+2\binom t2\right)u^2+
\binom t2\left[N-4-(t-2)(\mathbf1_{a=3}+\mathbf1_{b=3})\right]u^3+
6\binom t4u^4.}
\]
Thus the conventional super-domination polynomial counting selected vertices is exactly \(D_{\mathrm{sp}}(G_{a,b,t};z)=z^NQ_{a,b,t}(z^{-1})\).

In particular, \(\gamma_{\mathrm{sp}}(G_{a,b,t})\), the minimum size of a super dominating set, is
\[
\boxed{\begin{cases}
N-2,&t\leq1\text{ or }(a,b,t)=(3,3,3),\\
N-3,&2\leq t\leq3\text{ and }(a,b,t)\ne(3,3,3),\\
N-4,&t\geq4.
\end{cases}}
\]
The number of minimum sets in the three nonexceptional regimes is, respectively, \(ab\), \(\binom t2[N-4-(t-2)(\mathbf1_{a=3}+\mathbf1_{b=3})]\), and \(6\binom t4\); in the exceptional six-vertex crown graph it is \(15\). Since every vertex has degree at least two, the same enumerator counts *end super dominating sets*. For fixed \(a,b\geq3\), the graphs \(G_{a,b,0}\) and \(G_{a,b,1}\) have identical super-domination polynomials despite having different edge counts, whereas the coefficient of \(u^2\) strictly distinguishes every \(t\geq2\) from all other matching-deletion sizes.

## Assumptions and scope

The graphs are finite, simple, labeled bicliques, with bipartition \(A=\{A_1,\ldots,A_a\}\) and \(B=\{B_1,\ldots,B_b\}\), and exactly the edges \(A_iB_i\) for \(1\leq i\leq t\) deleted. Relabeling shows that all matching choices give the same polynomial. Only \(a,b\geq3\) are claimed. Counts are for distinct vertex subsets, not graph-automorphism orbits. All values of \(t\), including \(t=0\), are included.

The definition of super domination uses **open** neighborhoods, not closed neighborhoods; every omitted vertex must have a *selected* witness adjacent to no other omitted vertex. The empty omitted set (selecting every vertex) is valid vacuously.

## Proof

**Step 1: At most two omitted vertices in each bipartition.** For any super dominating \(S\), put \(X=V\setminus S\), \(I=\{i:A_i\in X\}\), and \(J=\{j:B_j\in X\}\). Write \(\alpha=|I|\) and \(\beta=|J|\). Every \(B_j\) is adjacent to all but at most one vertex of \(A\). Therefore, if \(\alpha\geq3\), no selected vertex on \(B\) has exactly one neighbor in \(X\cap A\), contradicting the super-domination requirement for each omitted \(A\)-vertex. Hence \(\alpha\leq2\). The same argument gives \(\beta\leq2\).

**Step 2: Exact conditions for the boundary occupancies.** If \(\alpha=2\), write \(I=\{i,k\}\). To witness \(A_i\), a selected \(B\)-vertex must be adjacent to \(A_i\) but not \(A_k\). This is possible only when \(k\leq t\) and \(B_k\in S\). Similarly, witnessing \(A_k\) requires \(i\leq t\) and \(B_i\in S\). Thus the necessary and sufficient condition for the two omitted \(A\)-vertices is
\[
I\subseteq\{1,\ldots,t\},\qquad I\cap J=\varnothing.
\]
For \(\beta=2\), symmetrically, the exact condition for the two omitted \(B\)-vertices is \(J\subseteq\{1,\ldots,t\}\) and \(I\cap J=\varnothing\). The witness on the other side is necessarily the deleted-matching partner of the *other* omitted vertex.

If \(\alpha=1\), with \(I=\{i\}\), a witness on \(B\setminus X\) exists unless *every* selected \(B\)-vertex is the unique nonneighbor \(B_i\) of \(A_i\). Because \(|B\setminus X|=b-\beta\geq b-2\geq1\), this failure can occur only when \(b=3\) and \(\beta=2\), so that exactly one \(B\)-vertex is selected; it fails precisely when that vertex is \(B_i\) for \(i\leq t\). The symmetric exception when \(\beta=1\) requires \(a=3\), \(\alpha=2\), and the sole selected \(A\)-vertex to be the deleted-matching partner of the omitted \(B\)-vertex. When an omitted side is empty it imposes no requirements. This proves a complete if-and-only-if criterion for all nine pairs \((\alpha,\beta)\in\{0,1,2\}^2\).

**Step 3: Count the nine disjoint occupancy types.** For \((\alpha,\beta)=(0,0),(1,0),(0,1),(1,1)\), the numbers are, respectively, \(1,a,b,ab\). For \((2,0)\) and \((0,2)\), each count is \(\binom t2\). For \((2,1)\), choose two indices in the deleted matching and then an omitted \(B\)-vertex outside that pair, initially giving \(\binom t2(b-2)\). When \(a=3\), precisely \(\binom t2(t-2)\) of these choices fail the single-selected-vertex witness test in Step 2. Thus this type contributes
\[
\binom t2\big[b-2-(t-2)\mathbf1_{a=3}\big].
\]
Similarly, type \((1,2)\) contributes \(\binom t2[a-2-(t-2)\mathbf1_{b=3}]\). For \((2,2)\), the two disjoint deleted-matching index pairs can be chosen in \(\binom t2\binom{t-2}2=6\binom t4\) ways; the extra singleton witness exceptions cannot occur here because \(t\geq4\) forces \(a,b\geq4\). Summing by \(\alpha+\beta\) proves the polynomial.

**Step 4: Determine the minimum size and its multiplicity.** The polynomial degree is the largest feasible number of omitted vertices. Its fourth-degree coefficient is positive exactly when \(t\geq4\). Its third-degree coefficient is positive for \(t=2\), and for \(t=3\) except when \((a,b,t)=(3,3,3)\); this follows directly from the two occupancy counts. Otherwise the quadratic coefficient \(ab+2\binom t2\) is positive. The minimum size is \(N\) minus this degree, and the leading coefficient counts exactly the minima. For the exceptional profile, \(ab+2\binom t2=15\). Finally, the minimum degree is at least \(\min(a,b)-1\geq2\), so end super domination imposes no additional restriction. For the polynomial-separation corollary, the coefficient of \(u^2\) is \(ab+t(t-1)\), which is the same for \(t=0\) and \(t=1\) and strictly increases thereafter; those two graphs have different edge counts. This proves all claims.

## Verification

The standalone file `check_super_match.py` constructs every graph directly and checks, for every omitted vertex, the existence of a selected witness whose open neighborhood meets the omitted set in that singleton. It does not assume the classification in the proof. It enumerates every vertex subset for all \(a,b\in\{3,4,5,6,7\}\) and every \(0\leq t\leq\min(a,b)\), then compares a *bivariate omitted-occupancy table* with the separate combinatorial count. There are \(130\) graph profiles and \(407040\) tested vertex subsets; the total number of feasible sets across profiles is \(9388\). The executed result appears in `verification_output.txt`.

The checks are exhaustive only over the specified finite test range. The proof in Steps 1–4 establishes the claim over the entire stated infinite family.

## Relationship to prior work

Ghanbari, Jäger, and Lehtilä introduced enumerations of minimum super dominating sets in several graph families, including complete bipartite graphs, in a paper first released on 5 September 2022. In the no-deletion case \(t=0\), our result recovers their \(ab\) minimum sets but specifies the full polynomial; its new scope is an arbitrary *matching* of deleted edges and the ensuing sharp two- and four-edge thresholds. Akbari, Ghanbari, and Henning studied end super domination and graph modifications; their complete-bipartite case is subsumed at \(t=0\), but their inspected results do not enumerate these matching-deleted graphs. Published work on complete multipartite graphs also gives full super-domination enumerators, but those graphs do not in general contain the missing cross-edge pattern considered here (except at \(t=0\)).

Kaidash's 2024 chapter defines the full super-domination polynomial and reports formulas for unspecified graph families. Its accessible abstract does not list the matching-deleted biclique family, but the complete chapter could not be inspected; coverage there remains an explicit literature-priority risk.

## Limitations

The theorem excludes parts of order below three, where selected-witness availability has additional cases. No claim of a generally new definition, algorithm, or complexity classification is made. The formal mathematical claim is established directly, while originality remains subject to further bibliographic assessment, particularly against inaccessible full texts. Independent validation has not been performed.

## References

1. N. Ghanbari, G. Jäger, and T. Lehtilä, *Super Domination: Graph Classes, Products and Enumeration*, first public arXiv version 5 September 2022, https://arxiv.org/abs/2209.01795, later *Discrete Applied Mathematics* 349 (2024), 8–24.
2. S. Akbari, N. Ghanbari, and M. A. Henning, *End Super Dominating Sets in Graphs*, arXiv:2209.02980 (7 September 2022), https://arxiv.org/abs/2209.02980.
3. P. A. Kaidash, *Super Domination Polynomial of a Graph*, *Communications in Computer and Information Science* 2239 (2024), 85–95, DOI 10.1007/978-3-031-73365-9_6 (abstract publicly accessible; full text not inspected).
