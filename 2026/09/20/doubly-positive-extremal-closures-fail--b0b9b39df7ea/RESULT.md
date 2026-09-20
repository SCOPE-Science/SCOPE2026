# Product and convolution can destroy extremality in the doubly-positive cone

Let \(\Omega_+^1\) denote the cone of continuous functions \(f:\mathbb R\to\mathbb R\) that are nonnegative and positive definite. For the Fourier convention
\[
\widehat f(\xi)=\int_{\mathbb R}f(x)e^{-2\pi i x\xi}\,dx,
\]
every Schwartz function in \(\Omega_+^1\) has \(f\ge0\) and \(\widehat f\ge0\).

Jaming, Matolcsi and Révész asked in Question 1 of their 2009 paper whether the product of two extremal rays of \(\Omega_+^1\) must again be extremal, and likewise for convolution when it is defined. Both answers are negative.

## Theorem

Put
\[
Q(X)=X^2+(2\sqrt6-10)X+15-2\sqrt6,
\qquad
R(X)=\bigl(X-(1+\sqrt6)\bigr)^2,
\]
and define
\[
F(x)=Q(4\pi x^2)e^{-\pi x^2},
\qquad
H(x)=R(4\pi x^2)e^{-\pi x^2}.
\]
Then:

1. \(F,H\in\Omega_+^1\), both \(F\) and \(H\) generate extremal rays, and \(H=\widehat F\).
2. The product \(F^2\) belongs to \(\Omega_+^1\) but is not extremal.
3. The convolution \(H*H\) belongs to \(\Omega_+^1\) but is not extremal.

Consequently, neither pointwise multiplication nor convolution preserves extremal rays of the positive-positive-definite cone, even for one-dimensional Schwartz Hermite functions and even when the two factors are identical.

## Proof

Jaming--Matolcsi--Révész write their degree-four Hermite family as
\[
f_{a,b}(x)=\bigl(H_0(x)+2aH_2(x)+bH_4(x)\bigr)e^{-\pi x^2},
\]
with
\[
H_0=1,\qquad H_2=4\pi x^2-1,\qquad
H_4=(4\pi x^2)^2-6(4\pi x^2)+3.
\]
Their Proposition 4.3 says that, for \(a\le0\), \(f_{a,b}\) is positive positive definite precisely in the region
\[
(-a+2b)^2+2\left(b-\frac14\right)^2\le\frac18,
\]
and it is extremal on the boundary.

Choose
\[
a=\frac{2-\sqrt6}{8},\qquad b=\frac18.
\]
Then \(a<0\) and
\[
(-a+2b)^2+2\left(b-\frac14\right)^2=\frac18,
\]
so \(f_{a,b}\) is extremal. With \(X=4\pi x^2\), eight times its polynomial factor is
\[
Q(X)=X^2+(2\sqrt6-10)X+15-2\sqrt6.
\]
Its discriminant is
\[
32(2-\sqrt6)<0,
\]
hence \(Q(X)>0\) for every real \(X\). Thus \(F=8f_{a,b}\) is strictly positive.

Fourier transformation changes \(a\) to \(-a\) in this Hermite family. Direct substitution gives
\[
8\bigl(1-2a+3b-2(-a+3b)X+bX^2\bigr)
=\bigl(X-(1+\sqrt6)\bigr)^2.
\]
Hence
\[
\widehat F(\xi)
=\bigl(4\pi \xi^2-(1+\sqrt6)\bigr)^2e^{-\pi\xi^2}
=H(\xi)\ge0.
\]
The Fourier transform is a linear cone automorphism on these even Schwartz functions, so \(H\) is extremal as well.

Now \(F^2>0\). Also
\[
\widehat{F^2}=H*H.
\]
The nonnegative function \(H\) vanishes only at the two points
\[
\xi=\pm\sqrt{\frac{1+\sqrt6}{4\pi}}.
\]
For each fixed \(\xi\), the integrand \(H(\eta)H(\xi-\eta)\) is therefore positive except at finitely many \(\eta\), so
\[
(H*H)(\xi)>0\qquad(\xi\in\mathbb R).
\]
Thus \(F^2\) and its Fourier transform are both strictly positive.

