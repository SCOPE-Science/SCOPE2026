---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

For triangular graph J(n,2), n>=5, Lipschitz-dual polar Q is defined on the canonical N=binom(n,2) vertex-coordinate zero-sum space, so primal inradius is the reciprocal of maximal centered Euclidean norm over 1-Lipschitz potentials. The oriented incidence inequality matrix is totally unimodular; strict convexity reduces maximizers to integral vertices, and diameter 2 reduces heights to {0,1,2}. Zero-height and two-height edges, viewed as edges of K_n, must have disjoint endpoint sets. The two-variable centered variance V(a,b)=a+b-(a-b)^2/N is dominated by maximal clique-edge counts in endpoint sets; the t>=n/4 derivative comparison and t<n/4 quadratic estimate force the balanced partition |S|=floor/ceil(n/2). This yields exact r_n=[(n-2)/n floor(n^2/4)]^-1/2, T_n balanced facet contacts and graph spread exactly 2(n-2)floor(n^2/4)/(n^2(n-1)). Centered indicator differences span the n-1 dimensional additive-edge subspace, leaving inball-center dimension N-n by strict slack at all other normals. Independent exhaustive standard Python enumeration of all 1133 normalized 3-level Lipschitz assignments for n=5 gave max N*norm²=36, 20 contacts; this is finite corroboration, with all-n proof by inequalities and linear rank.

## originality

PASS

Best-of-knowledge original exact graph-spread extremizers and full maximal-center dimension for Johnson triangular graphs n>=5; metric/free-space identification, spread definition, and complete multipartite comparison are known.

## value

PASS

Determines a natural graph invariant and all equality cases for the entire nontrivial triangular Johnson family, and additionally the codimension-n affine freedom of optimal Euclidean inball centers of the associated transportation polytope. This exact structural equality classification is useful independently of a downstream general theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
