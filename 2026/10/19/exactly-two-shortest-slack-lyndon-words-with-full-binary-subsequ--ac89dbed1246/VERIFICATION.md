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

The supplied Python 3 file `CHECK.py` implements two independent decision procedures for binary subsequence universality: direct membership tests for every length-\(k\) pattern, and counting greedy full-alphabet arches. Both procedures agree on all binary inputs with lengths \(2k\) and \(2k+1\) for \(k=1,\ldots,6\).

An exhaustive list of all words of length \(2k+1\), for \(k=1,\ldots,9\), confirms that the number of universal hosts is \((k+2)2^k\) and the Lyndon universal subset is precisely the two formula words. Exhaustive tests at the optimal absolute length \(2k\), for \(k=2,\ldots,9\), find no Lyndon universal word. Additional checks of the two witnesses were performed at \(k=10,15,20,30,50,100,200\).

The execution output ended in `ALL CHECKS PASSED`. Every assertion can be replayed with `python3 CHECK.py` in a standard Python 3 installation. These tests alone cannot prove the unbounded claim: the proof is the arch/rotation argument in `RESULT.md`.
