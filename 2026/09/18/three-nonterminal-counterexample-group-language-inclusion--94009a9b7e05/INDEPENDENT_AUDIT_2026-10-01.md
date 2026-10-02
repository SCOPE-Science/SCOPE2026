# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260918-94009a9b7e05`

## Correctness — PASS

The counterexample follows directly from the published definitions. The three-production grammar generates only the terminal word \(x_1x_1'\), which freely reduces to the identity in the chosen free group. Yordzhev's Definition 3.1, however, keeps the first component in the literal free monoid, so \(\langle x_1x_1',e\rangle\) is not the monoid identity. The published closure recurrence places that label in the final \(g_{1,4}\), and Algorithm 4.4 rejects whenever the set is nonempty but not the identity singleton. The primary PDF confirms the mismatch: Theorem 2.1 uses membership in the group language, while Theorem 4.3 and Algorithm 4.4 replace it by literal empty-word equality. The assigned exact verifier independently reproduces the four-step recurrence.

### Correctness sources

- Yordzhev, Filomat 38 (2024), DOI 10.2298/FIL2412157Y
- assigned RESULT.md
- artifacts/verify_counterexample.py
- artifacts/verification.txt

### Correctness risks

- The counterexample addresses the theorem and algorithm under the published algebra \(U=\Sigma^*\times T\); it does not analyze a modified quotient construction.

## Originality — PASS

Current semantic and theorem-number searches located the published paper and the audited correction but no erratum, published counterexample, or broader theorem already identifying this specific false negative. The novelty claim is appropriately narrow: the explicit three-nonterminal witness and diagnosis of the free-monoid versus group-equality mismatch.

### equivalent_formulations

Searches:
- Resultary semantic search for Yordzhev Theorem 4.3 Algorithm 4.4 counterexample
- exact DOI/arXiv/theorem-number searches

Evidence:
- The audited finding was the only matching published correction returned.

Reasoning:
Equivalent formulations as failure of condition (i) iff condition (iv), failure of the semiring path test, and literal-versus-group equality were checked.

### broader_coverage

Searches:
- Yordzhev's earlier Theorem 2.1 and later Theorem 4.3 in the same paper
- formal-language/group-language correction searches

Evidence:
- The earlier theorem actually exposes the distinction used by the counterexample; no stronger published repair or counterexample was found.

Reasoning:
The primary source is broader in problem scope but does not imply its own later criterion is false.

### exact_database_or_table

Searches:
- Resultary current formal-language findings
- published erratum/correction searches for DOI 10.2298/FIL2412157Y

Evidence:
- No exact correction database entry or erratum was located.

Reasoning:
This is not a known finite table result.

### claim_vs_prior_implication

Searches:
- direct implication check from the definitions of \(U\), Theorem 4.3, and Algorithm 4.4

Evidence:
- The source's literal identity test rejects the nonempty identity-representing terminal word.

Reasoning:
No prior theorem located turns this witness into a previously stated corollary; the contradiction is the new correction.

### source_inspections

- **On A. V. Anisimov's problem for finding a polynomial algorithm checking inclusion of context-free languages in group languages** — https://doi.org/10.2298/FIL2412157Y. Trigger: Primary source containing the disputed criterion and algorithm. Material read: Full published PDF, with detailed inspection of Theorem 2.1, Definition 3.1, Theorem 4.3, and Algorithm 4.4. Method: Primary full-text definition and algorithm trace. Assessment: The primary text confirms the counterexample's exact mismatch. Evidence: Theorem 2.1 tests group-language membership, while Theorem 4.3 uses the singleton empty word and Algorithm 4.4 tests literal monoid identity.
- **Assigned exact recurrence verifier** — artifacts/verify_counterexample.py. Trigger: Compact replay of the published closure recurrence. Material read: Complete source and saved output. Method: Line-by-line inspection and independent recurrence check. Assessment: Correct corroboration. Evidence: The generated group word freely reduces to identity while the final semiring label set is not the identity singleton.

### checked_sources

- Yordzhev published full text
- arXiv:2602.18305
- assigned exact verifier
- current Resultary and correction searches

### residual_risks

- An informal or poorly indexed observation could exist; no such source was located.

## Scientific value — PASS

A three-nonterminal false negative in the central correctness theorem and advertised algorithm is a substantive correction: it invalidates the published criterion in its stated algebra and identifies exactly what any repair must change. The witness is small enough to be independently checked from the definitions.

### Value sources

- Yordzhev Theorem 4.3 and Algorithm 4.4
- assigned explicit witness

### Value risks

- The result does not prove undecidability or rule out a corrected algorithm.

## Limitations

- The conclusion is restricted to the published definition of \(U\).
- No claim is made about the complexity or correctness of a redesigned quotient/group-equality semiring.
- Originality is best-of-knowledge.

## Disposition

**PASSED**
