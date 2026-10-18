# Independent mathematical audit

## correctness

PASS

At t=1 the exact published quartic F_1 and its homogeneous Hessian give the resultant 729*x^3*(x^3-3x+1)^6*(106x^3+3x^2-6x-2). The source verifies no intersections at infinity and a residual Gröbner basis q(x), 106x^2+23x+19y+3, isolating three smooth flexes; at x=0 tangent contacts are 3 at P0 and 4 at H. Independently recomputed the homogeneous Hessian and factorized resultant in exact SymPy rational arithmetic and checked the cubic discriminant -1026^2 and the mod-5 irreducibility argument. Therefore the residual roots are one degree-three irreducible divisor, with Galois S3 (one real, a complex conjugate pair), and the weight cycle sums to 24. The claim concerns solely this singular quartic over Q, not the general Kenyon–Smillie family.

## originality

PASS

Lax's primary published computation identifies this quartic's singular points and flex-weight pattern and reports the three residual weight-one flex coordinates numerically, not with an exact cubic/Galois orbit in the inspected principal computation. The candidate supplies explicit rational elimination, irreducible degree-three divisor and S3 arithmetic refinement. Full-text coverage cannot be excluded in other research or software appendices; the specifically inspected Lax treatment contains only approximations.

## value

PASS

An exact Galois-stable Weierstrass divisor on a named Teichmüller-curve cusp fiber is a natural arithmetic-geometric invariant that upgrades a numerical flex list to reproducible exact coordinates and field of definition. This is narrowly but genuinely useful for comparisons of special fibers and arithmetic of canonical divisors, not an arbitrary slice chosen solely to print a polynomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
