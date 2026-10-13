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

# Reproducibility and mathematical scope

Use Python 3 with SymPy and execute `python verify.py` from the directory containing this file. The exact symbolic checks reconstruct the damping adjoint on all Pauli matrices, all eight marginal identities, symbolic determinants, the two relevant pair constructions, and the strictly pairwise-but-not-triple witness at \(q=2/5\). The source of the infinite family of necessity results is the analytic positive-operator trace bound and the symmetry/conditioning argument in RESULT.md, not a finite experiment. Recomputed command output: `VERIFY_OK symbolic_marginals=passed Kraus_dual=passed pair_and_triple_determinants=passed rational_Specker_witness=2/5`.

The scope is the fixed orthogonal Pauli triple, not all possible input qubit measurements. Literature search risks include broader equivalent dichotomic-compatibility formulations. Independent audit has not been performed.
