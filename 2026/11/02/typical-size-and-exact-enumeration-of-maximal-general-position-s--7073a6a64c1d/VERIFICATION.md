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

The induced-P3 criterion in a diameter-two graph makes selected root edges form vertex-disjoint clique components in the line graph. Two-edge stars can be completed; an uncovered vertex is insertable at a star centre, and two uncovered vertices can be joined. Conversely a new edge joining blocks gives an induced P3, an extra edge inside a large star misses a third spoke, and an edge from an isolate to a triangle misses the opposite triangle edge. This proves the precisely labeled block model, including one star center per possible root on blocks of size at least four and the exceptional singleton. In the independent-Poisson model the means grow as E J ~ n/r, Var(J)=O(n/r), Var(N)~nr, with r~log n. For the conditioning estimate, the middle block sizes [r/2,2r] carry asymptotically all the variance and give Gaussian domination for |t|≤δ/r; outside it the exponential term gives a gap Ω(n/r²), dominating the O(r³) polynomial subtraction. The cubic moment bound O(nr²) is negligible at the central scale. Thus P(N=n)~(2πnr)^(-1/2), and conditioned Chebyshev costs only O(r^(3/2)/sqrt(n)). The log count of the exceptional class is smaller by order n log n, so the same limit holds for the uniform maximal-set distribution.

## originality

PASS

For the narrowed asymptotic claim. The known maximal block description, including the exceptional configurations and the deficit as the number of stars in the covered class, makes its labeled enumerator a direct exponential-formula consequence. An exactly equivalent later catalogued enumerator is noted. The inspected work does not give the uniform asymptotic deficit on this restricted assembly, and the standard general saddle theorems have analytic hypotheses requiring proof for it.

## value

PASS

The asymptotic distinguishes what is typically sampled from both size extrema of a natural graph family: most maximal sets are short of n by asymptotically n/log n, although optimum size is within one of n and minimal maximal size is on a different linear scale. The normalization and leading constant answer that concrete distributional question; the routine EGF alone is not the value claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
