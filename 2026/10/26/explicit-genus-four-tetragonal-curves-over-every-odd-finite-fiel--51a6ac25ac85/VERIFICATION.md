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

# Verification and limits

The complete argument for all odd finite fields is in `RESULT.md`, Steps 1–5. The proof identifies an exact fiber-product equation on the geometric splitting of the quadric and uses the absence of common branch values, including the wild characteristic-three case. The explicit rational point and Riemann–Roch produce the degree-four pencil. The nonsplit canonical quadric excludes rational trigonal pencils.

`verify.py` is self-contained except for Python 3 and SymPy. Execute it from the package directory with `python verify.py`. The replay returned `VERIFY_OK`, after checking the exact Segre identity, exceptional-characteristic arithmetic, and the Jacobian-minor ideals on all projective affine charts for \(p=3,5,7,13,17\), with nonsquares \(c=2,2,3,2,3\), respectively. Those five tested curves have \(6,10,16,14,30\) rational points over their prime fields. In particular, they contain the rational point certified symbolically for every odd field.

The finite Gröbner checks do not themselves establish universal geometric smoothness. No numerical point counts beyond the stated prime-field cross-checks, isomorphism classification, optimality of point counts, or characteristic-two existence statement is claimed. The originality assessment relies on accessible literature and may not capture unindexed later results. Independent audit has not been performed.
