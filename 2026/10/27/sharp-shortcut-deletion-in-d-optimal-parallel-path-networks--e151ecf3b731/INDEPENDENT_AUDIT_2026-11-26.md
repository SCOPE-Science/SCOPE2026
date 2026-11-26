# Independent mathematical audit

## correctness

PASS

A tree retains exactly one complete terminal path (possibly the direct edge); every other long path must lose exactly one edge to avoid cycles without isolating internal vertices. This gives the multiaffine path polynomial even at zero weights. A positive design exists, and on the positive-determinant domain the reduced Laplacian depends injectively on conductances of this simple graph. Off-diagonals recover nonroot edge weights, then diagonals recover root edge weights. Strict log-det concavity gives uniqueness, and polynomial invariance under intra-path permutations then forces equal weights within each path. The common weights are positive because deleting a whole long path isolates internal vertices. With path budget coordinates x_i and V=x_0+sum(c_i x_i), c_i=1/ell_i^2, the objective up to constants is sum((ell_i-1)log x_i)+log V. The stationarity multiplier is rho by summing coordinate derivatives against the allocation. If x_0 is positive, V=1/rho and x_0=(1-S)/rho; that solution also satisfies complementary slackness when S=1. On the zero-shortcut face, xi=rho V must solve sum((ell_i-1)c_i/(xi-c_i))=1 above max(c_i). This sum is strictly decreasing there and takes value S at xi=1. The root satisfies the omitted-edge inequality 1/V<=rho exactly when S>=1. The stationarity formula budgets correctly: sum((ell_i-1)xi/(xi-c_i))=sum(ell_i-1)+1=rho. Converting back gives both stated weight formulas and determinant factors, which agree at equality. The concavity argument makes the feasible KKT solution globally optimal and unique.

## originality

PASS

Exact overlap exists in restricted graph families, notably the unicyclic case and cone-over-star cases. The distinct claim credited here is the heterogeneous, arbitrary-number parallel-path allocation and its shortcut criterion, not the determinant objective, effective-resistance calculus, unweighted theta count, or previously solved subcases. No inspected result covered both arbitrary path counts and the heterogeneous lengths with these closed formulas.

## value

PASS

Uniform-cost budgeted D-optimality is a natural criterion on parallel routes. The solution predicts a support transition that a generic determinant formulation does not locate, and distinguishes threshold equality from strict deletion by the direct-edge marginal gain. The exact heterogeneous reciprocal-length rule and single-root allocation are useful beyond the previously covered cycle, short-route and book cases; they decide both whether a shortcut is worth any budget and how to allocate the rest without an edge-by-edge optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
