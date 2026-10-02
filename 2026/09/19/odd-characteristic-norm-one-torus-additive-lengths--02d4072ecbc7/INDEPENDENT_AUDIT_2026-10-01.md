---
audit_date: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

For every odd prime power \(q\), the norm-one torus \(T\subset \mathbb F_{q^2}^{*}\) has exact additive lengths determined by \(\chi(1-4/N(S))\); in particular \(|T+T|=(q^2+2q+3)/2\), every nonzero element has length at most three, and \(T+T+T\) omits exactly zero when \(q\equiv1\pmod 3\).

## Correctness — PASS

The two-sum criterion was reconstructed from the quadratic \(X^2-SX+S/\bar S\): its normalized discriminant is \(1-4/N(S)\), and Frobenius conjugation gives exactly the zero-or-nonsquare condition. Norm fibers then give the two-sum cardinality. For three summands, the map \(\beta\mapsto N(S-\beta)\) from \(T\) has fibers of size at most two, so its image of size at least \((q+1)/2\) must meet the equally large admissible norm set; zero is a three-sum exactly when \(\chi(-3)
e1\). The inspected verifier exhaustively checks the displayed formulas on many prime fields and on \(q=9,25,49\); these finite checks corroborate but do not replace the proof.

**Checked sources.** assigned RESULT.md at the frozen tree; artifacts/verify_torus_sums.py and verification.txt; Shi--Li--Xia--Helleseth--Ozbudak, arXiv:2609.20402

**Residual risks.** The final congruence reformulation uses the standard quadratic-character identity for \(-3\), including characteristic three; no gap was found.

## Originality — PASS

The 2026 primary source explicitly treats \(q=3^m\). Searches covering norm-one torus sums, generalized Zetterberg covering radii, and equivalent additive-length language found no earlier all-odd-\(q\) unweighted classification with the discriminant \(1-4/N(S)\), the exact two-sum size, and the \(q\bmod3\) three-sum endpoint.

### Equivalent formulations

Aliases through quadratic finite-field norm-one subgroups and Zetterberg-code covering radius were included; no statement-level equivalent all-odd-characteristic theorem was located.

### Broader coverage

Those results do not mechanically imply the claimed norm-only classification because their allowed coefficients and syndrome model differ.

### Exact database or table

This is an infinite symbolic theorem; a finite table is not decisive beyond sanity checking.

### Claim versus prior implication

The checked prior theorems do not imply the final all-odd-\(q\) formula without new algebraic analysis.

**Source inspections.**
- Norm-One Torus Decompositions and Decoding of Gashkov-Sidel'nikov Codes: Primary abstract and theorem summary; complete article text was not available through the accessible route. Assessment: Covers \(q=3^m\), not the all-odd-characteristic theorem.
- Determining the Covering Radius of All Generalized Zetterberg Codes in Odd Characteristic: Abstract and indexed theorem description. Assessment: Related covering-radius theorem, but no exact unweighted norm-one-torus length distribution located.

**Checked sources.** https://arxiv.org/abs/2609.20402; https://doi.org/10.1109/TIT.2023.3296754; https://doi.org/10.1109/TIT.2025.3544025; published-results semantic search

**Residual risks.** The full 2026 motivating preprint was not available for complete-text inspection. A short finite-field argument of this kind may exist under older additive-combinatorics terminology that was not indexed by the searches.

## Value — PASS

The theorem gives a complete exact additive invariant of a natural algebraic subgroup, resolves the explicitly motivated odd-characteristic extension, and exposes a genuine \(q\bmod3\) boundary absent in characteristic three. Exact length distributions and sumset sizes are reusable in both finite-field additive geometry and coding interpretations.

**Checked sources.** Shi et al. 2026 characteristic-three problem; generalized Zetterberg covering-radius literature

**Residual risks.** The result is structural and exact but does not by itself supply efficient decoding for every related code family.

## Limitations

- The theorem concerns the full unweighted norm-one torus in a quadratic extension and does not by itself produce a decoder for arbitrary odd-characteristic code families.
- The motivating characteristic-three preprint is very recent, and the extension has a short elementary proof, so near-simultaneous or folklore priority remains a residual risk.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
