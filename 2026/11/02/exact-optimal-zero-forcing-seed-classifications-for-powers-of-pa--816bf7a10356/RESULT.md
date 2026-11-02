# Exact optimal zero-forcing seed classifications for powers of paths and cycles

## Finding

**Theorem.** Fix an integer \(k\ge 2\). For the labelled \(k\)-th power \(P_n^k\) of the path on \(n\ge k+2\) vertices, there are exactly \(2k\) minimum ordinary zero-forcing sets. All of them are
\[
S_{1,w}=\{v_1\}\cup\bigl(N(v_1)\setminus\{w\}\bigr),\quad w\in N(v_1),
\]
or their reflected counterparts
\[
S_{n,w}=\{v_n\}\cup\bigl(N(v_n)\setminus\{w\}\bigr),\quad w\in N(v_n).
\]
These form exactly \(k\) orbits of size two under reversal of the path. The coefficient of the minimum degree of its ordinary zero-forcing polynomial is therefore \(z(P_n^k;k)=2k\).

For the labelled \(k\)-th power \(C_n^k\) of a cycle on \(n\ge2k+3\) vertices, the minimum ordinary zero-forcing sets are exactly
\[
S_{v,w}=\{v\}\cup\bigl(N(v)\setminus\{w\}\bigr),\qquad w\in N(v).
\]
There are exactly
\[
z(C_n^k;2k)=n(2k-1)
\]
distinct such sets. Under the natural dihedral group, they split into one orbit of \(n\) consecutive blocks of \(2k\) vertices, and \(k-1\) orbits of size \(2n\), one for each omitted-neighbour cyclic distance \(d\in\{1,\ldots,k-1\}\).

The underlying minimum values \(Z(P_n^k)=k\) and \(Z(C_n^k)=2k\) were established previously; the statement above classifies and enumerates every optimizer.

## Assumptions and scope

All graphs are finite, simple, undirected and **labelled**. The vertices of \(P_n\) are \(v_1,\ldots,v_n\), and \(v_i\) and \(v_j\) are adjacent in \(P_n^k\) precisely when \(0<|i-j|\le k\). The vertices of \(C_n\) are residue classes modulo \(n\), and distinct vertices are adjacent in \(C_n^k\) when their cyclic distance is at most \(k\). The conditions \(n\ge k+2\) and \(n\ge2k+3\) exclude, respectively, a complete path power and the complete or nearly complete cycle-power boundaries.

An ordinary zero-forcing process begins with an initially black set \(S\); a **black** vertex with exactly one white neighbour may turn that neighbour black. A zero-forcing set is one for which iterative application can colour every vertex. Write \(Z(G)\) for the smallest size of such a set and \(z(G;j)\) for the number of distinct labelled zero-forcing sets of cardinality \(j\). In particular, all counting is of initial **subsets**, not forcing sequences or sets modulo automorphisms.

## Proof

**First-step lemma.** Let \(G\) have minimum degree \(\delta\), and suppose an initially black \(\delta\)-set can perform at least one force. If \(v\) is its first forcing vertex and \(w\) its unique white neighbour, then \(v\) has degree exactly \(\delta\), and the initial set is precisely \(\{v\}\cup(N(v)\setminus\{w\})\). Indeed, \(v\) and its \(\deg(v)-1\) black neighbours are distinct black vertices, whence \(\delta\ge \deg(v)\ge\delta\), forcing equality. The same observation shows \(Z(G)\ge\delta(G)\): no set of size less than the minimum degree can make even a first force.

**Path powers.** For \(n\ge k+2\), precisely the two endpoints of \(P_n^k\) have degree \(k\); every other vertex has degree at least \(k+1\). The first-step lemma therefore forces any successful \(k\)-set to be on the displayed list. Conversely, every displayed seed can force its one omitted neighbour at the endpoint. After that first force the initial \(k+1\) vertices of the path are black (or the final \(k+1\), symmetrically). To extend a black prefix ending at \(v_j\), where \(j\ge k+1\), use the black vertex \(v_{j-k+1}\): its only white neighbour is \(v_{j+1}\). Induction colours the whole path. Each endpoint gives \(k\) distinct seeds, and the two collections are disjoint because a left-end seed is contained in the first \(k+1\) vertices and contains \(v_1\) but not \(v_n\), whereas a right-end seed contains \(v_n\) but not \(v_1\). Reversal exchanges the two sets corresponding to each omitted-neighbour distance, yielding the \(k\) claimed two-element orbits.

**Cycle powers: candidate classification.** In \(C_n^k\) with \(n\ge2k+3\), every vertex has degree \(2k\). By the first-step lemma, every successful \(2k\)-set must be on the displayed list. Conversely, any such seed can force its omitted neighbour \(w\) from \(v\), after which the closed radius-\(k\) neighbourhood \(N[v]\) is black. It is a cyclic interval of \(2k+1\) consecutive vertices. If a cyclic interval of length at least \(2k+1\), but not yet all \(n\) vertices, is black, choose its vertex \(k-1\) positions to the left of its right endpoint; its single white neighbour is the next vertex to the right. The cyclic interval extends by one. This gives a complete forcing sequence and proves that the displayed candidates are precisely the minimum sets.

