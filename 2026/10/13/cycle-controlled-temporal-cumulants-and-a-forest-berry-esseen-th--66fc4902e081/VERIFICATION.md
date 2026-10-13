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

The claim is proved analytically from the one-particle trace formula, Haar equidistribution of relative phases, and graph-incidence cancellation. The finite checker is supplementary and does not replace the proof.

Running `python3 verify.py` performs four independent checks. First, it expands torus moments by enumerating signed edge monomials on a six-vertex graph containing one triangle and one four-cycle with nonzero phases, and verifies the formulas for \(\kappa_2\), \(\kappa_3\), and \(\kappa_4\). Second, it checks that the vertex-to-root-and-edge-difference coordinate matrix for representative forests has determinant of absolute value one. Third, it confirms that a triangle has one linear edge-difference relation. Fourth, it verifies the algebraic Berry–Esseen prefactor \(8\sqrt2/(3\pi)\) from the exact cosine second and third absolute moments.

The proof covers every finite simple active graph for the displayed second through fourth cumulants and every finite forest for the exact independent-cosine law. The checker samples representative graphs only; no exhaustive enumeration is claimed or needed. No statement is made for resonant one-particle gaps, pairing Hamiltonians, or a sharp universal Berry–Esseen constant.
