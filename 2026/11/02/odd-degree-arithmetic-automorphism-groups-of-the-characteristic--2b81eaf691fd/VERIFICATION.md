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
# Reproduction and scope

Run `python3 verify.py` with an ordinary Python 3 interpreter; no external packages are required. The program builds \(\mathbb F_{32}=\mathbb F_2[\alpha]/(\alpha^5+\alpha^2+1)\), enumerates exactly the binary cyclic-matrix centralizer, constructs the self-dual degree-five normal-basis change of coordinates, computes the binary orthogonal group by a complete basis backtracking, and checks the resulting 720 matrices after conjugation against the defining semilinear isometry equation. The execution result in `verification_output.txt` ends in `VERIFY_OK`.

The executable check verifies the finite binary and extension-field calculations. It does not establish by enumeration the claims over infinitely many odd extension degrees, which rest instead on the algebraic field-of-definition identity and cube-normalization proof in `RESULT.md`. The complete-group assertion also invokes the classical Picard-group theorem for smooth cubic threefolds. The current review is not independent expert certification.
