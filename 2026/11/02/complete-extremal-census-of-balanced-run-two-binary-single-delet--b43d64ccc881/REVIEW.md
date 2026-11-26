# Independent mathematical audit

## correctness

PASS

This is a finite unrestricted-subset problem on noncyclic words, not a linear-code problem. The explicit graph criterion is equivalent to pairwise shadow disjointness. In the frozen pivot recursion, any unreported maximal clique must either use the pivot (if eligible) or contain a vertex not adjacent to it; otherwise the pivot extends it, or it was already excluded by X. Removing each processed branch from P and putting it in X prevents duplicates. Independently, I treated each candidate as a set of descendants and branched on the parent group of a descendant: a packing uses exactly one of that group or none, and choosing a word forbids all parents of its descendants. A partition of the remaining candidates into such conflict groups gives an upper bound of one per group. The independent search discards only branches strictly below the current best, so it counts ties and certifies exhaustiveness. It gives (admissible words, maximum size, labeled maxima)=(6,2,4),(14,4,4),(34,8,1),(84,15,20), agrees with every literal codebook and ordering in maxima.json, and obtains syndrome 3 modulo 5 at length eight and exactly syndromes 3,4 modulo 6 at ten. Applying the four reversal/complement maps gives six two-element and two four-element orbits at ten.

## originality

PASS

Modified-VT validity and the deletion-conflict graph model are known, as is the length-four optimum size from the identical balanced layer. The supported distinct result is the exact optimum and equality census of the intersection of balance and run ceiling two, particularly the labeled maximizers and orbit structure at lengths eight and ten. Neither of the closest exact broader-domain tables yields that census.

## value

PASS

The balanced layer and symmetric run restriction define a natural intersection of two distinct constrained-code regimes. The exact equality census distinguishes whether the standard algebraic construction merely attains the optimum or classifies all optimal codes. Length eight gives uniqueness, whereas length ten exposes substantial structure outside the syndrome construction, still with eight inequivalent classes under the two natural symmetries. This is a concrete benchmark for future constrained packing or classification algorithms, not a claim that VT codes lose optimal size here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
