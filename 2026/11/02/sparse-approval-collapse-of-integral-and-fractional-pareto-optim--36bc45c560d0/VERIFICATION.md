---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible checks

Execute `python3 verify.py` with a standard Python 3 interpreter. The verifier uses exact `fractions.Fraction` arithmetic and only Python standard-library modules. It checks all 10 two-seat committees for the three-approval witness and 1024 supports of distinct singleton/doubleton approval ballots on 4 candidates across all committee sizes with denominator-2 or denominator-3 fractional vectors. Expected counts: 10,544 integral PO committees and 460,068 tested fractional alternatives. An independently checked four-candidate two-approval example defeats single-swap-only Pareto improvement.

These are finite tests, not an infinite proof. The exact all-size argument is the exchange lemma and layer-cake proof in `RESULT.md`. Independent scientific audit has not been performed.
