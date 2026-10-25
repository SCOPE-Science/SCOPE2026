---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For uniformly random ranking sign vectors, the pair-sign covariance from 3-label enumeration is T=(I+B^TB)/3; BB^T=nI-J determines its gradient and cycle eigenvalues. Conditioning permutation sign to be even alters no moment supported on <=4 labels if n>=6 (swap two unused labels). For n=4,5, one-point means vanish but disjoint-edge covariance obtains the explicitly oriented alternating matrices H4/3 and H5/15. Direct exact enumeration of all n4,5,6 permutations independently verifies these parity corrections and det(C)/det(T)=64/125,64/125,1. The formula's stated H4/H5 matrix identities yield the spectra and C positive definiteness, proving full affine dimension. The alternating relabeling group acts transitively by orthogonal signed-coordinate permutations, so all generating vertices have Mahalanobis norm squared d; averaging (including arbitrary centers) plus trace-AMGM forces the unique containing ellipsoid shape d*C. Determinant gives volume ratio 8/(5 sqrt(5)) for n=4,5, and 1 for n>=6. The Euclidean smallest enclosing ball follows from equal vertex norms sqrt(d) and mean zero. Universal n>=6 relies on the parity involution, not finite n6 enumeration.

## originality

PASS

Qualified best-of-knowledge originality for the precise final theorem and its stated parameter domain. The four named implication comparisons discriminate known mathematical inputs from the sharp new increment; an unindexed equivalence remains possible. It supplies the potential/circulation decomposition of unrestricted P_n, but parity restriction changes second moments in n4/n5, so it does not imply the new ellipsoid without new alternating-parity correction.

## value

PASS

Parity restriction of the classical linear-ordering polytope is a natural alternating-group orbitope. The exact covariance and minimum-volume ellipsoid exhibit a genuinely surprising finite dimensional cutoff: removing half the vertices affects the optimal Euclidean-volume ellipsoid only in n4/n5, and in both by identical nontrivial ratio. The exact classification is useful for ellipsoid approximation of ranked-data polytopes and does not require a downstream theorem to be valuable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
