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

# Verification

Run `python verify.py` with Python 3.10 or later and no non-standard packages. The verifier independently generates tree permutations, builds each inversion graph, searches all nonempty vertex subsets for a smallest closed-neighborhood dominating set, computes diameter by breadth-first search, and compares both statistics against the binary-run formula for every bit word of length \(n-2\) with \(3\le n\le11\). It checks exactly \(1{,}022\) such words. It separately evaluates the iid-cycle moment decomposition with exact rational fractions, recovering density \(2/7\), variance slope \(18/343\), covariance slope \(3/49\), diameter variance slope \(1/4\) and determinant \(45/4802\).

The verifier completed successfully for the included source. These are finite identity checks and symbolic rational checks, not exhaustive proofs of the asymptotic central limit or moment convergence. The unrestricted proof uses the closed-neighborhood caterpillar optimization and iid renewal-reward arguments given in RESULT.md. External independent scientific audit has not been performed.
