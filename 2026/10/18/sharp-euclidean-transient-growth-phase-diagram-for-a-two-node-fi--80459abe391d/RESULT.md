# Sharp Euclidean transient-growth phase diagram for a two-node finite-element heat semigroup

## Finding
For the standard consistent-mass piecewise-linear finite-element semidiscretization of the one-dimensional homogeneous Dirichlet heat equation on three successive element lengths \(u,1,v>0\), the semigroup is contractive in its physical mass norm for every mesh, but its **unweighted Euclidean nodal-coefficient norm** is contractive if and only if an explicit polynomial inequality holds. This is an exact classification of the first nontrivial spatial finite-element dimension. For the natural one-parameter meshes \((u,1,v)=(1,1,r)\), the Euclidean contractivity region is a single closed interval with two sharp algebraic boundaries, outside which strictly positive initial nodal data can undergo instantaneous norm growth. Moreover, as \(r\downarrow0\), the positive Euclidean numerical abscissa diverges as \(r^{-1}\) although the consistent mass matrix remains uniformly well conditioned.

Define
\[
\begin{aligned}
Q&=4uv+4u+4v+3,\\
X&=2uv+3u+2v+2,\\
Y&=2uv+2u+3v+2,\\
Z&=2u^2v+2uv^2+6uv+u+v,\\
\Delta&=4uvXY-Z^2.
\end{aligned}
\]
For every \(u,v>0\), the full semigroup satisfies \(\|e^{tA}\|_{2\to2}\le1\) for all \(t\ge0\) **if and only if** \(\Delta\ge0\). When \(\Delta<0\), a strictly positive vector \(x_0\) has \(\left.\frac{d}{dt}\|e^{tA}x_0\|_2^2\right|_{t=0}>0\).

For \(u=1,v=r\), set
\[
P(r)=4r^4-44r^3-79r^2-62r+1.
\]
This polynomial has exactly two positive simple roots \(r_-\in(0.01580,0.01582)\) and \(r_+\in(12.6570,12.6571)\). Euclidean contractivity holds precisely when \(r_-\le r\le r_+\); positive-data transient growth occurs precisely outside this interval. In the thin-right-element regime,
\[
\lim_{r\downarrow0}r\,\omega_2(A_r)
=\frac{3\sqrt{17}-12}{7}>0,
\quad
\sup_{0<r\le1}\kappa_2(M_r)
=\frac{3+\sqrt2}{3-\sqrt2}<2.8,
\]
where \(\omega_2(A)=\lambda_{\max}((A+A^\mathsf T)/2)\).

## Assumptions and scope
Consider \(\partial_t z=\partial_{xx}z\) on the interval partitioned by four nodes \(x_0<x_1<x_2<x_3\), with zero Dirichlet values at both endpoints. Let \(x_1-x_0=u\), \(x_2-x_1=1\), \(x_3-x_2=v\), and use the continuous piecewise-affine nodal basis with the **consistent** (not lumped) mass matrix. The two interior coefficients \(c(t)\in\mathbb R^2\) satisfy \(M\dot c=-Kc\), with
\[
M=\begin{pmatrix}(u+1)/3&1/6\\1/6&(v+1)/3\end{pmatrix},
\qquad
K=\begin{pmatrix}1+1/u&-1\\-1&1+1/v\end{pmatrix},
\qquad A=-M^{-1}K.
\]
All parameters and evolution times are real; \(u,v>0\), \(t\ge0\). The Euclidean vector norm is applied to the **nodal coefficients** rather than to the finite-element function in its physical \(L^2\) norm, which is \(\|c\|_M=(c^\mathsf TMc)^{1/2}\). No reaction, advection, forcing, or time integrator is included.

## Proof
**Positive definiteness and physical dissipation.** The assembly formulas give \(M\succ0\) and \(K\succ0\). Consequently, \(M^{-1/2}KM^{-1/2}\succ0\), and \(A\) is similar to the real symmetric negative-definite matrix \(-M^{-1/2}KM^{-1/2}\); in particular all eigenvalues of \(A\) are strictly negative. Along every nonzero solution,
\[
\frac{d}{dt}\|c(t)\|_M^2=-2c(t)^\mathsf TKc(t)<0.
\]
Direct multiplication of the two \(2\times2\) matrices shows that both off-diagonal entries of \(A\) are strictly positive, so \(e^{tA}\) is also entrywise nonnegative for \(t\ge0\).

**Exact Euclidean logarithmic norm.** Set
\[
H=-\frac{A+A^\mathsf T}{2}
=\frac{M^{-1}K+KM^{-1}}2.
\]
Straight two-by-two inversion, with the abbreviations above, gives the exact identity
\[
H=\frac{3}{uvQ}
\begin{pmatrix}2vX&-Z\\-Z&2uY\end{pmatrix},
\qquad
\det H=\frac{9\Delta}{u^2v^2Q^2}.
\]
All \(u,v,Q,X,Y,Z\) are strictly positive. Thus both diagonal entries of \(H\) are strictly positive, and Sylvester's criterion yields \(H\succeq0\) exactly when \(\Delta\ge0\). In finite-dimensional Euclidean space,
\[
\|e^{tA}\|_{2\to2}\le1\ \forall t\ge0
\iff\ \frac{A+A^\mathsf T}{2}\preceq0
\iff\ H\succeq0.
\]
The forward implication follows by differentiating the squared norm at zero in every direction, and the reverse implication follows by differentiating it along arbitrary trajectories. If \(\Delta<0\), then \(-H=(A+A^\mathsf T)/2\) has one strictly positive eigenvalue and positive off-diagonal entries. Its top eigenvector has strictly positive coordinates, so it is a positive-data witness of initial squared-norm growth.

