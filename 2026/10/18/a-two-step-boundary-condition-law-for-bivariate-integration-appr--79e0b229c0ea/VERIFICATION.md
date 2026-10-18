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

# Verification details

The exact one-dimensional singular spectra are reconstructed from the Green kernels \(\min(x,y)\) and \(\min(x,y)-xy\), with Dirichlet–Neumann and Dirichlet–Dirichlet boundary conditions respectively. Sorted tensor products give exact finite-rank approximation errors. The rank-counting identity is proved by decomposing the lattice hyperbola at its square-root cutoff, including its overlap correction. Harmonic-number identities produce the constants \(2\gamma+(4-2r)\log2-1\) without numerical inference. The maximum divisor multiplicity controls tied ranks and makes the Lambert inversion valid at every rank.

Run the accompanying `check.py` with a standard Python interpreter. Its 636 successful assertions compare two independent integer enumeration strategies, test exact positions of tied ranks, and inspect representative values of the count asymptotic and boundary corrections. It does not establish infinite limits by enumeration. The proof gives asymptotic errors, not explicit optimal remainder constants. No independent mathematical audit has been performed.
