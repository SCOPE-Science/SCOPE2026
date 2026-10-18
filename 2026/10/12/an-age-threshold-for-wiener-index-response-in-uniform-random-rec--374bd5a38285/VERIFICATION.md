---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The leaf attachment identity W_(m+1)=W_m+m+S_U and s_v(m)=m*(H_m+H_(v-1)-3+2/v) give the conditional deviation delta_(i,v). Future independent attachments multiply that deviation by prod_(m=i)^(n-1)(1+2/m)=n(n+1)/(i(i+1)). g(v)=H_(v-1)+1+2/v has g(1)=g(2)=3, strictly rises for v>=2. Mean-zero parent average forces a crossing, while g(floor(a i)) - ((i+1)/(i-1))H_(i-1)->1+log(a) gives tau_i/i=e^-1. Sum conditional P_i=1 covariance across i to derive the exact root-degree covariance n(n+1)*(3/2-3/(n+1)-H_(n-1)^(2)+H_(n-1)/n). Independent complete enumeration n=2..7 checked conditional means, Wiener means and covariance. Scope restricted to uniform recursive labelled trees.

## originality

PASS

Neininger (2002) full primary 11 pages establish E[W_n] and covariance W_n with *internal path length*, not root degree or single specified parent choice. Prior Resultary root-degree/path-length regression concerns a different distance statistic; related root-degree/leaf covariance also differs. Dobrow 1996 fixed-labelled pair distance paper is plausible indirectly equivalent source but its full text was inaccessible; this residual risk alone does not cancel the new conditional mixed-statistic classification.

## value

PASS

Exact conditional response as a function of vertex age, its sharp natural exp(-1) sign boundary and the negative root-degree/Wiener covariance classify a meaningful mixed statistic of uniform recursive trees, useful for sensitivity of global pairwise distances to local attachment choices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
