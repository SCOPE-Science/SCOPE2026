# Independent mathematical audit

## correctness

PASS

The invariant tracks a set of nonempty ranges for each labelled coalition, not an upward closure or a multiset. At k=1 the occurring outcomes determine the flip orbit. At k=2 the constants, the cases with one exceptional entry, and the three two-ones configurations are separated: a singleton coalition sees both singleton outcomes for the corresponding stripe, only the mixed range for the transverse stripe and both checkerboard directions, and a singleton plus a mixed range for an exceptional entry. At k=3 the displayed tables have the same range families, and have three and two ones respectively, so even cube coordinate and outcome permutations cannot identify them. A fresh exhaustive calculation partitioned all 4, 16 and 256 Boolean tables by translation orbit and constructed range families by grouping profiles by their fixed coordinate tuples. It obtained 3/3, 7/7 and 41/46 signatures/orbits respectively; the only ambiguous signatures contain 2, 2 and 4 orbits with 12, 12 and 32 labelled tables. Burnside independently gives 46: (256+7*16)/8. Replay with python3 /workspace/branches/independent_checks.py 1; the uploaded verifier was inspected, not executed. This tests exactly the specified fixed action/outcome sizes and k<=3, not higher dimensions or any broader invariant.

## originality

PASS

The exact range-family object is already present in Wang. The supported distinct contribution is the faithful-versus-nonfaithful boundary for the fully labelled binary signature under action flips and the complete first-layer census, not the definition or the broad fact that monotone effectivity can lose information.

## value

PASS

Keeping every exact attainable range rather than just the monotone closure naturally raises a faithfulness question. This result says exactly when that finer abstraction first loses information in the binary setting, shows the loss survives enlarged relabelling, and identifies how much ambiguity the first possible failure can hide. Those facts are relevant to recovering concrete game forms rather than just deciding whether signatures can be realized.

The dated certificate retains the supplied scientific assessment, sources and limitations.
