# Odd-cycle remanence: strict nesting and exact DFA sizes \(6,18,102,1098\)

## Finding
For each integer \(n\ge3\), let \(C_n\) be the simple cycle whose vertices are \(0,1,\ldots,n-1\), with cyclic consecutive edges. Each orientation \(\mathcal O\) defines a nondeterministic automaton on \(\{+,-\}\): every vertex is both initial and final, a \(+\)-transition follows an oriented edge, and a \(-\)-transition follows that edge backwards. Define \(\operatorname{Rem}(C_n)\) as the intersection of the languages of all orientations.

The following inclusions are strict:
\[
\operatorname{Rem}(C_9)\subsetneq\operatorname{Rem}(C_7)\subsetneq\operatorname{Rem}(C_5)\subsetneq\operatorname{Rem}(C_3).
\]
In fact, for every \(n\ge3\),
\[
\operatorname{Rem}(C_{n+2})\subseteq\operatorname{Rem}(C_n).
\]
For \(n\in\{3,5,7,9\}\), the exact state counts in *complete minimal deterministic finite automata* are respectively
\[
6,\quad18,\quad102,\quad1098.
\]
The corresponding accessible-state counts of the direct intersection determinization, with all rejecting tuples collapsed to one dead state, are \(6,24,230,8936\). All three successive strictness witnesses are supplied and verified.

## Assumptions and scope
All cycles are finite, simple and labeled in cyclic order. An orientation chooses one direction of each undirected edge. A word is accepted by its oriented-graph automaton if it labels at least one walk starting at any vertex; an empty walk accepts the empty word. The deterministic state counts include a rejecting sink when present. A word rejected by any one orientation is absent from the remanent intersection. The exact state-count assertion concerns only the four displayed orders, whereas the inclusion assertion holds for every \(n\ge3\).

## Proof
**Graph homomorphism inclusion.** For each \(n\ge3\), define a vertex map from \(C_{n+2}\) to \(C_n\) by the cyclic image walk
\[
0,1,\ldots,n-1,0,1,0.
\]
The first and last symbols are the images of the same initial/final vertex, so the intermediate images describe all \(n+2\) edges of \(C_{n+2}\). Each consecutive pair is an edge of \(C_n\). Pulling back any orientation \(\mathcal O\) of \(C_n\) along this homomorphism gives an orientation of \(C_{n+2}\), and a signed walk in the pullback maps to a signed walk in \(\mathcal O\). Thus the language of the pullback is contained in the language of \(\mathcal O\). Intersecting over the orientations of \(C_n\) gives \(\operatorname{Rem}(C_{n+2})\subseteq\operatorname{Rem}(C_n)\).

**Strictness.** The words `++-++`, `++-+-++`, `++-+-+-++` are in the remanent languages of \(C_3,C_5,C_7\), respectively, but not those of \(C_5,C_7,C_9\). All accepting assertions follow by exhaustive evaluation of the respectively \(8,32,128\) orientations using the standalone checker. For the rejecting assertions, take the orientation whose edge-direction mask (edge \(i\to i+1\) coded by bit \(i\), indices modulo \(n\)) is respectively \(5,21,85\); the checker verifies the corresponding labeled path set becomes empty. Each mask is one explicit counter-orientation, so these witnesses prove all strict inclusions.

**Exact finite state complexity.** Fix one of the four orders \(n\). Number the \(2^n\) orientations by edge-direction masks. For each mask and letter, construct the integer-bitmask transition function on all subsets of the \(n\) vertices by taking the union of successor sets. For a word \(w\), the determinized state is the tuple of its \(2^n\) reachable vertex sets, initially the all-vertices tuple. If any component becomes empty, no continuation can be accepted by that orientation, so all such tuples can be identified with one absorbing rejecting state \(\bot\). All other tuple states accept, because all original vertices were final. Starting at the all-vertices tuple, breadth-first search follows both letters until no new tuple remains. This explores *every reachable deterministic state*, by induction on input length.

Initialize a partition into rejecting and accepting states. Repeatedly split blocks according to the triple consisting of current block, block of the \(+\)-successor and block of the \(-\)-successor. Stop when the number of blocks stabilizes. Each split separates states by an explicitly bounded distinguishing suffix; when stable, the block relation is a right congruence respecting acceptance, so no two states in a block are distinguishable by any suffix. Conversely, states in different blocks have a distinguishing suffix by induction over refinement rounds. This is exactly Myhill--Nerode equivalence on reachable states. Thus the stable number of blocks is the *provable* minimal complete DFA size, not a sampled lower bound.

The exact exhaustive run obtains the following pairs (reachable tuple states, stable equivalence classes):
\[
(6,6),\quad(24,18),\quad(230,102),\quad(8936,1098)
\]
for \(n=3,5,7,9\), respectively. The standalone `verify.py` implements every described finite step, checks transition-class invariance, and asserts the numerical results. Its loops are exhaustive over all orientation masks, all reachable states and all required block refinements, with no randomized or timeout-dependent criterion. The recurrence and exhaustive finite algorithm above, together with that reproducible source, constitute the exact finite proof certificate.

## Verification
Run `python3 verify.py` using the standard library. Its recorded output appears in `checks.txt`. It reports the four exact determinizations, the four minimized DFA sizes, and all three witness checks, ending in `ALL CHECKS PASS`. The code constructs the orientation transitions directly from the graph definition and never imports precomputed state counts as transition data; expected counts are assertions against independently computed objects. Neither checked logs alone nor an unbounded extrapolation establishes the theorem: the finite algorithm exhausts precisely the four finite cases, while the graph homomorphism argument proves the general inclusion.

## Relationship to prior work
Pujol introduced graph-based oriented automata and the remanent intersection over orientations; the first publicly posted version is dated 2026-09-08. The present claim uses that precise path-language notion to ask a more quantitative question: exact complete-DFA size for the first four odd cycles, alongside strict inclusion of their remanent languages. A previously observed run-avoidance description when clique and chromatic numbers coincide already handles triangles, and the word `++-++` was previously known as a five-cycle obstruction; neither observation determines the exact minima \(18,102,1098\) or the new strict comparisons between longer odd cycles. Closest indexed descriptions and searches did not yield these values. The full originating article could not be examined, so equivalent results in its body or in unindexed literature are an acknowledged priority risk rather than declared absent.

## Limitations
The exact DFA counts do not give a closed formula for all odd cycles. Apart from the elementary inclusion property, no claims are made for higher cycle orders or for arbitrary nonperfect graphs. The original paper was available to this review only in its indexed abstract, not as accessible full text, which leaves an unresolved but non-decisive novelty risk. The result has undergone only the documented self-review, not independent scientific audit or validation.

## References
1. Pujol, C. (2026), "Graph-based automata", arXiv:2609.08843v1 (first posted 2026-09-08). https://arxiv.org/abs/2609.08843.
2. Myhill--Nerode theorem, standard right-congruence characterization of minimal complete deterministic automata (used with its elementary partition-refinement proof given above).
