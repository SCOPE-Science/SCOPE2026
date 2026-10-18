# Independent mathematical audit

## correctness

PASS

For integer n>=2 and 0<t=1/p<1, q dual to p, coordinate second moment of B_p^n is I_n(p)=2^n/3 Gamma(1+3t)Gamma(1+t)^(n-1)/Gamma(1+(n+2)t); orthogonal coordinate symmetry yields Ball functional B(B_p^n)=n I_n(p)I_n(q). Define Phi_a(t)=logGamma(1+at)+logGamma(1+a(1-t)); log F_n=Phi_3+(n-1)Phi_1-Phi_(n+2)+constant. Differentiated Gauss multiplication implies Phi_a doubleprime=sum_{r=1}^a G_t(r/a), G_t(x)=psi_1(t+x)+psi_1(1-t+x), strictly decreasing x>0 by the positive trigamma series. For N=n+2>=4 the N grid r/N, r=1..N, is termwise <= sorted multiset {1/3,2/3,1,...,1} with a strict first inequality; hence Phi_N doubleprime>Phi_3 doubleprime+(N-3)Phi_1 doubleprime and log F_n doubleprime<0 for all n,t. Symmetry t to 1-t and strict concavity give unique maximum p=2 and monotonic decay for p>2. Evaluating I_n(infty)=2^n/3, I_n(1)=2^(n+1)/(n+2)!, I_n(2)=pi^(n/2)/((n+2)Gamma(n/2+1)) gives the stated cube-crosspolytope endpoint. No assertion about general convex-body paths or p-parametrized concavity.

## originality

PASS

Best-of-knowledge: distinct exact theorem or implication not supplied by the materially inspected primary results; the same Resultary indexed SCOPE entry is the audited work, not prior independent coverage. F_n(t)<=1 and equality at t=1/2 allow non-monotonic oscillations below 1; the derived negative logarithmic second derivative and strict off-center order are stronger, and not a corollary of the inspected general inequality.

## value

PASS

Ball’s quadratic Santaló inequality is well-motivated in convex geometry. This theorem gives an exact strict profile on the canonical primal-dual ℓp family rather than just maximality at the Euclidean ball: it compares any two non-Euclidean exponents and computes a natural endpoint. The trigamma grid comparison is a nontrivial structural property, not merely restating a known pointwise upper bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
