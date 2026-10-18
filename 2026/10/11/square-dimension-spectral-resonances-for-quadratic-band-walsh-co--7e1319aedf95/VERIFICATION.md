---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Compute shell Gram G(x,y)=2^(−n)[1+s+((s²−n)/2)] with s=n−2dist(x,y), and expand as constant + point-incidence + pair-incidence kernels. On the k-slice with 2≤k≤n−2, two-subset incidence columns are independent: swap fixed vertices among k-sets forces row differences constant and then zero. Johnson sectors have dimensions 1,n−1,n(n−3)/2, and the bandwidth operator has n+1 zero modes. Incidence eigenvalues yield displayed a0,a1,a2, all positive. Independently factored every pairwise difference: a0−a1=((t−n)²−4(n−1))/(2(n−1)(n−2)); a1−a2=(n²−t)(t−1)/(n(n−1)(n−3)); a0−a2=((n−4)t²+(2n+4)t+n(n−2)(n−6))/(2n(n−2)(n−3)). Parity and interior shell range exactly force square n−1 and listed small exceptions. Rechecked algebra symbolically; stored checker finite 35 shells and n≤500 not substituted for proof.

## originality

PASS

A complete exact binary Walsh spatial-concentration spectrum plus an all-dimension arithmetic classification of degeneracies is not stated in the actual related Johnson-basis or Terwilliger block results inspected. The Johnson decomposition itself is old and credited. The new bounded conclusion is the explicit operator-specific three eigenvalue profile and perfect-square dimension crossings, not the existence of Johnson eigenspaces. Prior general block formulas might imply the values after nontrivial specialization and remain an explicit residual risk.

## value

PASS

Natural binary quadratic Fourier concentration on fixed Hamming shells has a complete exact spectrum, fixed nullity, and unexpectedly arithmetic collisions for infinite square dimensions. Identifying all sector crossings and triple degeneracy is a motivated, reusable exact spectral classification beyond the abstract Johnson module machinery.

The dated certificate retains the supplied scientific assessment, sources and limitations.
