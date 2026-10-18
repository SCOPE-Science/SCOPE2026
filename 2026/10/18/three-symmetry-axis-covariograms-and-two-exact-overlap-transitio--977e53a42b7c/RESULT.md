# Three symmetry-axis covariograms and two exact overlap transitions for the rhombic dodecahedron

## Finding

Let \(K\subset\mathbb R^3\) be the regular rhombic dodecahedron
\[
K=\{(x,y,z): |x|+|y|\le1,\ |x|+|z|\le1,\ |y|+|z|\le1\},
\]
of volume \(2\). Write \(g(h)=\operatorname{Vol}_3(K\cap(K+h))\) for its covariogram. Three inequivalent crystallographic directions have *exact* complete profiles. For \(t\ge0\),
\[
\begin{aligned}
 A(t)&:=g(t,0,0)=\begin{cases}2-2t+t^3/3,&0\le t\le1,\\(2-t)^3/3,&1\le t\le2,\\0,&t\ge2,\end{cases}\\
 F(t)&:=g(t,t,0)=\begin{cases}(1-t)(2-t),&0\le t\le1,\\0,&t\ge1,\end{cases}\\
 D(t)&:=g(t,t,t)=\begin{cases}2-3t,&0\le t\le1/2,\\4(1-t)^3,&1/2\le t\le1,\\0,&t\ge1.\end{cases}
\end{aligned}
\]
Here \(A\) is a fourfold vertex-axis profile, \(F\) is a twofold facet-normal profile, and \(D\) is a threefold vertex-axis profile. The internal positive break at \(t=1\) makes \(A\) exactly \(C^2\) but not \(C^3\); that of \(D\) at \(t=1/2\) makes \(D\) exactly \(C^1\) but not \(C^2\).

For fixed *Euclidean* translation distance \(0<r<2\), compare just these three symmetry-axis orbits, not all possible directions:
\[
\mathcal A(r)=A(r),\quad \mathcal F(r)=F(r/\sqrt2),\quad
\mathcal D(r)=D(r/\sqrt3).
\]
Let
\[
\alpha=3\sqrt2-2\sqrt3=0.778539071981\ldots,
\]
and let \(\beta\in(1,\sqrt2)\) be the unique root in that interval of
\[
2r^3-9r^2+(24-9\sqrt2)r-4=0,\qquad
\beta=1.213144601953\ldots.
\]
Then \(\mathcal D\) uniquely maximizes the overlap among these three axes on \((0,\alpha)\), \(\mathcal F\) uniquely maximizes on \((\alpha,\beta)\), and \(\mathcal A\) uniquely maximizes on \((\beta,2)\). At the first boundary precisely \(\mathcal D=\mathcal F>\mathcal A\), and at the second precisely \(\mathcal F=\mathcal A>\mathcal D\). Thus **both transitions are genuine two-way ties; no orbit is skipped and no triple tie occurs for positive overlap**.

## Assumptions and scope

The containing solid is fixed exactly by the inequalities above; no additional scaling or rotations of one copy are allowed. The second solid is translated but not rotated. The covariogram is a three-dimensional Lebesgue volume, and the three ray parameters are *not* equal Euclidean distances: the directions have lengths \(1,\sqrt2,\sqrt3\) per unit \(t\), respectively. All formulas include endpoints; for fixed distance the strict comparison is asserted only for \(0<r<2\). At \(r=0\) the values all equal \(2\), and at \(r\ge2\) all vanish. The comparison theorem makes no assertion that one of the three crystallographic axes maximizes the covariogram *over every spatial direction*.

## Proof

