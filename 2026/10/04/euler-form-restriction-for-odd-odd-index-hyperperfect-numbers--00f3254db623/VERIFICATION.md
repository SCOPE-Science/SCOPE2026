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

From the defining equation, \(k\sigma(n)=(k+1)(n+1)-2\). With \(k,n\) odd, the right side is \(2\pmod4\), so \(v_2(\sigma(n))=1\). Multiplicativity of \(\sigma\) and the parity of \(1+p+\cdots+p^a\) for odd \(p\) show that exactly one prime exponent is odd. If that exponent is \(\alpha\), LTE gives \(v_2(\sigma(q^\alpha))=v_2(q+1)+v_2(\alpha+1)-1=1\), forcing both valuations on the right to equal one and hence \(q,\alpha\equiv1\pmod4\). The inspected package verifier only enumerates small examples and is correctly treated as regression evidence, not the proof.

## originality

PASS

McCranie's full primary paper gives an odd-index sufficient family \(p^2q\) and explicitly labels its converse as Conjecture 1. It does not state the unrestricted two-adic valuation or Euler-form restriction. Fresh semantic searches for odd-index hyperperfect valuations, unique odd exponents, and modulo-four conditions returned no equivalent or stronger theorem. The audited result therefore supplies a genuine necessary condition strictly weaker than, but not implied by, the open converse conjecture.

## value

PASS

The theorem gives an Euler-style structural restriction for a longstanding odd-index hyperperfect problem, excludes all odd squarefree composites, and narrows any odd candidate toward the stronger published converse conjecture. The proof is short but the restriction is natural and applies uniformly to the unresolved family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
