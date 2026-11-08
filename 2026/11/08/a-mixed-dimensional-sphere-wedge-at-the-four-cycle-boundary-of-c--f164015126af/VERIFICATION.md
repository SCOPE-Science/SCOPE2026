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

# Verification of the finite neighborhood-complex classification

The included script `verify_k5c4.py` requires Python 3 and no third-party packages. Run `python3 verify_k5c4.py` from the directory containing the file. The exact standard output is recorded in `verification_output.txt`.

The computation exhaustively tests all \(2^{20}=1,048,576\) vertex subsets by a common-neighbor predicate and independently constructs subfaces of the twenty explicit open neighborhoods. It compares the two complete sets and obtains 950 distinct nonempty faces with face vector \((20,130,360,300,120,20)\). The deterministic matching has 446 pairs and one, 53, and four critical cells of dimensions zero, two, and three. An oriented Hasse diagram with 3,260 cover incidences is topologically sorted to establish acyclicity, rather than relying on critical counts alone.

The verifier calculates the full integral Morse boundary between the critical three-cells and critical two-cells using exact signed gradient recursion, then independently cancels all 446 matched pairs using unit pivots in the original integer chain complex. Both leave zero differentials. The absence of critical one-cells and Hurewicz \(\pi_2\cong H_2\) for the simply connected two-skeleton turn these zero attaching degrees into the stated wedge homotopy type. The alternating face sum equals \(50=1+53-4\) as an auxiliary consistency check.

This is an exhaustive verification of a *fixed finite object*, not a numerical survey of an unbounded family and not a claim of independent mathematical audit.
