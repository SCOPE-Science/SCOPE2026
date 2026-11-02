# Independent mathematical audit

## correctness

PASS

Dirichlet moment and covariance inversion give K(x,y)=(S+1) sum_i x_i y_i/p_i -S, reproducing constants and coordinates. Since row absolute integral is convex, a maximal row is at a vertex and strict Jensen plus sign-changing neighborhoods excludes all nonvertices. At vertex e_i, its value reduces to E|((S+1)/p_i)Y_i-S| with Y_i~Beta(Sp_i,S(1-p_i)); splitting at t=Sp_i/(S+1) yields exactly F_S(p_i). To compare 0<p<q<1, couple (A,B,C)~Dirichlet(Sp,S(q-p),S(1-q)); (A+B)/q=E[A/p | A+B] is a strict mean-preserving contraction across the absolute-value kink, so F_S(p)>F_S(q). This gives unique fixed-S balancing, boundary supremum and the fixed-alpha gamma, fixed-total and fixed-dimension Gaussian limits with uniform-integrability/moment bounds. Independent incomplete-beta evaluations for S=6,p=1/6 and 1/3 give 4.551972392 and 3.090557506; for S=7 and p=.05,...,.95 strict order holds; fixed-alpha n=240 gives normalized norm 0.736194 approaching 2/e=0.735759; S=5000,n=3 yields 1.128558 approaching sqrt(4/pi)=1.128379. The checker code uses exact rational integer beta moments, but universal strict inequality relies on the conditional Jensen proof.

## originality

PASS

The first-degree Jacobi kernel and beta marginals are prior results of Griffiths--Spano and related classical orthogonal-polynomial theory. The equal-weight uniform simplex norm was already published. The assessed new theorem is the full asymmetric sharp norm profile together with strict convex-order balancing and three joint asymptotics, not a fresh claim to the kernel formula or beta identities.

## value

PASS

Dirichlet/Jacobi densities are standard families of weighted polynomial approximation, and the endpoint projector norm is a natural stability/positivity invariant. Showing that only p_min matters and proving unique balancing at fixed total concentration solves a natural optimization problem; the qualitatively different high-dimensional regimes have direct stability meaning, rather than a mere parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
