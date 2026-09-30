# Independent audit — 2026-09-28

Record: `2026/09/11/036`  
Audited tree: `a5a1c2c2ae881ded6dd044da9b70cb594ff4f6aa`  
Disposition: **repaired**

## Correctness

A fresh implementation reproduced `τ=4`, exactly 25 disjoint edge pairs with a third edge in every six-vertex union, the full rational Hochster Betti table, and `reg_Q=4`. The top homology witnesses are masks 511 and 383. Mask 383 is `{0,1,2,3,4,5,6,8}`; the old slogan incorrectly wrote vertex 7 in place of 6.

## Scope repair

The original package repeatedly called the example “extremal” without proving a minimality, maximality, facet, or classification statement. The guarded change set removes that unsupported adjective while preserving the exact tuple and certificates.

## Originality and value

Targeted searches found general work on Betti/regularity phenomena, including Bolognini–Macchia–Strazzanti–Welker, but no exact copy of this edge set or tuple. The scientifically defensible value is a compact reproducible finite witness, not an extremality theorem.

Sources: https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/11/036 ; https://arxiv.org/abs/2201.00571
