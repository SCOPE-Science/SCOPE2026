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

# Reproducibility and verification

Run `python3 VERIFY.py .` (Python 3.10 or later; standard library only) beside `CHARACTER.csv` and the other included files.

The program constructs the 16-vertex Cayley graph and verifies each of the 192 affine permutations preserves all distances, then proves no more automorphisms exist using the hexagonal vertex neighborhood. It enumerates all ordered endpoint-pair orbits (16+96+48+96 = 256), all length-four magnitude chains in one representative fiber of each orbit, the exact signed boundaries in degrees 3 and 4, and checks the chain identity. It independently builds exact rational pivot bases for those boundary matrices and checks the following representative dimension/rank data, in order of terminal vertex indices 0, 1, 2, 6:

- `(9,54,96;9,45;0)`
- `(6,54,80;6,48;0)`
- `(4,66,80;4,61;1)`
- `(4,66,80;4,61;1)`.

It checks explicit nonboundary closed chains `(0,4,13,2)` and `(0,3,10,6)`, then every element of both ordered-pair stabilizers, and finally every one of the 192 full-group traces against the embedded CSV. All rational computations use exact `fractions.Fraction`; no floating-point rank test occurs. The actual final run's output is recorded in `verification_output.txt` and concludes `VERIFY_OK`.

The proof does not use finite experiments to infer an infinite theorem; the claim concerns exactly this 16-vertex graph and this bidegree. The verifier does not establish any integral torsion, other bidegrees, or publication priority. Independent mathematical validation has not been performed.
