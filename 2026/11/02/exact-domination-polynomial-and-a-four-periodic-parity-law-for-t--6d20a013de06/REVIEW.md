# Review of the three-row cylindrical king domination polynomial

## Correctness

**PASS.** The claim is an identity for the complete ordinary domination polynomial of the explicitly defined strong product \(P_3\boxtimes C_n\) for each integer \(n\ge3\). The proof compresses all column selections into four exact row-coverage classes, proves that domination is a local condition on every three consecutive columns, and identifies the complete counting polynomial with the trace of a specified finite transfer matrix. The factored characteristic polynomial is an exact determinant identity over \(\mathbb Z[z,X]\), not inferred from numerical values, and gives the nine-root formula. Specialization at \(z=-1\) gives the stated four-periodic values by explicitly listing the roots. A separately implemented vertex-neighborhood enumerator agrees with every coefficient for \(n=3,4,5,6\). The statement makes no claims about cycles of order one or two.

## Originality

**PASS, subject to publication-priority risk.** Moore and Mertens [1] prove the free-boundary king-graph parity identity and explicitly describe changed behavior under cyclic boundary conditions; their paper does not give this complete all-\(n\) polynomial formula or its characteristic factorization. Mertens [2] develops algorithms for Cartesian grid/cylinder/torus products and rectangular, noncyclic king graphs; neither the graph family nor the proved closed-form conclusion subsumes the present result. Klobučar [3] concerns independent rather than all dominating sets. Searches for strong products, cylindrical king graphs, signed domination polynomials, algebraic transfer formulas and mathematical research records found no matching complete theorem. The finite cylinder table in [1] takes the first coordinate cyclic, \(C_m\boxtimes P_n\), rather than \(P_3\boxtimes C_n\); thus its displayed \(m=3\) entries are not counterexamples or covered specializations of the present theorem. Residual priority risk: unindexed or alternate-notation equivalent results.

## Mathematical value

**PASS.** A 2024 result explicitly highlights how cyclic king-board boundaries destroy the free-board alternating-sum rule. The theorem determines the *entire* ordinary domination polynomial for one natural infinite cylindrical family with a fixed-degree algebraic expression, not merely its minimum degree or a handful of specializations. The striking exact jump of the even-minus-odd count from \(1\) to \(9\) when the circumference is divisible by four is explained by the factorization of a reduced transfer operator. The four coverage types also isolate a structural mechanism useful for nearby constant-width cyclic domination problems. No statement is made for wider cylinders.

## Sources and limitations

[1] C. Moore and S. Mertens, *Domination by kings is oddly even*, arXiv:2407.19344v1 (July 27, 2024), Sections 2–3 and the cylinder discussion.

[2] S. Mertens, *Domination Polynomials of the Grid, the Cylinder, the Torus, and the King Graph*, arXiv:2408.08053v1 (August 15, 2024), graph definitions, algorithm sections, and conclusion.

[3] A. Klobučar, *Independent sets and independent dominating sets in the strong product of paths and cycles*, Mathematical Communications 10 (2005), 23–30 (full text not obtained; publicly accessible abstract and journal metadata inspected).

The independent audit remains outstanding. A symbolic determinant check and bounded exhaustive graph checks are available in `verify.py`; neither is represented as independent external certification.

Self-review: passed. Independent audit: not yet performed.
