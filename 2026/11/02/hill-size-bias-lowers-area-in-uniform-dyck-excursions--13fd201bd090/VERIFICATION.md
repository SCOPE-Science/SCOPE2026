---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For every Dyck semilength n>=1, the first-return Catalan pair (B,C) with |B|=j is bijective both with ordinary path UBDC and with marked ground-level hill path BUDC. Thus the same uniform Catalan pair space gives uniform P and H-size-biased P* (since total marked hills=Cn), and A(P)-A(P*)=j>=0 under the stated sum-of-up-step starting heights convention. Pair counts give P(J=j)=Cj C_(n-1-j)/Cn, swapping pair pieces gives EJ=(n-1)/2. Therefore Cov(H,f(A))=E[f(A*)-f(A)]<=0 for every increasing f, strict for strictly increasing f when n>=2; covariance(H,A)=-(n-1)/2. Independently enumerated all Dyck paths n=1..8, validating area distributions, all threshold inequalities and exact rational covariance. This is a true all-n bijection; enumeration is supplementary. The n=1 zero difference boundary is covered.

## originality

PASS

Catalan first-return decomposition, hill counting, area q-Catalan recurrences and classic Dyck area bijections are prior. Elizalde–Deutsch’s fully inspected hills bijection does not state an all-increasing-functions hill-size-biased area dominance. Haug–Prellberg treat area weights; Kargin treats total peaks rather than ground-level hills. The explicit marked-hill transport and exact stochastic order are the assessed contribution, though Pergola’s potentially relevant 2001 area-bijection article remained inaccessible, so implicit prior equivalent statements are a real priority risk.

## value

PASS

The explicit transport is stronger than computing a covariance: it identifies the entire area distribution under a natural local root-hill size bias and proves stochastic dominance for every increasing observable, with sharp exact covariance and all-size Catalan difference law. It is a motivated structural combinatorial connection rather than arbitrary finite enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
