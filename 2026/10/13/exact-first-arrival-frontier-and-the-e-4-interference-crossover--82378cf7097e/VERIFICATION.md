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
The proof is analytic and uses only the exact Grover coin entries, shortest-path counting, orthogonality of final coin sectors, and Stirling's formula.

The accompanying `verify.py` performs an independent finite replay. It rescales amplitudes by \(\sqrt n\), so every amplitude remains rational. For each \(2\le n\le7\) and every \(1\le w\le n\), it evolves the full coined state for exactly \(w\) steps, selects one vertex of Hamming weight \(w\), and compares the exact rational point probability with
\[
\frac{w!(w-1)!4^{w-1}}{n^{2w-1}}.
\]
It also checks the exact ratio against the simple classical first-arrival probability \(w!/n^w\).

Finite replay is not evidence for the universal quantifiers; it only checks implementation and algebra on small cases. The asymptotic crossover is proved from Stirling's formula, not from numerics. The critical subexponential scaling at \(\rho=e/4\) is intentionally left outside the claim.
