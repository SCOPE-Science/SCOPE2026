---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For w_{j,n}=r_n P_n z_j, t_{j,n}=||w_{j,n}||Y satisfies r_n<=t_{j,n}<=1 by f_j norm 1, hence v_{j,n}=x_j⊗w_{j,n}/t_{j,n} lies on the projective unit sphere and source exposing φ(v_{j,n})>=r_n→1. Independently checked g1=(4f1+2f2)/3, g2=(-2f1-4f2)/3, g3=(-2f1+2f2)/3 sum to zero and have evaluations on z1,z2,z3 of (1,0,-1),(0,-1,1),(-1,1,0). The generator ball of Y bounds all three dual norms by 1; C(xj)=gj is a norm-one operator because B_X=aco{x1,x2,x3}. Its projective bilinear functional Θ gives Θ(v1,n)=r_n/t1,n and Θ(v2,n)=-r_n/t2,n for n>=3. Thus ||v1,n-v2,n||π>=2r_n→2 while both eventually belong to every exposing slice, proving diameter 2. The original isometric embedding J and contractive projection M carry the exact same diameter witness to the degree-two symmetric construction. This proof is infinite via r_n↑1, not finite sampling.

## originality

PASS

Construction-specific maximal slice diameter is not a mere restatement of exposure; prior broader sufficient theorems do not meet these space hypotheses.

## value

PASS

Exposedness is usually understood qualitatively; the maximal diameter of every arbitrarily thin exposing slice of a concrete exposed non-elementary tensor is an informative quantitative extremal separation from strong exposure. The same mechanism persists under a nontrivial symmetric tensor transfer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
