# Review of Lower moment thresholds for independent-coordinate high-dimensional random walks

## Correctness
PASS. For fixed times, scalar \(p\)-moment convergence implies uniform integrability of \(n^{-p/2}|\sum_{j\le nt}\xi_j|^p\); independence across coordinates then gives a triangular weak law by truncation for every \(d(n)\to\infty\), with no \(2p\)-moment. Jin's monotone-plus-martingale decomposition remains valid. Squaring its martingale term requires the partial-sum moment of order \(2p-2\), and the dimension factors yield \(\mathbb E|Q_n|^2=O(n^p/d)\). Doob's inequality and Jin's grid/block argument then give the uniform metric limit and the Gromov--Hausdorff conclusion.

## Originality
PASS. The motivating theorem assumes a finite \(2p\)-moment under pairwise uncorrelated coordinates and explicitly notes the stronger-than-known fourth moment at \(p=2\). Kabluchko--Marynych cover the Hilbert \(p=2\) iid-coordinate case under finite variance, but not non-Hilbert \(p\ne2\). Targeted searches for the independent-coordinate non-Hilbert theorem with a finite \(\max\{2,2p-2\}\)-moment, its finite-variance \(1<p<2\) specialization, and its \((2p-2)\)-moment \(p>2\) specialization did not identify a source implying the final claim.

## Value
PASS. The result isolates where Jin's \(2p\)-moment is spent and shows a natural structural tradeoff: full coordinate independence removes the bivariate \(2p\)-moment bottleneck, leaving only the lower martingale moment. This materially enlarges the admissible tail class for every non-Hilbert \(p>1\), including a finite-variance theorem throughout \(1<p<2\), while retaining arbitrary relative growth of time and dimension.

The main limitation is that the threshold is sufficient rather than proved optimal, and the theorem does not improve the moment assumption under mere pairwise uncorrelatedness.

Same-model review: passed. Independent audit: not yet performed.
