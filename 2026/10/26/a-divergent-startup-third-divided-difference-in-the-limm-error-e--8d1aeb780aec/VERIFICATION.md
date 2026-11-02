---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Directly read the lawful Virginia Tech accepted manuscript (2022), Section 7: equation (7.4) defines delta^{k+1}=y^{(k+1)}(xi)/(k+1)!; (7.5) multiplies by (k+1)! C_k h^{k+1}; Remark 7.2 prints delta2=[(y1-y0)/h-f0]/(2h), delta3=[delta2-J0 f0]/(3h). For y′=y y0=f0=J0=1 and first-order LIMM (1-h)(y1-y0)=h, exact algebra gives y1=1/(1-h), delta2=1/[2(1-h)], delta3=(2h-1)/[6h(1-h)]. Thus h delta3 -> -1/6 while exact limit +1/6. Independent fractions verify formula for h=1/10,1/100,1/1000; the rational identity proves the asymptotic, not finite extrapolation. arXiv v1 numbering differs (Remark8.2), accepted manuscript confirms cited Remark7.2/eq7.4,7.5.

## originality

PASS

Best-of-knowledge after statement-level comparison: Equivalent formulation: the printed initial delta3 estimate fails even consistency on analytic scalar y′=y and its h^3-scaled contribution is O(h^2) rather than O(h^3). This is an explicit symbolic comparison within the same paper, not independent method invention. Standard divided-difference convergence and consistency theory entails the correct target y′′′/6; the submitted discovery identifies a specific contradicting printed instruction. No broader LIMM convergence theorem is disproved, and code may use a corrected formula.

## value

PASS

This is a mathematically explicit inconsistency between a published numerical method’s normalized divided difference and its startup approximation. The wrong asymptotic *order*, not merely coefficient, matters for the adaptive controller’s first error estimate and motivates checking or correcting implementations, without claiming convergence failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
