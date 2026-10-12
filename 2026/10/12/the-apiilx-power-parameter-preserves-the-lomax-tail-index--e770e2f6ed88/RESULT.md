# The APIILx power parameter preserves the Lomax tail index
## Finding
For the alpha power type-II Lomax (APIILx) distribution with parameters
\[
\alpha>0,\qquad \theta>0,\qquad \lambda>0,
\]
set
\[
v(x)=\left(\frac{\lambda}{\lambda+x}\right)^\theta.
\]
Its published survival function can be written
\[
S(x)=\frac{2^\alpha-(2-v(x))^\alpha}{2^\alpha-1}.
\]
As \(x\to\infty\),
\[
S(x)=C_\alpha v(x)
\left[1-\frac{\alpha-1}{4}v(x)+O(v(x)^2)\right],
\qquad
C_\alpha=\frac{\alpha2^{\alpha-1}}{2^\alpha-1}.
\]
Therefore
\[
S(x)\sim C_\alpha\lambda^\theta x^{-\theta},
\qquad
f(x)\sim C_\alpha\theta\lambda^\theta x^{-\theta-1},
\qquad
h(x)\sim\frac{\theta}{x}.
\]
The alpha-power parameter changes the multiplicative tail constant but does not change the Lomax tail index \(\theta\).

This gives the exact positive-moment domain:
\[
\boxed{\mathbb E[X^q]<\infty\quad\Longleftrightarrow\quad 0<q<\theta.}
\]
In particular,
\[
\mathbb E[X]<\infty\quad\Longleftrightarrow\quad\theta>1,
\]
and
\[
\operatorname{Var}(X)<\infty\quad\Longleftrightarrow\quad\theta>2.
\]
At the critical order,
\[
\mathbb E\!\left[X^\theta\mathbf 1_{\{X\le R\}}\right]
\sim
\theta C_\alpha\lambda^\theta\log R.
\]
For \(q>\theta\), the truncated moment grows polynomially:
\[
\mathbb E\!\left[X^q\mathbf 1_{\{X\le R\}}\right]
\sim
\frac{\theta C_\alpha\lambda^\theta}{q-\theta}R^{q-\theta}.
\]

Finally,
\[
\mathbb E[e^{tX}]=\infty
\qquad\text{for every }t>0.
\]
Thus the distribution has no ordinary moment-generating function that is finite on an open interval around zero. The exponentially damped integral obtained after writing \(r=-t>0\) belongs to the Laplace-transform side \(t<0\).

These statements supply the missing existence conditions for the moment formulas in the 2026 source. Its printed \(r\)-th raw-moment expression is a genuine moment only for \(r<\theta\); its first-moment formula requires \(\theta>1\), and its second-moment and variance formulas require \(\theta>2\).

## Assumptions and scope
The model is exactly the APIILx law defined by Kalt et al. with
\[
F(x)=\frac{[2-v(x)]^\alpha-1}{2^\alpha-1},
\qquad x>0,
\]
where \(v(x)=(\lambda/(\lambda+x))^\theta\).

The moment theorem is stated for real \(q>0\), which is slightly broader than the source's integer-order binomial calculation. Near \(x=0\), the density is finite, so positive-moment existence is controlled entirely by the right tail.

The conclusion about the moment-generating function uses the standard definition requiring finiteness in some open neighborhood of zero. The Laplace transform \(\mathbb E[e^{-sX}]\) remains finite for every \(s\ge0\).

## Proof
Because \(v(x)\to0\), expand
\[
(2-v)^\alpha
=2^\alpha\left(1-\frac v2\right)^\alpha
=2^\alpha\left[1-\frac{\alpha v}{2}
+\frac{\alpha(\alpha-1)v^2}{8}+O(v^3)\right].
\]
Subtracting from \(2^\alpha\) and dividing by \(2^\alpha-1\) gives
\[
S(x)
=\frac{\alpha2^{\alpha-1}}{2^\alpha-1}v(x)
\left[1-\frac{\alpha-1}{4}v(x)+O(v(x)^2)\right].
\]
Since
\[
v(x)=\lambda^\theta(\lambda+x)^{-\theta}
\sim\lambda^\theta x^{-\theta},
\]
the survival asymptotic follows.

From the published density,
\[
f(x)=\frac{\alpha\theta\lambda^\theta}{2^\alpha-1}
[2-v(x)]^{\alpha-1}(\lambda+x)^{-\theta-1},
\]
and \([2-v(x)]^{\alpha-1}\to2^{\alpha-1}\), yielding the density asymptotic. Dividing gives \(h(x)\sim\theta/x\).

