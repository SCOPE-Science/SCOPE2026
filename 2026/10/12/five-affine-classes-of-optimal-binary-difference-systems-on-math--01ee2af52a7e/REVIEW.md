# Review

## Correctness
PASS. The sharp redundancy lower bound and its equality condition are stated in the inspected Tonchev–Wang article. At \((n,q,ho)=(19,2,1)\), equality forces two blocks of size \(3\). The bundled verifier then exhausts every unordered pair of disjoint triples, checks the exact external-difference condition, counts all \(1{,}482\) unordered and \(2{,}964\) ordered optima, and exhausts the stated finite symmetry group. The classification does not extrapolate from samples.

## Originality
PASS, with residual risk. Exact-claim, external-difference-family, count, affine-orbit, and modulus-\(19\) searches found no source that states or implies the \(2{,}964\)-system census or the five affine classes. Tonchev–Wang supplies a general exhaustive algorithm and printed representative tables but no inspected length-\(19\) equality census. Chisaki–Miyamoto has a modulus-\(19\), block-size-three construction with different parameters. A historical extended online table or an unindexed external-difference-family classification could still overlap the result.

## Value
PASS. Length \(19\) is the natural third equality parameter \(n=2m^2+1\) for regular binary index-one systems, after \(n=3\) and \(n=9\). The verifier finds one affine class at each of those earlier parameters but five at \(n=19\), so the result identifies the first nontrivial moduli split at the sharp synchronization-redundancy bound. The exact count and the unique symmetric class are structural information not supplied by the known optimum value alone.

## Closest literature and limitations
The closest broad source is Tonchev–Wang (2007), which gives the lower bound, a general exhaustive algorithm, and optimal-solution tables; the inspected printed binary table stops at length \(12\). Levenshtein (2004) surveys the motivating comma-free-code problems. Zhou–Tang (2010) places optimal perfect DSS constructions explicitly in synchronization coding and carries the published MSC string `94A55-94B05`. Chisaki–Miyamoto (2015) studies triple-block DSSs and a modulus-\(19\) example with six blocks and index \(15\), not the binary case here. The comparison does not rule out an obscure unindexed prior enumeration.

Self-review: passed. Independent audit: not yet performed.
