# Sharp determinant-asymmetry threshold for an attracting four-cycle in the border-collision normal form

## Finding
Consider the continuous planar piecewise-affine map
\[
F(x,y)=\begin{cases}
(tx+y+1,ux),&x\le0,\\
(-rx+y+1,-vx),&x\ge0,
\end{cases}
\]
with fixed \(0<u,v<1\) and variable \(t>1-u\), \(r>1+v\). Both fixed points are saddles, and the branches fold into the same lower/upper orientation class. Call a periodic orbit a **strict \(LRRR\) four-cycle** if its successive first coordinates satisfy \(x_0<0<x_1,x_2,x_3\), and call it attracting if the four-step derivative has both eigenvalues strictly inside the unit disk.

**Theorem.** There are parameters \(t>1-u\) and \(r>1+v\) with an attracting strict \(LRRR\) four-cycle **if and only if** \(u>v\). In particular, the projection of the entire attracting-four-cycle region onto this natural unit determinant square is exactly \(\{(u,v):0<v<u<1\}\), an open triangle.

Moreover, for each \(0<v<u<1\), set
\[
r_0=1+v,\qquad t_0=\frac{(1+u)(1-v)}{1+v},\qquad D_0=2\bigl(1-uv^3-v(u-v)\bigr)>0.
\]
For all sufficiently small \(\varepsilon>0\), choosing \(r=r_0+\varepsilon\), \(t=t_0+\varepsilon\) gives an attracting strict \(LRRR\) cycle, with first coordinates asymptotic to
\[
 x_0=-\frac{2(1+v^2)}{D_0}\varepsilon+O(\varepsilon^2),\qquad
 x_2=\frac{r_0+t_0}{D_0}\varepsilon^2+O(\varepsilon^3),
\]
while \(x_1,x_3\longrightarrow(1+v)^{-1}\). Thus two distinct points of the attracting cycle approach the switching line at different **linear and quadratic** rates along this explicit boundary approach.

## Assumptions and scope
All parameters are real. The strict inequalities \(0<u,v<1\), \(r>1+v\), \(t>1-u\) are essential to the stated global necessity and sufficiency. The two branch Jacobians are
\[
A_L=\begin{pmatrix}t&1\\u&0\end{pmatrix},\qquad
A_R=\begin{pmatrix}-r&1\\-v&0\end{pmatrix}.
\]
Their determinants are \(-u\) and \(v\), respectively. The result concerns hyperbolic attraction of a specified symbolic periodic orbit, not global attraction, chaos, nor all periodic itineraries. Switching-line points themselves are excluded from the strict itinerary.

## Proof
Write \(\alpha=(1+u)(1-v)-rt\), \(M=A_R^3 A_L\), and \(T=\operatorname{tr}M\). Direct multiplication gives
\[
 T=-rt(r^2-2v)+(u-v)(r^2-v),\qquad \det M=-uv^3.
\]
The four-step affine branch composition has a unique fixed point whenever \(D=\det(I-M)=1-T-uv^3\ne0\). Its successive first coordinates \(x_0,x_1,x_2,x_3\), calculated by solving the affine fixed-point equations, obey the exact identities
\[
D x_0=-(r-v-1)\bigl(r^2+(v-1)^2\bigr),\qquad
D x_2=-(r-v-1)\alpha.
\]
These identities also follow by substituting the successive recurrences
\[
 x_1=t x_0-vx_3+1,\quad x_2=-r x_1+u x_0+1,\quad
 x_3=-r x_2-vx_1+1,\quad x_0=-r x_3-vx_2+1.
\]
The latter are valid for the indicated branch order and do not assume its admissibility beforehand.

**Necessity.** If the strict four-cycle attracts, its real two-by-two multiplier \(M\) is Schur stable. The elementary Schur criterion, together with \(0<uv^3<1\), implies
\[
-1+uv^3<T<1-uv^3,\quad D>0.
\]
Since \(r>1+v\) and the orbit's \(x_2>0\), the second exact coordinate identity forces \(\alpha<0\), equivalently \(rt>(1+u)(1-v)\). Using \(r^2-2v>0\), we get
\[
\begin{aligned}
T&<-(1+u)(1-v)(r^2-2v)+(u-v)(r^2-v)\\
 &=-(1-uv)r^2+2v(1+u)(1-v)-v(u-v)\\
 &<-(1-uv)(1+v)^2+2v(1+u)(1-v)-v(u-v)\\
 &=-1+uv^3+2v(u-v).
\end{aligned}
\]
The strict Schur lower bound forces \(2v(u-v)>0\), hence \(u>v\). This excludes **all** slopes in the two-saddle domain whenever \(u\le v\).

