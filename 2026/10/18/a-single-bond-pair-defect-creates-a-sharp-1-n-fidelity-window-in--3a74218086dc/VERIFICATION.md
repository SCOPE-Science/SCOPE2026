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

# Reproducibility and verification

Run `python verify.py` with Python 3 and NumPy. No network, external dataset, or unpublished attachment is required. The program reconstructs the hopping map \(B\), computes \(P=I-B^\top(BB^\top)^{-1}B\), and checks its entries against all three exact rational formulas. It also rebuilds the entire projected two-endpoint Hamiltonian, directly diagonalizes it, and compares the computed transition amplitude against the two-frequency closed form at five different times for each tested parameter set.

The tested lengths were \(2\le N\le22\), with nine defect values in \((-1,1)\) at each length, including zero. It additionally checks the asymptotic slow-beat coefficient for four values of the scaled defect parameter. Recorded run: **2,818 comparisons passed**, worst numerical error \(7.590\times10^{-15}\). The inverse and projection checks are necessary numerical sanity checks; the uncountable parameter assertion and density-based supremum are proved symbolically in `RESULT.md` and are not certified by these samples.

The physical channel at fixed nonzero coupling \(g\) includes dispersive states; its finite-coupling errors are outside the exact projected theorem. No outside laboratory replication or independent mathematical audit has been carried out.
