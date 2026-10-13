# Scientific review

## Correctness — PASS

The exact domain is a single cyclic ternary word, four-symbol Hamming windows, radius one, and arbitrary positive cycle length. The volume-one Hamming ball contains exactly nine targets, excluding lengths at most eight. Every one of the \(3^9+3^{10}+3^{11}+3^{12}=787320\) indexed sequences at the next four lengths is evaluated with the explicit \(81\)-bit covering test; the numbers of valid sequences are \(0,0,0,48\). The explicit twelve-symbol witness is independently checked. The orbit calculation constructs *all* symbol permutations and rotations of the witness and its reversal; these form two disjoint 24-element sets whose union equals the set of all 48 enumeration winners. The standalone Python verifier and the separately written embedded C++ enumerator agreed; both independently encode the covering predicate. The finite exhaustive proof is valid because every candidate of relevant length is included, not because a partial search or solver terminated. Risk: as with any computer enumeration, an undetected shared conceptual interpretation error is possible; the definition and code are small and fully reproduced.

## Originality — PASS, with residual risk

The relevant 2003/2004 Chung–Cooper source was examined in full, including its **binary** small-parameter table (not a ternary length-four classification). The 2025 Chee–Etzion–Ta–Vu article was inspected in full: its tabulated small exact lengths are binary. Etzion's 2026 arXiv:2607.14840v1 gives constacyclic ternary Hamming covering-*sequence codes* (possibly multiple cycles), which do not entail the minimum length and complete orbit classification for a *single* ternary cycle. The full Ta–Vu 2026 preprint provides asymptotic existence bounds for large span, without the precise finite optimum. Searches for aliases including de Bruijn covering cycles, ternary radius-one length-four parameters, ordinary covering-code reductions, and cyclic Hamming ball covers found no prior source whose theorem implies the entire exact statement. The most plausible remaining risk is an earlier unindexed finite enumeration, not a theorem in an inspected source.

## Value — PASS

This is a natural finite parameter at the first nonbinary ternary Hamming-perfect span: the ordinary ternary radius-one covering-code sphere bound is attained by nine words, whereas requiring those codewords to appear as consecutive cyclic windows forces **twelve**, a sharp three-window or one-third overhead. Counting all optimizers and determining their symmetry type provides the complete equality-case classification, rather than a routine unmotivated code example. The precise obstruction clarifies the finite-vs-asymptotic and single-cycle-vs-multicycle distinctions highlighted by the literature.

## Scope and outstanding limits

No theorem for other alphabets, spans, or radii is claimed. The finite census is reproducible from the fully embedded standard-library verifier, but it is not an independently validated external proof. No unindexed finite table can be absolutely ruled out.

Self-review: passed. Independent audit: not yet performed.
