# Fibonacci overhead for cyclic covers of \(001\)-avoiding binary words

## Finding

Let \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\). For every integer \(n\ge3\), let \(\mathcal A_n\) be **all ordinary finite binary words of length \(n\) that contain no contiguous occurrence of `001`**. Let \(L_n\) be the smallest positive integer for which a circular binary word of length \(L_n\) has, among its cyclic length-\(n\) windows, every member of \(\mathcal A_n\). Windows not in \(\mathcal A_n\) and repeated windows are permitted. The exact minimum is

\[
\boxed{L_n=F_{n+3}-1+(n-2)F_{n-1}.}
\]

There are exactly \(F_{n+3}-1\) distinct required windows, so the necessary and sufficient number of extra windows is exactly \((n-2)F_{n-1}\). In particular, the relative overhead grows linearly with \(n\), rather than remaining bounded. The values for \(n=3,4,\ldots,12\) are \(8,16,29,53,94,166,290,504,871,1499\).

## Assumptions and scope

Indices for windows are cyclic in the covering word, not in each required finite word: a finite word such as `1000` is admissible even though its infinite periodic repetition contains `001`. The cover itself need not avoid `001`. Let \(\mathrm{D}_n\) denote the full directed binary de Bruijn multigraph with vertices \(\{0,1\}^{n-1}\) and a directed edge for every indexed binary word \(a_1\cdots a_n\), from \(a_1\cdots a_{n-1}\) to \(a_2\cdots a_n\). Even when there are parallel arcs in degenerate orders, each length-\(n\) word is treated as its own edge; for \(n\ge3\), distinct words yield distinct directed arcs.

## Proof

**1. Counting required windows.** Binary words of length \(n\) without `00` number \(F_{n+2}\). Every word avoiding `001` but containing `00` is uniquely of the form \(u0^k\) with \(k\ge2\), where \(u\) is empty or is a word avoiding `00` and ending in `1`. Otherwise a `1` after the first `00` would create `001`. Summing over \(0\le |u|\le n-2\), the latter class has \(\sum_{j=1}^{n-1}F_j=F_{n+1}-1\) members. Thus

\[
|\mathcal A_n|=F_{n+2}+F_{n+1}-1=F_{n+3}-1.
\]

**2. Locating the imbalance.** Retain in \(\mathrm D_n\) exactly the edges \(\mathcal A_n\), obtaining the required-edge graph \(G_n\). Each vertex containing `001` has no incident required edge. For a vertex \(v\in\{0,1\}^{n-1}\) avoiding `001`, the required indegree and outdegree are

\[
 d^-_{G_n}(v)=2-\mathbf 1\{v\text{ begins with `01`}\},\qquad
 d^+_{G_n}(v)=2-\mathbf 1\{v\text{ ends with `00`}\}.
\]

Consequently the positive imbalance \(d^+-d^-=1\) occurs precisely at vertices \(T_n\) beginning in `01` and containing no `00`: any word avoiding `001` that contains `00` has only zeros following its first `00`, hence ends in `00`. Exactly \(F_{n-1}\) vertices belong to \(T_n\), because their remaining \(n-3\) bits avoid `00`. The negative imbalance \(-1\) occurs at a set \(S_n\) of equally many vertices, each ending in `00`; all other vertices have zero imbalance.

**3. Unavoidable augmentation.** A circular covering word determines a closed directed walk in the full \(\mathrm D_n\) that traverses every required edge at least once. Remove one copy of each required edge from its edge multiset. The remaining nonnegative integral edge flow has one extra outgoing unit at every vertex in \(S_n\) and one extra incoming unit at every vertex in \(T_n\), with no other imbalances. Such a flow decomposes into \(F_{n-1}\) directed paths from \(S_n\) to \(T_n\), together with directed cycles (the path count includes multiplicities).

Every path from \(s\in S_n\) to \(t\in T_n\) has length at least \(n-2\). Indeed a path of \(k<n-2\) edges would require an overlap of length \((n-1)-k\ge2\) between the suffix of \(s\) and the prefix of \(t\). That suffix ends in `00`, while \(t\) has no `00`, a contradiction. The extra flow therefore has at least \((n-2)F_{n-1}\) edges. This proves the asserted lower bound even when arbitrary forbidden windows and repeats are allowed.

