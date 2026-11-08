---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Write S=P/2=a+b, t=ab, theta=asin(A/t), with exact feasible interval A<=t<=S²/4. The support-width formula W(phi)=a|cos phi|+b|cos(phi-theta)| yields E W²=S²/2+t(2g(theta)-1), g=[sin theta+(pi/2-theta)cos theta]/pi. Its derivative H(theta)=2/pi[sin theta+(pi/2-theta)/cos theta]-1 is positive and increases with theta; because theta decreases in t, F(t) is strictly increasing and concave. Endpoint derivatives H(pi/2)=4/pi-1 and H(asin(4A/S²)) are sharp. Rectangle (t=A) and rhombus (t=S²/4) exhaust extrema; a=b and theta=pi/2 uniquely for delta=1. Independent numeric recomputation confirmed monotonicity, concavity, and derivative endpoint inequalities for three shape families. Read verify.py from exact blob: seeded quadrature/bisection spot checks only, not an infinite proof.

## originality

PASS

Best-of-knowledge original for replacing maximum width with area as third scalar and for exact sharp fixed-area slope: the closest published record supplies the same projection moment formula but its inverse uses maximum width, a distinct measurement. No inspected distribution or chord-power result entails fixed-area monotonicity. Historical priority may differ if older special geometry formulas are unindexed.

## value

PASS

Recovering any parallelogram from readily motivated perimeter, area and second width moment is a natural finite-scalar tomography problem, with complete inverse and best possible conditioning for the side-product plus sharp rectangle/rhombus variance envelope. This is more than a named reparametrization or a known table computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
