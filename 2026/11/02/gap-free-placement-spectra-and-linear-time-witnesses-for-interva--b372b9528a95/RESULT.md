# Gap-free placement spectra and linear-time witnesses for interval-approved housing on degree-two networks

## Finding

**Theorem (exact size spectrum and constructive complexity).** Let \(G=(V,E)\) be a finite simple undirected graph of maximum degree at most two. A subset \(I\subseteq V\) contains fixed incumbent inhabitants and \(U=V\setminus I\) is the set of candidate homes. Every \(h\in I\) approves a nonempty interval of integer refugee-neighbor counts \([\ell_h,u_h]\), with \(0\le\ell_h\le u_h\le |N_G(h)\cap U|\). Set

\[
\mathcal F=\{S\subseteq U:\ell_h\le |S\cap N_G(h)|\le u_h\ \text{for every }h\in I\}.
\]

If \(\mathcal F\ne\varnothing\), write \(L=\min_{S\in\mathcal F}|S|\) and \(H=\max_{S\in\mathcal F}|S|\). Then

\[
\{|S|:S\in\mathcal F\}=\{L,L+1,\ldots,H\}.
\]

There is a deterministic \(O(|V|+|E|)\)-time algorithm which determines if \(\mathcal F\) is empty, computes \(L,H\) when nonempty, and returns an explicit feasible set of *every* requested size \(k\in[L,H]\), rejecting requests outside this interval. A stronger exchange property holds: for any two feasible sets \(A,B\), there is a sequence of feasible sets from \(A\) to \(B\) whose successive cardinalities differ by at most one; the sets in the sequence need not differ at only one site.

**Sharp structural boundary.** The gap-free conclusion fails already on a tree of maximum degree three with seven vertices and three exact-one incumbent approvals: its feasible placement sizes are precisely \(\{1,3\}\).

## Assumptions and scope

The occupants of the candidate homes are indistinguishable, have no individual preferences, and each home holds at most one. Inhabitants remain fixed. The approval interval concerns the number of newly placed occupants in the *open* neighborhood; permanently occupied neighboring houses do not count. The case \(I=\varnothing\), isolated candidate sites, empty components and \(k=0\) are included. A resident with zero candidate neighbors necessarily approves zero by the displayed interval assumption. Inputs are adjacency lists and one pair of interval endpoints per inhabitant. All bounds count elementary RAM operations on indices and integers bounded by \(|V|\).

The proof also applies verbatim to a binary constraint system in which each variable appears in at most two constraints, and every constraint tests whether the sum of at most two distinct binary variables belongs to an integer interval. This is a strictly local reformulation; it does **not** assert the claim for arbitrary binary CSPs or higher-degree networks.

## Proof

**1. Reduction to a path/cycle constraint graph.** Write \(x_v\in\{0,1\}\) for occupancy of each \(v\in U\). Inhabitant \(h\) restricts a sum of zero, one or two such variables. Zero-variable constraints are checked immediately; one-variable constraints restrict the allowed state of that variable. For two-variable constraints on the same unordered pair, intersect their approval intervals; an empty intersection is infeasible. Make a graph \(P\) on the candidate variables, joining two variables precisely when they appear together in a remaining two-variable constraint. Each candidate appears in at most two inhabitant-neighborhoods because \(\deg_G(v)\le2\), so \(P\) is a union of isolated vertices, paths and cycles. This reduction requires linear time.

**2. Cardinality extrema in linear time.** For each path component ordered \(v_1,\ldots,v_s\), the usual two-state dynamic program stores the minimum (respectively maximum) number of occupied sites in its processed prefix, conditional on the last state being zero or one. The transition checks the unary restriction at \(v_j\) and whether the two consecutive states have sum in their pair interval. It takes constant time per vertex. On a cyclic component, try both states of the first vertex and finally test the wrap-around pair constraint, retaining the best of two constant-state computations. Backpointers recover optimizing assignments. Separate components optimize independently; their concatenation gives feasible extrema \(x\) and \(y\) of cardinalities \(L\) and \(H\). If any component is infeasible, \(\mathcal F\) is empty.

**3. A switching implication system.** In fact take *any* feasible assignments \(x,y\in\{0,1\}^{U}\). Put \(D=\{v:x_v\ne y_v\}\), and for \(v\in D\), let \(t_v=0\) mean retaining \(x_v\) and \(t_v=1\) mean adopting \(y_v\). Assignments at sites outside \(D\) remain fixed.

A unary constraint is automatically satisfied at either endpoint. In a two-site constraint on \(a,b\), if only one site changes, either choice is an endpoint of a feasible assignment. If both change in the same direction, the endpoint sums differ by two and the interval necessarily includes the intermediate sum, so both mixed choices are feasible. In the remaining case the signs \(y_a-x_a\) and \(y_b-x_b\) are opposite and both endpoint sums equal one. The only potentially disallowed mixed states are \((t_a,t_b)=(1,0)\) and \((0,1)\). If \(y_a+x_b\) is outside the approved interval, impose the directed implication \(t_a=1\Rightarrow t_b=1\); if \(x_a+y_b\) is outside it, impose \(t_b=1\Rightarrow t_a=1\). If a mixed state is accepted, omit its implication.

