---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Reconstructed the EXACT best-response map from the source PGG/Friedkin–Johnsen payoff with zero prejudice coupling: x_i^+=1{(Wy)_i>theta}, y^+=rho Wy+eta x^+, theta=1/2+alpha(1-r/4)/(beta lambda/(beta+lambda)), rho=beta/(beta+lambda), eta=1-rho. On 4 players with two influence pairs, mate weight epsilon and cross-pair each (1-epsilon)/2, the states (H,H,L,L) and (L,L,H,H) with H=(eta+rho epsilon)/(eta+2rho epsilon), L=rho epsilon/(eta+2rho epsilon) alternate strictly whenever epsilon/D<theta<1-epsilon/D. The rational witness alpha=1/20,beta=1/5,lambda=3/4,r=3,epsilon=1/10 gives rho=4/19, theta=139/240, H=77/79, L=2/79, inputs 19/158 and 139/158 and action vectors (0,0,1,1)/(1,1,0,0), all exactly independently checked. Strict margins and infinity contraction <=rho (two-step <=rho²) give genuinely attracting open neighborhoods; invertible I-rho²W² and strict inequalities persist for nearby parameters. Both consensus all-0/all-1 are additional strict attracting fixed points. This refutes unrestricted convergence in permitted SIMULTANEOUS revision only, not singleton-asynchronous convergence.

## originality

PASS

The 2026 original Davidson et al. paper explicitly permits synchronous R(t)=V and conjectures equilibrium convergence, but gives no strict attracting two-cycle. Earlier synchronous best-response oscillations are known in other binary/social games; those do not prove the given exact model-specific rational orbit with continuous opinion update and primitive complete weighted graph. The specific construction and parameter-open robustness are additional to the primary original theorem; later revised preprint could change conjecture.

## value

PASS

This is a concrete, strict, structurally robust counterexample to an explicitly stated convergence conjecture in a recently proposed opinion–action public-goods model. The complete graph has positive off-diagonal weights and primitive mixing, so connectivity/aperiodicity do not restore convergence under synchrony. This identifies an important exact boundary on allowed revision schedules rather than claiming generic synchronized cycles are new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
