---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For circle Haar probability, the integral is the squared coefficient norm of (a+bz+cz²)³. Among its seven coefficients, only 3a(ac+b²), b(6ac+b²), and 3c(ac+b²) carry interference, and their squared moduli give a single cosine of δ=2arg b−arg a−arg c with coefficient 6AB²C(3A²+2B²+3C²). When ABC>0, both phases are achievable and the minimum integral is positive (also at least (A²+B²+C²)³ by Jensen). If any magnitude vanishes all phases tie. Divide the extrema by (AC)³ and set S=(A²+C²)/(AC)≥2 and T=B²/(AC)>0. The denominator H simplifies to S³+9TS²+(6−18T+9T²)S+18T−12T²+T³. The derivative numerator for 12T(3S+2T)/H in S is −36T[2S³+12ST²+5T³+T(11S²−14)], strictly negative. At S=2 the denominator is (T+2)(T²+4T+10); differentiation gives −24 times T⁴+6T³−40T−60 divided by its square. Descartes' rule and the opposite signs at zero and large positive T give exactly one positive root, with the derivative strictly changing from positive to negative. The maximum is attained exactly at A=C>0 and T=t_*, with δ=0,π respectively for the two extrema. A nontrivial integer rescaling preserves Haar by the power map; translating the spectrum only multiplies by a unit modulus monomial. Taking the sixth root gives the norm contrast, not the sixth moment contrast.

## originality

PASS

The strongest same-support results give a maximum divided by coefficient energy or a phase response restricted to unit magnitudes. Neither determines the maximal distortion relative to the minimum at the same unknown magnitudes. The known cubic-convolution mechanism is not the distinct claim; the contribution is the exact global ratio, its balancing and unique amplitude optimum. Arestov's 1980 article could not be compared in full; no absence is inferred from that access gap.

## value

PASS

This is the exact largest phase distortion of the sixth norm for the shortest analytic progression with a genuine relative-phase interaction at this exponent. It measures a different property from the well-studied maximum norm per coefficient energy and identifies a different optimizing amplitude. The optimizer and constant give a concrete reference for coefficient-multiplier distortion on small spectra rather than a new claim about general majorant theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
