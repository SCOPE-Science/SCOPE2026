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

The standalone `verify.py` is executable with the Python standard library. It enumerates all \(6211\) independent faces from the twenty-vertex graph and computes the full augmented \(\mathbb F_2\) boundary ranks by exact bit elimination; this is an exhaustive finite check, not a sample. It constructs all \(240\) graph automorphisms and computes their signed fixed-simplex Lefschetz numbers from the actual chain action, checking the full character formula. Run `python3 verify.py` in the directory containing the file, compare to `verify_output.txt`, and require the terminal marker `VERIFY_OK`.

The rational homology representation is then proved by the universal coefficient bound, the Hopf trace formula, finite-group character semisimplicity, and the coefficient-one argument for the sign-on-both-factors irreducible. The verifier does not calculate integral torsion or independently validate publication priority; neither is asserted. Independent audit has not been performed.
