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

The exact claim is the global \(\ell_\infty\)-Lipschitz modulus of **Euclidean** nearest-point projection onto \(\{(s,x):s\ge\|x\|_2\}\) for each integer \(d\ge1\). It is not the Lipschitz norm of an \(\ell_\infty\)-nearest-point map.

The proof verifies the three projection regions, the full middle Jacobian, the induced maximum row sums, the reduction to a unique one-variable maximizer, the dimension-five strict transition, and the segmentwise global bound and limiting sharpness. The inequality at dimension five is exact: \(g_5(a)\le(9+4\sqrt2)/12<11/9<\sqrt5-1\). For greater dimensions, the differential comparison remains strict for all \(a\in[0,1]\).

Run `python3 verify_lorentz.py` from the extracted file directory using the Python standard library. An execution from the self-contained package returned `VERIFIED 5461 finite assertions; max-dimensional test d=32`; it checked Jacobian first differences, the exact formula branches and random spatial-row constraints. These checks do **not** establish all-dimension inequalities: that is the purpose of the written proof. No independent mathematical or bibliographic verification was performed. Priority remains provisional and the result does not cover weighted norms or other cones.
