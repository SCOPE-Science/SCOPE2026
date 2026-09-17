# The one-half threshold is sharp for discrete-potential AVE certification

## Statement

Chen and Xia (arXiv:2609.12763v2) introduce, for the absolute value equation
\[
Ax-|x|=b,
\]
the sign-indexed candidate
\[
x(z)=(A-Z)^{-1}b,\qquad Z=\operatorname{Diag}(z),\qquad z\in\{-1,1\}^n,
\]
and the discrete potential
\[
F(z)=z^\top(A-Z)^{-1}b=z^\top x(z).
\]
Their DPO theory proves that, under \(\|A^{-1}\|_1<1/2\), global maximizers of \(F\) correspond to AVE solutions, and it obtains a spectral-radius extension by positive diagonal scaling when \(\rho(|A^{-1}|)<1/2\).

The constant \(1/2\) is sharp for this global-potential characterization. For every
\[
c\in(1/2,1),
\]
there exists a two-dimensional AVE satisfying
\[
\|A^{-1}\|_1=\rho(|A^{-1}|)=c
\]
for which the AVE is uniquely solvable, but \(F\) has a unique global maximizer whose associated candidate is not an AVE solution. The same bad maximizer has exactly one sign mismatch, and correcting that mismatch strictly *decreases* \(F\). The construction persists under small perturbations and embeds into every dimension \(n\ge2\).

Dimension two is minimal: in dimension one, throughout the standard well-posed regime \(|A^{-1}|<1\), every global maximizer of this potential does correspond to the AVE solution.

## A sharp two-dimensional family

Fix
\[
0<\varepsilon<\frac12,\qquad c=\frac12+\varepsilon,
\]
and set
\[
B_\varepsilon:=A_\varepsilon^{-1}
=
\begin{pmatrix}
\frac12+\varepsilon&-\frac12\\
0&-\varepsilon
\end{pmatrix},
\qquad
b=
\begin{pmatrix}-1\\-3\end{pmatrix}.
\]
Equivalently,
\[
A_\varepsilon=
\begin{pmatrix}
\frac{2}{1+2\varepsilon}&-\frac{1}{\varepsilon(1+2\varepsilon)}\\
0&-\frac1\varepsilon
\end{pmatrix}.
\]

Both absolute column sums of \(B_\varepsilon\) equal \(1/2+\varepsilon\), hence
\[
\boxed{\|A_\varepsilon^{-1}\|_1=\frac12+\varepsilon.}
\]
Moreover
\[
|B_\varepsilon|=
\begin{pmatrix}
\frac12+\varepsilon&\frac12\\
0&\varepsilon
\end{pmatrix}
\]
is upper triangular, so
\[
\boxed{\rho(|A_\varepsilon^{-1}|)=\frac12+\varepsilon.}
\]
Since this number is strictly below one, the standard AVE sufficient condition
\(\rho(|A^{-1}|)<1\) guarantees unique solvability for every right-hand side. Thus the failure below is not caused by loss of AVE well-posedness.

Write \(F_{s_1s_2}=F((s_1,s_2))\). Direct inversion gives
\[
F_{--}
=
\frac{2(2\varepsilon+1)^2}{(\varepsilon-1)(2\varepsilon+3)},
\]
\[
F_{-+}
=
\frac{2(4\varepsilon^2+6\varepsilon-1)}
{(\varepsilon+1)(2\varepsilon+3)},
\]
\[
F_{+-}
=
\frac{2(4\varepsilon^2-2\varepsilon+1)}
{(\varepsilon-1)(2\varepsilon-1)},
\]
and
\[
F_{++}
=
\frac{2(2\varepsilon+1)}{\varepsilon+1}.
\]

The candidate associated with \(z_{\rm bad}=(1,-1)\) is
\[
x_{+-}
=
\begin{pmatrix}
\dfrac{2\varepsilon^2-\varepsilon+2}
{(1-\varepsilon)(1-2\varepsilon)}\\[1.2ex]
\dfrac{3\varepsilon}{1-\varepsilon}
\end{pmatrix}.
\]
Both entries are strictly positive. Therefore the second sign of \(z_{\rm bad}\) is wrong and
\[
(A_\varepsilon-Z_{\rm bad})x_{+-}=b
\]
does not imply
\[
A_\varepsilon x_{+-}-|x_{+-}|=b.
\]
By contrast,
\[
z_{\rm sol}=(1,1),\qquad
x_{++}
=
\begin{pmatrix}
\dfrac{\varepsilon+2}{\varepsilon+1}\\[1.2ex]
\dfrac{3\varepsilon}{\varepsilon+1}
\end{pmatrix}>0,
\]
so \(x_{++}\) is the unique AVE solution.

Nevertheless \(z_{\rm bad}\) is the unique global maximizer of \(F\). Indeed,
\[
F_{+-}-F_{++}
=
\frac{12\varepsilon^2}
{(1-\varepsilon^2)(1-2\varepsilon)}>0,
\]
\[
F_{+-}-F_{--}
=
\frac{4(2\varepsilon^2-\varepsilon+2)}
{(1-\varepsilon)(1-2\varepsilon)(2\varepsilon+3)}>0,
\]
and
\[
F_{+-}-F_{-+}
=
\frac{4(8\varepsilon^3+10\varepsilon^2-5\varepsilon+2)}
{(1-\varepsilon)(1+\varepsilon)(1-2\varepsilon)(2\varepsilon+3)}>0.
\]
The last numerator is positive because
\[
8\varepsilon^3+10\varepsilon^2-5\varepsilon+2
=
8\varepsilon^3+10\left(\varepsilon-\frac14\right)^2+\frac{11}{8}>0.
\]

