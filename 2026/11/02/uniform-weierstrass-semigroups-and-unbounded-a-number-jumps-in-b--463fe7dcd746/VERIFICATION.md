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

# Verification and reproducibility

The theoretical proof uses characteristic-two substitutions, pole-valuation strict inequalities, the numerical-semigroup Apéry genus formula, and the established one-point Cartier-kernel formula. The key steps, including dependence on \(M/2<D<M\), are written in `RESULT.md`.

Run `python verify_semigroups.py` to check the semigroup and finite arithmetic counts by a second integer enumeration path. The checker is purely standard-library Python. It tests odd \(5\le M\le105\) with all admissible odd \(D\) and the jump ray through \(s=80\). A successful run emits `VERIFY_OK`. This does not establish the infinite family by itself; the displayed proof does.

The provenance of the genus and Cartier formulas is given in [1], Propositions 10.1 and Lemma 2.1. The genus-six case \((M,D)=(5,3)\) is existing literature, and the parameter-uniform claim is the contribution under review. No independent audit has been performed.
