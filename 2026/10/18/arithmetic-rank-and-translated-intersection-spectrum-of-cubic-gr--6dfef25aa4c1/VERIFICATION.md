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
# Verification and reproducibility

The included pure-Python program `cubic_gabor_verify.py` uses only the standard library, with no randomization and no external files. Run `python3 cubic_gabor_verify.py` from this directory. Its standard output is embedded separately in `cubic_gabor_verify_output.txt`.

It reconstructs each translated intersection for all \(p^2\) shifts at primes \(p\in\{5,7,11,13,17,19,23,29,31,37\}\). It compares each intersection size with the completed-square criterion, tests ambiguity zeros on every nonempty translation by exact prime-cyclotomic coefficient multiplicities rather than floating-point tolerance (empty intersections vanish identically), compares the counted rank with the closed formula, and verifies that each two-point shift has uniform nonzero character differences among all modulation frequencies. The output ends in `ALL EXACT CHECKS PASSED`.

The test enumerates finite cases, **not** infinitely many primes. The all-prime mathematical proof is in `RESULT.md`: it uses exact finite-field algebra, the elementary quadratic-form level count, irreducibility of the prime cyclotomic polynomial, and Weyl-character diagonalization. No direct full complex measurement-matrix singular-value decomposition was used. In particular the identity-translation nonzero cubic Gauss-sum magnitudes are not classified beyond their exact defining expression and their zero locations. Independent mathematical auditing was not performed.
