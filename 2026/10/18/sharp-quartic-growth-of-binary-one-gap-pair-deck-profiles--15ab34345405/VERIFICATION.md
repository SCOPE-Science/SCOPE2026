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

# Verification and reproducibility

Execute `python3 verify.py` using Python 3 with only its standard library. The program independently constructs every one-gap ordered pair count directly from position pairs, and reconstructs the same profile from the four proof statistics. It checks all words through length \(12\) (the first counts are \(2,3,8,16,32,61,118,202,356,559,874,1296\) for lengths \(1\) through \(12\)). The program checks the full construction at the five lengths \(100,200,300,400,500\), obtaining respectively \(180,2793,13552,41625,99636\) pairwise distinct witnesses by their sufficient statistics, and directly checks their full pair counts at the first two lengths.

The arbitrary-length upper bound follows from reconstructing the observed pair counts using one-bit composition, alternating constant runs, and unrestricted scattered \(01\) counts. The lower bound follows from the explicit words and coprimality argument in `RESULT.md`. The program corroborates these identities at finite sizes; it does not prove the unbounded statement, which is established in the written proof. The leading coefficient, exact class counts at general lengths and ambiguity-class distribution have not been determined.
