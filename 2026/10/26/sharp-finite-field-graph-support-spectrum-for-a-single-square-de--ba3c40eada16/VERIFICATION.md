---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Independence of the n−1 square representatives makes the product of distinct basis vectors vanish coefficientwise. In every singleton coordinate exactly one column is nonzero; the singleton rows must use distinct columns by invertibility. The other two columns span U and are B-orthogonal, so neither is isotropic and the nondegenerate B forces all remaining U-components to vanish. Perpendicularity is an involution of q+1 projective lines with exactly 2 or 0 fixed points in odd characteristic according to −λ, and exactly 1 in even characteristic by bijectivity of squaring. A nonzero v_i receives one target coordinate precisely on its own nonisotropic orbit; hit orbits are separated by their nonempty disjoint one-arrow index sets, while all unhit orbits coincide in support. The two sources in U have identical support and the singleton-target supports are fixed, so the count survives the common swap and is for the whole marked graph. Choosing u_1=e_1 and u_i=e_i+v_i on distinct remaining orbits makes t=min(n−1,N) with independence automatic. This proves the maximum, including N=1; the F5 example has the stated distinct outdegree multisets.

## originality

PASS

The structural block theorem and orthogonal parametrization are prior results, and the projective basis count follows by a fixed-point calculation. The supported distinct claim is the marked graph-support spectrum for a sole square-dependence pair with independent representatives, and its sharp extremum over realizable algebras. The strongest inspected comparisons do not cover that classification.

## value

PASS

The graph of an evolution algebra depends on its natural basis. On a minimal nontrivial dependence stratum, the invariant specifies exactly which basis moduli genuinely change the graph, including when different moduli collapse to one marked pattern. The attained bound limits simultaneous marked realizations by both dimension and field size, independently of the sizes of the basis-change groups. This is a useful complete classification in the direction of the survey questions, not a solution to unrestricted graph realization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
