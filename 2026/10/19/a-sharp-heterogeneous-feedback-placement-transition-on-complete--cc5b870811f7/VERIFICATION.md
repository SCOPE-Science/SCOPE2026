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
# Exact verification and scope

Run `python verify_bipartite.py` with Python 3 and the dependency in `requirements.txt`.

The script constructs the Laplacian pseudoinverse and squared pseudoinverse using its spectral projectors; it computes four closed-form trace expressions for possible placements; and it verifies three exact rational difference identities. It checks the strict lower-bound calculation for the on-diagonal threshold and independently evaluates inverse traces of complete rational Laplacian matrices for \(2\le p\le6\) and \(p<q\le9\), several unequal and equal gain pairs, all four leader orbits, and the exact seven-vertex instance. Its latest reviewed output was:

`VERIFY_OK 880 exact symbolic identities, rational matrix traces and location inequalities`

The symbolic difference identities hold with indeterminates for the part sizes and gains. The global location classification follows analytically from the signs of their factors and the quadratic root argument given in RESULT.md. Finite direct-matrix tests are auxiliary and are not substitutes for arbitrary-dimensional proof. No independent audit or external certification has been performed.
