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

Conditioning on K occupied sites gives a uniform K-subset and, by the support-to-spacings bijection, L=K+1 gaps (including zero entries) summing to N=n−K. Only positive ties count. To check the uniform tie lemma, use IID geometrics with q=L/(N+L), p=1−q, conditioned on their sum. Under a fixed equality pattern the constrained sum has an exponential tail on the 1/q scale. For the remaining s=L−v variables, the mass at u is s/(s+u) times the Bin(s+u,q) mass at s. At u=N−t and t≤log²(L)/q the binomial displacement from its mean is O(log² L) and its variance is comparable to L since p≥1/3. Stirling gives the uniform local mass q/√(2πsp) times 1+o(1), and the same order bounds the global maximum by using the negative-binomial mode. This proves the required conditioning ratio even as q→0. At the first window K=m with high probability, disjoint factorial-moment edges contribute (c³/4)^r and any connected component of size h≥3 has O(L^h q^{h−1})=o(1). For the first moment, a useful uniform bound even on the exceptional support event is P(G1=G2≥1)≤E[1/(G1+G2+1)]=(L−1)/(N+L−1) for L≥2 (uniform split given the sum; L=2 is direct). This also proves subcritical extinction, with m=0 handled separately. For m≤n/2 and m≫n^{1/3}, K concentrates above the initial scale; the pair/triple/disjoint tie estimates give relative variance o(1). For n/2≤m≪n², the zero count z tends to infinity with z/n≤3/4 with high probability. The isolated interior zero count has mean comparable to z and variance O(z+z²/n) from the disjoint hypergeometric joint probabilities and the O(n) overlaps, forcing length-one ties. These two uniform arguments also cover nonconvergent m/n. At m~bn² the exact zero factorial moments converge to b^{−r} and the expected adjacent-zero count is O(1/n), giving the stated Poisson transform, not a Poisson law for Y. Above the terminal scale the expected zero count tends to zero. Frozen finite verification was inspected read only; it is not the asymptotic proof.

## originality

PASS

The supported distinct contribution is persistence of equal positive zero-gap lengths throughout the full intermediate range. The first window is a credited transfer of Klykova, the final window is a short consequence of known gap isolation and elementary zero-count factorial moments, and extinction above n² is already implied by known no-gap results. Neither of those ends gives the entire intermediate interval.

## value

PASS

Repeated positive gap lengths are a natural extension of the individual gap thresholds in the same composition model. Equal-length collisions persist uniformly along all intermediate sequences between the two scales, not merely in easy subranges where there are many singleton gaps. The two distinct mechanisms and full coverage answer that motivated persistence question; standalone priority of either endpoint law is not needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
