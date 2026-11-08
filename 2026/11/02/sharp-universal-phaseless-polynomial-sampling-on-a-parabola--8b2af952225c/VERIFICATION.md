---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For z(t)=t+it^2, the two deck symmetries t->i-t and t->-i-t of z and its coefficient-conjugate reflection imply that any rational quotient of polynomial pullbacks with modulus one on the parabola has period 2i, hence is constant. The squared-modulus difference of two degree<=n complex polynomials is a real polynomial in t of degree<=4n, so any 4n+1 distinct samples enforce phase-equivalence. Sharpness is all-degree: the base pair z-100i and (z-50i)/4 has two positive u=t^2 magnitude crossings; adding distant imaginary roots and scaling one branch by alpha between A_n^-1/2 and 1 creates two additional separated crossings, until exactly 2n positive simple u roots yield 4n distinct t samples. The n=0 case and Euclidean similarity reductions are addressed. Independent exact rational Sturm isolations for n=1,2,3 corroborated the inductive signs but do not replace the all-degree proof.

## originality

PASS

Published phase retrieval on unions of straight lines and circles and lemniscate intersection theory are genuinely related. Reading their theorem statements and hypotheses did not find an implication for a single real parabola with any 4n+1 samples and sharp all-degree 4n obstructions. O remains qualified given possible alternate real algebraic curve intersection bounds.

## value

PASS

Identifies an exact worst-case deterministic sampling number for a natural curved real analytic sampling arc and gives nontrivial reflection-group phase rigidity plus an explicit matching obstruction in every degree. A generic-position result would not replace this for arbitrary predetermined sample sites.

The dated certificate retains the supplied scientific assessment, sources and limitations.
