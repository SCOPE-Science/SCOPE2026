---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Reconstructed g=x⁴+2x²+2 and g(x)-g(y)=(x-y)(x+y)(x²+y²+2). On each 2-adic parity ball strict contraction implies a unique g fixed point; f swaps those roots. First g sends evens to 2 mod8 and odds to 5 mod32. In the corresponding congruence classes, the two non-difference factors' valuations add exactly three, giving a sharp gain of three bits per further two-step iteration. The initial event reduces to y² congruent to odd a² modulo 2^h, with 4 square roots for h>=3 and small-exponent boundaries h<=2; these yield the piecewise alpha,beta and ceiling cutoff formulas for all k. Exhaustive separately written iteration through k=12 matched both full parity depth distributions, including k=1. The cited pre-existing attracting-two-cycle theorem is not claimed as a new proof.

## originality

PASS

Fan–Liao 2010 Theorem 6.1(4) already proves existence and attraction to a single 2-cycle for x²+1 on Z2, so that is *covered* and excluded from novelty. Their inspected theorem and local proof do not state the exact all-k finite quotient parity-resolved first-hitting histograms or the precise cutoff depths. Anashin's ergodicity results concern measure-preserving compatible maps rather than this noninvertible attraction. The new assertion is a quantitative refinement, not renaming the known period-two attractor.

## value

PASS

The complete transient-depth profile of the noninvertible functional graph is a natural dynamic invariant; its even/odd asymmetry and exact three-bits-per-pair growth are genuinely structural and not determined by the qualitative global basin. It gives every finite quotient, not merely small enumerations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
