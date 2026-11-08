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

# Reproduction

Run from a directory containing the single standalone file `checker.py`:

```sh
python3 checker.py
```

The checker uses only Python's standard library. It enumerates exactly the generated subgroup of \(S_k\times\mathbb Z_r\) for each parameter triple \(2\le k\le6\), \(2\le r\le4\), \(1\le m<k\), checks the full expected group order, enumerates the accepted group projections to the point stabilizer, independently computes the quotient final set, and checks accessibility and pairwise distinguishability of the two inputs and the quotient through iterative DFA partition refinement. It separately verifies the group identity that the product of the chosen cycle and transposition has order dividing \(k-1\).

Expected output on successful completion is a PASS line covering 45 complete parameter cases, 37,494 exact group-state checks counting repeats among different choices of final set, and 165 quotient accepting-state checks. The current copy was executed successfully and reproduced this output.

# Mathematical verification boundaries

Finite group enumerations do not certify the unrestricted parameter theorem. The infinite proof relies on the explicit generating relations, the elementary finite-group fact that nonnegative words realize every group element, transitivity of the symmetric group and its point stabilizer, and Myhill–Nerode distinguishability. The existing unary spectrum \([1,mn]\) is invoked from the cited Rauch–Holzer theorem; its general proof is not reproduced or computationally rechecked here. No independent audit or external formal certification is claimed.
