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
# Verification of threshold-reset stationary weak-field law

The standalone Python 3 checker `checker.py` uses SciPy and mpmath. Execute `python checker.py` from a directory containing the extracted files. The program tests the four pieces of the stationary density against direct numerical integration and the published closed expression for resetting-rate self-consistency, obtains the small branch by root-solving, and checks each weak-field regime. It also evaluates the special \(eta=2,lpha=3/4\) case using high precision and exact rational arithmetic, recovering \(45/16\).

Analytical reproducibility: verify \(Dk^2+hk=1\) and \(D\ell^2-h\ell=1\), continuity at the spatial joins, the reset-source derivative jump, and the exact exterior masses \(hC\), \(hCr\). For \(D\simlpha h^eta\) and \(eta>1\), apply the bounds \(r=O(e^{-h/D})\), \(\eta=1/k=O(h+\sqrt D)\), and \(C=1+O(h+D/h)\) to deduce the total-variation limit. Finally expand the exact mean expression through first or second order as appropriate. Numerical checks do not prove infinite-parametric asymptotics or originality; these depend on the proof and the comparisons separately.
