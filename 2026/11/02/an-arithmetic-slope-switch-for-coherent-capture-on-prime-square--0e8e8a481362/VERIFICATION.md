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

The self-contained checker `verify_torus.py` has no external Python dependencies and can be run with `python3 verify_torus.py`. Its recorded stdout is provided as `verification_output.txt`. It tests all line slopes for each of nine primes through \(29\), using exact combinatorial Fourier-orbit ranks, and independently tests physical-site adjacency block-Krylov ranks for selected slopes at primes \(5,7,11,13\), each modulo two different primes. Actual rank values are in the output file. The checks are finite and do not prove the theorem for untested primes: the proof is in `RESULT.md`. The classification of absorption is an infinite-time statement and does not bound capture times. Independent audit has not been performed.
