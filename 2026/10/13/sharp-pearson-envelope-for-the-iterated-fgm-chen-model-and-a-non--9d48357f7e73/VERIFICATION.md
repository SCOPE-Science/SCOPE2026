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

With identical Chen quantile Q and IFGM density c=1+gamma(1-2u)(1-2v)+omega*u(2-3u)*v(2-3v), covariance separates as gamma A^2+omega B^2; Pearson rho=a gamma+b omega, a=A^2/Var(Q), b=B^2/Var(Q). Integration by parts gives A=-int Q'u(1-u), B=-int Q'u^2(1-u) and Q'>0, hence 0<b<a. The stated full admissible region has gamma in [-1,1], omega between -1-gamma and U(gamma)=(3-gamma+sqrt(9-6gamma-3gamma^2))/2. Lower bound rho=-a attained uniquely at (-1,0); maximizing the affine functional along U, set t=1+gamma and apply sharp circle Cauchy-Schwarz, obtaining -a+2b+sqrt((2a-b)^2+3b^2) uniquely at gamma*=-1+2(2a-b)/sqrt((2a-b)^2+3b^2), omega*=U(gamma*). At (1,1), rho=a+b strictly lower by sqrt((2a-b)^2+3b^2)-(2a-b). Independently computed high-precision Chen integral coefficients for theta=2,beta=1.5: a~0.32220220885248, b~0.09586239733703, corner ~0.4180646061895 and max ~0.4426431191991, gamma*~0.914229 and omega*~1.544677.

## originality

PASS

The 1984 Huang-Kotz primary abstract claims general IFGM maximum correlations and parameter region; this may already cover the generic linear-functional geometry and is explicitly not claimed as novel. Alawady et al 2026 make a specific incorrect Chen-margin Pearson maximizing-corner statement and numerical conclusion in their Section 3.1. The inspected primary full text supports that source-specific error, while this result supplies its exact corrected Chen-parameter optimizer and strict gap for all positive parameters. Neither earlier generic ingredients nor other marginal-specific studies are assumed absent; their possible implication is a residual risk. Accept as an explicitly motivated source-specific correction on best knowledge, not priority for generic support function.

## value

PASS

Corrects a materially wrong published model-specific optimum and its reported dependence envelope. A universal strict corner shortfall, unique optimizer and concrete corrected Chen correlation are meaningful for interpretation/calibration of that model; generic optimization tools are credited to prior work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
