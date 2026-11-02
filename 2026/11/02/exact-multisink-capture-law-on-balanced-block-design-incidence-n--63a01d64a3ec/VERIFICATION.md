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

The standalone checker `proof/verify_general.py` uses standard Python with NumPy, SciPy and SymPy (versions in `proof/requirements.txt`). Run `python proof/verify_general.py` after installing the requirements. Recorded stdout is supplied as `proof/verification_general_output.txt`.

It constructs the Fano plane, projective plane of order three, an \((11,5,2)\) biplane, the point-hyperplane design of \(\operatorname{PG}(3,2)\), the affine plane of order three, the point-line design of \(\operatorname{PG}(3,2)\), and all triples of seven points. It independently verifies incidence identities, subspace ranks, closure under the adjacency action, exact symbolic projectors, numerical QR projections, and selected non-Hermitian survival amplitudes.

The output reports **244 distinct marked-point subsets**, **6,936 point/block site comparisons**, **150 exact symbolic projection cases**, and **20 dissipative tests**. Maximum numerical projector discrepancy is \(1.110\times10^{-15}\). Numerical dissipation tests used finite evolution times and a tolerance of \(5\times10^{-5}\); these tests do not establish infinite-time decay. The proof of infinite-time decay in RESULT.md uses dissipativity plus nonexistence of undamped modes in the generated invariant subspace.

No independent external audit was performed. The mathematical result is proved in RESULT.md; sample computations do not exhaust all designs, subsets or absorption rates.
