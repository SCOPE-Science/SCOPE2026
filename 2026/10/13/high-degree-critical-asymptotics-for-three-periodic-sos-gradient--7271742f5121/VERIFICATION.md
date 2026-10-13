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

The analytic proof is primary. The packaged checker performs the following independent finite tests against the formulas used in the proof.

1. It brackets the unique positive root of \(e^c+1-2e^{-c}-3c=0\) by bisection and reconstructs \(C_*\), \(D_*\), and \(\sqrt{C_*}\).
2. For selected orders \(k\), it solves the exact derivative polynomial from the source-derived objective on \((0,1)\), then evaluates \(\psi_k(a_k)\).
3. It verifies numerically that \(-k\log a_k\) approaches \(c_*\) and that the residual after subtracting \(2+C_*/k+D_*/k^2\) is consistent with order \(k^{-3}\).
4. It checks the source normalization \(\tau_c(k)=2\cosh\beta_c(k)\) against the displayed inverse-temperature expansion.

The finite checks do not prove the asymptotic theorem. The proof uses exact inequalities, compactness, uniform analytic expansion, uniqueness and nondegeneracy of the limiting minimum, and Taylor expansion of \(2\cosh\beta\).
