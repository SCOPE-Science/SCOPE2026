---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For t>0 the sinc-fourth-derivative identity is exact: F_t(z)=2(s(z)-t s^(4)(z)), s=sin(z)/z. At w=z² the meromorphic ratio R=s^(4)/s has simple poles a_n=n²π² and positive residues c_n=8-48/a_n, obtained from the Mittag-Leffler cotangent expansion; R(w)=1+Σc_n/(w-a_n). Its imaginary part has strict sign opposite Im(w), excluding off-axis zeros; R is strictly decreasing on every real pole gap and the sinc-pole locations are not F_t zeros. R(0)=1/5 and R(-∞)=1 yield exactly the t=1 and t=5 transitions, root counts and locations. The expansion F_5(z)=(8/21)z²+O(z⁴) gives double origin and z²=(21/20)(t-5)+...; hyperbolic asymptotic yields y_t~4/(t-1). Independent exact SymPy reconstruction verified the fourth derivative, R(0) and critical Taylor coefficient; the full continuum proof relies on positive residues, not numerical tests.

## originality

PASS

No prior work inspected supplies the exact all-parameter quartic-taper complex-zero classification with its critical t=1 and t=5 transitions. Baricz–Kokologiannaki–Pogány study zeros of pure Bessel derivatives under order restrictions, rather than the pencil s-t s^(4). Published Resultary Fourier-zero hits concern finite cyclic supports. The inaccessible complete Ki–Kim 2000 comparison is retained explicitly as priority risk. This is best-of-knowledge, not priority certification.

## value

PASS

This is a complete infinite zero classification for the first genuinely quartic even polynomial taper beyond the quadratic/Dini case. The strict positive residues establish axial rigidity despite changing-sign density, exactly locate the zero-total-mass double collision and imaginary-to-real transition, and yield a parametric square-root law. The exact result is natural for Fourier-window spectral zeros and does not claim arbitrary tapers or larger even powers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
