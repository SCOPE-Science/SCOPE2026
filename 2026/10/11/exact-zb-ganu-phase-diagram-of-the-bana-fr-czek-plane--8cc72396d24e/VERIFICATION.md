---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Original RESULT correctly splits N(p)N(q) into EE,FF,EF,FE products. EE<=D by Euclidean parallelogram; FF<=D since F(x)^2+F(y)^2<=D. For mixed EF, optimize the quadratic minorant N(z)^2 >= Aθ z1²+θ z2², Aθ=λ²-(λ²-1)θ, to derive ratio <=λ/sqrt(Aθθ). Maximizing Aθθ on θ∈[0,1] yields λ for 1<λ<=sqrt2, then 2sqrt(1−λ^-2). Direct pairs attain each bound. Equality tracing gives a low-λ continuous orthogonal family, transition α=π/4, high-λ unique circle/strip transition orbit. λ→1 excluded and λ=sqrt2 checked in both formulas.

## originality

PASS

The full phase diagram includes a classification of Zbăganu maximizing pairs and a real-parameter transition at sqrt2, not just the piecewise value. Published Resultary Ptolemy computations on the identical space yield numerically identical branch values but concern a different supremum; known CP>=CZ cannot by itself prove equal CZ without an attaining CZ witness. The same paper on both parameters remains an explicit access risk, not declared NOT_COVERING.

## value

PASS

The norm is a canonical disk intersected with a strip, and the phase change explains when maximizers leave the Euclidean circle and meet the clipped boundary. Classifying all CZ equality configurations is a structural geometric fact independent of a coincident CP scalar profile; applicable in estimates for fixed-point and geometric constants. The exact full parameter locus is mathematically motivated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
