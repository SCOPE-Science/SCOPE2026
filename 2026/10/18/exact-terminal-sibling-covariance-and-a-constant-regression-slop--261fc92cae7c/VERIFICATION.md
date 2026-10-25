---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For rooted uniform recursive attachment P_t uniform in {1,...,t-1}, terminal means no children (root excluded). For an old nonroot terminal indicator I_v and parent terminal-child counts ell_v, the exact increments are Delta L=1-I_V and Delta C=ell_V-I_V(ell_{P_V}-1), giving conditional moments E Delta L=1-L/n, E Delta C=(L-2C)/n, and E(Delta L Delta C)=L/n. Expand L^2 and LC to obtain four triangular moment recurrences; n=2,3 bases produce E L=n/2, E C=n/6 (n>=3), Var L=n/12 (n>=3), E LC=n^2/12+n/8 and Cov(L,C)=n/8 (n>=4). The individual sibling-pair probability for 2<=i<j<=n is (i-1)/((n-1)(n-2)), from shared-parent choice, exclusion of later attachments to i, and exclusion of both children after j. Independent exhaustive enumeration of all rooted recursive parent vectors for n=2..7 recovered covariance 0,1/4,n/8 and the age-index probabilities; these finite tests corroborate, not prove, all n. The least-squares regression slope is n/8 divided by n/12 =3/2, not the conditional expectation slope.

## originality

PASS

Best-of-knowledge: the mixed terminal-sibling pair statistic on uniform recursive attachment is not supplied by the inspected leaf-count or degree-count results; this does not certify historical priority.

## value

PASS

An exact all-n mixed covariance measures dependence of global terminal abundance on sibling aggregation, a genuine local-versus-global random recursive tree question. The n-independent least-squares coefficient and birth-order-resolved probabilities give structural, reusable identities beyond the classical one-variable leaf-count mean/variance. Rooted terminal and unordered-pair conventions are essential; no full joint law or monotonic regression is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
