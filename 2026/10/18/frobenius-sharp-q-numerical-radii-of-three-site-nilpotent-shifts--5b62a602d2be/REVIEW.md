# Independent mathematical audit

## correctness

PASS

Diagonal unitary conjugations remove the phases and rotate the whole constrained range, so the radius is the maximal real part. The Hermitian part has eigenvalues 0 and ±1/2 at the stated Frobenius normalization, proving q=1 and giving F(t)=||T+tI||≥t+1/2. Convexity is strict: equality for distinct shifts would produce a common norming vector with positively collinear shifted images; their difference forces it to be an eigenvector of T, hence killed by nilpotency, contradicting F(t)>t. For t>0 and two positive weights, the top eigenvalue of the Gram matrix is simple by irreducible nonnegative tridiagonal structure. With one weight zero the nontrivial 2×2 block dominates the isolated singular value t and still has a simple largest singular value. Norm differentiation gives the overlap of the top singular vectors; F'(t) tends to 1 by convexity and t≤F(t)≤t+||T||. At t=0 the right derivative is 0 for distinct weights. For equal weights the first derivative of the Gram matrix compressed to its top eigenspace has eigenvalues ±1/sqrt(2); conversion to the singular value gives right derivative 1/2. Nonnegative top pairs at zero realize every overlap up to that value. Thus the finite minimum of F(t)−qt for q<1 is attained by a singular-pair witness at the appropriate slope or at zero, not just an upper bound. The characteristic polynomial has trace coefficient 3t²+1, principal-minor coefficient 3t⁴+t²+π, and constant −t⁶. At the simple largest root its z-derivative is positive, so the root decreases strictly with π, with continuous endpoint extension; the t=0 root also decreases strictly. Evaluation at a finite minimizer for the smaller π transfers strictness to the radius. This identifies both equality cases, and direct minimization for one edge and the balanced cubic derivative yield the profiles. For an unbalanced allocation, the positive minimizing shift for any q>0 gives strict decrease in q, including departure from q=0.

## originality

PASS

The rank-one endpoint, circularity, scalar norm-envelope mechanism, balanced plateau, and balanced Jordan profile have existing coverage. The 2010 primary paper actually includes the balanced plateau at its b=0 endpoint, contrary to the frozen discussion's omission. The supported distinct claim is the strict fixed-energy ordering of all two-edge allocations for every q<1, with the resulting simultaneous unique extremizers. The inspected cubic geometry, endpoint results, and a related dilation-radius calculation do not imply that ordering.

## value

PASS

The fixed Frobenius budget makes this the first one-step shift family with a free allocation between two nonzero links. Uniform strict ordering solves a natural optimization of the q-numerical radius and its scaled version simultaneously for the full overlap interval, distinguishing the rigid interior regime from complete degeneracy at q=1. It gives sharp constants and exact equality cases for all admissible weights, not merely computations of previously known endpoints.

The dated certificate retains the supplied scientific assessment, sources and limitations.