**Cycle powers: exact multiplicities.** Put \(L=2k+1\) and let \(I_v=N[v]\), a cyclic interval of length \(L\). Every ordered pair \((v,w)\) with \(w\in N(v)\) describes the \(2k\)-set \(I_v\setminus\{w\}\), giving \(2kn\) descriptions. If two distinct centres \(v,v'\) produce the same set, then \(|I_v\cap I_{v'}|\ge L-1\). Since \(n\ge L+2\), two distinct cyclic intervals of length \(L\) intersect in at least \(L-1\) vertices only when their starting points are cyclically adjacent. In that case their intersection is exactly the consecutive \(L-1\)-vertex block shared by both, and both deleted vertices are the respective unshared endpoints. Exactly \(n\) such blocks exist, each with two descriptions; all remaining descriptions are unique. No block has a third description because three distinct length-\(L\) cyclic intervals cannot share \(L-1\) vertices under \(n\ge L+2\). Subtracting the \(n\) duplicate descriptions gives \(2kn-n=n(2k-1)\) distinct sets.

The duplicated sets are precisely the \(n\) cyclically consecutive \(2k\)-blocks, constituting a single dihedral orbit. For each cyclic distance \(d\in\{1,\ldots,k-1\}\) there are \(2n\) descriptions omitting a neighbour at distance \(d\); these sets have unique descriptions, and rotation and reflection act transitively on them, yielding one orbit of size \(2n\) per \(d\). Different distances yield distinct orbits by the uniqueness of the centre–omitted-neighbour description. This completes the classification and count.

## Verification

The accompanying standalone standard-library Python program \(\texttt{verify.py}\) constructs the two graph families independently from their edge definitions, implements the black-vertex/unique-white-neighbour propagation rule, and checks all candidate sets. It exhaustively enumerates every set of the minimum cardinality for \(83\) parameter triples across both families, examining \(102073\) subsets, and agrees exactly with the structural classification and multiplicity formulas. An additional \(96\) parameter cases verify all constructed candidates, including near-complete cycle boundaries treated only as consistency tests. The recorded replay line is:

`VERIFY_OK exhaustive_cases=83 examined_minimum_cardinality_subsets=102073 additional_constructive_cases=96`

The exhaustive experiments cover finite parameter ranges only. The universal statement is proved by the first-step lemma, forcing extension, interval intersection and counting arguments above.

## Relationship to prior work

Abiad, Flagg, Ghasemi Nezhad and Zeijlemaker (arXiv:2610.03892, first submitted 2026-10-02) determine the minimum zero-forcing **numbers** of path and cycle powers. Their proof uses consecutive blocks to obtain upper bounds but does not state the complete set of optimizers, minimum coefficients or orbit counts. The present result takes their exact minima as motivation and supplies that missing optimizer classification.

Boyer and collaborators (arXiv:1801.08910) introduced the ordinary zero-forcing polynomial and count minimum sets in several familiar graph families. In particular, the power-one instances (ordinary paths and cycles) are already covered by their work; that is why the theorem states \(k\ge2\). Their generic coefficient results also imply isolated boundary cases in which the minimum set has size \(n-2\). For cycle powers of order \(2k+1\) or \(2k+2\), complete-graph and complete-multipartite formulas are known and are deliberately excluded from the main theorem: those dense boundary counts should **not** be regarded as novel. The minimum-rank/zero-forcing study by Chang and Lin likewise determines values for cycle powers, not this general optimum-set census. Work on **failed skew** zero forcing of path powers uses a different forcing rule and objective.

Meaning-based comparisons with accessible published mathematical findings did not locate an equivalent classification for the full noncomplete path-power and non-nearly-complete cycle-power families. Failure to locate one is not an exhaustive priority guarantee.

## Limitations

The result enumerates only minimum-cardinality ordinary zero-forcing sets. It does **not** supply the entire zero-forcing polynomial, classify all inclusion-minimal sets, establish a stronger result for arbitrary graph powers, or count inequivalent forcing sequences. The graph labels and natural path-reversal/dihedral actions are fixed. Familiar boundary cases and the minimum **numbers** are previously known. An older general theorem for neighbourhood-overlap structures could subsume part of the counting argument, and independent historical-priority assessment remains appropriate.

## References

1. A. Abiad, M. Flagg, S. Ghasemi Nezhad and S. Zeijlemaker, *The Zero Forcing Number of Graph Powers*, arXiv:2610.03892, originally posted 2026-10-02. https://arxiv.org/abs/2610.03892
2. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips and C. Reinhart, *The zero forcing polynomial of a graph*, arXiv:1801.08910, 2018. https://arxiv.org/abs/1801.08910
3. C.-H. Chang and C.-H. Lin, *Minimum Rank of Powers of Cycles and Trees*, https://www-math.nsysu.edu.tw/~chlin/Publications/Articles/GJpower.pdf
4. A. Johnson, A. Vick, R. Flórez and D. A. Narayan, *Failed Skew Zero Forcing Numbers of Path Powers and Circulant Graphs*, AppliedMath 5(2), article 32 (2025). https://doi.org/10.3390/appliedmath5020032
