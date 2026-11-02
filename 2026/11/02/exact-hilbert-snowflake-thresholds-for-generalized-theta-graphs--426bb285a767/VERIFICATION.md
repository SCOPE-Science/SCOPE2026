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

# Reproducibility and verification scope

`check.py` uses only the Python 3 standard library. Run `python3 check.py` in the directory containing the checker; a successful run prints `CHECK_OK`. It constructs the exact graph adjacency relation and independently derives each graph distance by breadth-first search, then tests the analytically predicted least centered-adjacency eigenvalue and its multiplicity. It also tests strict negative type at one subcritical exponent, endpoint nullity, and a positive supercritical direction for each of the 21 graph sizes \(m=1,\ldots,18,22,29,40\). The checker uses a Jacobi diagonalization rather than the proof's generalized \(2\times2\) matrix formula for numerical spectra.

Replayed result: `CHECK_OK`. Representative thresholds: \(p_3=0.757908242053\), \(p_4=0.673098261472\), \(p_{10}=0.511248489367\), and limit \(p_\infty=0.393115281945\). Numerically, \(m(p_m-p_\infty)\) tends to \(1.239434587929\); sample values at \(m=100,1000,10000\) were \(1.232743515677\), \(1.238755021256\), and \(1.239366524656\).

All finite diagonalizations use tolerances defined within the source. They do not establish infinite strict monotonicity, the error term, or absence of overlooked literature. Those statements are addressed analytically in `RESULT.md`. No claim of independent validation or formal proof certification is made.
