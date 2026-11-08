---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Every retained translation contributes two rank-one Gabor atoms on edge (k,k+1) with diagonal two at each endpoint and offdiagonal modulus 2q, q=|cos(pi*ell/N)| in (0,1). Removing pairs creates positive-length path components or isolated vertices. Gauging phases along each path gives the exact disjoint union of blocks 2H_m(q) with diagonal 1,2,...,2,1 and q super/subdiagonals. The eigenvalue alpha_m is the unique hyperbolic root t_m via q(cosh t+sinh t*tanh(mt/2))=1, and increases strictly with m; beta_m increases strictly from Perron-positive Rayleigh extension. Therefore the condition number is beta_(max gap)/alpha_(min gap). Integer averaging forces min gap<=floor((N-h)/h), max gap>=ceil((N-h)/h), and strict monotonicity makes precisely balanced positive gap lists optimal, counted by (N/h)*binomial(h,r). For h>N/2 an isolated vertex is unavoidable. Independent complex Hermitian operator reconstruction and numerical spectra for 18,966 N,ell,h,E combinations across 190 families with N=3..11 agreed with Jacobi blocks and optimal masks, after correcting an initial integer-dtype bug in the *independent test*; the all-N proof is analytic, not finite enumeration.

## originality

PASS

Existing Gabor block-equivalence and erasure-robustness theory supplies foundational structure, and Resultary has similar-looking two-character harmonic frames, but not this two-tap, N-dimensional paired translation-erasure optimization. The exact Jacobi spectral decomposition, strict monotonicity, sharp optimal erasure geometry and labeled count were not covered by inspected primary statements. The elementary graph eigenvalue tools are not claimed new.

## value

PASS

Finite-frame conditioning after structured adversarial erasures is a natural signal-recovery design invariant. The result solves all configurations exactly under a motivated two-tap/two-modulation model, including a sharp survival threshold and complete equality classification, not a generic balanced-gap platitude.

The dated certificate retains the supplied scientific assessment, sources and limitations.
