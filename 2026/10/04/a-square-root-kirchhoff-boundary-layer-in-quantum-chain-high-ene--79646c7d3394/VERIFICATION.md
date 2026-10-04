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
# Verification

`verify.py` reconstructs the exact \(\gamma=0\) coefficients of the primary secular equation and solves that scalar equation near the predicted branch. It does not insert the limiting width as an equation to be solved.

For \(\ell_1=2\pi\), \(\ell_2=2\pi/3\), \(\ell_3=4\pi/3\), \(\ell=1\), \(m\equiv1\pmod6\), and \(\tau=1.4\), the phase data are \(a=\pi/3\), \(b=2\pi/3\), and \(\varepsilon=-1\). The predicted limiting width is \(128\sqrt3/(\pi^3\tau^2)\). Exact-equation bisection at \(\theta=0\) and \(\theta=\pi\) gives decreasing absolute width errors for \(m=121,241,481,961\), ending below \(0.05\). A nontrivial Bloch-phase residual check also decays after the \(m^{-3}\) normalization. A successful replay prints `VERIFY_OK`.

The computation is supplementary. The infinite-sequence claim is established by the exact-coefficient asymptotic argument in `RESULT.md`; finite numerical convergence alone is not used as a proof. Resonant phase limits and the regimes \(\sqrt m\,t_m\to0\) or \(\infty\) are not verified or claimed.
