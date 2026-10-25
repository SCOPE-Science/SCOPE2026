---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Reconstructed the proof for smooth n-dimensional intersections of n+1 split quadrics in P^(2n+1) over C with the assumed free fixed-point-free sign involution; n is EVEN and at least 4. Integral complete-intersection Lefschetz below degree n yields H0Y=Z, H1Y=0, H2Y=Z (hyperplane), H3Y=0 and pi1Y=0. The involution acts trivially on H2Y; integral Cartan–Leray for C2 has E2^{p,q}=H^p(C2,H^qY). Every total-degree-three term is zero, so H3(T,Z)=0 without hidden differential, and surviving terms in degree two give 0→Z/2→H2T→Z→0, split. H1,H2 of O_T vanish by finite étale averaging and Hodge/Lefschetz; exponential sequence identifies Pic(T)=H2(T,Z) and H2(T,O*_T)=0, hence analytic/cohomological and algebraic Azumaya Brauer vanish. Residue top-form changes by determinant (-1)^(n+1)=-1 for even n, giving nontrivial order-two canonical class. This excludes n=2 and nonfree members. The source parity script is confirmatory only, not the proof.

## originality

PASS

Best-of-knowledge originality of the precise final claim, with prior partial/general coverage credited. Boissière–Camere–Sarti already construct the same split-quadric free quotients and prove order-two canonical behaviour; those are not new. Frassineti et al. compute Brauer for Enriques manifolds with hyper-Kähler covers, which are not the Calabi–Yau complete intersections here. Standard topological results make the calculation accessible but do not themselves state this geometric family’s uniform Brauer vanishing. Search failure alone is not proof of novelty, and explicit residual risks remain.

## value

PASS

Computing the Brauer group of a natural family of smooth Enriques-type Calabi–Yau quotients in every higher even dimension is an independently useful exact invariant: despite persistent nontrivial canonical order-two torsion, Brauer becomes zero, unlike Enriques surfaces. It resolves a concrete previously unevaluated invariant for an identified geometric family through a uniform proof; it is more than a bare restatement of the Cartan–Leray formalism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
