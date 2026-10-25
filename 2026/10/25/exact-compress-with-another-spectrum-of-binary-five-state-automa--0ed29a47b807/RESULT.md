# Exact compress-with-another spectrum of binary five-state automata

## Finding
For an automaton \(\mathcal A=(Q,\{a,b\},\delta)\) with \(Q=\{0,1,2,3,4\}\), let \(\mu_{\mathcal A}(q)\) be the least length of a word \(w\) for which there exists some \(p\in Q\setminus\{q\}\) with \(\delta(q,w)=\delta(p,w)\). For a synchronizing automaton set \(\tau(\mathcal A)=\max_{q\in Q}\mu_{\mathcal A}(q)\).

Among all \(5^{10}=9,765,625\) ordered labeled binary five-state automata, exactly \(8,063,385\) are synchronizing. The full distribution of \(\tau\) on that class is
\[
\begin{array}{c|rrrrr}
\tau&1&2&3&4&5\\\hline
\#\mathcal A&3,444,345&3,763,200&738,000&108,720&9,120.
\end{array}
\]
Thus the largest possible value is exactly \(5\). All \(9,120\) maximizers are strongly connected, and they form exactly \(38\) isomorphism classes under simultaneous state relabeling and optional interchange of the two letters. Every class has a full labeled orbit of size \(240\). Classified by the unordered pair of ranks of the two letter maps, the \(38\) classes split as \((3,4):8\), \((4,4):12\), and \((4,5):18\).

The accompanying exact census contains the least integer encoding of each of the \(38\) classes and all \(9,120\) labeled extremal encodings.

## Assumptions and scope
The transitions \(a,b:Q\to Q\) are arbitrary total maps, with the two alphabet letters **ordered** and the five states **labeled** in the census. No initial state or acceptance set is needed. Synchronizing means that some word maps every state into the same state. Strong connectivity is *not* imposed on the census; it is a proved property of all extremizers. A state permutation \(\pi\) conjugates each map by \(\pi\circ a\circ\pi^{-1}\) and \(\pi\circ b\circ\pi^{-1}\); exchanging the letters is also an allowed isomorphism. The rank of a map is the number of distinct images it takes.

All map pairs are encoded as ten base-five digits, with images of states \(0,1,2,3,4\) under \(a\) first and then under \(b\), least significant digit first. The integer range is \(0\) to \(5^{10}-1\), inclusive. A listed canonical representative is the smallest encoding in its state-permutation/letter-swap orbit.

## Proof
First prove the standard pair criterion: a deterministic finite automaton is synchronizing exactly when *every* two distinct states admit a common-image word. One direction is immediate. Conversely, begin with the entire state set; whenever its image has at least two elements, choose two current image states and append their merging word. The image cardinality decreases strictly. Finitely many iterations reach one state.

For a fixed transition pair, form the directed graph on the ten unordered two-element subsets \(\{p,q\}\). Each letter maps a pair either to a singleton (a successful merge) or to another unordered pair. Define \(d(p,q)\) to be the least positive word length merging the pair, or infinity if no such word exists. Precisely those pairs merging under one letter have distance one. For every other pair, the exact recurrence is
\[
d(p,q)=1+\min\{d(\delta(p,a),\delta(q,a)),d(\delta(p,b),\delta(q,b))\},
\]
where a singleton successor has zero remaining distance. Reverse breadth-first search from all one-step merging pairs computes exactly the finite distances, with unreached pairs infinite. Correctness follows from the first-letter decomposition of every merging word. By the pair criterion, an automaton is synchronizing if and only if all ten pairs have finite distances. Moreover,
\[
\mu_{\mathcal A}(q)=\min_{p\in Q\setminus\{q\}}d(p,q),\qquad
\tau(\mathcal A)=\max_{q\in Q}\mu_{\mathcal A}(q).
\]

The source file `census.cpp` implements this recurrence while looping through every ten-digit base-five transition encoding. It records the exact synchronizing count and the five-bin histogram, hence gives the claimed universal bound, sharpness, and 9,120 extremal encodings. This is an exhaustive finite proof, not a statistical sample.

