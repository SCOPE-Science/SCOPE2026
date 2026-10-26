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

# Reproducibility

Execute `python3 verify_annihilation.py` with a standard Python 3 interpreter. It requires no external packages or network access.

The program constructs the full labeled-state jump generator independently from the closed formulas and verifies the exact Poisson equation \(-L f=1\) on each transient occupancy configuration. The tests cover 1–8 leaves and five exact positive rational hub speeds per graph size, totaling 4,840 transient-state residual identities. The smallest graphs are independently solved by exact-rational Gaussian elimination of the full transient generator, giving 210 statewise comparisons; there are also 12 fixed-hub-rate and six linearly scaled hub-rate numerical asymptotic checks. The tests passed when executed from the actual supplied program.

Finite-state tests are not an infinite proof. The proof in `RESULT.md` establishes the claim for every integer number of leaves and every positive real hub rate by first-step conditioning, explicit solution, and asymptotic analysis. No independent external scientific audit has been performed.
