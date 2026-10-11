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

# Verification details

Run `python3 artifacts/verify.py` with Python 3 and its standard library. Successful output is:

`VERIFY_OK cases=107 primes=3 direct_fourier=4 exact_fiber_deficit_and_packet_tests=passed`

For \(p=3,5,7\), the checker enumerates all ordered parameter pairs \((x,y)\) modulo \(p^2\) and groups them by \((x+y,x^2+y^2)\). It independently groups the same input into residue-class convolution energies. It compares both values for eight deterministic Gaussian-integer test functions per prime; the arithmetic values are integral, so the tiny numerical tolerance serves only to accommodate built-in complex-number representation. The program checks all \(p^2\) character packets in each field and confirms the sharp value, then performs four explicit complex-exponential Fourier-synthesis evaluations at \(p=3,5\). It also verifies the global distance-to-packet estimate for the deterministic examples.

The checker provides finite consistency evidence; no finite test is asserted to prove a universal infinite family. The universal mathematical verification is the pair-fiber injectivity argument, cyclic Parseval identity, nonnegative deficit factorization, and equality characterization in `RESULT.md`. The distance constant is valid, not asserted best possible.
