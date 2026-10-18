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

# Verification of the polygon corner-law calculation

The proof is given in `RESULT.md`: exact radial integration, within-edge Taylor expansion, vertex switching-strip rescaling, divergence identity and positivity. The angular switching-rate identity was evaluated from two consecutive supporting-line equations. The coefficient of the order-\(p^{-1}\) term is a finite sum over actual edges and vertices; no discretization is used in its derivation.

Execute `python CHECKER.py` in a Python 3 environment. The checker requires only the Python standard library and implements independent adaptive angular integration of the original radial definition with breaks at all old and translated vertex rays. It evaluates the proposed analytic coefficient on a triangle, a nonsymmetric pentagon and a square at smoothing parameters \(p=64,256,1024\), and checks the non-even cubic term of an explicit triangle at two small scales.

The checker was executed successfully. Exact standard output:

`VERIFY_OK polygons=3 angular_integrals=9 cubic_asymmetry=2`

The coefficient formula is an analytical result with a local-uniform remainder; passing numerical tests provides evidence about implementation and normalization only, not a proof of uniformity or originality. No independent scientific audit has been performed.
