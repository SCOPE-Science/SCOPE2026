---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Let K=Q(a,b,c,d,e) with algebraically independent distinct branch parameters outside {0,1}. The source family f(Y,Z)=G(Y²,Z²) is invariant under independent sign changes. Moriya–Kudo Prop. 4.2.6(I) shows one origin node and four nonzero sign nodes generically. The unique nonzero squared pair (u*,v*) is fixed by absolute Galois and hence lies in K×; its field of definition is K(sqrt(u*),sqrt(v*)). For the claimed rational tuple (2,3,4,5,6), an INDEPENDENT exact resultant calculation gives G=-12(600u³−520u²v−50u²+142uv²+33uv+u−12v³+13v²−v). The exact ideal (G,G_u,G_v) has reduced Groebner basis {560u−11,56v−1}; G(u0,v0)=0 at u0=11/560,v0=1/56 and det Hess(G)=-253584. The origin affine Hessian is diag(-24,24); at all four points (±sqrt385/140,±sqrt14/28), det Hess f=-348678/245. The leading infinity sextic has squarefree univariate polynomial and both coordinate-axis potential noncentral singular loci have constant gcd, ruling out other projective singularities independently of the source bound. Thus exactly five ordinary nodes. The square classes [385] and [14] and their product are nontrivial over Q, hence the specified node field has Galois group V4. The nonzero Jacobian/Hessian at the rational parameter tuple makes the unique squared node pair regular on a local normal open of the parameter space. If any of u*,v*,u*v* were a square in K, its integral square root would be regular there and would specialize to a rational square, contrary to the exact rational witness. Therefore the generic classes are independent and the four-node action is regular V4. Outside finitely many primes the projective reduced singular scheme extends as a finite etale five-point scheme; the central point stays rational and the other four are simultaneously rational iff (385/p)=(14/p)=+1. Since those quadratic characters are independent, Chebotarev gives densities 1/4 for five and 3/4 for one, without counting smooth Fp curve points. A separate modular program exhaustively enumerated all projective singular points for 18 odd representative primes 13..83, matching predictions; finite samples are not an infinite density proof. 

## originality

PASS

The natural geometric theorem in Moriya–Kudo arXiv:2310.15993v1 explicitly provides the five nodes and four independent geometric sign choices; it does not establish that the two *arithmetic* square classes are independent over the rational function field. Its theorem permits Galois subgroup orders 1, 2, or 4; the exact specialization and local argument supply the missing order-4 proof. Moriya–Kudo II arXiv:2401.00760v1 repeats the earlier geometry and studies a distinct genus-five Howe construction. Ohashi arXiv:2604.18074v3 handles superspeciality over finite characteristics, not this fixed characteristic-zero singular-node field. The earlier table counts geometric node types over varying parameters mod p, not the Frobenius distribution of a single Q-curve over varying primes. Three Resultary semantic searches and three repository searches returned no demonstrably covering published statement. That negative evidence is not a proof of novelty; the inspected primary comparisons by exact mathematical implication support PASS at best of knowledge, subject to the uninspected MEGA poster/unindexed computations.

## value

PASS

A genus-five Howe plane sextic has a natural complete singularity scheme, and arithmetic descent asks over which fields its four noncentral geometric nodes exist. The paper’s mere geometric V4 sign symmetry does not force arithmetic transitivity or full biquadratic degree. Showing full generic degree four requires an exact independent-square-class witness and a specialization theorem; this answers a motivated structural question about the whole generic five-node locus. The explicit rational model then gives a complete Chebotarev splitting-type frequency for rational singularities upon reduction, distinct from earlier varying-parameter node tables. This is an exact and potentially useful arithmetic invariant of a natural family rather than a rewording of the geometric count. It does not classify nongeneric members, the full bad-prime set, or all finite-field point counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
