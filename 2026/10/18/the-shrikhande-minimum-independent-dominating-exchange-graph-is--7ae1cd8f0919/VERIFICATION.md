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

# Finite verification and limits

Reproduce with Python 3, from a directory containing these embedded files:

```sh
python3 verify_enumeration.py --certificate certificate.json
python3 verify_structural.py
```

`verify_enumeration.py` independently enumerates all independent subsets of sizes one, two, and three, builds all permitted exchanges, computes shortest-path histograms from each of the 32 optimum sets and rewrites `certificate.json` byte-identically. `verify_structural.py` independently constructs the full two-orbit description, checks the origin-pair classification, reconstructs the 32 triangular faces and all 48 dual adjacencies, and verifies the invertible linear map onto the face-dual adjacency graph. Its checks are not merely repetitions of prior output logs.

`enumeration.out` and `structural.out` are the recorded outputs. The finite certificate encodes all 32 optimal sets, all 48 legal transitions, and the uniform distance histogram. The mathematical proof in `RESULT.md` supplies the structural enumeration and bijection; the executable checks guard the small exact calculations.

No statement about infinite families is tested or claimed. Publication novelty may be affected by unindexed results; independent external audit has not been performed.