**The exact three-element phase boundary.** Substituting \(u=1,v=r\) gives \(\Delta(1,r)=-P(r)\). The sequence of nonzero coefficients of \(P\) in descending degree is \((+,-,-,-,+)\), so Descartes' rule allows at most two positive real zeros, counting multiplicity. Exact rational evaluations show \(P(0.01580)>0>P(0.01582)\) and \(P(12.6570)<0<P(12.6571)\). The intermediate-value theorem therefore supplies two distinct positive zeros, which are the only positive zeros and are both simple. Since \(P(1)<0\), the complete sign profile implies \(P(r)\le0\) exactly on their closed interval. All claimed equivalences follow from the preceding criterion. With only one interior unknown the scalar generator is strictly negative, proving minimality in interior-node count.

**Unbounded initial growth with bounded mass conditioning.** Direct evaluation of the exact formula for \(H\) shows
\[
\lim_{r\downarrow0}rH_{1,r}
=\frac17\begin{pmatrix}0&-3\\-3&24\end{pmatrix}.
\]
The smaller eigenvalue of the right-hand matrix is \((12-3\sqrt{17})/7<0\), hence continuity of eigenvalues gives \(r\omega_2(A_r)\to(3\sqrt{17}-12)/7\). Meanwhile
\[
\lambda_\pm(M_r)=\frac{r+3\pm\sqrt{(r-1)^2+1}}6.
\]
For \(0<r\le1\), the numerator \(r+3\) increases and the radical decreases with \(r\), so \(\kappa_2(M_r)\) decreases and its supremum is the displayed \(r\downarrow0\) limit. Thus the exploding positive numerical abscissa is not caused by an ill-conditioned mass matrix. At the same time, the already-known mass-energy estimate and norm equivalence show \(\|e^{tA_r}\|_{2\to2}\le\sqrt{\kappa_2(M_r)}\le\sqrt{(3+\sqrt2)/(3-\sqrt2)}<1.67\) for every \(t\ge0\) and \(0<r\le1\): the divergence concerns **infinitesimal** Euclidean growth rate, not unbounded eventual amplification. As fully rational explicit witnesses, for \(r=1/100\) the positive vector \(c_0=(1,1/10)^\mathsf T\) satisfies \(c_0^\mathsf T(A+A^\mathsf T)c_0/2=453/295>0\); for \(r=20\), \(c_0=(1,3)^\mathsf T\) gives \(921/1670>0\).

## Verification
A standalone standard-library exact-rational checker in `verify.py` independently assembles both matrices from local element contributions and cross-checks the formula for \(H\), its determinant, mass and stiffness positive definiteness, positive generator off-diagonals, rational polynomial brackets, both explicit positive witnesses, and the small-element matrix limit. It reports **10,623 passed exact-rational checks**. These finite checks are reproducibility aids; the statements for all positive real parameters are justified by the algebraic and analytic proof above, not by finite enumeration. Run using `python3 verify.py` from this directory; no external libraries or input files are needed.

## Relationship to prior work
Tatsuoka, Miyatake and Sogabe (2026) motivate error control for exponentials of matrices from finite-element discretization. In their framework, conjugation by the square root of the mass matrix gives a negative numerical range for pure diffusion. The present result makes precise why the **untransformed coefficient-space numerical range** can behave differently, even for pure diffusion on the smallest nontrivial one-dimensional finite-element mesh. The new claims are the full three-element mesh phase criterion, the two exact one-parameter thresholds, positive-data witnesses, and the divergent numerical abscissa under uniformly bounded mass conditioning—not the known mass-energy identity or the generic logarithmic-norm contractivity equivalence.

For comparison, a published analysis of planar upper-triangular shear semigroups gives an exact \(\ell_p\) contractivity phase diagram for a different matrix class; an arbitrary similarity to triangular form does not preserve unweighted Euclidean operator norm and therefore does not supply the present finite-element mesh classification. Results about backward-Euler-filtered Crank–Nicolson positivity on uniform heat lattices instead address discrete time-stepping positivity, not untransformed coefficient semigroup contractivity.

## Limitations
The classification is for exactly two interior degrees of freedom, positive real element lengths, consistent piecewise-linear Galerkin mass and stiffness, and the unweighted Euclidean nodal-coefficient norm. It is not a failure of physical \(L^2\) energy stability, which always holds. No claim is made for arbitrary meshes, higher-order elements, mass lumping, reaction/advection problems, floating-point errors, matrix exponential approximants, runtime, or positive semigroup norm for all initial data (only entrywise semigroup positivity). The novelty comparison is best-knowledge bibliographic evidence, not a proof of uniqueness among all publications.

## References
1. S. Tatsuoka, Y. Miyatake and T. Sogabe, *An error control framework for computing the exponential of matrices arising from the finite element discretization*, arXiv:2603.11871v1, first posted March 12, 2026.
2. *Exact \(L^p\) contractivity phase diagram for planar triangular shears*, published mathematical research record dated October 11, 2026; comparison to its complete publicly available result.
3. *Unconditional lattice positivity from backward-Euler-filtered Crank–Nicolson*, published mathematical research record dated September 20, 2026; comparison by problem and claim scope.
