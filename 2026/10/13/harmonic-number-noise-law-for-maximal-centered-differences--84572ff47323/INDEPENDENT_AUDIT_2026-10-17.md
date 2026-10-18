# Independent mathematical audit

## correctness

PASS

For each m>=1 and h>0, differentiation of degree-2m equispaced Lagrange cardinal polynomials yields weights alpha_{m,j}=(-1)^(j+1)(m!)^2/[j(m-j)!(m+j)!] on paired +/-jh nodes. The beta-integral identity a_{m,j}=binom(m,j)*int_0^1 t^m(1-t)^(j-1)dt gives sum_j a_{m,j}=H_m/2 after substituting s=1-t. Therefore the l_infinity sampled-input norm is exactly 2sum|alpha|/h=H_m/h; aligned signs independently attain it. Independently reconstructed exact rational weights and every polynomial moment through degree 2m for m=1..20, all passed. This is not a stochastic-noise, nonuniform-grid, or floating-point-weight computation result.

## originality

PASS

The prior complete available Sadiq–Viswanath source gives finite-difference weight algorithms and stability of coefficient computation, while the closest Resultary hit concerns monotone-data behavior. Neither inspected material directly states the sharp all-order H_m/h sampled-noise operator norm. Fornberg original PDF inaccessible this execution; older conditioning formulas remain the explicit priority risk.

## value

PASS

This is a sharp, exact all-order robustness invariant for a canonical maximal-order differentiation stencil. It quantifies the log m data-noise tradeoff independently of coefficient-generation algorithms, including matching extremizers; this is mathematically useful rather than merely a few numerical cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
