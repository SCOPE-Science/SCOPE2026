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

Modulo π, X gives A²=0 of rank r, counted by choosing image U, kernel K⊃U and isomorphism k^n/K→U; 2r<=n. Every A conjugates to J=[0 0 I_r;0 0 0;0 0 0]. GL_n(R)→GL_n(k) is onto, so all fibers over A biject to lifts X=J+πB, including mixed characteristic, since J²=0 over R. X²=0 iff JB+BJ=0 over k, which forces B_WU=B_WC=B_CU=0 and B_WW=-B_UU; other free blocks dimension 2r(n-r)+s². Remove r unit Smith pivots; residual πB_CC is arbitrary s×s, giving t=rank_k(B_CC). Multiply independent count factors and divide for conditional rank law. Independent full enumeration n=2 over Z/4 gives strata (0,0):1,(0,1):9,(0,2):6,(1,0):12, total 28; Z/9 gives 1,32,48,72 total153, matching formula. These finite tests do not establish all n/rings.

## originality

PASS

General similarity classification for matrices over length-two local rings can imply ring-characteristic universality of some conjugacy statistics, and unrestricted Smith-type counts of chain-ring matrices are known. Neither the inspected Prasad–Singla–Spallone theorem nor Byrne et al unrestricted type counts explicitly supplies the full nonlinear square-zero Smith-stratified law; block-fiber analysis is required. This is qualified originality, with strong residual Hall-polynomial implication risk.

## value

PASS

The natural full Smith type distribution on the nonlinear variety X²=0 is an exact all-size invariant. It identifies the conditional free random-matrix rank law and proves equal/mixed characteristic universality, information useful for module-endomorphism enumeration and finite-chain-ring matrix problems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
