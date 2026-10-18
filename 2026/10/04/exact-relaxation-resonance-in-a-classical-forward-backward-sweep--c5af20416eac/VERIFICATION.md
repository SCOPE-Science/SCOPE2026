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

For the exactly specified continuous-time LQ problem x'=x+u on [0,1] with state weight 3 and terminal adjoint zero, control differences satisfy tilde e=-3K*K e with Volterra Kf(t)=int_0^t e^(t-s)f(s)ds. A=K*K positive compact self-adjoint. Direct calculation K(1-t)=t and K*t=1-t gives eigenvalue 1; boundary eigenproblem f''+(1/mu-1)f=0, f'(0)+f(0)=f(1)=0 excludes mu>1 and gives subleading mu_j=(1+k_j^2)^-1, tan k_j=k_j, k1>pi, mu_j->0. Therefore norm(I-omega(I+3A))=max(|1-omega|,|1-4omega|). All-error L2 contraction iff 0<omega<1/2, unique minimax omega=2/5 factor 3/5; leading mode -3 unrelaxed and -1 at half relaxation, with orthogonal component contracting at norm 1/2 and consecutive averaging canceling neutral two-cycle. Independent dense quadrature gave K*K(1-t) agreement ~1e-6, plus exact rational endpoint/minimax checks. No claims about discretized implementation.

## originality

PASS

Best-of-knowledge statement-level prior comparison: the exact final claim goes beyond inspected narrower qualitative, lower-bound, upper-bound or Poisson-restricted results. This is not a claim of exhaustive historical priority; see four comparisons and source-specific risks.

## value

PASS

Sharp analytic resolution of the divergence/alternation boundary in a canonical documented counterexample to forward–backward sweep; explicitly identifies a bad eigenmode, stabilizing relaxation interval, optimal fixed relaxation, and why paired averaging works. This is a motivated exact numerical-analysis benchmark, not a generic Richardson parameter restatement absent the nontrivial source-specific spectrum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
