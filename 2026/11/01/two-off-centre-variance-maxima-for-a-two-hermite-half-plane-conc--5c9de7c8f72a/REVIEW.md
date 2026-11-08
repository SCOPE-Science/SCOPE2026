# Independent mathematical audit

## correctness

PASS

Recomputed Gaussian tail compression A(t) from normalized h0 and h1 and diagonalized it. The exact trace defect is V=2Q(1-Q)+tϕ(1-2Q)-(1+t²)ϕ² with ϕ=e^-t²/sqrtπ. Differentiation gives V'=ϕ[4t(1+t²)ϕ-(1+2t²)erf(t)]. For t>0 the sign is that of R(t)-L(t), L=erf(t)/(2tϕ(t))=∫_0^1 exp(t²(1-u²))du strictly increasing from 1 to infinity, R=2(1+t²)/(1+2t²) strictly decreasing from 2 to 1. Hence exactly one positive root τ, and parity gives exactly stationary set {0,+τ,-τ}; V(0)=1/2-1/π, V''(0)=2/π positive, ±τ unique global maxima with tail limits zero. Independent symbolic expansion gave V=1/2−1/π+t²/π−4t⁴/(3π)+26t⁶/(45π)+O(t^8), numerical τ≈0.748111391996, Vmax≈0.257120277198. The polyanalytic Toeplitz identification follows by substitution in prior Hermite horizontal-Fourier fiber formula; it claims only fiber trace, not a global trace.

## originality

PASS

2018 horizontal-symbol poly-Fock Toeplitz representation and Lee-Guzmán et al Proposition 10.4 already give the Hermite integral matrix generality; their existing operator representation is not new. A distinct Resultary half-line Hermite spectral-gaps result at exactly t=0 gives midpoint parity and gamma/Barnes products, not the shifted t variable or two-peak variance extremum; this conclusion was drawn from its complete RESULT.md rather than snippets. Plausible earlier two-particle GUE counting-variance optimization under random-matrix vocabulary is a specifically retained priority risk.

## value

PASS

Determines an exact global, nonobvious symmetry-breaking maximizer of fermionic number variance in the first nontrivial Hermite fiber. The analytic monotone-ratio argument proves uniqueness for every threshold and distinguishes order-two behavior from the analytic order-one central maximum, making the result useful beyond an easily computed matrix entry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
