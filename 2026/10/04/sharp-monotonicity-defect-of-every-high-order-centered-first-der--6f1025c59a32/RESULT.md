# Sharp monotonicity defect of every high-order centered first derivative
## Finding
For an integer \(m\ge1\), let \(D_m\) be the standard maximal-order centered finite-difference approximation to the first derivative on the \(2m+1\) equispaced nodes \(jh\), \(-m\le j\le m\), with \(h>0\):
\[
D_m y
=
\frac1h\sum_{j=1}^{m}\alpha_{m,j}(y_j-y_{-j}),
\qquad
\alpha_{m,j}
=
(-1)^{j+1}
\frac{(m!)^2}{j(m-j)!(m+j)!}.
\]
This formula is exact on every polynomial of degree at most \(2m\).

Assume only that the sampled data are nondecreasing and bounded,
\[
0\le y_{-m}\le y_{-m+1}\le\cdots\le y_m\le M,
\qquad M>0.
\]
Then
\[
\min D_1y=0,
\]
whereas for every \(m\ge2\),
\[
\min D_my
=
-\frac{M}{h}V_m,
\qquad
V_m
=
\frac{m}{m+1}
-
\bigl(H_{2m}-H_m\bigr),
\]
where
\[
H_n=\sum_{k=1}^{n}\frac1k.
\]

The constant is sharp. One extremizer is the monotone step
\[
y_j=
\begin{cases}
0,&j\le1,\\
M,&j\ge2,
\end{cases}
\]
and the reflected one-step placement
\[
y_j=
\begin{cases}
0,&j\le-2,\\
M,&j\ge-1
\end{cases}
\]
gives the same minimum.

Moreover,
\[
0<V_2<V_3<\cdots<1-\log2,
\qquad
V_2=\frac1{12},
\]
and
\[
\lim_{m\to\infty}V_m=1-\log2
=
0.3068528194\ldots.
\]
Thus the three-point centered derivative is the unique member of this maximal-order centered family that can never reverse the sign implied by monotone sampled data. Every higher-order member can return a strictly negative derivative on nondecreasing data, and its sharp worst-case sign defect increases with the formal order, approaching \((1-\log2)M/h\).

The sign reversal also persists for strictly increasing data. Any sharp step extremizer can be perturbed by sufficiently small positive increments at every node; continuity of \(D_m\) keeps the derivative estimate negative.

## Assumptions and scope
The theorem concerns the classical centered first-derivative stencil on an equispaced grid and exact real arithmetic. It makes no smoothness assumption on the underlying function beyond the existence of sampled values satisfying the displayed monotonicity constraints.

The result is a statement about what the linear differentiation functional can infer from monotone samples alone. For samples of a sufficiently smooth monotone function and sufficiently small \(h\), consistency can of course force the numerical derivative toward the true derivative. The theorem instead gives the exact finite-stencil cone defect before any smoothness or scale-separation information is imposed.

The data bound \(0\le y_j\le M\) is only a normalization. Translation invariance of \(D_m\) means the same result holds for any data range of width \(M\).

## Proof
The standard centered weights follow by differentiating the Lagrange interpolant at the central node. For \(j\ge1\),
\[
\alpha_{m,j}
=
(-1)^{j+1}
\frac{(m!)^2}{j(m-j)!(m+j)!}.
\]
Their magnitudes are strictly decreasing:
\[
\frac{|\alpha_{m,j+1}|}{|\alpha_{m,j}|}
=
\frac{j(m-j)}{(j+1)(m+j+1)}
<1.
\]
Hence the positive-side weights alternate with decreasing magnitude, beginning with \(\alpha_{m,1}>0\).

Let \(c_j\) denote the dimensionless coefficient of \(y_j\), so \(c_0=0\), \(c_j=\alpha_{m,j}\) for \(j>0\), and \(c_{-j}=-\alpha_{m,j}\). Because constants differentiate to zero,
\[
\sum_{j=-m}^{m}c_j=0.
\]
Define nonnegative increments
\[
d_\ell=y_\ell-y_{\ell-1},
\qquad -m+1\le\ell\le m.
\]
Then
\[
\sum_{\ell=-m+1}^{m}d_\ell
=
y_m-y_{-m}
\le M,
\]
and summation by parts gives
\[
hD_my
=
\sum_{\ell=-m+1}^{m}d_\ell T_\ell,
\qquad
T_\ell
=
\sum_{j=\ell}^{m}c_j.
\]
Therefore the minimum over all monotone data is \(M/h\) times the most negative tail coefficient.

Put
\[
A_q=\sum_{j=q}^{m}\alpha_{m,j}.
\]
For positive indices, \(T_q=A_q\). By antisymmetry,
\[
T_{-q}=A_{q+1}
\qquad(1\le q\le m-1).
\]
Thus it suffices to minimize the positive-side tails \(A_q\).

Because the \(\alpha_{m,j}\) alternate in sign with strictly decreasing magnitude, every odd tail \(A_{2q+1}\) is positive and every even tail \(A_{2q}\) is negative. Moreover,
\[
A_{2q}-A_{2q+2}
=
\alpha_{m,2q}+\alpha_{m,2q+1}<0,
\]
so the most negative tail is \(A_2\).

