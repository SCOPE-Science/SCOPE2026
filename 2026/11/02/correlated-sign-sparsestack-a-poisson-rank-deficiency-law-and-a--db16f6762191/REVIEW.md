# Independent mathematical audit

## correctness

PASS

For each column, scaling away the common sign gives the signed incidence vector e_u+sigma e_v of a bipartite multigraph. On a connected component with e edges and v vertices, left-kernel propagation has dimension one exactly for balanced cycle sign products, yielding contribution e-v+1_balanced to column nullity; trees contribute zero and each balanced unicyclic component contributes one. For fixed c<1, edge-labeled 2l-cycle factorial moments converge to independent Poisson variables with rates c^(2l)/(2l), including parallel-pair 2-cycles. Expected bicyclic kernels are O_c(1/r) and long-cycle tails are summable for c<1. Independent sign products thin each length with probability (1+rho^(2l))/2, giving Pois[-(log(1-c²)+log(1-rho² c²))/4]. Appending columns is nullity-monotone, and comparison to every fixed c0<1 proves divergence at c>=1 as c0 approaches one. This proves rank only for fixed coordinate subspaces, not conditioning or embeddings; finite graph-vs-matrix checks did not substitute for Poisson limit proof.

## originality

PASS

PASS, qualified: neither the primary SparseStack performance analysis nor its general oblivious embedding bounds specifies the rank-nullity law for a two-block coordinate restriction with correlated relative signs. Classical signed-graph rank and sparse-cycle Poisson limits are antecedents, so the potential advance is their explicit correlation-resolved synthesis and exact half-density boundary. A same-model preprint could not be read fully and older random signed-incidence literature could subsume the formula.

## value

PASS

A natural coordinate-subspace failure mode of an actually studied sparse randomized linear-algebra sketch has a sharp full-rank probability, including a parameter-interpolating sign correlation and a threshold at half the total row count. These are design-relevant structural quantities not implied by norm-distortion estimates or a finite matrix experiment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
