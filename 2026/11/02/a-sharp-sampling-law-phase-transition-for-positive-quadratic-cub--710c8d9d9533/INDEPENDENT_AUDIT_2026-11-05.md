# Independent mathematical audit

## correctness

PASS

For iid arcsine X_i and target moments (1,0,q), q in (0,1), strictly positive all-node weights exist iff both signs occur and a*b<q<A*B, where a,b are smallest opposite-sign magnitudes and A,B largest. This follows from the convex hull of (x,x^2) and its x=0 vertical section. Extreme-point integrals decompose failure into outer-spread U and central-gap L. Nondegenerate interior Laplace saddle at a=sqrt(q) yields L~sqrt(sqrt(q(1-q))/r_in)*sqrt(m)*r_in^m, while two endpoint contributions yield U~2 r_out^m. Rates r_in=1-2 asin(sqrt(q))/pi strictly decrease, r_out=1/2+asin(q)/pi strictly increase, with sole crossing at q=1/3; at equality sqrt m makes L dominant. The finite-m double integral is correctly derived. m=2 has P=0 and strict boundary equalities have probability 0.

## originality

PASS

Neumayer–Schaefer–Ullrich 2026 establish existence of positive random-node cubature with high probability under Lewis-type sampling and oversampling, not exact arcsine-node quadratic moment feasibility, exact failure integrals or the polynomially corrected phase transition. Bělik–Narayan–Turnage provide constructive Tchakaloff and randomized least squares in the closely related application but do not state the exact all-positive Chebyshev-node event in their inspected Sections and theorems. Uniform-node quadratic feasibility was known and explicitly distinguished.

## value

PASS

The target moment q=1/3 corresponds to integrating 1,x,x^2 under uniform target measure, while nodes are sampled from a different natural Chebyshev law; the exact endpoint/interior-hole competition gives a sharp and practically motivated sampling threshold and quantifiable exponential gain over uniform nodes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
