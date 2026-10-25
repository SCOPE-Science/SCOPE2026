---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

The exact inverse is lower bidiagonal with entries i/n and -(i-1)/n. Delete interblock entries: rank <=L-1 gives Kolmogorov distance <=(L-1)/n and W1 <=2(L-1)/n on [0,2]. Freezing each m-length block in spectral norm costs <=2m/n. The eigenvalues of (I-S_l)^*(I-S_l) are 4sin^2((2j-1)pi/(4l+2)); angle-cell coupling costs <=pi L/n and position coupling <=2m/n. Summing gives [2(L-1)+pi L+4m]/n, under 12/sqrt(n) for m=ceil(sqrt(n)) and n>=16; support diameter handles n<16. Conditioning U derives CDF and strictly positive interior density, yielding quantiles. The clipping map is M^2-Lipschitz on [0,2]. Independent finite singular-value and CDF-integral checks agreed at small/moderate n; these checks are diagnostics, not the all-n argument.

## originality

PASS

PASS is restricted to the explicit all-dimension quantitative W1 bound and clipped reciprocal consequences. General GLT theory already gives the unquantified bulk symbol, and the fixed-higher-rank edge result covers a different asymptotic. No inspected primary theorem supplied this W1 rate or its universal numerical constant; undiscovered quantitative GLT refinements remain possible.

## value

PASS

The uniform effective transport error controls a natural full-bulk spectral invariant and finite-matrix nonlinear statistics, unlike mere weak convergence or a fixed-rank edge expansion. The exact constant is not claimed sharp. This is more than recomputation of a known limiting distribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
