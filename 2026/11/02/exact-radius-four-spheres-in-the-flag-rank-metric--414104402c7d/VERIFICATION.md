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
# Reproducibility and evidence

The all-parameter theorem is proven by a six-type count in `RESULT.md`. The executable `verify_flag_rank_radius4.cpp` independently generates every matrix in each finite test field, computes all crossing ranks by Gaussian elimination, classifies matrices of total rank sum four, and compares each class total with the polynomial term. It tests \(\mathbb F_2\) for \(n=3,4,5,6\), \(\mathbb F_3\) for \(n=3,4\), and \(\mathbb F_4\) for \(n=3,4\). The latter field uses the irreducible relation \(z^2+z+1=0\).

Compile with `g++ -O3 -std=c++17 verify_flag_rank_radius4.cpp -o flag_rank_check`, then run `./flag_rank_check`. Compare with the supplied `verification_output.txt`; all eight tests pass and the final marker is `FLAG_RANK_RADIUS_FOUR_EXACT_CHECK_OK`.

The finite checks do not prove the result for all fields or lengths, and do not validate an independent mathematical audit. The proof uses no numerical optimization and no unprovided computational certificate. The historical literature comparison retains the possibility of implicit equivalent formulations.
