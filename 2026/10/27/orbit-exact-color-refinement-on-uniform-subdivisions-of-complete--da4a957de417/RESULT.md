# Orbit-exact color refinement on uniform subdivisions of complete graphs

## Finding
For every integer \(n\ge4\), every integer \(L\ge2\), and **every** set \(S\) of individually colored vertices of the graph \(G_{n,L}\) obtained by replacing each edge of \(K_n\) with a path of exactly \(L\) edges, synchronous one-dimensional counting color refinement reaches precisely the orbits of the pointwise stabilizer \(\operatorname{Aut}(G_{n,L})_{(S)}\). All remaining vertices initially have the same color. The orbit partition is obtained in at most \(2L-2\) refinement rounds, independent of \(n\) and the number and placement of marks.

There is an exact closed classification. Let \(M\) be the graph on the \(n\) original branch vertices whose edges are those subdivided paths with at least one marked interior vertex. Call an edge of \(M\) *free central* if its component in \(M\) consists of just this edge, its unique marked interior vertex is the midpoint of the path (thus \(L\) is even), and neither endpoint branch vertex is marked. Let \(p\) be the number of free-central edges. Let \(u\) be the number of unmarked branch vertices incident with no edge of \(M\), and put \(f=n-2p-u\). Define
\[
q=f+p+\mathbf1_{u>0},\qquad h=p+\mathbf1_{u\ge2}.
\]
The number of stable color classes is exactly
\[
\boxed{q+(L-1)\binom q2+\left\lfloor\frac L2\right\rfloor h.}
\]
Their sizes are explicitly given in the proof. In particular the count depends on the individualized vertices only through \(p,u,n,L\).

## Assumptions and scope
Vertices are the original branch vertices \(B=\{1,\ldots,n\}\) and the interior vertices \(v_{ab,t}\), with \(\{a,b\}\in\binom B2\) and \(1\le t\le L-1\), where \(t\) is the distance along the designated path from \(a\). All graphs are finite, simple, undirected, and unweighted. The markers form an arbitrary subset \(S\subseteq V(G_{n,L})\), including the empty set, and are assigned pairwise distinct colors not used elsewhere. The synchronous recursion retains the current color and appends the multiset of neighbor colors at each round. Rounds are numbered starting at zero for the initial marking. The asserted bound is a uniform upper bound, not a general assertion of optimality.

## Proof
**1. Automorphisms and marked-support components.** Branch vertices are precisely those of degree \(n-1>2\); every other vertex has degree two. Therefore automorphisms preserve \(B\). Each unordered pair of branches is joined by a unique internally degree-two path of length \(L\), so an automorphism is uniquely determined by its induced permutation of \(B\), and all permutations occur. Hence \(\operatorname{Aut}(G_{n,L})\cong S_n\).

A marked branch vertex fixes its branch label. A marked path vertex \(v_{ab,t}\) forces the branch pair \(\{a,b\}\) to be preserved. If \(t\ne L-t\), it fixes \(a\) and \(b\) separately; if \(t=L/2\), it allows their interchange. When two distinct marked-support edges share a branch vertex, their distinct preserved endpoint pairs determine that common branch vertex uniquely, and then both other endpoints, and by connectivity every vertex of that component. An isolated marked-support edge is likewise fixed endpointwise if it has an off-center mark or a separately marked branch endpoint. Exactly the free-central edges admit independent endpoint flips. All branch vertices outside the support and not directly marked can be permuted arbitrarily. Consequently
\[
\operatorname{Aut}(G_{n,L})_{(S)}\cong C_2^{\,p}\times S_u,
\]
acting on \(B\) as \(f\) fixed singletons, \(p\) independently flippable pairs, and one size-\(u\) symmetric block when \(u>0\). Its branch orbit count is \(q\).

**2. Branch orbits are visible by round \(L-1\).** For a marked branch \(s\), its distance to a branch \(a\) equals zero if \(a=s\) and \(L\) otherwise. For a marked internal vertex \(s=v_{ab,t}\), the distances from branches are
\[
\operatorname{dist}(x,s)=\begin{cases}
t,&x=a,\\L-t,&x=b,\\L+\min(t,L-t),&x\notin\{a,b\}.
\end{cases}
\]
Thus distances **less than \(L\)** from all individually marked vertices distinguish marked branch points, endpoints of oriented marked paths, and incident marked-support edges; the only equal branch distance signatures are the free-central pairs and the unused size-\(u\) block. These are exactly the branch orbits established in Step 1.

For clarity, color refinement with an initially singleton-colored marker \(s\) determines, at round \(r\), whether \(\operatorname{dist}(x,s)\) equals each integer up to \(r\), or is larger; induction uses the neighbor multiset together with the previous color. At round one, the branch vertices are also distinguishable from path interiors by their different degrees. At round \(L-1\), colors therefore separate every distinct branch orbit. Colors never separate members of the same automorphism orbit, so the branch color classes are exactly those branch orbits.

