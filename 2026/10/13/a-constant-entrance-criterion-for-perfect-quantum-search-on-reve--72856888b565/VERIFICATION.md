---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Reversibility makes Delta=I-P selfadjoint on l²(pi); Delta s=0 and <s,e>=a=sqrt(pi_w). If exact unit success, final state is a phase multiple of e, and commuting time evolution with H forces equality of first and second moments of s and e. First moment fixes gamma=(1-a²)/(1-r); second gives ||Delta e||²=(1-r)²/(1-a²). Cauchy–Schwarz between e-a*s and Delta e is saturated; its equality case implies Delta e=kappa(e-a*s) with kappa=(1-r)/(1-a²), equivalent coordinatewise to constant entrance. Conversely that identity implies H*s=-a e and H*e=-a s at gamma*, so invariant span{s,e} yields evolution cos(at)s+i sin(at)e, exact probability and all perfect times. Independently tested exact reversible weighted networks including cone-over-path with pi_w=1/3, P_uw=1/2 and asymmetric triangle that fails. Restricted to finite irreducible chains pi_w∈(0,1), gamma>0; no conclusions on approximation or nonreversible walks.

## originality

PASS

The Mograby–Balu–Okoudjou–Teplyaev paper studies weighted reversible graph Laplacians and Grover walks and gives exact complete-graph example but not an arbitrary-chain iff in the inspected full text. Ide–Narimatsu 2022 Theorem3.1 is a consequence of perfect state transfer between equitable partition cells with adjacency Hamiltonian and uniform initial vector, and concerns asymptotic success or a sufficient transfer condition; their original full text does not imply unique gamma and constant-entrance necessity for all reversible chains. Chakraborty–Novo–Roland 2020 provides asymptotic optimality spectral criteria, not finite-time probability-one classification. Classical unweighted regular-complement cone is a covered special case; weighted cone with irregular path-base is outside it.

## value

PASS

Gives a sharp universal iff for exact search attainability, unique tuning and all success times with arbitrary reversible weights/self-loops. The entrance condition has a physical Markov interpretation and shows how weights can enable or prevent exact spatial search even at fixed graph topology, a meaningful design invariant rather than simple special-case execution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
