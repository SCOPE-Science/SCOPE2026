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

# Reproducible checks

Use Python 3 to execute `python3 check_rank2_successors.py` from a directory containing the provided source. The program requires no external dependencies. It exhaustively examines all \(n!\) choices of the second uniform ordering relative to a fixed first ordering for sizes \(5\) through \(9\), checks first and cross factorial-moment quantities, and verifies predicted realized row-mask signatures for clean samples with sufficient unused vertices. It additionally draws uniform orders for \(r=2,3,4\) on \(n=150\) vertices and checks the same signature-support prediction when cleanliness holds. Reproduction returned the final marker `RANK2_SUCCESSOR_PROFILES_OK`.

The mathematical proof is independent of the finite computations. In particular, finite enumeration cannot establish convergence in distribution, and a sampled clean-event frequency does not prove a high-probability statement. The critical symbolic checks are the exact probability \((n-s)!/n!\) for compatible directed-arc constraints; the strict vertex-versus-arc excess for every overlapping motif cluster; and the two-round back-and-forth equivalence through realized local mask signatures. The proof excludes quantifier ranks greater than two, extra predicates, and a growing number of independent orders. No independent external audit has been performed.
