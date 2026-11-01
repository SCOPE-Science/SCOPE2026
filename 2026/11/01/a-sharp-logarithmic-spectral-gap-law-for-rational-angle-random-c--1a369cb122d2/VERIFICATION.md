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

# Scientific verification

The packaged standalone `check_feres.py` reconstructs the original four-branch transition kernel numerically, independently forms the exact edge-conductance graph from its displayed trigonometric formulas, verifies all row sums, reversibility, stationary probabilities and agreement of both constructions, and computes real symmetric-conjugate spectra at specified small and medium integers. Those are finite reproducibility checks only; they are not an infinite proof or an independent scientific audit.

The analytical spectral-gap proof uses exact finite edge identities, the two parallel resistance sums, a weighted same-parity variance estimate and a matching Rayleigh-quotient argument. The source of the original probability functions is Vales and Pinto-de-Carvalho, arXiv:2005.01892, §3.1, with earlier derivation by Feres (2007), §2.2. The closest literature comparisons and remaining novelty risks are described in `REVIEW.md` and `AUDIT.json`.

Run `python check_feres.py` with NumPy and SciPy installed. No inaccessible computation or other package files are required.
