# Universal John ellipsoids of homothetic frusta and a sharp contact transition

## Finding

For every integer \(d\ge3\), every full-dimensional compact convex body \(B\subset\mathbb R^{d-1}\), and every \(0\le q\le1\), the unique maximum-volume ellipsoid of the homothetic frustum
\[
K_q(B)=\{(x,z):0\le z\le1,\ x\in[1-(1-q)z]B\}
\]
is explicitly determined by the John ellipsoid of \(B\). In affine coordinates in which that base John ellipsoid is the unit Euclidean ball, write
\[
q_0=\frac{d-1}{d+1},\quad a^2=\max\{q,q_0\},\quad
b=\begin{cases}\frac1{(d+1)(1-q)},&0\le q\le q_0,\\\frac12,&q_0\le q\le1.\end{cases}
\]
The frustum's unique John ellipsoid is exactly
\[
J(K_q(B))=\left\{(x,z):\frac{\|x\|^2}{a^2}+\frac{(z-b)^2}{b^2}\le1\right\}.
\]
The upper cap is untouched when \(q<q_0\), first touched when \(q=q_0\), and touched for every \(q>q_0\). The lower cap and lateral boundary are touched throughout.

Writing \(\kappa_j\) for the volume of the unit \(j\)-ball, the exact inscribed-ellipsoid volume fraction factorizes as
\[
\frac{|J(K_q(B))|}{|K_q(B)|}=\frac{|J(B)|}{|B|}\frac{\kappa_d}{\kappa_{d-1}}F_d(q),
\qquad F_d(q)=\frac{d a^{d-1}b}{\sum_{j=0}^{d-1}q^j}.
\]
The scalar \(F_d(q)\) is strictly increasing on \([0,1]\) and satisfies
\[
F_d(0)=\frac{d}{d+1}\left(\frac{d-1}{d+1}\right)^{(d-1)/2},
\qquad F_d(1)=\frac12.
\]
In particular, the shape-dependent factor \(|J(B)|/|B|\) separates completely from a universal truncation law.

## Assumptions and scope

A convex body is compact, convex and has nonempty interior. The base \(B\) may be asymmetric, nonsmooth or a polytope. The family has precisely homothetic parallel sections with common affine center; the top and bottom planes are distinct, normalized here to height one. For arbitrary \(B\), let \(T\) be an invertible affine map of the transverse space taking \(J(B)\) to the unit ball, and shear the ambient space to center that unit ball at the transverse origin. The displayed normal-form ellipsoid pulls back under this transformation; volumes and John ellipsoids are affine equivariant. The limiting \(q=0\) is a cone with one vertex; \(q=1\) is a prism.

## Proof

**Base normalization and containment.** Normalize \(J(B)=B_2^{d-1}\). Thus \(B_2^{d-1}\subset B\), and John's characterization supplies finitely many unit vectors \(\xi_i\in\partial B\cap S^{d-2}\) and positive weights \(w_i\) satisfying
\[
\sum_iw_i\xi_i=0,\quad \sum_iw_i\xi_i\xi_i^\mathsf T=I_{d-1},\quad \sum_iw_i=d-1.
\]
Each tangent hyperplane \(\langle\xi_i,x\rangle=1\) supports \(B\). Hence \(\langle\xi_i,x\rangle+(1-q)z\le1\) supports \(K_q(B)\).

Put \(m=1-q\). In both branches \(0<b\le\tfrac12\) and \(a^2=1-2mb\). An ellipsoid point at \(z=b(1+v)\), \(-1\le v\le1\), satisfies \(\|x\|\le a\sqrt{1-v^2}\). By Cauchy--Schwarz,
\[
a\sqrt{1-v^2}+mbv\le\sqrt{a^2+(mb)^2}=1-mb,
\]
so \(\|x\|\le1-mb(1+v)=1-mz\). Because \((1-mz)B_2^{d-1}\subseteq(1-mz)B\), the entire proposed ellipsoid lies in \(K_q(B)\). Its lowest point lies at \(z=0\); its highest point is \(z=2b\le1\).

**A complete John certificate.** Define \(y=mb/(1-mb)\). One checks \(0\le y\le1/d\), with \(y=1/d\) exactly for \(q\le q_0\). Upon sending the proposed ellipsoid to the unit \(d\)-ball, every support contact above \(\xi_i\) becomes
\[
U_i=(\sqrt{1-y^2}\,\xi_i,y)\in S^{d-1}.
\]
The bottom axial pole \(U_-=(0,-1)\) also contacts. At \(b=1/2\), the top axial pole \(U_+=(0,1)\) contacts. The lateral points really are boundary contacts because \(a\sqrt{1-y^2}+mb(1+y)=1\), and the supporting normal is proportional to \((\xi_i,m)\).

