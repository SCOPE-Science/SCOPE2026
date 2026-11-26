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

Adding a diagonal weight in (0,1) implements the stated ties without changing nonzero neighbor sums. Symmetry gives E_(t+1)−E_t=−(s_(t+2)−s_t)^T B s_(t+1), strictly negative whenever two-step equality fails; finite energy values give eventual period at most two. Within a periodic state all leaves at a site agree, and an ordered pair of core and leaf words is periodic exactly when both updates swap the words. With one leaf the two conditions mean no isolated bit in the bipartite double cover, which is one cycle of length 2n for odd n and two of length n for even n. The cyclic length-j count is the trace of the four-state consecutive-bit matrix with polynomial (z²−z−1)(z²−z+1). With two leaves a bit matching its leaves always retains that value, even at a tie; a differing bit must have at least one core neighbor matching its leaves, in both phases. The closed-walk trace counts indexed words, not rotation classes. Independently formed the 16-state matrix by literal four-vote majorities in both phases and recomputed its characteristic polynomial symbolically; all factors match, and the first trace counts agree with frozen VERIFY.out. The quartic has two positive roots in (1/2,1) and (3,4), exactly two by Descartes. For z=−u<0 it is positive (if u≥1/3 then 3u³≥u²; otherwise 2−u²>0). The remaining conjugate pair has squared modulus 2/(product of the positive roots)<4/3, and the other factors have moduli ≤sqrt(2); hence the large root governs growth. With r≥3 a monochromatic bundle dominates after one step, and a nonmonochromatic starting bundle is not recurrent, proving sharpness. Fixed points are counted separately and dividing P−H by two counts unoriented primitive cycles. Read VERIFY.py and VERIFY.out without executing the supplied script. Replay the independent matrix construction via `python3 /workspace/branches/independent_checks.py` (section 3; SymPy and mpmath); the finite determinant is exact, while the all-size counting and growth arguments are analytic.

## originality

PASS

Credit the established period-two theorem and cyclic no-isolated-bit count. Exact coverage of the one-leaf parity regime and the many-leaf regime exists in two distinct later-dated listings; neither covers the central two-leaf spectrum or the complete frozen census, and their dates do not prove historical priority. No inspected pre-existing statement gives that middle regime and census. This is limited to the specific labelled cycle-corona result.

## value

PASS

A full recurrent-state census for a natural graph family in one leaf-multiplicity parameter distinguishes three exponential growth rates and identifies the degree-four ties as a genuinely different constrained phase-pair system. The exact transfer quartic determines every labelled two-leaf count and the growth constant, which neither generic convergence nor the known ring word count provides. The result is not a basin or entry-time census for r=1,2.

The dated certificate retains the supplied scientific assessment, sources and limitations.
