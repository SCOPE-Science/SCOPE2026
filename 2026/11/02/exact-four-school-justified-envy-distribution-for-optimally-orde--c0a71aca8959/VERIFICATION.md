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

With four unit-capacity schools, four students and a uniformly random common strict preference, for a fixed student serial order rho each school s is assigned to each rank t with probability 1/4, hence conditional expected justified envy equals (1/4) sum_s KT(rho, pi_s). A fresh independent C++ program enumerated all 24^4=331776 ordered priority quadruples and each of the 24 serial orders, reproducing all 13 optimal-score counts and all 9 nonzero optimal-multiplicity counts; total sum of K=2488608 and unique optimum frequency=51192. Therefore E[min envy]=8641/4608; a uniformly random order yields 3 for every fixed priority profile. A score-constant adjacency swap proves K=12 iff each unordered student pair is split exactly two-versus-two, occurring 2376 times.

## originality

PASS

Hamdan already establishes the general Kemeny/expected-justified-envy equivalence, which is not claimed new. The exact finite four-priority score and optimizer multiplicity distributions, exact mean, and 2-2 split characterization are distinct data not established by inspected Kemeny distribution sources.

## value

PASS

The complete first small four-school risk spectrum is a natural finite invariant of optimal fairness under uncertain common preferences, including frequencies of unique ties and of zero improvement. Its joint distribution is not implied by the mechanism-to-Kemeny theorem and is useful for exact benchmarks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
