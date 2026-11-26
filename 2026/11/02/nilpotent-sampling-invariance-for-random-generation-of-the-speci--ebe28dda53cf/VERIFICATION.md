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

In odd characteristic a two-dimensional subalgebra is nonabelian (a noncentral traceless matrix has one-dimensional centralizer in the Lie algebra). If its derived line is spanned by E and [H,E]=E, invariance of trace gives tr(E²)=0. Since 2 is invertible, E is square-zero, and the subalgebra is the stabilizer of ker E. Thus a nonzero seed has one, two, or no such planes according to its rational eigenlines. For both sampling measures, a prescribed Borel has mass 1/q: among square-zero matrices its intersection is exactly the nilpotent line. The intersection of two such Borels, or the line of a nonsplit seed, has mass 1/q² for either measure (only zero contributes on the cone). This yields all nonzero-seed cases by inclusion–exclusion. In characteristic two, the bracket on the two-dimensional quotient by the center is a nondegenerate alternating form, so generation is equivalent to spanning the quotient. Each quotient vector (b,c) has the unique square-zero lift with diagonal coordinate sqrt(bc), and the lift is linear along each quotient line. This proves identical spanning probabilities for both measures, including central seeds, and excludes dimension two for unseeded nilpotent tuples. In odd characteristic the same exclusion follows from the nilpotent line in each Borel. Counting nonzero tuples on the q+1 nilpotent lines gives the dimension-one mass; the all-zero tuple gives q^(−2k). For unrestricted sampling in either characteristic there are q+1 subalgebra planes (in characteristic two they are the preimages of quotient lines), and the number of spanning tuples on each plane is (q^k−1)(q^k−q). Counting planes, lines and zero separately gives the stated unseeded success probability and dimension-two count. For an odd field and fixed Δ, the count of (a,b,c) with a²+bc=Δ is q(q−1)+q times the number of solutions of a²=Δ, giving the four type counts after isolating zero. Summing the geometric failure tails, including failure at k=0, gives the means. The frozen checkers and logs were inspected as small-field evidence and not executed.

## originality

PASS

The passing claim is the simultaneous full-vs-square-zero sampling comparison for every fixed seed and length (and the contrasting unseeded generated-dimension behavior). The full-sampling no-seed count is an exact earlier specialization. In odd characteristic the unrestricted fixed-seed counts are immediate from already published Borel incidence and should be credited to it as consequences, not claimed as new incidence or as independently novel counts. The restricted-sampling comparison, with its characteristic-two lift and its dimension-distribution distinction, is not covered by the compared generation-existence, exact full-sampling, or graph results.

## value

PASS

Restricting each draw to a natural subset of relative size 1/q preserves every fixed-seed success probability and waiting-time law, even though it removes an entire generated-dimension stratum for unseeded tuples of length at least two. This is a substantive distinction between success probability and the distribution of what is generated. The odd-characteristic incidence mechanism and the characteristic-two quotient mechanism make the exact, uniform-in-q assertion useful beyond an isolated small-field probability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
