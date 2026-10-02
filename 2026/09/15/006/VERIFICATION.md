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

Schreier-Aigner's published QTC2 definition imposes the complementarity relation at all cells with unequal row and column indices, so the main diagonal is exempt. The involution sends \((i,j)\) to \((a+1-j,a+1-i)\), whose fixed set is the anti-diagonal. For every \(a\ge2\), the anti-diagonal cell \((1,a)\) is fixed and is not on the exempted main diagonal, forcing \(2\pi_{1,a}=c\). Integer entries therefore make every odd box height impossible. The same source's Conjecture 4.2 and Appendix A.2 give nonzero odd-height values, including the \(a=2,c=1\) value 4, so the universal formula is indeed false. The brute-force package script independently corroborates small cases but is not needed for the proof.

## originality

PASS

Fresh Resultary and literature searches found no prior published correction of Conjecture 4.2 by this fixed-cell parity obstruction. A nearby later paper concerns first-kind QTCPP, not QTC2. Thus the disproof is best-of-knowledge original.

## value

PASS

Although the proof is short, it invalidates an explicit published conjecture and data table for an infinite family of parameters and pinpoints the structural source of the error: the wrong diagonal is exempted relative to the symmetry's fixed set. This is a motivated correction, not an arbitrary tiny counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
