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

# Reproducing the exact finite classification

Python 3.9 or newer and the standard library suffice. Place `verify.py` beside `optimal_codebooks.json` and execute `python3 verify.py`. The script first constructs the finite GC-balanced candidate universe and all reverse-complement orbits from definitions, then builds all forbidden comma splices and forbidden Hamming pairs. Its exhaustive exact integer branch-and-bound verifies that no codebook has respectively more than 21, 17 and 7 words. The routine enumerates all equality cases and independently direct-tests their word-level properties. It recalculates self-reverse-complementary word counts and orbit counts under the eight complement-preserving alphabet permutations. The complete calculated inventory must equal the supplied JSON data.

A successful execution prints `distance=1: max=21, count=136, fixed=3, upper_nodes=381, census_nodes=1534`, corresponding distance-two and distance-three lines, followed by `VERIFY_OK`. The expected other two lines are:

```
distance=2: max=17, count=16, fixed=1, upper_nodes=360, census_nodes=718
distance=3: max=7, count=72, fixed=1, upper_nodes=89, census_nodes=259
```

The script's correctness argument does not infer impossibility from a timeout or a numeric search status: it enumerates the entire finite search tree subject only to a mathematically proved upper bound. This establishes the finite asserted results if the transparent code is executed as specified. The results are not independently audited and do not extend to any block length other than four or to unframed error correction.
