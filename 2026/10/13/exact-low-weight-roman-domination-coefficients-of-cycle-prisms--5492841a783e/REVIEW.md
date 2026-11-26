# Independent mathematical audit

## correctness

PASS

A rooted length-n trace walk determines exactly one labeling of the labeled prism: at each step the middle column is checked against its rung and the two neighboring columns and contributes its weight once. This works at n=3 as well, where the two rail neighbors are still distinct. The tabulated potential telescopes and makes every weight after subtracting n nonnegative. The constant coefficient uses only B0; the linear coefficient uses exactly one B1, with its n possible positions related by cyclic trace. Independently regenerated all 601 admissible triples, with reduced exponent counts 104,299,144,54 at exponents 0,1,2,3. Exact sparse path counting established B0^3=B0^7 entry by entry, traces (0,4,0,0) and marked traces (5,6,4,2,4); multiplication by further powers proves the eventual period. A separate count chooses the set S of 2-labels, forces each vertex outside its closed neighborhood to be 1, and chooses additional 1s freely in the closed neighborhood minus S. This gave the two stated coefficients and no smaller weights for n=3 through 10, including (0,15) at n=3. Replay: python3 -I -B /workspace/audit_replays/frozen_math.py 3.

## originality

PASS

The supported distinction is the unrestricted standard-Roman count at n+1 for labeled prisms, including the next-to-minimal layer when 4 divides n. The minimum weight is known; the weight-n coefficient reduces to efficient domination, and the small triangular-prism instance falls within an existing atlas's stated coverage. No independent novelty is attributed to those overlaps. Closest same-day indexed records count different graph classes or domination objects; the later unique-response restriction omits genuine labelings of the layer at issue.

## value

PASS

A minimum weight alone cannot tell how many optimal labelings exist; the leading and first-excess coefficients of the natural Roman polynomial encode that multiplicity and the first defect layer. In this canonical periodic graph family the count changes residue class and rule, is exact for unbounded n, includes label 1, and has a nontrivial matrix-period certificate. The supported contribution is the all-order n+1 enumeration rather than the known weight threshold, the perfect-code coefficient alone, or the isolated six-vertex exception.

The dated certificate retains the supplied scientific assessment, sources and limitations.
