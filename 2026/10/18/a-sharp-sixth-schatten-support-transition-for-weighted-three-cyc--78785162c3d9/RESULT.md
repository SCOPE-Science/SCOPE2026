# A sharp sixth-Schatten support transition for weighted three-cycles

## Finding
For a nonnegative weighted three-cycle \(S_w\) on \(\mathbb C^3\), put
\[
S_we_j=w_j e_{j+1\pmod3},\qquad w_j\ge0,\qquad \sum_{j=0}^{2}w_j^2=1.
\]
For \(0\le t\le1\) define the unnormalized weighted Schatten-six numerical radius
\[
\mathcal W_{t,6}(S_w)=\sup_{\theta\in\mathbb R}
\left\|te^{i\theta}S_w+(1-t)e^{-i\theta}S_w^*\right\|_6,
\qquad \|M\|_6^6=\operatorname{tr}((M^*M)^3).
\]
Set \(u=1-t\), and define
\[
C=t^6+u^6,\quad D=3(t^2+u^2)(t^2-u^2)^2,\quad E=3(t^6+u^6)+6t^3u^3.
\]
The exact **global minimum**, including all zero weights, is
\[
\boxed{\min_{\sum w_j^2=1}\mathcal W_{t,6}(S_w)^6
=\min\left\{C-\frac D3+\frac E{27},\quad C-\frac D4\right\}.}
\tag{1}
\]
Let \(q_*= (3\sqrt5-5)/4\), and let \(t_*\) be the unique point in \((0,1/2)\) satisfying
\[
\frac{t_*(1-t_*)}{t_*^2+(1-t_*)^2}=q_*;
\qquad t_*\approx0.359741911255301.
\tag{2}
\]
For \(0\le t<t_*\) or \(1-t_*<t\le1\), the only minimizing squared-weight profile, up to permutation, is \((1/3,1/3,1/3)\). For \(t_*<t<1/2\) or \(1/2<t<1-t_*\), the only minimizing profile, up to permutation, is \((1/2,1/2,0)\). At \(t=t_*\) and \(t=1-t_*\), **both** profiles and no others minimize. At the symmetric parameter \(t=1/2\), **every** profile with at least one zero weight minimizes, with no further equality cases.

Thus the minimizer jumps discontinuously from a fully supported directed triangle to a broken two-edge path at a sharp, explicitly determined parameter. The sixth Schatten moment is the first even Schatten moment in which the triangle's winding phase contributes.

## Assumptions and scope
The matrices are exactly \(3\times3\) complex Hilbert-space operators with a directed three-cycle and nonnegative real weights. The weights may be zero, the Hilbert–Schmidt energy is normalized to \(1\), and the Schatten-six norm uses the ordinary, not dimension-normalized, trace. The parameter \(t\) ranges over the closed interval \([0,1]\); all displayed equality classifications include endpoint and degenerate parameters. The assertion is about the global **minimum**, not the maximum, and does not claim analogous results for arbitrary matrices, other cycle lengths, or Schatten exponents.

## Proof
**1. Exact phase-sensitive sixth moment.** Write \(x=w_0^2\), \(y=w_1^2\), \(z=w_2^2\). Then \(x,y,z\ge0\) and \(x+y+z=1\). For
\(A_\theta=te^{i\theta}S_w+ue^{-i\theta}S_w^*\), direct multiplication of the three-by-three matrices gives
\[
\begin{aligned}
\operatorname{tr}((A_\theta^*A_\theta)^3)
={}&(t^6+u^6)(x^3+y^3+z^3)\\
&+3t^2u^2(t^2+u^2)
  (x^2y+xy^2+y^2z+yz^2+z^2x+zx^2)\\
&+\bigl(9t^2u^2(t^2+u^2)+6t^3u^3\cos(6\theta)\bigr)xyz.
\end{aligned}
\tag{3}
\]
This identity follows either by expanding the matrix product or by recording the six-step closed walks of the three-cycle: the only phase-carrying words make a full clockwise or counterclockwise winding twice and contribute the pair of phase factors \(e^{6i\theta}\) and \(e^{-6i\theta}\). In particular, the coefficient of \(\cos(6\theta)\) is nonnegative. The supremum in the definition is attained at \(\theta=0\) for every admissible choice, including all degeneracies.

Let \(s_2=xy+yz+zx\) and \(s_3=xyz\). Using
\[
x^3+y^3+z^3=1-3s_2+3s_3,
\qquad\sum_{\mathrm{sym}}x^2y=s_2-3s_3,
\]
and
\[
(t^6+u^6)-t^2u^2(t^2+u^2)
=(t^2+u^2)(t^2-u^2)^2,
\]
formula (3) becomes the exact identity
\[
\boxed{\mathcal W_{t,6}(S_w)^6=C-Ds_2+Es_3.}
\tag{4}
\]
**2. The sharp simplex inequalities.** For every nonnegative triple summing to one,
\[
s_2\le\frac13,
\qquad
s_2-\frac94s_3\le\frac14.
\tag{5}
\]
The first inequality follows from \(x^2+y^2+z^2\ge1/3\). The second is the classical cubic Schur inequality \(1+9xyz\ge4(xy+yz+zx)\). Equality in the first occurs only at \((1/3,1/3,1/3)\). Equality in the second occurs precisely at that uniform triple and at permutations of \((1/2,1/2,0)\).

