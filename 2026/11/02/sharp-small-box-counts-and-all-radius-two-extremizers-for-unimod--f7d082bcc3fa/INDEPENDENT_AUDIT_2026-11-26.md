# Independent mathematical audit

## correctness

PASS

Each closed coordinate interval contains at most w=floor(2T)+1 consecutive integers and its integer intersection is contained in a width-w integer block; every full block fits at its midpoint since w−1≤2T. For w=1 the count is at most one and is attained. If any width-w block misses [−(w−1),w−1], every value of that coordinate has modulus at least w. Fix its column v; a determinant-one completion requires v primitive, and any two completions differ by an integer multiple of v. The corresponding coordinate of the other column has integer diameter w−1, so there is at most one completion. Hence any nonlocalized block box has count at most w². The localized starts are exactly −2(w−1) through w−1 in each coordinate. Independent exhaustive integer enumeration over these starts at w=2,3,4,5 tested respectively 256, 2401, 10000, 28561 tuples and found maxima 6,20,36,60 with 4,1,16,8 maximizing tuples. All maxima exceed w², proving global exhaustiveness. At w=5 the eight starts are precisely those of RESULT.md, with all five coordinate values used in every coordinate of every maximizing block, so a subbox missing one value cannot tie. A real radius-two box can therefore maximize only if each coordinate interval has five consecutive integers, forcing the midpoint in every coordinate. Moving from starts to midpoints yields exactly the eight stated centers. Origin and shifted-box counts independently reproduced as 52 and 60.

## originality

PASS

Known uniform large-box bounds treat the same counting problem but do not determine the finite maximum or the equality centers. Krieg's exact shell count, as quoted by Wurzinger, already determines the benchmark 52 using the radius-one base count, so that benchmark is not credited as new. OEIS A171503 is a fixed nonnegative cube, not an extremum over translates. The supported distinct contribution is the sharp translated profile through radius two and the exhaustive radius-two equality classification.

## value

PASS

This is the exact finite counterpart of a natural translation-uniform counting problem. Radius two is already enough for the centered integer-radius box to lose to translates (the centered radius-one box attains 20), and the result quantifies the gap and completely identifies equality even among noninteger centers. The localization lemma makes the exact calculation a statement over all translates, not a search confined to a chosen neighborhood. The origin benchmark or additional small counts alone would not provide this extremal comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
