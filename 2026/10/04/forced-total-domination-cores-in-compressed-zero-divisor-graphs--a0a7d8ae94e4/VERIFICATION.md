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

It constructs the simple valuation graph with vertex set
\[
\prod_i\{0,1,\ldots,\ell_i\}
\setminus
\{(0,\ldots,0),(\ell_1,\ldots,\ell_r)\}
\]
and adjacency given by the coordinatewise thresholds
\[
a_i+b_i\ge\ell_i.
\]
It checks every claimed unique-neighbor witness, exhaustive total minima, and exhaustive paired minima over the tested parameter boxes.

A second layer of the checker constructs actual rings
\[
\prod_i \mathbb Z/(2^{\ell_i})
\]
from multiplication tables, computes annihilator sets directly, forms equivalence classes, and verifies that their simple compressed graph agrees with the valuation graph.

Exact replay output:

```text
(1,): empty graph
(2,): one isolated vertex; no total/paired domination
(3,): |V|=2 gamma_t=2 min_total=1 gamma_pr=2 min_paired=1
(4,): |V|=3 gamma_t=2 min_total=2 gamma_pr=2 min_paired=2
(5,): |V|=4 gamma_t=2 min_total=3 gamma_pr=2 min_paired=3
(6,): |V|=5 gamma_t=2 min_total=4 gamma_pr=2 min_paired=4
(1, 1): |V|=2 gamma_t=2 min_total=1 gamma_pr=2 min_paired=1
(1, 2): |V|=4 gamma_t=2 min_total=1 gamma_pr=2 min_paired=1
(1, 3): |V|=6 gamma_t=2 min_total=1 gamma_pr=2 min_paired=1
(2, 1): |V|=4 gamma_t=2 min_total=1 gamma_pr=2 min_paired=1
(2, 2): |V|=7 gamma_t=2 min_total=1 gamma_pr=2 min_paired=1
(2, 3): |V|=10 gamma_t=2 min_total=1 gamma_pr=2 min_paired=1
(3, 1): |V|=6 gamma_t=2 min_total=1 gamma_pr=2 min_paired=1
(3, 2): |V|=10 gamma_t=2 min_total=1 gamma_pr=2 min_paired=1
(3, 3): |V|=14 gamma_t=2 min_total=1 gamma_pr=2 min_paired=1
(1, 1, 1): |V|=6 gamma_t=3 min_total=1 gamma_pr=4 min_paired=3
(1, 1, 2): |V|=10 gamma_t=3 min_total=1 gamma_pr=4 min_paired=7
(1, 2, 1): |V|=10 gamma_t=3 min_total=1 gamma_pr=4 min_paired=7
(1, 2, 2): |V|=16 gamma_t=3 min_total=1 gamma_pr=4 min_paired=13
(2, 1, 1): |V|=10 gamma_t=3 min_total=1 gamma_pr=4 min_paired=7
(2, 1, 2): |V|=16 gamma_t=3 min_total=1 gamma_pr=4 min_paired=13
(2, 2, 1): |V|=16 gamma_t=3 min_total=1 gamma_pr=4 min_paired=13
(2, 2, 2): |V|=25 gamma_t=3 min_total=1 gamma_pr=4 min_paired=22
(1, 1, 1, 1): |V|=14 gamma_t=4 min_total=1 gamma_pr=4 min_paired=1
(1, 1, 1, 2): |V|=22 gamma_t=4 min_total=1 gamma_pr=4 min_paired=1
(1, 1, 2, 2): |V|=34 gamma_t=4 min_total=1 gamma_pr=4 min_paired=1
direct R=product Z/(2^L), L=(3,): 2 compressed vertices OK
direct R=product Z/(2^L), L=(2, 1): 4 compressed vertices OK
direct R=product Z/(2^L), L=(2, 2): 7 compressed vertices OK
direct R=product Z/(2^L), L=(3, 1): 6 compressed vertices OK
direct R=product Z/(2^L), L=(3, 2): 10 compressed vertices OK
direct R=product Z/(2^L), L=(2, 2, 1): 16 compressed vertices OK
VERIFY_OK
```

These finite computations do not prove the arbitrary-ring theorem. The general proof is the symbolic chain-ring annihilator calculation together with the forced-core and matching arguments in `RESULT.md`.
