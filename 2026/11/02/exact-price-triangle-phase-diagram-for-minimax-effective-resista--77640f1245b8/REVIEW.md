# Research review: price-triangle law for double-star resistance diameter

## Correctness — PASS

The claim is quantified over every integer \(p,q\ge2\), every strictly positive \(a,b,c,B\), and every individually adjustable nonnegative conductance vector. The proof starts with the exact resistance-as-tree-path-sum identity, treats disconnected allocations as infinite, normalizes the worst path resistance to one, and minimizes a strictly convex reciprocal-cost function. Unique full-dimensional minimization proves that orbit symmetry is a *consequence* of price and graph symmetry, not a restriction imposed on competitors. The three possible active sets follow from Cauchy--Schwarz and checked KKT derivatives. Scaling back gives the exact optimum and unique conductances; inequalities also classify all diametral pairs, including equality boundaries. The asymptotic \(3/2\) ratio follows by direct substitution. The executable independently checks 225 grounded-Laplacian inverses, 14,625 nonsymmetric allocations and 54 unconstrained-by-symmetry numerical minima; experiments are supportive only.

## Originality — PASS, with stated uncertainty

Ghosh--Boyd--Saberi formulate the **general** convex minimax-effective-resistance problem as an SDP (2006 conference Section VII; 2008 journal Section 8), so neither the objective nor convexity is novel. Their accessible versions were compared at the problem-statement, tree-formula, analytical example and extension sections, and do not exhibit the present explicit three-regime formula, price-triangle boundary or exact worst-pair classification. Ellens et al. optimize **total** effective resistance and graph topology at fixed combinatorial diameter, not the same objective or variable-price allocation. A previous priced-star minimax classification and a double-star spectral-gap classification are close in object or method but do not imply the two-hub, three-path-family result. Actual database searches for aliases, price thresholds, resistance diameter and double stars returned no demonstrated exact coverage. This is evidence for best-knowledge distinctness, not a proof of publication priority.

The earlier Hambrusch--Lim tree edge-reduction paper is a material residual risk. Its full text was inaccessible despite open-access attempts and an institutional-access attempt, so the abstract alone does not justify a whole-paper exclusion. Its described reduction-cost problem has not been shown equivalent to the reciprocal-conductance model. If it contains that exact cost model or a stronger parameterized result, originality requires renewed comparison.

## Mathematical value — PASS

The result supplies a complete infinite-family, globally unique design rule for a natural two-community tree, under a worst-pair robustness objective rather than the better-studied total-resistance objective. The sharp square-root triangle inequality predicts whether only cross-community pairs are worst or both cross-community and same-community pairs tie. With all edge prices one and one community growing, optimizing independent conductances reduces the resistance diameter relative to equal conductances by a factor tending to \(3/2\), a fixed and non-negligible improvement. This transition and exact performance are not a renaming of the general SDP; the restrictions \(p,q\ge2\) and classwise uniform prices are motivated by the competing path families.

## Limits

Not claimed: independent priority certification, arbitrary individual spoke prices, cyclic graphs, or proofs based solely on random tests. Potential specialized older coverage, particularly tree-diameter reduction literature, remains. A separate independent mathematical audit was not performed.

Self-review: passed. Independent audit: not yet performed.
