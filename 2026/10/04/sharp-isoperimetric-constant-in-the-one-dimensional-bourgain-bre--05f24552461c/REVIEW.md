# Review of Sharp isoperimetric constant in the one-dimensional Bourgain--Brezis model

## Correctness

PASS. The primary source fixes the Fourier convention, Hermitian pairing, Hardy projections, and the exact identity
\[
\|\Pi_+f\|_{\dot H^{-1/2}}^2-\|\Pi_-f\|_{\dot H^{-1/2}}^2
=
\langle f,|D|^{-1}\operatorname{sign}(D)f\rangle.
\]
Under that convention, the inverse transform of \(1/\xi\) is \((i/2)\operatorname{sign}(x)\). Mean zero therefore turns the operator exactly into \(iF\), where \(F\) is the closed primitive. The Hermitian pairing is exactly twice the algebraic area of that curve. Arclength parameterization, periodic Wirtinger, and Cauchy--Schwarz give
\[
|\mathcal A(F)|\le \frac{\|f\|_1^2}{4\pi},
\]
so the energy imbalance is bounded by \(\|f\|_1^2/(2\pi)\). Equality in both inequalities forces a first harmonic with equal orthogonal coordinate amplitudes, hence a once-traversed circle. The explicit circle primitive attains the coefficient. The source's annular approximation, or equivalently symmetric frequency truncation, passes the identity and sharp bound to the stated \(L^1_0\) class and simultaneously proves finiteness of the missing frequency component.

## Originality

PASS with a stated terminology risk. The full primary paper was inspected through Appendix A. Proposition A.1 gives only an unspecified comparison constant, despite writing the exact difference-of-frequency-energies identity used here. It does not identify that pairing with algebraic area, state the coefficient \(1/(2\pi)\), or classify equality.

A full later paper by the same author on Bourgain--Brezis selection maps was also inspected. Searches of that text for one-dimensional, Hilbert, and isoperimetric formulations found no matching refinement. Classical geometric references do contain the sharp signed-area isoperimetric theorem and its Fourier proof, but not the operator-theoretic half-Sobolev statement in the recent Bourgain--Brezis model.

Semantic searches covered Hardy projections, positive/negative frequency imbalance, \(\dot H^{-1/2}\) endpoint estimates, Hilbert-transform primitives, signed area, and isoperimetric formulations. No covering published statement was located. The residual risk is that this exact reformulation may appear in older Fourier-geometry literature under terminology not connected to Hardy projections.

## Value

PASS. The source presents the one-dimensional estimate as the model for its Hilbertian reflection mechanism, but leaves its constant hidden. The result identifies the cancellation quantity geometrically, determines the optimal coefficient, and classifies every equality case. This is a natural structural completion of the model estimate rather than an arbitrary constant optimization: it explains why the self-pairing has substantially more cancellation than the raw endpoint operator bound and converts the analytic endpoint mechanism into a classical extremal geometry problem.

Same-model review: passed. Independent audit: not yet performed.
