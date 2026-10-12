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

# Verification of mathematical construction

The theorem is proved analytically in `RESULT.md`. Its critical identities are the dual-gradient equality \(2^{1/q}/(2-c)=1\), the strict gradient obstruction for every \(q'<q\), the strict interpolation difference \(M(3/4,3/4)-B_c(3/4,3/4)=c/[4(2-c)]\), compactness of the product cube, and nonvanishing power-Vandermonde determinants.

`check.py` is standalone and needs no third-party packages. Run `python3 check.py` in the extracted directory. It evaluates 12,706 finite identities or representative inequalities and gives `PASS 12706 finite identities and representative inequalities`, followed by `exact Vandermonde determinant: 3/1024`. The test uses deterministic pseudorandom values and representative finite exponents; it does not enumerate all copulas, certify all real exponents numerically, or replace the analytic proof. No independent scientific audit has been performed.
