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

# Verification record

A direct proof is presented in `RESULT.md`. It uses no heuristic estimates, enumeration-to-infinity argument, or external mathematical verification service. Required nonstandard steps are: invertibility of the base adjacency makes neighborhood vectors independent; multiplication-operator rank counts nonzero twin blocks; an isomorphism must permute these rank-one blocks; the norm identity and connectedness force degree regularity along even walks.

The checked standalone script `verify.py` uses exact rational row reduction to test the neighborhood-vector independence and multiplication rank invariant. It enumerates 117 blow-ups with sizes from one to three of base graphs \(K_2\), \(K_3\), and \(P_4\), and performs 3480 finite rank checks. It also checks the normalization of explicit diagonal isomorphisms when degrees are regular or bipartite biregular. Replay command: `python3 verify.py`. Expected last line: `VERIFY_OK cases= 117 rank_tests= 3480`.

Scope limits: enumeration covers only those finite samples; nonisomorphism across all sizes follows from the proof and not from exhaustive matrix search. In particular, the script does not enumerate all real linear maps. An independent mathematical audit has not been performed.
