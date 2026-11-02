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

# Reproducibility and verification

Run `python3 verify.py` with Python 3 (standard library only). `verification_output.txt` contains the result of an actual invocation. The script computes the noncommutative truncated signature by dynamic programming, performs exact rational row-reduction to select homogeneous difference pairs, and checks the required cancellations for every selected pair in several small ranks. It checks expansion factors \(m=2,3\) by direct integer signature comparison at the critical homogeneous degree.

For \((q,k,R)=(2,2,2)\), the code checks all \(64\) constructed words against the *actual* length-two deck; for \((2,3,1)\) it checks all \(512\) actual length-three decks, and for \((3,2,1)\) it checks all \(256\) actual length-two decks. There are no collisions in these finite codebooks. It verifies the lower-deck recovery identity on representative examples. For three larger parameter sets, it verifies the rank and leading-term identities but does not enumerate the full codebook, since the predicted sizes are very large.

The all-parameter theorem follows from the symbolic word-pair induction, triangular injectivity, and fixed-length padding proof in `RESULT.md`; a finite computation cannot certify any untested value of \(q,k,R\). The imported upper bound is Nilforoushan–Parvaresh, Theorem 5.1 (arXiv:2609.23106). No independent mathematical review has been performed.
