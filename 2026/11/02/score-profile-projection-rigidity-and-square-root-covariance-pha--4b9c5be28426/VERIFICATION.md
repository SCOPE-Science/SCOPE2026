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

# Verification evidence and limits

Run `python verify.py` using Python 3 and only its standard library. It enumerates every labeled fair tournament for orders 3 through 6, computes all directed cycle lengths and every score class, checks the covariance and projection identities with exact fractions, and checks the integer-score sign/zero characterization through order 120.

The executed checker reported 41,341 exact assertions passed, including enumeration of all 32,768 tournaments on six vertices. This establishes only finite cases computationally. The proof in `RESULT.md` gives the arbitrary-size result by conditioning, elementary identities, and finite-dimensional orthogonal projection. No proof assistant, external certificate, or independent mathematical audit was used.

The selected source's earliest explicitly verified public date is 2000-01-03. Material inspected for historical comparison includes complete openly available papers on tournament score geometry and the 3-cycle/4-cycle tradeoff; older full texts on conditional score enumeration and Hamilton-cycle counts were not accessible, leaving residual priority risk.
