# Exact 1-limited domination and all minimizers of clique–cycle Cartesian products

## Finding
For all integers \(m,n\ge3\), put \(G_{m,n}=K_m\square C_n\) and define
\[
h(n)=2\left\lfloor\frac n4\right\rfloor+\mathbf 1_{n\equiv3\pmod4}.
\]
Then
\[
\gamma_1^{\mathrm L}(G_{m,n})=m\bigl(n-h(n)\bigr).
\]
For \(m\ge3\), every minimum 1-limited dominating set is obtained by omitting \(h(n)\) complete clique fibers according to a cyclic binary word of length \(n\) with no three consecutive ones and no cyclic factor \(101\), except that when \((m,n)=(3,3)\) or \((3,6)\), three additional minimizers omit a complete cycle fiber (one fixed clique-coordinate row). The cyclic word's ones are the omitted complete clique fibers; in particular, the word has exactly \(h(n)\) ones.

For labelled vertices the number \(a_{m,n}\) of minimum sets is
\[
a_{m,n}=\begin{cases}4,&n\equiv0\pmod4,\\n,&n\equiv1,3\pmod4,\\ n^2/4,&n\equiv2\pmod4\end{cases}
+3\mathbf1_{m=3,\ n\in\{3,6\}}.
\]
Thus \(a_{3,3}=6\) and \(a_{3,6}=12\); all other cases use the displayed base count. The scalar identity also shows that the already-known Cartesian-product upper bound \(m\gamma_1^{\mathrm L}(C_n)\) is sharp throughout this family.

## Assumptions and scope
All graphs are finite, undirected and simple, with the usual Cartesian product. For \(n\ge3\), the cycle \(C_n\) has distinct predecessor and successor vertices. A set \(D\) is 1-limited dominating when (i) every vertex not in \(D\) is adjacent to a vertex of \(D\), and (ii) each vertex in \(D\) has at most one neighbor not in \(D\). We count subsets of a specified, labelled graph; graph automorphisms are not factored out.

Index clique vertices by \(i\in\{1,\ldots,m\}\) and cyclic columns by \(j\in\mathbb Z/n\mathbb Z\). Let \(S=V(G)\setminus D\). A column is *full* if it is wholly contained in \(S\), *empty* if it contains no vertex of \(S\), and *singleton* if it contains one vertex of \(S\).

## Proof
**1. Column types and exclusions.** Let \(s_j\) be the number of omitted vertices in column \(j\). A selected vertex in column \(j\) has exactly \(s_j\) omitted neighbors in its clique, before its two cyclic neighbors are considered. If \(0<s_j<m\), the 1-limited constraint therefore forces \(s_j=1\). Thus the three column types just defined are exhaustive.

A full column must have a non-full adjacent column to dominate its omitted vertices, so there cannot be three consecutive full columns. Moreover, a non-full column between two full columns would have a selected vertex with two omitted cyclic neighbors, so the cyclic type \(\text{full},\text{non-full},\text{full}\) is impossible. Consequently, each maximal full block has one or two columns and successive full blocks are separated by at least two non-full columns.

A singleton cannot be one column away from a full column: its selected vertices already have their one omitted clique neighbor and also have an omitted cyclic neighbor in the full column. Neither can it be two columns away: the intervening column is necessarily empty (it cannot be singleton by the preceding argument), and a selected vertex there has omitted cyclic neighbors in both the singleton and the full columns, violating the 1-limited constraint. Hence singletons must be at cyclic distance at least three from every full column.

**2. The maximal number of omissions in the presence of full columns.** Suppose \(S\) has \(b\ge1\) maximal full blocks, containing altogether \(f\) full columns. Then \(b\le f\le2b\). Write \(g_1,\ldots,g_b\ge2\) for the numbers of consecutive non-full columns separating the blocks, so \(\sum_i g_i=n-f\). In a gap of length \(g_i\), the distance-two exclusion permits singleton columns only at its \(\max\{0,g_i-4\}\) interior positions. Putting \(e=n-f-2b\), the total number of singleton columns is at most
\[
\sum_{i=1}^{b}(g_i-4)_+\le(e-2)_+,
\]
where \(u_+=\max\{0,u\}\). Therefore
\[
|S|\le mf+(n-f-2b-2)_+.
\]
For fixed \(b\), this bound strictly increases with \(f\), because \(m\ge3\); its largest feasible \(f\) is \(f_b=\min\{2b,n-2b\}\), and \(1\le b\le\lfloor n/3\rfloor\). Write \(n=4q+r\) with \(0\le r\le3\). For \(b\le q\) the bound becomes \(2mb+(n-4b-2)_+\), strictly increasing in \(b\). For \(b\ge q+1\) it is \(m(n-2b)\), strictly decreasing in \(b\). Comparing the boundary possibilities (or taking \(n=3\) separately) yields precisely the largest possible omitted-vertex count
\[
mh(n)=m\bigl(2q+\mathbf1_{r=3}\bigr).
\]
Equality forces no singleton columns: the only maximizing block configurations are \(b=q,f=2q\) when \(r=0,1\); either \(b=q,f=2q\) or \(b=q+1,f=2q\) when \(r=2\); and \(b=q+1,f=2q+1\) when \(r=3\). For \(n=3\), the unique block profile is \(b=f=1\). In all these cases the separating gaps leave at most two positions beyond their mandatory two non-full columns, which are all within distance two of a full column.

