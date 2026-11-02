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

## Reproduction
Execute `python3 verify.py` using the Python 3 standard library. The script has no network dependency, fixed test limits, and no external data files. It derives multiplicative orders using Euler-totient reduction and modular exponentiation, checks the original gcd modulo \(n^2\), and separately calculates the prime-support threshold prediction.

Expected output:

```
VERIFY_OK odd_n=7500 wieferich_cases=1538 supports=6
EXAMPLES 21=defect3 63=non-Wieferich 1093=defect1093 1093^2=non-Wieferich
```

The verification range is all odd integers \(3\le n\le15001\), supplemented by six explicitly listed prime supports that include both known base-two Wieferich primes. The verifier also checks that decrementing any threshold exponent by one (when possible) restores a nontrivial defect. These tests are finite, not an exhaustive verification of the infinite theorem. The proof uses the multiplicative-order formula modulo odd prime powers and lifting the exponent.

## Source comparison and limits
The full eight-page text of arXiv:2610.28685v1 was inspected for the squarefree sufficient condition, local obstructions, and global asymptotics. The OEIS order test was compared as an equivalent computational reformulation. Full historical text of Franco–Pomerance (1995) was not available to complete that particular comparison, so mathematical priority remains subject to independent review. No independent audit or external certification has taken place.
