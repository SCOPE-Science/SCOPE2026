# Strict singular-value ordering by relative squeezing phase in Fock cross products

## Finding

Let \(\mathcal F^2\) be the normalized one-variable Bargmann–Fock Hilbert space, with inner product from \(\pi^{-1}e^{-|z|^2}\,dA(z)\). Fix \(0<r<1\) and nonzero complex numbers \(t,s\) satisfying
\[
2|t|<1-r^2,\qquad 2|s|<1-r^2.
\]
Define \(W_t f(z)=e^{tz^2}f(rz)\) and \(T_{t,s}=W_tW_s^*\). Put
\[
\sigma=1-4|s|^2,\quad
b=\frac{r^4}{\sigma},\quad
 a=t+\frac{r^4s}{\sigma},\quad
p=1+b^2-4|a|^2,\quad
 d=\frac{p+\sqrt{p^2-4b^2}}2.
\]
Then \(0<b<d\le1\), \(T_{t,s}\) is trace class, and **every** decreasing singular value, indexed from zero, is exactly
\[
\boxed{s_n(T_{t,s})=\sigma^{-1/4}d^{-1/4}\left(\frac bd\right)^{n/2},\qquad n=0,1,2,\ldots .}
\]
In particular, for every real \(p_0>0\),
\[
\|T_{t,s}\|_{\mathcal S_{p_0}}
=\sigma^{-1/4}d^{-1/4}
\left(1-(b/d)^{p_0/2}\right)^{-1/p_0}.
\]
For fixed \(r\), \(|t|>0\), and \(|s|>0\) in this range, **each singular value strictly increases with** \(\cos(\arg t-\arg s)\). Consequently, aligning the two quadratic phases uniquely maximizes each singular value, every finite Ky Fan sum, and every Schatten quasi-norm; opposite phases uniquely minimize them. Uniqueness is modulo a common phase and integer multiples of \(2\pi\) in the relative angle.

The squared Hilbert–Schmidt norm also has the symmetric expression
\[
\|T_{t,s}\|_{\mathcal S_2}^2=
\left[(1-4|t|^2)(1-4|s|^2)-2r^4+r^8-8r^4\operatorname{Re}(t\overline{s})\right]^{-1/2}.
\]

## Assumptions and scope

The scalars \(t,s\) may have arbitrary complex phases, but are nonzero for the strict phase assertion. The contraction \(r\) is real and strictly between zero and one. The weighted composition operators act on holomorphic functions, and the adjoint is the Hilbert-space adjoint. The index \(n\) ranges over every nonnegative integer. The assumptions are strict subcritical inequalities, not endpoint statements; no extension to critical squeezing, unequal affine slopes, linear translations, or higher-dimensional Fock spaces is claimed.

## Proof

**1. Both factors are Hilbert–Schmidt.** The normalized monomials \(e_n(z)=z^n/\sqrt{n!}\) are an orthonormal basis. Parseval, monotone convergence, and a real two-dimensional Gaussian integral give
\[
\begin{aligned}
\|W_t\|_{\mathcal S_2}^2
&=\int_{\mathbb C}|e^{tz^2}|^2e^{r^2|z|^2-|z|^2}\,\frac{dA(z)}\pi\\
&=\frac1{\sqrt{(1-r^2)^2-4|t|^2}}<\infty.
\end{aligned}
\]
The analogous formula holds for \(W_s\). Hence their product \(T_{t,s}\) is trace class and in particular Hilbert–Schmidt.

**2. Positive Gram-kernel reduction.** The reproducing kernel is \(K_w(z)=e^{z\overline w}\). Thus the integral kernel of \(T_{t,s}\) is
\[
H(z,\overline w)=\exp\left(tz^2+\overline{s}\,\overline w^{\,2}+r^2z\overline w\right).
\]
For complex \(u,v\) and \(|s|<1/2\), direct completion of the square establishes
\[
\int_{\mathbb C}
 e^{sw^2+\overline s\,\overline w^{\,2}+uw+v\overline w}
\,\frac{e^{-|w|^2}dA(w)}\pi
=\sigma^{-1/2}
\exp\left(\frac{\overline s\,u^2+s v^2+uv}{\sigma}\right).
\]
Applying this identity to \(Q=T_{t,s}T_{t,s}^*\) yields the positive trace-class kernel
\[
Q(z,\overline w)=\sigma^{-1/2}
  \exp\left(a z^2+\overline a\,\overline w^{\,2}+b z\overline w\right).
\]
Here \(b>0\). Moreover,
\[
2|a|+b\le 2|t|+\frac{r^4(1+2|s|)}{1-4|s|^2}
=2|t|+\frac{r^4}{1-2|s|}<2|t|+r^2<1.
\]
This verifies all positivity and integrability conditions needed below, not just formal Gaussian manipulation.