**3. The case without full columns.** There is at most one omitted vertex in each column, so \(|S|\le n\). Equality forces every column to be a singleton. If consecutive singleton columns omitted vertices in different clique-coordinate rows, a selected vertex in one column would have both an omitted clique neighbor and an omitted cyclic neighbor; hence every omitted vertex must lie in the same row. Conversely, omitting any entire cycle row is feasible: every omitted vertex has selected clique neighbors, and each selected vertex has exactly one omitted clique neighbor. Since \(mh(n)\ge n\) for all \(m,n\ge3\), with equality exactly for \((m,n)=(3,3),(3,6)\), these are precisely the two exceptions contributing three further optimal sets.

**4. Attainment and full classification.** Omitting any \(h(n)\) whole clique columns whose cyclic binary indicator avoids \(111\) and \(101\) is feasible. An omitted vertex in a full column has a selected cyclic neighbor (no three full columns in a row), and a selected vertex has at most one omitted cyclic neighbor (no \(101\)). The maximizing run configurations of step 2 exist in every residue class, proving the value of \(\gamma_1^{\mathrm L}\) and the classification.

**5. Counting.** For \(b\) cyclic blocks of full columns, comprising \(f\) full columns and separated by at least two other columns, the number of cyclic labelled indicator words is exactly
\[
\frac nb\binom b{f-b}\binom{n-f-b-1}{b-1}.
\]
Indeed, choose which of the \(b\) full blocks have length two, distribute the \(n-f-2b\) extra non-full positions over the \(b\) gaps, choose a starting column, and divide by the \(b\) choices of a distinguished block of any resulting word. Summing this count over the maximizing \((b,f)\) profiles of step 2 gives \(4,n,n^2/4,n\) in residue classes \(0,1,2,3\pmod4\), respectively. Adding the three distinct whole-cycle-row minimizers in the two equality cases completes the enumerator.

## Verification
The accompanying C++17 source `verify.cpp` independently enumerates every vertex subset of ten small labelled Cartesian products using the original graph adjacency relation; in each case it computes the minimum size and number of minimum 1-limited dominating sets. In a separate dynamic program it enumerates all 0/singleton/full column configurations directly from the local dominating and neighbor-capacity conditions for all \(3\le m\le8\) and \(3\le n\le34\), without using the structural classification to generate valid states. The results were:

```
DIRECT_ORIGINAL_GRAPH_EXHAUSTIVE_OK 10 CASES
COLUMN_PATTERN_DP_OK 192 CASES
VERIFY_OK
```

Compile and run using `c++ -O2 -std=c++17 verify.cpp -o verify && ./verify` from a directory containing the supplied source file. These finite checks support, but do not replace, the proof for all integers.

## Relationship to prior work
Božović, Radić, Kovijanić-Vukićević and Tepeh [1] introduce 1-limited domination, identify its regular-graph equivalence with \((1,d-1)\)-domination, and obtain the cycle formula \(\gamma_1^{\mathrm L}(C_n)=n-h(n)\) (their Corollary 8). Tepeh [2] gives the general product upper bound \(\gamma_k^{\mathrm L}(G\square H)\le\min\{|V(H)|\gamma_k^{\mathrm L}(G),|V(G)|\gamma_k^{\mathrm L}(H)\}\), among other product results; it does not state an exact classification for \(K_m\square C_n\) with \(m\ge3\). Equality in this upper bound is already forced by published general bounds for some residue-zero cases, and is not claimed independently of that implication. The new contributions are the uniform two-parameter exact formula beyond such directly forced cases and, especially, the complete classification and exact counts of all minimum sets, including the two exceptional cycle-fiber families. These facts are not implied by the cited scalar results.

## Limitations
The formulas require \(m,n\ge3\), the ordinary undirected Cartesian product, and the 1-limited (capacity-one) condition. They do not enumerate nonminimum dominating sets and do not determine values for other capacities or arbitrary Cartesian products. Independent mathematical audit has not been performed; historical priority remains subject to literature not yet located or accessible.

## References
[1] D. Božović, G. Radić, Ž. Kovijanić-Vukićević and A. Tepeh, *On \(k\)-limited domination in graphs*, arXiv:2606.22422, first posted 2026-06-21; Computational and Applied Mathematics, DOI:10.1007/s40314-026-03902-2.

[2] A. Tepeh, *On \(k\)-limited domination: complexity and Cartesian products*, arXiv:2606.22428, first posted 2026-06-21, MSC 05C69.

[3] G. Radić, *An improved lower and upper bound of the \(k\)-limited domination number*, arXiv:2610.01442, first posted 2026-10-01 (related general bounds; abstract consulted).
