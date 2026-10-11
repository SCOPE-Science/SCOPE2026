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

From \(3\sigma(m)=4m+d\), parity gives odd \(d\) exactly when odd \(m\) is a square. Otherwise \(d\mid2m\) gives \(v_2(d)=1\), hence \(v_2(\sigma(m))=1\). Multiplicativity leaves exactly one odd prime exponent, and the exact lifting formula \(v_2(\sigma(p^a))=v_2(p+1)+v_2(a+1)-1\) forces \(p\equiv a\equiv1\pmod4\). The actual finite verifier was inspected but is only corroborative.

## originality

PASS

The foundational and two-prime classification papers do not state the arbitrary-support valuation-one exponent-parity theorem or the odd-redundant-divisor iff square criterion.

## value

PASS

This gives a reusable structural filter for a natural 2-adic slice at arbitrary odd-prime support and explains the exponent patterns of early examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
