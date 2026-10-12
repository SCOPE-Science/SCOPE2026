# Rényi entropy for NTPN needs a real-order correction
## Finding
Let
\[
f(x;\alpha,\lambda)
=
\frac{q(x)}{C}
\frac{1}{\sqrt{2\pi}}
e^{-(x^2+\lambda^2)/2}
\cosh(\lambda x),
\]
where
\[
q(x)=(1-\alpha x)^2+1,
\qquad
C=\alpha^2(\lambda^2+1)+2,
\]
with
\[
\alpha\in\mathbb R,
\qquad
\lambda\ge0.
\]
This is the NTPN density introduced in the 2026 source.

For every real Rényi order
\[
\gamma>0,
\qquad
\gamma\ne1,
\]
the entropy exists and has the exact representation
\[
\boxed{
H_\gamma
=
\frac{1}{1-\gamma}
\log\!\left[
C^{-\gamma}(2\pi)^{-\gamma/2}
e^{-\gamma\lambda^2/2}
\sqrt{\frac{2\pi}{\gamma}}\,
\mathbb E\!\left\{
q(Z_\gamma)^\gamma
\cosh(\lambda Z_\gamma)^\gamma
\right\}
\right],
}
\]
where
\[
Z_\gamma\sim N(0,1/\gamma).
\]

The finite-sum expression printed as Eq. (3.4) in the source does **not** cover all real
\[
\gamma>0,\qquad\gamma\ne1.
\]
Its derivation uses two finite expansions:
\[
q(x)^\gamma
=
(2-2\alpha x+\alpha^2x^2)^\gamma
\]
is expanded by a finite multinomial sum, and
\[
\cosh(\lambda x)^\gamma
=
2^{-\gamma}(e^{\lambda x}+e^{-\lambda x})^\gamma
\]
is expanded by a finite binomial sum. Those finite identities require a nonnegative integer exponent. For noninteger Rényi order, their upper limits cannot be interpreted as the claimed finite sums.

The failure is a domain error in the closed-form theorem, not a failure of Rényi entropy itself. In fact,
\[
\int_{\mathbb R} f(x;\alpha,\lambda)^\gamma\,dx<\infty
\]
for every real \(\gamma>0\).

A decisive benchmark is the standard-normal submodel
\[
\alpha=0,\qquad\lambda=0.
\]
Then
\[
f(x)=\phi(x),
\]
and the exact real-order Rényi entropy is
\[
\boxed{
H_\gamma
=
\frac12\log(2\pi)
+
\frac{\log\gamma}{2(\gamma-1)}.
}
\]
For example,
\[
H_{1/2}=1.612085713764618051\ldots,
\]
which is finite and unambiguous, while the finite sums in Eq. (3.4) have noninteger upper limit and therefore do not instantiate at \(\gamma=1/2\).

The source's contour plot uses \(\gamma=2\), an integer order. This correction therefore does not invalidate that particular plotted order; it corrects the theorem's stated domain and supplies a valid representation for all positive real orders other than one.

## Assumptions and scope
The NTPN parameters satisfy
\[
\alpha\in\mathbb R,\qquad\lambda\ge0.
\]
The Rényi order satisfies
\[
\gamma>0,\qquad\gamma\ne1.
\]

The finding distinguishes the existence of the entropy from the validity of a finite algebraic expansion. The entropy exists throughout the stated real-order domain. The finite Hermite-polynomial expression obtained through finite multinomial and binomial expansions is justified only at positive integer orders for which those expansions are finite.

No claim is made here about the Shannon limit
\[
\gamma\to1.
\]
No other moment, likelihood, reliability, or data-fitting result of the NTPN source is reassessed.

## Proof
By definition,
\[
H_\gamma
=
\frac{1}{1-\gamma}
\log\!\left(
\int_{\mathbb R}f(x;\alpha,\lambda)^\gamma\,dx
\right).
\]
Substituting the NTPN density gives
\[
\int_{\mathbb R}f(x;\alpha,\lambda)^\gamma\,dx
=
C^{-\gamma}(2\pi)^{-\gamma/2}e^{-\gamma\lambda^2/2}
\int_{\mathbb R}
q(x)^\gamma
e^{-\gamma x^2/2}
\cosh(\lambda x)^\gamma
\,dx.
\]

Let
\[
Z_\gamma\sim N(0,1/\gamma).
\]
Its density is
\[
\sqrt{\frac{\gamma}{2\pi}}e^{-\gamma x^2/2}.
\]
Therefore the remaining integral is exactly
\[
\sqrt{\frac{2\pi}{\gamma}}\,
\mathbb E\!\left\{
q(Z_\gamma)^\gamma
\cosh(\lambda Z_\gamma)^\gamma
\right\},
\]
which proves the displayed all-real-order representation.

