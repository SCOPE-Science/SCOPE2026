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
# Verification summary

The exhaustive scripts use only the Python 3 standard library. All expected outputs are embedded as corresponding `.out` files; the scripts are fully standalone and do not read external data. Run `python3 verify_fishburn.py`, `python3 verify_extensions.py`, and `python3 verify_witnesses.py` from the package directory.

`verify_fishburn.py` produced 5335 unique interval-order types and 5333 distinct round-two global fingerprints at order eight, with exactly two two-member collision classes; all smaller sizes had no round-two collisions; round three distinguished every eight-vertex type. `verify_extensions.py` independently rebuilt the same 5335 type counts and the two exceptional pairs using maximal-element extensions and a nested-downset criterion. `verify_witnesses.py` verified equality after two rounds, inequality after three, nonisomorphism, and the pairing under order duality. Exact output records are present in `verify_fishburn.out`, `verify_extensions.out`, and `verify_witnesses.out`.

The exhaustiveness rests on the classical Fishburn-matrix bijection and, independently, the fact that every finite poset has a maximal element removable to a smaller poset. Both were used explicitly; no heuristic isomorphism sampling was used. The code does not establish claims beyond eight elements. A separate independent scientific audit has not been performed.
