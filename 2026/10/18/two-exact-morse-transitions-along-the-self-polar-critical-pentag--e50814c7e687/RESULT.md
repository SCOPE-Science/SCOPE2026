# Two exact Morse transitions along the self-polar critical-pentagon curve

## Finding

The projectively critical pentagons introduced by Balacheff, Solanes, and Tzanev have **exactly two** interior quadratic-degeneracy parameters. Between them, the Santaló-optimized volume product has a strict local maximum on the two-dimensional projective deformation space modulo affine transformations; outside them it has a nondegenerate saddle. Equivalently, the unreduced four-dimensional projective Hessian has Morse index two in the central interval and index one in both flanking intervals.

Here are exact transition parameters:
\[
\beta_y=\sqrt{u_*},\quad 16u_*^4-90u_*^3+9u_*^2+20u_*+4=0,\quad u_*\in(1/2,1),
\]
\[
\beta_x=\sqrt{(5+3\sqrt{17})/16},\qquad
1/\sqrt2<\beta_y<1<\beta_x<\sqrt2.
\]
The root \(u_*\) is uniquely characterized by its displayed interval (indeed it is the only root in \((1/2,2)\)). Numerically, \(\beta_y\approx0.7956936349\) and \(\beta_x\approx1.0419128106\).

For \(b\in(1/\sqrt2,\sqrt2)\), write \(q=q(b)\) for the unique root in \((-1/\sqrt2,1/\sqrt2)\) of
\[
F=bq^3-(b^2+1)q^2+(2b^5+b)q+3b^4-1=0,
\]
and put \(r=\sqrt{1+q^2}\), \(c=(1+bq)/r\). Let \(P_b\subset\mathbb R^2\) be the convex hull of the cyclically listed points
\[
(-1/b,0),\quad(q,-r),\quad(b,-c),\quad(b,c),\quad(q,r).
\]
At every such \(b\), \(P_b\) is a strictly convex, centroid-zero pentagon with \(P_b^\circ=-P_b\). Consequently it is critical for the projective volume-product functional. With \(\mathcal F_b(x,\xi)=\mathcal P(((P_b^\circ+\xi)^\circ)+x)\) and \(\mathcal P(K)=\operatorname{area}(K)\operatorname{area}(K^\circ)\), the full Hessian at the origin has the following inertia:

* \(1/\sqrt2<b<\beta_y\): three positive eigenvalues, one negative eigenvalue;
* \(\beta_y<b<\beta_x\): two positive eigenvalues, two negative eigenvalues;
* \(\beta_x<b<\sqrt2\): three positive eigenvalues, one negative eigenvalue;
* \(b=\beta_y\) or \(b=\beta_x\): two positive eigenvalues, one negative eigenvalue, one zero eigenvalue.

For the smooth, locally Santaló-optimized function \(\xi\mapsto\min_x\mathcal F_b(x,\xi)\), the Hessian is negative definite precisely when \(\beta_y<b<\beta_x\), making the origin a **strict local maximum** in that interval. It is indefinite in both open flanking intervals. At either transition the quadratic test is inconclusive in its one null direction: no higher-order extremality is claimed there.

## Assumptions and scope

Use Euclidean Lebesgue area and standard polarity \(K^\circ=\{z:\langle z,y\rangle\le1\ \forall y\in K\}\). A project's non-affine deformation is parametrized near the identity by \(\xi\); independent translations are parametrized by \(x\). Both are restricted to sufficiently small neighborhoods where the indicated polarities exist. The centered minimum is taken over translations local to zero; since the translation Hessian is positive definite, this minimum is smooth and unique locally. The signs, indices and local maximality statements concern this two-parameter projective family, **not** all convex bodies or a global Mahler-product bound. Endpoints \(b=1/\sqrt2\) and \(b=\sqrt2\) are excluded. Morse index counts strictly negative eigenvalues; nullity counts zero eigenvalues.

## Proof

