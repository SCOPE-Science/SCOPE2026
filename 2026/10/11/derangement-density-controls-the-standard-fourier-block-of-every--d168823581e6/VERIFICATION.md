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

The universal proof is analytic. The critical checks are:

1. For a doubly transitive action, the permutation character has inner product \(2\) with itself, so after removing the trivial constituent the remaining degree-\(n-1\) character is irreducible.
2. Schur orthogonality gives the central primitive idempotent kernel \(d\chi(g^{-1})/|G|\).
3. The endpoint norm of finite-group convolution is the absolute mass of its kernel.
4. The standard character is \(F(g)-1\), so its negative support is exactly the derangement set and every negative value is \(-1\). Zero total character sum therefore gives \(\sum_g|\chi(g)|=2D\).
5. The complement kernel has positive identity coefficient because double transitivity gives \(|G|\ge n(n-1)\), and direct absolute summation yields \(1+2(n-1)(D-(n-1))/|G|\).
6. Cameron--Cohen's rank-two specialization gives \(D\ge |G|/n\) with equality precisely in the Frobenius equality case, completing the sharp-double-transitivity criterion.

`verify.py` performs exact integer/rational checks for \(S_n\), \(2\le n\le8\), and for \(\operatorname{AGL}(1,p)\), \(p\in\{3,5,7,11\}\). It also checks that in the sharply doubly transitive affine cases the complementary convolution kernel is exactly uniform on the translation subgroup. Expected terminal line:

`VERIFY_OK symmetric_n=2..8 affine_primes=3,5,7,11`

The finite computations do not prove the general theorem; they only replay representative consequences and normalization choices.
