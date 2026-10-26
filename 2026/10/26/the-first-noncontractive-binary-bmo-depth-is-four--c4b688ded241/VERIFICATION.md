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

# Reproduction

Place `VERIFY.py` and `DUAL_CERTIFICATES.json` together and run `python3 VERIFY.py DUAL_CERTIFICATES.json` (Python 3, standard library only). The checker reconstructs each of the 1540 orbit representatives and the 63-row integer linear system, checks positive rational dual multipliers, unrestricted leaf-variable stationarity, nonnegative auxiliary-variable reduced gradients, and the bound `dual_objective <= 64` for all instances. A completed local execution returned `PASS: 1540 orbit-complete cases; all exact dual equalities and bounds; largest scaled upper bound 64.`

The mathematical proof of exhaustiveness is the recursive count `4 -> 10 -> 55 -> 1540` of unordered rooted binary trees with four leaf colors. Every simultaneous pair of leaf-sign patterns belongs to one such orbit under swaps of equal-size siblings. Each dual inequality bounds every real leaf vector compatible with that pair, not only vectors sampled during computation. The input seminorm normalization, representation of absolute deviations, root objective, and descendant cases are explicit in `RESULT.md`.

The cited depth-four example, independently averaged with rational arithmetic, gives input BMO `5`, output BMO `41/8`, and quotient `41/40`. This serves as an external comparison, not as a new sharp depth-four result.

No infinite-depth computation, independent external audit, or proof of priority is claimed. The rational certificate and code are research artifacts for direct checking.
