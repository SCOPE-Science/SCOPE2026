# Sharp classification for a gamma complete-monotonicity family

**Publication date:** 2026-09-21 (UTC)

**Same-model review: passed. Independent audit: not yet performed.**

## Statement

For real parameters `a,c` and `b>=0`, define

\[
f_{a,b,c}(x)=(x+a)\log x-x-\log\Gamma(x+b)+c,\qquad x>0.
\]

Set

\[
b_*:=\frac12-\frac{\sqrt3}{6}=\frac{1-1/\sqrt3}{2}.
\]

Then

\[
\boxed{
 f_{a,b,c}\in CM(0,\infty)
 \iff
 b_*\le b\le\frac12,\quad a=b-\frac12,\quad c\ge\log\sqrt{2\pi}.
}
\]

Moreover, whenever these conditions hold, all complete-monotonicity inequalities are strict:

\[
(-1)^n f_{a,b,c}^{(n)}(x)>0
\qquad (x>0,\ n=0,1,2,\ldots).
\]

This completes the parameter classification left implicit by Guo (2015): that paper proved the necessary conditions
\(b-a=1/2\), \(0<b\le1/2\), \(c\ge\log\sqrt{2\pi}\), and proved sufficiency on
\([b_*,1/2]\), but did not exclude the remaining interval \(0<b<b_*\).

## Necessity and the sharp lower endpoint

