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
# Reproducibility and boundaries

Run `python3 check_two_amplitude.py` with Python 3.9 or later (standard library only). The script enumerates the \(N^2\) cyclic Gabor ambiguity entries for every odd \(N\) from \(5\) through \(25\), every nonzero defect spacing and a list of real generic and exceptional amplitudes; it compares each counted nonzero with the closed all-dimensional formula. The finite sweep contains 2,392 tests. Additional direct Gaussian elimination of vectorized orbit projectors in dimensions \(5,7,9\) provides 42 tests. No external data are required.

These calculations use floating-point complex roots of unity and a tolerance. They do not prove universal nonvanishing. Exact correctness instead follows from the three displayed ambiguity identities, odd-order root rigidity, integer congruence counts and the proven projector-Gram diagonalization. Normalization is nonzero for the declared domain. No claim is made for even orders or nonreal amplitudes.
