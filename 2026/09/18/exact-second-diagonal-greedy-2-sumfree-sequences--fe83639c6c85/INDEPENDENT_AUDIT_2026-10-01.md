# Independent mathematical audit — SCOPE-20260918-fe83639c6c85

Final disposition: **PASS**.

## Correctness
**PASS.** The modular proof was reconstructed. The four periodic residue blocks modulo M=9f-1 have pair-sum residues disjoint from the allowed set, and the two exceptional elements are separately compatible with strict 2-sumfreeness. The saturation table gives, for every excluded residue, two distinct earlier allowed summands after the specified period shift, so greedy induction proves the exact set formula for all f>=4. Reading the ordered set yields the displayed difference word; its period block contains a unique entry 2f, so it is primitive, and the one-step backward mismatch proves the stated preperiod is minimal. A separately written greedy enumeration reproduced the formula for f=4 through 14 over 300 terms each.

## Originality
**PASS.** The complete 15-page van Berkel–Bosma 2026 paper was inspected. It states general period/preperiod conjectures, proves d<f and d=f infinite families, and proves finite computational ranges up to f,d<=500, but does not prove the infinite second diagonal d=2f. Its formulas predict exactly period 2f+2 and preperiod f+2 there. Exact/synonymous searches under 2-sumfree and older 0-additive terminology found no prior all-f theorem. Older Queneau/Finch full texts were not available, so a historical-notation residual risk remains.

### Equivalent formulations
The equivalent historical terminology was searched; no earlier all-f second-diagonal theorem was located.

### Broader coverage
The inspected general theorems do not dominate the audited infinite family.

### Exact database or table
Known finite table entries do not mechanically prove the all-f residue formula.

### Claim versus prior implication
The final claim is a proof of a previously conjectural infinite subfamily, not a corollary of the source's proved families.

## Value
**PASS.** This replaces finite computation with a uniform proof on a natural infinite ray singled out by the current conjectural classification and supplies a stronger complete residue description. It is a motivated structural family, not an arbitrary finite instance.

## Source inspections
- **Periodicity conjectures for all 2-sumfree sequences** (arXiv:2609.18522v1): complete 15-page PDF, including Definitions 3 and 8, Conjectures 5 and 9, Theorems 12, 14, 15, 16 and 17 Assessment: NOT_COVERING_THE_INFINITE_SECOND_DIAGONAL; predicts it and verifies finite ranges only. Evidence: Theorem 14 proves only d=f; Theorems 16 and 17 are bounded computations, while Conjectures 5 and 9 govern all d.

## Residual risks
- The 1972 Queneau and 1992 Finch sources were not available in full text, so an older equivalent theorem under 0-additive notation remains a best-of-knowledge risk.
- The finite independent enumeration supports but does not replace the all-f modular proof.

The JSON companion records the structured four-part originality comparison and the same limitations.