For \(q>0\), the tail identity
\[
\mathbb E[X^q]
=q\int_0^\infty x^{q-1}S(x)\,dx
\]
applies whenever the integral is finite, and its divergence also detects an infinite positive moment. Since \(S(x)\) is asymptotic to a positive constant times \(x^{-\theta}\), the tail integral behaves like
\[
\int^\infty x^{q-\theta-1}\,dx,
\]
which converges exactly when \(q<\theta\). This proves the full moment domain.

For the truncated moment,
\[
\mathbb E[X^q\mathbf 1_{\{X\le R\}}]
=q\int_0^R x^{q-1}S(x)\,dx-R^qS(R).
\]
Substituting \(S(x)\sim C_\alpha\lambda^\theta x^{-\theta}\) gives the logarithmic boundary law at \(q=\theta\) and the stated polynomial coefficient for \(q>\theta\).

Finally, the density asymptotic implies that for sufficiently large \(x\),
\[
f(x)\ge c x^{-\theta-1}
\]
for some \(c>0\). Hence for every \(t>0\),
\[
\int_0^\infty e^{tx}f(x)\,dx
\ge
c\int_M^\infty e^{tx}x^{-\theta-1}\,dx
=\infty.
\]
So no ordinary MGF exists around zero. For \(t<0\), \(0<e^{tX}\le1\), so the transform is finite.

## Verification
The bundled checker evaluates the exact survival and density formulas for several parameter triples. It verifies convergence of
\[
x^\theta S(x)
\]
to \(C_\alpha\lambda^\theta\), of \(x h(x)\) to \(\theta\), and of the scaled critical truncated moment to its logarithmic coefficient.

It also evaluates truncated positive-exponential transforms and confirms rapid growth as the truncation point increases. These calculations are consistency checks only. The infinite-domain conclusions are proved by the analytic tail comparison above.

## Relationship to prior work
Kalt et al. derive an incomplete-beta formula for the \(r\)-th raw moment, then display the first moment, second moment, variance, and a quantity labeled as the MGF. In the moment derivation, the incomplete-beta integral has first parameter \(1-(r-i)/\theta\); the \(i=0\) term is an ordinary convergent beta integral only when \(r<\theta\). The source does not state this as the moment-existence domain.

In its MGF section, the source defines \(M_X(t)=\mathbb E[e^{tX}]\), sets \(r=-t\), and then evaluates an exponentially damped integral involving \(e^{-rx}\). That real integral is convergent for \(r>0\), corresponding to \(t<0\), whereas the positive-\(t\) transform diverges because of the power-law tail.

Mohsin and Kalt's 2025 APII-G paper introduces the generator and studies exponential and Weibull baselines. Those light-tailed examples do not establish the heavy-tail phase for the Lomax specialization. Classical Lomax theory has moment cutoff at its tail-shape parameter; the present result proves that the APII transformation preserves that cutoff exactly and supplies the transformed tail constant and critical divergence rates.

Focused searches for the APIILx model together with tail index, regular variation, moment existence, MGF divergence, and correction terms did not locate a published theorem or corrigendum covering these statements.

## Limitations
The finding concerns positive raw moments and exponential transforms; it does not classify negative moments or complex transforms.

The source's algebraic incomplete-beta expressions may admit analytic continuations outside the convergent-integral region, but such analytic continuations are not equal to divergent probabilistic moments. Likewise, an incomplete-gamma formula on the Laplace side is not an ordinary MGF on a neighborhood of zero.

The result does not invalidate likelihood-based estimation merely because moments fail in part of the parameter space. It corrects the interpretation and domain of the model's claimed moment and MGF properties.

## References
1. H. G. Kalt, A. Ben Ghorbal, I. Elbatal, A. Z. Afify, and H. A. Mahran, “A new alpha power type-II Lomax distribution with applications to radiation and materials sciences,” AIMS Mathematics 11 (2026), 8134–8167. DOI: 10.3934/math.2026334.
2. L. A. J. Mohsin and H. G. Kalt, “Alpha Power Type II-G Family: Adding a Power Parameter of Distributions,” Mathematical Modelling of Engineering Problems 12 (2025), 1031–1042. DOI: 10.18280/mmep.120330.
3. K. S. Lomax, “Business failures: Another example of the analysis of failure data,” Journal of the American Statistical Association 49 (1954), 847–852. DOI: 10.1080/01621459.1954.10501239.