Assign total probability masses
\[
\lambda=\frac{d-1}{d(1-y^2)},\qquad
\alpha=\frac{1-dy}{2d(1-y)},\qquad
\beta=\frac{1+dy}{2d(1+y)}
\]
to the lateral contacts, top pole and bottom pole, respectively; distribute the lateral mass as \(\lambda w_i/(d-1)\). The three masses are nonnegative. When the top pole is not a boundary contact, \(\alpha=0\). Direct rational identities give
\[
\lambda+\alpha+\beta=1,\quad
\lambda y+\alpha-\beta=0,\quad
\lambda y^2+\alpha+\beta=\frac1d,\quad
\frac{\lambda(1-y^2)}{d-1}=\frac1d.
\]
The first and second moments of this finite contact measure are therefore \(0\) and \(I_d/d\). Multiplying the masses by \(d\) gives John's necessary-and-sufficient decomposition for the full, unrestricted ellipsoid problem. Uniqueness follows from uniqueness of the maximum-volume inscribed ellipsoid. No rotational symmetry of \(B\) was used.

**Sharp transition.** Since \(2b<1\) when \(q<q_0\) and \(2b=1\) when \(q\ge q_0\), the top-face contact begins exactly at \(q_0\); at equality the top contact has zero weight in this particular certificate. Conversely, the candidate's only possible points at the cap planes are its poles, so the stated contact classification is exact.

**Volumes and strict monotonicity.** Integrating the homothetic transverse slices gives
\[
|K_q(B)|=\frac{|B|}{d}\sum_{j=0}^{d-1}q^j.
\]
In the chosen normalization \(|J(B)|=\kappa_{d-1}\), while the ellipsoid has volume \(\kappa_d a^{d-1}b\). This yields the factorization. For \(q\le q_0\),
\[
F_d(q)=\frac{d}{d+1}\frac{q_0^{(d-1)/2}}{1-q^d},
\]
which is strictly increasing. For \(q\ge q_0\),
\[
F_d(q)=\frac{d}{2\sum_{j=0}^{d-1}q^{j-(d-1)/2}}.
\]
On \((0,1)\), pair the exponents \(j-(d-1)/2\) and their negatives. Every nonconstant pair is \(2\cosh(c|\log q|)\), strictly decreasing as \(q\) increases toward one. Consequently the displayed reciprocal is strictly increasing for \(q_0\le q\le1\). The two branches agree at \(q_0\); their endpoint evaluations are as stated.

## Verification

The included standalone `check.py` uses exact rational arithmetic to verify all four John mass identities and the sharp contact transition for dimensions three through ten at boundary and interior rational values. It also checks normalized tangential triangular, quadrilateral and heptagonal bases in dimension three, numerically optimizes a separately parametrized ellipsoid under its containment constraints, and checks the volume-ratio profile. All checks passed. These are diagnostics; the mathematical proof above establishes the theorem for every allowable dimension, base and truncation ratio.

## Relationship to prior work

John's classical contact-decomposition theorem supplies the sufficiency criterion, and modern generalizations discuss optimal ellipsoid conditions in much wider settings [1,2]. Mordhorst treats a specially selected simplex frustum in a study of extremal affine invariant points [3, §6.2]. That example and the classical prism/cone endpoint geometries are compatible with, but do not assert, the arbitrary-base full-parameter classification and strict frustum-efficiency law derived here. Literature comparisons remain subject to historical-priority uncertainty.

## Limitations

The family requires *homothetic* parallel sections, not arbitrary morphing convex sections. The statement concerns exact John ellipsoids and exact geometric volumes; it does not derive a stability theorem for perturbed nonhomothetic frusta. Historical priority is not independently certified.

## References

[1] P. M. Gruber and F. E. Schuster, *An arithmetic proof of John's ellipsoid theorem*, arXiv:1207.7246 (2012).

[2] G. Ivanov and M. Naszódi, *Functional John and Löwner conditions for pairs of log-concave functions*, arXiv:2212.11781, first public December 22, 2022, MSC2020 52A23.

[3] O. Mordhorst, *New results on affine invariant points*, arXiv:1509.06023, especially §6.2 (2015–2016).
