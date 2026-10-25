# Independent mathematical audit

## correctness

PASS

Derived coarea-normalized pushforward densities kappa_(m-1) a^-m (a^2-v^2)^(m-1)/2 and similarly for n; their convolution yields the actual section-volume formula for unit normal. When both exponents p,q integers (both factor dimensions odd), expand polynomial integrand and evaluate at finitely many algebraic endpoints min(a,t+b), max(-a,t-b), giving finitely many algebraic branches and, by elimination of a^2=||xi_1||^2,b^2=||xi_2||^2, one joint polynomial relation for integrated cutoff volumes. If exactly one exponent is half-integer, monomial primitives contain arcsin of (t-a)/b; its polynomial coefficient is nonzero because its highest t term has integral of a strictly positive (1-w^2)^(k+1/2), so nonalgebraicity by infinite monodromy. If both exponents half-integers, colliding endpoints at internal knot t=a-b yield nonzero epsilon^j log|epsilon| via binomial(q,j), j=(m+n)/2; for a=b the two contributions cancel at odd j but the next even j+1 logarithm has coefficient proportional (q-p)j binom(q,j)/(j+1), nonzero since odd j forces p!=q. Independently checked exact symbolic normalized coefficients (m,n)=(2,2):2,(2,4):-pi/2,(4,4):-2pi^2/3, and the exact 3+3 convolution polynomial; inspected source verify.py quadrature/fits as finite corroboration only. Algebraic functions cannot develop these logarithms (Puiseux), and algebraic cutoff derivative would be algebraic section density, giving the obstruction. Singular-axis normals ab=0 are separately algebraic and do not alter the all-direction criterion.

## originality

PASS

Best-of-knowledge after two real Resultary searches, public-primary reading and comparison of mathematical implications, not merely titles. Classical convolution of slice densities is known and not claimed novel. Neither uniform-separability rigidity nor smooth-ellipsoid results imply the product-specific iff parity and exact resonance coefficient; those require evaluating exponents and local monodromy.

## value

PASS

Algebraic integrability of hyperplane slices is a central question in convex geometric tomography. This theorem provides a full parity classification for a canonical nonsmooth two-factor convex-body family and addresses a subtle equal-radius resonance that defeats a naive leading-log argument. It identifies explicit nonsmooth globally algebraic examples, not merely a genericity computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
