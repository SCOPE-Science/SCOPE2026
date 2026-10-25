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

Run `python3 verify_johnson_rep.py` and `python3 decompose.py` in the same directory. Only Python 3 standard-library modules are required.

The signed simplicial-trace script enumerates every clique-complex simplex for \((6,3)\), \((7,3)\), and \((8,4)\), and checks the predicted Euler character against direct oriented fixed-face traces. It checks all 720 and 5,040 permutations in the first two cases, and all 22 conjugacy-class representatives for the third, totaling 5,782 comparisons. The exact finite GF(2) boundary ranks for the first two cases confirm a unique positive homology degree (degree two) of ranks 19 and 55. All three cases have zero group-averaged trace. Successful output ends in `JOHNSON_EQUIVARIANT_CHECKS_OK 5782`.

The second checker implements symmetric-group irreducible characters by explicit rim-hook recurrence and computes all character inner products. It obtains multiplicity one precisely for the partitions \((n-j-2,j,1,1)\), for all valid \(j\), in the six test cases \((6,3),(7,3),(8,3),(8,4),(9,4),(10,5)\); every other irreducible has multiplicity zero. Calculations test finite examples only, and no finite test establishes the all-parameter theorem. The uniform conclusion instead uses the proof from star/top equivariant Euler classes and Pieri decomposition. No independent mathematical audit has been performed.
