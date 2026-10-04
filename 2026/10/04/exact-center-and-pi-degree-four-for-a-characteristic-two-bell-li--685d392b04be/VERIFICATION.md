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

The proof uses only symbolic identities in the Ore extension and the PBW basis.

1. With \(\delta(y)=z\) and \(\delta(z)=\gamma y\), verify \(A_\gamma=K[y,z][x;\delta]\).
2. In characteristic \(2\), compute \((\operatorname{ad}x)^2\) on \(y,z\) and verify centrality of \(x^4+\gamma x^2\).
3. Reduce uniquely to degree at most \(3\) in \(x\) over \(K[y,z,x^4+\gamma x^2]\).
4. Expand commutators with \(y,z\). The \(x^3\) coefficient first vanishes, then the remaining two coefficients are killed by the nonzero determinant \(\gamma(z^2+\gamma y^2)\).
5. Write \(K[y,z]\) freely over \(K[y^2,z^2]\) with basis \(1,y,z,yz\) and solve \(\delta(r)=0\), obtaining only \(K[y^2,z^2]\).
6. Reduce PBW exponents modulo \((2,2,4)\) to obtain exactly \(16\) center-basis classes.
7. Central localization remains a domain and has dimension \(16\) over its center field, so it is a central division algebra of degree \(4\).

Finite computation is not used as a substitute for any infinite argument. The limitations are exactly those stated in RESULT.md.
