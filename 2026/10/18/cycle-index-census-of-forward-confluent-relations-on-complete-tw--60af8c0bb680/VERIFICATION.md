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

# Reproduction and verification

`verify.py` is a complete standalone Python 3 script requiring only the standard library. Run `python3 verify.py` in the same directory; it prints `VERIFY_OK` only after all computations and assertions finish.

The checker calculates the labelled formula and the cycle-type Burnside formula using exact arbitrary-precision integers and rational numbers. For \((p,q)=(2,2)\), \((2,3)\), \((3,2)\), \((3,3)\), and \((2,4)\), it obtains respectively \((11{,}401,3{,}067)\), \((1{,}252{,}925,111{,}183)\), \((3{,}771{,}875,324{,}244)\), \((847{,}519{,}079,24{,}206{,}336)\), and \((495{,}407{,}161,10{,}719{,}206)\) for (labelled, isomorphism) counts.

The first independent test evaluates the published FC condition directly on **every** binary relation for six small profiles of total size at most four, including the essential \((2,2)\) example. The next independently loops through every assignment of bottom-source rows and every possible single top-source row, tests the original FC condition rather than the support formula, and raises the allowable-row count to the number of upper worlds. This agrees with the labelled formula at \((2,2)\), \((2,3)\), and \((3,2)\). Finally, for \((1,3)\), \((2,2)\), and \((2,3)\), the program enumerates every relation fixed by each nonidentity order permutation using its ordered-pair orbits; it tests FC on each and compares those fixed counts with the derived cycle formula. Combining the independently counted identity fixed set with the nonidentity fixed sets recovers the isomorphism count by Burnside's lemma.

The exact counting theorem follows from the proof in `RESULT.md`. These finite computations are cross-checks and do not certify either infinite cardinalities or originality. They do not replace independent external mathematical review.
