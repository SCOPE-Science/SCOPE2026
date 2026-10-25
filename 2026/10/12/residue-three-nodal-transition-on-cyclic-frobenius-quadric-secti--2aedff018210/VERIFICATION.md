---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

For p>=5 the quadric has nonsingular rank-four polar matrix and two intersecting F_p-lines, hence is F_p-split. The degree-(p+1) Frobenius surface has gradient (W^p,Y^p,Z^p,X^p), nonvanishing projectively; on W=1 the proportionality equations are 2x^p=x+y, 2y^p=y+z, 2z^p=z+x. Euler identities ensure such critical points on Q also lie on S. Summation and cyclic-pair identities yield s in F_p and 4r^p=s^2+r; Q gives r=-1, so s^2=-3. For p=2 mod 3 no roots. For p=1 mod 3 diagonalize the cyclic shift by cubic roots omega: a^p=a, b^p=(1+omega)b/2, c^p=(1+omega^2)c/2; r=3a^2-3bc=-1 and (bc)^p=bc/4 force bc=0,a^2=-1/3. Two a values and 2p-1 axis choices yield 4p-2 distinct affine singularities. The W=0 split conic parametrization gives section t(1+t)H_p(t). Its derivative H_p_prime=(1+t)^(p-2)*(1-t^(p-2)*(1+t)^2); simultaneous roots are two primitive cubic roots exactly if p=1 mod3, each double, with t=0,-1,infinity simple. The resulting 4p singularities (including 2 at infinity) have local quadratic form proportional to the nondegenerate split second fundamental form of Q, because all ordinary second derivatives of S vanish; hence ordinary nodes. The finite singular locus makes the Cartier curve generically reduced and therefore reduced. Bidegree (p+1,p+1) gives degree 2(p+1), arithmetic genus p^2. On F_p points S=Q pointwise, yielding (p+1)^2 F_p-points; the 4 F_p-nodes are split and each lifts to two normalization points, adding 4. For p=2 mod 3 the smooth positive-bidegree divisor on P1xP1 is geometrically connected and irreducible. An independent direct enumeration for p=5,7,11,13,17,19 verified all F_p projective Q points, their S membership, rational Jacobian singularity counts 0/4, and gcd(H_p,H_p_prime)=1 or t^2+t+1; these tests corroborate, but do not prove the all-prime claims.

## originality

PASS

Closest initiating paper exactly establishes the p=5 equations and generic Frobenius nonclassicality but not the uniform geometric 4p-node versus smooth dichotomy. The published classification of full-rank Frobenius forms pertains to the hypersurface alone and does not imply the interaction with this fixed F_p-split quadric. Independently queried published Resultary findings and searched primary literature for aliases and dominating implications; no covering result identified. Some bibliographic risk remains and search failure is not proof of novelty.

## value

PASS

A natural cyclic degree-(p+1) Frobenius form intersected with its own F_p-split Frobenius-locus quadric produces a genuine infinite family of complete-intersection curves. Determining whether these curves are smooth or have ordinary nodes controls the applicability of smooth curve constructions, and the exact 4p node count and +4 normalized rational-point jump supply precise geometric/arithmetic invariants, not an arbitrary tiny computation or simple table restatement. The arithmetic genus and raw F_p point count are elementary deductions and are not independently credited as novelty/value; the substantive contribution is the residue-three discriminant transition and split-node geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
