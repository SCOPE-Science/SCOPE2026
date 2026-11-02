# Endpoint probes create the first online-shattering gain for two-east-step lattice paths

## Finding
For each integer \(b\ge1\), let \(\mathcal P_b\) be the complete family of northeast lattice paths from \((0,0)\) to \((2,b)\), with two east steps and \(b\) north steps. A hypothesis is the set of vertices visited by one path; the Boolean label of query vertex \(q\) is one exactly when the path visits \(q\). Let \(\mathcal P_b^{\mathrm{mid}}\) use the same hypotheses but permit only queries in column one.

The two classes have VC dimension one at \(b=1\) and **VC dimension exactly two for every \(b\ge2\)**. Their Littlestone dimensions (full, middle-only) for \(b=1,\ldots,10\) are, respectively,
\[
(1,2,3,3,4,4,4,5,5,6),\qquad
(1,2,3,3,4,4,4,5,5,5).
\]
Consequently the first strict gain from adding queries in columns zero and two occurs at \(b=10\): full online shattering has depth six whereas middle-only online shattering has depth five, without any VC-dimension gain. At \(b=7\), the full class first fails to attain its hypothesis-count upper bound, having Littlestone dimension four instead of five.

For all \(b\ge1\), writing \(t=\lfloor b/2\rfloor\), one also has
\[
\lfloor\log_2(t+1)\rfloor+\lfloor\log_2(b-t+1)\rfloor
\le\operatorname{Ldim}(\mathcal P_b)
\le\left\lfloor\log_2\binom{b+2}{2}\right\rfloor.
\]
In particular, \(\operatorname{Ldim}(\mathcal P_b)=2\log_2 b+O(1)\), while its VC dimension remains two. The lower bound and finite exact classifications concern different statements; the finite table is not extrapolated to larger \(b\).

## Assumptions and scope
A path visits both endpoints. The universe of allowed query vertices is \(\{0,1,2\}\times\{0,\ldots,b\}\) for the full language and \(\{1\}\times\{0,\ldots,b\}\) for the middle-only language. Both languages retain all \(\binom{b+2}{2}\) hypotheses. Repeated or constant queries cannot help shatter. VC shattering requires all label patterns on a *fixed* support, whereas Littlestone shattering permits separate queries on each adaptive decision-tree branch.

Each path has unique first and second east-step heights \(0\le u\le v\le b\). The exact vertex-label predicate is
\[
\mathbf 1_{(0,y)}(u,v)=[y\le u],\quad
\mathbf 1_{(1,y)}(u,v)=[u\le y\le v],\quad
\mathbf 1_{(2,y)}(u,v)=[v\le y].
\]
Thus middle-column queries are nonempty interval-incidence queries, while outer-column queries reveal endpoint thresholds. Empty intervals are not included.

## Proof
**Hypothesis count and VC dimension.** The weakly increasing pairs \((u,v)\) number \(\binom{b+2}{2}\). For \(b\ge2\), queries \((0,1)\) and \((1,1)\) realize, respectively, the four binary traces \((1,1),(1,0),(0,1),(0,0)\) using pairs \((1,1),(2,2),(0,1),(0,0)\). The middle-only supports \((1,0),(1,1)\) are shattered for \(b\ge2\) using intervals \([0,0],[1,1],[0,1],[2,2]\). At \(b=1\), three hypotheses preclude two-dimensional shattering and a nonconstant query gives dimension one.

No three vertices are shattered by the full language. If all three can lie on one monotone path, put them in visiting order \(q_1,q_2,q_3\), so both coordinates are nondecreasing. If two lie in the same outer column, their membership events are nested, preventing even their pair from being shattered. If all three lie in the middle column, interval convexity excludes the pattern \((1,0,1)\). If two lie in the middle and the remaining one is in the left column, the pattern \((0,0,1)\) is impossible because absence of the left-column vertex together with presence of the later middle vertex forces presence of the earlier middle vertex. If the remaining one lies in the right column, the reflected implication excludes \((1,0,0)\). Finally, when the three queries occupy columns zero, one and two, respectively, two negative outer labels force the middle label to be positive, excluding \((0,0,0)\). If no path contains all three points the all-positive pattern is itself absent. This proves the upper bound. Because restricting the query language cannot raise VC dimension, the middle-only upper bound follows too.

**Uniform online lower bound.** Fix \(t\in\{0,\ldots,b\}\) and restrict to pairs \(0\le u\le t\le v\le b\). The two parameters independently range over sets of sizes \(t+1\) and \(b-t+1\). Column-zero queries compare \(u\) to a threshold; column-two queries compare \(v\) to a threshold. A set of \(m\) ordered hypotheses distinguished by threshold queries has Littlestone dimension \(\lfloor\log_2m\rfloor\): repeated midpoint splitting proves the lower bound and distinct terminal witnesses prove the upper bound. Stacking optimal threshold trees for \(u\) and \(v\) gives the displayed sum. The hypothesis-count bound follows because a shattered depth-\(d\) tree requires \(2^d\) different hypotheses. Choosing \(t=\lfloor b/2\rfloor\) gives both asymptotic bounds.

