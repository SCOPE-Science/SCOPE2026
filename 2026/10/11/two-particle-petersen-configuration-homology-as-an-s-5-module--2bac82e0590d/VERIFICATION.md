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
# Verification

Run `python3 verification.py` in the directory containing `verification_certificate.json`.

The verifier reconstructs the Petersen graph as \(KG(5,2)\), verifies its girth and the five maximal four-cliques in the complement used to identify the automorphism group, constructs the unordered two-particle discrete configuration complex, and checks all cellular boundaries. It then rebuilds the spanning-tree presentation of first homology, verifies the certified \(70\times70\) determinant and modular ranks, and checks the five explicit integral generators of second homology.

For equivariance, the verifier enumerates all \(120\) permutations of the underlying five-element set, computes their signed actions on cells and on the explicit \(H_2\) basis, derives the \(H_1\) traces from the Hopf trace identity, and checks constancy and the expected values on all seven conjugacy classes. It also verifies character orthogonality.

All arithmetic used for the accepted claim is integral or exact rational arithmetic. The finite model proves the two-particle statement only; no higher-particle extrapolation is performed.
