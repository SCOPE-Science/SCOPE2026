# Sharp first-five quantifier-rank profiles of finite directed cycles

## Finding
For each integer \(n\geq1\), let \(C_n\) be the finite relational structure with domain \(\{0,\ldots,n-1\}\), one binary relation \(R\), and
\[
R(i,j)\quad\Longleftrightarrow\quad j\equiv i+1\pmod n.
\]
Let \(C_n\equiv_q C_m\) mean agreement on **all** first-order sentences of quantifier rank at most \(q\), in the relational language \(\{R,=\}\), with unrestricted numbers of variable names but no function or order symbol. Then for every \(q\in\{1,2,3,4,5\}\),
\[
 C_n\equiv_q C_m\quad\Longleftrightarrow\quad
 (n=m<T_q)\ \lor\ (n\geq T_q\ \text{and}\ m\geq T_q),
\]
where the sharp thresholds are
\[
(T_1,T_2,T_3,T_4,T_5)=(2,4,7,11,19).
\]
Thus rank five distinguishes every cycle shorter than 19 from every cycle of a different size, but cannot distinguish any two cycles of size at least 19. The thresholds concern **directed, loop-allowed successor relations**; \(C_1\) has a loop and \(C_2\) has two opposite arcs.

## Assumptions and scope
All structures are finite and nonempty, and *each structure is a single directed cycle*, rather than a disjoint union of cycles. The quantifier rank counts maximum nested quantifiers. The relation is given explicitly above, rather than by a unary function symbol: in a functional language, terms of unbounded iteration make the claimed cutoffs false. The claim does not give a formula for arbitrary quantifier rank and does not classify arbitrary bijections or disconnected successor graphs.

## Proof
**Back-and-forth types.** For an ordered tuple \(\bar a\) of vertices of \(C_n\), define \(\tau_0(n,\bar a)\) as its complete atomic diagram: the truth values of every \(a_i=a_j\) and \(R(a_i,a_j)\). For \(r\geq0\), define recursively
\[
\tau_{r+1}(n,\bar a)
=\left(\tau_0(n,\bar a),\ \{\tau_r(n,\bar a b): b\in C_n\}\right).
\]
The same definition applies to the empty tuple. The usual back-and-forth induction proves that two tuples in possibly different finite relational structures have identical \(\tau_r\) precisely when they satisfy the same first-order formulas of quantifier rank at most \(r\). For the inductive step, equality of the sets of one-point extension types is exactly the conjunction of the forward and backward extension conditions. Conversely, every finite type can be defined by a finite characteristic formula built from the atomic diagram and conjunctions of existential and universal extension conditions. In particular, \(C_n\equiv_q C_m\) iff \(\tau_q(n,())=\tau_q(m,())\).

**Exhaustive finite comparison.** The supplied standard-library program `verify_cycle_types.py` constructs these finite hereditarily nested types using global exact interning, with no probabilistic hashes and no heuristic pruning. Because rotation of a directed cycle is an automorphism, every one-point type of a fixed cycle agrees with the type at vertex 0: the empty-tuple extension set can therefore be represented by this one type. For nonempty tuples, the first coordinate is fixed at 0 and each possible new coordinate is enumerated from 0 to \(n-1\). The program computes the rank profiles for **every** \(1\leq n\leq32\) and every \(1\leq q\leq5\), and asserts that the equivalence classes are exactly the singletons \(\{1\},\ldots,\{T_q-1\}\) followed by \(\{T_q,\ldots,32\}\). The complete partitions and the counts \(2,4,7,11,19\) are recorded in `certificate.json`. Since every vertex and every extension choice is represented by the symmetry reduction, this is exhaustive rather than sampled evidence.

**All larger cycles.** For every \(q\geq1\), Duplicator wins the \(q\)-round Ehrenfeucht--Fraïssé game between \(C_n\) and \(C_m\) whenever \(n,m\geq2^q\). After the first move, match arbitrary vertices and preserve the directed cyclic order of selected vertices. With \(r\) moves remaining, maintain the following invariant for each corresponding gap between consecutive selected vertices around the oriented circles: its two positive integer arc lengths are equal when one is less than \(2^{r+1}\); otherwise **both** are at least \(2^{r+1}\). Initially there is one full-circle gap of lengths \(n,m\), and \(r=q-1\), so the invariant holds.

