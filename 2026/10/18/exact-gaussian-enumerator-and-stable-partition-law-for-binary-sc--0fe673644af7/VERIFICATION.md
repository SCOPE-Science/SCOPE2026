---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

Canonical binary gap decomposition w=b^x a b^{u1}...a b^{u_(A-1)}a b^z has total interior d=sum uj and ab count Σ j uj+A z. Scattered a b^t a occurs iff d>=t, so avoiding words have d<=t-1. Weighted gap compositions give q^d Gaussian [A+d-2 choose d]_q and z contributes Σ_(z=0)^(B-d) q^(Az). For C<A, z=0; since B>=C and A-1>=C, the partitions of C are unrestricted except for at most t-1 parts. The full denominator Gaussian coefficient stabilizes to p(C). For fixed r=t-1, p_<=r(C)~C^(r-1)/(r!(r-1)!) and Hardy–Ramanujan p(C)~exp(pi sqrt(2C/3))/(4sqrt(3)C), giving 4sqrt(3) C^r/(r!(r-1)!) exp(-pi sqrt(2C/3)). Independent literal subsequence enumeration matched the polynomial on 84 parameter triples A=2..5,B=0..6,t=3..5. These are bounded checks.

## originality

PASS

Fazekas–Huang–Mercaş study the same Parikh-matrix fixed (A,B,C) languages but their accessible abstract claims an additive approximation algorithm for any fixed pattern, not this exact all-parameter a b^t a conditional Gaussian enumerator and fixed-t asymptotic. Richomme establishes partition-lattice denominator and classical q-binomial identities, credited here. Institutional full-text download for the Fazekas paper failed with VPN disconnected after arXiv and OA routes were attempted; that unresolved comparison is an explicit substantial residual risk, but not evidence of coverage.

## value

PASS

The triple statistic (A,B,C) and fixed scattered-pattern avoidance problem is a natural exact conditional enumerative invariant of Parikh-matrix languages. The single polynomial simultaneously describes all coefficients and yields an A/B-independent stable partition probability with a sharp asymptotic, refining general approximation schemes. This is not just relabeling a Gaussian denominator.

The dated certificate retains the supplied scientific assessment, sources and limitations.
