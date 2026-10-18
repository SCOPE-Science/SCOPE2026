# Review: sharp cyclic-gap thresholds for digit-appending walks

## Correctness — PASS

The exact normalized digit discrepancy, with a uniform threshold that does not depend on the appended digit count, forces every late step to have index increment equal to the appended digit length. An exact inequality on the periodic corrections reduces the question to a finite directed residue graph. Correction values outside \(\{0,-1\}\) move strictly and hence cannot lie on directed cycles; a cyclic-gap lemma completely characterizes cycles in either stable correction class. Finite-graph acyclicity yields the uniform \(M+h-1\) bound, and repeating the circular tour supplies the infinite walks. The proof addresses singleton correction classes, missing classes, and unbounded append counts. A dependency-free checker independently tests graph and arithmetic cases. Checks establish consistency but not proof of the all-parameter theorem.

## Originality — PASS, with residual risk

The first-public primary source is Kominers, *Uniform Bounds for Digit-Appending Fibonacci Walks* (arXiv:2512.06446v1, 2025-12-06), sections 1–4. The closest theorems establish termination for Fibonacci/Lucas families and do not impose or cover the resonance condition with characteristic root equal to the appending base and arbitrary root-of-unity corrections. The earlier Miller et al. works arXiv:2204.08138 and arXiv:2010.14932 likewise address distinct sequences. Targeted exact-language, parameter, equivalence, and stronger-coverage searches found no same-family classification in the accessible research index or published sources. A hidden implicit observation about periodic corrections remains a genuine risk; search absence alone cannot establish uniqueness.

## Mathematical value — PASS

The theorem resolves a natural sharp boundary left by the termination-versus-infinite-walk distinction for exponentially growing number-theory sequences. An infinite parameter family of integer recurrences with characteristic polynomial dividing \((X-b)(X^h-1)\) has a complete classification by an explicit combinatorial invariant. It identifies both the only two correction values capable of sustaining infinite walks and their optimal cyclic spacing, and strengthens negative cases to a finite length bound uniform in digit budget when no critical values occur. The result is a natural complete resonant-family classification rather than a numerical increment or a reformulation of a known result.

## Scope and risk

Generality is limited to bounded periodic integer corrections; arbitrary bounded nonperiodic corrections and other dominant roots remain open for this argument. The upper bound is not claimed optimal. Literature access cannot eliminate earlier equivalent statements under different terminology.

Self-review: passed. Independent audit: not yet performed.
