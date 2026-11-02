---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

The mass Gram matrix is (6n)^{-1} times a strictly positive circulant tridiagonal matrix A with diagonal 4 and neighbor 1 (including n=3). The Green recurrence 4g_j+g_{j-1}+g_{j+1}=delta_{0j} has summable solution (-q)^|j|/(2sqrt(3)), q=2-sqrt(3); periodization gives the exact inverse A_n. Differencing rows 1 and 0 yields a signed derivative hat kernel, and L-infinity/L1 duality gives the sharp norm attained by the sign of that kernel. Nodal sign alternation (one exact zero for odd n) makes absolute affine-cell integrals equal the displayed cyclic rational expression, without vanishing denominators. The infinite signed kernel has exact absolute integral (9-sqrt(3))/2 from a central crossing plus geometric tails. The finite kernel is its absolute-convergent periodization, where cancellation of opposed copies on a positive-length subinterval makes strict inequality; the tail bound on a centered length-n interval is O(q^(n/2)). These analytic facts prove all n>=3, not merely numerically tested n.

## originality

PASS

Best-of-knowledge: inspected relevant primary proofs on interval Lebesgue norms and periodic spline projector L-infinity boundedness do not imply the sharp norm after differentiation, the all-n formula or strict exponentially decaying finite-period deficit. The bi-infinite Gram recurrence is prior technique, not claimed novelty. Search comparisons considered equivalent operator formulations, broader prior results, databases/tables and exact claim implication, with an inaccessible plausible Oswald paper recorded as a risk, not a fabricated negative result.

## value

PASS

Sharp rough-input to slope amplification is a mathematically natural stability invariant of the uniform periodic linear-spline L2 projector. Its exact finite-mesh values and sharp algebraic constant with exponential finite-circle stabilization give quantitative benchmark information for Galerkin reconstruction that generic order-of-growth inverse estimates and the projector Lebesgue norm do not determine. This is an exact structural family, not an arbitrary small numerical slice or a claim about all spline orders.

The dated certificate retains the supplied scientific assessment, sources and limitations.
