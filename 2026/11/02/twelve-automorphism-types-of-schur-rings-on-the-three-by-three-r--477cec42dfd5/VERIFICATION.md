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

# Reproducible finite verification

The semigroup, partition encoding, and complete row/column criterion are defined in `RESULT.md`. No third-party packages or external data are required.

Execute the two genuinely separate verification routes:

```sh
python3 CHECK_DIRECT.py
python3 CHECK_PROFILE.py
```

`CHECK_DIRECT.py` enumerates all restricted-growth strings of length nine and directly calculates all class-sum product structure constants in the nine-element semigroup. Separately, it constructs all subgroups of \(S_3\times S_3\) by repeated group closure and computes all orbit partitions. It tests equality between orbit partitions and Schur partitions, computes the 25 direct products, and derives the 12 automorphism orbit representatives.

`CHECK_PROFILE.py` independently enumerates the partitions, applies the complete profile-equality criterion, and checks by direct action of all 36 automorphisms that each accepted class is an orbit of its full class stabilizer. It also independently computes the 12 automorphism types.

The outputs are stored exactly as UTF-8 text in `CHECK_DIRECT_OUTPUT.txt` and `CHECK_PROFILE_OUTPUT.txt`. Both programs were run on their actual included contents and returned `VERIFY_OK`. Tested coverage is complete for the nine-cell problem (21,147 out of 21,147 partitions). Neither program purports to prove a statement about all rectangular bands or historical originality. No independent external audit has been performed.