Consequently a switched assignment satisfies **every** constraint if and only if the set \(\{v\in D:t_v=1\}\) is closed under the arcs of the resulting directed graph \(Q\). The underlying undirected graph of \(Q\) is a subgraph of \(P\), so has maximum degree two, and every arc joins sites whose differences \(y_v-x_v\) have opposite signs.

**4. Small net jumps for strongly connected blocks.** Each strongly connected component \(C\) of \(Q\) is a connected path or cycle in its underlying undirected graph (singletons included). Because every edge joins opposite signs, the \(+1\) and \(-1\) signs alternate along a path; therefore

\[
\left|\sum_{v\in C}(y_v-x_v)\right|\le1.
\]

If the component is a cycle, alternation makes its length even, with the same sum equal to zero. The statement also holds for a singleton.

**5. Gap-free interpolation and explicit construction.** Contract the strongly connected components of \(Q\), forming its acyclic condensation. Activate entire components in **reverse** topological order: whenever \(C\to C'\) is an implication, \(C'\) is activated before \(C\). The set of activated sites is thus closed under implications after every activation. The successive occupancy vectors are feasible, start at \(x\), end at \(y\), and have cardinality jumps of absolute value at most one by step 4. A finite integer walk from \(|x|\) to \(|y|\), with all steps in \(\{-1,0,1\}\), visits every integer between its endpoints, regardless of monotonicity. Taking \(x\) and \(y\) from step 2 proves the displayed complete interval of sizes. To construct a specified size \(k\), stop at its first visit, and output the activated configuration. Building \(Q\), its strongly connected components, a topological order and the output requires \(O(|V|+|E|)\) time altogether.

**6. Degree-three obstruction.** Take four candidate homes \(c,a,b,d\) and three distinct incumbent homes \(h_a,h_b,h_d\). Join \(h_z\) only to \(c\) and \(z\), for \(z\in\{a,b,d\}\), and require exactly one newly occupied neighbor for each incumbent. The underlying seven-vertex topology is the subdivision of a three-leaf star, so its unique degree-three vertex is \(c\). The three constraints are \(x_c+x_z=1\). If \(x_c=1\), then \(x_a=x_b=x_d=0\), giving size one. If \(x_c=0\), all leaves are occupied, giving size three. Both assignments are feasible; none of size two exists. This establishes failure upon relaxing the maximum-degree-two hypothesis without asserting a minimum obstruction order.

## Verification

Run the standalone dependency-free script `python3 verify.py`. It implements both stages of the algorithm, independently enumerates all binary assignments for small instances, and compares every requested placement size and witness against exhaustive truth. Its checks include 10,843 path/cycle systems with every possible pair interval on up to five candidate sites, 1,150 randomly generated valid-incidence systems with unary restrictions, the degree-three gap witness, and an explicit construction with 10,000 candidate sites. All these checks succeeded. The script performs finite tests; the theorem for all graph sizes follows from steps 1–6, not from enumeration or timing experiments.

## Relationship to prior work

Knop and Schierreich, *Host Community Respecting Refugee Housing* (first arXiv version 2023-02-27), introduced anonymous inhabitant-respecting placement with arbitrary approval sets and proved polynomial-time solvability on maximum-degree-two topologies. Their construction uses an exact-cardinality dynamic-programming dimension, and the path case has a quadratic table; it does not state the gap-free cardinality spectrum or the present linear-time construction for all intervals. Schierreich, *Towards More Realistic Models for Refugee Integration: Anonymous Refugee Housing with Upper-Bounds* (first arXiv version 2023-08-18), proved linear-time solvability on maximum-degree-two topologies for **upper-bound-only** approvals \([0,u_h]\). In that subcase feasible sets are closed under deletion, making the absence of cardinality gaps immediate; the present result permits strictly positive and heterogeneous lower bounds, where this monotonicity is unavailable. Both papers also document degree-three hardness phenomena, logically different from the explicit three-arm size-spectrum obstruction here.

The contribution is the interval-specific exchange theorem and constructive linear-time arbitrary-cardinality algorithm, not the original problem definition, the ordinary constant-state path dynamic programming for minima/maxima, or any assertion that search alone establishes novelty.

## Limitations

The theorem assumes each local approval set is a single integer interval. Disconnected approval sets, residents with three or more candidate neighbors, candidate sites constrained by three or more residents, heterogeneous agent identities or additional global quotas are outside its guarantee. The interpolation may flip several sites simultaneously in one block, and does not prove existence of a sequence of valid **single-site** changes. No claim of minimum-size degree-three obstruction is made. Equivalent interval-binary-CSP results under other terminology may exist despite comparison with the cited primary sources.

## References

1. Dušan Knop and Šimon Schierreich, *Host Community Respecting Refugee Housing*, arXiv:2302.13997, first posted 2023-02-27. https://arxiv.org/abs/2302.13997. Consulted complete arXiv HTML text, especially Section 3 and the degree-two algorithm.
2. Šimon Schierreich, *Towards More Realistic Models for Refugee Integration: Anonymous Refugee Housing with Upper-Bounds*, arXiv:2308.09501, first posted 2023-08-18. https://arxiv.org/abs/2308.09501. Consulted complete arXiv HTML text, especially Sections 3–4 and the upper-bound degree-two theorem.
