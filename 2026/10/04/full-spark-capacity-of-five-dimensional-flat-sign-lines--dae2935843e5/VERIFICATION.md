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

The finite domain consists of the sixteen projective representatives
\[
(1,\varepsilon_2,\varepsilon_3,\varepsilon_4,\varepsilon_5),\qquad \varepsilon_j\in\{-1,1\}.
\]
The bundled `verify.py` uses exact integer arithmetic throughout. It computes all \(\binom{16}{5}=4368\) five-line determinants by the Bareiss algorithm, tests all \(\binom{16}{7}=11440\) seven-line subsets and all \(\binom{16}{6}=8008\) six-line subsets for full spark, and constructs all \(2^4\cdot5!=1920\) projective signed-coordinate-permutation actions.

A successful replay prints:

`VERIFY_OK projective_lines=16 max_full_spark=6 full_spark_6sets=1088 symmetry_group=1920 orbits=5 orbit_sizes=16,160,192,240,480`

`WITNESS (0, 1, 2, 4, 8, 15) DETS 16,16,-16,16,-16,-48`

The exact finite verification establishes the capacity, count and orbit decomposition only for the flat sign-line configuration. The statement that eight flat vectors cannot perform weak phase retrieval additionally uses the published theorem that a real weak-phase-retrieval family of minimal size \(2n-2\) must be full spark. No finite experiment is used as a substitute for that analytic theorem.
