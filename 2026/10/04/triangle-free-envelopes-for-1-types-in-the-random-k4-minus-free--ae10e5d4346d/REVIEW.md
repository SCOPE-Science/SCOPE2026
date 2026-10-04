# Review: Triangle-free envelopes for 1-types in the random K4-minus-free 3-hypergraph

## Correctness
**PASS.** The source class at \((m,l,s)=(3,4,1)\) is exactly the class of finite 3-graphs in which each four-set has at most two edges. The cited paper proves free amalgamation in this parameter range and states quantifier elimination for the Fraïssé limit. For a new point, checking the unique four-set \(\{x,a,b,c}\) above each old triple gives exactly the two local inequalities in the proof. Translating them into 2-edge or 3-edge conflicts is reversible, so the independence-polynomial identity is exact. Free amalgamation produces arbitrarily many realizations of every outside diagram. The coefficientwise extremum follows because every legal link is triangle-free and an old hyperedge excludes a two-edge path that remains triangle-free. The bundled exhaustive checks agree with the proof on every legal labelled parameter structure through five vertices.

## Originality
**PASS, with residual folklore risk.** The closest combinatorial prior explicitly states that \(K_4^-\)-free 3-graphs are characterized by triangle-free vertex links; that fact is excluded from novelty. Kikyo–Tsuboi supply the homogeneous model-theoretic framework but do not give the parameter-sensitive link polynomial, conflict hypergraph, coefficientwise extremum, or worst-case 1-type asymptotic. published-finding corpus searches using the exact object, the \(\mathcal H^3_{4,1}\) notation, “finite parameter types,” “independence polynomial,” and “triangle-free envelope” returned no equivalent result. The own-ledger comparison found nearby generic-hypergraph and Henson-graph type-count results, but neither implies this mixed-rank constraint system.

## Value
**PASS.** This gives a closed combinatorial representation for every finite parameter set, not only an aggregate orbit count, and identifies a sharp unique worst-case parameter geometry. It quantitatively shows that the local \(K_4^-\) prohibition cuts the worst-case quadratic 1-type exponent from \(1/2\) in the unrestricted generic 3-hypergraph to \(1/4\). The construction also exposes a natural restricted family of mixed-rank independence polynomials for further structural or algorithmic study.

Same-model review: passed. Independent audit: not yet performed.
