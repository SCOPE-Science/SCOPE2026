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
# Reproducibility

Run `python3 verify.py` using Python 3 standard library. The code directly implements the four-dimensional quotient-ring multiplication, formal derivatives and bracket, and finite-field arithmetic with irreducible modulus \(T^2+T+1\) for \(\mathbb F_4\). It enumerates the full four-parameter bracket space, checks alternation and Jacobi on all basis triples, and enumerates all invertible linear parts and quadratic corrections of associative automorphisms. It constructs the actual action from the differentiated Jacobian rather than assuming the theorem's normal-form action.

Verified outputs:

```
char2_GF_2: PASS, all 16 brackets satisfy Jacobi; 24 automorphisms; 6 disjoint exact isomorphism orbits
char2_GF_4: PASS, all 256 brackets satisfy Jacobi; 2880 automorphisms; 12 disjoint exact isomorphism orbits
VERIFY_OK
```

All observed orbits have the stated sizes and partition the full bracket set. The arbitrary-field classification and all-parameter finite-field formulas rest on the symbolic proof. No independent audit or machine-checked infinite proof has been performed.
