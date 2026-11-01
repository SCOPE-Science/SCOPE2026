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
# Verification instructions and limits

Execute `python3 verify.py` with a standard Python 3.9+ interpreter. It should print `FACES_OK`, `MATCHING_OK`, `ACYCLIC_OK`, `CHARACTER_OK`, `SPECHT_OK`, and finally `ALL_VERIFY_OK`. No external dataset or Python dependency is required. The file enumerates all 2,097,151 nonempty vertex subsets, reconstructs all 37,527 simplices, and checks all 218,673 Hasse incidences, rather than sampling. It also calculates original mod-two boundary ranks \((0,20,190,1140,3955,5222,4410,2520,945,210,21)\) by bitset Gaussian elimination. It separately computes the full \(S_7\) character by oriented fixed-face traces and orbit-union sums. All integer/rational multiplicity checks use exact arithmetic.

The actual finite computation was executed successfully on the provided standalone source. Its success establishes an exhaustively verifiable finite certificate conditional on the stated definitions and the standard discrete-Morse and Hopf trace theorems; it does not extend the conclusion to larger Kneser graphs. This is a self-review only. Independent audit was not performed.
