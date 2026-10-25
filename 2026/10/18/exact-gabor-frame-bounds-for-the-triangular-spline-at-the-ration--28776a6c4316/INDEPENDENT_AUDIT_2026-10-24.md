# Independent mathematical audit

## correctness

PASS

The final claim fixes unit-height g(x)=(1−|x|)_+, translation a=1, and b=m/(m+1), integer m>=2. From the compact-support Walnut identity, only lag 0 and ±(1+1/m) survive, decomposing the infinite frame operator as a direct integral of m-by-m symmetric tridiagonal Jacobi fibers M_m(τ)/b. The diagonal entries D_j=((m-j-τ)^2+(j+τ)^2)/m^2 and offdiagonals e_j=(j+τ−1)(m−j−τ)/m^2 are explicit, with all endpoint phase terms treated a.e. A nonnegative row-sum bound ≤1 and endpoint eigenvalue 1 give sharp B_m=1/b. For the alternating-sign conjugate J, set μ_m=2(m−1)/m^2; positive gamma-binomial ground-state ratios v_(j+1)/v_j=(m−j−τ−1)/(j+τ) yield an exact PSD sum-of-squares with endpoint residuals, so eigenvalues ≥μ_m. At τ=0 the explicit binomial eigenvector on sites 1..m−1 attains μ_m in the spectral-edge limit. Thus A_m=μ_m/b=2(m²−1)/m³, condition ratio m²/[2(m−1)], A_m/(1−b)→2. An independent numpy implementation evaluated all Jacobi fibers for m=2..15 at τ=0,0.02,0.11,0.5,0.89,0.98: edge eigenvalues exactly μ_m and 1 to 1e−10, every tested interior eigenvalue above μ_m and max ≤1. This finite check corroborates the algebraic all-m ground-state proof.

## originality

PASS

Best-of-knowledge primary-statement comparison plus actual Resultary query, checked exact and broader implications, and explicit residual source-access risk. The novelty is the substantive stated result, not a theorem inferred merely from negative search.

## value

PASS

The compactly supported canonical hat spline is a model Gabor frame and b=m/(m+1) is the natural sequence approaching critical density with increasing rational denominator. Exact optimal spectral constants, condition number and linear critical slope go substantially beyond qualitative frame membership/nonsharp estimates and expose a motivated growing-family conditioning law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
