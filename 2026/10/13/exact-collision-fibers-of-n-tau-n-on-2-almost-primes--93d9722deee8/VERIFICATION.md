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
The proof was reconstructed from the complete factorization-type list for inputs with \(\Omega(n)\le2\): primes have \(\tau=2\), prime squares have \(\tau=3\), and squarefree semiprimes have \(\tau=4\). Ordering a nontrivial collision forces exactly three comparisons, all resolved symbolically in `RESULT.md`.

The bundled `verify.py` independently enumerates the stated domain through \(10^6\), computes all fibers of \(n+\tau(n)\), and checks both directions of the classification. Its recorded output is:

`VERIFY_OK limit=1000000 low_omega_inputs=288533 nontrivial_fibers=21909 exceptional_4_5=True theorem_mismatches=0 max_fiber=2`

The finite scan is regression evidence only and is not an exhaustive proof of the infinite theorem. No assertion is made for inputs with \(\Omega(n)\ge3\) or for infinitude of the prime pattern \(qr+2\).
