# Minimum zero-forcing starters and parallel propagation profiles of path and cycle powers

## Finding

Let \(k\ge1\), and let \(P_n^k\) and \(C_n^k\) denote the graphs joining vertices at path or cyclic distance at most \(k\). For a graph \(G\), set
\[
F_G(y)=\sum_{\substack{B\subseteq V(G),\ |B|=Z(G)\\ B\text{ zero forcing}}}y^{\tau_G(B)},
\]
where \(\tau_G(B)\) is the number of synchronous rounds obtained by turning *every* currently forceable white vertex black at each round. The zero-forcing number \(Z(G)\) is the minimum number of initially black vertices needed to force all vertices.

For every \(n\ge2\),
\[
F_{P_n^k}(y)=
\begin{cases}
ny,&2\le n\le k+1,\\
2k\,y^{n-k},&n\ge k+2.
\end{cases}
\]
For every \(n\ge3\),
\[
F_{C_n^k}(y)=
\begin{cases}
ny,&n\le2k+1,\\
nk\,y,&n=2k+2,\\
n\,y^{\lceil(n-2k)/2\rceil}
+2n(k-1)\,y^{1+\lceil(n-2k-1)/2\rceil},&n\ge2k+3.
\end{cases}
\]
Coincident powers of \(y\) in the last line are understood to have their coefficients added. Thus, for \(n\ge2k+3\), exactly \(n(2k-1)\) minimum zero-forcing sets occur: \(n\) cyclic intervals of length \(2k\), and \(2n(k-1)\) sets formed from an interval of length \(2k+1\) by omitting a noncentral interior vertex (not an endpoint or the middle vertex). The latter family is empty for \(k=1\). If \(n-2k\) is even, the interior-hole configurations need one extra round; if it is odd, all optimum starters have the same parallel propagation time.

The classification is exact. In noncomplete path powers, all minimum sets have the form \(N[v]\setminus\{w\}\), where \(v\) is a path endpoint and \(w\) is one of its \(k\) neighbors in the power graph. In cycle powers with \(n\ge2k+3\), they are precisely \(N[v]\setminus\{w\}\) for any vertex \(v\) and neighbor \(w\) of \(v\). In the boundary case \(n=2k+2\), they are precisely the complements of pairs of vertices that are not antipodal on the underlying cycle.

## Assumptions and scope

All graphs are finite, simple, undirected, and labeled by their natural path or cyclic order. In a zero-forcing step, a black vertex with exactly one white neighbor forces that neighbor black. Synchronous time \(\tau_G(B)\) is the number of iterations of this color-change rule when every available force is performed simultaneously, with time zero for the starting set. In the stated domain every minimum set is proper, so all times displayed are positive. \(N[v]\) denotes closed neighborhood in the **power graph**. The graph \(P_n\) has \(n\ge2\) vertices and \(C_n\) has \(n\ge3\) vertices. The parameter \(k\) is a positive integer with no bound in terms of \(n\).

The scalar minimum forcing numbers are previously known; the contribution here is the exhaustive classification and the complete propagation-time enumerators. The formula does not count forcing sets larger than the minimum, nor does it count individual choices of force orders.

## Proof

**1. Minimum-cardinality first-force principle.** For any graph without isolates, \(Z(G)\ge\delta(G)\): before the first force, its forcing vertex must be black, together with all but one of its neighbors. If a minimum set \(B\) has cardinality \(\delta(G)\) and a vertex \(v\) first forces \(w\), then \(d(v)=\delta(G)\) and necessarily \(B=N[v]\setminus\{w\}\). Conversely, whenever that configuration subsequently forces every vertex, it is a minimum set. We use this necessity to avoid assuming that one exhibited forcing sequence accounts for all optimal starters.

**2. Path powers.** If \(n\le k+1\), the graph is complete and its minimum sets are all complements of one vertex; each forces its sole white vertex in one round. If \(n\ge k+2\), the minimum degree is \(k\), attained only at the two path endpoints. Hence every minimum set must be the initial or terminal \(k+1\) vertices with one vertex other than the endpoint omitted. From either endpoint, the omitted neighbor is forced in round one; after that round the entire endpoint interval of \(k+1\) vertices is black. In each subsequent round exactly its next outside vertex can become black, so the total time is \(1+(n-k-1)=n-k\). There are \(k\) distinct choices per endpoint and the two endpoint families are disjoint when \(n\ge k+2\). This proves the path line.

**3. Noncomplete cycle powers: first-force classification.** If \(n\ge2k+2\), the power cycle is \(2k\)-regular, so any minimum set has at least \(2k\) vertices. Every set of \(2k\) consecutive cyclic vertices forces the next white vertex from a suitable black vertex on both sides, and propagation fills the cycle. Thus \(Z(C_n^k)=2k\), and the first-force principle makes all minimum sets exactly the sets \(N[v]\setminus\{w\}\) for an ordered pair \((v,w)\) of adjacent vertices of the power graph. Such a set forces \(w\) initially, then contains the full cyclic interval \(N[v]\) of \(2k+1\) black vertices, which subsequently expands from its two ends and forces everything. In the complete range \(n\le2k+1\), the standard complete-graph argument gives the first cycle line instead.

