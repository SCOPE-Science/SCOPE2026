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

# Reproducibility and limits

Run `python3 verify.py` with Python 3 and the standard library. The verifier implements an independent monotone bisection construction for \(\kappa\), checks the scalar identities, all \(2^d\) proposed corner contacts for 210 positive parameter selections with dimensions two through eight, the sum-of-squares polynomial identity, direct point containment, independent support-function comparisons, and the symmetric rounded-cube limiting formula. The completed run returned: `PASS: 29400 numeric support/containment/identity tests; all sign contacts verified for 210 independent parameters`.

The package includes the full source of `verify.py`. Its finite checks support implementation reproducibility, but do not establish a universal theorem or originality. The proof in `RESULT.md` is independent of numerical precision, optimization software and unrecorded computational data. Historical-priority inspection of all potentially relevant specialist texts remains incomplete; no independent audit is claimed.
