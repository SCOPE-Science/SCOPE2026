---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For every n≥2, parity alternation and F=f²=x²(x²−2) prove ν₂(F(x))=2ν₂(x)+1 for even x and the exact iterated recurrences for the odd stage with b=ν₂(x²−1)≥3. The four square roots of 1 modulo 2^k for k≥3 produce exact even/odd valuation populations E_n,O_n. The four phase-specific thresholds yield the displayed C_n(t) and maximal depth, with power-of-two jump. Verified directly by independent exhaustive functional graphs and depth histograms for n=2,…,12 (all 8188 residue vertices in total). The unique cycle follows since valuations strictly rise after two steps. The supplied verifier source was inspected rather than trusted as proof.

## originality

PASS

Covers exactly the quantitative finite quotient histogram and sharp preperiod; Fan–Liao previously establishes the attracting two-cycle. Best-of-knowledge no dominating quantitative prior identified; older functional-graph literature remains a risk.

## value

PASS

The first-arrival histogram and maximal preperiod for every residue modulo all dyadic powers provide a complete, exact invariant for an important arithmetic dynamical map. Sharp logarithmic discontinuities refine qualitative p-adic attraction and can support future orbit statistics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
