---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Reconstructed odd-majority polynomial h_r and its exact two-new-voter step: h_(r+1)-h_r=binom(2r+1,r)p^(r+1)(1-p)^(r+1)(2p-1). Integrating against Beta(alpha,beta) and evaluating at mu=alpha/(alpha+beta) gives the stated successive-gain ratio R_r. Its initial value s^2/((s+1)(s+2))<1; the sign of R_(r+1)/R_r-1 is controlled by F(t)=(alpha-beta)^2*t^2+[s^3-alpha*beta*(4s+6)]*t-alpha*beta*(3s+2), t=r+1. For alpha!=beta, positive leading coefficient and negative constant imply exactly one positive root and a single valley in R; asymptotic quotient s^2/(4alpha beta)>1 forces a unique crossing of 1, with a possible equality step/two adjacent maxima. The signed accuracy gap begins zero, rises then falls toward a strictly positive de Finetti/LLN limit, hence its absolute value has the same peak and remains positive. alpha=beta gives symmetry and identically zero gap. Independently recomputed 168 exact-rational majority-step comparisons including alpha,beta fractional values and the (10,1) five-juror maximizer; this is only a finite cross-check.

## originality

PASS

Best-of-knowledge new exact finite-jury-size optimization of the error caused by replacing a *fixed Beta latent mixture* with equal-marginal unconditional independence. Earlier jury theorems, including explicit Beta-binomial treatments, establish dependence and asymptotics but consulted material did not exhibit the one-valley consecutive-gain ratio or global index/tie classification. Berg 1993 is a serious potentially overlapping source: only a citation/indexed description was accessible, not its full theorem proofs; this is a genuine residual priority risk rather than proof of noncoverage.

## value

PASS

The fixed-marginal correlated-vote independence approximation is a natural and consequential calibration question; the exact unique worst finite panel size and a constructive five-voter counterexample to monotone-in-size error are not a routine bound or arbitrary slice. The result supplies a sharp global structure and exact tie criterion in the canonical exchangeable Beta mixture, while clearly excluding arbitrary voting dependence and strategic behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
