# Exact fair-efficient allocation for two agents with disjoint complementary pairs

## Finding
Let \(G\) be any finite set of \(g\) indivisible goods, and let agents \(A\) and \(B\) have valuations
\[
 v_i(S)=\sum_{e\in M_i}\mathbf 1[e\subseteq S],\qquad i\in\{A,B\},
\]
where \(M_A\) and \(M_B\) are matchings on \(G\) (not necessarily perfect, and allowed to share an edge). A pair is worth one only when both of its goods are owned by its agent. Each good is allocated to exactly one of the two agents.

**Theorem.** For these valuations, the set of attainable four-coordinate utility/envaluation signatures is computable exactly by a dynamic program with \(O(g^5)\) elementary transitions and \(O(g^4)\) live states. It follows that one can decide, and construct when possible, a complete allocation simultaneously envy-free up to one good (EF1) and Pareto optimal (PO), and compute the maximum utilitarian welfare attainable under EF1, in polynomial time. The construction is exact for all finite \(g\), including disconnected interaction graphs and coincident complementary pairs.

The connected perfect-matching case has a sharp boundary. If the two matchings together form one alternating cycle of \(2\ell\) goods, counting a shared pair as the two-edge cycle \(\ell=1\), then an EF1+PO allocation exists exactly when \(\ell\ne2\). For \(\ell\ge2\), the maximum total welfare under EF1 is exactly \(\ell-1\), whereas unrestricted maximum total welfare is \(\ell\); at \(\ell=1\), both maxima are one. At \(\ell=2\), the EF1 optimum is not PO. For every \(\ell\ge3\), an EF1+PO allocation with welfare \(\ell-1\) is explicit.

Even without a four-good alternating-cycle component, simultaneous EF1+PO may fail: the disjoint union of a shared pair (\(\ell=1\)) and an alternating six-good component (\(\ell=3\)) is an eight-good counterexample.

## Assumptions and scope
All utilities are nonnegative, integer-valued, and additive *over completed complementary pairs*, not additive over individual goods. Each agent's pair list is internally disjoint, which is a free-matroid subcase of purely complementary binary SPOC-2 valuations. Pair lists may overlap across agents; goods outside both matchings are allowed. EF1 means that for any envy by one agent, removal of at most one good from the other agent's bundle eliminates that envy. Pareto optimality excludes another complete allocation weakly improving both own utilities and strictly improving at least one. Neither valuations with overlapping pairs *within one agent* nor general matroid-rank substitutes over pairs are covered.

The number \(g=|G|\) measures input size, and the two matchings contain at most \(\lfloor g/2\rfloor\) edges each. The stated complexity counts integer-state transitions; retaining all reconstruction predecessors consumes polynomial additional space. The included standard-library program implements the state propagation with one representative bit mask per signature.

## Proof
**1. Degree-two structure.** Construct the edge-coloured multigraph on vertex set \(G\), giving one \(A\)-coloured edge for each pair in \(M_A\) and one \(B\)-coloured edge for each pair in \(M_B\). At a vertex there is at most one edge of either colour, hence degree at most two, counting parallel edges. Thus each connected component is a path, an isolated vertex, or an alternating cycle. Two coincident pairs give a two-vertex cycle with parallel edges. Enumerate the vertices of each path or cycle in adjacency order.

**2. Sufficient exact signature.** For a complete allocation \((X_A,X_B)\), define
\[
(a,b,c,d)=\bigl(v_A(X_A),v_B(X_B),v_A(X_B),v_B(X_A)\bigr).
\]
Because every pair in each \(M_i\) is disjoint from the other pairs in that same matching, deleting one good can destroy at most one completed pair of the envious agent in the other's bundle. If \(c>a\), some completed \(A\)-pair lies within \(X_B\), so deleting one endpoint decreases \(c\) by exactly one. Therefore agent \(A\)'s EF1 inequality is *equivalent* to \(c\le a+1\). Similarly agent \(B\)'s inequality is equivalent to \(d\le b+1\). Hence
\[
\boxed{\mathrm{EF1}\iff c\le a+1\ \text{and}\ d\le b+1.}
\]
PO depends only on the own-utility pair \((a,b)\): it holds exactly when no other attained pair \((a',b')\) satisfies \(a'\ge a\), \(b'\ge b\), with at least one strict inequality. These tests require no other features of an allocation.

**3. Exact transfer dynamic program.** When a good is assigned to \(A\) or \(B\), encode its recipient by zero or one. Traverse each path in order, or each cycle in cyclic order, processing the last closing edge after the final vertex. For each processed edge, inspect its colour and its two endpoint labels. An \(A\)-edge with labels \((0,0)\) increments \(a\), with labels \((1,1)\) increments \(c\), and otherwise contributes zero. A \(B\)-edge with labels \((1,1)\) increments \(b\), with labels \((0,0)\) increments \(d\), and otherwise contributes zero.

At every step retain the four integer counters, the label of the current component's first vertex and that of its most recently processed vertex, and one representative allocation of processed vertices. The next recipient has two possibilities. Upon completing a component, process its closing edge if any and discard its two boundary labels before beginning the next component. Two partial allocations with the same four counters and the same boundary labels have identical possible future increments, so keeping one representative does not lose any attainable signature. By induction over vertices and components, the final table is exactly the set of all attainable signatures, with a representative allocation for each.

Each counter is between zero and \(\lfloor g/2\rfloor\); there are at most four label pairs. Thus each layer contains \(O(g^4)\) states and the \(g\) vertex steps require \(O(g^5)\) transitions. On finishing, project signatures to the \(O(g^2)\) possible own-utility pairs and calculate their northeast Pareto frontier (for instance by a suffix-maximum table). Filter the signatures by both EF1 inequalities and this frontier. Nonemptiness decides EF1+PO and any retained representative is a witness. Separately maximizing \(a+b\) over EF1 signatures yields the exact EF1 welfare optimum.

