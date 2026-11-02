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

# Verification and scope

The proof uses a local semi-free dg resolution of a hypersurface, the globally defined fiber Euler vector field, and the Cartan formula on the derived de Rham bicomplex. Explicit identities include \(\partial\eta=t^m\), \(E(\eta)=m\eta\), and \(d_1\iota_E+\iota_Ed_1=w\) on the weight-\(w\) part. Nonzero rational weights therefore give a contracting homotopy. The weight-zero subcomplex is ordinary de Rham on the smooth reduction, whose Hodge sequence degenerates at the first page. No numerical experiment is used as a substitute for this argument.

The standalone Python 3 artifact `artifacts/verify_local_e1.py` runs exact rational Gaussian elimination on the local derived-exterior presentations. Command: `python3 artifacts/verify_local_e1.py`. Observed output: `VERIFY_OK 224 exact local E1 blocks checked`. It checks \(2\le m\le17\) and \(0\le p\le13\), including upper and lower cohomology ranks, but cannot by itself certify global Hodge degeneration, arbitrary tensor twists, or all positive integers.

Only split thickenings over smooth projective complex reductions are asserted. Nonsplit ribbons, positive characteristic, and arbitrary nonreduced singularities remain unproved. No independent audit was performed.
