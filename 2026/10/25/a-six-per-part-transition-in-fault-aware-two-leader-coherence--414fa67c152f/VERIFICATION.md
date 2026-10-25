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

# Verification of the defective-biclique leader theorem

Execute `python verify.py` using Python 3 and a compatible SymPy installation (`requirements.txt`). The program recomputes all eight formal symmetry-orbit costs by invariant-subspace decomposition, reduces them to the five quoted rational values, checks the rational difference factors and their sign certificates, and independently forms and inverts the grounded Laplacian for every one of the 245 unordered leader pairs on sizes \(3\le n\le7\). It also checks the integer sign transition from five to six. A successful replay prints:

`VERIFY_OK 8 symbolic orbit identities, 4 exact comparison identities, 245 direct rational grounded inverses, all minimum classes n=3..7`

The claim for **every** integer \(n\ge3\) relies on the quotient-decomposition identity and the exact polynomial signs proved in `RESULT.md`. The finite checks are corroborative only; they are not an infinite proof. The analytical argument does not address arbitrary weights, other deleted-edge patterns, or noise-corrupted leaders. The public evidence here has undergone self-review only; no independent audit is claimed.
