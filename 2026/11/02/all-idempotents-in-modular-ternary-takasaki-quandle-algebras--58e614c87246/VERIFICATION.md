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

# Verification and limits

The complete proof is in `RESULT.md`. Execute `python3 verify.py` in a Python 3 environment. The sole dependency is the standard library. `checker_output.txt` records one successful run ending `VERIFY_OK`.

Direct brute-force star-idempotent checks: \(27\) algebra elements over \(\mathbb F_3\) at \(d=1\); \(729\) over \(\mathbb F_9\) at \(d=1\); and \(19\,683\) over \(\mathbb F_3\) at \(d=2\). Their complete counts are respectively \(4\), \(10\), and \(82\), with exactly the parametrized points and zero. The program checks all \(6\,561\) parameters for \((q,d)=(9,2)\) but does not enumerate all \(9^9\) ambient elements. For \((3,3)\) it checks 100 reproducible parameter values, not all \(3^{13}\) possible nonzero idempotents. Separate convolution and direct quandle multiplication routines cross-check the normalization; small pairwise products cross-check closure.

The all-dimensional statement rests on the symbolic argument \(u\star v=\sigma(uv)\), \(u^3=arepsilon(u)^3\), and the inverse bijection \(w=u-\sigma(u)\). Finite tests are independent cross-checks, not proofs for infinitely many dimensions or coefficient fields. No automated formal proof or independent audit is claimed.
