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

Progressive strict-majority activation has a unique final closure: the union of all resistant sets disjoint from the seeds stays inactive, where each vertex of such a set has at least ceil(deg(v)/2) neighbors in it; conversely the final inactive set itself satisfies that criterion. An independent exact replay (house in /workspace/audit_evidence/replay.py) tests every labeled edge set on 2–5 vertices for connectivity via cuts, selects the top two only if unique, and obtains final sizes by exhausting resistant subsets rather than either of the frozen closure algorithms. For orders 2,3,4,5 the connected counts are 1,4,38,728 and the eligible counts 1,0,18,290. The only five-vertex eligible spread pairs (heuristic,optimum) are (5,5):230 and (3,5):60. The failure set equals the entire orbit under permutation of {01,03,04,12,14,23}, with orbit size 60 and stabilizer size 2. Its top-degree seed pair {0,1} activates 4 only; the four full-activation pairs are {0,2}, {1,3}, {2,4}, {3,4}. The incidence fractions follow. The order-statistic test d₂>d₃ is for n≥3; at n=2 the only pair qualifies, and n<2 has no eligible pair. The frozen checker compares both closures after its eligibility filter, not on every connected graph as the verification prose suggests; this does not affect the eligible census.

## originality

PASS

The supported distinct claim is the least graph order, unique obstruction class, and exact labeled census for fixed-budget strict-majority degree-pair seeding with no tie at the cutoff. High-degree seeding, strict-majority dynamics, and the existence of failures of degree heuristics in other models are known. The closest indexed census contains the same house orbit but classifies a different predicate.

## value

PASS

Two seeds are the first budget that can initially satisfy a degree-two vertex's strict majority. Minimizing graph order and removing degree cutoff ties give a clear benchmark for failure intrinsic to the degree rule rather than its tie policy. The unique first-layer graph and exact counts sharpen a single counterexample; its 3-versus-5 outcome is a reproducible test case. No claim is made about incidence at larger orders or under other threshold rules.

The dated certificate retains the supplied scientific assessment, sources and limitations.
