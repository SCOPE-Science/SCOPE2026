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

The four possible two-step words under fair A/B marginals have necessarily P(AA)=P(BB)=r and P(AB)=P(BA)=1/2-r, 0<=r<=1/2. Direct independent symbolic multiplication of D=[[1,h],[0,1]], K=[[1,0],[-h,1]], A=KD, B=DK verified (Gram(A²)+Gram(B²))/2=[1+h^4(h²-2)²/2]I and (Gram(AB)+Gram(BA))/2=(1+2h^6)I for symbolic h. The conditional expected energy multiplier for every state is therefore g_r(h)=1+2h^6+r h^4(h^4-8h²+4), and block independence proves E(E(z_{2m}))=g^m E(z0) for every m. The r slope factors at h=sqrt(3)-1 and sqrt(3)+1, giving unique endpoint optimizers except exactly at switches. At h=sqrt(2), r=1/2, A²=B²=-I and energy is conserved pathwise on even endpoints; positivity of both endpoint energy increments proves uniqueness. Fresh exact symbolic matrix calculation reproduced both scalar Gram identities and resonance, not by reusing logged verifier output.

## originality

PASS

Best-of-knowledge PASS for the specific fair joint coupling design problem and exact all-horizon mean energy multiplier, two coupling switches, and the pathwise resonance. Classical symplectic Euler/splitting ordering effects are known; McLachlan 2021 considers optimizing fixed ordering/composition. Cohen--Vilmart 2020 considers additive stochastic forcing for Poisson Hamiltonian flows, not randomizing deterministic adjoint orderings. Older random matrix products or correlated splitting studies remain a meaningful priority risk.

## value

PASS

Temporal correlation is a natural controllable design choice when two first-order symplectic integrators have identical marginals and cost. The sharp correlation-reversal phase diagram, despite both elementary maps being individually elliptic for 0<h<2, and unique exact energy-neutral block make a useful structural counterexample/benchmark. Does not assert phase accuracy or almost-sure stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
