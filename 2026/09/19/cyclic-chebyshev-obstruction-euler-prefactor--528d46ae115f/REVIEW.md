# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**PASS.**

The result rests on a direct extension and exact optimization of the cyclic functional in Yang, arXiv:2609.14769.

For even \(k\), replacing the half-shift functional
\((F(1/2)-F(k+1/2))/2\) by
\((F(a)-F(k+a))/2\) still annihilates the one-dimensional sampling kernel spanned by \(\sin(\pi t)\). Applying the source cardinal formula gives the stated weights
\[
w_j^{(a)}
=
\frac{(-1)^j\sin(\pi a)}
{2k\sin(\pi(a-j)/k)}.
\]
Their total absolute weight and maximum absolute weight are obtained by direct pairing and nearest-sample geometry.

The source proof before its final coarse estimate gives
\[
H\ge W_k-2k\epsilon(H+1)\|w\|_\infty.
\]
The same argument with the shifted weights therefore gives the exact certificate
\[
\epsilon<
\min\left\{
1/k,\,
(W_k(a)-H)/(2k(H+1)M_k(a))
\right\}.
\]
The condition \(1/k\) is the same strict spectral condition \(\epsilon k<1\) used in the source.

The asymptotic for \(W_k(a)\) was checked by endpoint-singularity subtraction and digamma identities. Substitution into the exact certificate reduces optimization to
\(u e^{-u/A}\), whose unique maximizer is \(u=A\). The half-shift constant reduces algebraically to
\(8e^{\gamma-1}/\pi\). A compact numerical artifact checks the half-shift cosecant asymptotic, the predicted optimizing period, and the scaled certificate.

## Originality

**PASS, to the best of our knowledge.**

The nearest source is Yang, arXiv:2609.14769. It proves the leading exponential coefficient \(\pi/2\) for the true Chebyshev-grid parameter and gives the explicit lower bound
\[
\frac{e^{-\pi/2}}{4(H+1)}e^{-\pi H/2}.
\]
Its Section 6 contains the exact pre-estimate with \(\|w\|_\infty\), but then replaces that quantity by \(1/2\), uses only a lower bound for \(W_k\), and chooses a convenient period. It does not state the optimized Euler-constant prefactor, the asymptotically optimal period, or the shifted-phase family.

Searches were made for the source identifier and title together with terms including cyclic obstruction, two-point functional, shifted phase, cosecant sum, Euler constant, asymptotic prefactor, and Chebyshev--Lobatto robust interpolation. No equivalent result or stronger theorem covering the claimed phase-dependent certificate was located.

Finite cosecant sums have an extensive classical literature. Blagouchine's 2025 paper explicitly studies Watson-type cosecant sums and asymptotic expansions. The present review therefore treats the cosecant asymptotic as an ingredient, not as a new special-function result.

### Residual literature risk

Yang's preprint is very recent, so an unindexed contemporaneous refinement remains possible. Classical work on finite trigonometric sums was not exhaustively searched theorem-by-theorem; such work could contain equivalent formulas for \(W_k(a)\) or its digamma constant. That would not by itself cover the robust-interpolation optimization or the shifted cyclic obstruction, but it could reduce the novelty of the summation step.

The unsigned Erdős draft discussed by Yang gives a qualitative robust-interpolation argument and, according to Yang's description, no quantitative dependence of the obstruction parameter on \(C\). It was not used as evidence for originality of the new prefactor.

## Value

**PASS.**

The direct source explicitly notes that its Chebyshev-grid bounds do not determine a prefactor and that its cyclic proof uses an explicit but non-optimized admissible parameter. The present result exactly optimizes that explicit cyclic mechanism at leading order: it identifies the Euler-constant coefficient
\[
8e^{\gamma-1}/\pi,
\]
the optimal period scale, and the full fixed-phase exponent
\[
\pi/(2\sin\pi a).
\]
This also explains structurally why the half-period shift used in the source is distinguished: it is the unique fixed phase in the natural shifted two-point family that attains the optimal exponential coefficient \(\pi/2\).

The result is intentionally method-level rather than a claimed solution of the remaining true-prefactor problem.

## Limitations

The asymptotic equivalent is for the explicit shifted cyclic certificate, not for the true \(\epsilon_{\mathrm{Ch}}\). The order-\(H\) gap between Yang's best known upper and lower bounds for the true parameter remains open. The theorem treats fixed phases and does not optimize over all periodic functionals, all sign constructions, or phases varying with \(H\). It also inherits the source period-averaging argument's non-quantitative threshold in the grid size.

**Same-model review: passed. Cross-model review: not yet performed.**
