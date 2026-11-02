---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Let a=v^T A^{-1}v, m=v^TAv, tau=||A^{-1}v-av||>0, u=(A^{-1}v-av)/tau, r=||(I-P2)Av||>0, w=(I-P2)Av/r, and P3 project onto span{v,u,w}. From Au=(v-aAv)/tau, the third mixed candidate is nonzero when a!=0. Multiplying A v=m v+((1-am)/tau)u+r w by A^{-1} and projecting orthogonally to P3 yields (I-P3)A^{-1}w=-[(1-am)/(tau*r)](I-P3)A^{-1}u. Thus premature fourth mixed breakdown with continuing split channel occurs exactly when am=1 and the four Laurent vectors A^{-2}v,A^{-1}v,v,Av are independent. Independence requires at least four distinct eigenvalues active in v: a polynomial of degree <=3 cannot have more than three distinct spectral roots; conversely four active points give independent Laurent vectors by multiplication by A^2. For either definite sign Cauchy-Schwarz forces am>=1, with equality only for a one-eigenvalue vector; indefinite four-distinct spectra permit positive spectral weights with am<1 and >1, and continuity gives am=1 while all four weights stay nonzero. Independent exact SymPy projector calculations for diag(-1,1,2,3) and v=(sqrt3,sqrt56,3,3)/sqrt77 yield a=11/14, m=14/11, tau²=103/539, r²=564/847, fourth split squared=14112/498623>0, mixed squared=0. These exact numbers corroborate the fully quantified spectral proof.

## originality

PASS

Qualified best-of-knowledge original contribution: A fourth-vector premature breakdown in inverse-leading extended Krylov construction. Closest prior work and limits are compared by implication, not title; priority risk retained.

## value

PASS

This identifies a genuinely algorithm-relevant structural counterexample: mixed-channel basis generation may falsely terminate on a zero candidate after successful first three vectors although the extended Krylov space still grows. The all-indefinite-four-distinct spectral iff and explicit condition-number-three witness show the failure is not solely due to ill-conditioning. The exact local obstruction is a motivated stability boundary rather than an arbitrary matrix certificate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
