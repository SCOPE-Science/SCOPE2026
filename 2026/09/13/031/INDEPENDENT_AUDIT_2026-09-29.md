# Independent audit — 2026-09-29

Record: `2026/09/13/031`  
Audited source tree: `0debfda3f55d9b9f39fae596a5c11f8250dbc840`  
Disposition: **passed**

## Correctness

The map-specific argument is coherent. The duplication map acts by folded doubling on the Tate skeleton quotient, its off-skeleton components are open Berkovich disks, and type-II attachment points over C_5 have rational normalized skeleton coordinates because the value group is 5^Q. Those boundary points are therefore preperiodic under folded doubling. Once a boundary is periodic, the tangent-direction map is defined over a finite residue-field extension; each residue direction lies in a finite further extension, so its orbit is finite. This gives preperiodicity of every off-skeleton disk and excludes wandering disks. The record's sentence that every attracting cycle attracts a critical point is not true for arbitrary non-Archimedean maps, but the needed statement does hold here because residue characteristic 5 is strictly larger than degree 4, matching the sharp 2026 critical-point criterion.

## Originality

Rivera-Letelier's 2026 work explicitly notes rational wandering Lattès examples when the Q-rank of the value group is at least 2. The present C_5 value group has Q-rank 1, so that construction does not settle this case. A focused search did not locate this exact q=5 duplication-map no-wandering analysis; that absence is not treated as a priority proof.

## Scientific value

The record isolates a concrete rank-one Lattès map just outside the known higher-rank wandering mechanism and gives an explicit skeleton/direction argument for no wandering. This is scientifically useful as a sharply specified boundary case, while relying on standard Berkovich dynamics theorems.

## Limitations

- The audit did not derive a closed-form rational expression for the Lattès map; it checked the argument through Tate uniformization and the induced skeleton/tangent dynamics.
- The no-attracting-cycle step must be read with the map-specific residue-characteristic condition p=5>deg(L)=4, not as an unconditional theorem for all non-Archimedean rational maps.
- The published reproducibility text uses output/artifacts/tent_ledger.py while the archived file is at artifacts/tent_ledger.py; this is a packaging path mismatch, not a mathematical defect.
- The exact originality of this single-map conclusion remains qualified rather than established by a priority search.

## Sources checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/13/031
- https://arxiv.org/abs/2505.09383
- https://doi.org/10.1112/blms.70299
- https://arxiv.org/abs/2601.12163
