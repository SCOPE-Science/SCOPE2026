# Exact positivity threshold on a four-node alternating periodic finite-element mesh

## Finding

For the unit-diffusivity heat equation on a periodic one-dimensional mesh with four nodes and alternating positive cell lengths \(a,b,a,b\), use continuous piecewise-linear finite elements with the consistent mass matrix and one backward-Euler step of size \(\tau\ge0\). The nodal transition matrix \(P_\tau=(M+\tau K)^{-1}M\) is entrywise nonnegative if and only if

\[
\tau=0\quad\text{or}\quad \tau\ge \tau_*(a,b):=\frac{\sqrt{a^2b^2+2ab(a+b)^2}-ab}{12}.
\]

This is an exact necessary-and-sufficient threshold for this four-node periodic mesh; it is not a claim about arbitrary nonuniform meshes or larger periodic meshes.

## Assumptions and scope

The domain is a circle partitioned into four consecutive edges of lengths \(a,b,a,b\), with \(a,b>0\). The heat equation is \(u_t=u_{xx}\); \(\tau\) is the time-step size. Let \(M\) and \(K\) be the standard assembled consistent mass and stiffness matrices for the continuous piecewise-linear nodal basis. Then \(M\) is positive definite and \(K\) is positive semidefinite, so \(M+\tau K\) is invertible for every \(\tau\ge0\).

## Proof

In node order \(0,1,2,3\), with edge lengths \(a,b,a,b\), the assembled matrices are

\[
M=\frac16\begin{pmatrix}
2(a+b)&a&0&b\\
a&2(a+b)&b&0\\
0&b&2(a+b)&a\\
b&0&a&2(a+b)
\end{pmatrix},
\qquad
K=\begin{pmatrix}
a^{-1}+b^{-1}&-a^{-1}&0&-b^{-1}\\
-a^{-1}&a^{-1}+b^{-1}&-b^{-1}&0\\
0&-b^{-1}&a^{-1}+b^{-1}&-a^{-1}\\
-b^{-1}&0&-a^{-1}&a^{-1}+b^{-1}
\end{pmatrix}.
\]

Put \(A_\tau=M+\tau K\) and

\[
D_\tau=(ab+12\tau)(a^2+3ab+12\tau)(3ab+b^2+12\tau)>0.
\]

Direct multiplication verifies \(A_\tau P_\tau=M\) for the following entries. All four diagonal entries equal \(N_d/D_\tau\), where

\[
\begin{aligned}
N_d={}&3a^4b^2+10a^3b^3+3a^2b^4\\
&+36a^3b\tau+144a^2b^2\tau+36ab^3\tau\\
&+72(a^2+b^2)\tau^2+504ab\tau^2+432\tau^3>0.
\end{aligned}
\]

The two edge classes have entries \(P_{01}=P_{23}=N_a/D_\tau\) and \(P_{03}=P_{12}=N_b/D_\tau\), where

\[
\begin{aligned}
N_a&=6\tau\bigl(a^3b+5a^2b^2+2ab^3+36ab\tau+12b^2\tau+72\tau^2\bigr),\\
N_b&=6\tau\bigl(2a^3b+5a^2b^2+ab^3+12a^2\tau+36ab\tau+72\tau^2\bigr).
\end{aligned}
\]
For \(\tau>0\), both are strictly positive. The remaining off-diagonal class consists of the two opposite-node entries:

\[
P_{02}=P_{13}=\frac{6\tau q(\tau)}{D_\tau},\qquad
q(\tau)=72\tau^2+12ab\tau-ab(a+b)^2.
\]

The matrix is symmetric in this four-node case, so these classes account for every entry. At \(\tau=0\), \(P_0=I\). For \(\tau>0\), the diagonal and edge entries are positive, so entrywise nonnegativity is equivalent to \(q(\tau)\ge0\). Since

