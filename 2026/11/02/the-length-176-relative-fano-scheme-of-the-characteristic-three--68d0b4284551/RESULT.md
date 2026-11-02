# The length-176 relative Fano scheme of the characteristic-three Dwork quartic pencil

## Finding

Let \(k\) be an algebraically closed field of characteristic \(3\). Consider the Dwork pencil of quartic surfaces
\[
X_\lambda=V(X^4+Y^4+Z^4+W^4+\lambda XYZW)\subset\mathbf P_k^3,
\qquad \lambda\in\mathbf A_k^1.
\]
Let \(\mathcal F\subset\operatorname{Gr}(2,4)\times\mathbf A_k^1\) be the relative Fano scheme of projective lines contained in the fibers \(X_\lambda\). Then \(\mathcal F\) is a finite, zero-dimensional scheme supported over \(\lambda=0\), with **exactly \(112\) geometric support points** and total scheme length \(176\). Its local Artin rings are
\[
\mathcal O_{\mathcal F,L}\cong
\begin{cases}
k,&\text{at \(48\) coordinate-pair lines},\\
k[\epsilon]/(\epsilon^2),&\text{at the other \(64\) lines}.
\end{cases}
\]
At the doubled points, the base parameter \(\lambda\) generates the maximal ideal, up to a unit. Consequently \(X_\lambda\) contains **no projective line for any \(\lambda\ne0\)**, even when the surface is singular. The special Fermat quartic \(X_0\) has \(112\) reduced lines in its individual Fano scheme; the extra length \(64\) is an infinitesimal *relative* deformation effect.

The coordinate-pair lines are those obtained, for a partition of the four coordinates into pairs \(\{i,j\}\) and \(\{r,s\}\), from
\[
X_i=\alpha X_j,\qquad X_r=\beta X_s,\qquad \alpha^4=\beta^4=-1.
\]
There are \(3\cdot4^2=48\) such lines. The remaining \(64\) lines are the diagonal fourth-root orbit of
\[
L_0:[s:t]\longmapsto[s:t:s+t:s-t].
\]

## Assumptions and scope

All lines, parameters, local rings, and counts are geometric over an algebraically closed field \(k\) of characteristic exactly \(3\). The relative Fano scheme is the closed zero locus of the universal restricted quartic, a section of \(\operatorname{Sym}^4\mathcal S^\vee\), on the Grassmannian \(\operatorname{Gr}(2,4)\) times the coefficient line. The count \(176\) is its total scheme length as a \(k\)-scheme, **not** the number of lines on a smooth individual surface. No assertion is made in another characteristic.

## Proof

**1. Every nonspecial fiber is line-free.** The equation is symmetric under all coordinate permutations. Every projective line has two independent coordinate functions, so after permuting coordinates it admits a unique expression on the open Grassmann chart
\[
[s:t]\longmapsto[s:t:as+ct:bs+dt].
\]
Expanding its quartic equation in characteristic \(3\), where \(\binom42=0\), gives precisely five equations:
\[
\begin{aligned}
A&=1+a^4+b^4=0,\\
B&=1+c^4+d^4=0,\\
C&=a^3c+b^3d+\lambda ab=0,\\
D&=ac^3+bd^3+\lambda cd=0,\\
E&=\lambda(ad+bc)=0.
\end{aligned}
\tag{1}
\]
For \(\lambda\ne0\), the final equation gives \(ad+bc=0\). If \(a=0\), the first equation makes \(b\ne0\), hence \(c=0\); then the second makes \(d\ne0\), contradicting \(C=0\). The case \(b=0\) is symmetric; if \(c=0\) or \(d=0\), the same equations give an immediate contradiction. Thus all four entries are nonzero. There exists \(u\ne0\) with \(c=ua\) and \(d=-ub\). Equations \(A=B=0\) imply \(u^4=1\). Substitution into \(C=D=0\) yields
\[
u(a^4-b^4)+\lambda ab=0,
\qquad
u(a^4-b^4)-\lambda ab=0.
\]
Since \(2\ne0\) in characteristic \(3\), this forces \(\lambda ab=0\), a contradiction. No line exists for nonzero \(\lambda\).

**2. The lines of the special fiber.** At \(\lambda=0\), the Fermat quartic is smooth because its four partial derivatives are the four coordinate cubes. For every line \(L\subset X_0\), the exact normal sequence gives \(N_{L/X_0}\cong\mathcal O_{\mathbf P^1}(-2)\); thus the *individual* Fano scheme has zero tangent space at every support point.

If at least one of \(a,b,c,d\) in (1) is zero, its equations force a diagonal or anti-diagonal nonzero matrix of remaining coordinate functions. Such lines are coordinate-pair lines, and all three coordinate partitions yield \(48\) different lines as described above. No coordinate function vanishes identically on a line: otherwise a smooth Fermat plane quartic would contain a line. If the first two coordinate functions are dependent, choose another independent pair and apply the same argument; this again produces a coordinate-pair line.

For a line not of coordinate-pair form, all \(a,b,c,d\) are nonzero. Put \(r=b/a\). Equations \(C=D=0\) give
\[
\frac cd=-r^3,\qquad \left(\frac cd\right)^3=-r,
\quad\text{so}\quad r^8=1.
\]
Since \(a^4(1+r^4)=-1\), necessarily \(r^4=1\), and then \(a^4=1\). From \(c=-d/r\) and \(B=0\), also \(d^4=1\). Conversely all triples \((a,d,r)\in\mu_4^3\) give lines via
\[
(a,b,c,d)=(a,ra,-d/r,d),
\]
and these are pairwise distinct. Thus there are exactly \(4^3=64\) additional lines, all on the chart and all satisfying \(ad+bc=0\). They are the orbit of \(L_0\) under diagonal fourth-root scalings. This proves that \(X_0\) has exactly \(48+64=112\) lines, each reduced in the individual Fano scheme.

