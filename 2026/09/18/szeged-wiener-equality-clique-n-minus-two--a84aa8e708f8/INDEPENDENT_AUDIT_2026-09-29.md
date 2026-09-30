# Independent audit — 2026-09-29

Record: `2026/09/18/szeged-wiener-equality-clique-n-minus-two--a84aa8e708f8`  
Assigned and audited source tree: `820386a39f42d4d7fe3159fbfa68eabf01f3a2c5`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Disposition: **passed**

## Correctness

**independently_reproduced**. The three four-parameter formulas and the equality classification check from the definitions. I independently reconstructed every graph type, computed all-pairs distances, W and Sz, and exhaustively tested every two-connected parameter tuple with clique size q=2,…,10 for both xy adjacent and nonadjacent; there were no formula failures. For orders n≥10 in that range, the only equality tuples are the Zhang–Li family (a,b,c,d)=(1,1,n-4,0) with xy adjacent and, at n=10, the two label-swapped tuples (0,1,6,1) and (1,0,6,1), exactly the stated J_10 type. The algebraic case split in the record then excludes all further n≥10 tuples.

## Originality

**qualified_recent_problem_progress**. Zhang–Li's September 17, 2026 preprint proves the 2n lower bound, constructs equality examples for every n≥10, and explicitly leaves the necessary-and-sufficient equality classification as a problem. The older 2017 work concerns the 2n−6 equality theory. Current searches did not locate the present complete high-clique (ω≥n−2) classification. The contribution is supported as a partial solution of an extremely recent open problem, with substantial concurrency risk.

## Scientific value

**meaningful_partial_classification**. The record gives exact Szeged–Wiener formulas for the entire n−2-clique regime and completely solves equality there, proving uniqueness of the Zhang–Li family for n≥11 and isolating the extra n=10 graph. This is a nontrivial structural slice of the global equality problem rather than a finite example.

## Evidence and literature checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/18/szeged-wiener-equality-clique-n-minus-two--a84aa8e708f8
- https://arxiv.org/abs/2609.20025
- https://arxiv.org/abs/1602.05184

## Limitations

- The theorem only treats graphs with clique number at least n−2.
- The global Zhang–Li equality problem remains open.
- The motivating problem was only days old when the record was committed, so simultaneous work is a serious originality risk.
