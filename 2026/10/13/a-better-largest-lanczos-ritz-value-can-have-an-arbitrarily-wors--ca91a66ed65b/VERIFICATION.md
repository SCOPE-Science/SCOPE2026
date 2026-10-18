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

For 0<eps<1 the SPD diagonal family diag(1,1+eps,2) has condition number exactly 2. The first normalized Rayleigh residual has square eps^2(eps^2-2eps+3)/(eps^2+2)^2. The explicit Krylov basis u=(1,1,eps), w=(-1,0,1-eps) yields a symmetric definite 2x2 pencil whose limiting matrices G=[[2,-1],[-1,2]], H=[[2,-1],[-1,3]] have Ritz roots 1 and 5/3. Its larger unit Ritz vector tends to (-1,1,2)/sqrt(6), residual sqrt(2)/3. Since r1/eps ->sqrt(3)/2, r2/r1~2sqrt(6)/(9eps), while the top Ritz value strictly increases and the eigenvalue-error ratio ->1/3. In dimension 2 the second Krylov space is either invariant already or full, hence no positive second residual. Fresh independent symbolic pencil and numerical eigenresidual checks reproduced all central claims. Finite checks do not supply the limiting proof; simplicity and continuity of the limiting pencil do.

## originality

PASS

Earlier Rayleigh–Ritz convergence results identify conditional convergence of Ritz vectors and importance of residual diagnostics. A Resultary study gives extremal residual gain under a prescribed spectral filter, not this adaptively selected largest Ritz vector after one Lanczos step. Neither inspected primary source or related published record supplies the condition-two, dimension-three near-breakdown asymptotic and strict Ritz-value improvement as a single instance.

## value

PASS

A sharp counterexample separates monotone extremal Ritz-value improvement from monotonicity of eigenpair residuals in exact Hermitian Lanczos, with no nonnormality or ill-conditioning; it provides an explicit scaling law for a practical convergence diagnostic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
