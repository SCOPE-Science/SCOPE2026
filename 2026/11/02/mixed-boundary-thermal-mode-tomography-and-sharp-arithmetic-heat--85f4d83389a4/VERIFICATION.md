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

# Verification instructions

Run `python checker.py` from a directory containing the embedded program; requirements are Python 3, NumPy, and SciPy. No external data or network connection is needed. The reproducibility file constructs the mixed-boundary stiffness independently and solves the stationary Lyapunov matrix equation before comparing its mode energies with the proposed transfer. It tests dimensions 2 through 150 for the algebraic identities, inversion, singular-norm scaling and exact modular maxima/minima, plus smaller independently simulated stationary covariance systems.

Recorded checks: 745 transfer/recovery/norm tests, 36,055 arithmetic comparisons, and 44 independent Lyapunov comparisons passed. Arithmetic counts use direct numerical congruence identities in addition to independent maxima over matrix rows. The computational checks do not establish all-dimension correctness: the exact cosine orthogonality and modular proof in `RESULT.md` do. The primary physical model and its forward transfer were compared against arXiv:1505.05088, equations (6), (8), (11), and (A13), with its free-boundary inverse equation (12) explicitly excluded from claims of novelty.

No external independent audit or experimental validation was performed. Historical priority for simple consequences of the existing forward equation remains a limitation.
