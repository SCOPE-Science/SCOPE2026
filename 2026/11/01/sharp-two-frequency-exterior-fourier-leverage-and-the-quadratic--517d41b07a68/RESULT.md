# Sharp two-frequency exterior Fourier leverage and the quadratic collision defect

## Finding

For every real observation point \(x\) with \(|x|\ge 1\), the optimal point-evaluation inequality over all sums of two complex exponentials with **distinct arbitrary real frequencies** is
\[
|g(x)|^2 < \frac{1+3x^2}{2}\int_{-1}^{1}|g(t)|^2\,dt
\]
for each nonzero such sum \(g\), with the constant \((1+3x^2)/2\) being the exact supremum over all frequency choices and coefficients. The strict inequality is essential: the universal supremum is approached as the frequencies coalesce but is not attained by any distinct pair.

More precisely, for \(d>0\), put \(s_d=\sin(d)/d\). On any fixed pair of real frequencies whose absolute separation is \(d\), the exact optimal squared evaluation constant is
\[
\boxed{K_d(x)=\frac{1-s_d\cos(dx)}{1-s_d^2}.}
\]
For each fixed \(|x|\ge1\), the sharp small-separation correction is
\[
\boxed{K_d(x)=\frac{1+3x^2}{2}
-\frac{15x^4+6x^2-5}{120}\,d^2+O_x(d^4),\qquad d\downarrow0.}
\]
The quadratic-defect coefficient is strictly positive throughout \(|x|\ge1\).

## Assumptions and scope

Use the unnormalized Lebesgue norm \(\|g\|_2^2=\int_{-1}^1|g(t)|^2dt\). Let \(\lambda_1\ne\lambda_2\) be arbitrary real frequencies, let \(a,b\in\mathbb C\) not both vanish, and define
\[
g(t)=a e^{i\lambda_1t}+b e^{i\lambda_2t},\qquad
 d=|\lambda_1-\lambda_2|>0,\qquad
 c=\tfrac12(\lambda_1+\lambda_2).
\]
The evaluation point \(x\in\mathbb R\) is fixed and satisfies \(|x|\ge1\). The first result is an equality in a finite-dimensional extremal problem for **each** \(d>0\); the subsequent strict inequality and expansion are uniform over coefficients and center frequencies but the stated \(O_x\) remainder is for fixed \(x\), not uniform as \(|x|\to\infty\).

## Proof

**Step 1: Exact fixed-gap evaluation norm and extremizer.** After removing the unimodular carrier \(e^{ict}\), the two-frequency space is spanned by the orthogonal functions \(\cos(dt/2)\) and \(\sin(dt/2)\). Their squared norms on \([-1,1]\) are exactly \(1+s_d\) and \(1-s_d\), respectively. Since \(|s_d|<1\) for \(d>0\), point evaluation has squared norm
\[
\frac{\cos^2(dx/2)}{1+s_d}+\frac{\sin^2(dx/2)}{1-s_d}
=\frac{1-s_d\cos(dx)}{1-s_d^2}=K_d(x).
\]
Cauchy–Schwarz gives the claimed fixed-gap optimum and characterizes equality. Indeed, for any choice of center frequency \(c\), all nonzero maximizing functions are scalar multiples of
\[
g_{d,x}(t)=e^{ict}\left[
\frac{\cos(dx/2)\cos(dt/2)}{1+s_d}
+\frac{\sin(dx/2)\sin(dt/2)}{1-s_d}
\right].
\]
Its evaluation and squared norm both equal \(K_d(x)\). Thus the formula gives the exact sharp constant, not merely an upper bound.

**Step 2: High-frequency gaps.** If \(d\ge\pi\), then \(|s_d|\le1/\pi\). Directly from the orthogonal-basis formula,
\[
K_d(x)\le\frac1{1-|s_d|}
\le\frac{\pi}{\pi-1}<2\le\frac{1+3x^2}{2}.
\]
The inequality is strict for all \(|x|\ge1\).

