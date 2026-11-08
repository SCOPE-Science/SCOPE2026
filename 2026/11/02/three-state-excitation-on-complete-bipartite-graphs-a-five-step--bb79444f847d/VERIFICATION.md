---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Partition each shore by initial color and cap its multiplicities at 2; each initial color class remains synchronized at every future step, and the threshold-two neighbor predicate depends exclusively on the capped counts. Thus 23 attainable profiles per shore, 529 pairs, form an exact symbolic factor for every a,b>=2. The complete deterministic recurrence has period classes 476 fixed, 52 period-four, one period-three; maximum preperiod five. Independent reimplementation of the cap-update and signature recurrence obtains the same classes and the exact U,A,Q,H period-four coefficient matrix [[6,6,3,3],[6,6,3,3],[3,3,2,1],[3,3,1,0]]. Exact multinomial counts of each initial profile produce B3=H_aH_b and displayed B4 formula, and initial period-four states are only profiles (202,220),(220,202), producing U_a U_b/2 orbits. Every profile with 2 as a cap is realized by arbitrarily many vertices, so the 529-case exhaustion is a genuine all-shore-size proof, not extrapolation.

## originality

PASS

Exact period-stratified basin polynomials and sharp universal five-update cutoff for threshold-two bipartite GHM are not supplied by the broader graph excitation literature.

## value

PASS

The exact quotient yields a complete, all-parameter classification of attractor periods and labelled basin sizes for a natural dense bipartite network, with sharp minimum shore sizes and maximum transient; meaningful finite structural factor and dynamical census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
