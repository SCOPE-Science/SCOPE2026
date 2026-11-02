---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Just before vertex j arrives the i-subtree size W follows a two-color Pólya urn. Its first two rising factorial moments yield P(j descendant of i)=1/i and size-biased E[S_i(j)|A]=2j/(i+1); complement gives j/(i+1). A three-color Dirichlet–multinomial urn for vertices after j gives conditional cross-class covariance −n(n−j)ab/[j²(j+1)] and variance n(n−j)a(j−a)/[j²(j+1)]. As j is one initial singleton, averaging conditional Z yields covariances n(n−j)(i−1)/[(i+1)j(j+1)] on A and −n(n−j)/[(i+1)j(j+1)] off A. Their 1/i weighted cancellation is exact. Dependence is witnessed by S_i=n−i+1, where E[S_j]=(n−i+1)/(j−i+1)>n/j. i=1 or j=n gives deterministic subtree size. Independent complete parent-array enumeration n=4..7 verified each pair and signed formula exactly.

## originality

PASS

A broad Kuba 2006 multivariate framework handles several tagged node parameters, and Kuba–Panholzer give all factorial moments for a single tagged descendant subtree. These do not in the inspected material evaluate the conditional ancestor/nonancestor covariances or prove zero covariance with strict dependence for every interior pair. The general multivariate framework is substantial prior art and may contain an implicit derivative form, explicitly recorded as a residual risk. Best-of-knowledge qualified PASS.

## value

PASS

Nested versus disjoint descendant subtrees are natural dependent coordinates of a recursive growth tree. Exact zero covariance despite strict dependence, and conditioning that reveals opposite covariance signs, is a motivated structural warning against interpreting orthogonality as independence. Complete pairwise boundary classification is mathematically useful on its own.

The dated certificate retains the supplied scientific assessment, sources and limitations.
