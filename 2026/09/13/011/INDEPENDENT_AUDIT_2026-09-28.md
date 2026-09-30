# Independent audit — SCOPE-20260913-011

Date: 2026-09-28 (UTC)  

## Disposition: PASSED

### Correctness
The disproof is elementary and complete under the target’s own droplet definition. On a finite torus, closure under every +e_i step forces any nonempty set to contain the whole forward orbit of one point, which is the entire torus. Hence no proper cube is forward-closed. For a proper product cube and an exterior vertex x, at most one forward neighbour x+e_i can lie in the cube, because every missed coordinate other than i remains missed. Therefore a forward-2 update cannot create the first exterior infection and the cube is sterile. Since floor(F log n) is eventually between 1 and n-1 for every fixed F>0, the specified forward-closed deterministically expanding cube cannot exist for large n. This alone refutes the conjunction without deciding the true percolation window.

The reproducibility text points to `output/artifacts/verify_droplet_lemmas.py`, while the actual repository path is `artifacts/verify_droplet_lemmas.py`; this is a non-scientific path typo and does not affect the proof.

### Originality
Low. The decisive observation is a short group-orbit/product-cube argument, not a new threshold theorem. The record is best understood as exposing an internally incompatible droplet requirement.

### Scientific value
Useful as a rigorous negative check on an overconstrained target; limited as bootstrap-percolation research because it leaves the probabilistic window untouched.
