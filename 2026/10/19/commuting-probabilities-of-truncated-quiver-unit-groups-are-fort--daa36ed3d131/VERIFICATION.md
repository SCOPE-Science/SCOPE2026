---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

The nonisomorphism proof compares the kernels of two explicit character maps on \((\mathbb Z/(p-1))^3\). The cycle map has coordinate forms \(x-z,y-x,z-y\), whereas the transitive map has coordinate forms \(x+z,y-x,-y-z\). These yield the two displayed kernels and their distinguishing vector over every prime field in the stated range. This is a symbolic argument, not a finite search over group isomorphisms.

For equality of the class-size multisets, the proof in `RESULT.md` counts classes at each fixed diagonal and radical support by a torus stabilizer; the calculation is independent of the arrow directions. At \(p=5\), all-equal diagonal labels contribute \(4(1+3+3+4)=44\) classes; labels with exactly two equal coordinates contribute \(3\cdot4\cdot3\cdot2=72\); and distinct labels contribute \(4\cdot3\cdot2=24\). Thus the total is \(140\). The original `checker.py` is ancillary: it checks some commuting-pair totals against a subgraph formula, not complete conjugacy-class-size distributions or nonisomorphism.
