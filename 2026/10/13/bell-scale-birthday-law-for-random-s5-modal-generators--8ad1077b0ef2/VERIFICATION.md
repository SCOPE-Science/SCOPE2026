---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

A world's word and its class's palette determine truth by induction: the diamond tests the existence of a satisfying word in that palette. A depth-one test isolates each feasible signature. Thus all singleton sets are generated iff blocks are internally injective and their palettes are distinct. For a fixed partition this gives the falling factorial for choosing different palettes among blocks of the same size and s! bijections per block. Across all partitions a successful assignment is exactly a family of distinct nonempty palettes of total size n and a bijection from its n colored positions to the worlds, giving the coefficient and the n! factor. For H_n within-block pairs, contracting the prescribed one or two distinct pairs (whether disjoint or sharing a vertex) gives the Bell ratios in its first two factorial moments; the analogous triple contraction gives E sum_C |C|^3=O(nw_n^2). Fixed-shift Bell ratios imply H_n/(nw_n) tends in probability to 1/2. Conditional pair-collision indicators are independent off the dependency graph joining pairs that meet, and adjacent joint probabilities are Q^-2; the Stein–Chen error is bounded by C sum_C |C|^3/Q^2. It tends to zero in mean at critical scale, hence gives the claimed Poisson law for within-block collisions. For different blocks s<=t, t>=2, condition on the first palette: matching requires all t draws in at most s colors, with probability at most (s/Q)^t<=st/Q^2 when Q>=n. Singleton pairs have expected count binom(n,2) B_(n-2)/B_n. This gives a vanishing cross-block contribution at and above critical scale. The zero atom converges by the integer-valued law; above critical scale Markov bounds within-block collisions, and below it the conditional no-repeat probability is at most exp(-H_n/Q). The critical conclusion is along diverging admissible subsequences, not a claim that an allowable power-of-two sequence achieves a prescribed limiting ratio over every n. An independent replay checked 4509 Boolean-modal closures, 59473 frame/color assignments for both counts, and the moment identities through n=8.

## originality

PASS

The fixed-frame success condition is a distinguishing coloring of a disjoint union of cliques, and the graph-coloring and occupancy ingredients are classical. The supported distinct claim is their combination with the labeled Bell frame law and the asymptotic count of all modally indistinguishable pairs, including control of cross-class equal palettes. Exact indexed matches exist on later displayed dates; they establish mathematical equivalence but not earlier coverage of the assigned record. The inspected same-day deterministic-frame result has different assumptions and conclusions.

## value

PASS

For a standard random finite modal frame the result quantifies how many random propositions suffice to generate every subset and gives the law of the remaining indistinguishable pairs at the transition, not just an existence threshold. The exact labeled count serves finite sizes; the limit separates within-class birthdays from extra indistinguishability between classes. This is a natural random-generation invariant with a sharp quantitative answer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
