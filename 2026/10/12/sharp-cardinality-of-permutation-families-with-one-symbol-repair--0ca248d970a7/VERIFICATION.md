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

# Executable verification and scope

Run `python verify.py` and `python verify_n5.py` from the supplied file directory using Python 3.9 or later and no third-party modules. Both programs were executed successfully from the exact files included with this finding.

`verify.py` enumerates all explicitly constructed families for each \(2\le n\le11\), checks every word is a permutation, checks fixed one-coordinate recovery for each coordinate of each word, verifies uniqueness, and compares the exact count to the claimed formula. Results: sizes \(2,3,8,10,48,56,384,432,3840,4224\) for lengths \(2\) through \(11\).

`verify_n5.py` independently enumerates \(4^5=1024\) distinct fixed-observer maps in length five; reduction by all \(120\) coordinate permutations gives thirteen dependency-map orbits. For each orbit a compatibility graph on all \(120\) five-symbol permutations is constructed independently of the explicit family. Exhaustive bitset clique search with proper vertex-coloring upper bounds excludes an eleven-word code. This is a finite exact computation; no timeout, partial census, or inferred conclusion is used.

The arbitrary-length proof relies on component structure and explicit maps, not on these finite checks. Neither program provides an independent audit or a formal verification of all lengths.
