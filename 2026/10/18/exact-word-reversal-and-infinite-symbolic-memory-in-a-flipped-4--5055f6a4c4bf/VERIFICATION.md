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

# Reproducible mathematical verification

Run the included Python 3 program `verify.py` with no third-party dependencies. The observed output for the packaged script is `VERIFY_OK 4094`.

The exact-integer identities checked are the transpose symmetry \(M_{w^{\mathrm{rev}}}Q=(M_wQ)^{\mathsf T}\) for every one of the 4,094 nonempty binary words through length eleven; the exact rational interval endpoints for their cylinders; an ordered tiling of \([1/3,1]\) at each depth; the one-symbol and all-zero cross-ratio identities through length 59; and the transfer-operator identity for five rational points. Numerical logarithms are used only to corroborate that finite-cylinder probabilities sum to one and to distinguish the two-letter mass from an independent Bernoulli model.

The proof of arbitrary-length symmetry is the matrix identity \(M_jQ=QM_j^{\mathsf T}\) and multiplicative transposition. The proof of infinite memory uses a strict derivative argument rather than numerics. The finite test does **not** independently certify every word or every history length, and it is not an independent audit. Boundary itineraries occur on a null set and are immaterial to the probabilistic statement.
