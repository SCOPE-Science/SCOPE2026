---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

The Fryš--Kotrbatý simplex formula is exactly the stated degree-\(np\) Bernstein polynomial after absorbing the common \((1-t)^{n(p-1)}\) factor. Its Bernstein coefficients are \(a_j=\binom nj\) through \(j=n\) and zero afterwards. Differentiation gives coefficient differences \(a_{j+1}-a_j\), whose nonzero signs change exactly once. After \(x=t/(1-t)\), positive binomial multipliers preserve that single sign change, so Descartes gives at most one positive derivative zero. The constant coefficient is \(n-1>0\) and the last nonzero coefficient is negative, forcing one zero and a positive-to-negative derivative transition. The planar quadratic, critical point, maximum simplification and limits follow by direct algebra. The source's proved low-dimensional coefficientwise higher-order Godbersen inequality then gives the uniform-in-parameter convex-body bound for \(n\le3\). I independently checked the sign-change property for \(2\le n\le20\) and representative orders, while the inspected verifier checks the same identities on a broader finite grid; the all-parameter theorem rests on the symbolic sign argument.

## originality

PASS

The highly relevant Fryš--Kotrbatý primary preprint was inspected through its higher-order unbalanced-difference sections. It defines the body, proves the low-dimensional higher-order Godbersen cases, and gives the exact simplex-volume formula, including equation (21), but the inspected material does not optimize that formula in the imbalance parameter or state strict unimodality. Resultary search for the profile, Bernstein variation and optimizer returns the audited result as the direct exact match, with no earlier equivalent finding. The order-one predecessor studies the analogous body and pointwise inequalities but does not imply the all-order Bernstein-profile theorem.

## value

PASS

The imbalance parameter is intrinsic to the new higher-order unbalanced difference body, and the simplex is the conjectured extremizer. Determining the unique optimal imbalance in every dimension/order and converting the proved low-dimensional pointwise theorem into a sharp uniform bound are natural quantitative questions attached to the source construction. The explicit planar optimizer and asymptotics add usable structure beyond simply restating the source polynomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
