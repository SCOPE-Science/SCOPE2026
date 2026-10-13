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

# Verification record
The standalone `verify.py` uses Python 3 standard-library arithmetic. Run `python3 verify.py` from the directory containing this file and the program.

The program enumerates all nonzero isotropic rank-one dyads and removes scalar duplicates, directly multiplies matrices to build word-product multiplicities, and compares **every** zero and rank-one target with the closed formula. For fields of orders 2, 3, 4, and 5 it tests dimensions two through four as permitted by the explicit cases. The degree-two extension field of order four is represented by the irreducible polynomial \(z^2+z+1\). The observed completion marker is `VERIFY_OK`.

Checked field–dimension pairs and word lengths are: \((2,2)\) to length five, \((3,2)\) to length five, \((4,2)\) to length four, \((5,2)\) to length four, \((2,3)\) to length four, \((3,3)\) to length three, \((4,3)\) to length three, and \((2,4)\) to length three. Each case separately confirms the size of the factor orbit, the total number of words, the zero fiber, all rank-one target fibers, and absence of other produced ranks. A symbolic diagonalization verifies the general formula; the finite tests alone do not establish arbitrary field size, dimension, or word length.

No independent audit or independent validation has been performed.
