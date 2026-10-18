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

The standalone `verify.py` constructs the degree-two boundary directly from half-edge differences and exactly enumerated symmetric-power monomials. It checks the four-particle boundary ranks and the pole-swap involution eigenspaces for three through six edges; it also checks the three-particle precursor ranks. The expected terminal message is `VERIFY_OK`. The companion `verify_stabilization.py` imports the adjacent `verify.py`, constructs weight-three alternating cycles directly, checks zero boundary, applies every edge-stabilization variable, and compares their span against the predicted pole-even rank; the expected terminal message is `STABILIZATION_VERIFY_OK`.

The general proof uses the reduced Świątkowski quasi-isomorphism over the rationals, an exact joint polynomial-kernel computation, and rational Schur-functor decompositions. Finite-field eliminations alone do not prove characteristic-zero ranks or the unbounded family. No independent scientific audit has been performed.
