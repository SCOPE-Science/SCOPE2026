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
# Verification of the finite incidence and arithmetic counts

Run `python verify.py` using Python 3 standard library. The saved program output in `verification_output.txt` ends with `VERIFY_OK`.

The verifier builds 48 explicitly parameterized lines over the prime field of order 17, where the element two has multiplicative order eight. It computes 1,128 unordered pairs and groups their intersection points, verifies 192 double points, 24 fourfold points, 216 singular supports and the connected bipartite graph with 264 vertices and 480 branches. It computes all four residue-class Frobenius actions on lines and singularities, verifying no fixed vertices in nonsplit cases. It also exhaustively enumerates projective rational points in eight small prime fields through the three complete-intersection equations.

These checks corroborate the exact symbolic incidence argument, which is the proof in every characteristic at least five. The graph-cover integral module lemma and Picard unit-sheaf computations are written mathematical proofs and are not mechanically certified by the finite test. The material does not include a human or independent external audit.

A separate `python verify_characteristic_five.py` check uses explicit arithmetic in \(\mathbb F_{25}=\mathbb F_5[t]/(t^2-3)\) and confirms all \(216\) singular points with multiplicities \(192\) twofold and \(24\) fourfold, as reported in `verification_characteristic_five_output.txt`. This second calculation corroborates the lowest permitted characteristic, while the characteristic-uniform proof is symbolic.
