# Independent mathematical audit

## correctness

PASS

For graph K1 vee (disjoint clique blades B_i), after any one-unit move the positive support dominates iff the center is positive OR, when center zero, every blade contains a positive vertex. Splitting by original center label yields exact exhaustive cases: center 2 permits any labels on blades; center 1 permits at most one entirely zero blade (an empty blade must be defended by center, after which other blades must remain nonempty); center 0 requires every blade nonempty and is sufficient because donor moves within any blade retain support there, while a donor to zero center renders whole graph dominated. Therefore with T=1+x+x², Ai=T^{mi}-1, M=Σmi, W=x²T^M+(1+x)ΠAi+xΣ_i Π_{j!=i}Aj. At x=1 total count 3^M+2Π(3^{mi}-1)+Σ_iΠ_{j!=i}(3^{mj}-1); min weight 2, with (m1+1)(m2+1) minimizers for r=2, unique center-2 minimizer for r>=3. An independently implemented literal zero-vertex move/dominating support enumerator matched full polynomial and minima for (2,2),(2,3),(3,3),(2,2,2),(2,2,3). It is a finite consistency check; symbolic case proof covers all r>=2 and mi>=2.

## originality

PASS

Earlier weak Roman domination results define/general-bound the invariant; a published Resultary formula for complete multipartite graphs does not specialize, because blades are cliques and separate blades are anticomplete; its complement is different and weak Roman domination is not invariant under complementation. Roman-domination polynomials of generalized windmills count a stricter class (functions with no label 2 in the center-1, one-empty-blade case show separation). Same-object general position and dissociation polynomials count different predicates. The 2011 Pushpam–Mai weak Roman paper is only abstract/bibliographic access, so best-known PASS retains an explicit priority risk, not a whole-document noncoverage assertion.

## value

PASS

Heterogeneous windmills (unequal clique blades, universal cut vertex, friendship graph subfamilies) are a natural graph class. The theorem enumerates every feasible weak Roman defense function by weight and exactly its minimum-layer multiplicity, not merely an easy minimum parameter. Distinct center states and allowable empty blades yield a reusable product formula with a real r=2 vs r>=3 extremal transition; there is no inspected preexisting table that mechanistically supplies its coefficients.

The dated certificate retains the supplied scientific assessment, sources and limitations.
