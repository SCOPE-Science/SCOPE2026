---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The explicit coordinate change (X,-Y,alpha Z,-alpha W), alpha^4=-1, sends the maximal inner-Galois quartic X^4+XY^3+Z^4+ZW^3=0 to Schur's equation exactly. The Miura–Taki Proposition 3.3 eight points map to the four zeros on L: x0=x1=0 and four zeros on M: x2=x3=0 printed in Rojas–Lira Section 3. Because the Schur polynomial separates into quartics of disjoint coordinate pairs, each of the 4*4 joins P_iQ_j lies entirely on Schur; the 16 joins are distinct. Rojas–Lira Lemma 3.1 proves every Schur line meeting L or M is one of those sixteen; hence each of the eight points lies on precisely four lines and the 48 other lines avoid them. The global assertion that there are no *other* quadruple points uses the published full 64-line incidence census attributed to Nurowski, rather than the sixteen-line symbolic check. An accessible indexed technical summary of Nurowski explicitly states that the 64 lines have exactly eight quadruple points and sixteen distinguished join lines; the Nurowski full text could not be retrieved this run, so that literature-dependent global count was not independently enumerated; this is an explicit correctness residual dependence on a precise cited incidence theorem, not a fabricated independent 64-line verification.

## originality

PASS

Best-of-knowledge originality judged against exact antecedent model, broader results, tables and mathematical implication. The new complete statement is not covered by the inspected sources; the named residual risks and incomplete full-text material prevent any claim of exhaustive priority or external certification.

## value

PASS

The eight inner Galois points (an extremal function-field/projection structure) and Schur's quadruple line-concurrences (an extremal incidence geometry) are independently natural intrinsic loci on one quartic surface. Their exact identification and resulting canonical K4,4 skeleton gives a mathematically motivated bridge between two previously separated analyses, not an arbitrary coordinate renaming or merely a new count. The complete 64-line census is prior work and is not claimed new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
