# Independent mathematical audit

## correctness

PASS

If t>=2 leaves share a support, any secure dominating set contains at least t-1 of them: with two omitted leaves their common support is the only possible defender and moving it to one leaves the other undominated. Deleting t-1 selected twins and retaining one representative preserves all defenses, and adjoining them back also preserves security, proving exact leaf-twin additivity. In the reduced graph H, each side has at most one leaf. A general bipartite argument gives gamma_s(H)>=min{4,|X|,|Y|}: a secure set of size at most three smaller than both sides has exactly one selected vertex on one side, and defending an outside vertex on the other side would leave the selected set in one part without containing that whole part. Each whole bipartition side is secure when the opposite side has at most one leaf. If both reduced sides have size at least four, the four extreme vertices {x_{m-1},x_m,y_1,y_2} form a secure set; universal extreme vertices handle ordinary outside vertices and the unique possible leaf cases are handled by the second extreme. These bounds coincide. The verifier exhausts all canonical profiles through order ten and checks 511 twin reductions, but the proof is all-order.

## originality

PASS

The recent bisplit-graph preprint is the closest same-object source: it says secure domination is polynomial-time solvable on chain graphs and displays a four-extreme-vertex routine plus pendant-class handling, but the public full text does not state the closed formula audited here. More importantly, the displayed routine is not an implication of the formula in the small-side regime: on the 3-by-3 half graph it starts from four extreme vertices whereas an entire side is a secure set of size three. Secure total domination on chain graphs is a different, strictly stronger parameter. No broader or database result located determines the submitted ordinary secure-domination number.

## value

PASS

Secure domination is a standard graph-protection invariant and chain graphs are a canonical nested-neighborhood class. The theorem gives a complete exact formula, isolates the only effect of pendant-twin multiplicity, and resolves the small-side regime that the closest current algorithmic treatment does not capture transparently. This is a natural family classification rather than an arbitrary finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