**Exact finite recurrence and complete certificate.** For any finite version space \(V\) of endpoint pairs, and query \(q\), let \(V_q^+\) and \(V_q^-\) be its two subsets. Define \(L(V)=0\) when no query splits \(V\); otherwise
\[
L(V)=\max_{q:\;V_q^+,V_q^-\ne\varnothing}\bigl(1+\min\{L(V_q^+),L(V_q^-)\}\bigr).
\]
The verifier enumerates *all* pairs, all query cuts and all reachable version spaces, memoizing by an exact integer bit mask. It uses this recurrence separately for the full and middle-only languages for every \(b\le10\). An independent path generator lists east-step positions rather than relying on endpoint-pair predicates and recomputes the full ranks. The supplied `depth6_tree.json` has 63 query nodes and 64 terminal pairs. Every terminal pair satisfies all six query answers along its path, and all 64 terminal pairs are distinct, proving the full depth-six lower bound at \(b=10\). The hypothesis-count bound \(\lfloor\log_2 66\rfloor=6\) matches it.

**Direct upper check for the exceptional middle-only value.** At \(b=10\), a query at height \(y\) has \((y+1)(11-y)\) positive intervals out of 66. A depth-six tree would require at least 32 concepts on both sides, hence its first query must have \(y\in\{3,4,5,6,7\}\). For \(y=4,5,6\), the positive version space is a Cartesian rectangle of endpoint thresholds of respective sizes \(5\times7\), \(6\times6\), or \(7\times5\). Middle-column membership queries on this rectangle split into either endpoint-threshold queries, so the dimension is \(\lfloor\log_2a\rfloor+\lfloor\log_2c\rfloor=4\), insufficient for a depth-five child. At \(y=3\) (and symmetrically \(y=7\)), the negative version space is a disjoint union of 6 intervals on three left points and 28 intervals on seven right points. To support a depth-five subtree, its first query would need a positive branch with at least 16 intervals. Only the central point of the seven-point block meets this requirement, with exactly 16 positives. Its negative branch consists of three disjoint three-point interval families (six intervals each). Every middle point query has at most four positives there, precluding a depth-four subtree. This rules out depth six in the middle-only language. The finite recurrence supplies a depth-five witness, establishing equality.

## Verification
Run `python verify_lattice_paths.py` next to `depth6_tree.json` with a standard Python 3 interpreter. The script checks all \(b=1,\ldots,10\), recomputes all full-language ranks from an independently generated path-incidence family, tests all VC supports of size at most three through \(b=6\), and checks the full depth-six decision-tree certificate at \(b=10\). Expected final line: `ALL_TWO_EAST_STEP_PATH_CHECKS_PASS`. The exact finite recurrence is exhaustive; the asymptotic theorem and universal VC statement use the mathematical arguments above.

## Relationship to prior work
Bhaskar's *Thicket Density* (arXiv:1702.03956) and Walker's *Tree Dimension and the Sauer–Shelah Dichotomy* (arXiv:2203.12211) provide the general language of adaptive shattering; neither of their inspected introductory statements establishes this particular three-column path-incidence classification. Chase, Freitag and Reyzin (arXiv:2310.04812) study applications to equivalence-query learning and compression rather than this exact vertex-membership instance. Janardhanan and Reyzin (arXiv:2002.11541) consider learning a hidden directed graph using reachability/path queries, not learning a hidden lattice path from vertex-incidence queries. The interval-membership middle-column system is a familiar reformulation; the finite *endpoint-query gain* and its first exact threshold are the specific contributions examined here.

## Limitations
The proof classifies full VC dimension for every \(b\) and gives two-sided Littlestone estimates for every \(b\), but does **not** give a closed formula for Littlestone dimension at arbitrary \(b>10\). Exact finite Littlestone values and the first endpoint-query gain are certified only for \(b\le10\). Exhaustive finite computation is not a proof about larger values. The literature comparison is not a guarantee of historical priority under other terminology, and independent validation has not been performed. Vertex-incidence queries should not be confused with edge membership or queries that inspect a whole path.

## References
- S. Bhaskar, *Thicket Density*, initial preprint 2017-02-13, https://arxiv.org/abs/1702.03956 .
- R. Walker, *Tree Dimension and the Sauer–Shelah Dichotomy*, initial preprint 2022-03-23, https://arxiv.org/abs/2203.12211 .
- H. Chase, J. Freitag, L. Reyzin, *Applications of Littlestone dimension to query learning and to compression*, initial preprint 2023-10-07, https://arxiv.org/abs/2310.04812 .
- M. V. Janardhanan, L. Reyzin, *On Learning a Hidden Directed Graph with Path Queries*, initial preprint 2020-02-26, https://arxiv.org/abs/2002.11541 .