It remains to verify finiteness. There are constants \(A,B>0\), depending on the fixed model parameters and on \(\gamma\), such that
\[
q(x)^\gamma\le A(1+|x|)^{2\gamma}
\]
and
\[
\cosh(\lambda x)^\gamma\le e^{\gamma\lambda|x|}.
\]
Hence the integrand is bounded by a constant multiple of
\[
(1+|x|)^{2\gamma}
\exp\!\left(
-\frac{\gamma x^2}{2}
+
\gamma\lambda|x|
\right).
\]
Completing the square shows that this function is integrable over \(\mathbb R\). Thus the Rényi integral is finite for every real \(\gamma>0\).

For the standard-normal submodel, \(q(x)=2\), \(C=2\), and \(\lambda=0\). Direct Gaussian integration gives
\[
\int_{\mathbb R}\phi(x)^\gamma\,dx
=
(2\pi)^{(1-\gamma)/2}\gamma^{-1/2},
\]
hence
\[
H_\gamma
=
\frac12\log(2\pi)
+
\frac{\log\gamma}{2(\gamma-1)}.
\]

The source's proof instead applies a finite multinomial theorem to \(q(x)^\gamma\) and a finite binomial theorem to \(\cosh(\lambda x)^\gamma\). For nonnegative integer \(\gamma\), these are ordinary finite polynomial expansions. For noninteger \(\gamma\), the corresponding generalized binomial expansions are infinite series rather than the finite sums displayed in Eq. (3.4). Therefore the printed finite-sum derivation cannot establish its stated all-real-order theorem.

## Verification
The accompanying checker evaluates the corrected integral in two independent ways for noninteger orders
\[
\gamma=\frac12,\qquad
\gamma=\frac32,\qquad
\gamma=2.3.
\]
First it directly integrates \(f^\gamma\). Second it evaluates the Gaussian-expectation representation above. The two calculations agree to high precision for
\[
\alpha=0.7,\qquad\lambda=1.2.
\]

The checker also evaluates the standard-normal submodel at
\[
\gamma=\frac12
\quad\text{and}\quad
\gamma=\frac32
\]
and verifies agreement with the closed formula
\[
\frac12\log(2\pi)+\frac{\log\gamma}{2(\gamma-1)}.
\]

These computations are reproducibility checks only. The domain correction follows from the algebraic distinction between finite integer-power expansions and noninteger powers, while entropy existence follows from the Gaussian domination argument.

## Relationship to prior work
Elbarougy, Das, Hazarika, and Eliwa state Theorem 3.3 for every
\[
\gamma>0,\qquad\gamma\ne1,
\]
then derive Eq. (3.4) using finite multinomial and binomial sums with upper limit \(\gamma\). Their subsequent contour uses \(\gamma=2\), which is an integer and therefore does not expose the domain mismatch.

Related skew and bimodal distribution literature treats real-order Rényi entropy without this finite-sum shortcut. In particular, recent bimodal skew-symmetric work retains a one-dimensional entropy integral for arbitrary positive order, while other generated-distribution work uses an infinite generalized-binomial series when the Rényi order is noninteger. Those approaches support the distinction made here between integer-order finite expansions and the full real-order definition, but they do not state the NTPN correction.

Focused searches using the NTPN acronym, exact DOI, Rényi-order terminology, multinomial and binomial aliases, and correction terminology did not locate a corrigendum or a published NTPN real-order correction.

## Limitations
The corrected expectation representation is exact but generally requires numerical quadrature for noninteger \(\gamma\); it is not claimed to be a finite elementary closed form.

The finding does not assess whether every algebraic coefficient in Eq. (3.4) is correct for positive integer orders. Its claim is narrower: the finite derivation cannot support the theorem's stated noninteger orders.

The source was inspected in full at the Rényi theorem and proof. No independent audit has been performed.

## References
1. R. Elbarougy, J. Das, P. J. Hazarika, and M. S. Eliwa, “The bimodal two-piece skew-normal distribution: Mathematical theory, reliability aging measures, and simulation-oriented decision analysis,” AIMS Mathematics 11 (2026), 511–542. DOI: 10.3934/math.2026022.
2. G. Alomair, H. S. Salinas, H. S. Bakouch, I. E. Okorie, and O. Albalawi, “Advanced Bimodal Skew-Symmetric Distributions: Methodology and Application to Cancer Cell Protein Data,” Symmetry 16 (2024), 985. DOI: 10.3390/sym16080985.
3. F. Merovci, M. A. Khaleel, N. A. Ibrahim, and M. Shitan, “The Truncated Cauchy Power Family of Distributions with Inference and Applications,” Entropy 22 (2020), 346. DOI: 10.3390/e22030346.
