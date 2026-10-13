---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
The theorem concerns every integer \(n\ge2\), \(1\le c<n\), and all connected two-row binary incidence networks with \(n+c\) links and no isolated species. Its proof uses exact column types, the global Barber community-partition objective, and an integer quadratic comparison; finite tests do not establish the unbounded quantifiers on their own.

The embedded standalone `verify_nested_modularity_pareto.py` uses only Python 3 standard-library modules `fractions`, `itertools`, and `math`.

To verify independently, run `python3 verify_nested_modularity_pareto.py`. The first output line must be `VERIFY_OK`.

The script enumerates all allowed matrices with \(2\le n\le8\), including 9,322 labeled cases, and for each recomputes NODF directly from pairwise row/column overlaps. The global Barber optimum is checked against explicit community assignments of the columns and, for \(n\le5\), against **all unrestricted vertex set partitions**, independently of the proof's modularity simplification. The latter enumeration evaluates 198,158 network/partition combinations, while the two-row-label checker evaluates 1,927,648 assignments. All arithmetic is exact `Fraction` arithmetic.

The script additionally compares every attainable score pair in each small dimension for Pareto dominance and tests the sharp joint-maximizer threshold and concrete low-connectance example. The global theorem is proved in `RESULT.md`, not inferred from these bounded tests.
