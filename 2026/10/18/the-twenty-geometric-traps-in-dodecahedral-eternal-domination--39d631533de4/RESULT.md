# The twenty geometric traps in dodecahedral eternal domination

## Finding

Let \(D=\operatorname{GP}(10,2)\) be the twenty-vertex dodecahedral graph. In the standard all-guards-move, collision-free eternal-domination game, the domination number is \(\gamma(D)=6\) and the eternal-domination number is
\[
\gamma_m^\infty(D)=7.
\]
There are precisely ten dominating six-vertex configurations; each has exactly two unoccupied vertices whose attack cannot be answered even once. There are precisely \(780\) dominating seven-vertex configurations, of which precisely \(760\) defend against **every infinite attack sequence**. The other twenty are classified geometrically.

For \(x\in V(D)\), let \(S_j(x)=\{v\in V(D):d_D(x,v)=j\}\) be the distance-\(j\) sphere. The twenty nondefensible seven-guard configurations are exactly
\[
B_x=S_1(x)\cup S_4(x)\cup S_5(x),\qquad x\in V(D).
\]
Each \(B_x\) has seven vertices, dominates \(D\), and has exactly one fatal attack, at \(x\). No other seven-guard dominating configuration has any fatal attack: for every unoccupied attacked vertex, at least \(26\) different legal moves lead to another one of the same \(760\) defensible configurations. The lower bound \(26\) is attained.

## Assumptions and scope

Use vertices \(u_i=i\) and \(v_i=10+i\), for \(i\in\mathbb Z/10\mathbb Z\), with undirected edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\) for every \(i\). This is a fixed labelled copy of the graph \(D\). All guard sets are subsets of distinct vertices. A legal attacked vertex is unoccupied.

A guard placement \(A\) is *dominating* if every vertex belongs to \(A\) or is adjacent to some vertex of \(A\). A legal simultaneous move from \(A\) to \(B\) requires a bijection \(f:A\to B\) with \(f(a)=a\) or \(af(a)\in E(D)\) for every \(a\in A\); an attack at \(x\notin A\) is answered only if \(x\in B\) and \(B\) is dominating. The defender chooses a dominating starting placement and responds forever to adversarial sequential attacks. No two guards may share a vertex. The theorem concerns this game, this graph and guard numbers at most seven, without claims for larger guards, other graphs or other movement conventions.

## Proof

**Movement lemma.** For two equal-cardinality placements \(A,B\), form a bipartite graph with left vertices \(A\), right vertices \(B\), and edge \((a,b)\) whenever \(a=b\) or \(ab\in E(D)\). A collision-free simultaneous move exists exactly when this bipartite graph has a perfect matching. Indeed, a perfect matching assigns each initial guard a distinct legal destination, and every legal move yields such an assignment. Since an attacked vertex \(x\) is not initially occupied, the condition \(x\in B\) forces some guard to enter it across an edge.

**Finite exhaustive step.** Enumerate every subset of each size from one to seven in the twenty-vertex graph; a set is dominating exactly if the union of the closed neighborhoods of its vertices is all of \(V(D)\). There are no dominating sets of size at most five, exactly ten of size six, and exactly \(780\) of size seven. For each six-set \(A\), exhaust all dominating six-set targets \(B\) passing the movement lemma, take their union, and subtract it together with the occupied set from \(V(D)\). Exactly two unoccupied vertices remain; either one is an attack to which no legal response exists. Therefore six guards cannot win, and fewer than six cannot even dominate.

Repeat at size seven. Exactly twenty dominating seven-sets have a nonempty set of unanswerable attacks, and each has exactly one such attack. Breadth-first search on the given graph produces, from every vertex \(x\), the sphere-size profile
\[
\bigl(|S_0(x)|,\ldots,|S_5(x)|\bigr)=(1,3,6,6,3,1).
\]
The explicit twenty sets \(B_x=S_1(x)\cup S_4(x)\cup S_5(x)\) are pairwise distinct, and the independently checked exhaustive list of the twenty failing seven-sets agrees with them exactly, including the identification of each unique fatal attack \(x\).

