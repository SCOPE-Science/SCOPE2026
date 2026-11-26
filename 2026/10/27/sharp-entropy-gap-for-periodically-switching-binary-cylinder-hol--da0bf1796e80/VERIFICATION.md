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

Reconstructed the proof in RESULT.md, lines 34–60. XOR of the observed bits by the phase-dependent first forbidden bit turns each phase into L or F, with F exactly at a cyclic match. The matrices telescope by a genuine conjugacy over a period. At zero matches, prefixes are descending binary strings so there are n+2 words of length n+1 and exactly two recurrent two-sided points at phase zero, giving the asserted escape probability and zeta function. A product containing F has positive off-diagonals and a positive bottom-right entry: the property holds for L^a F and survives right multiplication by either factor. Its square is positive. In the strict comparison, F L^a F minus L^(a+1) F is the nonzero nonnegative matrix with first row (1,a) and second row zero; multiplying on either side by the invertible nonnegative factors keeps the difference nonnegative and nonzero. The comparison preserves length and primitivity, so strict Perron monotonicity applies, including for adjacent F factors. The trace and determinant of F L^(p−1) are p and −1, yielding the bound and equality for all p, including p=1. Choosing the first bits and the set of matches freely gives the schedule multiplicities. The monodromy counts labelled paths (including parallel edges) so traces count symbolic periodic points and the primitive Perron measure yields the dimension through cylinder decay. The canonical binary convention gives the stated Lebesgue normalization; the countable difference at ambiguous endpoints does not affect the dimension argument. The submitted checker was inspected, not executed and not used as an infinite proof. 'Sixteen original transition choices' in the verification paragraph is a typo: there are four individual matrices (sixteen period-two schedules).

## originality

PASS

The distinct supported finding is the sharp smallest positive entropy for all binary schedules and its exact equality characterization, together with the zero-entropy boundary. The transfer formalism and overlap parameter alone receive no novelty credit. The strongest matching indexed overlap classifications concern a different alphabet size or the two endpoint holes rather than the full four-hole optimization. No inspected prior statement supplies the sharp minimization; priority under an equivalent matrix-product formulation remains a limitation.

## value

PASS

For genuinely distinct moving holes of the same size, the theorem gives both an exact zero-growth mechanism and a sharp prohibited interval of escape rates. The equality condition gives a way to recognize the sparse slow-growth regime without multiplying a long list of matrices. This is an all-period structural result about dynamical escape, not merely a finite schedule census or use of a transfer matrix.

The dated certificate retains the supplied scientific assessment, sources and limitations.
