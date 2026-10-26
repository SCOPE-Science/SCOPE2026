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

The analytical certificate consists of identity (1), its symmetric specialization (3), and the prime-local two-case argument in `RESULT.md`. This gives a proof for **all** admissible bases, multipliers and lengths. The displayed prime-power exponents \(a,q,t\) are ordinary \(\ell\)-adic valuations, not heuristic numerical parameters. The proof treats primes shared by \(b\), \(n-1\) and \(n+1\), including \(\ell=2\).

To replay independent finite computations of **examples only**, run `python3 verify.py`. It enumerates 409,838 symmetric bounded-carry tuples for \(2\le n\le12\), \(n<b\le40\), and \(3\le k+1\le8\), reconstructs integer digits from the digit identity, checks leading/trailing nonzero digits, checks the exact multiplication equality and every carry equation. Exactly 384 tuples give palintiples; each has carries from \(\{0,n-1\}\) and \(n+1\mid b\). It also checks the two classical base-10 examples.

The check is exhaustive only for its stated finite parameters and does **not** certify infinite novelty or the theorem's universal quantifiers. No independent proof audit was performed.
