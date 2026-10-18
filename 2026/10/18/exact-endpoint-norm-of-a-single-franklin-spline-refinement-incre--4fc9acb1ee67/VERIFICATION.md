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

# Reproducibility and scope

The self-contained companion `checker.py` requires Python, SymPy, NumPy, and SciPy. Run `python checker.py` next to this document. It reports 590 passing assertions across exact symbolic Gram and rational identities, positive derivative coefficients, twelve independently solved finite-section Gram systems, independently evaluated cell integrals, and 101 sampled profile values. The finite-section computations test the analytic formulas but do not replace the infinite-dimensional proof.

The paper derives the infinite-grid inverse from an invertible Toeplitz Gram operator, reconstructs the unique rank-one difference, evaluates all infinite tails by convergent geometric sums, and certifies strict parameter monotonicity algebraically. The exact \(L^1\) endpoint equality follows from the symmetric rank-one kernel.

The historical Bechler Strömberg-wavelet paper was inaccessible in full, so historical priority is subject to external bibliographic comparison. No independent audit or validation has been performed.
