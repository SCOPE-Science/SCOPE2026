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

Run the included standalone script from the same directory with `python3 verify.py`. Expected final line: `VERIFY_OK`.

- Independently enumerate partitions with a given number of part sizes through \(n=120\), using a size-by-size dynamic program.
- Recompute exact two- and three-size counts from divisor convolutions, including the explicit two-equal-size and three-equal-size terms, and compare each coefficient.
- Check the \(k=2\) cumulative expansion at cutoffs \(1000\), \(10000\), and \(100000\). Recorded relative differences are about \(1.94\cdot 10^{-3}\), \(1.87\cdot 10^{-4}\), and \(1.72\cdot 10^{-5}\), respectively.
- The analytic proof uses the classical \(O(\sqrt X)\) divisor-summatory remainder and a finite-order inclusion-exclusion; none of the finite tests prove these estimates.

Independent audit has not been performed. Publication priority, particularly relative to the full Kim 2012 text, is not fully verified.