**3. The completed local rings of the *relative* Fano scheme.** On each Grassmann chart, the differentials in the four Grassmann variables of \(A,B,C,D\) at \(\lambda=0\) are linearly independent. Indeed, the derivative of the Fermat quartic with respect to line deformations is a sum of a cube of a linear form times a linear form; its restriction has no \(s^2t^2\)-coefficient. On the other hand \(H^0(N_{L/X_0})=0\), so the full linearized restriction map is injective of rank \(4\). Its image is therefore precisely the four-dimensional space of quartics missing the mixed \(s^2t^2\) term. The formal implicit-function theorem eliminates the four line coordinates through \(A=B=C=D=0\) as unique power series in \(\lambda\); the remaining completed local equation is
\[
\lambda\,q(\lambda)=0,
\qquad q(\lambda)=a(\lambda)d(\lambda)+b(\lambda)c(\lambda).
\tag{2}
\]
At a coordinate-pair line, a chart can be chosen with \((a,b,c,d)=(\alpha,0,0,\beta)\) where \(\alpha^4=\beta^4=-1\). Then \(q(0)=\alpha\beta\ne0\), so (2) is a unit times \(\lambda\), yielding local ring \(k\).

At the representative \(L_0\), write \((a,b,c,d)=(1,1,1,-1)\). Solving the first derivatives of \(A=B=C=D=0\) at \(\lambda=0\) gives
\[
(a',b',c',d')=(-1,1,1,1).
\]
Therefore
\[
q(0)=0,\qquad q'(0)=a'd+ad'+b'c+bc'=4=1\in k.
\]
Equation (2) is a unit times \(\lambda^2\), so the completed local ring is \(k[[\lambda]]/(\lambda^2)\). Diagonal fourth-root scalings act transitively on the \(64\) non-coordinate-pair lines and carry \(\lambda\) to a nonzero scalar multiple of itself; the same local ring occurs at each. Since all these local rings are Artinian, the completions equal the local rings. Summing their lengths gives \(48+64\cdot2=176\).

**4. Singular fibers (context).** The surface \(X_\lambda\) is smooth exactly when \(\lambda^4\ne1\). For \(\lambda^4=1\), all singular coordinates are nonzero; in the affine chart \(X=1\), they satisfy \(Y^4=Z^4=W^4=1\) and \(\lambda YZW=-1\), giving exactly \(16\) points. At each, the Hessian in \((Y,Z,W)\) has zero diagonal and off-diagonal entries \(\lambda W,\lambda Z,\lambda Y\); its determinant is \(2\lambda^3YZW\ne0\). These are \(16\) ordinary double points. Step 1 still excludes lines on these singular fibers.

## Verification

Two pure-Python exact scripts accompany this proof. `verify_dwork.py` enumerates all \(7462\) lines of \(\mathbf P^3(\mathbf F_9)\) and evaluates the restricted quartic at five independent points of \(\mathbf P^1(\mathbf F_9)\); it gives \(112\) lines for \(\lambda=0\) and none for the other eight elements of \(\mathbf F_9\). `verify_local.py` checks the \(48\)/\(64\) orbit cardinalities and computes the exact first-order obstruction at \(L_0\), confirming order two. The proof above is over the entire algebraic closure and does not infer infinite statements from these finite tests.

Run from the directory containing the files with `python verify_dwork.py` and `python verify_local.py` (Python standard library only).

## Relationship to prior work

The quartic Dwork pencil and its role in mirror K3 geometry are standard; see Braeger--Malmendier--Sung, *Kummer sandwiches and Greene--Plesser construction*, first posted 14 December 2019, arXiv:1912.06951, especially Equation (1.1). The \(112\) lines on the characteristic-three Fermat quartic and broad line-count bounds are established in work of Rams--Schütt, Degtyarev, and Veniani. The result here concerns a different invariant: the full scheme-theoretic *relative* Fano scheme of this pencil, including its nonreduced infinitesimal points. In particular, the general numerical bounds and the characteristic-zero mirror construction do not give the exact \(48+64\) local-ring decomposition.

## Limitations

This concerns the specified coefficient-marked Dwork pencil, not all deformations of the Fermat quartic or all K3 quartics. The nonreduced length is the relative line Hilbert scheme over the parameter line; the Fano scheme of the Fermat fiber itself is reduced. The proof does not determine Hilbert schemes of conics, higher-degree rational curves, or analogous pencils in other characteristics. Literature searches cannot exclude an unindexed earlier identical calculation; no independent external mathematical validation is claimed.

## References

1. N. Braeger, A. Malmendier, Y. Sung, *Kummer sandwiches and Greene--Plesser construction*, arXiv:1912.06951 (first public version 2019-12-14), especially the Dwork equation in Section 1.
2. D. C. Veniani, *Lines on K3 quartic surfaces in characteristic 3*, arXiv:1608.04209; *Manuscripta Mathematica* 167 (2022), 675–701, first public preprint 2016-08-15.
3. S. Rams and M. Schütt, *112 lines on smooth quartic surfaces (characteristic 3)*, arXiv:1409.7485 (2014).
4. A. Degtyarev, *Lines in supersingular quartics*, *J. Math. Soc. Japan* 74 (2022), 973–1019, DOI:10.2969/jmsj/81998199.
