---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For compact invariant μ supported in 0<m≤X≤M<∞, Y=log(X/K) and Y² are bounded. The EXACT cocycle Y∘F−Y=r(1−X/K) integrates to E[X]=K. Squaring the increment gives 0=−2r E[Y(X/K−1)]+r²E[(1−X/K)²]. Divide by r>0 and rescale to 2K Cov(log X,X)=r Var(X). Non-Dirac means Var(X)>0 and recovers r; Var=0 forces δ_K, invariant for every r. Mean K and non-Dirac force positive mass on both sides. Finite rational checker fetched at exact package path verifies expansion and rescaling only, not the invariant-law theorem.

## originality

PASS

Best-of-knowledge original structural inference is exact growth-rate recovery from a single non-Dirac invariant marginal, not the already known first-moment calibration. Primary Sacker 2007 full-text expression (1.8) telescopes first moment for periodic Ricker recurrence, but does not present the stationary second-log-moment covariance identity or its implication. Other identified parameter-inference works use observations or different dynamical systems; they do not imply this invariant-law formula.

## value

PASS

One-time stationary law identifies both K and r for a canonical nonlinear ecological model, and exact equilibrium/non-equilibrium exception is necessary; this is a motivated inverse-dynamics property and is not merely restating a routine first-moment average.

The dated certificate retains the supplied scientific assessment, sources and limitations.
