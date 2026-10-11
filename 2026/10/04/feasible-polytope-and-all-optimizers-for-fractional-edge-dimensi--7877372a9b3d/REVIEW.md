# Independent mathematical audit

## correctness

PASS

The exact resolving-neighborhood argument was rebuilt from the graph metric. With at least three parts, for any distinct vertices x,y a vertex z in a suitable third/different part makes R_e{zx,zy}={x,y}; every distinct-edge resolving neighborhood contains at least two vertices, so all pair inequalities are both necessary and sufficient. In the bipartite case, exact size-two neighborhoods generate precisely the same-part pair inequalities, and every other resolving neighborhood contains such a same-part pair. The optimization therefore separates into fractional clique-cover polytopes on the parts, yielding singleton weight 0, a size-two segment summing to one, and the unique all-1/2 solution for parts of size at least three. Independent exact small-family reconstruction checked the claimed generator neighborhoods and sufficiency for (1,2),(2,2),(1,1,1),(1,2,2),(2,3,1),(2,2,2).

## originality

PASS

PASS. Yi Proposition 3.7 determines only the scalar fractional edge dimension of complete multipartite graphs. Its proof gives selected pair inequalities sufficient for the scalar lower bound but does not characterize every edge resolving function or the optimizer face. The later Goshi–Zafar–Rashid–Guirao paper defines minimal edge resolving functions and a general criterion but its stated exact applications are other graph classes and it does not provide an arbitrary complete-multipartite feasible-polytope/optimizer theorem. Resultary searches returned other complete-multipartite resolving invariants, not this fractional-edge feasible set. The final claim is not a mere restatement of the scalar formula: it gives an if-and-only-if reduced constraint system and classifies all minimizers, including nonuniqueness.

## value

PASS

For an LP-defined graph invariant, the complete feasible constraint reduction and full minimizer face are natural structural data materially stronger than the optimum scalar. The theorem resolves exactly when the optimum is unique and when a continuum of optima occurs across the entire complete-multipartite family, not an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
