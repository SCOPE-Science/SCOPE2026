---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Parity of σ(m)=m+S forbids even S because two odd squares in a five block cannot differ by 2; odd S forces all even block terms to be squares or twice-squares, eliminating even N by three even terms. For odd N the two even terms N+1,N+3 are opposite square types, producing a²−2b²=−2 or b²−2a²=2, and the divisor identities via σ(2b²)=3σ(b²) for odd b. Descent/multiplication by 3+2√2 parametrizes both Pell equations and geometric growth yields O(log X) candidate starts. Independently regenerated exactly 25 candidates in EACH Pell family with N<10^38, factored all a,b with sympy.factorint, reconstructed prime-power products and exact σ values; all 50 identities have NONZERO residual (minimum absolute residual 2). Largest coordinate 9733505285848307044<2^64. Thus no five-term run starts at 1<=N<10^38; no assertion beyond.

## originality

PASS

Best-of-knowledge new sharp five-term boundary: published six-term impossibility does not cover it; Pell sparseness and exact cutoff are not just number-table lookups.

## value

PASS

Length five is the first genuinely open boundary not ruled out by the published six-run pigeonhole argument; Pell families expose sparse remaining arithmetic cases and an exact 38-digit exclusion with a short replayable certificate. Both structural and finite theorem are mathematically motivated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
