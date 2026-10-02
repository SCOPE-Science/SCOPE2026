# Independent mathematical audit — 2026-10-01

## Final claim
The generalized packing-covering conjecture holds for every linear code of redundancy at most fifteen over every finite field.

## Correctness — PASS
The parent paper's full text was inspected. Its general dimension cap, ball-covering inequality, established-case reductions, and large-alphabet theorem all apply beyond redundancy fourteen. Exact independent integer recomputation at redundancy fifteen gives 62 residual tuples: 6 are excluded by the low-dimension theorem, 55 by the binomial covering inequality, leaving only the binary triple with order three and covering radius six. For that triple, the dual fourth-weight argument, nine-coordinate shortening, two-space multiplicity bound, and exact covering volume give length at most 73 and then a contradiction. The finite arithmetic was independently reproduced.

## Originality — PASS
Best-of-knowledge originality passes for the all-field redundancy-fifteen extension.

### Equivalent formulations
Searches: generalized packing-covering redundancy fifteen all finite fields; generalized Hamming weight versus generalized covering radius redundancy 15
Evidence: The parent 2026 paper, including its revised full text, proves the universal theorem only through redundancy fourteen and explicitly identifies the first binary redundancy-fifteen residual triple. A 2026-09-17 record closes the binary redundancy-fifteen case only.
Reasoning: The assigned final claim is universal over every finite field, so binary-only coverage is not equivalent.

### Broader coverage
Searches: Auxiliary Codes and the Generalized Packing-Covering Conjecture full text; Resultary binary generalized packing-covering through redundancy 15
Evidence: The parent theorem is broader in method but stops at redundancy fourteen. The earlier published record is broader in no other field and covers only binary codes at redundancy fifteen.
Reasoning: Neither source dominates the all-field threshold claimed here.

### Exact database or table
Searches: Resultary exact search for redundancy fifteen all fields
Evidence: No earlier all-field redundancy-fifteen theorem was located; the earlier exact hit is binary only.
Reasoning: The 62-tuple exact finite reduction supplies the missing nonbinary closure.

### Claim versus prior implication
Searches: parent Lemma 4.1 and Appendix A; binary redundancy-fifteen record
Evidence: The parent provides reusable inequalities but does not perform the redundancy-fifteen nonbinary enumeration. The binary record supplies only the final binary residual obstruction.
Reasoning: Combining the two prior results still requires the nonbinary finite reduction; the all-field theorem is not a stated or automatic corollary without that check.

### Source inspections
- **Auxiliary Codes and the Generalized Packing-Covering Conjecture** (arXiv:2609.19098): Provides all imported lemmas and explicitly stops the universal theorem at redundancy fourteen. Material read: Complete ten-page preprint including the syndrome formulation, auxiliary criterion, dimension cap, redundancy-fourteen proof, conclusion, and appendices. Evidence: The conclusion identifies redundancy fifteen, order three, covering radius six as the first binary residual triple.
- **Binary generalized packing-covering through redundancy 15** (Resultary 2026/9/17/SCOPE014): Covers the binary case only, with the same line-cap obstruction used as one component of the assigned all-field result. Material read: Complete RESULT.md. Evidence: Its limitations explicitly state that it does not claim the all-field redundancy-fifteen theorem.

Checked sources: arXiv:2609.19098 full text; Resultary 2026/9/17/SCOPE014; assigned verify.py and verification.txt; Resultary published-record search
Residual risks: The parent theorem and the assigned extension are very recent, so a simultaneous unindexed all-field follow-up remains possible.

## Scientific value — PASS
The result closes the next universal redundancy threshold explicitly left open by the newest general theorem. The finite nonbinary reduction plus the structural binary obstruction produces a complete field-independent statement rather than a single parameter computation.

## Conclusion
The unchanged scientific claim passes correctness, best-of-knowledge originality, and scientific-value review.
