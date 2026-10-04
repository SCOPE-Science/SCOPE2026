# Three blocks create a sharp momentum-stability barrier for cyclic alternating minimization
## Finding
Consider the strongly convex symmetric block quadratic
\[
E_m(x)=\frac m2\sum_{i=1}^{p}x_i^2+\frac12\left(\sum_{i=1}^{p}x_i\right)^2,
\qquad m>0,
\]
and the following fixed-momentum extension of one exact cyclic alternating-minimization sweep: before each sweep form
\[
\bar x^k=x^k+\alpha(x^k-x^{k-1}),\qquad 0\le\alpha\le1,
\]
then minimize exactly in blocks \(1,2,\ldots,p\), using freshly updated earlier blocks and the components of \(\bar x^k\) for later blocks.

For \(p=2\), the iteration is asymptotically stable for every \(m>0\) and every \(\alpha\in[0,1]\).

For \(p=3\), put \(c=(1+m)^{-1}\in(0,1)\) and
\[
P_c(\alpha)=1+c+c^2+\alpha c^3(c^2-2c-2)+3\alpha^2c^3(c^2-c-1)+3\alpha^3c^5.
\]
Then the iteration is asymptotically stable if and only if
\[
P_c(\alpha)>0.
\]
Let \(c_*\) be the unique root in \((0,1)\) of
\[
7c^4+2c^3-3c^2-2c-1=0.
\]
Numerically,
\[
c_*=0.848972455633114467\ldots,
\qquad
m_*=c_*^{-1}-1=0.177894516323568991\ldots.
\]
If \(c<c_*\), every \(\alpha\in[0,1]\) is stable. If \(c=c_*\), stability holds exactly for \(0\le\alpha<1\). If \(c>c_*\), there is a unique \(\alpha_{\mathrm{crit}}(c)\in(0,1)\), the unique zero of \(P_c\), and stability holds exactly for
\[
0\le\alpha<\alpha_{\mathrm{crit}}(c).
\]
In particular, unit extrapolation \(\alpha=1\) is stable for every member of the two-block family but is unstable for the three-block family exactly when
\[
0<m<m_*.
\]
Thus three blocks are minimal for this momentum-instability mechanism inside the symmetric family.

## Assumptions and scope
The result concerns exact real arithmetic, exact minimization of each scalar block, the fixed cyclic order, and one global extrapolation before each complete sweep. The objective has unique minimizer \(x=0\) for every \(m>0\). Stability means that the lifted linear recurrence on \((x^k,x^{k-1})\) has spectral radius strictly smaller than one, equivalently that every initial pair converges to zero.

This is not a claim about every accelerated coordinate method. In particular, algorithms with per-block extrapolation, randomized coordinates, auxiliary sequences, line search, or restarting have different iteration matrices.

## Proof
Write
\[
c=\frac1{1+m}.
\]
For three blocks, exact minimization of one coordinate of \(E_m\) gives the update rule
\[
x_i\leftarrow-c\sum_{j\ne i}x_j.
\]
One complete cyclic sweep applied to an input vector \(v\) is therefore \(G_cv\), where
\[
G_c=
\begin{pmatrix}
0&-c&-c\\
0&c^2&c(c-1)\\
0&c^2(1-c)&c^2(2-c)
\end{pmatrix}.
\]
Its characteristic polynomial is
\[
\det(\lambda I-G_c)
=\lambda\left(\lambda^2-c^2(3-c)\lambda+c^3\right).
\]
For \(0<c<1\), the two nonzero eigenvalues are a complex-conjugate pair. Indeed their discriminant is
\[
c^3\bigl(c(3-c)^2-4\bigr)<0,
\]
because \(c(3-c)^2\) increases to \(4\) on \((0,1]\). Denote either nonzero eigenvalue by \(\lambda\). Then
\[
|\lambda|^2=c^3,
\qquad
\operatorname{Re}\lambda=\frac{c^2(3-c)}2.
\]

The extrapolated sweep satisfies
\[
x^{k+1}=G_c\bigl((1+\alpha)x^k-\alpha x^{k-1}\bigr).
\]
On a nonzero eigenmode of \(G_c\), the characteristic equation is
\[
r^2-(1+\alpha)\lambda r+\alpha\lambda=0.
\]
For a monic quadratic \(r^2+a_1r+a_0\) with complex coefficients, the Schur--Cohn criterion says that both roots lie strictly inside the unit disk exactly when
\[
|a_0|<1,
\qquad
|a_1-\overline{a_1}a_0|<1-|a_0|^2.
\]
Here \(|a_0|=\alpha c^{3/2}<1\) automatically for \(0\le\alpha\le1\) and \(0<c<1\). Squaring the second inequality and substituting the two identities for \(\lambda\) gives
\[
(1-\alpha^2c^3)^2-(1+\alpha)^2c^3
\left(1-\alpha c^2(3-c)+\alpha^2c^3\right)>0.
\]
Direct expansion factors the left side as
\[
(1-c)P_c(\alpha).
\]
Because \(1-c>0\), this proves the exact criterion \(P_c(\alpha)>0\). The zero eigenvalue of \(G_c\) contributes only zero roots to the lifted recurrence and causes no further restriction.

