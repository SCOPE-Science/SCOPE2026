# Sharp least-singular-value loss under stochastic rounding of planar rotations

## Finding

Let \(0\leq a,b\leq1\), with \(a^2+b^2>0\), and consider the scaled planar rotation
\[
A=\begin{pmatrix}a&b\\-b&a\end{pmatrix},\qquad s=\sqrt{a^2+b^2}.
\]
Independently round each entry to the adjacent integers, with probabilities chosen to preserve each entry's expectation. Thus \(\widehat A=\begin{pmatrix}X_1&Y_1\\-Y_2&X_2\end{pmatrix}\), where the \(X_i\) are independent Bernoulli variables of mean \(a\), the \(Y_i\) are independent Bernoulli variables of mean \(b\), and all four variables are independent. Write \(\sigma_2\) for the smaller singular value.

The exact expected squared least singular value and rank-loss probability are
\[
\boxed{\mathbb E\,\sigma_2(\widehat A)^2=s^2-(\sqrt5-1)ab(a+b-2ab)},\qquad
\boxed{\Pr(\operatorname{rank}\widehat A<2)=(1-a^2)(1-b^2)}.
\]
In particular, the first quantity is strictly smaller than \(\sigma_2(A)^2=s^2\) for every \(0<a,b<1\). Nevertheless, \(\mathbb E\|\widehat A\|_F^2=2(a+b)\geq2(a^2+b^2)=\|A\|_F^2\).

The sharp global relative bound is
\[
\boxed{\frac{\mathbb E\,\sigma_2(\widehat A)^2}{\sigma_2(A)^2}\geq\frac{5-\sqrt5}{4}},
\]
with equality if and only if \(a=b=1/2\). At that input, stochastic rounding loses a fraction \((\sqrt5-1)/4\) of expected squared least-singular-value energy, and returns a singular matrix with probability \(9/16\).

There is also an exact **orientation bifurcation** for the loss \(L(a,b)=ab(a+b-2ab)\) at fixed \(s\in(0,1]\). Put \(s_c=5/(4\sqrt2)\). For \(s\leq s_c\), the unique maximizer has \(a=b=s/\sqrt2\). For \(s_c<s\leq1\), the maximizers are precisely the two distinct coordinate swaps
\[
(a,b)=\frac{s}{2}\left(u_s+\sqrt{2-u_s^2},\ u_s-\sqrt{2-u_s^2}\right)
\]
and its swap, where \(u_s\in(1,\sqrt2)\) is the unique solution of
\[
4s u_s(u_s^2-1)=3u_s^2-1.
\]
Thus the orientation most vulnerable to stochastic rounding loses its equal-coordinate symmetry at the sharp scale \(5/(4\sqrt2)\).

## Assumptions and scope

The underlying unit-grid stochastic rounding is applied independently to all four real entries, including the two equal diagonal values and the opposite-signed off-diagonal values. The entrywise expectations equal the original entries. Zero and unit entries are rounded without noise; no correlations are imposed. All statements are finite-dimensional, exact-arithmetic results for the specified \(2\times2\) family. The orientation assertion assumes \(0<s\leq1\), ensuring every rotation orientation lies in the unit cell. Squared singular values are ordered decreasingly.

## Proof

**Exact distribution.** Write \(D=X_1X_2+Y_1Y_2=\det\widehat A\). A case classification by the number of nonzero entries gives the complete distribution of \(W=\sigma_2(\widehat A)^2\):
\[
\begin{array}{c|l}
W&\Pr(W=\cdot)\\\hline
1&a^2(1-b)^2+b^2(1-a)^2\\
(3-\sqrt5)/2&2a^2b(1-b)+2ab^2(1-a)\\
2&a^2b^2\\
0&1-\Pr(W=1)-\Pr(W=(3-\sqrt5)/2)-\Pr(W=2).
\end{array}
\]
Indeed, a pair of occupied entries has full rank exactly when both diagonal entries or both off-diagonal entries are occupied; the resulting singular values are both one. Any three occupied entries produce eigenvalues \((3\pm\sqrt5)/2\) of \(\widehat A^T\widehat A\). Four occupied entries yield \(\widehat A^T\widehat A=2I\); all remaining patterns have rank at most one. Multiplication by the displayed probabilities and algebraic simplification give the claimed expectation. Independence also gives
\[
\Pr(D=0)=\Pr(X_1X_2=0)\Pr(Y_1Y_2=0)=(1-a^2)(1-b^2).
\]
The loss is strictly positive when \(0<a,b<1\) since \(a+b-2ab=a(1-b)+b(1-a)>0\).

