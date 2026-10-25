---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

Marking disjoint r and s cycles in a derangement gives E C_r=a_{n-r}/(r a_n) and E C_rC_s=a_{n-r-s}/(rs a_n), hence the determinant formula. With B_{t,h}=sum_{j=1}^h(-1)^{j+1}/(t+j)!, subtracting alternating partial sums gives (-1)^m determinant=a_{m+r}B_{m,s}-(-1)^r a_mB_{m+r,s}. The first term dominates strictly if r is even by B_{m+r,s}/B_{m,s}<=1/[(m+1)(m+3)] and the elementary a_k bounds; for odd r both contributions have positive sign, including m=1. The leading term asymptotically is e^-1/(m+1)!, so division by rs a_n^2 yields e. At n<r+s the joint product vanishes; n-1 cycle class has zero mean. Independent exact-rational 2,420 shift-determinant cases and derangement examples n=5 (30/121), n=6 (-432/2809) reproduced claimed signs; analytic argument establishes all n.

## originality

PASS

Da Silva/Jamshidpey/Tavaré arXiv:2006.04840 Section 2.1 Eq. (6) already gives the general joint factorial-moment identity for conditioned Ewens cycle counts, and the determinant covariance formula is a direct substitution; both are expressly credited. The submitted nontrivial theorem is the strict parity sign for every finite n,r,s plus the sharp factorial coefficient e. The accessible primary text treats moments and Poisson limits, not an alternating determinant positivity theorem or that leading oscillation coefficient. A failed search alone does not prove novelty; the best-of-knowledge comparison rests on the specific prior formula and the additional inequality required.

## value

PASS

Conditioning random permutations to have no fixed points breaks the zero pairwise covariance enjoyed by unconstrained cycle counts. The exact sign oscillation with unused-label parity, nonvanishing and factorially small sharp magnitude provide a natural complete finite-size dependence classification for these fundamental cycle statistics, which does not follow as a routine sign statement from an arbitrary factorial-moment identity without a positivity argument.

The dated certificate retains the supplied scientific assessment, sources and limitations.
