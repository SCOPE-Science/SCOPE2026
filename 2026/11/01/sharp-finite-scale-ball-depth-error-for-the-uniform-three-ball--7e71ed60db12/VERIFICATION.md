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

# Verification of the exact three-ball depth gap

The self-contained argument in RESULT.md proves the formula, normalization, boundary behavior, global optimum, and expansion. The included standard-library `verify.py` checks the precise claim from independently integrated rational slices. Execute `python verify.py` using Python 3. It is expected to print `PASS: 1850 exact rational and high-precision diagnostic checks`; that output was observed for the packaged source before acceptance.

The script evaluates the radical-plane slice integrations for 8 rational testing radii and 38 interior radii, verifies the depth-minus-halfspace identity and geometric feasibility exactly, checks optimization equations in 65-digit decimal arithmetic at multiple scales, tests sampled global comparisons, verifies the endpoint exact constant, and checks the first asymptotic terms numerically.

These are finite diagnostics and are *not* substitutes for the continuous proof. The derivation of the exact lens expression, strict overlap decrease, unique critical radius, and precise boundary limits is given explicitly in RESULT.md. The claims are restricted to the three-dimensional volume-uniform ball and testing radii at least 1; no assertions of independent certification or generality to other measures are made.