Hence, for every \(c\in(1/2,1)\), the unweighted DPO objective can select a unique globally optimal sign pattern that is not the AVE sign pattern even though both
\(\|A^{-1}\|_1\) and \(\rho(|A^{-1}|)\) equal \(c\).

## The ascent mechanism also fails immediately above one half

At \(z_{\rm bad}=(1,-1)\), there is exactly one mismatched coordinate: the second one. Flipping it produces \(z_{\rm sol}=(1,1)\), but
\[
F(z_{\rm sol})-F(z_{\rm bad})
=
-\frac{12\varepsilon^2}
{(1-\varepsilon^2)(1-2\varepsilon)}
<0.
\]
Thus the mismatch-correcting move is a strict *descent* step for the DPO potential.

This does not prove that the full-flip generalized Newton method fails above \(1/2\): on this particular state it moves directly to the solution. What fails is the universal trap-free/ascent geometry used by the DPO analysis.

## Sharpness of the spectral scaling route

For every positive diagonal matrix \(W\),
\[
|WB_\varepsilon W^{-1}|=W|B_\varepsilon|W^{-1},
\]
and therefore
\[
\rho(|WB_\varepsilon W^{-1}|)
=
\rho(|B_\varepsilon|)
=
\frac12+\varepsilon.
\]
Every induced matrix norm dominates spectral radius, so
\[
\|WB_\varepsilon W^{-1}\|_1\ge\frac12+\varepsilon>\frac12.
\]
Consequently no positive diagonal scaling can move this family into the source paper's sub-\(1/2\) weighted \(1\)-norm regime. The same family therefore shows that the \(1/2\) threshold is sharp for that spectral-radius-to-diagonal-scaling route as well.

This statement is deliberately limited: it does not rule out a different potential, a different scaling argument, or additional structural assumptions above \(1/2\).

## Dimension two is minimal

For \(n=1\), let \(A=[a]\) with \(|a|>1\), equivalently \(|A^{-1}|<1\), and let \(b\in\mathbb R\). The two sign potentials are
\[
F(+)=\frac{b}{a-1},
\qquad
F(-)=-\frac{b}{a+1},
\]
so
\[
F(+)-F(-)=\frac{2ab}{a^2-1}.
\]
For \(b\ne0\), the sign of the unique scalar AVE solution is exactly
\(\operatorname{sgn}(ab)\), which is also the sign deciding which of \(F(+)\) and \(F(-)\) is larger. If \(b=0\), both sign candidates give the same primal solution \(x=0\). Hence no scalar counterexample exists anywhere in the usual \(|A^{-1}|<1\) uniqueness regime.

The two-dimensional family above is therefore dimension-minimal.

For any \(n>2\), append independent scalar blocks with \(A=4\) and \(b=1\). Each added scalar block has a unique DPO-maximizing sign \(+1\), while the block-diagonal inverse has the same overall \(1\)-norm and spectral radius \(c\). Thus the counterexample embeds into every dimension \(n\ge2\).

## Robustness and rational instances

For fixed \(\varepsilon\in(0,1/2)\), all sign inequalities and all three strict potential gaps above are strict. Since the candidates and potentials depend continuously on \(b\), the same wrong unique global maximizer persists for all right-hand sides in a sufficiently small open neighborhood of \((-1,-3)^\top\).

If \(\varepsilon\) is rational, then \(A_\varepsilon\), \(A_\varepsilon^{-1}\), and \(b\) are rational. Rational choices of \(\varepsilon>0\) can approach zero arbitrarily closely, so the failure occurs for rational-input instances arbitrarily close above the \(1/2\) threshold.

## Relation to prior one-half thresholds

The numerical value \(1/2\) is not itself new in AVE algorithms. Radons proved that a \(1/2\) infinity-norm restriction is sharp for a different property used by signed Gaussian elimination: guaranteed identification of a correct sign from a largest-magnitude right-hand-side coordinate. The present result concerns a distinct object introduced later: the global maximizers and ascent geometry of the DPO potential \(z^\top(A-Z)^{-1}b\), and it is sharp simultaneously in the source paper's \(1\)-norm and \(\rho(|A^{-1}|)\) formulations.

The standard AVE literature also gives the much weaker well-posedness condition
\[
\rho(|A^{-1}|)<1
\]
as sufficient for unique solvability. Hence the counterexample occupies the nonempty interval between DPO certification and AVE uniqueness: the AVE is completely well posed, yet the unweighted DPO global optimum is wrong.

## Reproducibility

`artifacts/verify_eps_1_20.py` uses exact rational arithmetic from the Python standard library to verify the concrete case \(\varepsilon=1/20\). It checks
\[
\|A^{-1}\|_1=\rho(|A^{-1}|)=\frac{11}{20},
\]
enumerates all four sign potentials, verifies that \((1,-1)\) is the unique global maximizer, verifies that its candidate has the wrong sign and nonzero AVE residual, and records the exact potential gap
\[
F_{+-}-F_{++}=\frac{40}{1197}.
\]
`artifacts/verified_output.txt` contains the executed exact-arithmetic output.

## References

1. C. Chen, Y. Xia, *Discrete Potential Optimization for Absolute Value Equations: A Sign-Flip Framework with Polynomial Complexity*, arXiv:2609.12763v2 (2026). https://arxiv.org/abs/2609.12763v2
2. M. Hladík, H. Moosaei, F. Hashemi, S. Ketabchi, P. M. Pardalos, *An overview of absolute value equations: from theory to solution methods and challenges*, Computational Optimization and Applications 93 (2026), 435–488. https://doi.org/10.1007/s10589-025-00717-5
3. M. Radons, *Direct solution of piecewise linear systems*, Theoretical Computer Science 626 (2016), 97–109. https://doi.org/10.1016/j.tcs.2016.02.009
