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

For each (k−1)-word v, successors of states av must be v(a⊕ε_v) with a common ε_v, since successor map is a permutation. Conversely a mask defines a permutation, and a single 2^k-cycle gives one de Bruijn cycle up to rotation. Uncrossed windows have equal first/last bits and thus a border; crossed windows contribute c_k(v). All-zero mask is cyclic word rotation partitioned by N_k necklaces; switching one ε composes a transposition, so attaining one cycle needs >=N_k−1 flips of the prescribed parity. At k=5, independent exhaustive loop over all 2^16 masks visited permutation orbits and accepted exactly 2048 single cycles, reproducing eight-cell distribution and moments; 4 weight-two v values verified. Exhaustion of all 65,536 masks is finite exact certificate for order five; no extrapolation needed for all-order identities.

## originality

PASS

Best-of-knowledge PASS for all-order weighted local transition identity plus complete nonconsecutive order-five unbordered-factor spectrum; classical total 2048 de Bruijn count and general de Bruijn permutation representations are known and not claimed as new. No inspected equivalent unbordered-factor spectrum, but specialized catalogues or unindexed combinatorics-on-words work remain a priority risk.

## value

PASS

A binary order-k de Bruijn cycle contains all length-k factors, making the next length k+1 the first nontrivial diversity scale. Complete order-five unbordered spectrum, excluded value 16, exact moments and all-order crossing-weight relation are natural concrete combinatorics-on-words invariants rather than arbitrary table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
