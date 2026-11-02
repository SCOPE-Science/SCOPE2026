# Independent mathematical audit

## correctness

PASS

For one-dimensional full even N>=4, alpha=1, kernel K=1+gamma sum_{k≠0} e^{2πik(s-t)}/k² and density mu=(π/2)|sin2πt|, nonzero circulant DFT modes of optimal weights equal integrals of periodic triangular nodal hats. Only the zero mode differs, yielding w_j=b_j-gamma*d_N/[N(1+gamma*a_N)]. Direct Fourier series of mu and cotangent sum give d_N=1-(π/N)cot(π/N)>a_N and b_min=B_N=1/2-N sin(2π/N)/(4π), only at j=0,N/2 by circular-unimodal convolution. Thus solving w_min=0 yields exact gamma_N, with two zero weights at equality and negative above. Transformed node coincidences allow a nonnegative polynomial supported only at x=0 to witness negative quadrature. Taylor expansion gives gamma_N=N+π²/3+O(N^-1), while constant Q(1) crosses at gamma=(d-a)^-1~45 N^4/π^4. Independent quadrature and direct Bernoulli-kernel matrix solves for N=4,6,...,16 matched hat+offset to 8.3e-13. Finite checks corroborate the Fourier argument, do not establish all N.

## originality

PASS

The October 2026 Bartel–Gilbert–Griebel–Kuo–Sloan method and kernel-optimal equation are direct background. Karvonen–Kanagawa–Särkkä (2019) gives general sufficient conditions and positive Brownian-hat cases, but those involve a different constant-mode normalization and do not establish this Chebyshev-density threshold. The recent method paper complete text could not be retrieved through public arXiv/OA attempts and authorized institutional access returned storage_limit. Best-of-knowledge O PASS is therefore qualified by this material same-method priority risk rather than a false full-text noncoverage claim.

## value

PASS

The exact loss of nonnegative weights for a natural kernel-based cubature algorithm is a numerical-stability boundary; identifying a linear-in-N onset while the constant remains positive to quartic-in-N gamma separates two fundamentally different positivity notions. It provides an explicit nonnegative polynomial counterexample rather than only numerical instability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
