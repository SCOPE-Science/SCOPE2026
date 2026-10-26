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

# Verification

Run `python3 verify.py` in the directory containing the proof. The program needs no external dependencies. It directly constructs every element of \(Q_n\) for \(1\le n\le5\), checks both oriented fixing relations against the centralizer-stabilizer formulas, and compares the resulting polynomial with an independently generated integer-partition formula.

The observed end marker was `VERIFY_OK degrees=5 operation_comparisons=739114`, with exact ordered fixing-pair counts \(1,8,72,672,7200\) for degrees \(1,2,3,4,5\) respectively. All monomial coefficients agreed. The program additionally checks the conjugation-specialization counts for trivial group actions.

The mathematical proof is self-contained apart from the standard Burnside lemma, orbit-stabilizer theorem, elementary permutation centralizers, and the classical Hardy–Ramanujan partition asymptotic. The finite tests do not claim exhaustive checking beyond \(n=5\) and do not certify the arbitrary-degree statement independently.
