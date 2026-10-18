---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

Under 0<b<1 and a>1-b, stationarity of L(x,y)=(1+y-a|x|,bx) gives E[y]=b E[x] and aE|x|+(1-b)E[x]=1, hence (a+1-b)E[x_+]+(a-1+b)E[x_-]=1. Affine branch matrices A_+=[[-a,1],[b,0]], A_-=[[a,1],[b,0]] have one eigenvalue inside (-1,1) and the other outside, as q_+(-1)=q_-(1)=1-a-b<0 and q_+(1)=q_-(-1)=1+a-b>0. An invariant support confined to either half-plane is bi-infinite bounded for that branch, hence only the corresponding fixed point. Otherwise sign mass on both sides, with strict mean bounds. Pushforward y_#μ=(bx)_#μ follows pointwise. For (a,b)=(17/10,1/2), coefficients 11/5 and 6/5 give 11E[x_+]+6E[x_-]=5 and endpoints 5/11,-5/6 exactly.

## originality

PASS

Collet-Levy 1984 constructs a strange-attractor invariant measure with ergodic properties, which does not by itself fix sign-amplitude moments for every compact invariant state. Classical fixed points and the left/right itinerary are prior, so the retained implication is the global moment simplex plus branch rigidity. A best-of-knowledge novelty conclusion is limited to the complete final theorem, not prior equations/local lemmas/classical parameters. Targeted original searches were undertaken but Resultary returned temporarily_unavailable/search_completed:false, not zero matches; full-text access gaps are candid risks.

## value

PASS

The left/right Lozi half-planes are the established symbolic partition. The sharp stationary sign-weighted amplitude simplex and one-sided-orbit rigidity restrict any compact recurrent symbolic state over a genuine parameter region and give a useful obstruction beyond merely locating fixed points.

The dated certificate retains the supplied scientific assessment, sources and limitations.
