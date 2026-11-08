---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

At lattice time step 1/2 and frequency step 1, integer-modulation Parseval and Zak fiberization reduce the frame form to S(x,theta)=|Zg(x,theta)|²+|Zg(x+1/2,theta)|². For y in [0,1], the geometric Zak transform equals [e^(-ay)-pr e^(by)+r(e^(by)-e^(-ay))e^(i theta)]/[(1-p e^(-i theta))(1-r e^(i theta))], with nonnegative numerator coefficients. Thus S is increasing in cos theta, with min at pi and max at zero. The zero-phase profile is strictly convex with equal endpoints, so maximum occurs at 0 modulo half-lattice. For theta=pi the profile F(x)=Acal e^(-2ax)-2Bcal e^((b-a)x)+Ccal e^(2bx); F prime has sign governed by an upward quadratic in t=e^((a+b)x) with strictly negative constant and one positive root, and equal endpoint values force unique interior minimizer. Two shifted H(y)=u e^(-ay)-v e^(by) cannot vanish simultaneously, giving strictly positive minimum. Independent phase/spatial numerical scans and exact-fiber evaluations for (a,b)=(1,1),(.5,2),(2,.5),(.01,3),(3,10) confirmed formulas for both extremal bounds, positivity, minimizing fiber and reflection symmetry. Numerical checks only corroborate continuous proof.

## originality

PASS

Exact optimal squared frame bounds for all positive unequal left and right slopes at fixed half translation, plus unique biased spatial minimizing fiber. General totally-positive frame-set characterization and symmetric-exponential bounds exist, but do not directly yield these explicit asymmetric extrema. Janssen 1996 full text inaccessible; this high-relevance comparison is a material unclosed priority risk, not a demonstrated prior theorem.

## value

PASS

Sharp conditioning constants and the precise worst spatial fiber are natural frame-stability invariants for a two-rate signal window; these are independent of qualitative membership in the frame set and useful in rigorous sampling design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
