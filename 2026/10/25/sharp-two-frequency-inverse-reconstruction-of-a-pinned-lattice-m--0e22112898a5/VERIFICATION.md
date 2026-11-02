---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The infinite nearest-neighbor host recurrence has essential squared-frequency band [kappa,kappa+4]. Strictly positive quadratic form for kappa,kappa0,mu>0 removes nonpositive eigenvalues; unit-modulus recurrence excludes embedded and band-edge square-summable modes. Outside the band the only allowed symmetric tails are p^|n| and (-q)^|n|, with 0<p,q<1. Defect matching yields two linear equations in (mu,kappa0); subtraction gives mu=2pq/(1+pq), and kappa0=2[kappa pq-(1-p)(1+q)]/(1+pq). Hence physical positivity iff kappa pq>(1-p)(1+q). F(r) is strictly decreasing on (-1,0),(0,1); its end signs show one simple localized eigenvalue on each side and none else. Equality gives excluded kappa0=0, not a physical impurity. The actual checker and an independent high precision four-pair reconstruction independently verify matching equations and feasible/infeasible boundaries; finite spectra do not prove the all-chain claims.

## originality

PASS

QUALIFIED PASS: Full primary Manzhelii-Feodosyev (2025) contains a three-parameter forward localized-mode analysis and approximate quadratic formulas; it is close antecedent for two-sided existence, not a proof written as two-eigenvalue-only exact inverse image/uniqueness theorem with an iff positive-pinning inequality at fixed host bonds. Finite spring-mass inverse results typically use eigenpairs or extra physical data. The algebraic derivation is short and source forward data may imply an equivalent specialization; residual priority risk is explicit.

## value

PASS

Exact spectral identifiability is a naturally motivated inverse problem. Two measured localization frequencies suffice for unique recovery only on a sharply identified physically realizable region; the boundary distinguishes a vanishing substrate spring from admissible positive pinning and excludes spurious band modes. The classification supports precise inverse benchmarks even though it does not establish noise robustness or laboratory recovery.

The dated certificate retains the supplied scientific assessment, sources and limitations.
