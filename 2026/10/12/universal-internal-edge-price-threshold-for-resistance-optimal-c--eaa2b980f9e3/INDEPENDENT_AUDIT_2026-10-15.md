# Independent mathematical audit

## correctness

PASS

For a connected weighted N-vertex graph, K=N tr((L+J/N)^-1)-N has strictly positive second derivative 2N tr(X^-1 H X^-1 H X^-1) along every nonzero edge direction (distinct edges are linearly independent via offdiagonals). Thus a unique price-feasible optimum exists and per-clique permutations force common spoke a_i and internal b_i. A q-leaf clique plus hub has R(h,u)=1/(qa)+(q-1)/(q(a+qb)) and R(u,v)=2/(a+qb), so exact cut-vertex decomposition is K_i=(N-q)/a+N(q-1)/(a+qb). With y=1+qb/a, beta=(q-1)d/(2qc), A=N-q, B=N(q-1), local cost-K product is qc(1-beta+beta*y)(A+B/y), y>=1; its derivative A*beta-B*(1-beta)/y² yields the sharp threshold d/c=2N/(N-1) independent of q. The minimizer is unique at y=1 when price is >= threshold and interior otherwise, even for beta>=1. Minimizing sum C_i/p_i at sum p_i=1 gives unique shares sqrt(C_i)/sum sqrt(C_j) and K=(sum sqrt Ci)^2. Independently an exact rational grounded-Laplacian test at N=6 with q=(2,3), a=(1/3,1/2), b=(1/6,0) yields Kirchhoff index 51 both by inverse and decomposition; the checker in the package is additional finite evidence only.

## originality

PASS

Ghosh–Boyd–Saberi provide general strict-convexity/optimization tools for total effective resistance; the inspected full PDF and examples do not establish the all-heterogeneous clique-bouquet closed optimum or a common size-independent internal-edge price threshold. Kooij covers structural/spectral windmill graphs, and Sardar–Xu abstract describes fixed unit-resistor indices; the latter full specialized article was not accessed. This is best-of-knowledge original at the level of exact threshold/equality/complete optimizer, with an explicit possible obscure network optimization corollary risk.

## value

PASS

Price-optimal conductance allocation is a natural electrical network design question. Exact global cost-allocation formulas for arbitrarily many heterogeneously sized cliques are nontrivial, and the same internal-edge deletion threshold depending only on N despite different block size and all other prices is a structural, useful phase transition. Uniqueness and boundary equality make it a complete classification, not an arbitrary small optimization instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
