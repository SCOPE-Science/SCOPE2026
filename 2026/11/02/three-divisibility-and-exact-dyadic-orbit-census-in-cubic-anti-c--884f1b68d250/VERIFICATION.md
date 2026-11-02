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

# Reproduction checks

Execute `python3 verify.py` using Python 3.10 or newer. No third-party packages, external downloads, or environment configuration are required. The script constructs Boolean adjacency matrices directly from the specified prism graph, calculates their powers and ranks over \(\mathbb F_2\), and checks the predicted invertibility, fixed-point dimensions, eventual-periodic ranks and nilpotent entry bounds. Every initial state is enumerated on \(G_4\) and \(G_8\), and exact cycle counts are compared to the theorem. Larger values use exact operator identities rather than state-space enumeration.

Successful verified output includes:

```
PASS: invertibility and eventual-periodic ranks, n=3..36 (34 graphs)
PASS: dyadic fixed-space dimensions and exact global orders, n=4,8,16,32,64
PASS: exhaustive orbit census, n=4 and 8 {4: {1: 16, 2: 240}, 8: {1: 16, 2: 240, 4: 65280}}
```

These are numbers of *states* with given least period, not numbers of distinct cycles. Divide them by their respective period lengths to obtain the cycle counts. The finite script does not prove the result for unrestricted circumference; the polynomial-ring argument in `RESULT.md` supplies that proof. No independent audit or validation has been performed.
