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

The bundled standalone Python program `verify_linear_inner.py` runs with Python 3 and no third-party packages. It enumerates every ordered pair \(g,h\) of two-by-two matrices over prime fields \(\mathbb F_2\) and \(\mathbb F_3\), constructs the exact domains and images of the partial-inner generators, deduplicates them, and checks closure under all ordered compositions.

Observed outputs:

- `VERIFY_OK` for \(q=2\): 16 matrices, 256 generator pairs, 52 distinct maps with domain-size profile 1, 2, 16 having multiplicities 1, 45, 6; all 2,704 compositions checked.
- `VERIFY_OK` for \(q=3\): 81 matrices, 6,561 generator pairs, 201 distinct maps with domain-size profile 1, 3, 81 having multiplicities 1, 176, 24; all 40,401 compositions checked.

Proof of the theorem for any prime power uses finite-field linear algebra and is independent of these computations. The program does not enumerate nonprime extension fields and does not verify the historical originality of the result. Independent audit has not been performed.
