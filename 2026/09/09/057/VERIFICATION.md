---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-09-30.md",
      "INDEPENDENT_AUDIT_2026-09-30.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

A fresh exact Murnaghan–Nakayama/class-algebra computation over all 3718 conjugacy classes at n=28 reproduced zero for all 80 partitions with at most three rows, including (16,8,4) and (17,8,3). The full row had 2557 positive and 1161 zero entries; all 43 partitions within box distance at most two of (16,8,4) were zero and exactly nine positives occurred at distance three, including the stated examples. Fresh n=29 and n=30 class sums also gave zero on the padded ray. These are finite exact certificates, not extrapolated infinite claims.

## originality

PASS

The exact mixed staircase-by-balanced-two-row vanishing row at n=28 was not found in the searched literature or other published SCOPE records. The closest closed-form Kronecker papers require two two-row/hook inputs, which does not include the staircase factor rho_7.

## value

PASS

The 80-member complete low-row vanishing family and its local zero neighborhood form a natural boundary statement for a Saxl-adjacent mixed staircase product, not a single arbitrary coefficient. It supplies a motivated obstruction and exact finite classification that could guide structural Kronecker positivity questions even without a general theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
