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

# Arithmetic verification of the radical Jordan spectra

The standalone implementation `artifacts/verify.py` constructs multiplication in the full 16-dimensional exterior algebra by enumerating disjoint bitmask monomials, with the correct inversion sign. It independently computes the ranks of the matrices of multiplication by \(a\) and \(a^2\) by modular Gaussian elimination. Its classification comparator uses only degree filtration and Pfaffian data, and it separately checks the predicted symbolic multiplicities sum to \(q^{15}\).

Executed successfully over prime fields of orders 2, 3, 5 and 7. Tests included 8,000 uniformly sampled radical vectors in characteristic two, 1,500 samples in each of characteristics three, five and seven; all 32,768 binary radical vectors were enumerated with the direct structural classifier; all 64, 729, and 15,625 pure two-forms over the fields of orders 2, 3 and 5 were individually checked via actual 16-by-16 matrix ranks, as well as their complete predicted rank histograms. The program terminates with `VERIFY_OK_EXTERIOR_JORDAN`.

The exhaustive binary classification step uses the structural classifier, not an independent full-matrix computation of all 32,768 elements. Rank-matrix checks for arbitrary radical vectors are randomized and reproducibly seeded. All-field and arbitrary prime-power validity is a theorem-level proof claim, not a computational certification. No independent mathematical audit was performed.