Let \(\mathcal W\) comprise the remaining \(760\) dominating seven-sets. Exhausting each equal-size target by the movement lemma shows that for every \(A\in\mathcal W\) and every \(x\notin A\), at least \(26\) destinations \(B\in\mathcal W\) both contain \(x\) and admit a legal simultaneous move from \(A\). The minimum of these \(760\cdot13=9880\) positive counts is exactly \(26\). Thus \(\mathcal W\) is closed under responses to all attacks. By induction on the number of attacks, every \(A\in\mathcal W\) admits defense forever. Conversely, each \(B_x\) loses against the immediate attack at \(x\). This proves the claimed classification and \(\gamma_m^\infty(D)=7\).

All enumerations and matching tests in this proof are finite, fully specified by the algorithms and the certificate in the accompanying files. The direct Python generator enumerates injective individual moves, while the separate C++ implementation enumerates pairs of dominating placements and decides their adjacency via augmenting-path bipartite matching. The latter independently checks complete move reachability, not merely supplied witnesses. They agree on the cardinalities, fatal attacks, sphere classification and minimum response count. The certificate includes, for every one of the \(9880\) possible attacks from a winning placement, one explicitly checked winning destination.

## Verification

Run `python3 generate_certificate.py certificate.json`, compile `matching_recompute.cpp` with `g++ -std=c++17 -O2 -Wall -Wextra -pedantic matching_recompute.cpp -o matching_recompute`, then run `./matching_recompute > matching_recompute_output.txt`. Finally run `python3 check_certificate.py certificate.json matching_recompute_output.txt`. The generator needs only the Python standard library; the other programs need a C++17 compiler and the Python standard library. Recorded output files permit comparison against the reproduced output.

The deterministic `certificate.json` contains the exact twenty-vertex edge list, all six- and seven-guard dominating masks, the fatal attacks at six and seven guards, and the selected all-attacks winning response table at seven guards. Bit \(i\) of an integer mask corresponds to labelled vertex \(i\). The direct generator produces a certificate of \(117503\) bytes with SHA-256 `8ce3213814565ac2cf419def755809fb0d6915876e4c17262214d7a84ae9f162`; the checker verifies \(9880\) response witnesses independently, and the C++ exhaustive pairwise matching search verifies the full finite complement of possible responses.

## Relationship to prior work

Klostermeyer and Mynhardt (first public arXiv version 2014-07-20) describe the all-guards-move model and general bounds, but do not classify its configurations for the dodecahedral graph. Shaheen and Kassem (2021) study the generalized Petersen graphs \(\operatorname{GP}(n,2)\) and construct seven-guard defenses for the case \(n=10\), via their two-block strategy. That previously known sufficient guard budget is not represented as a new construction here. Their relevant theorem concerns an upper bound and chosen strategic configurations; it does not give the complete \(780\)-configuration decision, the twenty distance-sphere traps, or the sharp minimum number of safe responses. The 2019 public benchmark page of Braga, de Souza, and Lee concerns random graph instances and does not contain this exact named-graph safety region.

## Limitations

The result is a finite exhaustive theorem about a single labelled graph. Its classification is invariant under relabelling, but it does not establish a formula for general generalized Petersen graphs. The finite certificate and two algorithms give repeatable exact checks, not a formal proof in an interactive prover. Publication originality is a best-knowledge comparison, not a claim of global uniqueness or an independent external audit. Some unindexed research, source-code repositories and supplementary material may contain an equivalent calculation.

## References

1. W. F. Klostermeyer and C. M. Mynhardt, *Domination, Eternal Domination, and Clique Covering*, arXiv:1407.5235 (first posted 2014-07-20), https://arxiv.org/abs/1407.5235.
2. R. Shaheen and A. Kassem, *Eternal Domination of Generalized Petersen Graph*, Journal of Applied Mathematics (first published 2021-01-27), DOI:10.1155/2021/6627272, https://onlinelibrary.wiley.com/doi/10.1155/2021/6627272.
3. A. Braga, C. C. de Souza, and O. Lee, *Eternal Dominating Set Problem — Benchmark Instances* (2019), https://www.ic.unicamp.br/~cid/Problem-instances/Eternal-Dominating-Set/.
