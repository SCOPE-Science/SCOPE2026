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

The theorem is proved symbolically in `RESULT.md`. The key checks are:

- \(B_j^p/B_{j+1}\in1+p\mathbb Z[[x]]\) by the coefficientwise Freshman's-dream congruence and unit division.
- For \(U\in1+p\mathbb Z[[x]]\), binomial induction gives \(U^{p^r}\equiv1\pmod{p^{r+1}}\) for every \(r\ge0\), including \(p=2\).
- The exact telescoping identity has exponents \(p^{2a-j-1}\), so the weakest factor has modulus \(p^{a+1}\).
- At \(m=p^{a-1}\), the first positive coefficient of \(R_{a-1}^{p^a}\) is exactly \(-p^{a+1}\); earlier factors are already \(1\) modulo \(p^{a+2}\), and \(B_a^{p^a}\) has no positive coefficient at or below degree \(m\).
- Division by \(A\) preserves the nonzero residue modulo \(p^{a+2}\) at degree \(m\) because the numerator's lower coefficients are divisible by \(p^{a+2}\) and \(A^{-1}(0)=1\).

`artifacts/verify.py` performs exact integer expansions through degree \(24\) for seven low-parameter cases. Replayed output:

`VERIFY_OK cases=7 sharp=[(2, 1, 1, -4, 2), (2, 2, 2, 88, 3), (2, 3, 4, 478480, 4), (3, 1, 1, -9, 2), (3, 2, 3, -75843, 3), (5, 1, 1, -25, 2), (7, 1, 1, -49, 2)]`

The finite expansion does not certify the infinite theorem; it only checks representative coefficients against the symbolic proof.
