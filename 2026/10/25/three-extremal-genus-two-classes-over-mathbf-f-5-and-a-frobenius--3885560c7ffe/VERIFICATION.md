---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

The hyperelliptic degree-two map has 6 points on P1(F5), so at most 12 rational points, with equality precisely if all six fibers split and are unramified. Lagrange interpolation produces exactly 2^5*2*5=320 binary sextics with F5 values {1,4} at all six base points. Independently enumerated all 320, computed polynomial gcd with derivative, found exactly 240 smooth sextics; independent factor degrees give 120 (2,4), 40 (3,3), 80 (6). Independently applied all 120 PGL2(F5) transformations and both square scalar factors, getting exactly three orbits of sizes 120,40,80; separate F25 quadratic-field exact enumeration gives counts 26/28/24 and by Newton identities Weil middle coefficients 18/19/17. PGL2 equivalence of genus-two hyperelliptic models is justified by uniqueness of hyperelliptic involution. Complete finite enumeration is a proof here, not a heuristic sample.

## originality

PASS

General 12-point bound, existence and PGL2-orbit method are known. Nart 2007 computes unrestricted totals of hyperelliptic classes but not the six-split-fiber sublocus and its branch/zeta joint table in the inspected theorem. Hernández Encinas–Menezes–Muñoz Masqué (2002) explicitly assumes characteristic different from 2 and 5 and a rational Weierstrass point, whereas these F5 extremal curves have no rational branch point; so that seeming exact classification is inapplicable. No demonstrated stronger database coverage of the exact three-way refinement, but all-genus-two finite-field catalogues remain a live priority risk.

## value

PASS

Sharp small-field locus of maximal-point genus-two curves is intrinsically motivated; its complete arithmetic orbit and Frobenius/Weil trichotomy give exact classification and extension-field arithmetic data not specified by the elementary bound. Natural finite exact fact need not assert all-q theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
