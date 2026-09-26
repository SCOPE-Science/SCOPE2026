# Independent audit — 2026-09-22

Record: SCOPE-20260909-022. Examined 2026-09-26.

## Correctness — PASS
I fetched the committed C enumerator and data, compiled and reran it for T5 and M6. The newly generated tables match the committed SHA-256 hashes `d9d3ee25e6a1d1afe7628c15b382d718cb0851aeca5e3d0026659950a9b280bf` and `d538c23cb1095e30088010b7963a3c85b31aeddeb3256f4c4d0787727b46689d`. Totals and nonempty profile cells are 7,579/94 and 7,741,776/362. The supplied verifier returned `VERIFY_OK`, including a separate pure-Python T5 recount, direct checks of all 456 profile witnesses, complementary symmetry, marginal distributions and exact coverage by the supplied 10-chain/20-chain partitions. The chain partitions plus full middle-rank antichains prove the stated widths 10 and 20. M6 has same-code replay and independent certificate/marginal checks, but no second full enumerator.

## Originality — PASS, narrowly
OEIS A000372 tabulates total antichains, and A059119 tabulates counts by antichain size. De Causmaecker–De Wannemacker give interval methods and totals. These checked sources do not provide the joint counts indexed by rank-layer profile in the two stated slices. The widths alone are immediate from Sperner theory; the 94- and 362-cell tables are the finite contribution.

## Scientific value — PASS, bounded
The tables quantify interactions among ranks that totals and single-size distributions lose (for example, M6 profile `(1,8,0)` has 193,050 antichains, while `(0,10,0)` has 184,756). Exact witnesses, full distributions and width certificates make the bounded middle-rank cases reusable as benchmarks. There is no general theorem for larger Boolean lattices.

Sources: [OEIS A000372](https://oeis.org/A000372), [OEIS A059119](https://oeis.org/A059119), [De Causmaecker–De Wannemacker, arXiv:1407.4288](https://arxiv.org/abs/1407.4288). Repository evidence: `artifacts/enum.c`, both profile CSVs, witness CSVs, chain CSVs, and `verify.py`.
