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

The analytic proof in `RESULT.md` establishes the entire stated parameter family. The `checker.py` program provides an illustrative floating-point test of the Green-matrix spectral index with direct finite-crossing matching, not an exhaustive computer proof.

Environment: Python 3 with NumPy and SciPy. Run `python checker.py` in the directory containing the program. The program forms transfer matrices for both zones, obtains the reciprocal growing/decaying Floquet solutions, constructs the diagonal matching function and the resolvent Green kernel, and solves one nonlinear crossing-location system per word.

Checked parameter choices: \(\alpha=1/4\), \(L_1=0.8\), \(L_2=1.6\), thresholds \(a=0.5\) (three crossings) and \(a=0.42\) (five crossings). For all 40 tested profiles, matching residuals were below \(10^{-8}\), crossings were transverse and the positive index matched the number of Q letters. The computed counts by positive index were respectively \((1,3,3,1)\) and \((1,5,10,10,5,1)\). Finite calculations do not establish the general theorem or historical novelty.

The source's Theorem 5.3 supplies existence and exponential crossing separation. Green-matrix index and isolated-phase derivative steps are reconstructed in `RESULT.md`. No independent mathematical audit has been performed. The nonlinear stability and full graph-symmetry-breaking questions remain open here.
