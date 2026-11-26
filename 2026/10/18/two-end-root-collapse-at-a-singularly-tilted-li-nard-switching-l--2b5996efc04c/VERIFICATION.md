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

Polar-coordinate first variation gives the stated angular integrand. Odd terms cancel under the half turn; the even forcing integral is twice the integral of a cosine-power primitive over the positive switching semicircle, giving 4 sin^(2j+1)(φ)/(2j+1) before period normalization. The disjoint even and odd monomials give the Descartes bound at fixed tilt. Prescribing p+q+1 distinct positive zeros gives a nonzero coefficient vector; the same bound rules out missing monomials, multiple zeros, or extra positive zeros. For fixed coefficients, simple finite roots persist by the implicit function theorem. A sequence of small roots forces r/s→−B0/A0, and r=su gives a simple limiting equation. A sequence of escaping roots must have sr→∞; comparing the two leading terms rules out q≤p and equal signs, and otherwise forces s^γr→(−A_p/B_q)^(1/d), d=2(q−p)−1, γ=(2q+1)/d. On this scale both lower-degree remainders converge to zero in C¹ near the candidate, ensuring exactly one simple root. Compactness in the extended radius line rules out any others. On a fixed crossing annulus at a fixed positive tilt, composing the two smooth crossing flow segments gives the C¹ first variation of the return map and hence a hyperbolic cycle at each simple zero.

## originality

PASS

The supported distinct claim is the exhaustive fixed-coefficient collapse and escape law at a straight-line tilt, with exact leading scales and sign criteria. The vertical cancellation, horizontal-switch optimized count, and standard simple-zero cycle-persistence mechanism are not claimed as new.

## value

PASS

The optimized count at each fixed angle does not say what happens under a small physical tilt without retuning coefficients. The classification answers that question, gives precise radius scales for branches entirely missed by compact-annulus convergence, and identifies which averaged crossings can persist without claiming more uniform cycle existence than proved.

The dated certificate retains the supplied scientific assessment, sources and limitations.
