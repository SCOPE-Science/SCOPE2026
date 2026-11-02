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

# Verification of the exact rook-graph Ising classification

The analytic argument is contained in `RESULT.md`. The accompanying script is `artifacts/verify.py`; from the extracted package root run `python3 artifacts/verify.py` with a Python 3 interpreter and NumPy installed. The expected stdout is in `artifacts/check_output.txt`.

The direct-edge spin census independently evaluates the Hamiltonian for every spin configuration on boards of sizes 2x2, 2x3, 3x3, 3x4 and 4x4 at 335 coupling/field trials. A separate dynamic program checks fixed-magnetization minima and counts for every sector of six board sizes through 5x5, for two exchange anisotropies; an independent elementary-symmetric generating-function coefficient counter agrees with all these sector counts. Exact rational covariances are checked for 39 nontrivial sectors, and six arithmetic breakpoint counts are tested. The extraction replay of the checker matched the embedded output.

These finite experiments do not prove all-size correctness or uniqueness. The proof requires simultaneous feasibility of balanced row/column degrees, provided by integer network flow, and the covariance argument requires fixed-magnetization permutation symmetry. The field boundaries, strict positive couplings, degenerate sectors and antiferromagnetic sign conventions are included in the analytic statement. Independent scientific validation has not been performed.