It remains to classify the sign. Differentiation yields
\[
\frac{\partial P_c}{\partial\alpha}
=c^3\left[(c^2-2c-2)+6\alpha(c^2-c-1)+9\alpha^2c^2\right].
\]
The bracket is convex in \(\alpha\). At the endpoints \(\alpha=0\) and \(\alpha=1\) it equals, respectively,
\[
c^2-2c-2<0,
\qquad
8(2c+1)(c-1)<0.
\]
A convex function on an interval cannot exceed the larger of its endpoint values, so \(P_c\) is strictly decreasing on \([0,1]\). Also \(P_c(0)=1+c+c^2>0\). At unit extrapolation,
\[
P_c(1)=(c-1)\left(7c^4+2c^3-3c^2-2c-1\right).
\]
The quartic in parentheses has exactly one positive root by Descartes' rule of signs; its values at \(0\) and \(1\) are \(-1\) and \(3\), so that root is the unique \(c_*\in(0,1)\). Strict decrease of \(P_c\) in \(\alpha\) now gives all three cases in the statement.

For two blocks, one cyclic sweep has eigenvalues \(0\) and \(c^2\). The only nonzero modal polynomial is
\[
r^2-(1+\alpha)c^2r+\alpha c^2.
\]
The real Jury conditions reduce to
\[
1-c^2>0,
\qquad
1+(1+2\alpha)c^2>0,
\qquad
1-\alpha c^2>0,
\]
which hold for every \(0<c<1\) and \(0\le\alpha\le1\). One block is trivial, so the three-block obstruction is minimal within this family.

## Verification
The accompanying `verify.py` independently reconstructs the sweep matrix, checks its characteristic polynomial numerically over exact-rational test points, verifies the Schur--Cohn factorization over a grid of exact rational \((c,\alpha)\) pairs, isolates \(c_*\) by bisection, and confirms stable, neutral, and unstable examples from the actual lifted modal roots. It also checks the two-block Jury inequalities over a dense rational grid.

The numerical checks are corroborative. The theorem for all \(m>0\) and \(0\le\alpha\le1\) follows from the analytic argument above.

## Relationship to prior work
Chambolle and Pock analyze alternating minimization for objectives consisting of block-separable convex terms plus a quadratic coupling. Their 2015 preprint proves an accelerated construction for the two-block case and explicitly notes the difficulty of extending acceleration to general deterministic alternating schemes. The quadratic family above is a direct smooth, strongly convex member of their model class. Their paper does not give the three-block constant-momentum stability boundary derived here.

Hong and Yavneh later analyze Nesterov-style acceleration of general stationary linear iterations. Their framework contains the modal recurrence
\[
r^2-(1+\alpha)\lambda r+\alpha\lambda=0
\]
and studies robustness when stationary iteration matrices possess complex eigenvalues. That general identity is prior work and is not claimed here. The new statement is the exact spectrum of this natural three-block cyclic alternating-minimization sweep, the resulting sharp Schur--Cohn phase boundary \(P_c(\alpha)=0\), and the proof that three blocks are minimal within the symmetric family. The inspected Hong--Yavneh results give sufficient complex-eigenvalue regions for preserving a real-spectrum optimal parameter; they do not state this exact block-count boundary.

A recent worst-case study of cyclic block coordinate methods analyzes alternating minimization and a different cyclic accelerated-coordinate construction. It reports that a standard randomized acceleration can be inefficient after deterministic cyclicization. Its inspected full text uses a two-sequence per-coordinate accelerated method rather than the global-before-sweep extrapolation studied here, and it does not state this quadratic stability diagram.

## Limitations
The theorem is deliberately narrow: it concerns the symmetric all-to-all quadratic family and a fixed global momentum parameter. It does not imply that cyclic acceleration is impossible in three blocks, nor does it assess randomized methods, restart mechanisms, per-block momentum, or the specific two-sequence cyclic acceleration analyzed in later work.

The strongest originality risk is the general stationary-iteration literature: the modal recurrence itself is known, and the present result combines it with the exact spectrum of a particular Gauss--Seidel-type sweep and a sharp Schur--Cohn calculation. No inspected source states an implication-equivalent three-block threshold, but differently phrased extrapolated Gauss--Seidel analyses may contain equivalent special cases.

## References
1. Antonin Chambolle and Thomas Pock, *A remark on accelerated block coordinate descent for computing the proximity operators of a sum of convex functions*, Optimization Online 4719, first posted January 3, 2015; SMAI Journal of Computational Mathematics 1 (2015), 29--54, DOI 10.5802/smai-jcm.3.
2. Tao Hong and Irad Yavneh, *On Adapting Nesterov's Scheme to Accelerate Iterative Methods for Linear Problems*, arXiv:2102.09239, 2021.
3. Yassine Kamri, François Glineur, Julien M. Hendrickx, and Ion Necoara, *On the Worst-Case Analysis of Cyclic Block Coordinate Descent type Algorithms*, arXiv:2507.16675, 2025.
