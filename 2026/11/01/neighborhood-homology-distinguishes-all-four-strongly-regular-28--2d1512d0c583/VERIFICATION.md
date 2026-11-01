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

# Verification of the exact finite classification

Run `python3 verify.py` using Python 3.10 or higher and no third-party dependencies. The script builds \(T_8\) and each of the three explicitly switched graphs from the vertex pairs of \(K_8\), checking each strongly regular parameter identity on every pair. It constructs all faces of each Lovász open-neighborhood complex by two exhaustive enumeration algorithms and asserts equality. It computes all simplicial boundary ranks over \(\mathbb F_2\) by bitwise elimination, then verifies their reduced homology again using independent low-pivot rank elimination on much smaller complexes obtained by sequential elementary free-face collapses. It also checks full and collapsed Euler–Poincaré identities and class-distinguishing clique counts. No random sampling or external dataset is required.

The complete exact face vectors and boundary ranks are embedded in `verification_output.txt`. Verification succeeds exactly when the final line reads `VERIFY_FOUR_28_VERTEX_NEIGHBORHOOD_COMPLEXES_EXACT_MOD2_PASS`. The full complexes have respectively \(105896,105896,105832,105868\) nonempty simplices; the collapse certificates delete \(49150,50538,51041,50161\) pairs, respectively. The reduced homology groups agree exactly in all degrees.

The computation is finite and exhaustive, not a proof for other parameter sets. The group coefficients are \(\mathbb F_2\); agreement of ranks does not certify integral torsion-freeness or a particular homotopy decomposition. The four-class graph census is independently sourced from the classical strongly regular graph classification. No independent external audit has been performed.
