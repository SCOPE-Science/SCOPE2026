---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For positive spike a and S_a e0=a e1 with later weights 1, RESULT.md decomposes (S⊗S*+S*⊗S)/2 into homogeneous real Jacobi blocks, then parity-reflected ± blocks. Uniform exterior Chebyshev Schur complements converge to f(lambda)=lambda-(a²/2)rho(lambda), and f=0 permits |rho|<1 precisely when a>sqrt(2), giving ±E=a²/(2sqrt(a²-1)). Separate parity-adapted Weyl sequences prove [-1,1] essential and boundary-localized ±E essential; no other exterior accumulation. Thus Fredholm essential spectra both equal band alone at/below threshold, plus detached ±E above; essential norm follows, not full norm. Independent numerical Jacobi and parity-folded block eigenvalues at n=120 for a=1,1.4,sqrt2,1.8,2.4 corroborated threshold and E to numerical precision. Unrestricted proof is resolvent convergence plus Weyl criterion, not numerics; low n blocks do not change essential spectrum.

## originality

PASS

Existing tensor-weighted-shift point spectrum decompositions and standard one-sided Jacobi boundary theory are substantial prior work; inspected papers do not compute the same infinite direct-sum Fredholm essential spectrum in both tensor flip sectors or the exact spike threshold. Best-of-knowledge with possible implicit reduction risk.

## value

PASS

Fredholm essential spectrum and essential norm are natural invariants of symmetric/exterior tensor operator constructions. The exact one-spike threshold separates pure continuous band from two isolated essential spectral points in both parity sectors, and explains a nontrivial finite-block versus infinite-sum distinction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
