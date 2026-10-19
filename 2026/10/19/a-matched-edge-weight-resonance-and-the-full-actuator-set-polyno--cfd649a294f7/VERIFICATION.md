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
# Reproduction and limitations

Run `python3 verify.py` in a directory containing the extracted standalone file. It requires only Python 3 standard library and prints `VERIFY_OK 2167 checks` after exhaustive and seeded finite assertions. Every possible actuator subset is tested by exact finite-field Kalman rank for \(n=3,4\), and additional seeded tests cover \(n=5,6,7\). Every subset is independently counted for \(3\le n\le7\) under three integer matching rates; both closed subset-count polynomials and Bernoulli probabilities at rational \(p=1/3,2/3\) are checked. The prime for finite-field rank is 1,000,003; these integer instances have no unintended modular spectral coincidences.

The infinite theorem, the unique weight-collision condition, and the random-asymptotic limits are established analytically in `RESULT.md`; no finite enumeration or numerical experiment is treated as an infinite proof. Reproduction of the rank code is finite evidence only. Scientific originality cannot be certified by search exhaustiveness. Independent audit status remains unperformed.
