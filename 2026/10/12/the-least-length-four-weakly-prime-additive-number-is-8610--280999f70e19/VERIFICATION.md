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

`verify.py` performs the exact finite search used in the proof. It builds a smallest-prime-factor sieve through \(8610\), obtains every distinct prime divisor of each integer, enumerates all positive powers below that integer for each chosen prime base, and checks every three- and four-base Cartesian product with exact integer addition.

The packaged replay returned:

`VERIFY_OK first_length4=8610 three_reps=0 four_reps=1 factor_primes=2,3,5,7,41 witness=3^8+5^2+7^3+41^2`

The finite search proves only the stated least-element boundary through \(8610\). It is not evidence for a density or infinitude claim. The separate symbolic congruence argument rules out two-term representations for every integer, so the exhaustive three-/four-term comparison suffices to identify length exactly \(4\).
