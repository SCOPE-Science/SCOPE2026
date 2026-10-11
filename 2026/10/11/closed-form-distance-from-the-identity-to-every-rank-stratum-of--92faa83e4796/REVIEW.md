# Same-model review

## Correctness
PASS. Chen's full-text distance formula was reconstructed with the ambient choice \(k=n\). After fixing the identity factor, every registered candidate of rank \(s\) is a collection of unit vectors in a common \(s\)-dimensional subspace. Projection onto that subspace gives the sharp termwise lower bound \(\arccos^2\sqrt{P_{ii}}\). The function \(p\mapsto\arccos^2\sqrt p\) is strictly convex, with the sign of its second derivative proved explicitly, so Jensen forces a constant projection diagonal. Real Schur--Horn supplies such a projection for every \(n\ge r\). Equality in each step yields exactly the constant-diagonal projections and therefore the claimed unit-norm-tight-frame Gram matrices. The corank-one equality classification is complete.

## Originality
PASS. The closest source is Hengchao Chen, *Quotient Geometry of Bounded or Fixed-Rank Correlation Matrices* (arXiv:2401.03126; DOI 10.1137/24M1630566). It defines the metric, proves the rank stratification, recommends the full ambient choice \(k=n\), and states that the nonlinear angular alignment problem has no closed-form solution in general before introducing numerical Riemannian gradient descent. It does not solve the identity-to-rank-stratum family. Exact-formula, alias, and database searches found no covering theorem. Classical frame-potential theory shares the tight-frame minimizers but optimizes a different quadratic energy, so it does not imply the arccos quotient value.

## Value
PASS. Rank is the organizing stratification of the motivating orbit space, and the source treats distance computation as a primary geometric task. The finding gives one exact distance for every rank stratum in every dimension and the complete optimizer set. In particular, it gives the exact distance from the identity to rank loss and shows that the nearest singular correlations are precisely the signed regular-simplex Gram matrices.

## Closest literature and limitations
The main source supplies the metric but not this closed form. Benedetto--Fickus supplies prior tight-frame structure under the frame potential, and Schur--Horn supplies the projection-existence lemma; both are credited as ingredients. A nearby indexed Wasserstein isotropization result has similar constant-projection geometry but a different cost and feasible class. The theorem is only for distances from \(I_n\) in the ambient metric \(d_{\mathrm{orb},n}\); arbitrary pairs and smaller ambient metrics remain outside the claim.

Same-model review: passed. Independent audit: not yet performed.
