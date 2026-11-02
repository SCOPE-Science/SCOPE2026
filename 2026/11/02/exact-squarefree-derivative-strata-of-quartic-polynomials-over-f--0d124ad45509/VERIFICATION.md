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

# Verification instructions and limits

The proof is given in `RESULT.md`. To reproduce the independent finite checks, run `python3 verify.py` with Python 3 and no dependencies. The verifier enumerates every monic quartic over nine finite fields, computes its nonzero formal derivative and polynomial gcds, stratifies the squarefree-derivative subset by \(\deg\gcd(f,f')\), and compares against the three universal formulas. Expected final line: `VERIFY_OK fields=9 quartics=94213`. The field definitions use explicitly stated monic irreducible polynomials. The check is exhaustive *for those nine finite fields* only, not for all prime powers; the symbolic counting argument proves the general result. No independent mathematical audit is asserted.