**Sufficiency and sharpness.** Suppose \(u>v\). Then \(t_0>1-u\), since
\[
 t_0-(1-u)=\frac{2(u-v)}{1+v}>0.
\]
At the boundary pair \((r,t)=(r_0,t_0)\), we have \(\alpha=0\) and
\[
 T_0=-1+uv^3+2v(u-v),\quad \det M_0=-uv^3.
\]
The lower Schur inequality holds because \(u>v\), and the upper one because
\[
 1-uv^3-T_0=2(1-uv^3-uv+v^2)>0;
\]
indeed \(1-uv^3-uv+v^2\ge(1-v)(1+v^2)>0\) as \(u<1\). Thus \(M_0\) is already strictly Schur stable, with \(D_0=1-T_0-uv^3>0\). At this pair the affine \(LRRR\) branch equations have \(x_0=x_2=0\) and \(x_1=x_3=(1+v)^{-1}\), although this boundary orbit does not have a strict symbolic itinerary.

Take \(r=r_0+\varepsilon\), \(t=t_0+\varepsilon\). For sufficiently small \(\varepsilon>0\), both two-saddle inequalities persist and Schur stability persists by continuity. Moreover
\[
 \alpha=-(r_0+t_0)\varepsilon-\varepsilon^2<0,
\]
so the two exact coordinate formulas give \(x_0<0<x_2\). Since the remaining first coordinates converge to the positive number \((1+v)^{-1}\), we also have \(x_1,x_3>0\). Hence this is a genuine attracting strict \(LRRR\) four-cycle (not a smaller-period orbit, since the itinerary has exactly one \(L\)). Expanding the exact coordinate formulas at \(\varepsilon=0\) and using \(D=D_0+O(\varepsilon)\) gives the asserted linear and quadratic grazing coefficients. This establishes both directions and the asymptotics.

## Verification
The complete symbolic identities for \(\operatorname{tr}M\), \(\det M\), \(D\), \(Dx_0\), \(Dx_2\), and the boundary trace have been independently expanded as multivariate integer polynomials by `verify.py` using only Python's standard library. The same program evaluates three exact-rational admissible attracting cycles and checks their four-step closure and Schur bounds. Run `python3 verify.py` in the folder containing this document and the program. These finite checks support the displayed algebra; the necessity and sufficiency for all parameters are established by the inequalities and continuity proof above, not by parameter sampling.

## Relationship to prior work
Ghosh, McLachlan, and Simpson (arXiv:2402.05393, first submitted February 8, 2024) introduce the same two-saddle border-collision family, identify the attracting \(LR\) region via their function \(\alpha\), and display an attracting \(LRRR\) region in their §9 and Figure 17. Their §4 renormalization provides general relations between the second iterate and a transformed family. The present result determines the **entire projection of existence of attracting strict \(LRRR\) cycles onto the pair of branch determinants** in the concrete unit-square mixed-sign regime; it also identifies a constructive, quantitatively anisotropic boundary emergence. Neither an existence-if-and-only-if determinant condition nor the two grazing coefficients was found in the inspected article. In fact, the necessity direction is compatible with the source's sufficient criteria and can also be inferred in part by combining its renormalization and trace inequalities; the significant added content is the global matching sufficiency and explicit degeneration rates.

Fatoyinbo and Simpson (arXiv:2210.14445, October 26, 2022) give a general noninvertible normal-form survey, numerical periodicity regions, and periodic-multiplier admissibility criteria, but do not identify this determinant-square projection or its boundary scaling. Ghosh, McLachlan, and Simpson (arXiv:2307.05144, July 11, 2023) prove robust-chaos conditions using trapping sets and expanding cones, rather than the existence projection of a stable four-cycle. Their results are not contradicted.

## Limitations
No assertion is made when either determinant magnitude is at least one, for border cases \(u=v\), or for other itineraries. The invariant polynomial identities have been verified, but no independent scientific audit has occurred. Priority claims are restricted to the literature and indexed mathematical records inspected; unavailable alternative formulations and unindexed results remain possible.

## References
1. I. Ghosh, R. I. McLachlan, D. J. W. Simpson, *The bifurcation structure within robust chaos for two-dimensional piecewise-linear maps*, arXiv:2402.05393 (first posted 2024-02-08), §4, §9 and Fig. 17. https://arxiv.org/abs/2402.05393
2. H. O. Fatoyinbo, D. J. W. Simpson, *A synopsis of the non-invertible, two-dimensional, border-collision normal form with applications to power converters*, arXiv:2210.14445 (2022), especially the periodic-orbit admissibility and stability discussion. https://arxiv.org/abs/2210.14445
3. I. Ghosh, R. I. McLachlan, D. J. W. Simpson, *Robust chaos in orientation-reversing and non-invertible two-dimensional piecewise-linear maps*, arXiv:2307.05144 (2023). https://arxiv.org/abs/2307.05144