**4. Single alternating cycle.** If both pair matchings cover the same \(2\ell\) vertices and form one alternating cycle, then any completed pair consumes two goods, so welfare is at most \(\ell\). For \(\ell\ge2\), attaining \(\ell\) means the completed pairs form a perfect matching of the cycle. Its only perfect matchings are the two alternating colour classes, so every good belongs to one agent. Such a full monopoly is not EF1 for \(\ell\ge2\): the other agent has utility zero and, after removal of one good, still evaluates the monopoly bundle at \(\ell-1\ge1\).

For \(\ell\ge2\), label the vertices consecutively \(0,1,\ldots,2\ell-1\), with the \(A\)-pairs \((0,1),(2,3),\ldots\) and the \(B\)-pairs \((1,2),(3,4),\ldots,(2\ell-1,0)\). Set \(k=\lfloor(\ell-1)/2\rfloor\). Give vertices \(0,1,\ldots,2k\) to \(A\) and the remainder to \(B\). The signature is
\[
(a,b,c,d)=(k,\ell-k-1,\ell-k-1,k).
\]
Since the first two coordinates differ by at most one, this allocation is EF1 and achieves welfare \(\ell-1\), proving the claimed optimum.

When \(\ell\ge3\), both own utilities are positive. Every allocation improving both weakly would have welfare at least \(\ell-1\). A strict improvement would force welfare \(\ell\), but all allocations with welfare \(\ell\) give one agent zero. Consequently this EF1 allocation is PO. When \(\ell=2\), no allocation can give both agents positive utility, since doing so would need all four vertices and two completed adjacent, differently coloured edges. The only PO utility pairs are \((2,0)\) and \((0,2)\), both violating EF1. When \(\ell=1\), either agent's monopoly is EF1 and PO: removal of one good destroys the only complementary pair.

**5. A disconnected obstruction.** Consider one shared pair and one alternating six-good cycle, with no overlaps between components. The attainable Pareto-optimal own-utility pairs are exactly
\[
(4,0),\quad(3,1),\quad(1,3),\quad(0,4).
\]
Indeed each component's Pareto frontier is, respectively, \(\{(1,0),(0,1)\}\) and \(\{(3,0),(1,1),(0,3)\}\); their componentwise sums give the displayed global frontier after removing dominated \((2,1)\) and \((1,2)\). All four frontier points have welfare four, forcing every edge of a perfect matching of each component to be completed; therefore the components are each assigned wholly to one agent. At all four allocations the cross-evaluations equal the other agent's own utility. The own utilities differ by at least two, so EF1 fails. This proves the eight-good failure without a four-good alternating component.

## Verification
Run `python3 checker.py` from the directory containing the attached standalone source. It generates complete outcomes by both the transfer dynamic program and an independent enumeration of every recipient assignment. It compares the *entire reachable four-statistic set*, the EF1+PO decision, and the maximum EF1 welfare. The supplied deterministic verification exercises 1,700 random disjoint-pair-list profiles with \(2\) through \(12\) goods, plus eight single-cycle instances of length one through eight; complete brute-force comparisons are also made for cycle lengths three through seven. The observed output was:

`VERIFY_OK complete_signature_and_PO_EF1_cases= 1708 single_cycle_lengths=1..8 independent_full_allocation_comparison=1700`

Enumeration is evidence for the implementation on the checked finite domain; the all-input theorem depends on the induction over the transfer states and on the cycle argument above.

## Relationship to prior work
Pyne, Viswanathan, Yang and Zick (2026) introduce binary submodular preferences over complements (SPOC), establish computational hardness for general instances, and give a four-item, two-agent example in which PO and EF1 cannot coexist (Proposition 2.1). That four-item example is exactly the length-two alternating cycle here and is **not a new obstruction**. Their existence and approximation results do not yield the exact two-agent disjoint-pair decision algorithm, the complete cycle-length boundary, or the eight-good disconnected obstruction. The present result applies only to additive rank over disjoint pairs, rather than arbitrary matroid-rank preferences over complements.

Teh (2026) establishes a seven/eight-good boundary for EF1+PO under strictly increasing valuations. That condition is inapplicable: every individual good in the present model can have zero marginal value until its complement arrives. Similarly, additive-valuation EF1+PO existence results do not cover complements. The finite-state method follows standard dynamic-programming principles for bounded-degree interaction graphs; equivalently phrased algorithms in specialized earlier literature remain a possible priority concern.

## Limitations
No polynomial algorithm is asserted for three or more agents, overlapping complement pairs within an agent, general SPOC matroid ranks, or complement sizes exceeding two. The decision algorithm determines whether a fair-efficient allocation exists; it does not guarantee existence. The bounded-degree decomposition would not survive unrestricted pair overlap. The source comparison is a best-knowledge originality assessment, not proof of publication priority, and independent scientific validation has not been performed.

## References
- S. Pyne, V. Viswanathan, W. Yang, and Y. Zick, *Fair Allocation with Dichotomous Preferences over Item Complements*, arXiv:2610.15801, first posted 2026-10-11, especially Sections 2–4 and Proposition 2.1. https://arxiv.org/abs/2610.15801
- N. Teh, *Fair Division with Strictly Increasing Valuations: A Tight Threshold for Two-Agent EF1 and PO*, arXiv:2607.23367, posted 2026-07-25. https://arxiv.org/abs/2607.23367