**1. Existence, geometry, and centering.** Put \(t=\sqrt2b\in(1,2)\). Direct substitutions yield
\[
F(-1/\sqrt2,t/\sqrt2)=-\frac{(t-2)(t+1)(t^3-2t^2-3)}4<0,
\]
\[
F(1/\sqrt2,t/\sqrt2)=\frac{(t-1)(t+2)(t^3+2t^2+3)}4>0.
\]
The discriminant of the quadratic \(F_q=3bq^2-2(b^2+1)q+2b^5+b\) is \(4(-6b^6+b^4-b^2+1)<0\): writing \(u=b^2\in(1/2,2)\), the expression \(-6u^3+u^2-u+1\) is strictly decreasing and vanishes at \(u=1/2\). Since \(3b>0\), \(F_q>0\) and there is exactly one smooth root \(q(b)\) in the stated interval.

The five consecutive oriented edge determinants are positive. In particular, the distinct vertex turns have positive numerators proportional to \(q+1/b\), \((b-q)^2/(br)\), and \(2c(b-q)\), all positive on this parameter interval (and their reflected turns agree). A direct global supporting-line check is also available: for all vertex pairs, \(1+\langle p_i,p_j\rangle\ge0\). The only potentially nonobvious positive numerators reduce to \(b-q>0\), \(1+bq>0\), and \(1+b^2-c^2=(b-q)^2/(1+q^2)>0\). Consequently every vertex lies in each claimed half-space. The supporting point dual to each successive edge equals the negative of one of its vertices, in the order \((-p_3,-p_4,-p_0,-p_1,-p_2)\); hence \(P_b^\circ=-P_b\). Reflection in the horizontal axis makes its vertical first moment zero. The shoelace first horizontal moment equals \(F(q,b)/(3b^2r)=0\). Thus its centroid is the origin, and the projective first-variation formula in [1] gives criticality.

**2. Exact area and moments.** Set
\[
D_1=r/b,\qquad D_2=br-qc,\qquad D_3=bc.
\]
The area and the two unnormalized diagonal second moments are, by the shoelace and polygon-moment identities,
\[
A=D_1+D_2+D_3,
\]
\[
I_{xx}=\frac{D_1(b^{-2}-q/b+q^2)+D_2(q^2+qb+b^2)+3b^2D_3}{6},
\]
\[
I_{yy}=\frac{D_1r^2+D_2(r^2+rc+c^2)+D_3c^2}{6}.
\]
The mixed second central moment vanishes by horizontal reflection. Hence the covariance matrix is \(C=\operatorname{diag}(I_{xx}/A,I_{yy}/A)\). Each diagonal entry is strictly positive.

**3. Projective Hessian and its Santaló reduction.** The two-variable second-variation identity of [1], specialized to the centered self-polar planar body, is
\[
\nabla^2\mathcal F_b(0,0)=3\mathcal P(P_b)
\begin{pmatrix}4C&-I_2\\-I_2&4C\end{pmatrix}.
\]
In the two orthogonal coordinate directions the matrix splits into blocks \(3\mathcal P(P_b)\begin{pmatrix}4\lambda&-1\\-1&4\lambda\end{pmatrix}\), where \(\lambda=I_{xx}/A\) or \(I_{yy}/A\). Its eigenvalues are proportional to \(4\lambda+1>0\) and \(4\lambda-1\). Thus the Morse index is precisely the number of negative members of \(4I_{xx}-A\) and \(4I_{yy}-A\). In the translation variable \(x\), the leading Hessian block is positive definite. The implicit function theorem gives a unique smooth local minimizing translation for each small \(\xi\); the reduced Hessian is its Schur complement, a positive scalar times \(4C-(4C)^{-1}\). Its inertia agrees with that of the two numbers \(4I_{xx}-A\), \(4I_{yy}-A\). A negative definite reduced Hessian proves strict local maximality by the second-derivative test.

