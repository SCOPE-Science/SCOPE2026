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

The symbolic proof shows that after the first move in a part \(X\), B can force one of exactly two terminal lengths: \(n_X\) by replying inside \(X\), or \(k\) by replying in a different part. This yields the normal-play and misere parity criteria directly.

`verify.py` independently constructs shortest-path distances, tests general-position legality without using the symbolic characterization, and solves both games by recursive minimax. The recorded output is:

```text
VERIFY_OK
checked 32 complete multipartite isomorphism types of order at most 10
K_{3,3}: B wins both games
K_{2,2,2}: B wins both games
```

The finite computation checks all admissible complete multipartite isomorphism types of order at most ten. It is corroboration only; the theorem for arbitrary part sizes follows from the proof.

The source comparison was performed against the primary statements in arXiv:2111.07425 and arXiv:2205.03526. The two propositions are retained; the correction concerns only the subsequent claimed equivalence.
