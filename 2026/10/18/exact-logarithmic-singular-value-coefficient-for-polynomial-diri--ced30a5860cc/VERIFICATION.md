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

# Verification record

The exact infinite-dimensional proof is the four-step argument in RESULT.md, independent of finite experiments. Step 1 is a coefficient identity on finitely supported inputs followed by bounded extension. Step 2 uses the finite-variable Hardy multiplier norm. Step 3 constructs a dimension-proportional orthonormal family whose image is uniformly bounded below, establishing the lower bound for every singular-value index. Step 4 is an exact quadratic optimization with parameter in \([-1,1]\).

Run \(\texttt{python3 check.py}\) from the extracted package. It uses only the Python standard library and reports 194,050 passed finite diagnostic assertions, including rational identity checks, multiplicative translation identities, disjoint support graph packing and the exact monomial formula. These tests do not prove the infinite-dimensional limit, nor independently validate the science. No proof assistant, external certification, or independent audit is asserted.
