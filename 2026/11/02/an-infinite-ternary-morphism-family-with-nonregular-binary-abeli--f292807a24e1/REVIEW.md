# Scientific review

## Correctness (C): PASS
The theorem has an unconditional, all-parameter proof. The key nonstandard weighted-extremum recurrence is proved with an upper bound from all nine legal adjacent pairs and a constructive induction that embeds each maximizing factor beside precisely \(r\) maximum-weight substitution blocks. The coordinate count Fourier formula follows directly from the circulant substitution matrix. Reduction modulo two shows why a parity exception persists regardless of \(r\)'s parity; irrational rotation then produces a genuinely non-eventually-periodic subsequence. The final finite-quotient argument excludes \((r+1)\)-regularity. The two finite check programs reproduce every tested value, but are not treated as infinite proof.

## Originality (O): PASS, subject to residual priority risk
The closely related 2026 manuscript [1] proves one repetition-count instance \(r=3\) and raises other repetition counts in its concluding discussion. Its proof does not state or imply the uniform assertion for every \(r\ge4\), and simply invoking its fixed numerical case cannot yield all parameters. Its weighted-factor method is explicitly acknowledged. The Parikh-collinear regularity results [2] require rank-one substitution geometry, whereas \(rI+C\) has full rank; the positive theorem does not dominate this result. The additive-complexity investigation [3] does not give this parametric classification. Searches under the substitution, equivalent digit-count word, mod-three coding, and regularity formulations did not locate an equivalent family theorem. Priority risk remains because negative searches do not establish novelty and older work under an alternate terminology may exist.

## Value (V): PASS
The source paper expressly raises generalization beyond its isolated counterexample. Establishing nonregularity for every repetition count \(r\ge4\) answers a natural infinite subfamily of this parameter question. The proof requires a uniform extremal-window induction and a congruence-sensitive parity obstruction that also works when \(r\) is even; it is not a mere relabeling of the \(r=3\) statement. The result does not settle other alphabet sizes.

## Scope, comparison and limits
Relevant primary sources: [1] J.-P. Allouche et al., arXiv:2610.03837v1 (2026-10-02), inspected Sections 2–4 including the weighted-window argument and generalization discussion; [2] M. Rigo et al., arXiv:2405.18032; [3] P. Popoli et al., arXiv:2410.02409. The computational checks stop at finite indicated lengths; they cannot verify the infinite density property. No independent audit or priority review has occurred.

Self-review: passed. Independent audit: not yet performed.
