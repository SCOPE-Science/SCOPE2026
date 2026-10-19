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

# Reproducibility and verification

Run `python3 verify.py` in the same directory as this document. The executable requires only the Python 3 standard library and prints `PASS` if all finite checks succeed.

The test checks exact rational bounds for the forcing, the two-step inward margin \(53/25\), the universal two-step increment bound \(54/5\), the attracting fixed-point Lipschitz constant \(27/40\), and the Jacobian row-sum bound \(469/512\). It independently computes the numerical unique fixed point, checks a collection of states in the guaranteed attraction square, verifies strict supercritical growth on sampled exterior orbits, and tests convergence of the normalized escape amplitude. It also runs finite endpoint-orbit diagnostics for several positive slopes.

Expected numerical fixed-point location at \(\alpha=1/4\): approximately \((-0.627008595473,0.251094384424)\). This numerical approximation is illustrative; the existence, uniqueness and stability proof uses only inequalities independent of this approximation.

All universal conclusions, infinite iteration limits and existence statements are proved in `RESULT.md`. Computations sample finitely many states and cannot prove those statements by enumeration. The critical inward-sign lemma is proved analytically using \(\tanh\) monotonicity and strict diagonal dominance. Independent validation is not represented by these checks.
