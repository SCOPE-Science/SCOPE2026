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

# Reproducibility and limits

Build and execute the portable C++17 verification source supplied alongside this document:

```sh
c++ -O2 -std=c++17 VERIFY.cpp -o verify
./verify
```

The successful program prints `WEDGE_TRIVECTOR_OK`. It independently enumerates all \(2^{20}=1,048,576\) elements of \(\Lambda^3(\mathbb F_2^6)\), creates the \(15\times6\) wedge-by-trivector matrix from coefficients, and computes its rank over \(\mathbb F_2\). The observed ranks are zero (1 case), three (1395 cases), five (54684 cases), and six (992496 cases); no other ranks occur. It separately constructs the four nonzero graded maps of the square-zero exterior multiplication operator in six generators for three representative divisor classes and primes \(2\), \(3\), and \(5\); all map ranks and resulting total homology dimensions agree with the theorem.

The program is not a verification of all field sizes or all dimensions and is not an independent mathematical audit. The mathematical proof in `RESULT.md` provides the stated uniform quantifiers. In particular the geometric statements apply to reduced varieties; no scheme-theoretic multiplicities or full orbit classification are tested. Independent audit remains not performed.
