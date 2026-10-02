---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-01.md",
      "INDEPENDENT_AUDIT_2026-10-01.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

From T=nH(n), reduction modulo each maximal prime power P_i leaves exactly 1+m_i(1+...+p_i^{a_i-1}); multiplying by p_i-1 yields the iff congruence m_i≡p_i-1 mod P_i. CRT gives integrality. For at most four supports, the reciprocal upper bounds are all <2, so a positive integral H(n) equals 1. In the three-support slice, the reduction d-1=(Aq-d(r-1))V is valid; d=1 forces (A,q,r)=(2,3,7), while d>1 first forces c=1 and then a modulo-3 contradiction. The finite verifier checks 98,158 integers through 100,000 and the first twelve 6·7^c cases, but is used only as corroboration.

## originality

PASS

No inspected prior source implies the exact maximal-prime-power congruence criterion or the three-support middle-exponent-one converse. Machacek gives the definition and sufficient constructions; the 1-Sondow congruence concerns a different reciprocal sum and coincides only in the squarefree specialization.

## value

PASS

This is a motivated structural result for a named Egyptian-fraction class: it converts a global integrality condition into independent prime-power congruences and gives a natural complete classification in the three-support slice with simple middle prime. Those facts can guide both construction and exclusion beyond a finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
