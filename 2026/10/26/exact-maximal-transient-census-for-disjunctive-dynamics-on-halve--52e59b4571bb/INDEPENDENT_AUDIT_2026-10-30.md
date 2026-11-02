# Independent mathematical audit

## correctness

PASS

OR dynamics propagates seed support along exactly-t graph walks. For t>=2, weight-two generators reach exactly even differences of weight <=2t: disjoint pair decomposition supplies minimal steps, replacing two pairs by three generators adds one step, repeated generators add two, and zero difference has 2/3-step closed circuits. Thus at T=floor(n/2) every occupied parity component fills, but at T-1 only its farthest shell can be missing. When n even the farthest parity-matched vertex has a unique antipode, yielding A=N singleton seed sets. When n odd the farthest shell is an ordinary cube-neighborhood; singleton supports counted once, pair supports have exactly two centers, >=3 supports have unique center, yielding A=N(2^n-n-C(n,2)/2). Components independent, inclusion-exclusion yields 2A 2^N-A^2. Direct shell, odd-subset counting n6..10 and finite first-entry checks passed; all-n claims rest on constructions.

## originality

PASS

General OR-network connectivity and exponent/height facts already follow from Jarrah et al 2008 and Goles--Hernández 2000. Those statements do not give the *number of maximal-depth starting configurations* in the halved cube. Resultary 2026 parity/XOR automata on the same distance-two graph have different addition law and periodic structure, so their rank formulas do not imply OR seed-support census. Earlier special halved-cube graph census may remain undiscovered.

## value

PASS

The exact number of extremal transient states is a natural quantitative dynamical invariant beyond knowing eventual fixed points or max height. Opposite parity dimension cases have qualitatively different seed geometry: singletons in even dimension, arbitrary nonempty subsets of antipodal Hamming-neighborhoods in odd dimension. The fully labeled census makes both effects explicit for an infinite graph family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
