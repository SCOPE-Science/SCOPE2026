---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For a unit v mod odd u, twice the uniquely possible coefficient y in [0,u) is congruent to r−1 mod u, with r the least positive inverse. The even-r candidate exceeds the bound from vy≤(u−1)(v−1)/2. For odd r, vr=1+ut with 0≤t≤v−1 makes the corresponding x nonnegative, including v=1. Reducing to each modulus a^k is therefore legitimate for every positive representative. The free reflection b→−b switches inverse parity at level a while fixing all even powers, so it pairs the two base values within each entire vector fiber, including empty fibers. After inversion modulo a², r+at maps under squaring to r²+2rat, and 2r is a unit even for composite a; each residue r² mod a has all a lifts in that fixed fiber. Summing alternating lift parities gives Q(a), and reflection halves both marginals. From 0≤S≤phi the two marginals are positive and the cell bias is at most 1/(4a); a root of −1 pairs opposite square parities. Each nonempty class gives an infinite progression, and counting complete periods gives relative density. The frozen verify.py and verify-output.txt were inspected, not executed; they record finite direct tests, 30 square moduli and selected higher-power vectors. No finite replay is needed for the universal proof.

## originality

PASS

Credit the known inverse-parity rule, not a new pointwise solvability criterion. The supported distinction is the full even-power conditional law together with the explicit square marginal and its four-cell consequences for all odd moduli. The closest full primary text and related indexed result do not supply this distribution. Unlike the frozen access note, the motivating manuscript's relevant full-text passages were available for this review.

## value

PASS

The squared-parameter problem gives a prior reason to ask whether the original bit has predictive power. The exact positive four-cell frequencies for each fixed odd first parameter rule out such a single-bit predictor on every full family, while the lift count quantifies the residual marginal bias. The simultaneous extension rules out predictive information about the base bit in any finite collection of even-power observations, without purporting to solve the general pointwise problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