**1. Coordinate-axis profile.** At fixed \((y,z)\) with \(|y|+|z|\le1\), the admissible \(x\)-fiber is \([-a,a]\), where \(a=1-\max\{|y|,|z|\}\). The overlap of this fiber with its translate by \(t\) has length \((2a-t)_+\). In the first-quadrant triangle \(y,z\ge0\), \(y+z\le1\), set \(m=\max(y,z)\). The distribution area is
\[
H(u)=\operatorname{area}\{(y,z):y,z\ge0,\ y+z\le1,\ m\le u\}
=\begin{cases}u^2,&0\le u\le1/2,\\1/2-(1-u)^2,&1/2\le u\le1.\end{cases}
\]
Differentiating the absolutely continuous fiber integral yields \(A'(t)=-4H(1-t/2)\) for \(0<t<2\). Hence \(A'(t)=-2+t^2\) for \(0<t<1\) and \(A'(t)=-(2-t)^2\) for \(1<t<2\). Since \(A(0)=\operatorname{Vol}(K)=2\), integration proves \(A\) on the entire nonnegative ray. At \(t=1\), the two second derivatives agree (both equal \(2\)) but the third derivatives are respectively \(2\) and \(-2\). In particular the break is \(C^2\), not \(C^3\).

**2. Facet-normal profile.** Make the linear change \(u=(x+y)/2\), \(v=(x-y)/2\). Then \(dx\,dy\,dz=2\,du\,dv\,dz\), and the pair-sum inequalities are equivalent to
\[
|u|\le1/2,\quad |v|\le1/2,\quad |u|+|v|+|z|\le1.
\]
For fixed \((v,z)\), the \(u\)-fiber has half-length \(m=\min(1/2,1-|v|-|z|)\). Translation by \((t,t,0)\) shifts \(u\) by \(t\), and therefore
\[
F(t)=8\int_0^{1/2}\int_0^{1-v}(2m-t)_+\,dz\,dv.
\]
For \(0\le t\le1\), split the inner integral at \(z=1/2-v\) and \(z=1-v-t/2\). Its value is
\[
\int_0^{1-v}(2m-t)_+\,dz
=(1/2-v)(1-t)+(1-t)^2/4.
\]
Consequently
\[
F(t)=8\left[(1-t)/8+(1-t)^2/8\right]=(1-t)(2-t).
\]
For \(t\ge1\), every \(u\)-fiber has diameter at most \(1\), so the overlap vanishes.

**3. Threefold-axis profile.** Put \(u=x-y\), \(v=x-z\), \(w=x\); the absolute Jacobian is \(1\). By \(|p|+|q|=\max(|p+q|,|p-q|)\), the three inequalities describe \(w\) constrained by three unit-length intervals whose centers are \(u/2\), \(v/2\), and \((u+v)/2\), plus the difference constraints
\[
\rho(u,v):=\max(|u|,|v|,|u-v|)\le1.
\]
The intersection of the intervals has length \(\ell=1-\rho/2\). For clarity, their centers have range \(\rho/2\), as follows from \(\max(u,v,u+v)-\min(u,v,u+v)=\rho\). A translation by \((t,t,t)\) changes only \(w\), hence the fiber overlap length is \((1-\rho/2-t)_+\). The centrally symmetric hexagon \(\{\rho\le s\}\) has area \(3s^2\), so integrating against its radial shell density \(6s\) gives
\[
D(t)=6\int_0^1 s(1-s/2-t)_+\,ds.
\]
When \(t\le1/2\), the upper endpoint is \(1\), giving \(2-3t\); when \(1/2\le t\le1\), it is \(2(1-t)\), giving \(4(1-t)^3\). The overlap is zero for \(t\ge1\). The second derivatives at the positive internal breakpoint \(t=1/2\) are \(0\) from the left and \(12\) from the right, proving the differentiability assertion.

**4. First transition and the dominance of the threefold axis.** For \(0<r\le\sqrt3/2\), substitution into the ray formulas gives
\[
\mathcal D(r)-\mathcal F(r)=\frac r2(3\sqrt2-2\sqrt3-r)=\frac r2(\alpha-r).
\]
In addition, for \(0<r\le\alpha<\sqrt3/2\),
\[
\mathcal D(r)-\mathcal A(r)=r(2-\sqrt3-r^2/3)>0,
\]
since \(3(2-\sqrt3)-\alpha^2=3(4\sqrt6-8-\sqrt3)>0\); the last inequality follows, for example, by squaring positive sides twice. Therefore the threefold axis is strictly best until \(\alpha\), and precisely the threefold and twofold axes tie at \(\alpha\).

**5. Twofold dominance and second transition.** For \(\alpha\le r\le1\),
\[
\mathcal F(r)-\mathcal A(r)
=r\left(2-\frac3{\sqrt2}+\frac r2-\frac{r^2}{3}\right).
\]
The bracket is concave and is strictly positive at both endpoints: at \(\alpha\) it is positive by Step 4, and at \(1\) it equals \(13/6-3/\sqrt2>0\). On \(1\le r\le\sqrt2\), set
\[
E(r)=\mathcal F(r)-\mathcal A(r)
=2-\frac{3r}{\sqrt2}+\frac{r^2}{2}-\frac{(2-r)^3}{3}.
\]
Its derivative \(4-3/\sqrt2-3r+r^2\) is negative at \(r=1\) and decreases throughout \([1,\sqrt2]\). Moreover \(E(1)>0\) whereas \(E(\sqrt2)<0\). Thus \(E\) has a unique root \(\beta\in(1,\sqrt2)\); multiplying its equation by \(6\) gives the cubic in the finding. The twofold axis strictly exceeds the fourfold axis before \(\beta\), and the reverse holds afterward.

It remains to exclude the threefold axis on \((\alpha,2)\). On \((\alpha,\sqrt3/2]\), the explicit difference in Step 4 is negative, so \(\mathcal F>\mathcal D\). On \([\sqrt3/2,\beta]\), the difference \(\mathcal F-\mathcal D\) has second derivative \(-7+8r/\sqrt3<0\), because \(r\le\beta<\sqrt2<7\sqrt3/8\). It is positive at \(r=\sqrt3/2\), where it equals \((15-6\sqrt6)/8>0\). It is also positive at \(\beta\), as shown next; strict concavity makes it positive throughout.

For \(1\le r<\sqrt3\), compare the cubic branches
\[
\mathcal A(r)=\frac{(2-r)^3}{3},\qquad
\mathcal D(r)=4(1-r/\sqrt3)^3.
\]
The positive quotient \((2-r)/(1-r/\sqrt3)\) increases strictly with \(r\), its derivative being \((2/\sqrt3-1)/(1-r/\sqrt3)^2>0\). At \(r=1\), \(\mathcal A(1)=1/3>4(1-1/\sqrt3)^3=\mathcal D(1)\), since \(40\sqrt3>69\). Hence \(\mathcal A>\mathcal D\) for \(1\le r<\sqrt3\), including \(r=\beta\). For \(\sqrt3\le r<2\), \(\mathcal D=0<\mathcal A\). Therefore the previous concavity argument implies \(\mathcal F>\mathcal D\) all the way from \(\alpha\) to \(\beta\), while \(\mathcal A>\mathcal D\) afterward. This gives both strict regimes and both exact two-orbit ties, completing the proof.

## Verification

The proof is analytical and covers every real parameter in the indicated intervals. The accompanying `verify.py` constructs the actual intersection of the 12 halfspaces defining \(K\) with their translated counterparts, computes its three-dimensional volume by convex hull, and compares it with the fiber-derived formulas at independent sample points. It also numerically checks the sharp crossing parameters and the ordering on representative distances. Reproduce using `python3 verify.py` with NumPy and SciPy. Finite numerical checks are corroboration, *not* proof of continuous assertions, uniqueness of roots, or historical priority.

## Relationship to prior work

Averkov–Bianchi, *Retrieving convex bodies from restricted covariogram functions* (arXiv:math/0702892), studies which restricted covariogram data determine a convex body. Bianchi, *The covariogram determines three-dimensional convex polytopes* (arXiv:0805.1605), proves a uniqueness theorem and examines singular structures of covariograms. Neither result computes these three rhombic-dodecahedral directional overlap polynomials or the fixed-distance two-transition comparison. A published *complete translation-distance phase diagram for hypercube covariograms* gives a qualitatively analogous optimization for cubes; its proof relies on Cartesian product factorization, which this solid lacks, and the published statement does not imply the three formulas here. The statements and proof are intentionally limited to the three symmetry-axis orbits. The general covariogram concept, reconstruction theorems, and generic piecewise-polynomial phenomena are not claimed as new.

## Limitations

This is not the unrestricted angular maximum of the covariogram. It does not classify every translation of fixed Euclidean length, arbitrary orientations of the two copies, or other lattice cells. The historical search does not exclude all unindexed crystallographic autocorrelation and diffraction tables, or equivalent piecewise-polynomial spline formulas; priority therefore merits independent inspection. No claim of independent certification is made here.

## References

1. G. Averkov and G. Bianchi, *Retrieving convex bodies from restricted covariogram functions*, arXiv:math/0702892, v1 submitted 2007-02-28 (https://arxiv.org/abs/math/0702892).
2. G. Bianchi, *The covariogram determines three-dimensional convex polytopes*, arXiv:0805.1605, v1 submitted 2008-05-12; *Advances in Mathematics* 220 (2009), 1771–1808 (https://arxiv.org/abs/0805.1605).
3. *A complete translation-distance phase diagram for hypercube covariograms*, publicly indexed geometric research record, October 2026 (https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-complete-translation-distance-phase-diagram-for-hypercube-cova--5fadf7c81348).
