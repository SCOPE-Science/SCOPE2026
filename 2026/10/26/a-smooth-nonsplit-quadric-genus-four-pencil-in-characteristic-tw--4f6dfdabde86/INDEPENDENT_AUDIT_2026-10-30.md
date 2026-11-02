# Independent mathematical audit

## correctness

PASS

PASS: Over the quadratic splitting field choose u=z+alpha w, v=z+alpha^q w and Segre parameters, obtaining exactly the (3,3) equation f(s)f(t)=kappa. Independently verified the full polynomial identity mod 2 by SymPy expansion. For kappa nonzero, f(s),f(t) are nonzero; with f prime=T^2, affine singularity forces s=t=0 and kappa=1. At infinity, f has simple roots (none zero) and the derivative is nonzero; kappa=0 consists of crossing horizontal/vertical components. Smooth connected bidegree (3,3) has K=O(1,1), degree6 and genus4. The unique nonsplit quadric has no k-ruling, so the canonical curve cannot carry a degree3 k-pencil (Faber-Grantham lemma), and not 1 or 2. The explicit point [1:t^2:t:0] satisfies both equations; Riemann-Roch supplies a nonconstant k-pencil of degree<=4. Existence: q=4 take t outside F2; q>=8 avoid at most six roots of f(f+1); F2 has no allowable kappa. Derivatives and boundary charts, geometric vs arithmetic gonality and all quantifiers were examined; finite-field package testing does not prove geometric smoothness.

## originality

PASS

PASS, qualified: The prior Faber/Grantham results already show the genus-four/nonsplit quadric mechanism and an isolated F2 example; Faber-Grantham-Howe poses the existence question and sketches an odd-characteristic approach. The concrete characteristic-two one-parameter pencil with exact two-point discriminant and uniform rational-point choice for all even q>=4 is not among the explicitly inspected results.

## value

PASS

PASS: A single explicit coefficient-marked pencil gives a complete geometric smoothness discriminant and a uniform rational-point certificate over every even finite field above a sharp exception, realizing maximal ground-field genus-four gonality in a natural canonical class. This resolves a meaningful explicit-construction gap in a stated finite-field gonality problem and is more than a random finite-field search.

The dated certificate retains the supplied scientific assessment, sources and limitations.
