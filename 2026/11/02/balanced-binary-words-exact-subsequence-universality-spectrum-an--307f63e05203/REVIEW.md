# Independent mathematical audit

## correctness

PASS

The greedy shortest-prefix arch decomposition gives the universality index exactly: each arch is 0^r1 or 1^r0 (r>=1), followed by a unary remainder. Mark word length z, excess ones-minus-zeros x and arch count u. The exact Laurent rational generating function F=(1-z²)/(1+(1-2u)z²-z(1-uz²)(x+x^{-1})) follows, with balance equal to CT_x. Applying CT(1/(a-b(x+x^{-1})))=(a²-4b²)^(-1/2) and factoring yields B(t,u)=sqrt((1-t)/(1-(1+4u)t+4u²t²)). Dominant root rho(u)=2/(1+4u+sqrt(1+8u)) is analytic around u=1 and provides mean 2n/3+2/9+O(1/n), variance 4n/27-2/81+O(1/n), and a Gaussian CLT by local quasi-powers/characteristic functions. Independent exhaustive enumeration of balanced words at each n=1,...,7 agreed with coefficients and both high-index boundary counts. Enumeration does not establish the all-n formula or CLT; the formal constant term and analytic transfer do.

## originality

PASS

The prior 2026 published binary universality law has rational GF (1+z)/(1-z-2uz²), summing over ALL binary words of each length, and is not the fixed-composition specialization. The submitted radical counts only exactly n zeros and n ones, adds conditional asymptotics. Day et al. study fixed-length scattered-factor spectra and maximum-universality boundary; arch factorization itself is old. No inspected earlier statement encodes the precise conditional radical law. An earlier Dyck-word enumeration has an algebraic transform relation but applies to nonnegative-prefix paths, not arbitrary bridges; possible implicit coverage through transform identities remains a risk.

## value

PASS

A complete equal-composition distribution and conditional central limit theorem quantify a basic universality statistic for random constrained words. Conditioning on exact balance changes both enumeration and asymptotic fluctuation constants, making the fact useful for random balanced combinatorics beyond the known unconstrained count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
