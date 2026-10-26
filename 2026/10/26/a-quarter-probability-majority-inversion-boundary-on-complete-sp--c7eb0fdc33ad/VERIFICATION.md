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

# Verification evidence
Run `python3 check.py` from the directory containing the standalone verification program. It constructs the complete split adjacency relation directly, independently computes every vertex's closed-neighborhood majority (including tie retention), and compares the result with the double-binomial inversion count for each admissible tested size. The check completed with `PASS: 114408 exact initial profiles, formula agrees with direct vertex-by-vertex voting`. The cases cover \(2\le c\le7\), \(1\le\ell\le9\), odd \(N=c+\ell\le16\), and both larger-core and larger-periphery regimes.

The program also prints exact rational inversion probabilities at the same-order boundary for \(c=2,4,6,10,20,40,80,160\), including \(R(4,5)=25/256\). Numerical convergence along these examples is a diagnostic only. The proof of the all-size formula is the case split on closed neighborhoods, and the proof of the limiting law uses the binomial central limit theorem and the exact angular formula for correlated Gaussians. Neither is replaced by computation. There is no claim of independent external validation.
