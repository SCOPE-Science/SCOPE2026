# Independent audit — 2026-09-26

Record: `2026/09/09/050`. Verdict: **correctness PASS; originality PASS (class-resolved profiles); scientific value PASS (bounded).** Disposition: retain accepted.

## Correctness
I independently enumerated determinant-one 2×2 matrices modulo ±I, constructing GF(27) from t³=t+2. The resulting group orders were 1092, 9828, 12180. For q=13,29 the order-2/order-3 populations were 91/182 and 435/812, and three order-7 trace-square types had 156 and 870 elements each. A fixed involution has 24 or 56 order-3 partners per order-7 type, giving N=2184 or 24360. For q=27 the populations were 351 involutions and 728 order-3 elements; conjugation divides the latter into two 364-element classes, and three trace-square order-7 classes contain 702 each. Every one of the six fibers has 28 partners, hence N=351×28=9828. Independent Cayley-closure BFS for *every partner* in all 12 fibers gave the full group order, a stronger direct check than one witness per class. The genus computations 1+|G|/84 give 14,118,146. M11 has order 7920 with 7∤7920, so the control is immediate by Lagrange. The archived long word spellings were not needed to establish existence once all pairs in each fiber were checked; their labels depend on chosen trace ordering.

## Prior work and originality
ATLAS lists the orders and relevant conjugacy classes and standard generators; L2(27)'s standard pair already has product order 7. Macbeath-type Hurwitz existence and Conder's quotient lists predate these calculations. The per-(2 class,3 class,7 class) pair constants and exhaustive generation profiles for this finite window are the bounded contribution. It is not a new Hurwitz existence criterion or a general PSL(2,q) theorem.

## Scientific value and limits
The exact class-resolved fibers and generating status can help enumerate epimorphisms, dessins and regular maps for these three groups. No orbit count under Aut(G), Nielsen equivalence, or complete surface classification is supplied. Counts are exact for the specified three groups only.

Sources: RESULT.md and output/artifacts/verify_hurwitz.py, verify_hurwitz_27.py; https://brauer.maths.qmul.ac.uk/Atlas/v3/lin/L213/; https://brauer.maths.qmul.ac.uk/Atlas/v3/lin/L227/; https://brauer.maths.qmul.ac.uk/Atlas/v3/lin/L229/; https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/M11/.
