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

# Exact finite verification

The distributed `verify.py` and `verify_alt.cpp` are self-contained. Build no graph from a downloaded table. Python generates adjacency from coordinate differences; C++ adds all product-factor edges directly. Both check 64 vertices, degree nine, reduced Laplacian size 63 and every valuation for primes two and three. Python checks the 16-vertex strongly regular parameters; C++ checks adjacency symmetry and regularity.

Run:

```sh
python3 verify.py
g++ -O2 -std=c++17 -Wall -Wextra verify_alt.cpp -o verify_alt
./verify_alt
```

The first must print `CRITICAL_GROUP_CERTIFICATE_OK`; the second must print `INDEPENDENT_CERTIFICATE_OK`.

Both implement ring-preserving elimination over modulus \(2^9\) and \(3^5\), with opposite choices among equally valued pivots. All 63 valuations lie below those bounds. For the Doob graph, the two-primary valuation counts are \((28,3,4,2,6,14,6)\) in exponents zero through six. For the Hamming graph they are \((28,1,8,0,6,14,6)\). Both have three-primary counts \((36,27)\) at valuations zero and one. By the common spectrum, the reduced determinant is \(2^{147}3^{27}\); neither other primes nor unobserved larger prime powers can enter.

The finite certificate establishes these two graphs only. Computational agreement and self-review are not external independent validation.
