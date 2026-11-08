# Independent mathematical audit

## correctness

PASS

For S(1^a,2^b) with integers a>=1,b>=2, the target inner long-arm vertex x_1 has eccentricity three. A stack of >=4 anywhere cannot end at x_1; a short leaf receiving >=3 cups is fatal because its only distance-three exit reaches a long-arm end and would create >=4 cups. Each short leaf must therefore either send its untouched one cup to center c or receive the lone original cup of c; after c empties it never refills, and after two unit-leaf incoming moves it has >=3 cups with eccentricity two, so two short leaves cannot both be cleared. For a=1 the four target orbits (c, short leaf, x_1, y_1) have explicit all-occupied legal sequences including parity-dependent b and all finish in 2b+1 moves. Independent BFS graph distances and complete replay checked 236 positive orbit representatives for every b from 2 through 60 and all four target types; independent full state graph obstruction exploration at six small (a,b) combinations found no path to x_1. The symbolic bottleneck/construction proves all unbounded a,b, not finite interpolation.

## originality

PASS

The primary 2023 cup-stacking paper introduces game and expressly leaves mixed short/long spider cases open aside from the one-long-arm subfamily, while proving all arms length >=2. A 2024 Hamilton-path sufficient condition is inapplicable because these spiders have >=3 leaves, and it addresses different graph families. The specific a=1 iff classification with b>=2 uses new obstruction and constructive parity sequences. An original Veselovac thesis and possible later unindexed solution remain priority risks.

## value

PASS

This resolves a precisely motivated subfamily within a previously identified open problem on which spiders permit every target. The threshold of one unit arm is structurally surprising, and the complete positive construction plus negative target obstruction is independently reusable for other cup games; not an arbitrary isolated small-instance count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
