# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260919-aa232bc40569`

## Correctness — PASS

The full primary 13-page cubic-tail paper was inspected. It proves only the eventual window \(g_n<S_n^{-1}<g_n+2/F_n\) and the floor formula. Independently, expanding Binet's formula gives the exact analytic series \(S_n=5\sqrt5\,x^3A(arepsilon x^2)\) with \(x=arphi^{-n}\), and \(A(0)
e0\), so its reciprocal has a convergent local expansion. I independently recomputed the first coefficients symbolically and obtained exactly \(\kappa=(948+72\sqrt5)/3509\) and \(\lambda=(18175-11739\sqrt5)/3666905\). This proves the displayed \(F_n^{-1}\) and parity-dependent \(F_n^{-3}\) terms; analyticity gives the \(O(F_n^{-5})\) remainder and arbitrary further terms.

### Correctness sources

- assigned RESULT.md and verify.py
- independent symbolic Binet-series computation
- Hwang–Park–Song, arXiv:2609.18179 full 13-page text
- earlier reciprocal-Fibonacci literature listed by the primary paper

### Correctness risks

- The theorem concerns the cubic full tail only.
- No least finite starting index for the asymptotic expansion is asserted.

## Originality — PASS

The fully inspected Hwang–Park–Song paper gives the exact same \(g_n\) but only a coarse \(2/F_n\) upper error window and an exact floor formula. Fresh Resultary searches returned no theorem with the sharp residual constant, the next parity coefficient, or the convergent all-order local expansion. Thus the audited claim is a genuine quantitative refinement rather than a restatement of the floor theorem.

### equivalent_formulations

Searches:
- Resultary searches for cubic reciprocal Fibonacci residual constants, parity term, and all-order Binet expansion

Evidence:
- Only the audited theorem matched the sharp coefficients.
- The source paper's theorem is an inequality window, not an asymptotic expansion.

Reasoning:
Equivalent formulations in \(F_n^{-1}\) and in the local Binet variable \(x=arphi^{-n}\) were compared.

### broader_coverage

Searches:
- Hwang–Park–Song 2026 full text
- Li–Yang–Yuan 2025 generalized-Fibonacci asymptotic literature

Evidence:
- The 2026 full text contains the algebraic \(2/F_n\) window and floor theorem but no sharp scaled residual limit.
- The older general asymptotic work supplies background rather than the audited exact coefficients.

Reasoning:
A difference-to-zero approximation does not imply the sharp residual constants without further expansion.

### exact_database_or_table

Searches:
- current Resultary reciprocal-Fibonacci findings

Evidence:
- No known-table or database entry for the two constants was found.

Reasoning:
The result is an infinite asymptotic identity, not a tabulated finite computation.

### claim_vs_prior_implication

Searches:
- claim comparison with Theorem 4.1 of arXiv:2609.18179

Evidence:
- The source only bounds the residual between zero and \(2/F_n\); the audited leading constant is about \(0.316/F_n\) and includes a next oscillatory term.

Reasoning:
The prior theorem leaves the sharp coefficient and parity correction undetermined.

### source_inspections

- **Continuous approximation to the reciprocal sum of the cubes of Fibonacci numbers** — https://arxiv.org/abs/2609.18179. Trigger: Direct primary source for \(g_n\) and the \(2/F_n\) window. Material read: Complete 13-page primary paper, including all theorem/proof pages and references. Method: Full primary-text statement and formula comparison. Assessment: NOT COVERING the audited sharp expansion. Evidence: Theorem 4.1 gives \(g_n<S_n^{-1}<g_n+2/F_n\); no \(\kappa\), \(\lambda\), or all-order local series is stated.
- **Assigned symbolic verifier** — artifacts/verify.py. Trigger: Exact radical simplification of the first two residual coefficients. Material read: Complete source file. Method: Line-by-line inspection and independent symbolic recomputation. Assessment: Correct corroboration. Evidence: The independent expansion reproduces both exact constants.

### checked_sources

- Hwang–Park–Song arXiv:2609.18179 full text
- current Resultary Fibonacci-tail searches
- assigned RESULT.md and verifier

### residual_risks

- Historical reciprocal-Fibonacci literature is broad; a differently phrased all-order Binet expansion remains a small residual risk, though none was located.

## Scientific value — PASS

Replacing the source's coarse coefficient \(2\) by the exact leading residual constant, resolving the first parity oscillation, and identifying a convergent all-order mechanism is a natural sharp refinement of a current exact floor theorem. It gives reusable asymptotic information rather than a cosmetic numerical improvement.

### Value sources

- Hwang–Park–Song cubic-tail theorem
- audited exact residual expansion

### Value risks

- No new floor formula or general arbitrary-power theorem is claimed.

## Limitations

- The theorem concerns only reciprocal Fibonacci cubes.
- No new exact floor formula or least threshold is claimed.
- Originality is best-of-knowledge over a broad historical literature.

## Disposition

**PASSED**
