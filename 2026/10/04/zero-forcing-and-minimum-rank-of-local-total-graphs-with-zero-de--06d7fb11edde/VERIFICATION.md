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

The standalone `verify.py` artifact was read from its packaged path before replay.

The checker directly constructs \(T_0(\Gamma(\mathbb Z/(p^k)))\) from the rule that two nonzero residues are adjacent exactly when their sum is divisible by \(p\). It verifies the predicted connected-component sizes in residue characteristic two and odd characteristic.

For every direct graph with at most \(15\) vertices, it exhaustively tests all subsets to obtain both the zero forcing number and the number of minimum zero forcing sets.

It also builds the block matrices used in the proof and computes their ranks exactly over rational arithmetic. A second, noncyclic local ring,
\[
\mathbb F_2[x,y]/(x,y)^2,
\]
is constructed independently and exhaustively checked.

Exact replay output:

```text
Z/4: |V|=3 components=[1, 2] exhaustive Z=2 min_sets=2 witness_rank=1
Z/8: |V|=7 components=[3, 4] exhaustive Z=5 min_sets=12 witness_rank=2
Z/16: |V|=15 components=[7, 8] exhaustive Z=13 min_sets=56 witness_rank=2
Z/9: |V|=8 components=[2, 6] exhaustive Z=5 min_sets=18 witness_rank=3
Z/27: |V|=26 components=[8, 18] structural Z=23 predicted_min_sets=648 witness_rank=3
Z/25: |V|=24 components=[4, 10, 10] structural Z=19 predicted_min_sets=2500 witness_rank=5
F2[x,y]/(x,y)^2: |V|=7 components=[3, 4] exhaustive Z=5 min_sets=12 witness_rank=2
VERIFY_OK
```

The finite checks do not establish the general theorem. The arbitrary-ring result follows from the published coset-component structure, direct forcing arguments for clique and balanced biclique components, the explicit real symmetric rank witnesses, and the standard inequality \(M(G)\le Z(G)\).
