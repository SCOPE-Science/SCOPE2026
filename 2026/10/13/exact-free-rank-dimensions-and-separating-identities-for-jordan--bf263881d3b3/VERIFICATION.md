---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For finite g_s, relatively free algebra equals coordinate-generated term-function algebra on g_s^n. Every bracket term is linear in ideal inputs u_i; polynomially varying action is P(a_i J_s) on J_s(a_i u_j-a_j u_i). The ring B_s=F_q[J_s]=F_q[eta]/(eta^s) is dimension s and faithful on the ideal. For nonzero a, some a_i !=0 makes polynomial evaluation onto B_s. Its kernel has radical the distinct rational point maximal ideal m_a, so CRT interpolates all nonzero fibers independently even when s>q. Basic scalar syzygies form a free B_s-module of rank n-1 at each a !=0, zero at a=0, yielding derived dimension s(n-1)(q^n-1); n independent t-coordinate functions give full formula, including n=1. Identity follows (aJ_s)^q-aJ_s=-aN_s(1-N_s^(q-1)), exact nilpotency index s for nonzero a; it fails for s+1 using top Jordan vector. Thus strict varieties and exponent q. Reconstructed a **separate** GF(2) term-function Lie-bracket closure algorithm: ranks (s,n)=(1,2)->5,(2,2)->8,(3,2)->11,(2,3)->31, agreeing with theorem; not an all-field proof.

## originality

PASS

Published exact affine 2-dimensional Lie free-rank dimension n+(n-1)(q^n-1) is precisely s=1; nonsemisimple indecomposable Jordan blocks require a local nilpotent operator-valued CRT interpolation rather than mere scalar pointwise interpolation. Bahturin--Olshanskii Example 7 considers arbitrary-dimensional **irreducible** modules and only q exponential growth, not indecomposable unipotent Jordan length s nor separating adjoint identities. Existing same-growth claims are credited. Old Bahturin 1979 identities literature is potentially relevant and unread in full.

## value

PASS

A natural exact invariant and explicit ascending identity hierarchy for indecomposable nonsemisimple Lie extensions over arbitrary finite fields. It distinguishes Jordan lengths that growth exponent alone cannot, determines all rank-n dimensions and derived sections, and extends published s=1 result substantively rather than scalar renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
