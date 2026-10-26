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

# Exact verification
Run each of the following standalone scripts using Python 3:

```sh
python3 verify_over_prime_field.py
python3 verify_over_extension.py
```

The first computes the coefficient's four essential powers over \(\mathbb F_{41}[u]/(u^2-3)\) and the exact remainder of \(Z^E\) modulo the monic degree-\(82\) polynomial \(G\). Observed output includes:

```
PRIMITIVE_LAMBDA_TESTS {2: (40, 0), 3: (20, 25), 5: (18, 0), 7: (15, 26)}
EXPONENT_DIGITS 131 EXPONENT_BITS 433
CERTIFICATE_OK p=41 lambda=2+16u u^2=3 irreducible_degree=41 nonprimitive_factor=83
```

The second uses an independent representation of the root in the degree-\(41\) quotient of a quadratic finite field and yields:

```
CERTIFICATE_OK independent_extension_ring p=41 degree=41 divisor=83
```

The checkers use exact modular integer arithmetic only. Correctness of the symbolic reduction and field structure is explained in the accompanying proof. The computation is not an infinite search and claims no results for other primes. Independently commissioned external validation has not been performed.
