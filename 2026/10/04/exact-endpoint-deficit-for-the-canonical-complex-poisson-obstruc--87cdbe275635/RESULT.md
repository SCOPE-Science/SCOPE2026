# Exact endpoint deficit for the canonical complex Poisson obstruction family

## Finding

For \(0<\varepsilon<1\) define
\[
f_\varepsilon(\zeta)
=
\zeta\frac{1-\varepsilon\overline{\zeta}^{\,2}}{1-\varepsilon\zeta^2},
\qquad \zeta\in\mathbb T.
\]
Then \(|f_\varepsilon|=1\) and \(\widehat f_\varepsilon(0)=0\). This is the one-parameter family used in the recent complex Poisson Schwarz-contractivity paper to obtain the obstruction above exponent \(4\).

For every \(0<r<1\), set \(s=r^2\) and \(x=\varepsilon^2\). Then
\[
1-\frac{\|P_r f_\varepsilon\|_4^4}{r^4}
=
\frac{x(1-x)(1-s)}{(1-xs^2)^3}P(s,x),
\]
where
\[
\begin{aligned}
P(s,x)={}&4s+x(1-7s+s^2-3s^3)\\
&+x^2(1+5s-6s^2+2s^3+s^4+s^5)\\
&+x^3(s^2-3s^3+s^4+s^5).
\end{aligned}
\]
The polynomial \(P\) is strictly positive for \(0<s,x<1\). Consequently
\[
\|P_r f_\varepsilon\|_4<r
\qquad
(0<\varepsilon<1,\ 0<r<1).
\]
Thus this canonical family, although it gives failure for every \(p>4\), obeys the conjectured endpoint inequality strictly at every finite radius.

## Assumptions and scope

The circle \(\mathbb T\) carries normalized Haar measure, and \(P_r\) is the Poisson multiplier
\[
\widehat{P_r f}(n)=r^{|n|}\widehat f(n).
\]
The statement concerns exactly the explicit unimodular family above. It does not assert endpoint Schwarz-contractivity for arbitrary complex-valued zero-mean boundary data.

## Proof

The geometric-series expansion from the defining family gives
\[
f_\varepsilon(\zeta)
=
-\varepsilon\overline\zeta
+
(1-\varepsilon^2)
\sum_{k\ge0}\varepsilon^k\zeta^{2k+1}.
\]
Hence
\[
\frac{P_r f_\varepsilon(\zeta)}r
=
-\varepsilon\overline\zeta
+
(1-\varepsilon^2)
\sum_{k\ge0}(\varepsilon r^2)^k\zeta^{2k+1}.
\]
With \(w=\zeta^2\), multiplication by \(\zeta^{-1}\) does not change the modulus, and the push-forward of Haar measure under \(\zeta\mapsto\zeta^2\) is again Haar measure. Therefore
\[
\frac{\|P_r f_\varepsilon\|_4^4}{r^4}
=
\|H\|_4^4,
\qquad
H(w)
=
-\varepsilon
+
\frac{(1-\varepsilon^2)w}{1-\varepsilon r^2w}.
\]
The Taylor coefficients of \(H\) are
\[
h_0=-\varepsilon,
\qquad
h_n=(1-\varepsilon^2)(\varepsilon r^2)^{n-1}
\quad(n\ge1).
\]
Since \(H\) is analytic in a neighborhood of the closed disk,
\[
\|H\|_4^4=\|H^2\|_2^2.
\]
Writing \(s=r^2\), \(x=\varepsilon^2\), \(A=1-x\), and \(q=xs^2\), direct summation of the coefficients of \(H^2\) gives
\[
\|H\|_4^4
=
x^2+4xA^2
+
A^2\left[
\frac{A^2(1+q)}{(1-q)^3}
-
\frac{4xsA}{(1-q)^2}
+
\frac{4x^2s^2}{1-q}
\right].
\]
Putting this expression over the common denominator \((1-xs^2)^3\) and subtracting from \(1\) yields exactly the displayed deficit formula.

It remains to prove \(P(s,x)>0\) on the open unit square. Let
\[
B_{i,5}(s)=\binom5i s^i(1-s)^{5-i},
\qquad
B_{j,3}(x)=\binom3j x^j(1-x)^{3-j}.
\]
Then
\[
P(s,x)=\sum_{i=0}^5\sum_{j=0}^3 b_{ij}B_{i,5}(s)B_{j,3}(x),
\]
with coefficient rows
\[
\begin{array}{c|cccc}
i&j=0&j=1&j=2&j=3\\
\hline
0&0&1/3&1&2\\
1&4/5&2/3&6/5&12/5\\
2&8/5&31/30&19/15&12/5\\
3&12/5&4/3&16/15&8/5\\
4&16/5&22/15&8/15&0\\
5&4&4/3&0&0
\end{array}
\]
All coefficients are nonnegative. On \(0<s,x<1\), every Bernstein basis function is positive and at least one coefficient is positive, so \(P(s,x)>0\). The prefactor in the deficit formula is also positive, completing the proof.

## Verification

The accompanying verifier uses exact rational polynomial arithmetic. It reconstructs \(P\) from the displayed Bernstein table and checks coefficient-by-coefficient that it equals the monomial formula above. Independently, it clears the denominator in the exact closed form for \(\|H\|_4^4\) and verifies the polynomial identity
\[
(1-xs^2)^3\bigl(1-\|H\|_4^4\bigr)
=
x(1-x)(1-s)P(s,x).
\]
The computation is a finite algebra check; positivity itself follows analytically from the Bernstein representation.

## Relationship to prior work

Kovalev's 2026 paper proves complex Poisson Schwarz-contractivity through exponent \(3\), conjectures the endpoint exponent \(4\), and uses the family \(f_\varepsilon\) above to show that every \(p>4\) fails in the small-radius limit. Its proof records only the asymptotic expansion responsible for the supercritical obstruction. The paper also notes that the limiting \(r\to0\) endpoint \(p=4\) was known earlier.

Brevig, Ortega-Cerdà, and Seip studied the corresponding sharp exponent \(4\) phenomenon for Riesz projections and supplied the earlier obstruction mechanism adapted in the 2026 paper. Their result concerns the projection/infinitesimal setting rather than the finite-radius Poisson deficit computed here.

The present statement is therefore deliberately narrow: it gives an exact all-radius endpoint formula for the particular family that witnesses sharpness above \(4\), not a proof of the full endpoint conjecture.

## Limitations

The result is restricted to one explicit one-parameter family. It does not imply
\[
\|P_r f\|_4\le r\|f\|_\infty
\]
for arbitrary complex \(f\) with zero mean. No quantitative stability claim is made for perturbations away from this family, and no assertion is made for the centered nonzero-mean conjecture.

## References

1. L. V. Kovalev, *Schwarz-contractivity of the Poisson operator*, arXiv:2609.28938v1, 2026.
2. O. F. Brevig, J. Ortega-Cerdà, and K. Seip, *A converse to the Schwarz lemma for planar harmonic maps*, arXiv:2011.10967v2; J. Math. Anal. Appl. 497 (2021), 124908.
3. J. Marzo and K. Seip, *\(L^\infty\) to \(L^p\) constants for Riesz projections*, Bull. Sci. Math. 135 (2011), 324--331.
