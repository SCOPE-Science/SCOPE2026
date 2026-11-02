# Scientific review

## Correctness

**PASS.** Every circular window with positive one-count can be shifted to begin at a one without lowering its one-count. For exactly three ones, the lengths at which the second and third ones enter a rooted prefix are \(g_i+2\) and \(n-g_{i-1}\); simultaneous threshold minimization proves the exact admissible-root condition. Distinct gap triples have exactly two cyclic orientations and only one fails. Substituting \(a=t\), \(b=t+1+u\), \(c=t+2+u+v\) proves the rational generating function. Words with at most two ones or zeros admit a root, establishing the sharp length-six boundary. The standalone checker passed direct exhaustive tests through length \(11\) at all weights and through length \(41\) at weight three. The asymptotic follows from the dominant pole and elementary necklace orbit counting. These computations supplement, rather than replace, the general proof.

## Originality

**PASS, with residual priority risk.** The original 2011 prefix-normal form theorem and the 2014 papers study linear substrings, ordinary prefix-normal words and gap inequalities. The stronger requirement here allows factors crossing the cut while restricting the answer to an original cyclic rotation. In particular, the published linearly prefix-normal word `110010` belongs to a circular class with no acceptable root. The closest 2014 gap lemma can motivate the method but does not determine which three-one gap necklaces fail or the rational necklace enumeration. Full accessible primary texts of the 2011 author manuscript and the 2014 and 2016 works were checked; searches for cyclic/conjugate versions and published mathematical-record comparisons revealed no coverage. Unindexed results and alternate terminology remain possible.

## Value

**PASS.** Prefix-normal forms encode maximum one-counts for all substring lengths and support binary jumbled matching. The natural circular analogue asks if a single physically realizable cut of the same necklace supplies those maxima simultaneously. This theorem gives a sharp first obstruction, a complete classification for a natural fixed-density family, exact generating functions at all lengths, and an asymptotic prevalence result showing that the obstruction affects roughly half of the three-one necklaces. It is not merely a fixed-size computation.

## Scope and limitations

The classification is for three ones. Larger weights and unrestricted-density necklaces are not classified. The contribution is an exact new cyclic enumeration built on classical prefix-normal ideas, not a new definition of ordinary prefix-normal forms. The standalone computational checks have finite scope; independent validation and absolute historical priority have not been established.

Self-review: passed. Independent audit: not yet performed.
