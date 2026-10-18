---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The polar mean weights are m_j=lambda*w_j+(1-lambda)*w_{j+1}; periodic powers T^n=(product w_j)U^n give r(T)=(product w_j)^{1/n} also for unilateral/bilateral shifts. Weighted geometric-AM inequality telescopes under multiplication for the lower ratio 1, with equality iff all weights equal for interior parameters. In logarithmic coordinates log w_j∈[0,log K], the log product is strictly convex in each coordinate for 0<lambda<1, forcing all upper maximizers to binary endpoint weights. Every a->Ka change pairs a reverse change; transition count 2k<=2floor(n/2), and exact product is Theta^k. This proves sharp extremizers and the odd-period single equal edge. Maximization in lambda of lambda(1-lambda) yields its unique midpoint in nondegenerate cases. Independent exact-rational enumeration verified transition formula and all binary maxima across 81 (n,lambda,K) families n=2..10; the proof, not finite enumeration, establishes all dimensions/real parameters.

## originality

PASS

The 2014 Lee–Lee–Yoon source defines the polar mean transform; Chabbabi–Curto–Mbekhta 2019 (arXiv:1812.03499), Section 4 materially read in original full PDF, proves relevant monotonicity and exhibits spectral radius growth for a two-period weighted shift, not the contrast-constrained upper envelope or all equality patterns. Das–Biswas–Nahak 2026 arXiv:2608.15180 concerns lambda-interpolated means in its public abstract; the full manuscript remained inaccessible, and is a notable same-operator priority risk. Search of related Resultary claims found the identical submitted entry and related mean/weighted-shift work, not a stronger all-period quantitative formula. This is a best-of-knowledge priority comparison, not a claim that those unread pages lack it.

## value

PASS

Weight contrast K is a natural scale-invariant condition on periodic shifts. The exact sharp inflation constant determines how badly the polar arithmetic mean may enlarge spectral radius, with a complete even/odd combinatorial equality law, unlike the already known monotonic lower bound or one 2-cycle example. This is a motivated exact extremal invariant across all finite periods; no unsupported general-operator iteration theorem is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
