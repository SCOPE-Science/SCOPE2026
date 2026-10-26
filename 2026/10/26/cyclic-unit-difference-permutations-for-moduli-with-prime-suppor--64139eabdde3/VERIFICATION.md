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

The theorem is proved algebraically in `RESULT.md` by a primitive-root construction modulo \(3p\) and a lifting lemma from \(m\) to \(mq\), for an odd prime \(q\mid m\). The script `verify.py` is standard-library-only and is supplementary, not an exhaustive infinite proof.

To replay: use `python3 verify.py` with Python 3. The expected line is `VERIFY_OK moduli 137 largest_n 89373 total_units_and_edges 1041828`.

The script checks prime inputs, generates all claimed cyclic vertices, checks equality with the exact reduced residue set and checks that the cyclic oriented differences give that same set. Every closing edge is included. The verification covers all claimed parameters up to the indicated finite bounds, not unbounded primes or exponents. The general proof rests on the invertibility of the two difference slopes in the lifting lemma and on the nonvanishing of the two CRT factors in the base construction.