**Sharp relative bound.** For \(ab>0\), set \(k=ab/s^2\), so \(0<k\leq1/2\), and observe \(a+b=s\sqrt{1+2k}\). Hence
\[
\frac{L(a,b)}{s^2}=ks\sqrt{1+2k}-2k^2s^2
=\frac{1+2k}{8}-2k^2\left(s-\frac{\sqrt{1+2k}}{4k}\right)^2
\leq\frac{1+2k}{8}\leq\frac14.
\]
Equality requires \(k=1/2\) and \(s=1/\sqrt2\), so \(a=b=1/2\). The cases \(ab=0\) have zero loss and do not attain equality. Substituting into the expected least-singular-value identity proves the sharp constant.

**Sharp fixed-norm orientation.** Let \(u=(a+b)/s\in[1,\sqrt2]\). Then \(ab=s^2(u^2-1)/2\) and
\[
L(a,b)=\frac{s^3}{2}(u^2-1)\bigl(u-s(u^2-1)\bigr),
\quad
\frac{2}{s^3}\frac{dL}{du}=3u^2-1-4su(u^2-1).
\]
For \(u\in(1,\sqrt2]\), the derivative has the sign of \(h(u)-s\), where
\[
h(u)=\frac{3u^2-1}{4u(u^2-1)},\quad
h'(u)=-\frac{3u^4+1}{4u^2(u^2-1)^2}<0.
\]
Moreover \(h(1+)=+\infty\) and \(h(\sqrt2)=5/(4\sqrt2)\). Thus for \(s\le s_c\) the loss strictly increases on \((1,\sqrt2)\), whereas for \(s>s_c\) it rises then falls with a unique interior maximum \(u_s\). The identity \(a,b=s(u\pm\sqrt{2-u^2})/2\) turns the latter into exactly two swapped maximizers. This proves the phase boundary, including equality at the threshold.

## Verification

Run `python verify_rounding.py` with Python, NumPy, and SymPy. This independently enumerates all sixteen Bernoulli outcomes; derives the exact spectrum and rank-loss polynomial; checks the sharp equality input and the bifurcation derivative symbolically; checks 121 rational choices of \((a,b)\); compares an additional 1,000 random choices with direct dense singular-value decompositions of all sixteen rounded matrices; and checks six orientation regimes. All checks passed. Algebraic checks and numerical experiments are supporting reproducibility evidence; the displayed argument proves the quantified identities and extrema.

## Relationship to prior work

Ma, Yu, and Drineas (2026, arXiv:2606.00312) analyze stochastic rounding as a mechanism for raising small singular values in sufficiently structured higher-dimensional regimes, with spectral separation, aspect-ratio, and rank hypotheses used for the principal results; their study motivates testing where this mechanism can fail. Dexter et al. (2024, arXiv:2403.12278; SIAM J. Matrix Anal. Appl. 2025) concern tall-and-thin matrices, unlike the square, initially perfectly conditioned family here. Boutsikas, Drineas, and Ipsen (2023, arXiv:2303.03547) provide deterministic lower-precision small-singular-value bounds under their separate assumptions. Those papers do not, in the inspected material, supply the complete four-state least-singular-value law, sharp relative loss, rank-loss probability, or orientation bifurcation above. This is a boundary result, not a contradiction of their stated hypotheses.

## Limitations

The theorem concerns independent entrywise stochastic rounding to a unit grid of a \(2\times2\) real scaled rotation and the **expected squared** least singular value, not the expectation of the singular value itself. The orientation classification is restricted to \(s\le1\); the other formulas hold throughout the closed unit square except the zero input when a ratio is used. The analysis gives neither high-dimensional spectral behavior nor implementation-specific floating-point guarantees and makes no claim about correlated rounding. Bibliographic novelty remains subject to independent literature verification.

## References

- L. Ma, T. Yu, P. Drineas, *Stochastic Rounding Increases Small Singular Values*, arXiv:2606.00312v1 (first public 2026-05-29), https://arxiv.org/abs/2606.00312.
- G. Dexter, C. Boutsikas, L. Ma, I. C. F. Ipsen, P. Drineas, *Stochastic Rounding Implicitly Regularizes Tall-and-Thin Matrices*, arXiv:2403.12278 (2024); SIAM Journal on Matrix Analysis and Applications 46 (2025), https://doi.org/10.1137/24M1647679.
- C. Boutsikas, P. Drineas, I. C. F. Ipsen, *Small Singular Values Can Increase in Lower Precision*, arXiv:2303.03547 (2023), https://arxiv.org/abs/2303.03547.
