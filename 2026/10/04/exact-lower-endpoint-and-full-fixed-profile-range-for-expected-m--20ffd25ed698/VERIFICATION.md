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

Writing \(w_i=P_i^n-P_{i-1}^n\) and \(s_i=w_i/p_i\) gives \(\mathbb E M_n-\mathbb E X=\langle X-\mathbb EX,S-1\rangle_p\), with strictly increasing score coordinates. Cauchy--Schwarz gives the stated upper endpoint and equality exactly for an increasing affine function of S. For the lower bound, every centered increasing support has the positive gap decomposition \(y=\sum_j d_jv^{(j)}\). Each threshold vector has ratio \((P_j-P_j^n)/\sqrt{P_j(1-P_j)}\), so positivity plus the triangle inequality yields the lower bound. With \(m\ge3\), at least two positive gaps multiply noncollinear threshold vectors, making the norm triangle inequality strict. Concentrating all but one gap to zero approaches the minimizing threshold ray. After quotienting translation and positive scale, positive gap vectors form a connected open simplex; continuity therefore makes the image the full interval from the unattained infimum to the attained maximum. An independent random-profile calculation over 200 profiles/supports reproduced \(L<R\le U\).

## originality

PASS

The accessible record for López-Blázquez's 1998 paper describes the opposite optimization—the upper expected-maximum problem under moment constraints—and is consistent with the projection endpoint used here. Papadatos's full paper characterizes entire sequences of expected maxima, not support-geometry minima for one fixed atom profile. Targeted Resultary search found no lower cut formula, two-level-collapse characterization, or full fixed-profile interval. Full text of the closest 1998 article remained inaccessible because the authorized institutional fallback was blocked by the platform safety gate; under the owner rule this is retained as an access residual rather than converted into failure.

## value

PASS

The upper expected-maximum geometry for discrete distributions is an established optimization problem. Determining the opposite sharp endpoint when the atom masses are fixed, including all near-minimizing shapes and every attainable intermediate value, gives the complementary geometry of the same natural statistic. The equal-mass formula and two-point boundary make the result directly reusable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
