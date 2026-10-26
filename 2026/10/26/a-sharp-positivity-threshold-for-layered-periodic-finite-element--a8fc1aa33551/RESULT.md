# A sharp positivity threshold for layered periodic finite-element heat steps

## Finding
Consider a periodic one-dimensional heat equation with two alternating strictly positive diffusion coefficients. For every even number \(N=2m\ge6\) of equal-length cells, the fully discrete, consistent-mass, piecewise-linear finite-element backward-Euler matrix is entrywise nonnegative **if and only if** the time step is zero or exceeds one explicit threshold:
\[
 P_\tau=(M+\tau K)^{-1}M\ge0
 \quad\Longleftrightarrow\quad
 \tau=0\ \text{or}\ \tau\ge\frac{\ell^2}{6\min(a,b)}.
\]
Here inequalities between matrices mean entrywise inequalities. For strictly positive \(\tau\) below the threshold, at least one entry is **strictly negative**. The threshold depends only on the weaker of the two alternating diffusivities, not on their contrast or on the number of cells. The lower size restriction is meaningful: a four-node alternating example remains strictly positive below this threshold.

## Assumptions and scope
Let a periodic interval be partitioned into \(N=2m\ge6\) cells, with common cell length \(\ell>0\). Associate cell \([j,j+1]\) with a conductivity equal to \(a\) when \(j\) is even and \(b\) when \(j\) is odd, where \(a,b>0\). Use standard continuous piecewise-linear periodic basis functions, the **consistent** (not lumped) mass matrix \(M\), and the diffusion stiffness matrix \(K\). There is no source, reaction, boundary flux or mass-lumping modification. Indices are cyclic modulo \(N\). The coefficient vector \(u^{k+1}=P_\tau u^k\) is obtained by solving \((M+\tau K)u^{k+1}=Mu^k\); thus entrywise nonnegativity of \(P_\tau\) is equivalent to preservation of all nonnegative nodal coefficient vectors in one step. The diffusion equation is a periodic divergence-form heat equation, not a nodally sampled nondivergence equation.

In dimensionless form put \(\sigma=\tau/\ell^2\), \(M_0=M/\ell\) and \(K_0=\ell K\). Then \(P_\tau=(M_0+\sigma K_0)^{-1}M_0\). On each edge, the local contributions to \(M_0\) and \(M_0+\sigma K_0\) are respectively
\[
 \begin{pmatrix}1/3&1/6\\1/6&1/3\end{pmatrix},\qquad
 \begin{pmatrix}1/3+\sigma c&1/6-\sigma c\\1/6-\sigma c&1/3+\sigma c\end{pmatrix},
\]
where \(c\in\{a,b\}\) is that edge's diffusivity. This completely fixes the normalization.

## Proof
By interchanging the two cell types through a cyclic relabeling, assume \(a\le b\). Define
\[
 x=\frac16-\sigma a,\quad y=\frac16-\sigma b,\quad
 d=\frac23+\sigma(a+b)=1-x-y,\quad
 u=d^2-x^2-y^2,\quad v=xy.
\]
Group the even nodes first, followed by the odd nodes, with \(m\) of each. If \(S\) denotes the cyclic forward shift in the \(m\)-dimensional block, the dimensionless backward-Euler coefficient matrix and its even-even Schur resolvent are
\[
 A=\begin{pmatrix}dI&xI+yS^{-1}\\xI+yS&dI\end{pmatrix},\qquad
 R=[uI-v(S+S^{-1})]^{-1}.
\]
The matrix \(A=M_0+\sigma K_0\) is positive definite for all \(\sigma\ge0\), since \(M_0\) is positive definite and \(K_0\) is nonnegative definite. In the ranges used below, \(d>|x|+|y|\), so \(u>2|v|\). Direct block inversion and multiplication by the consistent mass matrix give the exact even-even and even-odd blocks of \(P_\tau\):
\[
 P_{EE}=R\left[\left(\frac{2d}{3}-\frac{x+y}{6}\right)I-\frac{x}{6}S-\frac{y}{6}S^{-1}\right],
 \qquad
 P_{EO}=\frac{\sigma}{6}R\left[(5a+b)I+(a+5b)S^{-1}\right].
\]

**Sufficiency.** Whenever \(\sigma\ge1/(6a)\), both \(x\le0\) and \(y\le0\). Then \(A\) is a symmetric positive-definite matrix with nonpositive off-diagonal entries. Its inverse is entrywise nonnegative, as can be seen by writing \(A=dI-B\), where \(B\ge0\) and \(\rho(B)<d\), and expanding the convergent geometric inverse series. Since \(M_0\ge0\), also \(P_\tau=A^{-1}M_0\ge0\). At \(\sigma=0\) we have \(P_\tau=I\).

**Necessity, when both neighboring entries are nonnegative.** Assume \(0<\sigma\le1/(6b)\), so \(x>0\) and \(y\ge0\). If \(y=0\), then \(R=u^{-1}I\), and \((P_{EE})_{0,1}=-x/(6u)<0\). If \(x,y>0\), the resolvent is entrywise strictly positive (a positive Neumann series). Write \(R_k=R_{0,k}\). Its first-row recurrence is
\[
 R_1=\frac{xy}{u}(R_0+R_2),
\]
where \(m\ge3\) ensures that the indicated off-diagonal recurrence has no coincident shift entries. Consequently,
\[
 6(P_{EE})_{0,1}
 = (4d-x-y)R_1-xR_0-yR_2
 = (Q-x)R_0+(Q-y)R_2,
 \quad Q=\frac{(4d-x-y)xy}{u}.
\]
The two coefficients are negative. Indeed, writing \(p=1/6-x=\sigma a>0\) and \(q=1/6-y=\sigma b>0\), direct expansion gives
\[
 u-(4d-x-y)y=\frac{42pq+5p+30q^2+19q}{6}>0,
 \quad
 u-(4d-x-y)x=\frac{42pq+19p+30p^2+5q}{6}>0.
\]
These imply \(Q<x\) and \(Q<y\), so \((P_{EE})_{0,1}<0\).

