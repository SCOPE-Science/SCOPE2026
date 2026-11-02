# Scientific review — arithmetic specialization of Fermat-quartic sextactic points

## Correctness: PASS

For the exact integral ideal \((F,G)\) displayed in `RESULT.md`, all geometric fibers away from 2 and 3 consist of 48 distinct transverse points (twelve four-line factors, four points per line). In characteristic 3, the verified polynomial identity \(G\equiv(X^4-Y^4)^3\pmod F\) makes the zero-dimensional scheme the third Cartier thickening of a reduced degree-16 divisor on a smooth plane quartic. The completed local algebras are \(k[[t]]/(t^3)\). In characteristic 2, fourth Frobenius powers give the three reduced support points with completed local algebras \(k[[u,v]]/(u^4,v^4)\). Bézout plus proper quasi-finiteness and the constant-fiber-length criterion over a DVR give finite flat rank 48. An exact standard-library script checks the key identities, the 28/16/12 Hermitian rational-point partition, and the three characteristic-two support points. The script's finite checks do not replace the universal algebraic steps.

## Originality: PASS, with historical priority risk

Merta–Zieliński (arXiv:2410.13997, first public 2024-10-17, Section 4.1) establishes the 48 complex proper sextactic points and their exact complete-intersection ideal; this input is explicitly prior work. Toft–Moe (arXiv:2412.16993, first public 2024-12-22, Sections 2.2.4 and 3.1) establishes related complex Fermat-curve pencil geometry, including the 16 triple points of its three four-line pencils. Those results do not give the scheme-theoretic reductions in characteristics 2 and 3, their completed local rings, or the characteristic-three identification with the non-coordinate Hermitian rational-point locus. Relevant complete sections of these primary papers and available published-result searches were compared for implication, not merely matching keywords; no covering statement was found. A prior unindexed modular calculation remains possible. The abstract Hermitian point count is classical and is not claimed as new.

## Mathematical value: PASS

This is a complete exceptional-characteristic classification of the natural integral model of a distinguished 48-point sextactic configuration. The two very different nonreduced limits (16 curvilinear points of length 3 versus three noncurvilinear points of length 16), the local-algebra structures, and the link to Hermitian rational points and concurrency geometry give motivated geometric information beyond a routine point count. The particular integral model, rather than an arbitrary slice, is fixed by the original published complete intersection.

## Scope, closest literature, and limitations

The published defining ideal is not a new discovery. The characteristic-zero configuration and its pencil geometry are not new. The characteristic-three Hermitian rational-point count is a classical background fact. The new claim concerns the exact flat specialization and its local scheme structures. In characteristic 2 the quartic itself is nonreduced; in characteristic 3 intrinsic osculation may not commute with reduction. Neither intrinsic positive-characteristic sextactic geometry nor uniqueness of an integral model is claimed. Independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
