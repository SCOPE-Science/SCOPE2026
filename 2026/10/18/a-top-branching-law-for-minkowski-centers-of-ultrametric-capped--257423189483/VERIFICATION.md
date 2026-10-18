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
# Verification record

The mathematical proof is the seven-step derivation in `RESULT.md`. Its essential independently checkable identities are the exact support minima of the coordinate and triangle inequalities, the reflection reformulation \((s+1)a\cdot c\le sb+\min_{K_w}a\cdot d\), and the deficit propagation over the ultrametric's highest partition.

Run `python CHECKER.py` in Python 3 with NumPy and SciPy. The program constructs the original polytope inequalities, solves a distinct linear program for every triangle-support minimum, solves the Minkowski-asymmetry program, and then finds both extreme values of each optimal-center coordinate while fixing \(s=2\). It checks six hand-specified ultrametrics and 32 additional pseudorandom but reproducible hierarchical examples of size three through six. All 38 cases passed the stated comparisons. The numerical solver is finite-precision and does not prove the universal theorem; the seven symbolic proof steps supply that proof.

The research claim is limited to strictly positive ultrametric ceilings and at least three labels. The referenced literature on generic polyhedral center optimization, bounded metric-polytope ellipsoids, and tropical ultrametrics concerns different statements. Independent mathematical and bibliographic validation remain unperformed.
