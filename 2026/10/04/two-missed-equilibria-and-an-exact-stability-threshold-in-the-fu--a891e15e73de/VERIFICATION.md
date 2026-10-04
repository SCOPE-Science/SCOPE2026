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

The accepted claim was checked from the displayed vector field with exact symbolic algebra.

`verify.py` performs the following checks:

1. substitutes the two claimed off-origin equilibria and verifies all four vector-field components vanish identically;
2. derives the origin characteristic polynomial and confirms the spectrum \(\{-35,12,-3,0\}\);
3. derives the characteristic polynomials for \(E_{+1}\) and \(E_{-1}\) directly from the Jacobian;
4. reconstructs the Routh first-column expressions used in the proof;
5. verifies that \(d_H=(119105-455\sqrt{68521})/3\) is the smaller positive root of \(3d^2-238210d+147000\);
6. checks the exact imaginary-pair factorization at \(d=d_H\); and
7. checks representative numerical spectra only as a secondary sanity test.

The proof in `RESULT.md` supplies the interval sign analysis needed for the continuum statement. The numerical checks are not used as substitutes for that proof.

Replay command:

`python verify.py`

Observed output is recorded in `verification_output.txt`.

Limits: the checker does not establish nonlinear Hopf nondegeneracy, global boundedness, basin geometry, or the existence of a hyperchaotic attractor.
