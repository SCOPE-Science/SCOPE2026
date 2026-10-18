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

# Reproduction and limits

From the directory containing the files, run:

```text
python3 verify_switch.py
python3 verify_graph.py
```

Both programs use Python's standard library only and exact arbitrary-precision integers. `verify_switch.py` computes matching polynomials by path recurrences, checks the transfer-matrix switching identity in 73 parameter cases, checks the exact common-neighbour law in 1,005 parameter/partition instances, and computes the finite collision census through matching size 25. `verify_graph.py` independently counts forbidden-edge-avoiding perfect matchings by recursive bitmask enumeration in thirteen instances and independently computes rooted derangement-orbit refinement for sizes three through seven. Recorded standard output is included in `verification_output.txt`.

The mathematical theorem is proved for every integer \(m\ge2\) and every finite residual integer partition \(\rho\); these checks are finite corroboration and do not prove the quantified result. The odd-size conclusion asserts non-separation **after two rounds**, not permanent non-separation. The orbit classification uses the already published full automorphism-group result for the matching derangement graph, so it is not an independent new automorphism-group theorem.

No independent audit or external certification has been performed.
