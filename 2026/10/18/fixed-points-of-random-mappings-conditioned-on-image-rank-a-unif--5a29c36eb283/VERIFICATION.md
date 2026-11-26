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

Fix an image set S of size r. Every surjection onto S is equally likely, and each fixed point is in S. For k prescribed indices in S, fixing those k outputs leaves an inclusion–exclusion count of completions that hit the other r−k labels. Summing over the (r)_k ordered choices yields exactly the displayed moment; the same count is the probability of distinct initial k outputs of a uniform surjection. This proves mean one (k=1), and Var(F)=a₂, with r=1 giving F=1. For iid uniform outputs D counts distinct first-k labels. The probability of full coverage given D=d is nondecreasing in d by inclusion of the sets that still must be hit. Conditioning on coverage thus increases the probability of the top event D=k, proving the lower moment bound, while the distinctness interpretation gives a_k≤1. Expanding the PGF at 1 gives the stated sandwich for z≥1. The birthday bound 1−a_k≤binom(k,2)/r extends to k>r because then the right side is at least one. Factorial inversion is finite for F and absolutely convergent for Poisson(1); summing absolute differences gives (1/2)Σ 2^k(1−a_k)/k!≤e²/r. This includes r=n and is uniform in n. For fixed r the iid output list is onto with probability at least 1−r(1−1/r)^n, so the moments converge to the binomial moments on the same finite support, implying TV convergence. The frozen checker was inspected, not run; its recorded finite tests are not evidence for the uniform estimate or either limit.

## originality

PASS

There is demonstrable overlap in the exact factorial-moment and mean identities: earlier prescribed-fibre moments specialize by averaging, and the distinct same-day indegree-profile result also supplies the moment upper bound. Do not credit those consequences as independently new. The actual rank-conditioned theorem additionally proves a two-sided finite moment comparison and an explicit uniform Poisson error in the rank alone, without imposing a deterministic degree profile; these were not covered by the strongest checked results. The frozen finding is a quantitative rank theorem, not a claim to have discovered the finer conditional moment formula.

## value

PASS

Image rank is a natural coarse observable distinct from a fixed occupancy profile or the set of cyclic vertices. The moment comparison gives a uniform finite control of the change caused by conditioning only on rank and explains why even very sparse growing ranks have Poisson fixed-point counts, whereas bounded ranks give a different binomial regime. The finite-rank rate requires no relative scaling of n, and the lower moment and variance comparisons give information not contained in the exact mean or qualitative profile criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
