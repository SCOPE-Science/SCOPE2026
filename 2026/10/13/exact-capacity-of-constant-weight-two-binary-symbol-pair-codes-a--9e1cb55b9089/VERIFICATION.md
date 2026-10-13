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

# Reproducibility and mathematical scope

Execute `python3 verify_pairweight2.py` in the directory containing this file and the verifier; only the Python 3 standard library is needed.

The program constructs optimal graphs for every integer \(3\le n\le120\). For all these lengths it checks the cardinality \(\lfloor n\lfloor n/2\rfloor/2\rfloor\) and that every vertex-neighborhood is a cyclic independent set. For \(n\le15\), it also builds actual pair-read vectors and verifies the minimum pair-distance condition directly, checking every unordered pair of codewords.

An independent exact maximum-independent-set search over the entire conflict graph establishes the optimal cardinalities for \(n=3,4,\ldots,11\) without relying on the constructive families. The expected sequence is \(1,4,5,9,10,16,18,25,27\). On successful completion the script prints `VERIFY_OK`.

The all-integer theorem is proved by the degree inequality and the explicit constructions in `RESULT.md`; finite exhaustive searches do not establish the infinite assertion by themselves. No independent external audit has been performed.
