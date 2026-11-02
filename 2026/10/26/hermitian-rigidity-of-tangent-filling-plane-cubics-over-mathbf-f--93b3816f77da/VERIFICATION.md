---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Independently rebuilt F4=F2[a]/(a^2+a+1), all 21 rational projective points/lines, ten cubic monomials and their characteristic-two gradients. Wrote and executed an independently coded exhaustive C++17 finite-field incidence scan through every one of (4^10-1)/3=349525 last-nonzero-coefficient normalized cubics, checking all smooth rational tangent lines and coverage. Exact outputs: 11368 tangent filling, with 5320 nine-point and 6048 ten-point cubics; 280 without a rational line and 11088 with one. A second independent GL3(F4) enumerator scanned all 4^9 matrices, identified 181440 invertible, and computed the cubic (row_1)^3+(row_2)^3+(row_3)^3, yielding exactly 280 normalized Hermitian-orbit equations, stabilizer 648 in GL3 and 216 in PGL3; these 280 codes matched the independent incidence scan exactly, coefficient-for-coefficient. Restriction of degree-3 cubic to a rational line has 5 rational projective points, so vanishing at all 5 proves a rational factor. The original Jacobian rank-15 criterion for geometric smoothness also follows from regular-sequence/Hilbert-series reasoning, but we did not independently reproduce all 11368 rank calculations. Main no-line classification is independently exhausted, not extrapolated.

## originality

PASS

The Hermitian cubic and its tangent-filling property are already given by Asgarli–Ghioca, and its unitary stabilizer is classical. The new comparison is the converse for every F4 cubic without a rational line factor and all 11368/11088/280 counts. The primary 2023 paper discusses examples and large-field degree bounds, not this F4 exhaustive classification. Unindexed older small-field catalogues and full geometric references remain risks.

## value

PASS

F4 is the first square field where the smooth Hermitian unital is a cubic. An incidence-covering condition might permit many singular or non-Hermitian irreducible cubics; the exact complete classification of all line-free cases and decomposition of line-factor exceptions is a natural finite-geometry rigidity statement, not arbitrary data mining. An exact finite invariant with full orbit certificate is independently useful without higher-field generalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
