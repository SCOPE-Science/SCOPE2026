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

# Verification of the valuation-profile theorem

The proof is analytic and uniform in the prime and exponent. The supplied standard-library-only program, `verify_primepower.py`, is an independent exact-arithmetic implementation of the determinant and two-by-two-rank criteria, with no tolerance thresholds. It reduces the determinant polynomial modulo the exact cyclotomic polynomial, rather than evaluating complex exponentials numerically.

Running `python verify_primepower.py` reproduces the counts in `verify_output.txt`; the terminal marker is `EXACT_VERIFY_OK`. Full exhaustive scans cover \(4,8,9,16\) (\(323{,}808\) distinct minor pairs), and independent seeded samples contain \(40{,}000\) minors each at \(25,27,32,49,125\). The script checks the exact profile counts and rank total identities. Finite tests are not proofs of the all-order theorem; the algebraic argument and profile enumeration in `RESULT.md` supply the proof.

No external audit or independent mathematical validation has been performed.
