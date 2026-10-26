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

# Finite exhaustive verification

The self-contained `verify_latin5.py` uses Python standard-library backtracking, permutations, and breadth-first search. Execute `python3 verify_latin5.py` from the directory containing the verifier. It prints `VERIFY_OK` only after all the stated assertions succeed.

The verifier generates all Latin squares with first row fixed, then applies every symbol permutation, checking it obtains exactly \(1344\cdot120=161280\) fully labeled squares. It enumerates all row/column permutation pairs to derive the symbol map of every possible autotopism and asserts stabilizer sizes \(100\) and \(12\). It checks the four explicit even-isotopy witnesses, one breadth-first component of size \(18000\) and maximum distance \(13\), and performs a separate complete traversal of the full switching graph to check all degrees, all connected-component sizes, and all four parity sectors. Distance-shell counts from the base square are \((1,4,12,36,108,252,612,1284,2256,3624,4812,3828,1112,59)\).

The group-theoretic argument makes a single-root distance computation sufficient for the diameter: the component is precisely an orbit of \(A_5^3\) acting by graph automorphisms. The exhaustive census is finite and does not assert anything about larger orders or mixing rates. No separate implementation by an independent party, external formal proof assistant, or independent audit has been performed.
