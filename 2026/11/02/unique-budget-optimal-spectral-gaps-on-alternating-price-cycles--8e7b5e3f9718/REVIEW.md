# Independent mathematical audit

## correctness

PASS

Rotation averaging follows from Rayleigh-quotient concavity of lambda_2, producing at least one alternating optimum. The Bloch lower band at theta=2pi/m gives lambda_2(a,b)=a+b-sqrt(g^2(a+b)^2+h(a-b)^2), including m=2. The stated unit-vector Cauchy-Schwarz inequality yields exact upper bound 2B sin^2(pi/m)/(m(p+q+2sqrt(pq)g)), attained by the explicit a*,b*>0. Equality is unique among alternating designs. For unrestricted independent edge weights, PSD equality under rotation averaging forces every vector of the repeated Fiedler eigenspace to be an eigenvector of each optimum. Subtraction at each B vertex gives a complex linear relation in two real edge deviations, with coefficients non-collinear because 1,r,e^(2pi i/m) are three distinct unit-circle points; both deviations must vanish. The m=2 two-dimensional Fiedler case separately forces all four equal. Direct independently computed m=3,p=1,q=4,B=1 yields a=2/21,b=5/84, gap 1/14 and matching full six-eigenvalue spectrum. No finite optimization is used as the uniqueness proof.

## originality

PASS

Ghosh-Boyd prove concavity and symmetry averaging in Laplacian optimization; this method alone does not yield the explicit optimal allocation or uniqueness among every independent edge on alternating-price cycles. Wan et al. discuss generic structural eigenvalue design, different hypotheses; the Resultary weighted odd-cycle fourth-power result has a different graph and objective. The four-cycle equal-conductance case is not claimed independently novel; the infinite family exact price interpolation and global rigidity are the new statement. Specialized older priced-cycle work remains possible.

## value

PASS

Finding the exact maximum algebraic connectivity under alternating per-edge costs is a natural communication/consensus network design question. Exact unrestricted uniqueness is important because no symmetry is imposed on the designer; the allocation interpolates between equal four-cycle weights and inverse square-root price allocation, with an explicit speed gain approaching two. The result covers all even sizes, not an arbitrary finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
