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

The standalone `verify_crown.py` uses Python 3 and only the standard library. Reproduction command: `python3 verify_crown.py`. Its completed check generated: `VERIFIED {'distances': 3256, 'exact_quadratic': 9240, 'float_quadratic': 27720, 'transitions': 11, 'endpoint_dimensions': 11, 'comparison': 11}`. The numerical scalar roots for \(n=5,6\) were approximately \(0.537048034477\) and \(0.384010941242\), respectively.

The program computes shortest paths independently, verifies the \(1,2,3\) distance classes, compares direct zero-sum quadratic forms against the three-eigenspace formula over random integer coefficient vectors, tests exact rational identities at \(p=0,1\), checks noninteger powers with explicit tolerances, and verifies eigenvalue signs, sharp bipartition witnesses, endpoint ranks, and a second-order asymptotic consequence. Tests cover finite parameter values only. The infinite-family correctness claim is justified by the algebraic block-matrix proof in `RESULT.md`, not by exhaustive computation.

The originality review compared the theorem against identifiable earlier matrix criteria, roundness work, and accessible related records. Full-text inspection of certain older papers was not possible, and historical uniqueness is not established. Independent audit remains unperformed.
