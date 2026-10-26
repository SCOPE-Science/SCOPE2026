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

# Finite arithmetic verification

Run `python3 verify_census.py` with a standard Python 3 interpreter. The script has no network or nonstandard dependency. It enumerates all rowwise candidates, enforces the exact coherence identities, constructs full binary operation tables, and tests P1--P5, conditional identity, semicomplementation and, separately, double-negation inflation on every table. It also computes the automorphism orbits of all directed loop-free three-vertex graphs from first principles and checks their weighted count.

Expected completion marker: `BOOLEAN_PRECONDITIONAL_BINARY_CENSUS_OK`.

Expected exact counts: \(1,4,7820\) for \(\mathsf T\) and \(1,2,1021\) for \(\mathsf F\) on Boolean algebras with respectively one, two and three atoms. Three-atom unary reduct counts are \(125\) and \(8\); the \(\mathsf F\)-fiber multiplicities are \(729\) once, \(81\) three times, \(16\) three times and \(1\) once.

The checker verifies an entirely finite combinatorial statement; it does not certify any historical priority claim or independently validate the proof. The finite normal-form equivalence and the logical interpretation of the enumeration are justified mathematically in RESULT.md. An external independent audit has not been performed.
