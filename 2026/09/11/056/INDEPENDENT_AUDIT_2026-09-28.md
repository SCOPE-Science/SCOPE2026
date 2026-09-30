# Independent audit — 2026-09-29

Record: `2026/09/11/056`  
Audited tree: `69a6d34028b9f2703252a0179c58cbc5abf8a0c0`  
Disposition: **repaired**

## Correctness

The ATLAS HN page lists the same 14 maximal-subgroup conjugacy classes and indices, including two classes of `M12:2` at index `1,436,400,000`. Exact rational recomputation gives
`sum 1/m_i = 6979253/4266108000000`. Therefore the union bound yields
`P2(HN) >= 4266101020747/4266108000000`. A fixed `A12` conjugate has index
`1,140,000`, so every pair inside it is non-generating and
`P2(HN) <= 1 - 1/1140000^2 = 1299599999999/1299600000000`.
The stated interval and width are correct.

## Originality

The interval is a direct finite consequence of a published maximal-subgroup classification plus a standard union bound. Targeted search found general sporadic random-generation work but did not establish that this is the first published numerical HN interval. The staged repair removes the unsupported priority wording while retaining the exact benchmark.

## Scientific value

The result is modest but useful: it turns the complete HN maximal-subgroup ledger into a transparent, reproducible rigorous probability certificate with exact rational endpoints.

Sources: https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/11/056 ; https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/HN/ ; https://doi.org/10.1016/j.aim.2013.07.009
