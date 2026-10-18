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

# Reproduction and limits

Run `python verify.py` using Python 3 standard library. It verifies 2000 exact-rational rearrangements of the two-defect formula for generic finite moment data and two stationary Gaussian-kernel quadrature examples (2004 checks total). The examples use \(\lambda=1\), \(\sigma=\sqrt{2}\), \(k=1\) and \(arepsilon=0.05\). The lower baseline \(h_0=0.65\) produces a positive variance gap relative to constant step equal to the chain's mean \(H\); the upper baseline \(h_0=1.4\) produces a negative gap. The script also numerically checks that both computed gaps satisfy the analytical balance. Discretizing an integral kernel and checking finite cases cannot certify the uniform theorem or uniqueness; see RESULT.md for the analytic proofs of geometric drift, symmetry, covariance sign, and Gaussian perturbation asymptotics. All scientific evaluations described here were non-independent; independent validation has not occurred.
