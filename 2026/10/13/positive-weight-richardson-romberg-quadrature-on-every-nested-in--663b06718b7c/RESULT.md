# Positive-weight Richardson–Romberg quadrature on nested integer refinement chains

## Finding
Let \(a<b\), let \(d\ge1\), and take a finite **strict integer divisibility chain**
\[
N_0\mid N_1\mid\cdots\mid N_d,\qquad N_j\ge1,\quad N_{j+1}/N_j\in\{2,3,\dots\}.
\]
Set \(h_j=(b-a)/N_j\), and let \(T_j\) be the closed composite trapezoidal rule with \(N_j\) panels. The depth-\(d\) Richardson–Romberg extrapolate \(Q_d=\sum_{j=0}^d c_jT_j\) is determined uniquely by
\[
\sum_{j=0}^d c_j=1,\qquad \sum_{j=0}^d c_jh_j^{2q}=0\quad(1\le q\le d).
\]
After collecting on the finest grid, **every sample weight is strictly positive**. Precisely the nodes first introduced at level \(d\) attain the largest weight
\[
\boxed{\max_i w_i=h_d\prod_{j=0}^{d-1}\left(1-(N_j/N_d)^2\right)^{-1}.}
\]
Moreover \(\sum_i|w_i|=b-a\), the smallest possible absolute-sample-error operator norm for any constant-exact quadrature formula.

The condition \(d\ge1\) is essential for the **unqualified maximum formula**: at depth zero with the single-panel grid \(N_0=1\), there are only two endpoint weights \(h_0/2\), so the formula \(\max w_i=h_0\) would be false. The zero-depth trapezoidal rule is nevertheless positive. The positive-depth theorem makes no assertion about nonnested panel-count sequences.

## Scope and definitions
The weights are those of the **fully collected**, exact-arithmetic rule, not coefficients used in an intermediate extrapolation tableau. At each interior fine-grid node of first appearance level \(\ell\), every level \(j\ge\ell\) supplies the ordinary trapezoidal weight \(h_j\), and levels \(j<\ell\) supply zero. Each endpoint receives half those level weights. The conclusion holds at arbitrary finite depth \(d\ge1\) and for every changing sequence of integer refinement factors at least two. It does not cover floating-point accumulation, nonnested grids, arbitrary interpolation/extrapolation, stochastic data errors, or relative error models.

## Proof
Put \(x_j=h_j^2\). Then \(x_0>x_1>\cdots>x_d>0\), with \(x_{j+1}\le x_j/4\). Lagrange interpolation at zero for nodes \(x_j\) yields the unique Richardson coefficients
\[
c_j=\prod_{i\ne j}\frac{-x_i}{x_j-x_i},\qquad \operatorname{sgn}(c_j)=(-1)^{d-j}.
\]
Write \(b_j=|c_j|h_j\). Cancelling neighboring factors gives
\[
\frac{b_{j+1}}{b_j}=\sqrt{\frac{x_j}{x_{j+1}}}\prod_{i\ne j,j+1}\frac{|x_j-x_i|}{|x_{j+1}-x_i|}.
\]
Every factor indexed by \(i>j+1\) exceeds one. For an earlier index \(i<j\), let \(q=j-i\), \(X=x_i/x_j\ge4^q\), and \(y=x_{j+1}/x_j\le1/4\). Its factor obeys
\[
\frac{X-1}{X-y}>1-\frac1X\ge1-4^{-q}.
\]
Also \(\sqrt{x_j/x_{j+1}}=N_{j+1}/N_j\ge2\). Thus for \(j\ge1\),
\[
\frac{b_{j+1}}{b_j}>2\prod_{q=1}^{j}(1-4^{-q})
\ge2\left(1-\sum_{q=1}^\infty4^{-q}\right)=\frac43>1.
\]
For \(j=0\) the empty product gives \(b_1/b_0\ge2\). Therefore \(0<b_0<b_1<\cdots<b_d\).