For \(t\ne1/2\), \(D>0\); put \(r=E/D>0\). If \(r\le9/4\), the convex combination
\[
s_2-rs_3=\left(1-\frac{4r}{9}\right)s_2+
\frac{4r}{9}\left(s_2-\frac94s_3\right)
\le\frac13-\frac r{27}
\tag{6}
\]
proves that the uniform profile is optimal. At strict \(r<9/4\), it is the unique optimum. If \(r\ge9/4\), then
\[
s_2-rs_3\le s_2-\frac94s_3\le\frac14,
\tag{7}
\]
so the two-edge equal profile is optimal. At strict \(r>9/4\), it is the only optimum up to permutation. At equality \(r=9/4\), the Schur equality cases give exactly both profiles. Substituting these two profiles into (4) establishes (1) and all equality cases away from \(t=1/2\).

At \(t=1/2\), \(D=0\) and \(E>0\), so (4) is minimized precisely when \(xyz=0\). This proves the larger symmetric-parameter equality family.

**3. Exact transition parameter.** For \(0\le t<1/2\), set
\[
q=\frac{tu}{t^2+u^2}\in[0,1/2).
\]
Expanding \(C=(t^2+u^2)^3-3t^2u^2(t^2+u^2)\) gives
\[
\frac ED=\frac{1-3q^2+2q^3}{1-4q^2}
=\frac{(1-q)^2}{1-2q}.
\tag{8}
\]
This expression is strictly increasing for \(0<q<1/2\), from \(1\) to \(+\infty\). Solving \(E/D=9/4\) yields the unique permissible root \(q_*=(3\sqrt5-5)/4\). The map \(t\mapsto q\) is strictly increasing on \([0,1/2)\), so (2) defines the unique \(t_*\) there. Symmetry under \(t\leftrightarrow1-t\) supplies the other transition. This completes the proof.

## Verification
The standalone Python 3 checker `verify_triangle_s6.py` uses exact rational Gaussian matrix arithmetic to verify the sixth-moment expansion for seven weight patterns, seven parameter values and two phases (\(\theta=0,\pi/2\)): 98 independent exact matrix identities. It also checks Schur's sharp inequality and equality cases on a rational simplex grid and verifies the lower bound and attainment on 8,575 simplex-grid instances. The script computes the transition value separately. Run `python verify_triangle_s6.py`; the success marker is `TRIANGLE_SIXTH_MOMENT_EXACT_CHECK_OK`. These finite checks are supplementary; identities (3)–(8) and their equality arguments establish the continuum theorem.

## Relationship to prior work
Pal and Chandok, *On weighted Schatten p-numerical radii via generalized Aluthge transformation*, arXiv:2610.11336v1 (first submitted October 8, 2026), provides the current weighted Schatten-radius setting and general bounds. Its publicly available abstract and metadata were read, but the full paper was not accessible through attempted lawful routes; this imposes a residual priority risk rather than a claimed proof of noncoverage. The present result concerns a distinct **global constrained minimum and complete equality transition** for the first winding-sensitive moment of a three-cycle.

A published theorem on exact Schatten-fourth radii of **nilpotent path** shifts, *Sharp weighted Schatten-fourth radii of nilpotent shifts* (2026), supplies a fourth-order nearest-neighbor maximization law, not a sixth-order minimum on a closed triangle. A separate published theorem on even Schatten radii under **circle covariance**, *Sharp even Schatten numerical-radius moments under circle covariance* (2026), gives dimension-uniform upper bounds but does not apply to fully supported three-cycles: a nonzero three-cycle has a finite nonzero spectrum and cannot be unitarily equivalent to all of its scalar rotations. These distinct results do not imply (1), (2), or the equality classification. Schur's cubic inequality in (5) is classical and is expressly **not** claimed to be new; the operator identity and its sharp support transition are the asserted findings.

## Limitations
This is a three-dimensional, nonnegative-real-weight result with exact Hilbert–Schmidt normalization and Schatten exponent six. The result does not resolve optimization for other matrix shapes, dimensions, or exponents. A broader uninspected theorem or an unindexed exact calculation may subsume the classification, and the full source paper by Pal and Chandok could not be checked beyond its abstract and metadata. Publication priority is not independently certified.

## References
1. K. Pal and S. Chandok, *On weighted Schatten p-numerical radii via generalized Aluthge transformation*, arXiv:2610.11336v1, October 8, 2026, https://arxiv.org/abs/2610.11336 .
2. *Sharp weighted Schatten-fourth radii of nilpotent shifts* (2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-sharp-weighted-schatten-fourth-radii-of-nilpotent-shifts--17db4dbf42a4/RESULT.md .
3. *Sharp even Schatten numerical-radius moments under circle covariance* (2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-sharp-even-schatten-numerical-radius-moments-under-circle-covari--6104c50d4ada/RESULT.md .
4. J. Hamza and H. Issa, *Generalized Numerical Radius Inequalities for Schatten p-Norms*, arXiv:2204.02469 (2022), https://arxiv.org/abs/2204.02469 .
5. G. H. Hardy, J. E. Littlewood and G. Pólya, *Inequalities*, second edition, Cambridge University Press (1952), Schur's inequality.