It remains to evaluate \(A_2\). First,
\[
\alpha_{m,1}=\frac{m}{m+1}.
\]
Next, let
\[
S_m=\sum_{j=1}^{m}\alpha_{m,j}.
\]
Using
\[
\frac{(m!)^2}{(m-j)!(m+j)!}
=
\frac{\binom mj}{\binom{m+j}{j}}
\]
and
\[
\frac1{j\binom{m+j}{j}}
=
\int_0^1 t^{j-1}(1-t)^m\,dt,
\]
we obtain
\[
S_m
=
\int_0^1
(1-t)^m
\sum_{j=1}^{m}
(-1)^{j+1}\binom mj t^{j-1}\,dt.
\]
The finite binomial sum equals
\[
\frac{1-(1-t)^m}{t},
\]
hence
\[
S_m
=
\int_0^1
\frac{(1-t)^m-(1-t)^{2m}}{t}\,dt.
\]
With \(u=1-t\),
\[
S_m
=
\int_0^1
\frac{u^m-u^{2m}}{1-u}\,du
=
H_{2m}-H_m.
\]
Therefore
\[
A_2
=
S_m-\alpha_{m,1}
=
-\left[
\frac{m}{m+1}
-
(H_{2m}-H_m)
\right]
=
-V_m.
\]
For \(m\ge2\), \(A_2<0\) because it is an alternating tail beginning with the negative term \(\alpha_{m,2}\). Concentrating the full variation \(M\) in the increment associated with \(T_2\), or equivalently with \(T_{-1}\), gives the two displayed step extremizers and proves sharpness.

For monotonicity in \(m\), note that
\[
(H_{2m+2}-H_{m+1})-(H_{2m}-H_m)
=
\frac1{(2m+1)(2m+2)},
\]
while
\[
\frac{m+1}{m+2}-\frac{m}{m+1}
=
\frac1{(m+1)(m+2)}.
\]
The second increment is strictly larger, so
\[
V_{m+1}>V_m.
\]
Finally,
\[
\frac{m}{m+1}\to1,
\qquad
H_{2m}-H_m\to\log2,
\]
which gives the limiting defect \(1-\log2\).

## Verification
The accompanying `verify.py` uses exact rational arithmetic to regenerate the centered derivative weights from the closed form for every \(1\le m\le40\). It verifies exactness on monomials through degree \(2m\), strict decay of the weight magnitudes, the alternating-tail sign pattern, the location of the most negative tail, the harmonic-number identity, both step extremizers, and strict growth of \(V_m\) over the checked range.

The finite replay is not used to prove the all-order statements. The integral identity and alternating-tail argument above establish them for every integer \(m\ge1\).

## Relationship to prior work
Classical finite-difference literature gives systematic constructions of differentiation weights on arbitrary and equispaced grids. Sadiq and Viswanath treat finite-difference weights as derivatives of Lagrange cardinal polynomials, discuss centered formulas as standard examples, and analyze their accuracy and superconvergence. Those weight and accuracy facts are prior work.

Sign preservation is also a recognized structural requirement in high-resolution finite-difference reconstruction. Fjordholm and Ray emphasize that high-order linear or weighted reconstructions need special design to preserve the sign of discrete jumps in entropy-stable schemes. That broader motivation is prior work as well.

The present result addresses a different exact extremal question for the classical centered derivative itself: over the entire cone of bounded monotone sample vectors, what is the most negative derivative estimate? The answer is the closed harmonic-number formula \(V_m\), with exact extremizers, strict deterioration with increasing stencil order, and limiting defect \(1-\log2\). Targeted searches under monotonicity, sign preservation, cumulative stencil weights, harmonic numbers, and variation-diminishing terminology did not locate this all-order sharp formula.

## Limitations
The theorem is specific to first derivatives on symmetric equispaced maximal-order stencils. It does not classify one-sided, staggered, compact, optimized, or nonlinear differentiation formulas.

Monotone sampled data alone are deliberately weak information. If one imposes smoothness, derivative bounds, a minimum scale of variation, or samples generated by a fixed smooth function as \(h\to0\), much stronger sign guarantees can hold.

The earliest weight-generation paper by Fornberg was not recovered in full text through the lawful access routes used here. Its bibliographic record and abstract were inspected, while the full-text comparison relied on the later open Sadiq--Viswanath treatment. Older literature on positive linear functionals or variation-diminishing differentiation could contain an equivalent cumulative-weight observation under different language; this remains a residual originality risk.

## References
1. Burhan Sadiq and Divakar Viswanath, *Finite Difference Weights, Spectral Differentiation, and Superconvergence*, arXiv:1102.3203v1, February 15, 2011; Mathematics of Computation 83 (2014), 2403--2427.
2. Bengt Fornberg, *Generation of Finite Difference Formulas on Arbitrarily Spaced Grids*, Mathematics of Computation 51 (1988), 699--706, DOI: 10.1090/S0025-5718-1988-0935077-0.
3. Ulrik S. Fjordholm and Deep Ray, *A Sign Preserving WENO Reconstruction Method*, arXiv:1510.09038v1, October 30, 2015.
