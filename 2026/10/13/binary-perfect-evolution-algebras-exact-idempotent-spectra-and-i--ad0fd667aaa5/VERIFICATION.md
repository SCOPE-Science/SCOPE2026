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
Run `python3 evol_verify.py` and `python3 evol_orbits.py` from the same directory; Python standard library suffices. The first enumerates 2^(n*n) binary matrices for n≤4, checks invertibility and the nullity of the idempotent fixed-space equation, tests the closed-form coefficients, and checks total group size for n≤8. It emits VERIFY_OK if all assertions pass. The second independently forms the simultaneous row-column permutation orbits of all invertible fixed-point-free matrices for n=2,3,4, prints their sizes and stabilizer-sensitive histograms. Expected exact values: n=2: 2 presentations, 1 orbit; n=3: 48 presentations, 8 orbits; n=4: 5824 presentations, 248 orbits, two size-8, eight size-12, 238 size-24. Finite enumeration corroborates but does not prove the all-n formula. The all-n symbolic proof uses subspace-lattice Möbius inversion and irreducible companion matrices.
