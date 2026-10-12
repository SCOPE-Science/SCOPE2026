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
# Verification

The result is an all-state analytic statement within the precisely defined zero-dipole spin-one sector. The decisive proof establishes the equality between classical moment matrices and all trace-one positive semidefinite three-by-three matrices after antipodal symmetrization, and proves a global variational projection inequality for the displayed optimizer. These are mathematical arguments, not numerical extrapolations.

Run `python3 verify.py` using the standard Python library. It tests 342 rational triples of probabilities for spin-one zero-dipole states, checks the projected classical spectrum, the exact squared-distance identity, the 3-point moment construction and a nonaxial full-rank rational spin-one density. Its explicit partial-transpose spectrum includes the negative eigenvalue \(-1/4\) and gives the exact identity \(Q^2=3/32\).

The verifier does not test all continuum states, does not certify uniqueness, and is not an independent external audit. Those are addressed by the analytic variational proof and its stated hypotheses. The normalization is the ordinary Hilbert–Schmidt distance, with the spin-one Bloch Frobenius factor \(1/2\); negativity uses the symmetric two-qubit embedding. Other distance norms, nonzero first moments, and unrestricted two-qubit separable-state optimization are outside scope.
