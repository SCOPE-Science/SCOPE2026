---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

A fresh exact reconstruction of the asymmetric distance on all \(64\) binary words independently enumerated the maximum cliques and reproduced maximum size \(12\) with exactly 30 maxima. Independently generating all 15 perfect matchings and the two transversal-cube bipartition classes gives exactly 30 valid codes, and the generated set equals the exhaustive maximum-clique set. Exhausting all 720 coordinate permutations gives one orbit of size 30 and stabilizer 24.

## originality

PASS

Grassl--Shor--Smith--Smolin--Zeng give exactly the audited representative and state that it is an optimal length-six 1-code, but their inspected full text does not state a converse classification of every optimum. Fresh semantic search did not locate the count 30, one-orbit theorem, or perfect-matching/transversal characterization. The older Weber--de Vroedt--Boekee short-code paper remains a residual risk because its full text was not materially inspected this round.

## value

PASS

The scalar optimum and one example were known, but classifying every optimizer and exposing the perfect-matching/transversal mechanism is a natural complete finite extremal result. It explains uniqueness up to coordinate permutation rather than merely recomputing size 12.

The dated certificate retains the supplied scientific assessment, sources and limitations.
