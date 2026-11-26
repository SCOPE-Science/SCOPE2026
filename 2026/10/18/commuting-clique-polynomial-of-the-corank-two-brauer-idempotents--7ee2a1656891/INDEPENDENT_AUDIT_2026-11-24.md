# Independent mathematical audit

## correctness

PASS

For a rank n−2 diagram with upper cup I and lower cap J, the middle matching in its square preserves rank exactly when I and J meet. In that case its bijection between residual label sets forces a unique transversal bijection for idempotence, giving the pair projections and the six triangle diagrams per triple. There is also a direct check of the commutation converse: for e with cup/cap I,J and f with K,L, ef has rank n−2 if J meets K and rank n−4 otherwise; fe has the same rule with L and I. If both products preserve rank and are equal, their unique external cups and caps force I=K and J=L, hence e=f. In the rank-drop case equality requires a common diagram containing both external cups I,K and both caps J,L. Here I cannot equal K and J cannot equal L, since either equality would contradict disjointness of the relevant middle pair. It follows that I and K are disjoint and J and L are disjoint, and the two middle disjointness conditions then give disjoint supports. Disjoint support is sufficient by verticality off support. The frozen exact five-label reduction is also sound and the fresh path-tracing certificate checks all 2415 pairs of the 70 candidates, with 75 commuting pairs and no intersecting exception (replay: /workspace/branches/31900e4c-c973-4fc0-bd38-d05bf151d45b/independent_b5_check.py). Labelled packings with one decoration per pair and six per triple give the factorial formula and EGF, with the unused labels counted as singletons. At size floor(n/2), only pairs occur for even n; odd n permits either one unused label or a single decorated triple. This yields both maximal-size counts, including n=2 and n=3; n=0,1 are only EGF conventions.

## originality

PASS

The individual-idempotent stratum is antecedent. The supported distinct contribution is the full nonplanar pairwise commutation criterion and its decorated-packing enumeration. The strongest same-day match treats the planar Jones submonoid; neither its support rule nor its clique recurrence covers the extra nonplanar diagrams. No priority order within that day is inferred.

## value

PASS

This is the complete compatibility graph of a natural next-to-unit rank stratum, not a new tally of a known list. The disjoint-support condition allows all-size and extremal enumeration without multiplying large families of diagrams and distinguishes the nonplanar model from the planar one.

The dated certificate retains the supplied scientific assessment, sources and limitations.
