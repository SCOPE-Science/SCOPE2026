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

# Reproducibility and limits

The complete self-contained Python standard-library script `check.py` constructs the exact one-step success probability from two independent habitat-failure events and exhaustively computes all \((n+1)^2\) assignments for each founder budget \(1\leq n\leq12\). It uses exact rational arithmetic for four individual survival probabilities and four habitat-suitability probabilities (16 combinations) and tests the claimed candidate set, the exact advantage formula, and the even-budget factorization. The script verifies explicit below/above-threshold examples at \(n=2\) and \(r=1/2\). Executing `python3 check.py` prints `VERIFY_OK exact_profiles= 13088 population_sizes=1..12 parameter_pairs=16 special_transition=1`.

The unrestricted mathematical result follows from the explicit proof in `RESULT.md`: convex sex-balancing, a strict geometric-mean inequality, a concave polynomial of the exponential allocation sum, and exact threshold algebra. The finite census is not an infinite-family proof or independent external certificate. No benchmark against field reintroduction observations has been carried out. The model concerns one-step retained mating-pair viability only. Literature overlap uncertainty is documented in `REVIEW.md` and `AUDIT.json`.
