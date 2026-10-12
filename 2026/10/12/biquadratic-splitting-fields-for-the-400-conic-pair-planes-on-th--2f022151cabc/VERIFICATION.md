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

# Exact reproducibility

Run the accompanying `verify_planes.py` with Python 3; it has no nonstandard dependencies. It builds the exact number field \(\mathbb Q(i,\sqrt5)\) in the rational basis \((1,i,\sqrt5,i\sqrt5)\), with defining relations \(i^2=-1\) and \((\sqrt5)^2=5\). The source input consists of Naskręcki's four projective matrices and the two conic-cutting plane seeds, cited in `RESULT.md`.

The script performs complete breadth-first orbit enumeration, rational normalization of each row, disjointness tests, closure under four Galois automorphisms, subgroup-stabilizer classification for every plane, and independent checks of the three nontrivial involutions' fixed counts. All assertions must pass, including exact total \(400\) and field distribution \(16,144,48,192\).

Expected terminal output:

`VERIFY_OK planes=400 first_orbit=160 third_orbit=240 Q=16 Qi=144 Qsqrt5=48 K=192 Galois_orbits=16+96+48 fixed_i=64 fixed_sqrt5=160 fixed_both=16`

The program rigorously certifies consequences within the finite group orbits. The premise that these orbits exhaust all conic-pair planes is supplied by Naskręcki, Theorem 1.1 and Corollary 3.1, not independently derived by the script. Numerical experiments, heuristic extrapolation, and external independent certification are not asserted.
