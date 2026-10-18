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

# Arithmetic verification and proof boundary

The stated all-parameter result is proved by two applications of Lucas's theorem combined with the necessary Dold congruence. The first residue is \(p-r\) at a prime index; it is nonzero off the parameter diagonal. The second is \(s(s-1)/2\) at twice an odd prime; it is nonzero for every diagonal parameter \(s\ge2\). Both congruences hold for infinitely many arbitrarily large primes, so no fixed positive scaling factor can repair the failure. The sole remaining constant sequence has a direct dynamical realization.

The reproducible finite checker is `artifacts/verify.py`. Run `python3 artifacts/verify.py` with a Python 3 interpreter; the observed output is in `artifacts/verify_output.txt`. It verifies 2,880 exact integer values, 1,942 prime-index Lucas residues, and 203 diagonal twice-prime Möbius residues, as well as 200 terms of the singleton sequence. These tests are spot checks, not exhaustive in \(p,r,n\).

All source references and the mathematical limitations are provided in `RESULT.md`. No external validation or proof-assistant certification is claimed.
