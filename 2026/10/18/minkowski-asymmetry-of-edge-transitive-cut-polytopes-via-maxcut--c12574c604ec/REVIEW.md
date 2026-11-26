# Independent mathematical audit

## correctness

PASS

The repaired theorem classifies the affine hull, not the global center set. The signed orbit vertices have independent nontrivial edge characters for simple graphs, so their average 0 is interior and switching preserves the polytope. Averaging any feasible centers over switchings gives 0. Centered containment is determined by the negative diagonal radial point p=−1/s, where s≥1 automatically since the signed cut polytope is in the unit cube. The polar relation D_G=−K° makes the optimum face precisely the set of normalized inequalities tight at p. For any minimizing b, the switched reflection at each vertex is p+((s+1)/s)T_σ b, so any dual optimizer a yields a·T_σ b≥0 for all signs. This has average zero, and orthogonality gives a_e b_e=0 coordinate by coordinate. Conversely, all active facet inequalities at p remain equalities under any switched displacement supported outside E_*; the finitely many inactive facets retain positive slack for all sufficiently small displacements. This shows the exact affine dimension, not just forced equations. Finite-union avoidance of proper hyperplanes yields a single optimizer with every coordinate in E_* nonzero. The all-graph argument includes s=1, isolated vertices and disconnected simple graphs. Edge transitivity gives a full-support uniform optimizer by averaging maximum cuts, recovering rigidity and the numerical background. The triangle with pendant edges verifies that center freedom actually occurs: the polytope is a product and s=3, leaving one [1/4,3/4] center coordinate per bridge. The frozen support checker was inspected, not executed; the VERIFICATION output is labeled expected and pertains to the numerical cases only. The corrected proof does not use those checks.

## originality

PASS

Reassessment of the delivered repair: the supported distinct claim is the all-graph affine-hull formula from the support of the full Boolean edge-shell optimum face. The original numerical claim is covered by exact duality and is credited as such in the repair. Closest existing cut-polytope center results apply in special minor-free classes and the earlier optimization theorem gives a value and an extremizer in a special class, not the general support-to-center rule in both directions.

## value

PASS

The repaired statement answers a distinct structural question for the natural cut polytope: which edge coordinates must every optimal center share, and how many independent degrees of freedom remain? One exposed dual optimum face certifies that exact affine dimension for arbitrary simple graphs, beyond transitive or specified minor-free families. The converse neighborhood result is essential: absence of a pinned coordinate means a genuine locally free center direction, as the connected triangle-with-bridges example illustrates. It is not merely a numerical restatement of a known cut invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
