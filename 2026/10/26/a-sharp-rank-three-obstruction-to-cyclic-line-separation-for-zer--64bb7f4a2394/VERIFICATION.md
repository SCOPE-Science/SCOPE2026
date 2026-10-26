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

# Reproducible verification

Run the companion source from the same package with Python 3:

```sh
python3 verify.py
```

Expected output:

```
VERIFY_OK rank3,4,5; rank2 exhaustive zero-sum-free multisequences [0, 8, 32, 72, 72]
```

The verifier checks every nonempty indexed subset of the six-term witness in \(\mathbb F_3^3\), checks all six cyclic-line intersections, checks rank-four and rank-five extensions, and exhaustively checks the rank-two property for every unordered nonzero indexed multisequence of length one through four. The rank-two enumerator uses combinations with repetition and independently rejects sequences having nonempty zero-sum subsets. All checks use exact integers reduced modulo three; there is no probabilistic step.

The group-algebra nilpotence argument, the quotient Davenport argument and the final-coordinate induction are independent general proofs in RESULT.md. Enumeration in finitely many ranks is not a proof of the assertions for every rank.
