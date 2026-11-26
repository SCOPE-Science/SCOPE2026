---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The repaired finding claims exactly the minimum and maximum classification, expressly allowing other ties. With the stated Gram convention the roots-of-unity filter picks exponents j modulo N, and summation gives the positive eigenvalues. Adjacent ratios decrease with j and cross one at j=T_N(q). The hyperbolic-sine derivative and the two endpoint expansions establish the attainable staircase range. Strict log-concavity and the strict endpoint ratio place the unique minimum at N-1, including N=2. For fixed c, the error in j log(1-c/N) is O_c(1/N) on the whole grid; this and the denominator limit give the uniform profile. Its derivative changes sign only at x_c, and its positive equal endpoint values give the limiting minimum. Evaluation at x_c gives the condition number and its small/large-c limits. Synthesis uses the Gram quadratic form, so its condition number is the square root of the Gram ratio.

## originality

PASS

The repaired contribution is the exact extremal-mode staircase and the uniform many-node Bergman conditioning law. Cyclic Fourier filtering is standard, and the available same-kernel projection theorem gives the residue norms and hence the basic finite eigenvalue formula. Its fixed-orbit high-monomial-degree optimization does not already give this extremal-mode classification or many-node scaling. The strongest same-day match inspected has a different kernel and boundary scale.

## value

PASS

For normalized interpolation on a regular ring the worst upper mode changes discretely with radius, while the worst lower mode never changes. This affects sharp finite synthesis bounds; the uniform critical profile determines the limiting conditioning with an explicit dependence on how close to the boundary the nodes are. Fixing the overbroad degeneracy wording retains both useful results, beyond the finite spectrum computation alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
