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

The proof-critical finite statement is the emptiness of the valuation-support set after recursive unique-coordinate elimination for every prime at most \(50000\).

Run:

`python verify.py`

Expected output:

`VERIFY_OK cutoff=50000 primes=5133 rounds=[5074, 51, 5, 3] prime_factors=8367 max_factor=6154180859137036001`

The verifier performs the following checks from `certificate.json` rather than trusting a log: it regenerates the \(5133\) primes through \(50000\); checks that the certificate has exactly those keys; verifies every factorization of \(p^5-1\) by exact integer multiplication; verifies primality of every displayed factor using the deterministic seven-base Miller--Rabin criterion valid below \(2^{64}\); and replays every uniqueness witness before deleting its prime. All primes are deleted after four rounds.

The computation proves only the stated finite support cutoff. It is not evidence for global injectivity beyond \(50000\), and it does not search a bounded range of values of \(m\) or \(n\).
