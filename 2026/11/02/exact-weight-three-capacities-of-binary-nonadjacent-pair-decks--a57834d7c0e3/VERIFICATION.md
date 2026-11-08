---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

The nonadjacent two-deck has G11=k (#one-runs) because adjacent pairs among three ones equal 3−k. For z=n−3 zeros and ℓ zero-runs, G00=C(z,2)−(z−ℓ), and G10 is determined by total C(n−1,2), G00, G11 and J=G01. Thus (k,ℓ,J) completely specifies the profile. The eight admissible run-count pairs have exact integer intervals or progressions in J; key (2,2) row is full [0,3z−3] for even z but excludes specified even interior values when z odd; other run rows have interval-filling arguments by positive zero-run compositions. Summing distinct (k,ℓ,J) gives the parity piecewise expression for n>=8; lower n counted directly. Fresh literal G_ab exhaustive check for all C(n,3) words n=3..18 agrees with all counts. Symbolic run arguments, not finite checker, establish all n.

## originality

PASS

Golm et al establish gapped k-deck collision thresholds; Rigo–Stipulanti–Whiteland Lemma 2.1 gives an abstract equivalence test and studies infinite-word factor-language complexity; neither computes a fixed-composition three-one image and parity-dependent capacity. Ordinary ungapped k-deck counts concern a different observation channel.

## value

PASS

The complete natural fixed-weight-three gapped observation profile classification gives sharp zero-error capacity, explains parity, and quantifies loss from Θ(n³) possible words to Θ(n) distinguishable deck outputs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
