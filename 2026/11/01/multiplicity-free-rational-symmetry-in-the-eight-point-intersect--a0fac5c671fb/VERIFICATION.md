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

# Reproducibility and independent limitations

The standalone `verify.py` reconstructs all \(56\) three-subsets of the eight-point ground set; constructs the orbit-conflict graph for every one of the \(22\) conjugacy types; and evaluates its independence polynomial at \(-1\) via an exhaustive memoized deletion recursion. It separately computes the ninth-homology character from six-subset stabilizers, evaluates all irreducible \(\mathfrak S_8\) characters by Murnaghan–Nakayama, verifies their full orthogonality, and checks all Specht multiplicities and dimensions. The pair-orientation calculation explicitly checks the transposition giving the sign-twisted stabilizer action. Running `python3 verify.py` requires only Python 3.10 or later and no downloaded scientific data.

The checker does not recompute the entire high-dimensional simplicial boundary complex. Its inputs that the only rational homology degrees are six and nine and that their ranks are \(233\) and \(28\) come from Feng (2026), Theorem 18; the six-subset cross-polytope classes form an independent family by Feng and Wang (2024), Theorem 10. The first two are scientific premises, not computational assumptions inferred from a finite experiment. No integral homotopy claim or independent validation is asserted.
