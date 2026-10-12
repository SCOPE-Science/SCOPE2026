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

# Reproducibility and checks

The self-contained script `verify.py` uses Python 3 standard-library modules only (`fractions`, `math`). From the containing directory execute `python verify.py`. It reproduces 2,240 exact rational/integer comparisons of the factorial curvature identity, four exact boundary-equality patterns, four below-threshold examples, and seven numerical diagnostics of the inverse-hyperbolic threshold and adjacent endpoint ordering. A successful run prints `All standalone finite diagnostics passed; infinite statements rely on the proof.`

The theorem is an analytic statement for every finite \(0<a<b\), every \(0<w<1\), and all integer indices \(k\ge1\). Neither the 2,240 identities nor any finite grid certifies those quantifiers. The proof supplies the exact determinant factorization, a strict-concavity argument for the inverse-hyperbolic failure intervals and a strictly convex real-variable sign function. The first failure in the small-weight limit is proved to escape every fixed finite range.

Exact arithmetic examples include \((a,b)=(1,2)\), where \(w_*=e/(256+e)\) and the only equality indices at that weight are 8 and 9; and \((a,b)=(1,4)\), whose threshold odds are 1/8 with a single equality at index 2. The script is a diagnostic reproduction artifact rather than a separate general-purpose theorem prover.

Historical priority and external replication are not certified. The reference overview and scientific limitations appear in `RESULT.md`; C/O/V review and specific residual literature risks appear in `REVIEW.md` and `AUDIT.json`.
