---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Deleting a conditioned leaf gives a uniform (n-1)-vertex Cayley tree and uniform attachment. Splitting the marked leaf into root versus nonroot cases yields the stated exact covariance p_n[2n-1+(n-3)b_{n-1}-n b_n]. Path-counting produces w_n and b_n; integral remainder and Laplace expansion w_n=-3/(4n)-11/(16n^2)+O(n^{-3}) imply b_n=n/2+1/8+1/(32n)+O(n^{-2}), hence covariance 1/(8e)+O(1/n). Conditional bipartite Prüfer occupancy is correctly distinguished from novelty. Independent full Cayley enumeration at n=3..6 reproduces exact covariance 0,3/32,144/3125,665/11664.

## originality

PASS

Best-of-knowledge comparison of statements and mathematical implications; the named comparisons identify prior facts without conflating them with the claimed new invariant or construction. Historical-priority risks remain explicit.

## value

PASS

The nonzero unscaled mixed covariance 1/(8e) refines two natural statistics of a canonical random-tree model, quantifying dependence invisible from known individual Gaussian-scale fluctuations; exact n formula is useful for random-tree comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
