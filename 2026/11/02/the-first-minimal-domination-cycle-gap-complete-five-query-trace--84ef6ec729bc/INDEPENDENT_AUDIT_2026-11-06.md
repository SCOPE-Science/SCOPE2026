# Independent mathematical audit

## correctness

PASS

Minimal dominating set enumeration was independently implemented from the literal dominate-after-removal predicate on every 2^n vertex subset. For C11 it gives 44 hypotheses and a complete five-query trace histogram over all binom(11,5)=462 supports with maximum 29, excluding VC=5. The source four-query witness and full 32-leaf depth-five tree cover lower bounds; 44<64 excludes depth six. Independently recalculated the full n=3..11 sequence: VC and Ldim agree at (1,2,2,2,3,3,4,4) through C10, then (4,5) at C11. Disjoint-union minimal dominating sets factor, giving VC and Littlestone additivity by product and independent mistake bounds; automorphisms of m disjoint identical cycles are vertex-transitive. Computation proves finite base cases, product proof proves all m.

## originality

PASS

Couturier et al. primary 2013 full paper establishes minimal dominating set enumeration, private-neighbor criterion and component factorization (Observation 1), but not the VC/Littlestone measures or C11 trace histogram. Bhaskar thicket and Malliaris–Moran online-learning frameworks contain general definitions, not the claimed finite cycle spectrum. Published SCOPE cover-free path/cycle numbers concern another invariant, while path minimal-domination and cycle maximal-independent hypothesis classes are different. Thus known general theory does not imply first gap, adaptive tree, or trace distribution.

## value

PASS

A first graph-size gap for a natural canonical domination concept class, together with a vertex-transitive 2-regular unbounded additive amplification, provides a motivated structural learning-theoretic phenomenon rather than arbitrary finite cataloguing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
