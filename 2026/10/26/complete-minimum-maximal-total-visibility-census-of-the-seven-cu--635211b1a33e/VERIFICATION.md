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

# Reproduction and checks

Run `python3 verify.py` in a directory containing the standalone script. It needs no third-party modules. Its output should match `verification_output.txt`.

The script enumerates all independent dominating subsets of size at most four in the even Hamming-parity halfcube for each dimension from one through seven. For the seven-cube it exhaustively checks every independent candidate in each relevant size, reports 1,120 qualifying four-sets, verifies their pairwise-distance multiset and checks their affine XOR identity. It additionally constructs a concrete eight-vertex union and tests the *original shortest-path visibility condition*, over all ordered endpoint pairs, after removing forbidden internal vertices. All 120 possible single-vertex additions fail. These tests agree with, but are not substituted for, the structural proof in `RESULT.md`.

Actual recorded key output:

```
HALF n=7 minimum=4 number=1120
Q7_PATTERNS [((4, 4, 4, 4, 6, 6), 1120)]
Q7_ALL_AFFINE 1120
DIRECT_GEODESICS_Q7=PASS; ALL_120_SINGLE_VERTEX_ADDITIONS=FAIL
TOTAL_MINIMAL_Q7=8 TOTAL_NUMBER=1254400
VERIFICATION_OK
```

The code is a finite exact enumeration for this fixed dimension; it does not certify any arbitrary-dimension claim. The mathematical proof establishes the full census of the fixed seven-cube. No independent external audit or certification has been performed.
