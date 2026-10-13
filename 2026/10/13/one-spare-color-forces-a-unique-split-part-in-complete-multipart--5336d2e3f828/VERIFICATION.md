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

# Verification and limits

The theorem's proof is mathematical and applies to all integers \(r\ge3\) and positive part orders; finite testing is corroborative only.

For reproducibility, compile and run `verify.cpp` using a C++17 compiler:

```
g++ -std=c++17 -O2 -Wall -Wextra verify.cpp -o verify
./verify
```

The verifier enumerates every initial state of each checked profile, rejects assignments conflicting across parts, simulates missing-color forcing until no further changes, and counts successful initial domain sizes. Separately it evaluates the proposed size-enumerator via binomial coefficients and exact integer arithmetic; disagreement terminates the program with an error. It tested 34 nondecreasing profiles with two to four nonempty parts, part sizes at most four, and total vertices at most eight, comprising 9,213,533 initial states. This includes \(r=2\) boundary checks (not newly claimed) and \(r\in\{3,4\}\) cases within the theorem. Recorded console results are in `verification_output.txt`.

The test is exhaustive only over the stated finite profiles; it does not independently certify unbounded parameter values, exclude an undiscovered equivalence in prior literature, or replace outside review. No independent external audit was performed.
