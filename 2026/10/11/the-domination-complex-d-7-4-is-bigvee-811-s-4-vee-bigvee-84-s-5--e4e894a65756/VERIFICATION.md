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
The verification artifact reconstructs every labeled simple graph on seven vertices and tests the domination-number predicate directly. It obtains \(17{,}388\) nonempty faces with edge-count profile \((21,210,1330,4515,7077,3605,630)\) and confirms there are no larger faces.

It rebuilds the successive-toggle matching, checks all \(83{,}895\) Hasse cover relations, and topologically sorts the modified Hasse graph. The matching has \(8{,}210\) pairs and critical-cell counts \((1,847,120)\) in dimensions \((0,4,5)\).

The signed gradient-path recurrence reconstructs the integral Morse boundary \(\partial_5\). Exact arithmetic gives rank \(36\), and a specified \(36\times36\) minor has determinant \(-1\). Consequently every nonzero Smith invariant is a unit. Independent mod-\(2\) simplicial boundary ranks are \((20,190,1140,3375,2891,630)\), yielding reduced Betti ranks \(811\) and \(84\) in degrees \(4\) and \(5\), with all others zero.

The checker proves only this finite case. It does not infer a formula for other bounded-domination complexes and it does not treat literature search as mathematical evidence for correctness.