But \(F^2\) is a Hermite function of positive polynomial degree:
\[
F(x)^2=Q(4\pi x^2)^2e^{-2\pi x^2}.
\]
Lemma 4.2 of Jaming--Matolcsi--Révész gives a necessary condition for such a Hermite function to generate an extremal ray: at least one of its polynomial factors in the spatial or Fourier representation must have real zeros (indeed at least four, counted with multiplicity in their formulation). Here neither has any real zero, because \(F^2>0\) and \(\widehat{F^2}>0\). Therefore \(F^2\) is not extremal.

Finally,
\[
H*H=\widehat{F^2}.
\]
If \(H*H\) were extremal, applying the inverse Fourier transform, which is again a linear automorphism of \(\Omega_+^1\) on these even Schwartz functions, would make \(F^2\) extremal. This contradiction proves that \(H*H\) is not extremal.

## A general Hermite mechanism

The counterexample is not isolated. If
\[
f(x)=P(x)e^{-\lambda\pi x^2}\in\Omega_+^1
\]
is a nonconstant Hermite function with \(f(x)>0\) on \(\mathbb R\), then \(\widehat f\) is a nonnegative polynomial times a Gaussian and therefore is positive away from finitely many points. Consequently \(\widehat{f^2}=\widehat f*\widehat f\) is strictly positive everywhere, while \(f^2>0\). Lemma 4.2 then implies that \(f^2\) is not extremal. Fourier duality gives the companion statement: if \(\widehat f>0\), then \(f*f\) is not extremal.

Thus the degree-four boundary arcs from Proposition 4.3 supply continuous families of product and convolution counterexamples, not merely the explicit pair above.

## Context

The source paper proves positive closure results in the opposite directions for special degree-four Hermite extremals: products of its "time type" examples are extremal, and convolutions of its "frequency type" examples are extremal (Corollary 4.4). Question 1 then asks whether product and convolution preserve extremality without those type restrictions. The construction above shows that the restrictions matter: a frequency-type extremal can lose extremality under self-product, and Fourier duality gives a time-type extremal whose self-convolution loses extremality.

A 2011 paper of Hinrichs and Vybíral records that the full positive-positive-definite cone is closed under products and, when defined, convolutions, and cites the extremal-ray paper, but addresses a different matrix/Bochner conjecture rather than extremal-ray preservation. Later work on nonnegative positive-definite functions found in the citation chain, including integral-extremal problems, likewise concerns different extremal quantities.

## Limitations

This result disproves universal preservation of extremality; it does not classify which pairs of extremals have extremal products or convolutions. In particular, the positive subclasses from Corollary 4.4 remain intact. The argument is one-dimensional and Hermite-specific as a counterexample mechanism, although a single one-dimensional counterexample is enough to answer the universal questions. It does not settle the source paper's separate question about the existence of non-Gaussian extremals for which both a function and its Fourier transform are strictly positive.

The literature search located no published answer to Question 1 or an equivalent explicit counterexample. Because the proof is a short consequence of ingredients already present in the 2009 paper, an unpublished observation or a poorly indexed remark remains a meaningful originality risk.

## Verification

`artifacts/verify_hermite_counterexample.py` checks the boundary identity, the exact spatial and Fourier polynomial factorizations, the negative spatial discriminant, and an independent symbolic Fourier-transform calculation for \(F^2\). With SymPy 1.14 it also verifies that the resulting Fourier polynomial for \(F^2\) has no real roots.

## References

1. P. Jaming, M. Matolcsi, S. Gy. Révész, *On the extremal rays of the cone of positive, positive definite functions*, Journal of Fourier Analysis and Applications 15 (2009), 561--582. DOI: https://doi.org/10.1007/s00041-008-9057-6 ; arXiv: https://arxiv.org/abs/0801.0941
2. A. Hinrichs, J. Vybíral, *On positive positive-definite functions and Bochner's Theorem*, Journal of Complexity 27 (2011), 264--272. DOI: https://doi.org/10.1016/j.jco.2011.01.002
3. A. Efimov, M. Gaál, Sz. Gy. Révész, *On integral estimates of nonnegative positive definite functions*, Bulletin of the Australian Mathematical Society 96 (2017), 117--125. DOI: https://doi.org/10.1017/S0004972717000119
4. M. Gaál, Sz. Gy. Révész, *Integral comparisons of nonnegative positive definite functions on LCA groups*, Mathematische Zeitschrift 302 (2022), 995--1024. DOI: https://doi.org/10.1007/s00209-022-03055-y
