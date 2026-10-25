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

The standalone standard-library Python program `verify.py` enumerates every simplex and every orbit of the order-eleven multiplier, including signed orientations. It computes each of the eleven modular eigenspace ranks of the degree-one through degree-four boundary maps. In degree four, the rank drops by one exactly at eigenvalues \(1\) and \(12\), where the eigenspace homology dimension is five rather than four. The same program computes the fixed-chain homology in characteristic two, where the invariant degree-four homology dimension is five. It terminates with `VERIFY_OK` and `CHAR2_OK` if every expected count and rank is reproduced.

The independent mathematical premises are the standard equivariant universal coefficient exact sequence, the rational representation theory of \(C_{11}\), and Govc's published non-equivariant integral homology classification. The verifier checks finite matrix arithmetic but is not an independent audit, proof assistant, or external certification. No independent audit or independent validation has been performed.
