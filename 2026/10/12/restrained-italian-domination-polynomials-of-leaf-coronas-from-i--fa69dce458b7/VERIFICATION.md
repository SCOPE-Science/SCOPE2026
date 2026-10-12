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

Run `python verify.py` using Python 3 with no nonstandard dependencies. The script constructs leaf coronas and independently enumerates all \(3^{2n}\) ternary assignments on the combined root-and-leaf vertex set for the tested sizes. For each zero-labeled vertex, it checks separately (i) existence of a zero-labeled neighbor and (ii) total open-neighborhood label weight at least \(2\). It then compares each coefficient of the brute-force enumerator with formula (1).

The tests comprise all \(76\) labeled simple graphs of order at most four (orders \(0,1,2,3,4\) have \(1,1,2,8,64\) cases), plus \(30\) deterministic order-five and \(5\) order-six graph samples. For the sunlet orders \(3\) through \(11\) they compare the whole closed polynomial (3) with the general subset formula (1), and the minimum weight and coefficient with (4); direct independent ternary enumeration of the sunlets is also performed through order \(7\). The captured full script output is `verification_output.txt`, and it ends in `VERIFIED_FINITE_CHECKS_OK`.

These exact finite calculations support the algebra and boundary handling. The universal polynomial, cyclic-run enumerator, and all-order minimum identities are proved mathematically in `RESULT.md`. No external or independent audit has been performed.
