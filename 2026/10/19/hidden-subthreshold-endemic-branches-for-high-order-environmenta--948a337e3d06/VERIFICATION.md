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

# Reproducible verification

Run `python verify.py` with Python 3 and SymPy. The script reconstructs all stationary equations exactly in the fully positive rational witness, checks the scalar reduction, computes the exact Sturm count of strictly positive roots, evaluates exact rational signs at four points, checks the disease-free control reproduction number, and evaluates both singular-limit expressions symbolically.

The verified rational parameters are \(n=3\), \(\Lambda=4\), \(p=1/2\), \(\beta=1/4\), \(\epsilon=1/8\), \(\alpha_2=1\), \(\alpha=1000\), with all remaining positive rates and the Hill denominator constant equal to \(1\). The reproduction number is exactly \(5/42\); there are exactly two positive equilibrium infective coordinates, in \((1/20,1/10)\) and \((1/3,1)\).

Analytic verification beyond finite computation: the RESULT.md proof establishes the positive-denominator stationary reconstruction, the smooth singular rescalings, two nondegenerate limiting roots, and negative-real-part disease-free eigenvalues for all allowed parameters. The computer script illustrates and checks special algebraic identities; its finite outputs are not presented as an infinite-domain proof.

Limits: no proof of stability of the endemic equilibria, no disease-data fitting, no comprehensive publication-priority certification, and no independent scientific audit.