Complete monotonicity gives \(f\ge0\) and \(f'\le0\). The standard large-\(x\) expansion

\[
\log\Gamma(x+b)
=\left(x+b-\frac12\right)\log x-x+\log\sqrt{2\pi}+O(x^{-1})
\]

gives

\[
f_{a,b,c}(x)
=\left(a-b+\frac12\right)\log x+c-\log\sqrt{2\pi}+O(x^{-1}).
\]

If \(a-b+1/2>0\), then \(f'(x)>0\) for all sufficiently large \(x\); if
\(a-b+1/2<0\), then \(f(x)\to-\infty\). Hence necessarily

\[
a=b-\frac12,
\qquad
c\ge\log\sqrt{2\pi}.
\]

With this value of \(a\), the digamma expansion

\[
\psi(x+b)=\log x+\frac{b-1/2}{x}
+\frac{-b^2/2+b/2-1/12}{x^2}+O(x^{-3})
\]

yields

\[
f'_{a,b,c}(x)
=\frac{b^2-b+1/6}{2x^2}+O(x^{-3}).
\]

Since complete monotonicity requires \(f'\le0\), necessarily

\[
b^2-b+\frac16\le0,
\]

so

\[
\frac12-\frac{\sqrt3}{6}\le b\le
\frac12+\frac{\sqrt3}{6}.
\]

Finally, if \(b>1/2\), then \(a=b-1/2>0\), while

\[
f'(x)=\log x+\frac{b-1/2}{x}-\psi(x+b)\longrightarrow +\infty
\qquad (x\downarrow0),
\]

contradicting \(f'\le0\). Thus \(b\le1/2\), proving the sharp necessary range
\([b_*,1/2]\).

## Direct Laplace-kernel proof of sufficiency

Although sufficiency on \([b_*,1/2]\) was already available in Guo (2015), it also follows from a short positive-kernel argument.

Assume \(b\in[b_*,1/2]\), put \(a=b-1/2\), and define

\[
K_b(t)=\frac1t+\frac12-b-\frac{e^{-bt}}{1-e^{-t}},\qquad t>0.
\]

Then

\[
-f'(x)
=\psi(x+b)-\log x-\frac{b-1/2}{x}
=\int_0^\infty e^{-xt}K_b(t)\,dt,
\]

and therefore, with \(C=c-\log\sqrt{2\pi}\),

\[
f(x)=C+\int_0^\infty e^{-xt}\frac{K_b(t)}{t}\,dt.
\]

It remains to prove \(K_b(t)>0\). Write

\[
r=1-2b\in\left[0,\frac1{\sqrt3}\right],\qquad t=2y.
\]

The inequality \(K_b(2y)>0\) is equivalent to

\[
(1+ry)\sinh y>y e^{ry}.
\]

Set

\[
G_r(y)=\log\frac{(1+ry)\sinh y}{y e^{ry}}.
\]

For fixed \(y>0\),

\[
\partial_rG_r(y)=-\frac{r y^2}{1+ry}\le0,
\]

so it is enough to consider the worst case \(r=1/\sqrt3\). There

\[
G'_{1/\sqrt3}(y)
=\coth y-\frac1y-\frac{y}{3+\sqrt3 y}.
\]

For \(0<y\le2\), the partial-fraction expansion of \(\coth\) and
\(1/(A+y^2)\ge A^{-1}-y^2A^{-2}\) give

\[
\coth y-\frac1y
=2y\sum_{n\ge1}\frac1{y^2+\pi^2n^2}
\ge \frac y3-\frac{y^3}{45}.
\]

Consequently

\[
G'_{1/\sqrt3}(y)
\ge
\frac{y^2(15\sqrt3-3y-\sqrt3 y^2)}{45(3+\sqrt3 y)}>0.
\]

For \(y\ge2\), using \(\coth y>1\),

\[
G'_{1/\sqrt3}(y)
>
1-\frac1y-\frac{y}{3+\sqrt3 y}
=
\frac{(\sqrt3-1)y^2+(3-\sqrt3)y-3}{y(3+\sqrt3 y)}>0.
\]

Since \(G_{1/\sqrt3}(0+)=0\), one has \(G_r(y)>0\) for all
\(y>0\) and all admissible \(r\). Thus \(K_b(t)>0\) for every \(t>0\).
The Laplace representation then gives strict complete monotonicity whenever
\(C\ge0\).

Near \(t=0\), \(K_b(t)=O(t)\), so \(K_b(t)/t\) is locally bounded; at infinity the factor \(e^{-xt}\) gives convergence for every \(x>0\).

## Logarithmic-complete-monotonicity corollary

For

\[
g_{\alpha,\beta}(x)=\frac{x^{x+\beta-\alpha}}{e^x\Gamma(x+\beta)},
\]

one has

\[
\boxed{
 g_{1/2,\beta}\in LCM(0,\infty)
 \iff
 \frac12-\frac{\sqrt3}{6}\le\beta\le\frac12.
}
\]

Indeed, \(\log g_{1/2,\beta}\) has the same derivatives of positive order as
\(f_{\beta-1/2,\beta,c}\); the preceding necessity and positive-kernel argument give the exact interval.

## Literature status and originality

The primary source is Senlin Guo, *Some conditions for a class of functions to be completely monotonic*, Journal of Inequalities and Applications 2015:11. Its Theorem 1 gives the coarser necessary range \(0<b\le1/2\), while Theorem 2 proves the criterion for the subrange \([b_*,1/2]\). The same paper cites earlier logarithmic-complete-monotonicity results that supply the sufficiency mechanism.

Searches were made for the exact function, the source title and DOI, the algebraic threshold \(b_*\), the polynomial \(b^2-b+1/6\), and equivalent logarithmic-complete-monotonicity language. A 2016 review by Guo and a 2019 survey of gamma-ratio complete monotonicity were also checked for later coverage. No source was located that states the global if-and-only-if classification above or excludes every \(0<b<b_*\).

Accordingly, originality is claimed only **to the best of our knowledge**. A residual risk remains that an equivalent result appears under substantially different gamma-ratio notation or in literature not indexed by the searches used here.

## Limitations

- The result concerns this specific three-parameter gamma remainder family; it is not a classification of general gamma-ratio completely monotone functions.
- The proof uses standard asymptotic expansions and the classical partial-fraction expansion of \(\coth\); these ingredients are not claimed as new.
- The originality claim is literature-search based and not exhaustive.
- Independent audit has not been performed.

## References

1. S. Guo, *Some conditions for a class of functions to be completely monotonic*, Journal of Inequalities and Applications **2015**, 11 (2015). https://doi.org/10.1186/s13660-014-0534-y
2. S. Guo, *Logarithmically completely monotonic functions and applications*, Applied Mathematics and Computation **221** (2013), 169–176. https://doi.org/10.1016/j.amc.2013.06.037
3. S. Guo, *On Completely Monotonic and Related Functions*, Filomat **30** (2016), 2083–2090. https://doi.org/10.2298/FIL1607083G
4. F. Qi and R. P. Agarwal, *On complete monotonicity for several classes of functions related to ratios of gamma functions*, Journal of Inequalities and Applications **2019**, 36 (2019). https://doi.org/10.1186/s13660-019-1976-z
5. NIST Digital Library of Mathematical Functions, Chapters 5.9 and 5.11. https://dlmf.nist.gov/5.9 ; https://dlmf.nist.gov/5.11
