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

The exact matrix calculation shows \(A^2=(|S|\bmod2)I\) in every dimension. The idempotent argument then reduces to the quadratic-subfield alternatives for the polynomial \(z^4-z\), and the \(\mathbb F_4\) case is parametrized without omitted branches via \(B^2=0\). The hypercube computation reduces the rank to multiplication by one square-zero variable, proving its half-rank formula for every odd dimension.

Reproduce finite checks by running `python3 verify.py` with Python 3 and its standard library. The program builds original multiplication directly, enumerates all field-coordinate tuples in 17 small cases, independently constructs parameterized idempotents over \(\mathbb F_4\), validates the adjacency-square parity identity, and checks hypercube ranks for dimensions 1, 3, 5, and 7. Its successful terminal line is `VERIFY_OK 21 cases`. Field orders four and eight use irreducible binary polynomials. These computations do not certify general statements; those are proved symbolically in `RESULT.md`.

Scientific limitations: no assertions about general weighted Cayley algebras, other group exponents or characteristics, all possible ranks for a fixed graph size, or algebra isomorphism classifications. The verification here is same-model and does not constitute independent mathematical validation.