Independently, `check_independent.cpp` uses a **synchronous fixed-point recurrence**, not reverse breadth-first search: at stage \(t\), a pair is marked exactly if one of its two successor pairs either merges immediately or was already marked by stage \(t-1\). The previous-stage mask is held fixed during each iteration. A simple induction on \(t\) shows that the stage at which the pair first becomes marked is its exact shortest merging length. There are ten pair states, so any mergeable pair has a simple path of at most ten steps. Independently enumerating every one of the \(9,765,625\) transition pairs reproduces the exact same five-bin histogram and independently records all \(9,120\) extremal integers.

For classification, `census.cpp` applies all \(5!=120\) state permutations and both letter orders to each extremal and selects the smallest integer representation. Exactly \(38\) distinct canonical values occur. The separate `verify.py` recomputes each complete orbit directly from the canonical representative in Python. It verifies that every orbit has \(240\) members, that the \(38\) orbits are pairwise disjoint, and—crucially—that their union agrees *exactly* with the full independently enumerated list of \(9,120\) extremals. The same independent program checks strong connectivity of each of these \(9,120\) automata and counts the ranks of both letter maps in each class. These checks establish both the classification and its completeness.

## Verification
The human-readable summaries `census_report.txt` and `check_report.txt` and the sorted `extremal_ids.txt` are fully determined by the included C++ sources. On a machine with `g++` supporting C++17 and Python 3, run `python3 verify.py` in the directory containing the embedded files. The verifier freshly compiles and runs both complete enumerators, checks exact report text and the complete list of extremal integers, independently constructs the \(38\) symmetry orbits and checks their disjoint union, independently tests all representative shortest merging lengths by enumerating binary words of lengths \(1\) through \(5\), and checks all \(9,120\) extremizers for strong connectivity and their letter-rank types. Success prints `VERIFY_OK`.

The full finite enumeration is independently reproduced by two different pair-graph methods; the required logical link between the pair distances and the automaton-wide invariant is proved above. All claimed counts and classifications are testable from these included local source files; no online database or external dependency other than the noted compilers/interpreters is required.

## Relationship to prior work
Marek Szykuła's August 2026 survey introduces and motivates the compress-with-another threshold and open upper-bound questions. Its results and examples do not state the exhaustive binary five-state threshold distribution or symmetry classification. Qichao Wang's October 2026 article determines the threshold for a special family whose state counts are \(3p\) with \(p\ge3\), starting at nine states, and therefore cannot cover the all-automata five-state statement.

The published five-state 1-avoiding-threshold census establishes a different invariant: avoiding a chosen state from the image of the **whole** state set. Its maximum \(8\) and four extremal classes do not entail the present five-bin compression spectrum. The published five-state triple-rendezvous census concerns the shortest word merging **some three-element subset** rather than merging each *prescribed* state with any partner. Although both prior censuses confirm the total count of \(8,063,385\) synchronizing ordered labeled automata, they do not supply the \(9,120\) compression extremizers or the 38-class decomposition.

Targeted searches of recent primary publications, mathematical research records, and equivalent formulations did not locate the present histogram or its full orbit classification. Search failure alone is not proof of global novelty; see the limitations.

## Limitations
The theorem is a complete **finite five-state binary census**, not an all-state theorem and not a proof of a general linear bound. The isomorphism classes are defined only using state relabeling and alphabet interchange; changing the equivalence notion can change the count of classes. The source evidence establishes the figures through exhaustive finite algorithms and explicitly checkable invariants, not through a short closed-form symbolic count. Unindexed prior computations may contain the same data, and the complete text of one related larger-state-family preprint could not be fully examined, although its stated parameter domain excludes five states. Independent scientific validation has not been performed.

## References
1. Marek Szykuła, *Synchronizing Automata: Open Problems*, arXiv:2608.24245, first posted 25 August 2026, DOI 10.4204/EPTCS.451.3.
2. Qichao Wang, *The compress-with-another threshold of Szykuła's Figure 3 family*, arXiv:2610.07044, first posted 5 October 2026.
3. *Four extremal five-state binary avoiding-threshold classes*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-four-extremal-five-state-binary-avoiding-threshold-classes--add2e90918b8.
4. *The five-state binary triple-rendezvous extremal is unique*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-the-five-state-binary-triple-rendezvous-extremal-is-unique--c176f0fc06e0.
