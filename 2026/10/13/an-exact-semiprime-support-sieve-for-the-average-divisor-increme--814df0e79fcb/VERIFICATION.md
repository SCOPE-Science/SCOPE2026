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

The attached `verify.py` independently constructs a smallest-prime-factor table and the sum-of-divisors function by an additive divisor sieve through \(2{,}000{,}001\).

For each squarefree semiprime \(2\le n\le2{,}000{,}000\), it verifies the exact equivalence between the original equation and \(4\sigma(n+1)=5(p+1)(q+1)\), then checks that every solution obeys the support and residue restrictions. The \(p=3\) shifted-argument condition is separately recomputed at every such prime pair. It also verifies explicit witnesses at \(753\) and \(148173\), and the finite critical pairs in the \(p=7\) exclusion.

The computation is a finite consistency check. The proof of the unbounded exclusion and the exact \(p=3\) parametrization is entirely symbolic.
