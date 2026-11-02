---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Each factor distance partition about any root is equitable with transitions 0→1:k; 1→0,1,2:1,λ,k−λ−1; 2→1,2:μ,k−μ. Multiplying by counts a,b,c yields the five exact profile quotient transitions in RESULT.md. This prevents splitting within profiles and makes all class multiplicities factor-independent. A marked root propagates outward one graph-distance shell per synchronous step; shells at distances 2d−1 and 2d still share the far-region colour through 2d−2, so earlier stability is impossible. In the μ=2, k=2λ+2 regime, lower/same/upper shell degrees depend only on s=b+2c, so the distance shells are equitable and become distinct by round 2d−1. For μ≠2, B_s=s+(μ−2)c distinguishes coordinate profiles at round s; for μ=2 but k≠2λ+2, A_s=λs+(k−2λ−2)c distinguishes at the next round. The standard SRG parameter equation (v−k−1)μ=k(k−λ−1) supplies (1+(k/2)z)^(2d) distance sizes in the exceptional regime, and multinomial choices yield general profile sizes. Independently iterated this quotient refinement for C4, rook, Petersen and Clebsch parameters through d=5, matching sharp rounds and both class regimes. These experiments corroborate the uniform proof.

## originality

PASS

Best-of-knowledge: the complete mathematical claim was compared to exact or broader prior theorem statements, unlike-title aliases, current Resultary published findings and known data. Known premises and small cases are acknowledged. No inspected source demonstrates complete coverage; named inaccessible plausible full texts and reduction risks are recorded rather than claimed noncovering.

## value

PASS

This theorem exactly characterizes when a single rooted colour-refinement procedure detects coordinate-distance composition or only aggregate distance throughout an infinite class including nonisomorphic same-parameter factors. The exceptional linear-versus-quadratic colour count, sharp stopping round and precise multiplicities solve a natural graph-algorithm classification question; the distinctions are not routine graph-product terminology or mere finite-graph examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
