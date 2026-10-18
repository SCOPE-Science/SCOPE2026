# Independent mathematical audit

## correctness

PASS

Normalize nonzero real coefficients to norm one; sign changes and permutations allow 0<=b1<=...<=b5 after zero padding. For each subset J, the corresponding signed sum is s-2w(J), and the two-sided tail probability equals N/16, where N=#{J:w(J)<=(s-1)/2=τ}. Two exact polynomial identities verified symbolically show τ>=min(b3,b1+b2); the four minimal candidate subsets are therefore always admissible. Ordering candidate next weights {b3,b4,b1+b2} as u<=v<=w proves N=4 iff u<=τ<v, including ties and zero coordinates; otherwise at least five subsets qualify, hence tail >=5/16. The pairwise subset-weight comparison covers all other subsets, not just the displayed five. Direct independent exact arithmetic checks on 1286 nonzero nondecreasing integer tuples 0..8 confirmed all 32 sign counts and 261 equality cases, but the real-parameter theorem rests on the inequalities.

## originality

PASS

Hu–Lan–Sun 2021 gives the known sharp low-dimensional numerical values G3=G4=G5=1/4 and proves a stronger dimension-seven lower bound; that scalar lower bound is NOT novel. Hollom–Portier 2025 proves global bound 7/32 and describes global sharp behavior but does not state an at-most-five-coordinate exact equality locus with a fourth/fifth subset-sum gap. The new characterization is not implied by knowing the numerical infimum or a dimension-free weaker lower bound. An equivalent combinatorial Boolean-threshold lemma from prior inequality literature may remain unindexed; material considered includes full accessible primary texts, not titles alone.

## value

PASS

Classifying every extremal coefficient vector for a sharp Rademacher tail inequality is a motivated structural refinement of a known best constant. The explicit u<=τ<v condition includes all support sizes <=5 and boundary ties, and the discrete non-minimizer jump to 5/16 quantifies a real extremal dichotomy (one additional sign pattern). This is a complete natural small-support extremizer geometry, not merely another proof of G5=1/4.

The dated certificate retains the supplied scientific assessment, sources and limitations.
