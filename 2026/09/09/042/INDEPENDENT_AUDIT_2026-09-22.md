# Independent audit — 2026-09-26

Record: `2026/09/09/042`. Verdict: **correctness PASS; originality PASS (bounded tabulation); scientific value PASS (bounded).** Disposition: retain accepted.

## Correctness
I separately formed the real 2×2 rotations with tr(A)=2cos(pi/p), tr(B)=2cos(pi/q) and conjugation scale mu=t+sqrt(t²−1), then enumerated nonbacktracking words to length 10 with the stated self-inverse order-two convention. Vectorized matrix products over all 24 hyperbolic triples reproduced every reported trivial/elliptic/hyperbolic count and minimum absolute trace to 12 decimal places; no residual nontrivial parabolic occurred. In particular (2,4,5) gave (45,1353,1672), min 2.288245611271, while (6,6,6) gave (37,2900,115160), min 4.732050807569. The totals are 3070 or 118097 as claimed. Independently composing affine Euclidean isometries with exact rotation exponent mod lcm(p,q) reproduced (3,3,3): 1969/78892/37236, (2,4,4): 69/2277/724, (2,3,6): 59/2567/444 for identity/rotation/translation. The minimum trace relation gives the stated translation lengths. Numerical separation from |tr|=2 is broad for the hyperbolic minima, though this is floating computation and not formal interval arithmetic.

## Prior work and originality
The triangle group embeddings, trace-to-length formula, and global geometric systole questions predate this work. The open paper *Détermination géométrique de la systole des groupes de triangles* (2011), DOI 10.1016/j.crma.2011.10.015, already gives a formula for shortest geodesic loops of certain triangle orbifolds; Schein and Shoan, arXiv:2012.08796, compute systolic bounds for congruence subgroups. This table's stated novelty is only its chosen generator model, nonbacktracking word bound 10, full type counts, and Euclidean contrast, not a global minimum theorem. I did not establish precedence for the exact complete 24-row bounded table.

## Scientific value and limits
The reproducible word census is a small benchmark for trace enumeration and boundary behavior. Every minimum is explicitly *within* length 10 in this generating set; it cannot be promoted to a group systole. The published numerical gaps are between distinct values in this bounded enumeration, not certified separations of global spectra.

Sources: RESULT.md and output/artifacts/census.py, replay_verify.py; https://arxiv.org/abs/2012.08796; https://doi.org/10.1016/j.crma.2011.10.015.
