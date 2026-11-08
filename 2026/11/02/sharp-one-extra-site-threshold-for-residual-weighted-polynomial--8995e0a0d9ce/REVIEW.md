# Independent mathematical audit

## correctness

PASS

An (m+1)×m full-spark evaluation matrix has a one-dimensional left-nullspace spanned by w with all w_j nonzero, so every leave-one-out residual equals (wᵀf)/w_j, fixing rankings for n=m+1. At n=m+2 the two specified adjacent m-node stencils with one outside point each admit opposite indicator pairs from impulses at the first and last nodes. For 1D degree d on d+2 equally spaced nodes, endpoint barycentric weights have equal magnitudes, forcing exact cancellation of nonlinear indicator factors for all sample vectors. Explicit Lagrange evaluation of step data at h/2 and the compact geometric-weight ratio yield (-1)^d C(2d,d)/(4^d[1+(2d+1)^{2μ}]); verified independently for d=1..8 with exact rational arithmetic. The proof extends to all full-spark real polynomial spaces, not just the checked grids.

## originality

PASS

The 2026 Dell’Accio et al. Compact Multinode Shepard work introduces the residual indicator and conditional jump behavior, whereas the inspected accessible descriptions do not state the global rank-one rank-order obstruction, smallest m+2 two-sided discrimination threshold, or exact two-stencil jump profile. The primary arXiv text was not fully available and equivalent classical leave-one-out interpolation identities may imply the rank-one step; the exact application is assessed best-of-knowledge with residual risk.

## value

PASS

The exact minimal count of external samples needed for residual indicators to respond differently to data is a meaningful design limit for WENO/Shepard-type interpolation. The nonzero exact jump response demonstrates a persistent local limitation of a natural two-stencil selection, without unsupported claims about full automatic implementations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