**3. Exact spectral lemma for the positive kernel.** More generally, consider \(Q_{a,b,c}\) with kernel \(c\exp(a z^2+\overline a\,\overline w^{\,2}+b z\overline w)\), where \(c>0\), \(b>0\), and \(2|a|+b<1\). Define \(p=1+b^2-4|a|^2\) and \(d=(p+\sqrt{p^2-4b^2})/2\). Then \(0<b<d\le1\), and \(d\) is the larger root of
\[
d^2-(1+b^2-4|a|^2)d+b^2=0.
\]
Put \(h=ad/(d-b^2)\) and \(q=b/d\). The root identity implies both
\[
d=1-4h\overline a,\qquad h=a+\frac{h b^2}{d}.
\]
Also \(|h|<1/2\): indeed \(4|a|^2d^2=(1-d)(d-b^2)d<(d-b^2)^2\), with the strict inequality equivalent to \(d>b\). Thus \(h\) belongs to the Fock Gaussian integrability range. Set
\[
k=-\frac{\overline a}{d(1-q^2)},\qquad
F_\xi(z)=\exp(hz^2+\xi z+k\xi^2).
\]
For each \(\xi\in\mathbb C\), this is a Fock-space vector, locally analytically dependent on \(\xi\). The same completed-square integral shows
\[
Q_{a,b,c}F_\xi=\frac c{\sqrt d}\,F_{q\xi}.
\]
Writing \(F_\xi=\sum_{n\ge0}\xi^n f_n\) gives nonzero eigenvectors \(f_n\), each with eigenvalue \(c d^{-1/2}q^n\); nonzeroness follows from the leading polynomial term \(z^ne^{hz^2}/n!\). Since \(Q_{a,b,c}\) is positive self-adjoint, these vectors with distinct eigenvalues are mutually orthogonal.

To exclude missing positive eigenvalues, calculate its full trace by the diagonal-kernel integral:
\[
\operatorname{Tr}Q_{a,b,c}=\frac c{\sqrt{(1-b)^2-4|a|^2}}.
\]
The root identity is equivalent to
\[
\frac{(d-b)^2}{d}=(1-b)^2-4|a|^2.
\]
Consequently,
\[
\sum_{n\ge0}\frac c{\sqrt d}q^n
=\frac{c\sqrt d}{d-b}
=\operatorname{Tr}Q_{a,b,c}.
\]
Positivity and trace-class additivity force zero on the orthogonal complement. Hence this is the **complete** nonzero spectrum, with each listed eigenvalue simple.

Applying the lemma with \(c=\sigma^{-1/2}\) proves the singular-value formula as the positive square roots of the eigenvalues of \(T_{t,s}T_{t,s}^*\). Geometric summation gives all positive-order Schatten quasi-norms and Ky Fan sums. Expanding the diagonal trace in the original parameters gives the displayed Hilbert–Schmidt expression.

**4. Strict phase ordering.** At fixed positive magnitudes \(u=|t|\), \(v=|s|\),
\[
|a|^2=u^2+\left(\frac{r^4v}{\sigma}\right)^2
 +\frac{2r^4uv}{\sigma}\cos(\arg t-\arg s).
\]
Thus \(|a|^2\) strictly increases with the cosine. The function \(d=(p+\sqrt{p^2-4b^2})/2\) strictly increases with \(p\) for \(p>2b\), while \(p=1+b^2-4|a|^2\) decreases with \(|a|^2\). Therefore \(d\) strictly decreases with the cosine. Every individual singular value is \(\sigma^{-1/4}b^{n/2}d^{-n/2-1/4}\), and therefore strictly increases. This proves the unique alignment and antialignment extrema, together with every stated norm consequence.

## Verification

The accompanying `check_spectrum.py` constructs finite Laurent–Fock monomial matrices from the exact coefficients of the weighted compositions, compares their cross-product singular values with the closed formula, verifies algebraic trace identities, and checks strict phase ordering for several distinct complex parameter families. Execute `python check_spectrum.py` after installing the version specified in `requirements.txt`. Finite truncations and floating-point computations do not prove the infinite-dimensional assertions, which follow from the Gaussian integral and trace-exhaustion argument above. No computer algebra or numerical continuation is required for the proof.

## Relationship to prior work

Tian (2026) treats boundedness, compactness, invertibility, and isometry of Fock weighted-composition cross products, not the full singular-value-by-singular-value phase order proved here. Sang and Zhao (2026) characterize general Gaussian integral operators and calculate the Hilbert–Schmidt invariant, but their inspected Schatten section does not list the complete spectrum of a general two-squeeze cross product or the strict relative-phase comparison. Dong and Zhu (2025) evaluate singular values for their constrained canonical Gaussian kernel, whose two quadratic coefficients are linked by a sign relation; it is not the independent-phase cross-product family above. General oscillator-semigroup theory provides broader Gaussian-operator background, and an implicit equivalent in that literature remains a priority risk.

## Limitations

Only a real common contraction slope, homogeneous quadratic weights, and strict subcritical parameters are covered. Nothing is asserted about singular vectors beyond the explicit eigenfamily of the positive Gram operator, and no assertion is made about the spectrum of the generally nonnormal product itself. The phase result compares products at fixed two squeezing magnitudes and fixed contraction. Publication priority has not been independently established; the published literature may encode a related Gaussian normal form in different notation.

## References

- Xianchi Tian, *Weighted composition operators on the Fock space*, arXiv:2610.29786v1, first posted 2026-10-21, Sections 2–4. https://arxiv.org/abs/2610.29786
- Yuanqi Sang and Liankuo Zhao, *Gaussian Integral Operator between Fock Spaces* (HTML title: *Boundedness and Compactness of Gaussian Integral Operators between Fock Spaces*), arXiv:2610.28279v1, first posted 2026-10-20, Theorems 1.1–1.4 and Section 5. https://arxiv.org/abs/2610.28279
- Xingtang Dong and Kehe Zhu, *Canonical integral operators on the Fock space II*, arXiv:2509.16672v1, first posted 2025-09-20, Theorem A and Section 4. https://arxiv.org/abs/2509.16672
- R. Howe, *The oscillator semigroup*, Proc. Sympos. Pure Math. 48 (1988), 61–132 (general Gaussian-operator background; no claim of exhaustive full-text comparison).
