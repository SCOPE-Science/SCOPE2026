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
# Reproducible checks
Run `python3 verify.py` using Python 3 standard library. The program builds exact arithmetic for the prime fields of orders two and three, and for \(\mathbb F_4=\mathbb F_2[t]/(t^2+t+1)\). For every prescribed trace vector it exhaustively enumerates tuples and independently checks generation by iterative word-span closure, rather than by substituting the theorem's count or recognizing a precomputed orbit.

Tested counts: \(q=2,m=2\): 256 tuples, 24 generating tuples per each of 4 trace pairs, total 96. \(q=3,m=2\): 6561 tuples, 432 per each of 9 trace pairs, total 3888. \(q=4,m=2\): 65536 tuples, 2880 per each of 16 trace pairs, total 46080. \(q=2,m=3\): 4096 tuples, 336 per each of 8 trace triples, total 2688. Every test completed and yielded `VERIFY_OK_TRACE_GENERATION`.

The arbitrary-field and arbitrary-arity claims are proved by the algebraic counting and subdirect-product arguments, not by finite enumeration. There has been no independent audit.
