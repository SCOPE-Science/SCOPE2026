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

# Verification record

Reproduce with `python3 verify.py` (Python 3 standard library only); a successful run prints `VERIFY_OK_TRACEZERO_SQUAREZERO_ZETA_BRIDGE`. The program builds genuine finite rings, directly computes multiplication and every image pair for traceless matrices satisfying \(X^2=0\), and matches image cardinalities against exact coefficient formulas. Cases include \(\mathbb Z/2^j\mathbb Z\) for \(1\le j\le4\), \(\mathbb Z/3^j\mathbb Z\) for \(1\le j\le3\), truncated \(\mathbb F_2[t]\), \(\mathbb F_3[t]\), and \(\mathbb F_4[t]/(t^2)\). This checks different ring characteristics and a non-prime residue field. It also checks the rational-series algebra for \(q=2,3,4,5,7\) through exponent nine. These are finite experiments, not an exhaustive check of all chain rings. The general correspondence and its rank preservation are established by the valuation, Smith-normal-form, and Cayley--Hamilton argument in `RESULT.md`; no independent mathematical audit was performed.