If Spoiler repeats an already selected vertex, repeat its mate. Otherwise a move splits one gap into lengths \(a,b\). If the corresponding gaps have equal lengths, copy the split. If both original gaps are at least \(2^{r+1}\), put \(h=2^r\). If \(a<h\), match the first new gap exactly with length \(a\); the other new gap in both cycles has length at least \(h\). The case \(b<h\) is symmetric. If neither is smaller than \(h\), split the other original gap into two lengths at least \(h\), which is possible because its length is at least \(2h\). Hence the invariant persists with \(r-1\) moves. At the end, \(r=0\), every unit-length arc between consecutive selected vertices is matched by a unit-length arc, and conversely; cyclic order and equality of selected vertices have also been preserved. Thus all atomic facts are preserved, proving Duplicator's win.

For \(q=5\), this proves \(C_n\equiv_5 C_{32}\) for every \(n\geq32\). The finite comparison gives \(C_{19}\equiv_5 C_{32}\) and \(C_{19}\equiv_5 C_n\) for \(19\leq n\leq31\); transitivity gives the entire infinite class. The exact finite comparisons similarly establish all smaller-rank singleton classes and cutoffs. Since rank-five equivalence implies equivalence at lower ranks, the same infinite argument completes all five profiles. This proves the finding.

## Verification
Run `python3 verify_cycle_types.py` in a directory containing that file. It requires Python 3 with no third-party modules, recomputes all 160 cycle/rank combinations (32 lengths at each of five ranks), checks every claimed finite partition, and emits `certificate.json` as one compact JSON line. The included `certificate.json` was obtained by running the script and is a convenience output, not a substitute for the mathematical completeness argument above. The universal \(n,m\geq32\) bound is proved analytically, not extrapolated from the computation.

## Relationship to prior work
Pikhurko and Verbitsky (arXiv:math/0305244, public preprint of 16 May 2003) analyze quantifier rank for distinguishing or identifying general finite relational structures, with bounds dependent on the universe size. Those generic identification results do not determine when **distinct-sized directed cycles** become logically indistinguishable at rank five. Libkin's *Elements of Finite Model Theory*, Chapter 3, presents the back-and-forth type recursion and large-successor-structure games, including path-versus-cycle examples; they provide the general methods but not the five sharp directed-cycle thresholds stated here. Albert, Bouvel and Féray (arXiv:1808.05459) study permutations represented by a binary graph of a bijection, precisely the ambient signature relevant here, and prove qualitative expressibility results, without an exact small-rank single-cycle profile in the inspected material. A previously published exact result for directed *paths* gives the threshold \(2^q\) for path lengths for \(q\geq2\); this is a different class with definable endpoints and neither a specialization nor a stronger coverage of the cycle result.

## Limitations
The lower sharpness and the intermediate equivalence comparisons are certified by a fully specified finite back-and-forth recurrence; no concise hand-written distinguishing formula for each adjacent pair is included. The analytic large-size argument has the coarser bound \(2^5=32\); the improvement to 19 uses the finite certificate. No claim is made for quantifier ranks above five, for permutations with multiple components, for undirected cycles, or for functional-language successor. Originality is a best-knowledge literature assessment, not a proof of priority; earlier unindexed exact tables remain a possibility. Independent verification has not been performed.

## References
1. O. Pikhurko and O. Verbitsky, *Descriptive Complexity of Finite Structures: Saving the Quantifier Rank*, arXiv:math/0305244 (first public version 2003-05-16), especially Sections 1--2 and the general identification bounds.
2. L. Libkin, *Elements of Finite Model Theory*, Springer (2004), Chapter 3 (Ehrenfeucht--Fraïssé types, games, and successor-graph examples); publicly readable later PDF edition at `https://homepages.inf.ed.ac.uk/libkin/fmt/fmt.pdf`.
3. M. Albert, M. Bouvel and V. Féray, *Two first-order logics of permutations*, arXiv:1808.05459 (2018), particularly Sections 2 and 4; subsequently *J. Combin. Theory Ser. A* 171 (2020), 105158.
4. *Exact quantifier-rank threshold for finite directed paths*, published published-finding corpus mathematical finding, identifier `2026/10/4/SCOPE-exact-quantifier-rank-threshold-for-finite-directed-paths--75a6b05e7112` (path comparison only).
