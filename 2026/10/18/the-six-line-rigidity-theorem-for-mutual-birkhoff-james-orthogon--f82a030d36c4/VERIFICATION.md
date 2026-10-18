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

# Verification of the six-line orthograph theorem

The exact all-real-vector proof is in `RESULT.md`; there are no unresolved nonstandard analytic lemmas. The key coordinate criterion uses the entire subdifferential of the real \(\ell_1\) norm and treats zero coordinates correctly. The upper bound follows from a disjoint support classification, and the lower bound from six explicit bidirectionally orthogonal projective lines.

Replay the standalone Python standard-library checker from this package with `python3 CHECK.py`. It compares the signed-support criterion to exact minimization of the piecewise-linear norm over every rational breakpoint, checks all 2466 ordered pairs of primitive projective integer vectors with coordinate bound two for dimensions one through three, and uses a separate finite-graph clique search. Observed output:

```
dimension=1 vertices=1 clique=1 maximum_orbits_on_grid=1 search_nodes=2
dimension=2 vertices=8 clique=2 maximum_orbits_on_grid=2 search_nodes=10
dimension=3 vertices=49 clique=6 maximum_orbits_on_grid=1 search_nodes=97
VERIFY_OK direct_piecewise_pairs=2466
```

The grid is not an exhaustive collection of projective real lines, so the computational results do **not** independently prove the real-variable theorem. The proof in `RESULT.md` supplies all infinite-quantifier steps. The 2022 review literature risk and lack of an independent scientific audit remain as described in `REVIEW.md`.
