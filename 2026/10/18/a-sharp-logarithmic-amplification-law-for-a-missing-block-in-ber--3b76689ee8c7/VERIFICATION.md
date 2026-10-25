---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

With fixed k, h_N/N tending to interior theta and alternating weights reindexed after deleting h+1,...,h+k, positivity of finite alternating reciprocal tails rules out poles. On every ordinary unit cell, D>=F(u)=1/[u(u+1)]+1/[(1-u)(2-u)] >=8/3, A<=u^-1+(1-u)^-1+2H_N; therefore Lebesgue quotient <=(3/4)logN+O(1) uniformly (singular nearest-node terms are absorbed into F). On the enlarged gap, p_N,q_N~N and the finite alternating sums converge uniformly to D_infty(s)=2int_0^1 t^{(k+1)/2-1} cosh(s log t)/(1+t)dt. This denominator has strict unique minimum at s=0 equal Delta_k, while A=2logN+O(1) at interior fixed s. Near either gap boundary nearest reciprocal term dominates and quotient/logN tends to 0. The midpoint yields matching liminf 2/Delta_k; compactness and strict integral minimum show *every* global maximizer localizes. Independent finite computations at N=10000 for k=1,2,3,5 give normalized midpoint values about 1.424,2.145,2.863,4.267 versus true constants 1.443,2.330,3.259,5.177; convergence is slow and these checks do not prove the limit. Digamma identity follows by alternating Hurwitz sum. The large k expansion is after the fixed-k N limit, not uniform in k.

## originality

PASS

Bos–De Marchi–Hormann–Sidon prove O(log N) for well-spaced Berrut node families, which includes the fixed missing block with bounded adjacent gap ratio, but their Theorem 2.2 yields an unspecified bound rather than exact coefficient and maximizer localization. An author-hosted full primary paper was located and read (earlier assumed inaccessible), strengthening the actual comparison. No exact deleted-block constant was found in its central theorem or examples; this is best-of-knowledge, not a claim of exhaustive priority.

## value

PASS

Berrut interpolation is a natural pole-free data-interpolating method, and deleting one local sample block while retaining the endpoints is a practical stability perturbation. The exact amplification constant depends quantitatively on block length and singles out where the worst-case error concentrates; the localization is not available from general O(logN) well-spaced bounds. This is a reusable sharp stability invariant, not just a restatement of order-of-growth.

The dated certificate retains the supplied scientific assessment, sources and limitations.
