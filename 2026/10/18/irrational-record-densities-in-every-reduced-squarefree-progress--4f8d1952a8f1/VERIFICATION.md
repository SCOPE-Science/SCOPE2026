---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For each squarefree m and reduced a choose n0 with m|P_n0. The published primorial block translation then preserves residues for n>=n0; exact class-by-class recurrence w_(n+1)(a)=p_(n+1)w_n(a)−s_(n+1)(a) makes rho_n(a)=w_n/P_n a nonnegative decreasing sequence. The source’s block-copy mechanism with a two-scale boundary estimate O(P_(n−1)+p_(n+1)²)=o(P_n) extends convergence from primorial cutoffs to full natural density for all X. A class-specific scaled tail T_n=P_n(rho_n−delta)=sum_{k>n} s_k/(p_(n+1)...p_k) is strictly positive because Dirichlet ensures infinitely many record primes r≡a mod m. Its upper bound (p_(n+2)−p_(n+1))/(2p_(n+1))+1/(2(p_(n+1)−1)) tends to zero by PNT and Bertrand. If delta=u/v rational, vT_n=vw_n−uP_n is a positive integer for every n yet tends to 0, contradiction. Delta is positive and irrational. Independently generated 8,857 records through P6+1=30031 and checked all 90 stated class-by-class recurrences for m=2,3,5,6,7,10,11,15. This finite confirmation is not the infinite proof.

## originality

PASS

Best-of-knowledge originality is the irrationality, for every squarefree modulus and every reduced class, of an already established natural-density record set. Basistha–Ionascu 2023/2025 proves primorial replication and the existence of the unrestricted density about 0.294, not its irrationality or the classwise irrational densities in the inspected primary theorem. Remark 2.25 discusses the irrationality of the distinct sum of reciprocal primorials, not the record density itself. OEIS and a Resultary result about a period-30 record-multiple pattern do not cover this claim. An unindexed equivalent irrationality proof remains possible.

## value

PASS

The arithmetic nature of a natural density arising from the canonical primorial recurrence is a precise open-looking structural invariant. Proving irrationality simultaneously in infinitely many reduced progressions upgrades a known existence/density theorem, and the positive vanishing tail argument exploits genuinely number-theoretic information rather than a numerical decimal observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
