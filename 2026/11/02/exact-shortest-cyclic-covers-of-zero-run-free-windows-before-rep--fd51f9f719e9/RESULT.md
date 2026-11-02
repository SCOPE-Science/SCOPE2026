# Exact shortest cyclic covers of zero-run-free windows before repeated-run overlap

## Finding

Let \(q\ge2\), \(h\ge2\), and \(h\le k\le2h\) be integers. Fix a labeled alphabet \(\Sigma\) of \(q\) symbols containing a distinguished zero. Write \(\mathcal A_{q,h}(k)\) for the length-\(k\) words avoiding the contiguous factor \(0^h\), and \(A_{q,h}(k)=|\mathcal A_{q,h}(k)|\). Let \(L_{q,h}(k)\) be the least length of a nonempty **cyclic** word which avoids \(0^h\) at every circular position and contains **every** member of \(\mathcal A_{q,h}(k)\) as at least one cyclic length-\(k\) factor. Multiplicities are allowed.

Then
\[
L_{q,h}(k)=A_{q,h}(k)+(k-h)M_{q,h}(k),
\]
where \(M_{q,h}(h)=0\) and, for \(h<k\le2h\),
\[
M_{q,h}(k)=(q-1)\left(q^{k-h-1}-\mathbf 1_{\{k=2h\}}\right).
\]
Here \(A_{q,h}(n)\) is given without exhaustive word enumeration by \(A_{q,h}(n)=q^n\) for \(0\le n<h\) and
\[
A_{q,h}(n)=(q-1)\sum_{j=1}^h A_{q,h}(n-j)\quad(n\ge h).
\]

Moreover, there is a complete optimal-augmentation description: every shortest cyclic cover's edge-multiplicity excess in the admissible de Bruijn graph decomposes into \(M_{q,h}(k)\) directed paths, each exactly \(k-h\) edges long, matching the vertices ending (but not beginning) in \(0^{h-1}\) bijectively to vertices beginning (but not ending) in \(0^{h-1}\). Conversely **any bijection** between these two sets, with the unique shortest bridge for every matched pair, gives a connected Eulerian augmentation and hence a shortest covering cycle. The statement classifies path decompositions, not distinct cyclic words or distinct multiplicity vectors arising from different decompositions.

For the binary alphabet with \(h=3\), the optimum lengths at \(k=4,5,6\) are respectively \(14,28,53\). For \(q=3,h=3,k=6\), there are \(648\) required words, exactly \(48\) extra traversals are necessary, and the optimum length is \(696\).

## Assumptions and scope

Words are labeled, contiguous factors are counted cyclically with wraparound, and the entire host is subject to the zero-run prohibition. A cyclic word of length \(L\) has \(L\) starting positions for length-\(k\) factors even when \(L<k\); in the present setting a covering host necessarily has enough positions. The count \(L_{q,h}(k)\) measures cyclic symbols (equivalently, directed edge traversals), not the length of a linearized representation with \(k-1\) closing symbols. No optimality statement is made for \(k>2h\). The case \(k=h\) has no augmentation.

## Proof

**1. Admissible graph and degree imbalance.** Let \(G\) have as vertices the admissible words of length \(k-1\), and for every \(w\in\mathcal A_{q,h}(k)\) a directed edge from its \((k-1)\)-prefix to its \((k-1)\)-suffix, labeled by \(w\). Every edge is unique as a labeled \(k\)-word. The graph is strongly connected: from any vertex, append a fixed nonzero symbol \(k-1\) times to reach a constant nonzero vertex, then append the symbols of any desired vertex. No forbidden run appears at either junction.

If \(k>h\), a vertex has indegree \(q-1\), instead of \(q\), precisely when it **begins** with \(0^{h-1}\); it has outdegree \(q-1\), instead of \(q\), precisely when it **ends** with \(0^{h-1}\). Consequently the vertices with indegree exceeding outdegree by one form a set \(S\) of words ending but not beginning in \(0^{h-1}\); those with outdegree exceeding indegree by one form a set \(T\) of words beginning but not ending in \(0^{h-1}\). Every other vertex is balanced. When \(k=h\), all vertices are balanced, including \(0^{h-1}\).

**2. Exact defect count.** A vertex of length \(k-1\) ending with \(0^{h-1}\) must have a nonzero preceding symbol. The preceding \(k-h-1\) symbols are arbitrary because \(k-h-1\le h-1\). This gives \((q-1)q^{k-h-1}\) vertices. Such a vertex can also begin with \(0^{h-1}\) only if \(k=2h\); then it has the form \(0^{h-1}a0^{h-1}\) with \(a\ne0\), giving exactly \(q-1\) balanced vertices to subtract. Thus \(|S|=|T|=M_{q,h}(k)\).

**3. Sharp minimum bridge distance.** Fix \(s\in S\) and \(t\in T\) with \(k>h\), and let \(d=k-h\). Any directed path of length \(r<d\) starting at \(s\) leaves a length-\((k-1-r)\) suffix of \(s\) at the front of the final vertex. For that vertex to begin in \(0^{h-1}\), the original \(s\) must have an occurrence of \(0^{h-1}\) starting at position \(r+1\) (one-based). Since \(s\) ends with \(0^{h-1}\), another occurrence begins at position \(d+1\). Their starting positions differ by \(d-r\), which is between one and \(h\). If the difference is below \(h\), the two runs overlap or touch and force \(h\) consecutive zeros, a contradiction. If the difference equals \(h\), then \(d=h\) and \(r=0\), so \(s\) itself begins in \(0^{h-1}\), contrary to \(s\in S\). Hence every path from \(S\) to \(T\) has length at least \(d\).

