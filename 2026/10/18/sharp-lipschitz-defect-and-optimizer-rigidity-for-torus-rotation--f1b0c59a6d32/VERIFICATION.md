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

# Verification of the torus torsion-defect formula

The theorem is proved analytically in `RESULT.md`. The main logical checks were the classification of torsions on \(C(\mathbb T^d)\) as circle-valued multipliers, existence of the integer winding vector for every continuous multiplier, the exact Euclidean Lipschitz lower bound on winding, translation invariance of the Haar mean of the real phase coboundary, connectedness of the real phase-error image below operator defect \(2\), and the equality case at the endpoint of an interval. These jointly prove the infimum and all optimizer claims; no finite search is treated as a proof of universal validity.

The reproducible `CHECK.py` uses only the Python standard library. Running `python CHECK.py` checks the character formula at multiple one- and two-dimensional budgets and checks that explicit sine-perturbed phase functions do not beat the character bound on sampled grids. Example outputs for the circle rotation \(\beta=2\pi(\sqrt2-1)\) and target \(-1\) give defects approximately \(0.532510684083\) at budget \(1\) and \(0.092446900979\) at budget \(8\). These checks catch phase-sign and \(2\pi\)-scaling mistakes only.

No classification of all optimizers is claimed at the diametral defect \(2\); the exact finite minimization formula and character attainment do include that case. No general Diophantine decay rate is asserted. The critical assertion is proved for the continuous-function lattice and Euclidean flat torus metric only. Originality remains subject to possible unindexed cocycle-theory literature; independent review has not been performed.
