---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Conditioning on the focal spin leaves M=N−1 other agents, and gives the stated binomial versus without-replacement unanimity probabilities. Since p>0 the count chain is irreducible, with reflection-symmetric stationary law and mean N/2. Writing R_k=π_R(k)/π_D(k), detailed balance gives R_{k+1}/R_k=T(k)/T(M−k). For q=2, T(j)=1+b j(M−j)/[M²(M−1) D(j)], D(j)=a+b j(j−1)/[M(M−1)]. The difference D(M−j)−D(j)=b(M−2j)/M shows that T(j)>T(M−j) for 0<j<M/2, with equality at the endpoints and midpoint. Folding preserves the odds ratio, so R/D decreases with radial distance. The normalized ratio crosses 1 at most once on the ordered radial levels, implying stochastic dominance; if nonconstant, a strict tail difference yields strict variance inequality. For N=3 all ratios are 1 between adjacent states, and for N≥4 k=1 gives a strict step. Any convex test on K has the same expectation as its symmetrized test, which increases radially by convexity. For q=3,N=4 the distinct unanimity probabilities at j=1,2 vanish, whereas the repeated ones are 1/27 and 8/27. This gives T(1)<T(2) and T(0)=T(3)=1, so R is strictly smaller at K=2 than at every other state, reversing the radial order and the strict variance comparison. All arguments hold for real 0<p<1.

## originality

PASS

Neither the known sampling model nor the birth–death stationary formula is claimed as original. The theorem-level gap supported by the comparisons is the exact all-finite-size radial likelihood-ratio ordering between the two sampling rules at q=2, with sharp equality/strictness, and the all-noise reversal in the smallest q=3 case.

## value

PASS

Changing whether influence agents may repeat is a real modeling choice at finite size. The result orders every convex polarization statistic at once, not just a moment or a simulated histogram. The smallest q=3 reversal rules out a size-uniform heuristic based on repeated draws increasing unanimity; equality at N=3 pins down the boundary of strictness in the universal q=2 theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
