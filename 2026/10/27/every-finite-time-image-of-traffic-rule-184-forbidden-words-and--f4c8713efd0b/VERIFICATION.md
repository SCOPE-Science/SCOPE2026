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

The four-cell rule gives an output 11 iff the incoming 11 from the right is not met by a 00 from the left, and likewise for 00. Alternation between marked bonds imposes odd distances for like signs and even distances for opposite signs. The words in question are exactly neighboring +,− pairs separated by 2k+2 bonds. For an output +,− pair at distance d, its input ancestors are at distance d−2, and the intervening list, even if it includes annihilated particles, contains a neighboring +,− pair. Conversely shift the desired output marks back by one step: +,− distances shrink by two but remain positive; −,+ distances grow, and same-sign distances are unchanged. Parity reconstructs an input with the required gap bound and without a collision. The no-mark case is the exchange of the two alternating configurations. This proves the bilateral image equality by induction. No forbidden word contains another; the period 11(01)^t00 proves strict inclusion. Any finite avoiding word extends bilaterally by zeros to the left and ones to the right. No forbidden word can overlap another: proper suffixes of length ≥2 do not start with 11, and the one-symbol suffix is 0 rather than 1. Each rejected one-symbol extension therefore corresponds to exactly one forbidden suffix and an arbitrary avoiding prefix. This gives the recurrence and rational series. Its first positive pole is the unique z in (0,1/φ) with 1−z−z²=z^(t+2), and nonnegative coefficients identify that pole with the radius. The equation (λ−φ)(λ+φ^(−1))=λ^(−t) bounds λ−φ by φ^(−t)/√5, so (λ/φ)^t tends to 1, yielding the stated entropy constant after taking logarithms. The no-11 shift gives the lower bound at infinite time, with the finite-time entropies giving the matching upper bound. The t=0 case gives the full shift and λ=2. Inspected the finite checker and its recorded scope without executing it; the all-time argument, not bounded ring tests, proves the claim.

## originality

PASS

Bounded pass for the complete all-time spatial word series and sharp entropy relaxation, together with the verified finite-image presentation. Credit the established dynamics and explicit catalogue overlap on the all-time forbidden basis and strict descent; do not claim that the basis is absent elsewhere. Neither the inspected low-time exact results nor the overlapping all-time record states the all-time word series or sharp convergence law. Once the language is known these are derivable, but one must count all avoiding words using nonoverlap, factor the denominator, identify the dominant pole, and obtain the leading constant. The overlap does not establish historical priority.

## value

PASS

A full finite-time image classification for a standard elementary automaton distinguishes deterministic loss of spatial words from traffic statistics under a measure. The uniformly explicit language counts and leading entropy constant quantify a strictly descending chain whose entropy converges but whose images never stabilize. This is not just a finite catalogue of early-time automata.

The dated certificate retains the supplied scientific assessment, sources and limitations.
