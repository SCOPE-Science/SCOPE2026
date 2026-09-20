# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**Passed.**

Qin's Theorem 1.1 and Lemma 2.1 were checked at theorem level. The source gives the four-Gaussian representations of both symbols, with unimodular coefficients, and the kernel identity
\[
T_{\sigma_U}K_a=2^{-n-2}K_{D_U^*a},
\qquad
D_U=\operatorname{diag}(U/4,I_{n-2}/2).
\]
The standard reproducing-kernel identity \(C_A^*K_a=K_{Aa}\) therefore identifies the building block with a scalar multiple of the adjoint of a linear composition operator.

The singular-value calculation was checked directly on the normalized monomial basis. The two first coordinate moduli are \(1/4\), the remaining \(n-2\) coordinate moduli are \(1/2\), giving
\[
\|T_{\sigma_U}\|_p^p
=
\frac{2^{-p(n+2)}}{(1-4^{-p})^2(1-2^{-p})^{n-2}}
\]
for every \(p>0\), and \(\|T_{\sigma_U}\|_1=1/9\). Four-term trace-norm subadditivity then gives the bound \(4/9\).

The singular-value tail estimate was also checked independently. Total degree is invariant, the norm on degree \(q\) is at most \(2^{-q}\), and the degree-\(\le m\) polynomial subspace has dimension \(\binom{n+m}{n}\). Finite-rank truncation therefore yields
\[
s_{\binom{n+m}{n}+1}\le 2^{-n-m-1}
\]
for each of the two Toeplitz operators. The zero product and nonvanishing are taken from Qin's theorem and are not inferred from the Schatten calculation.

## Originality

**Passed, to the best of our knowledge.**

Qin's paper states that the symbols are bounded, nonradial, Schwartz, and Gaussian-decaying, and proves the nonzero zero-product relation. Searches of the paper and of external literature for combinations of zero product, trace class, Schatten, nuclear, compact, Fock, and Segal--Bargmann terminology did not locate the all-Schatten zero-divisor formulation or the quantitative bounds above.

There is substantial prior art on Schatten regularity of Toeplitz/localization operators. Cordero--Gröchenig give broad Schatten criteria for localization/anti-Wick operators; Isralowitz--Zhu treat compactness and Schatten membership for positive-measure Fock Toeplitz operators; and recent Schatten--Lorentz work treats broad complex-symbol classes. These sources make it plausible that the qualitative membership of Qin's Schwartz-symbol operators in many or all Schatten ideals can also be recovered from general theorems. The originality claim is therefore deliberately narrow: it is the operator-ideal sharpening of Qin's explicit two-factor zero-divisor construction, together with the exact building-block Schatten formula, the uniform nuclear bound, and the explicit singular-value tail. No claim is made that the underlying regularity mechanism is new.

Older or differently formulated localization-operator results remain the main residual prior-art risk. No source found in the search stated the same two-factor Fock zero-divisor conclusion with these quantitative estimates.

## Value

**Passed.**

The result sharpens the regularity boundary in a newly resolved Toeplitz zero-product problem: not only boundedness but compactness, trace class, and simultaneous membership in every Schatten quasi-ideal are compatible with two nonzero Toeplitz factors having zero product. The quantitative nuclear and singular-value estimates show that the obstruction persists far inside the compact ideal rather than only near its boundary.

## Limitations

The result is restricted to Qin's \(n\ge2\) construction. It does not settle the one-dimensional two-bounded-symbol problem. The bound \(4/9\) and the singular-value tail are not claimed optimal. General Schatten regularity of rapidly decaying Toeplitz/localization symbols has extensive prior literature, so originality is limited to the stated synthesis and quantitative refinement.
