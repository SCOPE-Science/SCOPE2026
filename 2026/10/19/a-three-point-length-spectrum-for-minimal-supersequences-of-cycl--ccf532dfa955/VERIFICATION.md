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

# Reproduction and scope

Run `python3 verify.py` in the directory containing the files to reproduce the exact finite computations, which require only the Python standard library. `verification_output.txt` records the tested outputs. The program's first enumeration uses all distinct order-preserving merges of the two input words; this covers every minimal supersequence because every position must belong to at least one of two selected source embeddings. Minimality is checked independently by deleting every individual position and testing both subsequence predicates. A second direct alphabet-product enumeration checks the complete small cases \(n=2,3,4\) without using the merge-generation procedure.

The tested length profiles are: \(n=2:\{3:2\}\); \(n=3:\{4:1,5:1,6:1\}\); \(n=4:\{5:1,7:1,8:8\}\); \(n=5:\{6:1,9:1,10:34\}\); \(n=6:\{7:1,11:1,12:122\}\); \(n=7:\{8:1,13:1,14:417\}\); \(n=8:\{9:1,15:1,16:1416\}\). The pair notation records length and number of minimal words at that length.

The infinite theorem depends on the combinatorial proof in `RESULT.md`, not on extrapolation from these counts. There is no externally performed independent audit or formal theorem prover claim.
