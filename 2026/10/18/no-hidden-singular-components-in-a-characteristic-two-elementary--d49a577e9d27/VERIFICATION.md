---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Over algebraically closed characteristic 2 with n>=11, n≡3 (mod 8), all gradient coordinates vanish only when each coordinate solves the same monic cubic x_i^3+e_1 x_i^2+e_2 x_i+e_3=0. The binomial translation coefficients for e4 vanish under n≡3 mod8, legitimate on affine cone representatives. Three distinct values force the three multiplicities ≡1 mod8 by successive e1/e2/e4 comparison; with exactly two, the binomial conditions yield multiplicity a≡1 or 2 mod8, always refinable to three 1-mod8 blocks. The all-equal point lies on all planes; conversely generating series makes e4 and gradient vanish on each plane. Generic Hessian is alternating block diagonal with rank sum(m_i−1)=n−3, and the full singular support has dimension 2, giving normality by R1+S2. Exact independent GF(4) enumeration evaluated every four-value multiplicity pattern at n=11 (364) and n=19 (1540), corroborating the characterization. Multinomial arithmetic verified 55 and 462061, and pair incidences follow two-index intersection. Enumeration is not substituted for the algebraically closed all-n proof.

## originality

PASS

The maximal-dimensional partition planes and generic Hessian rank were established by Xie 2026 and are not new. The distinct contribution is a complete reduction of every singular point in this n mod8=3 degree-four subfamily to one of those planes, ruling out hidden reduced components and giving an exact first incidence arrangement. Xie’s discussion does not classify all lower-dimensional components in general. Best-of-knowledge PASS for the missing full-support theorem; uncertainty remains over implicit consequences of broader statements.

## value

PASS

Exhaustive reduced singular-support classification is a natural geometric structural problem, beyond the already known top-dimensional component list. The argument rules out every possible lower-dimensional reduced component on an infinite arithmetic subfamily and specifies the first plane incidence configuration. It does not pretend to classify embedded nonreduced structure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
