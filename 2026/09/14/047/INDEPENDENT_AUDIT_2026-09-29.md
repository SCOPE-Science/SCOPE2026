# Independent audit — 2026/09/14/047

**Date:** 2026-09-29  
**Disposition:** **REPAIRED**  
**Audited tree:** `a2ed2d3d37b26bc86633e35d7130117dffd01ae6` at repository commit `253a0fe5d0217455660a277f9adb940030e567ad`

## Correctness

**PASS** — Independent reconstruction of both stated K3,3 signings gives connected 12-vertex lifts of girth 4 with signed spectral radius 2.5615528128 < 2sqrt(2), exactly ten 4-cycles, and an inconsistent rank-6 GF(2) shortest-cycle system. The K_{d,d} three-equation contradiction and the cube 128/4096 census are consistent with the supplied exact/enumerative artifacts. The only repair needed is reproducibility metadata/path wording.

## Originality

**PASS_WITH_CAUTION** — MSS supplies Ramanujan 2-lift existence and Hoory studies girth of graph lifts, but targeted comparison found no statement of the explicit 12-vertex one-step frozen Ramanujan witness or the rank-6 certificate. This supports originality of the explicit witness, not a general priority claim.

## Value

**PASS** — The witness gives a concrete branch-choice obstruction for greedy Ramanujan/girth tower construction and the contrasting cube census shows the obstruction is not vacuous. Its one-step limitation is clearly stated.

## Literature/evidence checked

- [Marcus–Spielman–Srivastava, Interlacing Families I](https://arxiv.org/abs/1304.4132): Ramanujan 2-lift existence; no girth-control certificate.
- [Hoory, On the Girth of Graph Lifts](https://arxiv.org/abs/2401.01238): General graph-lift girth results; no exact frozen Ramanujan witness found.

## Limitations of this audit

Literature comparisons are claim-specific and do not constitute an exhaustive priority proof. GitHub was read only. Computations described as independent were reconstructed from stated finite data or supplied artifacts; no inaccessible paper is claimed as read.
