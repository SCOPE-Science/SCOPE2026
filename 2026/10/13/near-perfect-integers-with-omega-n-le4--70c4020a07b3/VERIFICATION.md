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

The proof was reconstructed from the definition \(\sigma(n)=2n+d\) with \(0<d<n\) and \(d\mid n\), partitioning all possible exponent patterns for \(\Omega(n)\le4\). Critical exact checks include:

- \(\Omega=3\): the only surviving branches are \(4p\) with \(p=3,5\) and \(2p^2\) with \(p=3\).
- \(\Omega=4\): the \(8p\) branch yields \(p=3,5,7,11,13\); the \(4p^2\) branch yields only \(p=7\); squarefree four-prime integers are eliminated by a \(2\)-adic divisibility mismatch.
- For \(2r^2s\), exact divisor equations leave only \((r,s)=(3,13)\) and \((5,13)\), producing \(234\) and \(650\).
- For \(4rs\), the positivity inequality \((r-7)(s-7)<56\) and exact divisor equations eliminate every prime pair.

Running `verify.py` gives:

`VERIFY_OK expected=11 scan_limit=1000000 max=650`

The scan through \(10^6\) is regression evidence only. No finite bound is used in the universal proof.
