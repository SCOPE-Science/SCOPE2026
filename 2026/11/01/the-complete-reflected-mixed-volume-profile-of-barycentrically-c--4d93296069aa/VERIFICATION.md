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

The analytic proof is in `RESULT.md`. Run `python3 check_tetra.py` in a directory containing the checker (Python 3 standard library only). The checker independently enumerates rational vertices from bounding-plane triples, forms exact rational facet cycles, and computes both ordinary volume and mixed volume by oriented facet-area vectors. It reports twelve successful exact-rational vertex/facet reconstructions and twenty-four successful volume/mixed-volume identities at cap parameters \(13/50,3/10,1/3,7/20,2/5,9/20,1/2,11/20,3/5,3/4,9/10,1\).

The proof covers **every real** \(t>1/4\) and every full-dimensional tetrahedron; the finite checks do not constitute independent certification of that universal claim. The differentiability and monotonicity assertions are shown by exact polynomial identities and sign arguments in `RESULT.md`. The displayed ratios are undefined at the single-point degeneration \(t=1/4\).
