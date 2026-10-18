---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Independently expanded Lie derivative of P=z−ax: Ṗ=y²−a, so for a<0 every bounded segment has length at most 2R sqrt(1+a²)/(−a). For a=0, ż=y² yields ∫y²≤2R on a segment and ẋ=1+yz together with Cauchy–Schwarz yields T≤4R+2R³. For a>0, computed exact Lie derivative of G=(a+a^−1)x−(1−a^−2)z: Ġ=a+a^−1−(x²+y²+z²)+x²+(z+y/a)²; on R<sqrt(a+a^−1) this is strictly positive with bounded G, proving the stated uniform residence bound. Solving F=0 gives only (0,±sqrt(a),∓a^−1/2) at exact threshold, yielding arbitrarily long constant segments for any enclosing closed ball. The same identities integrated over compactly supported invariant measure give E(y²)=a, E(yz)=−1, E(r²)=a+a^−1+E[x²+(z+y/a)²]. Equality forces support on x=0,z=−y/a, and invariance imposes ẋ=1−y²/a=0, leaving exactly convex mixtures of equilibria. Independently verified both Lie polynomials symbolically with SymPy; no global completeness or chaos is inferred.

## originality

PASS

The 2014 introducing paper has precisely ẋ=1+yz,ẏ=−xz,ż=y²+ayz and the two positive-parameter equilibria; hence equilibrium positions and sufficiency R≥threshold are plainly prior. The 2015 follow-up analyzes time-reversal and attractor/repellor numerics, not a stated global uniform finite-ball residence estimate in the same-system sections inspected. The 2017 paper modifies the field by multiplying all components by a function that introduces a plane of equilibria; its modified conclusions are not equivalent to the original system confinement. The principal new ingredient is a tailored optimized monotone affine observable yielding sharp *negative* exclusion below the equilibrium radius plus stationary sum of squares. Other Sprott B/N records indexed in Resultary use inequivalent vector fields; no inference from them to this exact case B. General Lyapunov principle is known, but optimized system certificate is not contained in the original equilibrium result.

## value

PASS

Provides a complete, sharp radius threshold for arbitrarily long residence across all real parameters of a concrete reversible quadratic model used for numerical chaos; crucially finite residence below the equilibrium radius is stronger than merely exhibiting equilibria above it. Explicit passage time bounds and invariant probability moment equality/minimizer classification impose useful analytic limits on interpreting reported attractors, especially singular a→0. This is a meaningful natural exact classification, not merely restating equilibrium existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
