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

# Verification procedure and limits

Use `python check_erlang2.py` in a Python environment with SymPy, NumPy and SciPy. The program checks the exact four-state Feynman–Kac resolvent, spectral rational identity, derivative quintic, factorized discriminant, two explicitly positive global certificates, a unique critical positive root, and 150 independent random numerical evaluations of the four-by-four resolvent against the stated spectrum. It also checks the single positive quintic root at the reference parameter \(y=2\), where a monotonicity proof is supplied in RESULT.md.

The proof of universal peak count is analytical: a discriminant identity together with positivity of its remaining factor prevents any collision of finite roots for \(y>0\); the sole crossing of the nonnegative domain occurs at the unique positive zero of the constant coefficient. Finite numerical tests do not certify an infinite domain. Historical originality is provisional, and no independent scientific audit is asserted. All source details are in RESULT.md and REVIEW.md.
