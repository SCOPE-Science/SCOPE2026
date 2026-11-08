---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Equality of |P|,|Q| on each full circle yields the rational Schwarz reflection identity for F=P/Q after gcd reduction. Two reflections generate an infinite-order Möbius map except rational transverse angle, and nonconstant rational maps cannot be invariant under infinite-order maps. For angle p pi/q the cross-ratio w maps the circles to lines and rotation fixes exactly C(w^q). Rational-map composition multiplies degrees, forcing q divisibility. Conjugate numerator/denominator zeros prove the real-unimodular U/U-sharp normal form; explicit degree-q pair is coprime. Trigonometric polynomial degree <=d in circle parameter forces equality from any 2d+1 samples. Independently checked constructive pairs for q=2..9 on both image lines numerically; numerical tests not the all-degree proof.

## originality

PASS

Chalendar–Partington 2024 already gives irrational/nontransverse two-circle rigidity, rational-angle counterexamples, and a local Taylor-order divisibility restriction. The assessed claim is strictly the global rational-invariant field normal form, q times full reduced map degree, and sharp fixed-degree polynomial threshold. The primary Theorem 2.16 and proof of Theorem 2.1 inspected do not state this complete quotient-degree classification. A differently worded invariant-theory corollary may have appeared elsewhere.

## value

PASS

Polynomial degree is the natural complexity parameter for deterministic complex polynomial phase retrieval. Knowing exactly all rational-angle ambiguities and sharp degree threshold lets one decide uniform recoverability for arbitrary sample placements, stronger than qualitative existence of counterexamples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