An interior node first appearing at level \(\ell\) receives
\[
W_\ell=\sum_{j=\ell}^{d}c_jh_j=b_d-b_{d-1}+b_{d-2}-\cdots+(-1)^{d-\ell}b_\ell.
\]
The alternating tail is strictly positive because each finer magnitude is greater than its adjacent coarser magnitude. For \(\ell<d\), group the negative-leading remainder as \((-b_{d-1}+b_{d-2})+(-b_{d-3}+b_{d-4})+\cdots\); if needed the final term is negative. Hence \(0<W_\ell<b_d\). Endpoints have \(W_0/2>0\), strictly less than \(b_d\). Because \(d\ge1\) and each refinement factor is at least two, at least one new interior node appears at level \(d\), and each receives exactly \(W_d=b_d\). Consequently these and only these nodes maximize the collected weight.

The last Lagrange coefficient is positive and equals
\[
c_d=\prod_{j=0}^{d-1}\frac{x_j}{x_j-x_d}
=\prod_{j=0}^{d-1}\left(1-\left(\frac{N_j}{N_d}\right)^2\right)^{-1}.
\]
Thus \(b_d=h_dc_d\) is exactly the claimed maximum. Since constants are integrated exactly, \(\sum_i w_i=b-a\); strict positivity gives \(\sum_i|w_i|=b-a\). Conversely every constant-exact quadrature rule satisfies \(\sum_i|w_i|\ge|\sum_i w_i|=b-a\). The collected rule therefore achieves the optimal bounded-absolute-sample-error norm. \(\square\)

## Exact checks and boundary examples
For \((N_0,N_1,N_2)=(1,2,6)\) on \([0,1]\), the coefficients are \((1/105,-1/6,81/70)\). The seven collected weights are
\[
(5/84,\ 27/140,\ 27/140,\ 23/210,\ 27/140,\ 27/140,\ 5/84),
\]
which are strictly positive and attain the displayed maximum at newly introduced nodes. Independent rational arithmetic also checks mixed chains \((1,3,6,24)\), \((2,4,12)\), \((2,4,8,24)\) and \((1,2,4,16)\); such finite calculations corroborate, but do not replace, the universally quantified proof. The archived verifier under `artifacts/verify.py` evaluates 124 finite nested chains and confirms the claimed positive-depth algebra.

Nesting is substantive. The nonnested sequence \((1,2,5)\) on \([0,1]\) yields coefficients \((1/72,-16/63,625/504)\), and the midpoint belongs only to the two-panel grid, hence receives the negative collected weight \(-8/63\). This does not mean every nonnested chain fails positivity.

## Relationship to primary literature and limits of originality
Classical dyadic Romberg positivity and the general Richardson–Romberg interpolation framework are prior work. Pagès, *Multi-step Richardson-Romberg Extrapolation: Remarks on Variance Control and Complexity* (arXiv:math/0612523, 2006), develops multilevel extrapolation in a stochastic Euler setting, not positivity of collected composite-trapezoidal weights. Farzi, *Generalized extrapolation methods for solving nonlinear Fredholm integral equations* (Mathematical Communications 19(2), 2014, 375–390), analyzes general division sequences but discusses positive quadrature weights for named classical and selected Bauer sequences; no all-strict-divisibility statement appears in the inspected positivity material. The published finding *Positive-weight generalized Romberg quadrature for every integer refinement factor* (2026-09-21, `2026/9/21/SCOPE-generalized-romberg-positive-weights-integer-refinement--b7c2819b6648`) covers only a fixed geometric refinement factor \(N_j=s r^j\). The present theorem permits independent integer ratios at consecutive stages and gives an all-chain proof.

The historical numerical-integration literature is extensive; an equivalent nested-divisibility criterion may exist under terminology not recovered from the inspected sources. This best-of-knowledge claim does not assert classification of all positive division sequences, nor numerical stability of an uncollected floating-point extrapolation tableau.

## References
1. G. Pagès, *Multi-step Richardson-Romberg Extrapolation: Remarks on Variance Control and Complexity*, arXiv:math/0612523 (2006).
2. J. Farzi, *Generalized extrapolation methods for solving nonlinear Fredholm integral equations*, Mathematical Communications 19(2) (2014), 375–390.
3. *Positive-weight generalized Romberg quadrature for every integer refinement factor*, published finding, 2026-09-21, record `2026/9/21/SCOPE-generalized-romberg-positive-weights-integer-refinement--b7c2819b6648`.
4. A. Sidi, *A Complete Convergence and Stability Theory for a Generalized Richardson Extrapolation Process*, SIAM J. Numer. Anal. 34(5) (1997), DOI:10.1137/S0036142994278589.
