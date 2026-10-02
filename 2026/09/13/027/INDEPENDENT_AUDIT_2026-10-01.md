# Scientific audit — SCOPE-20260913-027

Date: 2026-10-01 UTC

## Final claim

Among cyclic Steiner triple systems of order 21, the maximum Pasch count is 63; the seven cyclic isomorphism types have Pasch counts 63,63,63,42,42,21,0.

## Correctness

**PASS** — A fresh exact-cover reconstruction of cyclic difference families on Z_21 reproduced 108 candidate full-orbit base triples, 224 raw three-block families, and seven multiplier classes. Expanding the seven representatives gives valid 70-block Steiner systems, and an independent six-subset recount reproduces Pasch counts 63,63,63,42,42,21,0. The source verifier’s all-point isomorphism search was inspected and the classical literature independently confirms that there are exactly seven cyclic STS(21) types.

Residual risk: The exhaustive classification is computational; the audit independently rebuilt the finite difference-family enumeration but did not replace the package’s general 21-point isomorphism routine with a second full implementation.

## Originality

**PASS** — Classical sources classify the seven cyclic STS(21) types and modern work records several Pasch-related properties, including the unique cyclic anti-Pasch type. The exact full Pasch-count vector and maximum 63 were not located in the accessible material or published-results corpus. A highly plausible 1981 classification paper was not available as verified full text; that source remains an explicit residual risk rather than being treated as novelty proof.

Residual risk: The inaccessible classical classification may contain a table whose invariant notation encodes some or all of these Pasch counts; this is the main originality risk.

### Equivalent formulations

Modern STS(21) property surveys were compared for Pasch/maxi-Pasch formulations; they do not state the complete seven-value cyclic vector in the material inspected.

### Broader coverage

Anti-Pasch census work and broader STS(21) classifications cover related configuration questions but do not imply the exact maximum over the seven cyclic types.

### Exact database or table

The classical Mathon–Phelps–Rosa classification is the key plausible table source. Open-access retrieval failed and authorized retrieval found no verified PDF, so full-table comparison could not be completed.

### Claim versus prior implication

Knowing there are seven cyclic types and that one is anti-Pasch does not imply the remaining six Pasch counts or the maximum 63.

## Value

**PASS** — Pasch configurations are a standard structural invariant in Steiner triple systems, and the seven cyclic STS(21) form a classical finite subclass. Determining the complete Pasch-count spectrum and exact maximum over that natural catalogued class is a motivated finite classification, with both maxi-Pasch and anti-Pasch boundary data.

Residual risk: The result concerns only cyclic systems and does not control the much larger non-cyclic STS(21) universe.

## Sources inspected

- Properties of Steiner triple systems of order 21 — https://arxiv.org/abs/2401.13356 — PARTIAL_COVERAGE: Confirms relevant classical context and a unique cyclic anti-Pasch type; does not state the complete vector in inspected material.
- Small Steiner triple systems and their properties — https://doi.org/10.1090/S0025-5718-1981-0616374-9 — UNRESOLVED_SOURCE_RISK: This is the main residual originality risk; no claim of exhaustive literature absence is made.
- Published finding SCOPE027 — https://github.com/Resultary/2026/tree/main/2026/9/13/SCOPE027 — SELF_MATCH_ONLY: The exact indexed match was the record itself; no stronger indexed table was found.

## Disposition

PASSED
