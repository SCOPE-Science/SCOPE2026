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

# Reproducibility and verified limits

The self-contained `verify_hopf.py` requires Python 3, SymPy, and NumPy. Run `python verify_hopf.py` from the directory containing this document and the script. It first computes the exact planar Lyapunov derivative expression and symbolically proves its equality to \(((r-2)\omega^2-(r+2))/(16s(1-s))\). It then evaluates both published-game and rational-payoff example equilibria, checks the logit fixed-point and zero-trace equations, and calculates the independent multilinear complex-eigenvector coefficient, verifying \(\operatorname{Re}G_{21}=8\ell_1\).

The source-game tests at \(\varepsilon=0.5,1,3,1000\) return negative coefficients; the second-game tests at \(\varepsilon=1\) and \(\varepsilon=200\) return negative and positive coefficients respectively. All six tensor comparisons passed with absolute error below \(3\times10^{-10}\). The symbolic identity, rather than the six tests, proves the parameter-wide coefficient formula. The ordinary Hopf theorem is used only where the real-part crossing and coefficient are nonzero. The vanishing first coefficient is **not** treated as evidence of a generalized Hopf point, and no global periodic-orbit assertion is verified.
