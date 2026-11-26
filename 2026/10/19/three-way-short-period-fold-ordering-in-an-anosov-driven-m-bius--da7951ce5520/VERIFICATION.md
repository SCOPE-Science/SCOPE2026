---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The determinants of A−I and A²−I give one and five fixed points, respectively; substitution of the listed fifth-denominator coordinates exhausts the two primitive base two-cycles. Writing the circle fiber as a rotation composed with (z+ε)/(1+εz), the product's normalized half-trace is [cos(2π(c+μ q_j sin α))+ε² cos(2πμ s_j cos α)]/(1−ε²). Thus the positive-trace component about zero drift is |c+μ q_j sin α|<h_j; the one-step analog uses h_0. The lower bound (2/5)cos(π/10)/π>1/10 puts zero strictly inside all three intervals. At the positive endpoint the trace crosses transversely, with derivative proportional to −sin(2πh_j) for the two-step returns; their off-diagonal term contains cos(πd_+)≠0 in the stated strip, and the one-step off-diagonal is always nonzero. These are genuine nonidentity parabolics, not identity resonances. The bound on h_j′ makes c_2−c_1 strictly increasing across the open strip, with opposite signs at −π/2 and zero. The difference c_1−c_0 is negative on the nonpositive half and strictly increases on the positive half, where its sign changes. The possible c_2=c_0 tie is not an envelope switch: on the positive half c_1<c_2. The uniform expansion h_j=h_0−ε π μ²s_j² cos²α/(2√(1−ε²))+O(μ⁴) gives roots of order μ. Using (s_1²−s_2²)/(q_1−q_2)=1/2 and s_1²/(1−q_1)=1+q_1 yields the stated coefficients and cubic remainders. Independent replay: python3 /workspace/independent_checks_oct19.py (moebius_check), using scalar Möbius composition at parabolic double roots and bisection for four amplitudes; at μ=0.1 it gave approximately −0.03370194797518 and 0.08814153511562. This is corroboration; the analytic bounds supply the full quantifiers. The supplied checker was inspected, not executed.

## originality

PASS

Credit the original model, periodic-driver saddle-node mechanism and numerical fold curves, plus the previously worked zero-slice resonances. The defensible distinct claim is the exact first-positive-fold formulas used to resolve the lower envelope of the three short base orbits throughout the variable-phase/amplitude strip, including both switches' uniqueness and weak-forcing constants. None of the compared results gives or mechanically implies that classification.

## value

PASS

The plotted fold mechanism motivates asking which low-period itinerary destabilizes first. The minimal three-competitor comparison gives a rigorous phase diagram and leading sensitivities, resolving a competition that a trace computation for one orbit alone would miss. This supplies a usable short-period benchmark without claiming the true all-period or global collision envelope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
