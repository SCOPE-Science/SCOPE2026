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

Both programs use Python 3 standard-library modules only. Run `python verify_kneser.py` and `python verify_generalized_petersen.py` from the extracted package. They must terminate with `KNESER_EXACT_RECONFIGURATION_PASS` and `GENERALIZED_PETERSEN_DIRECT_PASS`, respectively. These markers were actually obtained by running the programs.

The first enumerates all \(4944\) candidate subsets of sizes \(0\) through \(5\), all \(120\) natural permutations, all \(30{,}135\) pairs of minimum codes, and BFS distances from each of the \(246\) codes. The second independently constructs Petersen as \(GP(5,2)\), tests the same finite candidate universe with set-based neighbourhoods, checks a literal isomorphism with \(KG(5,2)\), and independently computes all pair distances and ten obstruction components. Neither test relies on random sampling, a timeout, or a numerical extrapolation.

The mathematical assertions are finite and fully specified, but an independent scholarly audit has not been performed. Absence of a covering historical publication has not been proved.
