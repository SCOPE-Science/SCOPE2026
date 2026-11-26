---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Invertibility of T gives [L_T,L_T]=V and center zero. Every automorphism preserves V and has e↦ae+w and restriction S, with bracket condition ST=aTS. The determinant of the triangular matrix of φ−I is (a−1)det(S−I), so w is unrestricted. The intertwiner maps the λ-primary space onto the λ/a-primary space, preserving the block sizes because the nilpotent parts differ only by multiplication by a unit. Each chosen map between those spaces ranges over a torsor for a module-centralizer unit group. On each eigenvalue module, a map from length i to length j needs a factor u^max(j−i,0), giving min(i,j) independent coefficients. The same-length constant matrices define a surjective algebra map to the product of full matrix rings. Its kernel is nilpotent: a kernel transition either picks up a factor u or strictly decreases block length, so if K is the maximum length, every product of K² kernel maps vanishes. Consequently a unit and the unit test on P−I are determined in that quotient, with equal-size fibers. Subspace Möbius inversion divided by |GL_d| gives the stated δ_q(d), since the expected number of pointwise-fixed r-dimensional subspaces is 1/|GL_r| by transitivity on ordered independent r-tuples. A vector fixed by cyclic S is uniquely propagated from a fixed vector of its return map; choosing all but the last link makes the return map run exactly once through the module-centralizer unit group. Choices from different orbits are independent. This gives the count, proportion and total. For q=2 only a=1 is available; for q>2 a nonidentity scalar times the identity in each return quotient shows positivity in every available a≠1 sector. Independent bounded module enumerations over F_3 gave 18 good cyclic pairs out of 36 for paired J_2 and 2916 out of 11664 for paired type (2,1), hence fixed-point-free Lie counts 1458 and 2125764, and total counts 5832 and 17006112. These checks can be replayed by enumerating the entries of X,Y over F_3, retaining invertible links with X T_1=2 T_2 X and Y T_2=2 T_1 Y, and rejecting pairs with det(YX−I)=0. The frozen verifier was inspected, not executed.

## originality

PASS

The block form, linear derangement count, centralizer unit factors, and general return-product method are prior ingredients. The strongest exact indexed overlap is earlier and genuinely includes the diagonalizable specialization of the FPF count; that specialization is not credited as new. The supported distinct claim is the extension of the exact enumeration to all split Jordan types, using the scalar action on complete partitions and return maps in the nilpotent-module centralizer quotients. Earlier complex existence and the earlier semisimple finite-field count do not cover that extension.

## value

PASS

The formula gives an exact census rather than just an existence test on a natural class of finite Lie algebras. It explains why equal eigenvalue multiplicities can still give different outcomes: scalar compatibility and return-map exclusion detect the full Jordan partitions. The nonsemisimple probability and count therefore add a usable invariant beyond the earlier diagonalizable case and complex existence criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
