---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Exact rational verification

`python3 check.py` checks the exact inequalities at every integer \(2\le n\le499\), including the boundary tie, using only Python's `fractions.Fraction` and `math.factorial`. For \(2\le n\le32\) it also compares the compact last-place formulas against independently expanded Erlang integrals. It checks the rational Taylor-series bounds on the exponential constants and the two explicit infinite-range lower estimates for \(n\ge500\).

The proof of the infinite-range estimates and of the integration identities appears in RESULT.md. Assertions on finitely many integer inputs do not, by themselves, prove statements for unbounded integer parameters. Scientific review was limited to these explicit assumptions and formulas; independent validation has not been performed.
