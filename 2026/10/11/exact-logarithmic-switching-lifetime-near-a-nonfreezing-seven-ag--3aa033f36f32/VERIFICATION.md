---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The packaged `check.py` script is a standalone exact-rational checker. Run `python3 check.py` from the directory containing this file and the script. The actual run covered 73 rational parameter pairs, 4,818 consecutive one-step evolution identities, directed neighborhood lists, switching-count formulas, equality thresholds, and exact switching-tail areas; it printed `PASS`.

The infinite-time statement has an independent analytic proof: for coefficient values \(-1/6\le u\le1\), \(0\le v\le1\), the source-to-target gap inequalities identify every possible outgoing neighborhood. Row averaging sends \((u,v)\) to \((-u/6,v/2)\), so this reachable rectangle and the exact mode decomposition are invariant. The center arcs appear if and only if \(v\ge3u\). At even instants this becomes \(b\ge3a9^{-j}\), while all odd instants include both arcs. Counting failures before the first satisfying even instant proves the sharp time law. Planar integration then proves the expectation and tail distribution.

Limits: the proof uses the stated inclusive confidence convention and the exact seven radii, with \(0\le a,b\le1\). A finite rational checker is neither exhaustive for real parameters nor independent formal verification. The count distribution assumes uniform Lebesgue area in the parameter square, not a dynamical random process. The original example and foundational fixed-topology facts are credited to their respective sources.
