# Scientific review

## Correctness — PASS
The upper bound partitions windows by their residues modulo the decoration period. Active phases have disjoint binary-coordinate supports and at most twice as many Sturmian patterns as sampled positions; inactive phases contribute exactly the signature-count invariant. Irrational rotation density lets every occupied residue class simultaneously realize the upper bound by choosing widely spaced indices. The alphabet-disjointness hypothesis is essential for disjointness. The combinatorial extremal bound follows from the number of inactive phases and q-ary signature capacities; a de Bruijn cyclic sequence attains it. Both the minimum threshold inequality and the boundary cases \(k=1\), \(m=2\), \(k\ge m\) have been checked against these definitions. An exact verifier exhaustively corroborates 91 finite parameter/window triples but does not substitute for the universal proof.

## Originality — PASS on the compared literature
Schlortt's arXiv:2505.05627v1, Theorem 1.3 and Section 6, proves eventual linearity with an unspecified correction and provides individual examples. Its phase-decomposition argument is acknowledged. The exact profile for **each** window size and the sharp q-ary de Bruijn extremum for every period and window size are stronger and are not asserted in the inspected source. Le–Pavlov–Schlortt's arXiv:2508.13420v1 addresses low-complexity shift classification, not sharp finite-window decoration optimization; Kamae–Zamboni and Kamae–Rao establish the invariant and earlier low-complexity context. Exact claim/alias searches found no identical result; a June 2026 dissertation's full text was inaccessible, so historical priority remains a residual risk.

## Mathematical value — PASS
The 2025 result leaves the excess intercept \(C\) undetermined even for periodic decorations. The new finite signature invariant resolves that question constructively for each window size and each decoration, while the alphabet-sized extremal formula identifies an exact information-theoretic phase boundary. For example, with two decorative symbols and period twelve, the maximal excess is eight, attained at window size three. The theorem covers arbitrarily large periods and infinite families of Sturmian slopes, not just an isolated computational example.

## Scope and risks
The active-residue argument relies on irrational rotation codings and on alphabets disjoint from binary symbols. The de Bruijn construction is for unrestricted decorative vectors of fixed length. The work does not establish priority across inaccessible dissertations or alternative terminology; no independent assessment is implied.

Self-review: passed. Independent audit: not yet performed.
