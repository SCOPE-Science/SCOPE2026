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

# Verification notes

`verify.py` is a standard-library Python program. Run it with `python3 verify.py` from the directory containing the file. Its emitted stdout is preserved in `verification_output.txt`.

The program checks that every template contains disjoint right-angle three-cell configurations. Its independently defined `exact_gpack` dynamic program enumerates all triples of cells with exactly two adjacency pairs, and recursively either leaves the first available cell unused or packs it in any available right-angle triple. This computes an exact maximum on each finite tested board, rather than trusting the constructed maximum.

All six base bricks are independently checked for optimum size. All 3,481 pairs \((m,n)\) with \(2\le m,n\le60\) are constructed and checked for membership, disjointness, and count \(\lfloor mn/3\rfloor\). The independent solver checks 14 smaller boards up to 21 cells. The captured run ends with `ALL_CHECKS_PASSED`.

The proof for all \(m,n\ge2\) is the explicit decomposition and upper bound in `RESULT.md`. Exhaustive finite computations do not imply the infinite statement by themselves, and the verifier does not establish originality, exhaustive literature coverage, or independence of review.
