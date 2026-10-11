# A one-over-root-two lower bound for the quantitative Baxter radius

## Finding

Let
\[
F\in\ell^2(\mathbb Z)
\]
have \(SU(2)\)-valued nonlinear Fourier transform
\[
(a_F,b_F),
\]
assume \(a_F\) is outer on
\[
\mathbb D^*,
\]
and write
\[
B=\|b_F\|_{A_1},
\]
where \(A_1\) is the Wiener algebra.

For every
\[
B<1,
\]
one has the explicit spectral-factor estimate
\[
\|a_F^{-1}\|_{A_1}
\le
(1-B^2)^{-2}.
\]

The March 2026 quantitative Baxter theorem proves, under
\[
B<\frac1{\sqrt2}-\varepsilon,
\]
that
\[
\|F\|_{\ell^1}
\lesssim
\frac1{\varepsilon}
\|b_F/a_F\|_{A_1}.
\]
The inverse estimate removes the remaining denominator:
\[
\|F\|_{\ell^1}
\lesssim
\frac{B}{\varepsilon(1-B^2)^2}.
\]

Consequently, if \(\tau\) denotes the largest radius in Question 3 of the October 2026 paper—so that, for every fixed \(\eta>0\), the conditions
\[
\|b_F\|_{A_1}<\tau-\eta
\]
and outerness of \(a_F\) imply a uniform \(\ell^1\)-bound depending only on \(\eta\)—then
\[
\frac1{\sqrt2}\le\tau\le1.
\]
The October paper records only the lower bound
\[
\tau\ge\frac1{\sqrt3}.
\]

## Assumptions and scope

The nonlinear Fourier transform is the \(SU(2)\) transform, so on the unit circle
\[
|a_F|^2+|b_F|^2=1.
\]

The function \(a_F\) is assumed outer on \(\mathbb D^*\), equivalently \(a_F^*\) is outer on \(\mathbb D\). The standard nonlinear-Fourier normalization makes the outer value at infinity positive.

The result does not determine the optimal radius \(\tau\). It proves only
\[
\tau\ge\frac1{\sqrt2}.
\]
Nor is the displayed inverse-Wiener constant asserted to be sharp.

## Proof

Put
\[
b=b_F,
\qquad
a=a_F,
\qquad
B=\|b\|_{A_1}<1.
\]
Let
\[
m=\widehat{|b|^2}(0)=\|b\|_2^2
\]
with normalized Haar measure on the unit circle, and set
\[
c=1-m.
\]
Since
\[
|a|^2=1-|b|^2,
\]
we may write
\[
|a|^2
=
c(1+h),
\qquad
h
=
-\frac{|b|^2-m}{1-m}.
\]

The Wiener algebra is a Banach algebra and reflection preserves its norm. Hence
\[
\||b|^2\|_{A_1}
\le
\|b\|_{A_1}^2
=
B^2.
\]
The zero Fourier coefficient of \(|b|^2\) is the nonnegative number \(m\). Removing that coefficient therefore gives the exact identity
\[
\||b|^2-m\|_{A_1}
=
\||b|^2\|_{A_1}-m.
\]
Consequently,
\[
\|h\|_{A_1}
\le
\frac{B^2-m}{1-m}.
\]
Because
\[
0\le m\le B^2<1,
\]
one has
\[
\frac{B^2-m}{1-m}
\le
B^2.
\]
Thus
\[
\|h\|_{A_1}\le B^2<1.
\]

The logarithmic power series therefore converges absolutely in \(A_1\):
\[
\log(1+h)
=
\sum_{j=1}^{\infty}
\frac{(-1)^{j+1}}{j}h^j.
\]
Since
\[
|a|^2=c(1+h),
\]
\[
\|\log|a|^2\|_{A_1}
\le
|\log c|
-
\log(1-\|h\|_{A_1}).
\]
Now
\[
c=1-m\ge1-B^2
\]
and
\[
1-\|h\|_{A_1}\ge1-B^2.
\]
Therefore
\[
\|\log|a|^2\|_{A_1}
\le
-2\log(1-B^2).
\]

Let
\[
u=\log|a|.
\]
Then
\[
\|u\|_{A_1}
\le
-\log(1-B^2).
\]
Because \(a^*\) is outer in the disk, with its positive value at zero, the boundary Fourier expansion of its logarithm is
\[
\log a^*
=
\widehat u(0)
+
2\sum_{n\ge1}\widehat u(n)z^n.
\]
The analytic Fourier projection is contractive on \(A_1\), so
\[
\|\log a^*\|_{A_1}
\le
2\|u\|_{A_1}
\le
-2\log(1-B^2).
\]
Reflection gives the same estimate for \(\log a\).

