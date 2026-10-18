---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The exact maxima/minima probabilities give c_i=K_n(P_i)-K_n(P_{i-1}), sum c_i=0, and R_n=sum p_i z_i(x_i-mu). Weighted Cauchy--Schwarz yields C_n(p)^2=sum c_i^2/p_i, with equality iff x_i=a+b z_i. K_n''=n(n-1)[u^(n-2)+(1-u)^(n-2)]>0 ensures consecutive cell-average z_i strictly increase, so equality is admissible iff b>0. For K_n'=n[u^(n-1)-(1-u)^(n-1)], beta-integral yields B_n^2; the orthogonal cell-average identity gives B_n^2-C_n(p)^2=sum int_{I_i}(K_n'-z_i)^2>0 for every positive cell. Independently tested 24 exact rational profile/sample-size cases, the exact polynomials, score ordering and norm deficit. Finite checks corroborate, not prove, the all-profile statement. m must be >=2 for a nondegenerate law; n>=3.

## originality

PASS

The unrestricted Plackett and Han--Wang--Wu bounds do not prescribe finite positive atom masses; the score's exact cellwise projection and strict deficit are a substantive fixed-profile refinement. A published same-day **later** complete attainable-interval result explicitly includes the same upper fixed-profile constant and equality support, so it is strong mathematical coverage now, but the target's original import (2026-10-04T06:01:17Z) precedes that record's import (2026-10-04T06:01:22Z), and the later full theorem does not express the continuous-score atomization-deficit identity. The pass is historical best-of-knowledge, not an assertion that no equivalent antecedent exists.

## value

PASS

The fixed probability vector is a natural constraint for categorical or empirical distributions. The result solves the sharp sample-range/variance problem at that information level, determines the unique optimal ordered support, and quantifies the unavoidable gap to the unrestricted sharp constant by a useful orthogonal-projection identity; this is more than a renamed global range bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
