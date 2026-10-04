# Review

## Correctness
PASS. The frame operator is computed explicitly through the row Gram matrix. Each off-diagonal vanishing condition is equivalent to divisibility of the frequency mask by the cyclotomic polynomial of the exact order of the corresponding difference character. Pairwise coprimality of the required cyclotomic factors gives the cardinality divisibility lower bound at \(X=1\), and the digit construction has exactly the product mask needed for equality. The singleton boundary case is included. Exact exhaustive replay on three small prime-power groups agrees with the theorem.

## Originality
PASS. The closest inspected source, Frederick--Mayeli, develops finite frame spectral pairs and lifting constructions but does not state the exact prime-power minimum in terms of distinct \(p\)-adic difference scales. Lam--Leung supplies general vanishing-sum machinery, and Malikiosis supplies cyclic cyclotomic/spectral structure, but neither inspected statement gives this tight-frame minimum or the canonical digit optimizer for arbitrary \(A\). Focused searches for prime-power tight exponential frames, cyclotomic balancing, and \(p\)-adic difference-scale classifications did not locate an implication covering the claim. Residual risk is an equivalent formulation in less directly indexed harmonic-frame literature.

## Value
PASS. The result extracts a natural invariant of an arbitrary subset of a cyclic prime-power group and turns it into an exact optimal frame size, with a canonical optimizer. It separates geometric complexity relevant to tight exponential oversampling into the number of active \(p\)-adic difference scales, providing a reusable structural lemma rather than a finite table or an arbitrary special case.

## Closest literature and limitations
The theorem is positioned inside the finite frame-spectral framework of Frederick--Mayeli and uses classical cyclotomic vanishing ideas associated with Lam--Leung and cyclic spectral-set work such as Malikiosis. It is limited to prime-power cyclic groups and unweighted frequency sets; it does not classify all minimizers or all oversampling levels.

Same-model review: passed. Independent audit: not yet performed.