Exponentiating in the Banach algebra,
\[
a^{-1}
=
\exp(-\log a),
\]
and hence
\[
\|a^{-1}\|_{A_1}
\le
\exp(\|\log a\|_{A_1})
\le
(1-B^2)^{-2}.
\]

The March 2026 theorem gives, whenever
\[
B<\frac1{\sqrt2}-\varepsilon,
\]
\[
\|F\|_{\ell^1}
\lesssim
\frac1{\varepsilon}
\|b/a\|_{A_1}.
\]
By the Banach-algebra inequality,
\[
\|b/a\|_{A_1}
\le
B\|a^{-1}\|_{A_1}
\le
\frac{B}{(1-B^2)^2}.
\]
Thus
\[
\|F\|_{\ell^1}
\lesssim
\frac{B}{\varepsilon(1-B^2)^2}.
\]

Finally, fix
\[
\eta>0
\]
and assume
\[
B<\frac1{\sqrt2}-\eta.
\]
Taking
\[
\varepsilon=\eta
\]
in the preceding estimate gives a bound depending only on \(\eta\). Therefore the radius from the October 2026 open question satisfies
\[
\tau\ge\frac1{\sqrt2}.
\]
Its published counterexample still gives
\[
\tau\le1,
\]
which yields the stated bracket.

## Verification

The October 2026 primary paper was checked at the precise statements of its quantitative theorem and Question 3. It proves a denominator-free estimate only under
\[
\|b_F\|_{A_1}<\frac1{\sqrt3}-\varepsilon
\]
and explicitly records the bracket
\[
\frac1{\sqrt3}\le\tau\le1.
\]

The March 2026 primary paper was checked at its quantitative proposition. In the unweighted case it proves
\[
\|F\|_{\ell^1}
\lesssim
\frac1{\varepsilon}
\|b_F/a_F\|_{A_1}
\]
through the larger range
\[
\|b_F\|_{A_1}<\frac1{\sqrt2}-\varepsilon.
\]

The new step is the explicit Wiener inverse estimate for the outer spectral factor. Every inequality in that step is an exact Banach-algebra estimate or an absolutely convergent power-series estimate. No numerical experiment is used.

## Relationship to prior work

The March 2026 paper establishes the \(SU(2)\) analogue of Baxter's theorem and a quantitative estimate up to the natural
\[
\frac1{\sqrt2}
\]
threshold, but the right-hand side still contains
\[
\|b_F/a_F\|_{A_1}.
\]
It invokes Wiener's lemma qualitatively to know this ratio is finite; it does not bound that norm solely by \(\|b_F\|_{A_1}\).

The October 2026 paper asks explicitly for the largest radius on which \(\|b_F\|_{A_1}\) alone controls the potential. Its direct Wiener estimate reaches
\[
\frac1{\sqrt3},
\]
leading it to state
\[
\frac1{\sqrt3}\le\tau\le1.
\]

Results from symmetric quantum signal processing give stronger neighborhoods for special symmetry classes, but they do not imply a uniform statement for arbitrary complex sequences \(F\).

The present spectral-factor calculation bridges the gap between the March ratio estimate and the October open question, extending the general lower bound to
\[
\frac1{\sqrt2}.
\]

## Limitations

The exact value of \(\tau\) remains open in the interval
\[
\left[\frac1{\sqrt2},1\right].
\]

The factor
\[
(1-B^2)^{-2}
\]
is a convenient explicit Wiener-algebra bound and is not claimed to be optimal.

The outerness hypothesis on \(a_F\) is retained. No assertion is made for data with a nontrivial inner factor.

## References

1. M. Alexis, G. Mnatsakanyan, and K. Oganesyan, *Quantitative possibilities for Baxter's theorem in nonlinear Fourier analysis*, arXiv:2610.01711v1, 2026.
2. G. Mnatsakanyan, *\(\ell^1\) mapping properties, smoothness and decay for \(SU(2)\)-valued nonlinear Fourier transform*, arXiv:2603.02021v1, 2026.
3. Y. Dong, L. Lin, H. Ni, and J. Wang, *Robust iterative method for symmetric quantum signal processing in all parameter regimes*, arXiv:2307.12468v1, 2023.
