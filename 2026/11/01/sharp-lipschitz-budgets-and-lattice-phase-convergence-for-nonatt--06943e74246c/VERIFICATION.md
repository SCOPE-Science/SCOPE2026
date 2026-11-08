---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

For real C([0,1]) the atomic positive/negative parts of mu have disjoint support and mass 1/2, hence ||mu||=1 and every projection onto ker mu is I-mu tensor h with mu(h)=1. Rank-one Daugavet equality (also verifiable by dense nonsupport test points) gives norm 1+||h||inf. The Lipschitz and amplitude constraints bound |mu(h)| by Phi_L(t)=sum w_m min(t,L/(2m^beta)); the clipped affine ramp h(x)=min(t,-t+Lx) attains every term, establishing exact feasibility L>=2/B and the unique minimum t_L including L=Lc. For s=(L/2)^(1/beta), the exact geometric tail eta(s), uniform Taylor remainder and bounded piecewise derivative imply t_L-1=beta*q^N/N*(1/(1-q)-r)+O(q^N/N^2), N=floor(s), r=s-N. Extremizing the continuous periodic profile gives liminf beta/(1-q) and limsup beta*exp((-log q)/(1-q)-1)/(-log q); both phases are realized. Independently solved finite scalar roots for q=1/2,beta=1 and q=.3,beta=2 with expected phase approach; read provided decimal code but did not treat its finite checks as proof.

## originality

PASS

Kania-Lewicki arXiv:2604.10771v1 explicitly has the dyadic nonattaining hyperplane and projection constant 2, but its qualitative Example 3.4(a) and surrounding Theorem 3.1 do not solve finite-L Lipschitz feasibility, the exact minimizing correction, or the geometric-lattice residual and sharp envelopes. The bounded-Lipschitz optimal-transport duality of Heinemann-Klatt-Munk is acknowledged; their finite-support general formalism does not state or directly evaluate the infinitely accumulating atoms' exact phase asymptotic. No equivalent exact result found among semantically searched published mathematical records; old unindexed regularization work may exist.

## value

PASS

The explicit Kania-Lewicki nonattainment example naturally raises the cost-of-regularity question, with a sharp feasibility threshold and an optimizing ramp. The nonconstant lattice phase and explicit liminf/limsup quantify a genuine effect of geometric atomic weights; these are not merely restatements of Daugavet nonattainment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
