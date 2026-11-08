---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For k=2^j with j>=1 and both cut sizes a,b>=k−1, computational basis phase is (−1)^{binom(w,k)}=(−1)^{bit_j(w)} by Lucas. Local block bit phases are removed, and the carry sign F_rs=1−2·1_{r+s>=k} yields exact k×k residue coefficient matrix K_rs=2^{−(a+b)/2}sqrt(N_a(r)N_b(s))F_rs. Distinct row differences imply det F=±2^{k−1}; all residue weights positive, so Schmidt rank k exactly. As a,b grow independently at fixed k, residues equidistribute and K→F/k. Then FF^T has entries k−2|r−s|; the antiperiodic discrete Laplacian L satisfies L(FF^T)=4I, eigenmodes give λ_h=[k²sin²((2h−1)π/(2k))]^{-1}, purity 1/3+2/(3k²). Finally pairing odd endpoint frequencies and dominated convergence using q^{-2}(1+log q) yields the iterated Shannon entropy log₂(π²/4)−2/3−12ζʹ(2)/(π²ln2)=2.2808853887532333… bits. k=2 boundary is handled by seam cancellation. Independent direct computational-basis SVD versus K gave discrepancies at most 1.89e−15 in six cases k=2,4,8; independent high-precision odd-series entropy matched the displayed constant. No simultaneous growing-(k,a,b) assertion.

## originality

PASS

Best-of-knowledge PASS for exact arbitrary-eligible-cut Schmidt spectrum, fixed-k trigonometric limiting spectrum, and finite entropy despite unbounded rank in an iterated dyadic-arity limit. Hypergraph-state phase definitions and symmetric-state entanglement methods are established; checked prior research emphasizes geometric multipartite entanglement, one-qubit measures, or rank bounds rather than this full cut eigenvalue law.

## value

PASS

Complete symmetric dyadic hypergraph states are natural highly structured quantum many-body objects. An exact full Schmidt spectrum across arbitrary cuts and a finite limiting von Neumann entropy with growing Schmidt rank give quantitatively meaningful entanglement invariants beyond a mere rank lower bound or numerical estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