**4. Sharp construction and connectivity.** Match the vertices of \(S_n\) bijectively with those of \(T_n\) in any order. Each source ends in `0`, and each target begins in `0`. For each matched pair append the last \(n-2\) symbols of its target to its source, creating a de Bruijn path of exactly \(n-2\) edges. Add all these paths to \(G_n\). The resulting directed multigraph is balanced and has precisely \(F_{n+3}-1+(n-2)F_{n-1}\) edges.

It is strongly connected on all incident vertices. From the vertex \(1^{n-1}\), appending the symbols of any required vertex \(v\) reaches \(v\) through required edges: the preceding run of ones cannot produce `001`, and \(v\) itself avoids `001`. Conversely, from \(v\), appending zeros reaches \(0^{n-1}\) through required edges. The latter is a member of \(S_n\), so its added path leads to a member of \(T_n\), which has no `00`; appending ones then reaches \(1^{n-1}\) via required edges. Finally, any vertex that occurs only on an added path is connected to both its source and target along that path. Thus all incident vertices lie in one strongly connected Eulerian multigraph. An Euler tour exists, and its edge labels form a circular word containing every required length-\(n\) word. The upper and lower bounds coincide.

## Verification

The accompanying standard-library Python program `verify.py` constructs the multigraph with lexicographically paired imbalance vertices, computes an Eulerian circuit, verifies every required cyclic window, balances the exact in/out degrees, and checks the formula for every \(3\le n\le18\). It also brute-forces all shorter circular binary candidates at orders three and four. Running `python3 verify.py` prints `VERIFY_OK`. Numerical enumeration is supplementary to the complete all-order proof above; it does not certify untested orders.

For \(n=5\), the program constructs the optimal \(29\)-bit cyclic witness `11111011100110101100010100000`. It contains all \(20\) finite five-bit words avoiding `001`; the lower bound proves that \(29\) is minimal.

## Relationship to prior work

Moreno and Matamala, *Minimum de Bruijn Sequence in a Language with Forbidden Substrings* (arXiv:0711.1695v1, 2007), construct exact-once de Bruijn cycles for irreducible subshifts and study lexicographic minimality. Their definition uses periodic admissibility: a word must have an infinite repetition avoiding the forbidden factors (Section 2.1). The present target set instead contains every **finite** `001`-avoiding word, including nonperiodically extendible transient words such as `1000`. The required-edge graph is not balanced, and extra, possibly forbidden, windows are allowed. Their Eulerian existence theorem does not imply the sharp length above.

Bernardini and coauthors, *On Strings Having the Same Length-\(k\) Substrings* (CPM 2022, DOI 10.4230/LIPIcs.CPM.2022.16), develop algorithms for shortest linear strings whose factor set equals a given set, with directed Chinese-postman reductions. That exact-factor-set condition differs from the present cyclic **superset**-cover requirement, in which the necessary extra paths may use forbidden edges. Their general algorithmic results do not state this Fibonacci optimum. The underlying de Bruijn and directed postman techniques are standard; the claimed contribution is the explicit all-length invariant and the tight uniform source-to-sink overlap obstruction, not invention of those techniques.

## Limitations

This theorem concerns the single excluded binary factor `001` (and, by reversal and complementation, its three symmetry equivalents `100`, `110`, and `011`) and all integer orders \(n\ge3\). It does not determine optimal lengths for avoidance of `000` or `010`, characterize every minimizing circular word, or require the cover to avoid forbidden factors. Historical originality has not been independently certified; publication indexing may omit relevant special-case results.

## References

1. E. Moreno and M. Matamala, *Minimum de Bruijn Sequence in a Language with Forbidden Substrings*, arXiv:0711.1695v1 (public preprint, 2007-11-12), https://arxiv.org/abs/0711.1695 . A related earlier 2004 conference version exists, but a calendar-specific first-public date for that version was not established here.
2. G. Bernardini, A. Conte, E. Gabory, R. Grossi, G. Loukides, S. P. Pissis, G. Punzi, and M. Sweering, *On Strings Having the Same Length-k Substrings*, CPM 2022, DOI 10.4230/LIPIcs.CPM.2022.16, https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CPM.2022.16 .
3. E. Moreno and M. Matamala, *Minimal de Bruijn Sequence in a Language with Forbidden Substrings*, Graph-Theoretic Concepts in Computer Science, WG 2004, pp. 168–176, DOI 10.1007/978-3-540-30559-0_14 (earlier related account; distinct from the explicit formula proved here).
