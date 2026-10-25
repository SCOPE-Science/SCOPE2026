# Independent mathematical audit

## correctness

PASS

Gamma integral of h_N gives Laplace profile Phi_N(x)/x with Phi_N=(4x/(1+x)^2)^N; angular integration produces exactly nonnegative Bergman diagonal lambda_n=sum_j Phi_Nj((n+1)/K_j). The h_N L1 mass <=8^N/2 and K_j=M 16^j 8^Nj make sum <=1/(30M)<epsilon. The K_j ratio >=16 bounds lambda_n<=128/15 while lambda_(K_j-1)>=1 at infinitely many distinct indices, so a bounded positive noncompact diagonal operator exists with essential norm>=1. For Berezin B_NK(s) the kernel coefficient m(1-s)^2 s^(m-1)<=4/m, and unimodal mesh bound with ∫Phi_N(x)/x dx =4^N B(N,N)<=4/sqrt N give sup B_NK<=16/sqrt N+12/K. N_j=(j+1)^4 makes these suprema summable, each block compact, so boundary B(s)->0 by dominated convergence. L1 convergence justifies fixed-kernel form interchange but no false operator-norm convergence is used. Independently recomputed exact rational Laplace identities for N=2..7 and x=1/3,1,5/2 and checked beta integrals.

## originality

PASS

General positive noncompact Toeplitz examples with vanishing Berezin are prior (Looi 2026). Its compact radial building blocks are translated by nonradial Bergman automorphisms; it explicitly says the radial L1 case remains open, and does not yield a radial final symbol. The present explicit inverse-Laplace construction answers that specific radial-symbol gap, not merely the general phenomenon.

## value

PASS

The radial restriction is not an arbitrary slice: radial Toeplitz forms are diagonal and bounded-symbol compactness/Berezin equivalences are known. The example separates symbol L1 mass from essential operator norm under positivity, closing a stated gap in the unbounded radial class by a constructive operator, with a meaningful new boundary to the compactness criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
