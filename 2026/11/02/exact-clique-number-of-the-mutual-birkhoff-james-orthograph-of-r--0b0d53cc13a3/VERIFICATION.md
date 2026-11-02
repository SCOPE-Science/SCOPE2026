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
# Verification and limitations

The analytic proof gives an exact test for directed real Birkhoff–James orthogonality, demonstrates that active-coordinate rounding is a graph retraction, and identifies the finite image with a signed-subset incomparability graph. A random full signing and ordering produces a uniform rank-\(k\) chain law. The resulting Lubell bound proves the upper inequality for all positive integer dimensions and is saturated by a full support-size layer.

Run the provided self-contained checker from this directory with `python3 verify.py`. On the recorded run it printed:

```
ternary pair/order tests: 74190
rounding edge tests: 15628
uniform-chain checks: 4
VERIFY_OK
```

The checks cover every distinct pair of projective ternary vectors in dimensions one through six and every mutual edge in the finite projective coordinate grid with entries -2,-1,0,1,2 through dimension four. They also verify uniform chain incidences in dimensions one through four. These tests verify finite instances and possible normalization mistakes; they do not certify the general theorem without the proof in RESULT.md. No external/infinite certification is claimed.

The exact statement is for real scalars only. It does not give the complex clique number or all maximizing cliques. Full-text examination of one plausible 2022 review chapter was not achieved; its abstract and references were inspected, and it remains a literature risk. Independent audit and independent validation have not been performed.
