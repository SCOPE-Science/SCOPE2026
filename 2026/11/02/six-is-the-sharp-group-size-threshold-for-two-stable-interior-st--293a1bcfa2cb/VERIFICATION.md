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

Install the declared dependency in `verification/requirements.txt`, then run `python verification/verify.py` from the package root. The script passes 145 exact symbolic/rational assertions on SymPy 1.14.0. Its claims include independent Bernoulli-state enumeration for the gain function, exact formulas for the six-person reward polynomial, its stationary points and levels, the four strictly interior algebraic roots at \(c=b/3\), vector-field sign alternation, and a symbolic discriminant for the only potentially exceptional five-person coefficient pattern.

The proof covers arbitrary positive real rewards and costs using Descartes' rule, cubic root classification, and a direct critical-point analysis. Exact finite rational tests alone would not establish the universal result; they supplement the proof. No exhaustive classification of models outside the two-stage strictly interior assumptions is claimed. There has been no independent audit or independent numerical reproduction beyond the indicated checks.
