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

The standalone file `verify.py` requires Python 3 standard library only. From the directory containing it, run `python3 verify.py`. It has been executed and reports `PASS 13714 independent equalities and feasible-comparison assertions`. It verifies exact rational balanced/dominant families, positive price-budget identities, direct weighted-tree all-vertex diameter versus leaf-pair diameter, and inequalities for many other independently generated feasible conductance allocations. Positive edge prices are tested both uniformly and nonuniformly. The proof in `RESULT.md` handles every real price and all finite arm lengths; no finite test can prove those quantifiers.

The optional `optcheck.py` requires NumPy and SciPy and is run as `python3 optcheck.py`. It independently formulates the nonlinear epigraph constraints for all leaf pairs, optimizes edge conductances under a full budget, and checks 20 cases against the formula to absolute tolerance \(10^{-7}\). All 20 objective comparisons agree. Of the 20 optimizations, 16 return successful optimizer status; four terminate with a line-search status while their objective values still agree to the stated tolerance. Such a status is not evidence of guaranteed global convergence or mathematical impossibility; the analytic proof supplies the global result.

The source comparison uses the inspected 2006 Ghosh--Boyd--Saberi proceedings (especially the introduction and Section VII), the accessible full text of Roos--Bai--Chaerani (2012), and mathematical overlap searches. The general minimum-maximum-resistance convex-programming formulation was already known. The new claimed item is only the closed-form spider solution and its uniqueness and threshold. No independent mathematical audit is claimed.
