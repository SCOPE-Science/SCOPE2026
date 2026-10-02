# Independent mathematical audit — Support-containment obstruction in a published length-24 ternary trifferent-code witness

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS** — Exact arithmetic on the six printed rows gives \(a=r_2+r_3=100112202000102002022001\) and \(b=r_1+r_4=211221201011101002221122\), with \(\operatorname{Supp}(a)\) a strict subset of \(\operatorname{Supp}(b)\). Hence the printed row space is not minimal. The source paper proves that a ternary linear code is trifferent exactly when it is minimal, so this already invalidates the claimed witness. Independently, the triple \(a,b,-a\) has no coordinate containing all three field symbols. The first six columns have determinant \(2\) modulo \(3\), verifying that the printed matrix still has rank six. An independent calculation reproduced every certificate datum.

Checked sources: Assigned RESULT.md and inspected verifier source; Bishnoi--D'haeseleer--Gijswijt--Potukuchi 2024 full journal HTML; Independent exact matrix calculation; Targeted correction/erratum search.

Residual correctness risks: The finding concerns the matrix as printed; it does not disprove existence of another \([24,6]_3\) trifferent code or the theorem if a corrected witness exists..

## Originality

**PASS** — The 2024 paper itself prints the exact matrix and uses it as the inner \([24,6]_3\) trifferent code in the proof of its explicit rate theorem, while also proving the minimal-code/trifferent equivalence that makes support containment decisive. Targeted searches for the exact certificate strings, errata, corrections, and later blocking-set work found no public correction or prior statement of this defect. Resultary likewise returned only the audited correction.

### Equivalent formulations

Searches/sources: Resultary query: trifferent [24,6]_3 matrix minimal code support containment correction; Web searches for both exact certificate codewords; Search for erratum/correction to DOI 10.1112/jlms.12938.

Evidence: The Resultary exact hit was the audited record. Searches for the two exact row-combination strings returned the original paper rather than an earlier correction. The paper's Theorem 6.2 makes strict support containment exactly equivalent to failure of trifference for a ternary linear code.

No earlier equivalent certificate or public correction was located.

### Broader coverage

Searches/sources: Bishnoi--Tomon 2026 explicit blocking-set/minimal-code paper; Later citations of the 2024 trifferent construction; Strong-blocking/minimal-code correction searches.

Evidence: The later work develops new blocking-set and minimal-code constructions but the inspected accessible material does not supply a correction of this printed \([24,6]_3\) matrix. No stronger source was found that already invalidates or replaces the exact published witness.

No inspected broader correction covers the specific matrix defect.

### Exact database or table

Searches/sources: Resultary exact theorem search; Search of the current 2024 journal HTML for the printed matrix and \([24,6]_3\) claim.

Evidence: The journal still displays the same matrix in the proof of Theorem 1.7. No separate erratum/correction record was found in the targeted searches.

The certificate is tied to one exact published matrix, so exact source matching is decisive and supports originality.

### Claim versus prior implication

Searches/sources: Does the 2024 minimal-code equivalence itself imply the matrix is bad?; Does the published rank claim imply trifference?.

Evidence: The source theorem says how support containment would refute trifference, but the source does not identify the required pair of codewords. Rank six alone does not establish minimality or trifference.

The new content is the explicit nested-support witness extracted from the printed rows.

### Source inspections

- **Blocking sets, minimal codes and trifferent codes** — PRIMARY_SOURCE_DEFECT.
  Identifier: https://doi.org/10.1112/jlms.12938
  Trigger: Primary publication containing the claimed matrix and the equivalence used to test it.
  Material read: Complete open journal HTML around Theorem 6.2 and the proof of Theorem 1.7, including the printed \(6\times24\) matrix.
  Method: lawful open-access full text
  Evidence: The paper states that the printed matrix generates a \([24,6]_3\) trifferent code; the audited row combinations contradict that claim.
- **Explicit constructions of optimal blocking sets and minimal codes** — NO_CORRECTION_FOUND.
  Identifier: https://arxiv.org/abs/2411.10179
  Trigger: Later work by an overlapping author that could plausibly contain a correction.
  Material read: Abstract and accessible publication/search material; targeted searches for the length-24 witness/correction produced no match.
  Method: lawful open-access material
  Evidence: The later work concerns new blocking-set constructions; no correction of the audited matrix was located in the material inspected.

Residual originality risks:
- A private, unindexed, or very recent correction could exist outside the searched public sources.

## Scientific value

**PASS** — The matrix is the explicit inner code used in a published asymptotic concatenation proof. A short exact certificate that the printed witness fails its required property is a motivated reproducibility correction with direct consequences for that proof, while the claim carefully avoids overstating what it disproves.

Residual value risks: A different valid \([24,6]_3\) witness could repair the original theorem without changing its final existence claim..

## Final assessment

The final claim survives unchanged on correctness, originality, and scientific value. No change to `RESULT.md` or `SLOGAN.txt` is proposed.

Earlier review evidence remains separately identified and is not relabeled as this independent assessment.

This is a best-of-knowledge mathematical audit, not formal proof-assistant verification or a guarantee against undiscovered prior art.
