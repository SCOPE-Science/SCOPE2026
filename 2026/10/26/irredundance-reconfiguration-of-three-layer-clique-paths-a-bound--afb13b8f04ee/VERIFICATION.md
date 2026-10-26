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

# Executed checks and limits

The self-contained script `verify.py` was executed using standard Python 3. It computes closed neighborhoods of \(K_n\square P_3\) directly, tests every subset against the original unique-private-witness predicate, compares the four structural cases and the all-set polynomial, tests inclusion-maximality by vertex additions, and independently derives slide edges and connected-component diameters of the maximum-set reconfiguration graph.

Exhaustive results:

| \(n\) | Examined subsets | Maximal sets | Maximum sets | Reconfiguration edges | Isolated vertices | Nontrivial component diameter |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 4 | 4096 | 113 | 49 | 104 | 16 | 4 |
| 5 | 32768 | 208 | 83 | 210 | 32 | 4 |
| 6 | 262144 | 353 | 137 | 372 | 64 | 4 |
| 7 | 2097152 | 570 | 227 | 602 | 128 | 4 |

All 2,396,160 subset comparisons and every enumerated maximum-set slide edge agreed exactly with the proved classification. Computations were finite; the infinite-domain assertions are supported by the combinatorial proof in `RESULT.md`. No independent audit or external formal certification has been performed.

To reproduce, place this file next to `verify.py` and run `python verify.py` with standard Python 3. The verifier has no third-party dependencies.
