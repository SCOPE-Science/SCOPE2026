# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS. The starting phase equation, principal eigenvalue formula, parity statement, and symmetric secular equation were checked directly in arXiv:2609.20221v1. For the principal symmetric mode, the phase equation gives the centered cosine form exactly. Expanding the symmetric secular equation yields

\[
2N\tan(\xi_N/2)\tan(\xi_N/(2N))=\frac{2N(1-\rho_N)}{1+\rho_N}.
\]

The left side is strictly increasing on \((0,\pi)\), converges locally uniformly to \(\xi\tan(\xi/2)\), and diverges only as \(\xi\uparrow\pi\). This establishes the finite and infinite scaled-correlation regimes. The finite-N overlap formula follows from exact geometric trigonometric sums; its limit gives the claimed alignment. Strictness of the DCT mismatch for positive scaled parameter follows because the limiting cosine profile is nonconstant. The largest-eigenvalue scaling follows by direct substitution into the exact eigenvalue formula.

A standalone numerical artifact independently constructs the dense covariance matrix and compares its top eigenpair with the phase-equation formulas. The tested overlap formula agrees to machine precision, and the eigenvalue checks converge as predicted. The small-parameter expansion was also checked numerically.

## Originality

PASS, to the best of our knowledge, with a deliberately narrow claim. Classical facts excluded from novelty include the AR(1)/Kac-Murdock-Szegő eigenproblem, the fixed-block limit from KLT to DCT-II as \(\rho\to1\), sinusoidal-family asymptotic-equivalence results, explicit AR(1) KLT kernels, and the continuum Karhunen-Loève eigenproblem for the exponential covariance kernel.

The recent motivating paper arXiv:2609.20221v1 explicitly states that its correction factors become identities as \(\rho\to1\) and develops exact DCT-core-plus-correction factorizations, but no growing-\(N\) uniformity condition or joint \(N,\rho\) scaling was found there. The 2013 Torun-Akansu paper was inspected in full around its DCT comparison and states the classical \(\rho\to1\) kernel identity; its numerical comparisons use fixed high correlations and finite block lengths. Searches combining AR(1), KLT, DCT, Kac-Murdock-Szegő, local-to-unity, \(N(1-\rho)\), and \(\rho=e^{-a/N}\) found classical fixed-parameter asymptotics and continuum exponential-kernel literature, but no source giving the explicit principal-mode overlap phase transition, the iff criterion \(N(1-\rho_N)\to0\), or the resulting nonuniformity statement for the fixed-size DCT endpoint. Existing SCOPE records were searched by the source identifier and synonymous mathematical terms, with no overlap found.

R. J. Clarke's 1981 two-page paper “Relation between the Karhunen-Loève and cosine transforms” is the most relevant residual originality risk. Its bibliographic record and later descriptions were inspected, but the full original text was not available in the checked sources. It is consistently cited for the fixed-\(N\), \(\rho\to1\) DCT-II limit; if it contains a joint growing-block result not reflected in later citations, the originality scope would need revision. A. K. Jain's 1979 paper is also a historical risk because its abstract states asymptotic equivalence of a sinusoidal transform family and warns that DCT is not always a good finite approximation to the AR(1) KLT. The checked abstract does not state the local-to-unity rowwise limit or the sharp \(N(1-\rho)\) criterion.

The classical continuous exponential-covariance KL solution is explicitly treated as background, not as a new result.

## Value

PASS. The result supplies a sharp and dimensionless design parameter for a current numerical-linear-algebra construction: block length divided by correlation length. It shows that a fixed-size statement used to motivate disappearance of the exact KLT correction factors is strongly nonuniform in dimension. The principal-row formula gives both an exact limiting angle and a necessary obstruction to operator-norm convergence of an uncorrected DCT approximation. This is directly useful when deciding whether the new correction factors can be truncated or omitted for large blocks with highly correlated data.

## Limitations

Only the principal KLT basis vector is characterized sharply. The result does not derive a complete norm asymptotic for the full correction matrices, nor does it quantify coding gain, rate-distortion loss, floating-point behavior, or the cost/accuracy tradeoff of a particular truncation strategy. It does not contradict classical aggregate notions of asymptotic equivalence between DCT and KLT. The continuum exponential-kernel interpretation is classical and is included only to identify the scaled parameter physically.
