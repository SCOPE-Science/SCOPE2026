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

# Exact verification and limits

The general proof is algebraic: cyclotomic linear disjointness over a dyadic field reduces a hypothetical zero minor to equal grouped coefficients, reduction modulo a prime over two forces each of six determinant exponent multiplicities to be even, and a two-parameter finite-field argument rules that out for every odd prime. No finite computation is used as a substitute for the universal proof.

The standalone `verify.cpp` was compiled with `g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify.cpp -o verify` and executed. It calculated grouped cyclotomic determinant coefficients exactly (Gaussian integers for a cyclic order-four factor, integers for a Klein-four factor). Every normalized admissible three-by-three minor was nonsingular:

| Auxiliary group | Odd prime | Normalized minors | Singular |
|---|---:|---:|---:|
| \(C_4\) | 3 | 256 | 0 |
| \(C_2\times C_2\) | 3 | 256 | 0 |
| \(C_4\) | 5 | 9,216 | 0 |
| \(C_2\times C_2\) | 5 | 9,216 | 0 |
| \(C_4\) | 7 | 57,600 | 0 |
| \(C_2\times C_2\) | 7 | 57,600 | 0 |
| \(C_4\) | 11 | 518,400 | 0 |

The exact total is **652,544 normalized minors**. The code independently checks the parity obstruction for **81,658 ordered normalized pairs** over twenty-six odd primes through \(103\), again with zero failures. Both enumerations are finite diagnostics. The all-prime, all-dyadic-group statement rests on the proof, including cyclotomic irreducibility and the general parity lemma.

No computational tests are claimed for arbitrary finite groups or unbounded primes. No independent external mathematical audit has been conducted.
