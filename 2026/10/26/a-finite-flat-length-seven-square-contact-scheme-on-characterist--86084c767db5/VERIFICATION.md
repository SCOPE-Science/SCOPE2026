---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The proposed square-contact scheme is explicitly defined as the vanishing locus of two odd mixed coefficients; in characteristic two a degree-four binary form is a polynomial square iff both are zero. Lines at dual infinity W=0 cannot enter because the odd coefficient c (when V nonzero) or the coefficient 1 (line X=0) is a unit, scheme-theoretically. In the W=1 chart Z=uX+vY, independent symbolic expansion modulo 2 confirmed odd coefficients v(a+c u²), u+c v³. Eliminating u=c v³ gives av+c³v^7, and since c is invertible the normalized monic relation v^7+(a/c³)v gives a free family basis {1,v,...,v^6}; finite flatness holds over the smooth coefficient base. In a nonzero-a geometric fibre v(v³+s)², s²=a/c³, and the cubic has simple roots since its derivative v² is nonzero at roots, yielding local lengths 1,2,2,2; when a=0 the quotient is k[v]/v^7 and the maximal ideal has Hilbert function seven ones. Smoothness follows since f and f prime have no common root in affine chart, and the point at infinity has nonzero Z derivative. This statement is only about the particular square-contact scheme, not theta-characteristic moduli or mixed characteristic.

## originality

PASS

PASS, qualified with significant classical source risk. Nart–Ritzenthaler arXiv:math/0312366 gives classification of geometric bitangent supports in characteristic two, including the 4-versus-1 types, but does not, in the inspected full-text material, identify the specific rank-seven square-contact scheme with local Artin lengths for this Picard family. C. T. C. Wall (1995) is a plausible historical source of exact plane-quartic degenerations; his full text was not available even after arXiv/OA and authorized institutional attempt, so only its bibliographic extract was read. No equivalent degree-seven monic quotient appeared in the targeted Resultary or wider searches, which is not proof of priority.

## value

PASS

Geometric bitangent support counts of characteristic-two genus-three quartics do not determine infinitesimal multiplicity or flat specialization. An explicit finite flat rank-seven incidence scheme on a natural Picard subfamily, including a curvilinear length-seven collision and full Hilbert function, gives independently useful local geometry beyond the known 4-point and 1-point supports. Its definition is motivated by square-contact lines rather than an arbitrary numerical invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
