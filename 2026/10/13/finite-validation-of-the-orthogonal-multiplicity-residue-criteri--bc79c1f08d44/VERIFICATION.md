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

The claim is finite and is checked by exhaustive exact arithmetic. Compile `verify.cpp` with a C++17 compiler and run the resulting executable. It enumerates all words in \(\{T,T+1\}^d\) for each \(15\leq d\leq22\), marks their continuant denominators, enumerates every squarefree monic polynomial of degree \(d\) prime to \(T(T+1)\), factors it exactly over \(\mathbb F_2\), evaluates every simple-pole trace \(\psi_P(f)\), and compares the two predicates.

The replay on the packaged source ended with:

`VERIFY_OK degrees=15..22 coprime_squarefree_cases=1856852 mismatches=0`

Degree-by-degree tested counts were 7,286; 14,559; 29,132; 58,249; 116,514; 233,011; 466,040; and 932,061, all with zero mismatches.

A separate direct continuant enumeration gave the distinct-denominator counts 10,302; 19,921; 38,680; 75,053; 146,230; 284,755; 556,082; and 1,085,674 for degrees 15 through 22, exactly matching Table 1 of arXiv:2610.02352v1. This cross-check validates the continuant-membership side against an independently published table.

The verification does not extrapolate beyond degree 22. It does not test nonsquarefree polynomials or polynomials divisible by \(T\) or \(T+1\), and those cases are not claimed.
