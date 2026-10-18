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

The proof reconstructs all \(k+1\) classes from their common-neighbour counts and proves stabilizer transitivity, for every prime power \(q\) and integer \(k\ge2\).

Reproduce finite checks using `python3 check_refinement.py` and `python3 check_formula.py`. Both need only Python 3 standard libraries. The exhaustive finite test enumerates all \(35\) vertices for \((q,k)=(2,2)\), \(130\) for \((3,2)\), and \(1395\) for \((2,3)\), checks every disjointness edge, direct common-neighbour count, and the two-round stable partition. The independent arithmetic test checks \(210\) intersection cases across \(35\) configurations for prime powers \(2,3,4,5,7\) and \(2\le k\le8\), using Möbius inversion.

The recorded deterministic outputs are in `CHECK_OUTPUT.txt`. The programs supply finite corroboration and do not constitute an infinite proof or any external certification. The two-round theorem and sharpness for every \(k\ge3\) rest on the self-contained linear-algebra proof in `RESULT.md`. No independent audit has been performed.
