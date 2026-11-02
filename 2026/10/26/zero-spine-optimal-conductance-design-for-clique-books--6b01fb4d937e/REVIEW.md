# Independent mathematical audit

## correctness

PASS

For connected weights, K=N(tr((L+J/N)^-1)-1) is strictly convex in individual edge weights since Laplacian edge coordinates are injective in a simple graph and trace inverse has positive quadratic Hessian. A global minimizer exists because K diverges at disconnectivity and graph symmetry forces the unique optimum to three edge orbits a,b,c. Direct eigenspace decomposition produces eigenvalues 0, ms a+2c, Na, 2a (m-1 copies), 2a+sb (m(s-1) copies). The transformed budget and positivity constraints reduce the c=0 face to A/a+Nm(s-1)/y with cost m(s+1)a+m(s-1)y/2=B; Cauchy–Schwarz gives T²/B at a*/y*. The all-parameter inequality 2<rho=y*/a*<ms proves b*>0 and strictly positive multiplier mu=N/y*²−N/(m²s²a*²)>0 for active spine constraint, satisfying the full three-variable KKT system; thus this is globally, not merely facewise, optimal. Independent exact-rational 6x6 Laplacian charpoly and inverse trace verified at m=s=2, and separately coded inequality checks covered every 2≤m,s≤19; finite tests support but do not prove the global integer range.

## originality

PASS

General convex effective-resistance design and weighted graph symmetry criteria are prior, but the inspected primary worked examples do not entail the exact zero-spine solution for K2∨(mKs), all m,s≥2, including proof of strict positivity of all non-spine weights. Neither nonconvex sparsity-regularized network designs nor topology-only optimizations imply the claimed unpenalized optimum. Historical specialized terminology/uncaptured general formula remains a risk.

## value

PASS

Kirchhoff-index minimization is a natural practical/electrical network-design objective. A pre-existing dense hub edge strictly reduces resistance if added without cost yet receives exactly zero optimal budget; the theorem proves that counterintuitive network-support transition for an infinite structured graph family, excludes asymmetric improvement, and evaluates every positive conductance and optimal value explicitly. This is a substantive sharp structural design result, not a generic restatement of convexity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
