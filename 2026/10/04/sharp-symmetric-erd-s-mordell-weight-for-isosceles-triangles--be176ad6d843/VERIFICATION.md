---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For a fixed height \(y\), the sum of the three vertex distances is an even strictly convex function of the horizontal coordinate, so the sharp symmetric inequality reduces to the altitude \(x=0\). There it is equivalent to \(K\le B_h(y)=[2\sqrt{1+y^2}+h-3y]/(h-y)\). The derivative has the sign of \(1-h(\sqrt{1+y^2}-y)\), yielding the boundary minimum \(y\downarrow0\) for \(0<h\le1\) and the unique interior minimum \(y_*=(h^2-1)/(2h)\) for \(h>1\). This gives the stated two-branch \(\Lambda(h)\) and equality behavior. For Liu's coefficient, the exact factorization \(H(s)^2-\lambda_L^2=(s-2)^2(s^3+2s^2+8s+8)/[8s^2(s+1)]\ge0\), together with \(\Lambda-H=(h-1)^2/(hs)\ge0\) on \(h\le1\), proves \(\lambda_L\le\Lambda\). Equality forces \(s=2\), hence the equilateral center. Independent parameter checks reproduced the formulas but are not used as the proof.

## originality

PASS

Liu's 2015 open-access primary paper explicitly states Conjecture 2 with the same median-to-angle-bisector coefficients \(m_i/w_i\). The audited result proves that conjecture for every isosceles triangle and, more strongly, determines the exact largest symmetric coefficient with a phase transition at \(h=1\). Later weighted Erdős-Mordell papers located in current searches use different weighting families; targeted searches did not find an isosceles resolution of this exact ratio conjecture. The complete bodies of some closely related later papers were not all inspectable, so they remain named residual risks rather than being declared noncovering.

## value

PASS

The theorem resolves an explicit published conjecture on the entire natural isosceles class and simultaneously identifies the sharp coefficient and extremizer transition. This is a motivated geometric classification, not merely a verification at a few symmetric examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
