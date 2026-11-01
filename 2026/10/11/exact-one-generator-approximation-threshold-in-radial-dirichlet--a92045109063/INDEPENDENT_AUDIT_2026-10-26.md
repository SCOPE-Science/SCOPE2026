# Independent mathematical audit

## correctness

PASS

For fixed d>=s>=1, real beta, and positive normalized p_j, checked both directions of polynomial division: deg(P)<=N iff the remainder R=1-(1-t)P has deg<=N+1 and R(1)=1. Distinct homogeneous t^n are orthogonal under the radial total-degree coefficient norm and have exact weights w_n=(n+1)^beta V_n(p). Weighted Cauchy-Schwarz gives E_N^2=(sum_{n=0}^{N+1}1/w_n)^-1, achieved by unique r_n=(1/w_n)/sum_j(1/w_j). Torus Parseval for V_n has unique maximal phase on its (s-1)-torus; the log-modulus Hessian is A=diag(p_1,...,p_{s-1})-vv^T positive definite with det A=product p_j, giving V_n~(4*pi)^(-(s-1)/2)*product p_j^(-1/2)*n^(-(s-1)/2). For s=1, V_n=1 and the formula follows directly. Positive-series comparison correctly gives the subcritical power, critical logarithm and positive supercritical limit, without assuming uniformity as weights tend to zero. For p=(1/2,1/2), Vandermonde gives V_n=binom(2n,n)/4^n. Independently implemented Fraction-based minimization and determinant/Vandermonde tests across support sizes 1-4 matched formulas; the infinite statement is supported by analytical localization and sum comparisons, not extrapolated from these finite checks.

## originality

PASS

Best-of-knowledge: investigated published mathematical research records, the entire accessible primary texts of the two contemporary radial Dirichlet/cyclicity sources, and classical product-weight optimal-approximant work. No independently established theorem located that implies the exact restricted fixed-affine all-N minimum, full unequal-weight support-size transition and constants. Published full cyclicity for beta<=2 quantifies over strictly more multipliers and does not entail restricted cyclicity; integral averaging across all affine slopes is not fixed-symbol substitution. This is not absolute priority certification; a recent thesis remained inaccessible.

## value

PASS

The fixed-one-generator multiplier class is motivated by the precise 3/2 difficulty of elementary radial Dirichlet cyclicity arguments. The finding determines an intrinsic and sharp barrier of that natural restricted scheme and exhibits an actual interval 3/2<beta<=2 where it fails despite known unrestricted full cyclicity. Its unique finite-N minimizer, exact all-degree errors and unequal-weight support-rank critical exponent give a reusable quantitative diagnostic, not an arbitrary tiny finite slice or mere reformulation of known unrestricted cyclicity. It does not assert the stronger statement about arbitrary multivariate polynomials.

The dated certificate retains the supplied scientific assessment, sources and limitations.