**Step 3: Gaps \(0<d<\pi\).** Here \(0<s_d<1\). Write \(y=d/2\in(0,\pi/2)\). For every \(x\ge1\) one has
\[
|\sin(xy)|\le x\sin y.
\]
If \(xy\le\pi\), this follows from the monotone decrease of \(\sin u/u\) on \((0,\pi]\). If \(xy>\pi\), concavity on \([0,\pi/2]\) yields \(x\sin y\ge(2/\pi)xy>2\), so the same inequality holds. Since
\[
K_d(x)=\frac1{1+s_d}+\frac{2s_d}{1-s_d^2}\sin^2(dx/2),
\]
we obtain the interpolation upper bound
\[
K_d(x)\le K_d(0)+x^2\bigl(K_d(1)-K_d(0)\bigr).
\]
We have \(K_d(0)=1/(1+s_d)>1/2\). Also \(K_d(1)<2\): multiplying \(2-K_d(1)\) by the positive quantity \(d^2(1-s_d^2)\) gives
\[
F(d)=d^2+d\sin d\cos d-2\sin^2d.
\]
Here \(F(0)=F'(0)=0\) and
\[
F''(d)=4\sin d\bigl(\sin d-d\cos d\bigr)>0
\qquad (0<d<\pi),
\]
because \(\sin d-d\cos d=\int_0^d t\sin t\,dt>0\). Therefore \(K_d(1)<2\). Combining the two strict estimates, and noting that \(1-x^2\le0\), gives
\[
K_d(x)\le (1-x^2)K_d(0)+x^2K_d(1)
<\frac{1-x^2}{2}+2x^2
=\frac{1+3x^2}{2}.
\]
Finally \(K_d(-x)=K_d(x)\), so the result extends to \(x\le-1\).

**Step 4: The sharp collision limit and defect.** The Taylor expansions \(s_d=1-d^2/6+d^4/120+O(d^6)\) and \(\cos(dx)=1-d^2x^2/2+d^4x^4/24+O_x(d^6)\), inserted in the exact rational expression for \(K_d(x)\), yield
\[
K_d(x)=\frac{1+3x^2}{2}
-\left(\frac{x^4}{8}+\frac{x^2}{20}-\frac1{24}\right)d^2
+O_x(d^4).
\]
The coefficient \((15x^4+6x^2-5)/120\) is at least \(2/15>0\) for \(|x|\ge1\). Consequently the upper bound is optimal over all distinct frequency pairs because \(K_d(x)\to(1+3x^2)/2\), but no fixed \(d>0\) attains it. The maximizing representer above converges, after a harmless normalization and removal of its carrier, to the degree-one Legendre reproducing kernel \((1+3xt)/2\), which provides a geometric interpretation of the collision limit.

## Verification

The complete proof is analytic. An accompanying optional Python script (`CHECK.py`, requiring `mpmath`) tests the exact fixed-gap Gram formula, the strict exterior comparison, the positive quadratic coefficient, the small-gap expansion, the maximizing representer's exact norm and evaluation, and Cauchy–Schwarz for nonextremal complex coefficients. At 65-digit working precision it passed 448 supplementary assertions. These checks test selected parameters and do not replace the all-gap proof.

## Relationship to prior work

Zhang (2026, first publicly available 2026-07-11) establishes a general frequency-separation-free extrapolation estimate for arbitrary \(k\)-term Fourier sums, along with exterior leverage-score bounds. Its stated bounds retain \(k\)-dependent unspecified constants and do not identify this sharp two-term pointwise constant, the exact gap-dependent maximizer, or its quadratic collision defect. Chen and Price (2019) provide a less precise outside-window growth estimate for frequency-cluster algorithms; their Lemma 8.5 does not imply the exact squared constant here.

Denisov–Erdélyi endpoint inequalities and Borwein–Erdélyi's earlier Remez/Nikolskii work provide important context, but the located statements concern endpoint/interior control or order estimates, not an exact all-exterior fixed-gap kernel. No equivalent implication was found in the examined accessible publications or mathematical research records. A complete reading of all historical literature was not possible; the Borwein–Erdélyi paper's full text was inaccessible through the available authorized route, so implicit equivalent coverage remains a residual originality risk.

## Limitations

The theorem is specific to **two** frequency atoms with real frequencies and complex coefficients, a symmetric observation interval, an unweighted \(L^2\) norm, and real exterior evaluation. No extension to three or more atoms, arbitrary weights, nonreal evaluation, or stability for noisy nonlinear frequency recovery is claimed. For a fixed nonzero gap the optimizer is attained; for the global frequency-unrestricted bound it is only approached as the gap vanishes. The small-gap expansion is pointwise in the fixed evaluation point.

## References

1. Ruizhe Zhang, *Optimal Extrapolation Bounds for Sparse Fourier Sums*, arXiv:2607.10501 (first public version 2026-07-11), https://arxiv.org/abs/2607.10501.
2. Xue Chen and Eric Price, *Estimating the Frequency of a Clustered Signal*, arXiv:1904.13043 (2019), https://arxiv.org/abs/1904.13043, particularly Lemma 8.5.
3. Tamás Erdélyi, *Inequalities for Exponential Sums*, arXiv:1602.02315 (2016), https://arxiv.org/abs/1602.02315, particularly Theorem 2.3 as quoted by Zhang.
4. Peter Borwein and Tamás Erdélyi, *Pointwise Remez- and Nikolskii-type inequalities for exponential sums*, Mathematische Annalen (2000), https://doi.org/10.1007/s002080050003 (abstract accessible; full text not examined).
