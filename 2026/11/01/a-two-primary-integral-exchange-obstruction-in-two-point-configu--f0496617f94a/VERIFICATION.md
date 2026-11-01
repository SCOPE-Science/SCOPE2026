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

# Reproduction and boundaries

Run `python3 check_integral_exchange.py` using standard Python 3. No external packages, network access, or downloaded datasets are required. It constructs the connected crown graph with directed edges from the first to the second vertex class, chooses a spanning tree, and generates the exact integer fundamental-cycle basis from each non-tree edge.

It checks both independent row and column zero-boundary equations for every basis cycle, computes the mod-two image of the parity map, confirms the even-degree/even-edge constraints, independently checks that images of explicit four-cycles span the same image, and checks the conjugacy-class trace identities of arm permutation and particle exchange. It never approximates rational matrix ranks by floating-point arithmetic. A passing invocation reports:

```
n=3 | H1 rank=1 | mod-2 gluing dim=0 | index=2^0 | conjugacy types=3 PASS
n=4 | H1 rank=5 | mod-2 gluing dim=2 | index=2^2 | conjugacy types=5 PASS
n=5 | H1 rank=11 | mod-2 gluing dim=5 | index=2^5 | conjugacy types=7 PASS
n=6 | H1 rank=19 | mod-2 gluing dim=9 | index=2^9 | conjugacy types=11 PASS
n=7 | H1 rank=29 | mod-2 gluing dim=14 | index=2^14 | conjugacy types=15 PASS
n=8 | H1 rank=41 | mod-2 gluing dim=20 | index=2^20 | conjugacy types=22 PASS
All exact checks passed.
```

The code tests six finite arm counts, not the general theorem. The unrestricted proof is in `RESULT.md`, specifically the two natural acyclic-intersection nerve reductions and the parity-kernel/four-cycle spanning arguments. The role of the published weighted-graph and rational representation calculations is delineated there. There has been no independent mathematical audit.
