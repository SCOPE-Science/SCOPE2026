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
# Verification record

Run `python3 verify.py` from the directory containing the result artifacts. The script needs Python 3's standard library only.

It independently forms graph adjacency matrices, checks the action on two peripheral eigenspaces and the hub/uniform-outer invariant subspace, and compares the claimed transition-amplitude identity with independently evaluated complex matrix exponentials at finitely many graph orders and times. The Taylor series is deliberately oversummed to suppress truncation error at the tested parameter ranges. The script also checks roots of both strictly convex variational objectives and finite large-parameter examples from each square and nonsquare regime.

Observed output:

`VERIFY_OK exact_invariant_subspace_checks=36 independent_matrix_exponentials=27 finite_asymptotic_tests=16 constants=0.292893218813,0.419296833428,1.305301344447`

These checks do not establish the unrestricted limit theorem. Proof of that theorem is the symbolic spectral reduction, Kronecker-density argument, and uniform localized expansion in `RESULT.md`. No independent mathematical audit has been performed.
