---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For arbitrary real symmetric X=[[m+d,z],[z,m-d]] with Frobenius PSD projection X_+, spectral eigenvalues m+-r, r=hypot(d,z), provide exact positive/mixed/negative formulas. In the mixed region the input-coordinate partial derivatives of output (11) and (12) have absolute row sums. With c=d/r, s=abs(z)/r, t=m/r these are optimized on t=-1,0,1 and c^2+s^2=1, yielding 3/2 for each diagonal and 9/8 for each off-diagonal, both strict away from rank-one limits. Piecewise segment integration yields global bounds; if a line is entirely determinant-zero, all its points share one rank-one direction and entrywise 1-Lipschitz holds. Explicit rank-one perturbations give first-order equality approach, so no two distinct finite matrices attain either larger Lipschitz supremum. Block embedding gives only L_n>=3/2, not sharp n>=3. Independent random finite-difference directional checks sampled 20,000 mixed-region perturbations; observed slopes below respective targets (1.4848,1.1148); the analytic inequality, not samples, proves uniform optimality.

## originality

PASS

Best-of-knowledge PASS: exact result and mathematical object are not established by accessible identified prior statements; reviewed aliases, reductions, stronger coverage and checked data. Distinct original ingredient: optimization of every coordinate derivative row in the transformed entrywise norm. Residual priority and access risks retained.

## value

PASS

Exact stability constants for the standard 2x2 PSD projector measured in an entrywise norm used in covariance approximation, and the genuinely different sharp diagonal/off-diagonal gains plus nonattainment. These are motivated sensitivity moduli not supplied by the Frobenius nonexpansivity theorem, and a nontrivial sharp inequality for a natural cone projection.

The dated certificate retains the supplied scientific assessment, sources and limitations.
