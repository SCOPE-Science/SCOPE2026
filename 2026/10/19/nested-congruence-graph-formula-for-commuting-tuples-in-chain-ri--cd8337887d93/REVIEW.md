# Independent mathematical audit

## correctness

PASS

The directed-arrow multiplication gives the two-row minor equations for the endpoint difference delta and the arrow coefficient vector; vertex coefficients commute and all two-arrow products vanish. Conditional on the vertices, distinct arrows are independent. For nu(delta)=a<L, write delta=pi^a u with a unit entry in u, and send u to the first unit vector by an invertible column transformation, which preserves vanishing of all wedge coordinates. The remaining t-1 entries each lie in Ann(pi^a)=pi^{L-a}R of size q^a, so the fiber is q^{L+(t-1)a}. For delta=0 that count is q^{Lt}. Telescoping the valuation factor gives the stated weights for congruence thresholds. At each lift from R/(pi^{h-1}) to R/(pi^h), every E_h-component already has a common residue below, since E_h is contained in E_{h-1}; choose one lift for that component, with q^t choices even in mixed characteristic, and there are no further restrictions at this level. Their product gives the stated exponent. Reversal negates delta; c(S)=n-r_G(S) gives graphic-matroid dependence including loops, repeated edges and isolated vertices. Loops impose no arrow constraints, t=1 gives |A|, m=0 gives q^{Lnt}, and L=1 gives the finite-field expansion. Independent replay: python3 /workspace/reproduction.py 1 enumerates the commuting relation by literal arrow products and uses centralizer intersections for triples. All ten cases agreed over Z/p^L and F_p[e]/(e^L) for the tested lengths and p=2,3. Examples include 25600 ordered triples for one arrow at q=L=2, 163840 ordered pairs for two opposite arrows and a loop there, and 47104 pairs for one arrow at q=2,L=3. These tests are bounded and not an all-ring proof; the lifting argument proves the general claim. No non-chain or noncommutative coefficient claim is made.

## originality

PASS

The reviewed sources give exact finite-field specializations, an exact later triangular one-arrow comparison and relevant ring/graph tools. None of the verified earlier results yields the combined L>=2, arbitrary-graph, all-arity law or the resulting mixed- versus equal-characteristic invariance. Only that combined extension is credited, not the finite-field expansion or the chain-ring filtration itself.

## value

PASS

The whole family of commuting-tuple counts is a natural finite-algebra invariant. The exact formula shows that the family cannot distinguish dissimilar equal- and mixed-characteristic chain rings sharing q and L in this class, and that it ignores orientation and all graph information outside graphic-matroid rank and vertex count. These are structural conclusions about nonlinear congruence constraints, not a finite verification or a restatement of the one-level Potts sum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