**4. Algebraic detection of all transitions.** Write
\[
G_x=3b^3r(4I_{xx}-A),\qquad G_y=3br^3(4I_{yy}-A).
\]
The multipliers are positive. Direct expansion shows that these are polynomials in \(b,q\); the accompanying symbolic checker provides the explicit expansions and independently reconstructs them from the displayed polygon moments. Their exact eliminants are
\[
\operatorname{Res}_q(F,G_x)
=-b^6(b^2-2)(2b^2-1)^3(b^2+1)^6(8b^4-5b^2-4),
\]
\[
\operatorname{Res}_q(F,G_y)
=-b^2(b^2-2)(2b^2-1)^2(b^2+1)^8
(16b^8-90b^6+9b^4+20b^2+4).
\]
Since \(1/2<b^2<2\), the only candidates for the zero of \(G_x\) and \(G_y\) are the respective roots of \(X(u)=8u^2-5u-4\) and \(Y(u)=16u^4-90u^3+9u^2+20u+4\). The first has exactly one root in \((1/2,2)\), namely \((5+3\sqrt{17})/16\). For the second, \(Y''(u)=192u^2-540u+18<0\) throughout \([1/2,2]\), as this convex quadratic is negative at both endpoints; also \(Y'(1/2)=-61/2<0\). Thus \(Y\) strictly decreases there, with \(Y(1/2)=6>0\) and \(Y(2)=-384<0\). It has exactly one root \(u_*\in(1/2,2)\). Note that a resultant root is initially only a *possible* simultaneous root on the physical branch; existence of the relevant crossings is certified by the sign changes next.

**5. Certified signs and ordering.** At the rational test values \(b=3/4,1,5/4\), the unique physical root \(q\) lies respectively in the rational intervals
\[
(438/10000,439/10000),\quad(-4780/10000,-4779/10000),\quad(-6597/10000,-6596/10000).
\]
Exact rational interval Horner evaluations, reproduced by `check_phase.py`, prove that \(F\) changes from negative to positive across each interval and that the \((G_x,G_y)\) signs are respectively \((- , +)\), \((-,-)\), and \((+,-)\) on each interval. The elimination identities and uniqueness of each eligible root forbid any other transition. Consequently \(G_y\) crosses exactly once between \(3/4\) and \(1\), while \(G_x\) crosses exactly once between \(1\) and \(5/4\). Their crossings occur precisely at the algebraic candidates \(\beta_y,\beta_x\), with \(\beta_y<\beta_x\); the sign patterns, Hessian index and reduced-maximality conclusions follow. At each threshold exactly one factor vanishes while the other remains strictly negative, so nullity is one. This proves all stated assertions.

## Verification

Run `python check_phase.py` with Python 3 and SymPy. The code independently checks the centroid and polar identities, all area and second-moment formulas, exact factorization of both resultants, uniqueness of eligible transition roots, and *rational arithmetic* certificates for all sign samples. Its final message is `PASS`. The proof of transition uniqueness is algebraic; no finite sampling is used to infer an absence of other roots. Numerical parameter values are illustrations only.

## Relationship to prior work

The polygon family, projective criticality, and general Hessian formula are due to Balacheff–Solanes–Tzanev [1]. Their treatment includes a numerical one-parameter exploration and a saddle-point construction; these are not claimed as new here. Klartag [2] supplied the general projective second-variation perspective. The present result adds an exact exhaustive classification of Hessian signature, two sharp algebraic thresholds, and the interval of strict Santaló-optimized projective local maxima; none is obtained just from the general Hessian identity without evaluating the pentagon-specific moment inequalities and their global zero sets.

## Limitations

The assertion is local within the smooth projective deformation family modulo affine transformations, not a global extremal characterization among arbitrary planar convex bodies. At the two degenerate parameters the sign of the first nonzero higher-order term is not established. The classification uses the original first-version parametrization of [1]; the later journal publication may contain elaborations that require separate bibliographic comparison. Independent validation has not been performed.

## References

[1] F. Balacheff, G. Solanes, K. Tzanev, *Projective transformations of convex bodies and volume product*, arXiv:2303.17794v1 (first public 2023-03-31); subsequently *International Mathematics Research Notices* (2024), DOI 10.1093/imrn/rnad310. https://arxiv.org/abs/2303.17794

[2] B. Klartag, *Isotropic constants and Mahler volumes*, arXiv:1710.08084v2 (2018). https://arxiv.org/abs/1710.08084
