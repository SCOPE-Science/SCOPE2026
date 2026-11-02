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

# Mathematical verification

The theorem is proved in `RESULT.md` using two bijections with explicit inverses: a first-return decomposition and deletion of a distinguished hill. It requires no computer algebra or external lemma. Exact-arithmetic checks were run using `python verify_hills_area.py` from this package: `PASS: 23957 exact assertions`.

For \(1\le n\le10\) the verifier exhausts Dyck words, matches Catalan counts, computes the area and hills, checks the exact covariance, reconstructs the hill-size-biased area law by a second Catalan-pair enumeration, confirms every area-drop identity, and checks all attainable integer-threshold stochastic tails. These checks do **not** by themselves certify all sizes; the unrestricted proof rests on bijective invertibility and the deterministic area relation. The historical-priority determination is not independently validated and retains the explicit inaccessible-source risk stated in the review.
