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
# Verification

The included `verify.py` constructs \(H_{m,n,t}\) as an explicit adjacency list. For every vertex it checks (i) properness against all incident edges, and (ii) that each distinct color appearing in the open neighborhood occurs a positive **odd** number of times. The resulting test is independent of the symbolic odd-block characterization.

Unlabeled color partitions are generated once each using restricted-growth strings. In the 16 parameter triples where \(2\le m\le4\), \(m\le n\le5\), \(1\le t<m\), and \(m+n\le9\), the checker examines exactly 87,448 such set partitions and matches the complete expected class-count polynomial, not just its smallest-degree term. For selected cases the checker brute-forces all labeled palette assignments at four palette sizes and matches the falling-factorial formula.

The checker independently constructs explicit minimum colorings for 13,795 parameter triples with \(2\le m\le31\), \(m\le n\le50\), and \(1\le t<m\), verifying both the graph predicate and the claimed minimum number of colors. It also verifies the even-crown two-color construction and its restored-edge formula through \(n=50\).

Recorded definition-level output:

```text
VERIFY_OK
m=2, n=2, t=1: chi_so=3, min_partitions=1, profile={3: 1, 4: 1}
m=2, n=3, t=1: chi_so=4, min_partitions=1, profile={4: 1, 5: 1}
m=2, n=4, t=1: chi_so=3, min_partitions=1, profile={3: 1, 4: 1, 5: 1, 6: 1}
m=2, n=5, t=1: chi_so=4, min_partitions=4, profile={4: 4, 5: 4, 6: 1, 7: 1}
m=3, n=3, t=1: chi_so=5, min_partitions=1, profile={5: 1, 6: 1}
m=3, n=3, t=2: chi_so=4, min_partitions=1, profile={4: 1, 5: 2, 6: 1}
m=3, n=4, t=1: chi_so=4, min_partitions=1, profile={4: 1, 5: 1, 6: 1, 7: 1}
m=3, n=4, t=2: chi_so=5, min_partitions=1, profile={5: 1, 6: 2, 7: 1}
m=3, n=5, t=1: chi_so=5, min_partitions=4, profile={5: 4, 6: 4, 7: 1, 8: 1}
m=3, n=5, t=2: chi_so=4, min_partitions=1, profile={4: 1, 5: 2, 6: 2, 7: 2, 8: 1}
m=4, n=4, t=1: chi_so=3, min_partitions=1, profile={3: 1, 4: 1, 5: 2, 6: 2, 7: 1, 8: 1}
m=4, n=4, t=2: chi_so=6, min_partitions=1, profile={6: 1, 7: 2, 8: 1}
m=4, n=4, t=3: chi_so=5, min_partitions=1, profile={5: 1, 6: 3, 7: 3, 8: 1}
m=4, n=5, t=1: chi_so=4, min_partitions=4, profile={4: 4, 5: 4, 6: 5, 7: 5, 8: 1, 9: 1}
m=4, n=5, t=2: chi_so=5, min_partitions=1, profile={5: 1, 6: 2, 7: 2, 8: 2, 9: 1}
m=4, n=5, t=3: chi_so=6, min_partitions=1, profile={6: 1, 7: 3, 8: 3, 9: 1}
direct_unlabeled_cases = 16
unlabeled_partitions_examined = 87448
palette_bruteforce_cases = 16
explicit_constructions_checked = 13795
single_edge_jump_checked_even_n = 2..50
```

This finite verification does not assert that arbitrary parameters were exhaustively enumerated. The infinite theorem is proved by the color-class argument in `RESULT.md`. Run `python verify.py` using Python 3 from the directory containing the packaged files.
