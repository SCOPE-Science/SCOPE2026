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

The finite checker is a standalone C++17 translation unit `checker.cpp`. Run:

```sh
c++ -std=c++17 -O2 checker.cpp -o checker
./checker
```

It enumerates all unordered three-element subsets of the dihedral group of order \(2n\), for each \(3\le n\le14\). For every support, it constructs the complete integer left-convolution matrix using the group law and recomputes its rank by modular Gaussian elimination modulo `1000003` and `1000033`; the formula is compared with the larger modular rank. The checker independently constructs the divisor-based expected multiplicity histogram and the closed singular-support total. Sample output includes \(S(3)=20\), \(S(6)=160\), \(S(9)=708\), \(S(12)=1280\), ending with `CHECK_PASS`. The checks involve \(12,736\) full matrices across the twelve tested orders. Modular agreement supports the integer-rank prediction only for tested orders; the all-orders proof is the representation-theoretic and counting argument in `RESULT.md`.
