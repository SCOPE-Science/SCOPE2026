---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For W_n=K1 join C_n (n>=5), graph diameter two. A hub-free set is GP exactly when its cyclic binary rim word avoids 111. Inclusion maximality forces every 1-run to have length 1 or 2, every 0-run length 1 or 2, and a 00-run precisely between two 11-runs; at least three selected rim vertices preclude adding hub. Hub-including maximal GP sets are exactly the n edge-plus-hub triples. The 2x2 transfer matrix indexed by selected-run sizes 1,2 has entries [[u²z,u²z],[u³z²,u³z²+u⁴z²]], determinant det(I-T)=1-zu²-z²u³-z²u⁴+z³u⁶, and rooted cycles are counted by n sum tr(T^t)/t; this proves A_n(z)=nz³-n[u^n]log det(I-T) for every n>=5. Simple b_i<=a_i constraints plus cyclic run counting yield the stated exact minimum/maximum rim subset multiplicities. Reciprocal polynomial substitution x+1/x shows only one expanding root α=1.401268..., four unit roots and one reciprocal, giving A_n(1)=n+α^n+O(1). Independently enumerated every subset of wheels n=5,...,12 using true graph geodesic triples and checked the maximal-set coefficients and extremal counts, not merely the transfer recurrence. Those finite tests support but do not substitute for the all-n run-decomposition proof.

## originality

PASS

Existing general-position polynomial of graph joins enumerates ALL GP sets, not inclusion-maximal ones; wheel largest-cardinality GP formula does not classify maximal set spectrum. Hub-free part is equivalent to maximal dissociation sets in C_n; Tian–Tu 2024 enumerates maximal dissociation sets in cyclical grid graphs and may imply the total number for cycle specialization, but the full graded polynomial and extremal coefficient classification are not identified in inspected material. Best-of-knowledge PASS with major historical-priority risk honestly recorded.

## value

PASS

A natural graph-family full inclusion-maximal-set polynomial, its sharp smallest/largest coefficients and exponential enumeration rate provide more information than previously known scalar GP number. The cyclic transfer method isolates a nontrivial boundary condition for consecutive 00 gaps; the exact counts are useful as extremal combinatorial benchmarks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
