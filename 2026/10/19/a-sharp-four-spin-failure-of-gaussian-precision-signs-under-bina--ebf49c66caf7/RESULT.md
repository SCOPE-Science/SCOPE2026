# A sharp four-spin failure of Gaussian precision signs under binary total positivity

## Finding

**Theorem (dimension threshold and curvature sign rule).** Let \(B=(B_1,\ldots,B_d)\) be a strictly positive binary law on \(\{0,1\}^d\) that is multivariate totally positive of order two (MTP2): for all configurations \(x,y\), \(p(x\wedge y)p(x\vee y)\ge p(x)p(y)\). Its covariance matrix \(\Sigma\) is positive definite. If \(d\le3\), every off-diagonal entry of \(\Sigma^{-1}\) is nonpositive.

This dimension bound is sharp even among ferromagnetic pairwise Ising laws. For \(X,Y,Z,W\in\{0,1\}\), consider

\[
 p(x,y,z,w)=\frac{a^x b^y u^z v^w r^{x(z+w)}s^{y(z+w)}t^{zw}}{\mathcal Z},
 \qquad a,b,u,v>0,\quad r,s>1,\quad t\ge1.
\]

Here \(\mathcal Z\) is the sum of the displayed numerator over all sixteen binary configurations. This law is strictly positive and MTP2, and \(X\) and \(Y\) are conditionally independent given \((Z,W)\). Let \(K=\Sigma^{-1}\), with coordinates ordered \((X,Y,Z,W)\). Then

\[
\operatorname{sign}K_{XY}=-\operatorname{sign}\big[(1-ar)(1-bs)\big].
\]

Thus the entry is positive exactly when one of \(ar,bs\) is below one and the other is above one; it is zero on the two exact transition hypersurfaces and negative when both lie on the same strict side of one. This sign classification is independent of \(u,v,t\). In particular, \(a=1/8\), \(b=2\), \(r=s=2\), \(u=v=t=1\) gives \(K_{XY}=235/60966>0\) and \(\operatorname{Cov}(X,Y)=304/55225>0\).

## Assumptions and scope

A strictly positive binary law assigns positive mass to every vertex of its binary cube. For any nonzero linear functional of the coordinates, its variance is strictly positive because that functional cannot be constant over all vertices. Thus all covariance inverses and Schur complements below exist. An MTP2 law is one satisfying the displayed lattice inequality, also known as the FKG lattice condition. A partial correlation here is *linear*, obtained by least-squares projection on the listed coordinates; it is not conditional correlation at a fixed configuration of the conditioning coordinates. The conclusion concerns ordinary covariance matrices, not conditional precision matrices.

## Proof

**1. Three coordinates cannot exhibit a positive off-diagonal inverse-covariance entry.** For two Bernoulli variables \(X,Y\), MTP2 implies \(\operatorname{Cov}(X,Y)\ge0\), so the off-diagonal of their inverse covariance is nonpositive. With three Bernoulli variables \((X,Y,Z)\), all conditional \((X,Y)\) distributions at each fixed \(Z\) are MTP2 and hence have nonnegative covariance. Since \(Z\) is binary, both conditional means \(\mathbb E[X\mid Z]\) and \(\mathbb E[Y\mid Z]\) are affine functions of \(Z\). Consequently, the law of total covariance gives the *linear regression residual* covariance

\[
 \operatorname{Cov}(X,Y)-\frac{\operatorname{Cov}(X,Z)\operatorname{Cov}(Y,Z)}{\operatorname{Var}(Z)}
 =\mathbb E[\operatorname{Cov}(X,Y\mid Z)]\ge0.
\]

The two-variable Schur complement is positive definite. Inverting it shows that the \((X,Y)\) entry of the full inverse covariance equals minus this residual covariance divided by the positive Schur-complement determinant. The same argument works for any chosen pair. This proves the assertion for \(d\le3\).

**2. Four-coordinate model and conditional means.** The log of its unnormalized probability is a sum of arbitrary one-spin fields, four pair interactions with coefficients \(\log r,\log s>0\), and one nonnegative pair interaction \(\log t\). Its pairwise lattice cross-differences are nonnegative, so it is MTP2. The absence of an \(xy\) term gives \(X\perp Y\mid (Z,W)\). Their conditional means are the logistic functions

\[
 f_{a,r}(k)=\frac{ar^k}{1+ar^k},\qquad
 f_{b,s}(k)=\frac{bs^k}{1+bs^k},\qquad k=z+w\in\{0,1,2\}.
\]

Every function of two binary variables has an exact multilinear expansion. Thus

\[
 \mathbb E[X\mid Z,W]=c_X+d_X(Z+W)+\delta_X ZW,
 \qquad
 \delta_X=f_{a,r}(2)-2f_{a,r}(1)+f_{a,r}(0),
\]

and likewise for \(Y\). Direct common-denominator simplification yields

\[
 \delta_X=\frac{a(r-1)^2(1-ar)}{(1+a)(1+ar)(1+ar^2)},\qquad
 \delta_Y=\frac{b(s-1)^2(1-bs)}{(1+b)(1+bs)(1+bs^2)}.
\]

**3. Exact linear partial covariance.** Let \(H=ZW-\operatorname{Proj}_{\operatorname{span}(1,Z,W)}(ZW)\), where the projection is in \(L^2\) of the underlying law. Let \(q_{zw}=\Pr(Z=z,W=w)\), which is positive at all four cells. Then \(H\not\equiv0\) and