**Necessity, when the two neighboring off-diagonal coefficients have opposite signs.** It remains to take \(1/(6b)<\sigma<1/(6a)\), possible only for \(a<b\). Put \(Y=-y>0\); then \(0<x<1/6\), \(v=-xY<0\), \(d=1+Y-x\), and
\[
 u=1-2x+2Y-2xY,
 \qquad u-10xY=(1-2x)+(2-12x)Y>0.
\]
Define \(0<r<1\) as the unique root of \(r+r^{-1}=u/(xY)\) and write \(z=-r\). The cyclic resolvent has the explicit kernel
\[
 R_k=\frac{z^k+z^{m-k}}{\sqrt{u^2-4v^2}\,(1-z^m)},\qquad 0\le k<m.
\]
It follows directly that \(R_1<0\). For \(m=3\), \(R_2=R_1<0\); for every \(m\ge4\), \(R_2\ge0\) and
\[
 \frac{R_2}{|R_1|}\le\frac{2r}{1+r^2}
 =\frac{2xY}{u}<\frac15.
\]
To verify the bound: for even \(m\ge4\) the ratio equals \(r(1+r^{m-4})/(1+r^{m-2})\), which is at most \(2r/(1+r^2)\) by \((1-r^2)(1-r^{m-4})\ge0\). For odd \(m\ge5\) the ratio equals \(r(1-r^{m-4})/(1-r^{m-2})<r\). Thus, because \((a+5b)/(5a+b)<5\), the exact even-odd formula gives
\[
 (P_{EO})_{0,1}=\frac{\sigma}{6}\bigl[(5a+b)R_1+(a+5b)R_2\bigr]<0.
\]
In both regimes below \(1/(6a)\), we exhibited a specific negative matrix entry. Together with sufficiency and the zero-step identity, this proves the equivalence for every \(m\ge3\).

**Why four nodes are exceptional.** Let \(N=4\), \(a=1\), \(b=2\), \(\ell=1\), and \(\tau=1/8\). Exact inversion yields the first row
\[
 (P_\tau)_{0,:}=\frac1{4004}(2609,537,9,849).
\]
All rows of this circulant-by-two-periodic operator have strictly positive entries (the least is \(9/4004\)). Yet \(1/8<1/6\), so the \(m\ge3\) restriction cannot simply be discarded.

## Verification
The accompanying `verify.py` script uses Python's standard-library exact rational arithmetic to construct the mass and stiffness matrices, invert the full finite matrices by Gauss-Jordan elimination, and check row sums and sign predictions for \(116\) parameter/time-step combinations with \(m\in\{3,4,5,6\}\), plus the separate four-node exception. Execute `python verify.py` in a Python 3 environment. The output is `VERIFY_OK 116 six-or-more-node exact rational cases; four-node boundary witness`. These checks corroborate computations only; the universal result follows from the analytic resolvent identities and inequalities above, not from finite testing.

## Relationship to prior work
Li and Huang (first available preprint September 2012) established sufficient mesh-and-time-step conditions for a discrete maximum principle with consistent-mass linear finite elements and pointed out that mass lumping removes the lower time-step restriction. The present exact one-dimensional periodic, alternating-diffusivity characterization strengthens a sufficient Stieltjes-matrix criterion to **necessity** within this family. Schatz, Thomée and Wahlbin developed positivity and maximum-norm conditions for parabolic finite-element time stepping, including sufficient resolvent/Stieltjes criteria. Thomée and Wahlbin and Chatzipantelidis, Horváth and Thomée studied related positivity failures and reappearance; their stated problems and accessible descriptions do not establish this alternating-diffusivity if-and-only-if threshold. Related finite-step positivity statements on Markov generators and other time integrators do not imply a result for a consistent-mass generalized discretization.

## Limitations
The theorem concerns a one-dimensional, periodic, equal-cell partition and strictly alternating coefficients. It makes no statement about arbitrary nonperiodic geometries, higher spatial dimensions, graded cell lengths, reaction terms, nonuniform time steps, or lumped-mass schemes. Entrywise positivity of the finite-element **nodal propagator** is distinct from a pointwise maximum principle for all continuous initial profiles. The four-node example shows that the restriction on the number of cells is mathematically substantive. A relevant 2015 finite-element positivity paper could not be examined in full during the literature comparison; it remains a source of possible stronger prior coverage, so originality should be independently assessed.

## References
1. X. Li and W. Huang, “Maximum principle for the finite element solution of time dependent anisotropic diffusion problems,” arXiv:1209.5657, first submitted 25 September 2012; subsequently *Numerical Methods for Partial Differential Equations* 29 (2013), 1963–1985. https://arxiv.org/abs/1209.5657
2. A. H. Schatz, V. Thomée and L. B. Wahlbin, “On Positivity and Maximum-Norm Contractivity in Time Stepping Methods for Parabolic Equations,” *Computational Methods in Applied Mathematics* 10 (2010). DOI: 10.2478/cmam-2010-0025.
3. V. Thomée and L. B. Wahlbin, “On the existence of maximum principles in parabolic finite element equations,” *Mathematics of Computation* 77 (2008). DOI: 10.1090/S0025-5718-07-02021-2.
4. P. Chatzipantelidis, Z. Horváth and V. Thomée, “On Preservation of Positivity in Some Finite Element Methods for the Heat Equation,” *Computational Methods in Applied Mathematics* 15 (2015), 417–437. DOI: 10.1515/cmam-2015-0018.
