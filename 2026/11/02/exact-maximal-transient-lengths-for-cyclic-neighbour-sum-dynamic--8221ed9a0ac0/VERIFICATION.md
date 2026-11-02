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
# Reproducible verification

Run the included `verify.py` using Python 3. The program enumerates 65 exact nilpotency indices for relevant polynomial quotients, and independently enumerates 87 complete finite functional graphs for small modules (up to 50,000 states each). The expected output is:

`VERIFY_OK prime_power_cases=65 whole_state_cases=87 examples=8:12:8,9:6:5,12:5:2,25:10:9,16:8:20`

The verifier uses exact integer modular arithmetic only and does not download dependencies. It validates sample calculations and two independent implementations of the maximum transient. It cannot certify infinitely many dimensions, moduli, or primes. The mathematical argument proving those universal quantifiers is the proof in `RESULT.md`, particularly the exact prime-power filtration/nonvanishing lemmas. The finite program therefore serves as a reproducibility check and catches indexing or normalization errors.
