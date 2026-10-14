---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

The bihomogeneous graph map is induced by A=xy²t,B=xw²t,C=yzwt,D=z²wt. In the actual X=D=1 torus chart, equations give Y=CZ, W=BZ² and C²=ABZ²; elimination closure is the irreducible hypersurface R=k[Z,A,B,C]/(C²−ABZ²), independently checked by solving the birational monomial ratios and reviewing exact Groebner script. Element T=C/Z is integral (T²=AB) but T∉R: modulo Z the class C is nonzero in k[A,B,C]/(C²). S=k[Z,A,B,T]/(T²−AB) is finite birational normal (hypersurface S2, singular V(A,B,T) codim2), hence normalization. The conductor ideal is (Z,C): ZT=C and CT=ZAB lie in R; modulo Z the image R/(Z,C)=k[A,B] cannot contain f(A,B)T unless f=0. Jacobian of C²−ABZ² gives V(Z,C)∪V(A,B,C), with the latter normal A1-transverse away from Z=0. The former is height one and is exactly the chart nonnormal locus. Proof needs characteristic zero for this Jacobian description; it does not assert global conductor classification.

## originality

PASS

The exact original Example 6.7 gives the four multidegrees (1,3,5,2) but does not assert the local equation, chart normalization, conductor, or codimension-one nonnormal component. Those geometric properties are not determined by multidegrees. General squarefree/Ferrers Rees-algebra normality theorems do not apply to the non-squarefree monomial ideal here.

## value

PASS

Codimension-one nonnormality of a natural explicitly published nonlinear multiview graph, together with complete affine normalization and conductor, is a meaningful geometric invariant beyond its known multidegree table. The normal A1 stratum/non-normal conductor dichotomy can inform subsequent birational and singularity work on this specific example, without requiring a global normalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
