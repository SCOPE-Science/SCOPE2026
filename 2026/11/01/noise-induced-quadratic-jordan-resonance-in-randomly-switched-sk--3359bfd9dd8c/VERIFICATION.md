---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Each full-branch skew tent preserves Lebesgue: inverse branch derivatives a and 1-a sum to one, so uniform initial law is annealed stationary. On centered polynomial u=x-1/2,v=x²-x+1/6, exact branch expansion gives P_a u=(2a-1)u and P_a v=[1-3a(1-a)]v-a(1-a)u. Thus annealed P has triangular matrix [[r,-q],[0,s]], q>0; its Jordan condition is r=s, precisely 3EA²-5m+2=0. Jensen q<=m(1-m) implies m>=2/3 and strict m<1. With h=u+v and orthogonal moments ∫u²=1/12, ∫v²=1/180, ∫uv=0, transfer duality yields the stated exact all-n covariance. At resonance geometric convolution becomes nλ^(n-1); divide by Var(X²)=4/45 to obtain λ^n(1-5(1-m)n/(8λ)). For the two-atom law m=3/4,q=1/6,λ=1/2, sign first reverses at n=4. Checked polynomial diagonal coefficient d_k for k>=3 is strictly below λ because a^(k+1)+(-1)^k(1-a)^(k+1)<a³+(1-a)³ pointwise. Independently symbolically expanded P_a u,P_a v and verified 25 rational-lag identities for two-atom covariance, including n=0. No full Banach-space resonance implied.

## originality

PASS

No decisive statement-equivalent or stronger-prior implication in the inspected comparisons; this is a bounded best-of-knowledge judgment rather than guaranteed priority. See four named check analyses and actual material-read logs. 

## value

PASS

The finding pins a precise moment surface on which random mixing creates a Jordan defect absent from each component and an observable switches sign at a sharp lag. This is a motivated quantitative stochastic-transfer calculation in a canonical full-height expanding family, with a concrete rational experimental benchmark and proof of isolation among polynomial degrees. Generic Jordan terminology alone is not the claimed new object-specific result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
