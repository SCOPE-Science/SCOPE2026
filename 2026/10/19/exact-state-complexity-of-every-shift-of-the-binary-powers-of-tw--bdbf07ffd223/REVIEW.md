# Review of the exact shifted powers-of-two automaton count

## Correctness — PASS

The theorem first identifies the accepted binary language exactly, including leading-zero padding and the exceptional accepted zero when the shift is a power of two. For nonpowers, it then classifies all right quotients into the root, sink, a family of infinite quotients indexed by an initial run of ones, finite two-element quotients indexed by the common-prefix overlap, and all padded-word singleton suffixes. Distinguishing cardinalities, lengths, and exceptional words proves the quotients pairwise inequivalent; explicit prefixes prove reachability. The power-of-two case is counted separately, including the boundary shift \(c=1\). The derived sharp dyadic bounds are immediate from the word-length inequalities and explicitly attaining shifts. This is an infinite Myhill–Nerode proof, not an extrapolation from a computation. Independently constructed automata and exact minimization agree for every shift from \(1\) to \(4095\), with additional arithmetic checks against the intended output function.

## Originality — PASS within examined evidence

Moradi, Rampersad, and Shallit's Theorem 21 (arXiv:2512.10017, §4.3) proves the asymptotic \(O(\log c)\) bound for the same indicator and msd-first convention; its explicit unminimized construction does not state an exact formula or a sharp dyadic state-count range. The separately examined 2026 paper on shifts of the Fibonacci word concerns another sequence and cites only the logarithmic behavior of the powers-of-two example. Other general tail-state-complexity results do not assert the quotient classification. Directed searches for minimal DFAs for translated powers of two, complemented binary patterns, right quotients, and precise automaton sizes yielded no corresponding exact theorem. Comparable research records concern synchronizing reset ranks, Thue–Morse odd parts, or string attractors, not this shifted-sparse-indicator state count. Related results about automata for shifts of the Thue–Morse word were compared by implication and concern a different sequence. The remaining risk is an unindexed or differently expressed earlier formula, including one recoverable from prior constructions with additional arguments. This self-review does not certify priority independently.

## Mathematical value — PASS

The 2025 source singles out the shifted powers-of-two sequence as an example of unusually small state complexity and proves only its logarithmic order. The exact minimum is thus a natural unresolved quantitative refinement, not an arbitrary numerical slice. The formula explains state merging through initial-run and padded-prefix overlap, reveals sharp variation of nearly a factor of two among shifts of identical bit length, and provides minimal state costs for every positive shift. It supplies a structural Myhill–Nerode classification rather than a list of finite examples. It does not claim a general theorem for all sparse automatic sequences or for other digit directions and bases.

## Closest literature and limitations

- D. Moradi, N. Rampersad, J. Shallit, *Complexity of Linear Subsequences of \(k\)-Automatic Sequences*, arXiv:2512.10017, Theorem 21, initially 2025-12-10: logarithmic size for the same sequence, no exact minimum given.
- D. Moradi, P. Popoli, J. Shallit, I. Vukusic, *State Complexity of Shifts of the Fibonacci Word*, arXiv:2603.18858, initially 2026-03-19: related complexity framework but a different characteristic sequence.
- H. Zantema, W. Bosma, *Complexity of Automatic Sequences* (2022): broad estimates for shifted/tail automatic sequences without the present exact quotient classification.

All state counts include a reachable rejecting sink and require correct output for arbitrarily padded inputs. Finite checker cases provide reproducibility but not independence or a formal proof. Overlap search does not exclude every possible unpublished or unindexed equivalent result.

Self-review: passed. Independent audit: not yet performed.
