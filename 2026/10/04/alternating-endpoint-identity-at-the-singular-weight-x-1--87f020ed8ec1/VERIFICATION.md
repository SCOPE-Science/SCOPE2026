---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The displayed quartic satisfies \(s_{n+1}-s_n=2P(n)\); this identity was independently expanded symbolically from the audited coefficients. Defining the stated endpoint quantity \(H_n\), substitution of the three-term recurrence makes the mixed coefficient equal to \(c n^r(-2P(n)+s_{n+1}-s_n)=0\), while the remaining square coefficient is exactly \(W_n\). The \(n=0\) boundary follows from \(u_1=P(0)u_0\), \(s_0=0\), \(s_1=2P(0)\). Telescoping therefore proves the identity for every \(N\ge1\), every integer \(r\ge1\), \(c\ne0\), and every cubic-or-lower \(P\).

## originality

PASS

Sun's current paper supplies a parameterized three-term-recurrence identity with auxiliary relation \(s_{n+1}(x)+x s_n(x)=2P(n)\), but the accessible detailed account confirms the printed formula has a singular \(x=-1\) boundary. The audited theorem solves the degenerate difference equation separately and produces finite endpoint coefficients rather than substituting into a legal source case. Resultary found only the assigned endpoint theorem. Full primary text of arXiv:2609.29910 and the closely related arXiv:2608.13192 could not be obtained through the checked lawful full-text routes; the authorized institutional retrieval attempt was safety-blocked and was not retried. That access gap is retained as a residual risk rather than treated as novelty proof.

## value

PASS

The result closes a natural singular boundary of a published parameterized identity where direct substitution is illegal. The exact finite endpoint formula and explicit polynomial solution are reusable for alternating Apéry-type sums, so this is a motivated boundary theorem rather than an arbitrary special value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
