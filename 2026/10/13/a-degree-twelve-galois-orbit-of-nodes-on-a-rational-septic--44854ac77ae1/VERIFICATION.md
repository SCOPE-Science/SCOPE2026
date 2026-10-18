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

The original normalization nu([u:v])=[u v^6-u^7:u^5(u^2+v^2):v^5(u^2+v^2)] yields in chart Z=1 the resultant E(x,y)=x^5(y^2+1)+5x^4(y^3-y)+10x^3(y^4-y^2)+5x^2(2y^5-y^3+y)+5x(y^6+y^2)+y^7-y. Independently computed resultant verifies this equation with correct sign. Exact symbolic discriminant wrt x is 3125 y^4 D(y)^2, D(y)=y^12+15y^10+71y^8+84y^6+9y^4-3y^2-1, and disc(D)=-2^36*5^18*821^2. The polynomial D is irreducible mod7 by actual factorization (degree12), hence irreducible over Q; the package verifier independently supplies a Rabin gcd certificate over F7. With r(y)=y(17y^10+254y^8+1193y^6+1371y^4+134y^2-1)/40, independently reduced E(r,y), E_x(r,y), E_y(r,y) all to 0 modulo D, giving 12 ordinary double points forming one rational Galois orbit. The parameter-line unibranch singularity at Q of type (2,5) contributes delta=2; P and twelve noncentral nodes contribute 13, saturating rational septic arithmetic genus 15, so no additional geometric singularities. Away from characteristic 2,5,821, the same separability and local-intersection conditions persist: rational ordinary nodes count 1 plus roots(D mod p), including p=7 giving 1 and p=11 giving 3. No unclaimed splitting Galois group or exceptional-characteristic classification is inferred.

## originality

PASS

Abouelsaad arXiv:2302.00324v1 and the Glasgow Mathematical Journal full article state the rational septic parametrization and the Galois-point nonextension phenomenon (Theorem C and Lemma 5.2). The paper discusses bounds on singular-point multiplicity, not the explicit rational twelve-node arithmetic orbit, irreducible discriminant factor, nor the rational point counts over finite fields. These latter statements require a new discriminant/normalization calculation and irreducibility certificate; the original parametrization itself is credited. Search and relevant related SCOPE results concern different explicit curves and do not dominate this fixed-septic arithmetic description. Historical unindexed computations of this same septic remain possible.

## value

PASS

The degree-12 orbit is a concrete exact arithmetic invariant of a natural nontrivial parametrized septic from Galois-point geometry. It identifies rational versus nonrational nodes and yields an exact finite-field rational-node counting law for all but three characteristics; the invariant is motivated independently of its polynomial computational complexity, and full splitting densities are not claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
