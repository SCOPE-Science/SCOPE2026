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

Run `python3 verify.py` with the standalone standard-library script in this package. The executed checks verify local residue counts for ten primes through 31, exact binary square-residue counts and their recurrence at depths 3 through 13, all 44,100 residue classes of the three-prime CRT subcase, the exact ten-prime rational fraction, and 50 positive explicit CRT witnesses. The root-lifting proof, CRT implication for all sufficiently large integers, and the density statement are symbolic and not implied by a bounded experiment. The review performed here is same-model only; independent audit has not been performed.
