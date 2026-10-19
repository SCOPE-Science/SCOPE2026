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

# Reproducibility and scope

Run the two self-contained scripts with Python 3:

```
python3 verify_incidence.py
python3 verify_lcf.py
```

Compare their entire output against `verify_incidence.out` and `verify_lcf.out`. The first algorithm enumerates each \(k\)-subset in affine point–line incidence coordinates, tests closed-neighborhood domination, then enumerates each injective old-to-new guard assignment via recursive bitmask search. It checks the explicit automorphisms and the single orbit of eighteen five-sets. The second builds the graph from the independent LCF representation `[5,7,-7,7,-7,-5]` repeated three times, represents candidates as sorted combinations, and tests movement with destination-subset dynamic programming. Exact assertions force both to reproduce the same finite counts.

The checked domain is **all** \(\binom{18}{4}\), \(\binom{18}{5}\), and \(\binom{18}{6}\) vertex subsets, respectively. For every surviving five-/six-vertex dominating placement, the checker examines every unattacked/unoccupied vertex and all possible legal one-step guard movements to another dominating placement of the same size. In particular, 5,076 six-placement/attack pairs have valid responses, and their response counts range from 25 to 81. Once every such state has the property, induction gives the infinite-horizon game bound. The scripts do not establish novelty, universal statements for other graphs, or independent external certification.
