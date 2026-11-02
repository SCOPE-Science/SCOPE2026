---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For every N>=1, fixed g in (0,1), a=1-g, the given homogeneous single-site rotation Ad_{R_N} commutes with the replacement/shift E_N(X)=(I/2) tensor Tr_N X. Direct tensor computation gives E_N^k(X)=(I/2)^tensor k tensor Tr_last-k(X), and E_N^N=D_N. Therefore T_N^t is a final unitary rotation followed by a Binomial(t,g) mixture of E_N^k. Unitary invariance of half diamond distance and maximal channel distance 2 gives uniform all-ancilla upper tail P(K<=N-1). A product input |0>^tensor N and a rightmost-L all-zero projector yields trace-distance witness P(K<=N-L)-2^{-L}, so the same holds for the diamond distance, even though the lower witness uses no ancilla. Choosing L=floor(N^(1/4)) yields vanishing projector baseline and L=o(sqrt N); the binomial triangular-array CLT at t=floor((N+s sqrt(N(1-g)))/g) squeezes to Phi(-s). CPTP contractivity gives monotone mixing times and the stated inverse-quantile N/g - Phi^-1(epsilon) sqrt(N(1-g))/g +o(sqrt N); endpoint g=1 saturates at t=N and g=0 remains unitary. Fresh independent binomial/measurement calculations verified finite-size inequalities for N=1..6 and g=1/4,1/2,2/3 and sampled normal profile at N=200, which corroborate rather than prove the infinite CLT.

## originality

PASS

Fresh best-of-knowledge statement-and-implication comparison across standard aliases, general theorems and exact tables. Inspected primary material does not establish the same final claim at the assessed level, although stated full-text access gaps and unindexed equivalences leave explicit priority risks. Once full shift-binomial decomposition is granted, upper tail is elementary; the matching trace/diamond lower witness and inversion are substantive additional results. Since the highly relevant same mathematical model full text is inaccessible, priority is best-of-knowledge and explicitly qualified, not certified.

## value

PASS

A sharp global *operational* mixing-time window in diamond norm, including arbitrary entangled reference systems, is a natural quantum-information invariant. The analytic Gaussian profile quantifies a sharp cutoff for a nonnormal quantum shift where the set of nontrivial multiplier moduli by itself fails to encode system-size mixing. Unlike a local observable bound, it resolves full distinguishability, including worst-case ancillary choices, in a physical model with exact finite-size Bernoulli erasure structure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
