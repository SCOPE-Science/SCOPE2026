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
# Exact verification scope

Execute `python verify.py` with Python 3 standard library. It constructs the fields of \(4\), \(16\), \(64\), and \(256\) elements, verifies the representatives and genera of all \(13\) cyclic quotient pairs, enumerates the seven positive-genus quotient point counts over the first two fields, reconstructs the zeta factors from the Weil functional equation, and compares direct covering counts for four extensions with Newton identities. It also exhaustively checks all \(85\) projective points of \(\mathbb P^3(\mathbb F_4)\). The expected terminal marker is `VERIFY_OK`.

The complete proof additionally requires the stated smoothness/connectedness argument, Kummer character decomposition, and irreducibility proof; program output alone does not certify these abstract steps or a literature novelty assertion. Independent audit and validation have not been performed.