**3. Interior orbits are visible within another \(L-1\) rounds.** Starting from any round at which a set \(C\) is a full color class, after \(r\) additional refinement rounds the color of a vertex determines its distance from \(C\), truncated at \(r\); this is the same neighbor-multiset induction applied to the predicate of membership in \(C\). Apply it to each branch orbit \(C\) at round \(L-1\).

If an interior vertex lies at path position \(t\) between endpoints in **different** branch orbit classes \(A,B\), its distances to these classes are precisely \(t,L-t<L\), whereas the distances to all other branch classes exceed \(L\). The pair \((A,B)\) together with the position measured from \(A\) identifies its full stabilizer orbit. If both endpoints belong to the **same** branch orbit class \(A\), the only branch class within distance less than \(L\) is \(A\), and the distance to it is \(\min(t,L-t)\). By Step 1, this folded distance again determines its full orbit: the stabilizer acts transitively on unordered pairs within each nonsingleton branch orbit, namely an isolated flippable pair or the unused symmetric block. Distances to the branch classes less than \(L\) are all available by round \((L-1)+(L-1)=2L-2\). Hence every full-graph orbit is a color class by this round. Since orbits are equitable and refinements are automorphism invariant, this is the stable partition.

**4. Exact counts and sizes.** The branch class sizes are a multiset of \(f\) ones, \(p\) twos, and (if \(u>0\)) one entry \(u\). For two distinct branch classes of sizes \(a,b\), each of the \(L-1\) relative positions gives one orbit of size \(ab\). For a single branch class of size \(a\ge2\), the internal positions are identified under reflection: for every integer \(j\) with \(1\le j\le\lfloor L/2\rfloor\), the orbit size is \(2\binom a2\) when \(2j<L\), and \(\binom a2\) when \(2j=L\). Singleton branch classes have no internal paths with both endpoints in the class. Only the \(p\) flippable pairs and, if \(u\ge2\), the unused symmetric block contribute these within-class path orbits. Summing produces the displayed class-count formula and every class size. These sizes sum to \(n+(L-1)\binom n2\), the vertex count, as required. \(\square\)

## Verification
The included standalone `verify.py` explicitly constructs the graph, executes synchronous refinement from arbitrary sets of uniquely marked vertices, and independently enumerates the \(n!\) induced branch permutations to obtain the pointwise stabilizer orbits. It also compares the formula for the total number and complete multiset of orbit sizes, checks the stabilizer order \(2^p u!\), and checks the depth upper bound \(2L-2\).

There were \(12,424\) tested configurations across \((n,L)=(4,2),(4,3),(4,4),(4,5),(5,2),(5,3),(5,4),(6,2),(6,3)\). All \(2^{10}=1,024\) marked subsets were exhausted for \((4,2)\); other cases were deterministically sampled from seeded pseudorandom subsets, including the empty mark set when sampled. All tests passed. The maximum observed depth over the tested examples was \(2L-2\) in each tested family. This experimental observation is not asserted as an all-parameter lower bound.

Run with `python3 verify.py`. No packages beyond the Python standard library are needed. The universal theorem is proved in the preceding steps, not inferred from finite tests.

## Relationship to prior work
Arvind, Köbler, Rattan, and Verbitsky (arXiv:1502.01255, originally public 2015-02-04), Appendix 0.A.2, prove that the Johnson graph \(J(n,2)\), the line graph of \(K_n\), is Tinhofer under arbitrary individualizations of its **edge-vertices**; their argument analyzes pointwise edge stabilizers. This is related to Step 1, but neither their statement nor their proof gives the present subdivided-graph classification, simultaneous marking of original branch and arbitrary path-interior vertices, or its \(2L-2\) depth bound. The same article's general hierarchy concerns amenability, compactness, Tinhofer and refinability, without directly classifying uniform clique subdivisions.

Bhattacharjee, Panse, and Sarma (arXiv:2605.19702, 2026) give a general stabilizer-orbit characterization of Tinhofer graphs. This translates the question into the appropriate orbit criterion but does not itself establish that this particular family satisfies it. A separate indexed result on metric Rips complexes of the once-subdivided clique involves the same underlying graph only for \(L=2\), but asks a topological persistence question, rather than studying color refinement. Its full text was not available in the present comparison, so this last distinction is based on its title and summary only.

## Limitations
No claim is made for nonuniform edge lengths, arbitrary precolorings beyond pairwise-distinct singleton marks plus a common background color, or other base graphs. The upper bound is not proven sharp for every \(n,L\). The findings do not assert compactness, amenability, or an isomorphism algorithm against arbitrary nonisomorphic inputs. The searches and inspected papers do not establish exhaustive worldwide novelty; specialized unlocated treatments remain possible. Independent scientific validation has not been carried out.

## References
1. V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255 (version 1, 2015-02-04; version 3, 2015-05-04), especially Section 8 and Appendix 0.A.2. https://arxiv.org/abs/1502.01255
2. S. Bhattacharjee, A. Panse, J. Sarma, *A Hierarchy of Tinhofer Graphs: Separations and Membership Testing*, arXiv:2605.19702 (2026), especially Sections 2–3. https://arxiv.org/abs/2605.19702
