---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Starting from the published endpoint formulas \(x=(v-u)/(uv)\) and \(y=(v-u)/((L-u)(L-v))\), midpoint and half-length variables give \(m^2=r^2+2r/x\) and \((L-m)^2=r^2+2r/y\). For arbitrary positive \(x,y\), the sum of the two positive square roots is continuous and strictly increasing from zero to infinity as \(r>0\) varies, so there is exactly one root equal to the chord length. Each square root exceeds \(r\), which forces \(0<u<v<L\), proving existence as well as uniqueness. Direct differentiation gives the stated determinant, whose remaining numerator factor equals \(u(L-v)+v(L-u)>0\), so the determinant is everywhere negative. Analytic bijectivity plus the local inverse theorem yields the global analytic inverse.

## originality

PASS

Lukács's Lemma 2.2 is very close prior art: it derives the same rational endpoint data and proves that data arising from an existing segment determine that segment, even writing explicit algebraic candidate coordinates. But the proof assumes realizable data and does not establish that every positive pair lies in the image, nor state the full positive-quadrant range, a global diffeomorphism theorem, or the Jacobian factorization. The submitted scalar inversion supplies the missing existence/domain argument for arbitrary positive data. Targeted Resultary searches found no stronger published range theorem.

## value

PASS

This is a natural complete classification of the feasible first-order data for the simplest one-segment masking inverse problem. It upgrades prior uniqueness-on-the-image to exact existence and uniqueness for all positive data, gives a constructive one-dimensional inverse, and supplies the Jacobian needed for sensitivity analysis. Natural complete range classifications are substantive even when the final proof is elementary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
