# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The explicit parameter choice
\[
a=(2-\sqrt6)/8,\qquad b=1/8
\]
satisfies the \(a\le0\) boundary equation in Proposition 4.3 exactly:
\[
(-a+2b)^2+2(b-1/4)^2=1/8.
\]
Hence the corresponding degree-four Hermite function is an extremal ray generator. Expanding its polynomial factor with \(X=4\pi x^2\) gives
\[
Q(X)=X^2+(2\sqrt6-10)X+15-2\sqrt6,
\]
whose discriminant is \(32(2-\sqrt6)<0\); with positive leading coefficient this proves strict positivity on the real line.

The Hermite Fourier rule from the source changes \(a\) to \(-a\). The transformed polynomial simplifies exactly to
\[
R(X)=(X-(1+\sqrt6))^2,
\]
so the Fourier transform is nonnegative and has only two distinct real zeros. The original function and its Fourier transform therefore lie in the cone, and Proposition 4.3 plus Fourier invariance gives extremality of both factors used in the two counterexamples.

For the product, \(\widehat{F^2}=H*H\). Since \(H\ge0\) and its zero set is finite, the convolution integrand is positive almost everywhere for every fixed output point, hence \(H*H>0\) everywhere. Thus both \(F^2\) and its Fourier transform are strictly positive. Lemma 4.2 of the source states that an extremal positive-positive-definite Hermite function of positive degree must have real zeros in at least one of its spatial or Fourier polynomial factors. Therefore \(F^2\) is not extremal.

Fourier transformation is a linear bijection of this even Schwartz subcone and preserves extremal rays. Since \(H*H=\widehat{F^2}\), nonextremality of \(F^2\) immediately implies nonextremality of \(H*H\). This also checks that the convolution counterexample is well defined and remains inside the cone.

The symbolic verification artifact independently checks the boundary identity and factorizations. It also derives the polynomial factor of \(\widehat{F^2}\) by differentiating the Fourier transform of \(e^{-2\pi x^2}\) and verifies exactly that this polynomial has no real roots.

## Originality

PASS, to the best of our knowledge.

The 2009 Jaming--Matolcsi--Révész paper was inspected at Lemma 4.2, Proposition 4.3, Corollary 4.4 and the conclusion. Its Question 1 explicitly asks whether products of two extremals and convolutions of two extremals are extremal and says that the authors had no proposed answer. The same paper proves only type-restricted positive results: products for degree-four time-type extremals and convolutions for frequency-type extremals.

Searches covered the exact Question 1 wording, the title and DOI of the source, "positive positive definite" and "doubly positive" terminology, extremal-ray preservation under product/convolution, Hermite extremals, and the explicit algebraic parameters appearing above. No published solution or equivalent counterexample was located.

The 2011 Hinrichs--Vybíral paper was inspected around its discussion of positive-positive-definite functions. It explicitly records closure of the cone under products and under well-defined convolutions and cites Jaming--Matolcsi--Révész, but its conjectures concern matrix inequalities/Bochner-type characterizations rather than preservation of extremal rays. Later accessible citing literature located in 2017 and 2022 studies integral comparison extremal quantities, not the product/convolution extremal-ray question.

The main residual originality risk is unusually important here: the counterexample is a short consequence of results already adjacent to the open question in the 2009 source. It may therefore have been noticed informally, in correspondence, teaching notes, or a poorly indexed remark without appearing in the searches. No specific source was found that gives concrete evidence of such prior coverage.

## Value

PASS.

The result gives explicit negative answers to both parts of a published two-part open question. It also identifies the structural reason that the source's type restrictions in Corollary 4.4 cannot be dropped: strict positivity on one side, together with finite-zero Hermite structure on the other, makes the opposite operation land in the nonextremal interior of the finite-dimensional Hermite cone. The argument yields continuous families of counterexamples rather than a single accidental example.

## Limitations

- The result does not classify pairs whose product or convolution remains extremal.
- The positive type-restricted families in Corollary 4.4 are not contradicted.
- The counterexample mechanism is one-dimensional and Hermite-specific.
- The separate strict-positive-extremal problem from the source paper remains open here.
- An unpublished or poorly indexed prior observation remains a residual originality risk because the proof is short and uses ingredients from the source itself.
- Independent audit has not been performed.
