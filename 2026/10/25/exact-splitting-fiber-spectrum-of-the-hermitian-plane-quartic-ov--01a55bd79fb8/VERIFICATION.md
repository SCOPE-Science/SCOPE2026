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

# Exact reproducibility of the arithmetic census

The curve is \(Y^3Z+YZ^3=X^4\) over \(\mathbb F_{729}=\mathbb F_3[t]/(t^6+t+2)\), using base-three coefficient encoding for field elements in the range 0 through 728. Both C++17 files are independent and require no third-party packages.

To replay from a directory containing the two source files:

```sh
g++ -O3 -std=c++17 verify.cpp -o verify
g++ -O3 -std=c++17 check_direct.cpp -o check_direct
./verify
./check_direct
```

The first program verifies all 728 field inverses, enumerates 892 curve points and 532171 rational projective lines, reconstructs curve-point pair incidence on all lines, then enumerates all centers and proves the exact 63-point \(\mathbb F_9\) exceptional locus. It prints `VERIFY_OK` only after all assertions succeed. The second obtains line intersection characters by an independent quartic-root equation and enumerates all 532171 lines and centers, printing `DIRECT_VERIFY_OK` after confirming the complete histograms.

Both programs were compiled and executed from the actual source files and returned their success markers. The complete exterior histogram has 17 support values, sums to 531279, and has weighted sum 28952154. There are 39879 four-secant lines, hence 29111670 point–four-secant incidences. The remaining 159516 incidences occur at the 892 rational points on the quartic. The result is exact for this finite field; it is not a general symbolic proof for all finite fields. External mathematical audit and independent validation have not been performed.
