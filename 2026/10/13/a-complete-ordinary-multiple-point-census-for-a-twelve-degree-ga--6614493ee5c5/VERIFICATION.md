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

The actual A,B,D polynomial coefficients were inspected. The 12-element A4 and 12-element C12 subgroup actions give invariant quotient functions A/D and B/D, with trivial group intersection, so the curve parametrisation is birational of degree 12 and has the two specified outer Galois points. Independently enumerated all 122 points of P1(F121) via exact F11[u]/(u^2-2) arithmetic, grouped the images into precisely 25 size-2, 6 size-3 and 2 size-4 fibers, and checked every branch tangent nonzero with pairwise nonzero determinant, including source infinity. Their delta sum 25*1+6*3+2*6=55 equals arithmetic genus (12-1)(12-2)/2, saturating the full normalization genus defect; hence no additional singularity outside F121. Exactly five nodes fixed by F11 Frobenius; source F11 points give eight distinct infinity images plus one rational affine node, #C(F11)=9. Finite enumeration proves global completeness only together with genus-saturation and birationality, not alone.

## originality

PASS

Fukasawa-Waki 2021 Theorem 1(a) and construction prove existence of characteristic-11 A4/C12 two-Galois-point degree-12 rational model and exhibit the group generators/common orbit, but inspected body does not state geometric 25/6/2 singularity basket of the *specific trace-coordinate embedding*. Other Fukasawa-Waki models use other pairs; general Fukasawa-Higashine criterion addresses embeddings, while Fukasawa-Speziali semidirect-product case cannot apply because generated group order 1320 versus 144. No matching exact basket/trace coefficient database result identified.

## value

PASS

The singularity basket is a natural fine geometric invariant of an explicit Galois-point plane embedding beyond group-existence. Multiplicities 2,3,4, arithmetic fields of definition, and delta-genus exhaustion constrain normalization, local geometry, and rational-point count. Restriction to the fixed trace model is natural, not an arbitrary small slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
