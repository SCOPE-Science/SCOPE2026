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

The unrestricted proof uses basis extension, dual-rank identity, Edmonds' matroid-intersection min-max theorem, and a deletion-contraction identity that agrees with the standard recursive definition of Littlestone dimension.

Run `python3 verify.py` with Python 3.9+ and no third-party dependencies. The program checks 1,347 distinct binary represented matroids across small ground-set sizes, including loops and coloops, and a rank-five direct sum on ten elements. It calculates each dimension by a different finite definition and also tests optimality of every nonconstant first query. The observed output is embedded as `check_output.txt`; test observations were generated from the exact embedded source before acceptance.

The program does not prove the theorem beyond its finite test domain. Generality is supplied by the written argument, especially the matroid-intersection identity. The uniqueness or publication priority of the theorem was not independently certified.