Conversely, for any \(s\in S\) and \(t\in T\), write \(t=0^{h-1}z\), where \(|z|=d\) and the first symbol of \(z\) is nonzero. Append precisely \(z\) to \(s\). Every intermediate \(k\)-window avoids \(0^h\): the initial suffix of \(s\) contains \(0^{h-1}\), the next appended symbol is nonzero, and the appended string is itself a suffix of the admissible vertex \(t\). After \(d\) shifts the state is exactly \(0^{h-1}z=t\). This bridge is unique among \(d\)-edge paths between the chosen endpoints.

**4. Lower bound for every cyclic cover.** A cyclic cover corresponds to a closed directed walk in \(G\) traversing each base edge at least once. Subtract one traversal of every base edge. The resulting nonnegative integral directed multigraph must balance the original deficits. In particular each vertex in \(S\) has one net additional outgoing unit, and each vertex in \(T\) has one net additional incoming unit. Decomposing the added integral flow into \(S\)-to-\(T\) paths and directed circuits produces at least \(|S|\) paths. Step 3 bounds each such path below by \(d\) edges; directed circuits have nonnegative length. Thus at least \(dM_{q,h}(k)\) extra edges are required.

**5. Attainment and equality classification.** Choose any bijection \(\pi:S\to T\) and duplicate every edge along the length-\(d\) bridge from \(s\) to \(\pi(s)\). Exactly \(dM_{q,h}(k)\) edges are added, and all vertices now have equal indegree and outdegree. Because \(G\) was strongly connected, this finite augmented directed multigraph has an Eulerian circuit. Reading its edge-ending symbols gives a cyclic word of the stated length, avoids \(0^h\), and covers every admissible word. The lower bound is attained. Equality in Step 4 leaves no added circuits and forces all \(|S|\) source-to-target paths to have length exactly \(d\); by Step 3 they are exactly the stipulated bridges, establishing the classification. When \(k=h\), the unaugmented graph is already Eulerian and the same conclusion holds with zero paths.

**6. Recurrence for required words.** For \(n\ge h\), every admissible length-\(n\) word uniquely ends in one nonzero symbol followed by \(j-1\) zeros, where \(1\le j\le h\). The preceding prefix has length \(n-j\) and can be any admissible word. There are \(q-1\) choices for that final nonzero symbol. This proves the recurrence and completes the theorem.

## Verification

The standalone `verify.py` uses only Python's standard library. Its first method constructs the entire legal overlap graph, inserts explicit matched shortest paths, finds an Eulerian tour, and directly scans all cyclic length-\(k\) factors of the produced word. Independently, breadth-first searches measure source-to-target distances, and a subset dynamic program computes exact minimum-cost bipartite assignments for every checked case with at most sixteen defects. The checks covered 37 parameter triples with alphabet sizes two through four, run bounds two through five, a total of 18,274 admissible graph edges, 995 source-target distance comparisons and 34 exact matching optimizations. The result was:

```text
VERIFY_OK q=2..4 h=2..5 cases=37 admissible_edges=18274 checked_source_target_pairs=995 exact_assignment_instances=34
```

These finite checks corroborate the construction and optimization; the proof above, not enumeration, establishes the all-parameter theorem. Run `python3 verify.py` from the directory containing this document and the verifier.

## Relationship to prior work

The general directed Chinese-postman and shortest-factor-set walk correspondence, including algorithms rather than explicit specialized formulas, is established by Bernardini et al. (2022). Chee et al. (2024) study **maximum** length run-limited sequences with no repeated windows; their full article describes the same type of imbalanced forbidden-run overlap graph but does not state a **minimum** repeat-allowed covering walk, its exact correction length, or its complete shortest-bridge characterization. These are different objectives with opposite treatments of extra edge traversals.

An earlier exact result for cyclic covers of **binary** words avoiding two consecutive copies of a fixed symbol covers a special \(q=2,h=2\) subfamily. The present all-alphabet, all-run-threshold pre-overlap theorem is not implied by that restriction, although the overlapping small cases must and do agree. Generic postman algorithms can compute any finite example but do not alone state the simple closed first-regime cost, its uniform endpoint distance, or the optimal matching description. A 2005 thesis of E. Moreno on restricted-language de Bruijn cycles is related, but its full text could not be inspected; equivalence to an unlocated specialization is a residual literature risk.

## Limitations

The result concerns one distinguished forbidden constant run, cyclic hosts, and \(h\le k\le2h\). It does not claim a formula for wider windows, linear hosts, several forbidden factors, or the number of distinct Euler tours. Distinct optimal path matchings may induce the same edge-multiplicity vector. The earlier restricted-language literature cannot be ruled out exhaustively, and no independent scientific audit has been performed.

## References

- Y. M. Chee, T. Etzion, T. L. Nguyen, D. H. Ta, V. D. Tran, and V. K. Vu, *Maximum Length RLL Sequences in de Bruijn Graph*, arXiv:2403.01454, initially publicly submitted March 3, 2024. https://arxiv.org/abs/2403.01454
- G. Bernardini, A. Conte, E. Gabory, R. Grossi, G. Loukides, S. P. Pissis, G. Punzi, and M. Sweering, *On Strings Having the Same Length-\(k\) Substrings*, CPM 2022, DOI:10.4230/LIPIcs.CPM.2022.16. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CPM.2022.16
- E. Moreno, *De Bruijn graphs and sequences in languages with restrictions*, doctoral thesis (2005), repository https://theses.hal.science/tel-00628709 (full text inaccessible in the present review).