\[
 V_H:=\mathbb E H^2
 =\left(\frac1{q_{00}}+\frac1{q_{01}}+\frac1{q_{10}}+\frac1{q_{11}}\right)^{-1}>0.
\]

To verify the equality, a mean-zero function orthogonal to \(Z\) and \(W\) has values proportional to \((1/q_{00},-1/q_{01},-1/q_{10},1/q_{11})\) on the four cells. Matching its discrete mixed difference to that of \(ZW\), namely one, gives the displayed proportionality factor and squared norm. The marginal weights themselves are explicitly

\[
 q_{zw}=\frac{u^zv^wt^{zw}(1+ar^{z+w})(1+bs^{z+w})}{\mathcal Z}.
\]

Write \(S\) for the \(2\times2\) Schur complement of the \((Z,W)\) covariance block in \(\Sigma\). Its off-diagonal entry is the covariance of the least-squares residuals from projecting \(X,Y\) onto \(\operatorname{span}(1,Z,W)\). Centered conditional noises \(X-\mathbb E[X\mid Z,W]\) and \(Y-\mathbb E[Y\mid Z,W]\) have zero conditional covariance, because \(X\perp Y\mid(Z,W)\), and are orthogonal to all functions of \((Z,W)\). The two residuals therefore share only their \(\delta_XH\) and \(\delta_YH\) pieces:

\[
 S_{XY}=\delta_X\delta_YV_H,
 \qquad K_{XY}=-\frac{\delta_X\delta_YV_H}{\det S}.
\]

As \(S\) is positive definite, its determinant and \(V_H\) are strictly positive. The sign is exactly the negative of the sign of \((1-ar)(1-bs)\), including its zero cases.

**4. Rational witness.** At \(a=1/8,b=2,r=s=2,u=v=t=1\), direct summation over the sixteen atoms yields

\[
 \mathcal Z=235/8,\qquad
 \Sigma=\frac1{55225}
 \begin{pmatrix}
 10384&304&1488&1488\\
 304&7954&1308&1308\\
 1488&1308&12166&416\\
 1488&1308&416&12166
 \end{pmatrix},\qquad K_{XY}=\frac{235}{60966}.
\]

All four crossed interactions are attractive (strictly positive log-coupling), despite the strictly positive off-diagonal inverse-covariance entry. This completes the dimension-sharp demonstration.

## Verification

Run the standalone file `verify_ferromagnetic_precision.py` with Python 3 and SymPy installed. It checks the exact logistic second-difference identity symbolically; enumerates all sixteen atoms for the rational witness; tests the MTP2 lattice inequalities with fixed remaining spins; computes exact covariance and its inverse; confirms the Schur-complement identity, the sign transition, and the exact witness \(235/60966\). It also tests thirty-six other rational parameter choices. These finite tests do not establish the universal dimension-three or all-parameter statements; those follow from the preceding proof.

## Relationship to prior work

The original theory of MTP2/association and the Gaussian inverse-covariance M-matrix equivalence are established in Karlin and Rinott (1980, 1983). Slawski and Hein (2014) study the Gaussian M-matrix estimation problem. Fallat et al. (arXiv:1510.01290, first posted October 5, 2015) analyze binary MTP2, positive log-linear interactions, graphical conditional independence, and Gaussian precision; its Section 4.2 and Sections 6–7 distinguish discrete graphical independence from Gaussian precision restrictions. The exact curvature sign rule above pertains instead to *ordinary linear partial correlations of a non-Gaussian binary pairwise Ising law*. Baba, Shibata, and Sibuya (2004) study the general gap between partial and conditional correlation, but their accessible abstract does not settle the specific sharp four-spin sign classification. The algebraic equivalence to logistic discrete curvature was checked against those formulations, not merely against titles.

## Limitations

The classification is for the indicated positive four-spin subfamily and for the stated \(X,Y\) precision entry. It does not classify every entry or every four-spin MTP2 law. Historical priority has not been independently certified; the general distinction between nonlinear conditional independence and linear partial correlation predates this result. An earlier implicit derivation from broader graphical-model formulas cannot be ruled out. No inference about Gaussian laws or nonbinary variables is intended. The computational verifier gives corroboration, not an infinite proof.

## References

1. S. Fallat, S. Lauritzen, K. Sadeghi, C. Uhler, N. Wermuth, P. Zwiernik. *Total positivity in Markov structures*. arXiv:1510.01290 (first posted 2015-10-05), later Annals of Statistics 45 (2017), 1152–1184.
2. S. Karlin and Y. Rinott. *Classes of orderings of measures and related correlation inequalities. I. Multivariate totally positive distributions*. Journal of Multivariate Analysis 10 (1980), 467–498.
3. S. Karlin and Y. Rinott. *M-Matrices as covariance matrices of multinormal distributions*. Linear Algebra and its Applications 52–53 (1983), 419–438.
4. M. Slawski and M. Hein. *Estimation of positive definite M-matrices and structure learning for attractive Gaussian Markov random fields*. arXiv:1404.6640 (2014).
5. K. Baba, R. Shibata, and M. Sibuya. *Partial correlation and conditional correlation as measures of conditional independence*. Australian & New Zealand Journal of Statistics 46 (2004), 657–664.
