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

The standalone `verify.py` uses Python's built-in arbitrary-precision integers and tuples representing \(\mathbb F_{41^2}\). It checks the quadratic-field nonsquare criterion, the four group-order tests for \(2+16w\), nonvanishing of its Frobenius difference, divisibility by \(83\), and the full \(41\)-coefficient identity
\[
X^{(1681^{41}-1)/83}\equiv1\pmod{X^{41}+X+2+16w}.
\]
The recorded result was:

```
lambda power obstructions: [(2, (40, 0)), (3, (20, 25)), (5, (18, 0)), (7, (15, 26))]
VERIFY_OK prime=41 primitive_constant_order=1680 irreducible_degree=41 nonprimitive_divisor=83 modular_identity=1 exponent_decimal_digits=131
```

The separate source `census.cpp` loops through all \(1681\) coordinate pairs, checks the primitive-element condition with the exact factorization of \(1680\), and evaluates the same order-\(83\) polynomial power for every primitive constant. Compile with `g++ -O3 -std=c++17 census.cpp -o census` (Boost.Multiprecision header required), then run `./census`. The result was:

```
CENSUS_OK primitive_constants=384 order_83_obstructions=64
```

The irreducibility argument is symbolic and holds because the Frobenius difference is nonzero; the computed exponent identity is an exact finite-field arithmetic witness, not a probabilistic or finite-sample proxy for an unverified universal identity. The census establishes an exhaustive count only for characteristic \(41\) and the particular \(83\) obstruction, not a classification of all reasons for nonprimitivity or a statement about other primes.