\[
q(0)=-ab(a+b)^2<0,\qquad q'(\tau)=144\tau+12ab>0\quad(\tau\ge0),
\]
\(q\) has exactly one positive root. Solving \(q(\tau)=0\) gives the stated \(\tau_*(a,b)\), proving both necessity and sufficiency.

The threshold recovers the uniform case: if \(a=b=h\), then \(\tau_*(h,h)=h^2/6\). It is strictly smaller than the usual sufficient bound \(\max(a^2,b^2)/6\) whenever \(a\ne b\). For example, if \(a\ge b\), then

\[
q(a^2/6)=a(a-b)(a+b)(2a+b)>0\quad\text{when }a>b,
\]
so the unique positive root lies below \(a^2/6\); the case \(b>a\) follows by symmetry. The usual sufficient bound \(\tau\ge\max(a^2,b^2)/6\) makes both off-diagonal entries \(a/6-\tau/a\) and \(b/6-\tau/b\) of \(A_\tau\) nonpositive. Since \(A_\tau\) is positive definite, it is then a nonsingular M-matrix, so \(A_\tau^{-1}\ge0\) and \(P_\tau=A_\tau^{-1}M\ge0\). The exact formula shows that this sufficient condition is not necessary when \(a\ne b\). With \(r=b/a\to0^+\),

\[
\frac{\tau_*(a,b)}{a^2}=\frac{\sqrt{r^2+2r(1+r)^2}-r}{12}\sim\frac{\sqrt{2r}}{12}\to0.
\]
Thus strong cell-length contrast can make the exact four-node threshold arbitrarily smaller than the maximum-cell sufficient bound. This comparison is a consequence of the proved formula, not a numerical extrapolation.

## Verification

The proof uses the assembled matrices and exact rational-function identities above. Each factor in \(D_\tau\) is positive for \(a,b>0\) and \(\tau\ge0\); the signs of all entries are therefore fully determined by the displayed numerators. The unique-root argument establishes the threshold for all real parameters in the stated domain. The accompanying `verify.py` checks the matrix identities using exact rational arithmetic at representative parameter values only; those spot checks are supplementary and are not used as a proof for all parameters.

## Relationship to prior work

Chatzipantelidis, Horváth, and Thomée studied positivity preservation for piecewise-linear finite-element approximations of the heat equation, including standard Galerkin, lumped-mass, and finite-volume-element methods. The accessible abstract describes homogeneous Dirichlet boundary conditions, unlike the periodic four-node problem here. Jin, Lazarov, Thomée, and Zhou developed general nonnegativity-preservation results and timestep bounds for finite-element approximations of subdiffusion, with the heat equation as a limiting/special case. The inspected material motivates the threshold question but does not state the exact formula above for this alternating periodic mesh. The full text of the closest 2015 heat-equation article was not accessible during this run, so no claim is made that the inaccessible text omits every related special case.

## Limitations

The theorem concerns only four periodic nodes, the alternating edge pattern \(a,b,a,b\), continuous piecewise-linear elements, the consistent mass matrix, unit diffusivity, and a single backward-Euler step. It does not classify six or more nodes, arbitrary nonuniform meshes, other time integrators, mass lumping, or nonperiodic boundary conditions. The full text of the closest heat-equation paper could not be inspected; that literature-overlap risk remains open.

## References

1. P. Chatzipantelidis, Z. Horváth, and V. Thomée, “On Preservation of Positivity in Some Finite Element Methods for the Heat Equation,” *Computational Methods in Applied Mathematics* 15(4) (2015), 417–437. DOI: 10.1515/cmam-2015-0018. Publisher metadata records online publication on 4 August 2015.
2. B. Jin, R. Lazarov, V. Thomée, and Z. Zhou, “On Nonnegativity Preservation in Finite Element Methods for Subdiffusion Equations,” arXiv:1510.02825 (2015); *Mathematics of Computation* 86 (2017), 2239–2260.
