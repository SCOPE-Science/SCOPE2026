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

# Verification of the Desargues metric-basis classification

The executable `verify_kneser_lift.py` independently constructs the twenty-vertex signed Kneser graph, checks \(400\) ordered distances against the claimed parity-transfer formula, enumerates all \(1140\) triple landmark sets, and reconstructs the exchange graph and exact distance profile \((1,9,15,7)\) for every basis. Its exact output is in `verify_kneser_lift.out`.

The executable `verify_gp103.py` uses the generalized Petersen \(GP(10,3)\) presentation, rather than the signed Kneser construction or its distance formula. It excludes every two-landmark set, enumerates all triples, computes components and all within-component distances, and checks a displayed twenty-vertex isomorphism to the signed-pair representation. Its exact output is in `verify_gp103.out`.

Run each file with Python 3 and compare output byte-for-byte with the corresponding `.out` file. Only the Python standard library is needed; no downloaded datasets or supplementary packages are necessary. Both checks were executed successfully. The proof in `RESULT.md` supplies the infinite-quantifier-free structural completeness argument; the enumerations additionally verify the finite graphs and the full list of configurations.

The verification programs are exhaustive for the specified twenty-vertex graph, but they do not audit all published mathematical literature, establish results for other graph families, or provide independent external validation.