**4. Distinctness and the boundary case.** Fix \(n\ge2k+3\) and write \(L=2k+1\), so \(L\le n-2\). Each closed neighborhood \(N[v]\) is an \(L\)-vertex cyclic interval. If two \(L\)-intervals differ by cyclic shift \(d\), their intersection has size
\[
\max(0,L-d)+\max(0,L-(n-d)).
\]
For \(1\le d\le n-1\), this equals \(L-1\) exactly when \(d=1\) or \(d=n-1\); for all other shifts it is at most \(L-2\). Consequently, the only minimum sets represented by two distinct first-force centers are the intersections of consecutive closed neighborhoods. They are exactly the \(n\) cyclic intervals of \(2k\) consecutive vertices, with two representations apiece. The remaining \(2kn-2n\) representations produce \(2n(k-1)\) different sets, each with one omitted interior neighbor of its defining interval center (the center itself cannot be omitted). This proves the classification and number.

If \(n=2k+2\), each vertex is adjacent to every other vertex except its unique antipode. Its closed neighborhood is the complement of that antipode. A minimum set is therefore the complement of two nonantipodal vertices. Conversely, the antipodes of the two initially white vertices can force them simultaneously, since those forcing vertices are black and see precisely one white neighbor each. The number of unordered nonantipodal pairs is \(\binom n2-n/2=nk\), and all have time one.

**5. Parallel rounds.** Suppose in a noncomplete cycle power that a cyclic interval of \(h\ge2k\) consecutive vertices is black and its complement is a nonempty single white interval of \(q=n-h\) vertices. In a parallel round exactly the first and last white vertices are forceable, with the understanding that these are one vertex when \(q=1\). Indeed, each boundary white vertex is the unique white neighbor of a black vertex positioned \(k\) steps beyond it into the black interval; every black vertex has a radius-\(k\) neighborhood meeting the white interval, if at all, in a prefix or suffix, because the opposite route passes through at least \(2k\) black vertices. Hence any singleton intersection is an endpoint of the white interval, and no interior white vertex can be forced yet. After the round, the black interval has grown by \(\min(2,q)\), and the same assertion repeats. Thus a full black interval of length \(h\) has parallel completion time \(\lceil(n-h)/2\rceil\).

In the duplicate-representation case (a consecutive initial \(2k\)-interval), the lemma immediately yields \(\tau=\lceil(n-2k)/2\rceil\). Otherwise the minimum set has one hole in a \((2k+1)\)-interval and only its unique first-force center acts at round one; after filling the hole there is a full black interval of length \(2k+1\). It therefore has \(\tau=1+\lceil(n-2k-1)/2\rceil\). Summing over the classified sets proves the cycle generating function. Comparing these exponents proves the parity statement.

## Verification

The accompanying standalone `verify.py` constructs independent path-power and cycle-power adjacency lists from distances and tests every subset of size \(Z(G)\) by the synchronous forcing rule. It compares the exact discovered set collection, time histogram, and minimum-degree lower bound with the formulas; it does not enumerate only the predicted candidate family. Additional larger cyclic profiles independently verify representation multiplicities. From `python3 verify.py` in the package directory, the recorded output is:

```text
ALL CHECKS PASSED
exhaustive_graph_profiles=97
initial_sets_independently_tested=115832
minimum_zero_forcing_sets_found=2466
interval_representation_profiles=180
tested_path_orders=2..14; cycle_orders=3..18; powers=1..5
```

The finite tests are consistency checks only; the argument for all integers \(n,k\) is the proof above.

## Relationship to prior work

Abiad–Flagg–Ghasemi Nezhad–Zeijlemaker (2026, arXiv:2610.03892v1), Section 3, Propositions 7 and 8, establish the *scalar* minimum forcing numbers of these graph powers; those numbers are not claimed as new. Boyer and collaborators (2018, arXiv:1801.08910v1), Theorem 1(3), already determine the next-to-leading zero-forcing-polynomial coefficient for any graph, and therefore encompass both the exceptional \(n=2k+2\) cycle count and the short-path boundary \(n=k+2\), because in those cases the minimum forcing size equals the order minus two. Ferrero–Hall–Hogben–Hunnell–Small (2025, arXiv:2511.16335), Example 3.1, cover ordinary cycles \(k=1\) and their propagation time. Our principal new refinement concerns **higher cycle powers with \(k\ge2\) and \(n\ge2k+3\)** (and path powers with \(k\ge2\) and \(n\ge k+3\)), where the complete census (including two cycle forcing-time classes and a fixed path time) does not follow from the scalar results, the universal near-leading coefficient, or the ordinary-cycle instance.

## Limitations

The claim concerns standard deterministic zero forcing with minimum-cardinality initial sets only. It does not cover other variants (positive semidefinite, skew, or probabilistic), nonminimal forcing sets, arbitrary graph powers, or propagation times under a different update convention. Searches cannot exclude unpublished results or every synonym in the older circulant-graph literature. The complete proof is elementary and self-contained, but independent external review remains unperformed.

## References

1. A. Abiad, M. Flagg, S. Ghasemi Nezhad, S. Zeijlemaker, *The Zero Forcing Number of Graph Powers*, arXiv:2610.03892v1 (first public 2026-10-02), especially Section 3, Propositions 7–8, https://arxiv.org/pdf/2610.03892v1.
2. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, C. Reinhart, *The zero forcing polynomial of a graph*, arXiv:1801.08910v1 (2018), Theorems 1–2 and Section 4, https://arxiv.org/html/1801.08910v1.
3. D. Ferrero, H. T. Hall, L. Hogben, M. Hunnell, B. Small, *Zero forcing propagation time intervals and graphs with fixed propagation time*, arXiv:2511.16335 (2025), Example 3.1, https://arxiv.org/pdf/2511.16335.
4. F. H. J. Kenter and J. C.-H. Lin, *On the error of a priori sampling: zero forcing sets and propagation time*, arXiv:1709.08740 (2017), https://arxiv.org/abs/1709.08740.
