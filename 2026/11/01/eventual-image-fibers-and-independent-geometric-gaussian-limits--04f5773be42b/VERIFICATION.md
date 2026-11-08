---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

The increments f(i+1)-f(i) in {0,1} make displacement f(i)-i weakly decreasing with endpoint signs, giving a nonempty fixed integer interval. Iteration traps every point at its nearest fixed endpoint within n steps. Fixing [a,b] forces boundary zero increments and inside ones; exactly max(0,a-2)+max(0,n-b-1) exterior increments are freely binary, and each additional one increases initial image rank by one. Summing locations gives J_n and stable-rank counts; conditional binomial CLT with tight geometric stable-rank tails proves the independent triple limit. Independent enumeration of all such maps and f^n for n<=9 matched exact binomial fiber and normalization. Boundary n=1 and n=2 checked.

## originality

PASS

Known directed-path monoid, initial-image rank, monoid size and idempotent count are credited to Fernandes–Paulista and Fernandes. The finer eventual-power fibers jointly refined by initial rank and their independent geometric/uniform/Gaussian limit were not found in the inspected full primary works; an unindexed iterate-statistics specialization remains possible.

## value

PASS

The eventual idempotent fiber and its joint initial-rank/stable-rank/location statistics are natural invariants of a known transformation monoid; the exact binomial classification and three-scale independent probability law add nontrivial information to aggregate cardinality and rank formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
