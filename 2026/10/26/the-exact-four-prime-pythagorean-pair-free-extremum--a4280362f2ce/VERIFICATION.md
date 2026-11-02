---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The 256 vertices 2^a3^b5^c7^d (0≤a,b,c,d<4) are distinct. Exact integer square-root testing exhausts all C(256,2)=32640 potential edges and yields exactly 408 forbidden Pythagorean pairs (unrestricted positive integer hypotenuse). An independent reimplementation using arbitrary-precision integer square roots checked the package CERTIFICATE.json blob 98ed409b09047a1950d23bc6cb581e93fb0d4c9b: it contains 144 distinct indices containing no forbidden edge and 112 true graph edges on 224 mutually different endpoints. This is a genuine finite exhaustive certificate: independent set yields f(4)≥144, disjoint-edge matching requires omitting at least one endpoint per pair, f(4)≤256−112=144. No numerical approximation, SAT proof assumption or non-exhaustive random search enters the equality. The prior verify.py checker was inspected as code, not executed opaquely.

## originality

PASS

Best-of-knowledge statement-and-implication comparison with primary literature, published results and a new Resultary search; foundational premises credited; no negative-search priority inference. The original exact equality is not implied merely by the definition of f(N) or a matching in another graph.

## value

PASS

The four-prime exponent box is the first natural four-dimensional small parameter of Xiao’s explicitly motivated extremal f(N). Its exact independence number 144 and matching witness give a sharp finite benchmark for asymptotic Pythagorean-pair avoidance. A finite fact can be independently useful even without a general f(N) formula: it resolves a genuine discrete optimization problem, with a short auditable upper certificate. The result does not claim general N or asymptotic density.

The dated certificate retains the supplied scientific assessment, sources and limitations.
