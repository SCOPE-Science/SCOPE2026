---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Basis of six differentials follows from unique infinity pole orders (-4,-5,-5). Cartier coefficients follow F^((11*l-j)/4), giving 3-by-1 V,1-by-3 W and 2-by-2 B with W=(1,0,2a), determinant D. Crucially use Frobenius-twisted compositions E^(11)E, not ordinary generic square: V-W subsystem stable rank 2 iff L=v0+2a^11*v2 !=0, B subsystem rank 2 iff D!=0 and otherwise 1 iff K=m10^11*m01+3 !=0. Discriminant exclusion prevents V=0 in smooth domain. Independently recomputed F11 Cartier ranks over all 121 prime-field pairs (10 singular,86 rank4/a2,15 rank2/a2,10 rank3/a3). Independently recomputed exact lex Gröbner elimination for (L,D) and (D,K): univariate degrees 75 and 70, both squarefree, both coprime to resultant of (D,Delta), intersection ideal (L,D,K)=(1). The algebraic elimination certifies counts over the full algebraic closure; the 121-field census alone could not.

## originality

PASS

Cartier–Manin matrices and Fermat-type p-rank are standard. The claim is the full smooth coefficient-marked characteristic-eleven deformation stratification and geometric scheme counts. No covering result identified in available literature, with high-relevance genus-six article and complete Fermat-family text inaccessible.

## value

PASS

Exact natural p-rank and a-number degeneration strata in a two-parameter genus-six cyclic-tetragonal deformation, including reduced 75- and 70-point geometric incidence schemes. Natural invariant motivated by Jacobian arithmetic, not arbitrary numerical test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
