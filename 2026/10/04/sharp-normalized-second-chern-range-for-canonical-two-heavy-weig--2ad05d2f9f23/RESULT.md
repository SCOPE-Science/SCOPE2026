# Sharp normalized second-Chern range for canonical two-heavy weighted projective stacks
## Finding
For every integer \(r\ge2\) and every canonical coarse weighted projective space \(X=\mathbb P(1^r,a,b)\) with \(1\le a\le b\), let \(\mathcal X=\mathbb P(1^r,a,b)\) denote the corresponding smooth weighted projective stack of dimension \(n=r+1\). Define
\[
\rho(\mathcal X)=\frac{\int_{\mathcal X}c_2(T_{\mathcal X})c_1(T_{\mathcal X})^{n-2}}{\int_{\mathcal X}c_1(T_{\mathcal X})^n}.
\]
Then
\[
\frac{23r-1}{72r}\le \rho(\mathcal X)\le \frac{r+1}{2(r+2)}.
\]
The upper equality holds uniquely for \((a,b)=(1,1)\), and the lower equality holds uniquely for \((a,b)=(2r,3r)\).

Equivalently, for every such stack,
\[
\rho(\mathcal X)=\frac{\binom r2+r(a+b)+ab}{(r+a+b)^2}
=\frac12\left(1-\frac{r+a^2+b^2}{(r+a+b)^2}\right).
\]
Thus the standard projective-space point is the unique maximum of the normalized second-Chern ratio in this canonical family, while the opposite canonical corner \(\mathbb P(1^r,2r,3r)\) is the unique minimum.

## Assumptions and scope
Fix an algebraically closed field of characteristic zero. The coarse space is \(X=\operatorname{Proj} k[x_1,\ldots,x_r,y,z]\) with weights \((1^r,a,b)\), where \(r\ge2\) and \(1\le a\le b\). Canonical means canonical singularities of the coarse variety. The smooth weighted projective stack is
\[
\mathcal X=[(\mathbb A^{r+2}\setminus\{0\})/\mathbb G_m]
\]
for the same weights. The ratio \(\rho\) is a stack intersection number; the common factor \(\int_{\mathcal X}H^n\) cancels, so no normalization of that factor is needed.

## Proof
Write \(d=b-a\). First recover the exact canonical region without importing any earlier classification. A cyclic quotient chart of type \(\frac1m(1^r,q)\), with \(0\le q<m\), is canonical exactly when \(m\le r+q\). Indeed, the age of the \(k\)-th nonidentity element is
\[
\frac{rk+(kq\bmod m)}m.
\]
Necessity is the case \(k=1\). For sufficiency, write \(kq=tm+s\) with \(0\le s<m\). Because \(q<m\), one has \(t\le k-1\), and from \(r+q\ge m\),
\[
rk+s=k(r+q)-tm\ge(k-t)m\ge m.
\]
The two nontrivial affine charts of \(X\) are the heavy-coordinate quotient charts. The \(b\)-chart gives \(d\le r\). Under that condition, the \(a\)-chart is automatic when \(a\le d\), while for \(d<a\) it gives \(a\le r+d\). Hence
\[
X\text{ is canonical}\iff 0\le d\le r\quad\text{and}\quad 1\le a\le r+d.
\]

For the stack, the weighted Euler sequence
\[
0\longrightarrow\mathcal O\longrightarrow
\mathcal O(1)^{\oplus r}\oplus\mathcal O(a)\oplus\mathcal O(b)
\longrightarrow T_{\mathcal X}\longrightarrow0
\]
gives, with \(H=c_1(\mathcal O(1))\),
\[
c_1(T_{\mathcal X})=(r+a+b)H,
\qquad
c_2(T_{\mathcal X})=\left(\binom r2+r(a+b)+ab\right)H^2.
\]
After cancellation of \(\int_{\mathcal X}H^n\), this is the displayed formula for \(\rho\).

For the upper bound, apply Cauchy--Schwarz to the \(r+2\) weights \((1^r,a,b)\):
\[
(r+a+b)^2\le(r+2)(r+a^2+b^2).
\]
Substitution in the second formula for \(\rho\) yields
\[
\rho\le\frac{r+1}{2(r+2)}.
\]
Equality in Cauchy--Schwarz requires all weights to coincide, hence \(a=b=1\), and this pair is canonical.

For the lower bound it is enough to maximize
\[
q(a,d)=\frac{r+a^2+(a+d)^2}{(r+2a+d)^2}
\]
over the canonical region, since \(\rho=(1-q)/2\). For fixed \(d\),
\[
\frac{\partial q}{\partial a}=
\frac{2\bigl(r(2a+d-2)-d^2\bigr)}{(r+2a+d)^3}\ge0,
\]
because \(a\ge1\) and \(0\le d\le r\) imply \(r(2a+d-2)\ge rd\ge d^2\). Thus the maximum occurs on \(a=r+d\). There
\[
q(r+d,d)=\frac{5d^2+6dr+2r^2+r}{9(r+d)^2},
\]
and
\[
\frac{d}{dd}q(r+d,d)=\frac{2r(2d+r-1)}{9(r+d)^3}>0
\]
for \(r\ge2\). Hence \(d=r\), so uniquely \((a,b)=(2r,3r)\). At this pair
\[
q=\frac{13r+1}{36r},
\qquad
\rho=\frac{23r-1}{72r},
\]
which proves the lower bound and its equality statement.

## Verification
The standalone checker `artifacts/verify_c2_ratio.py` uses exact rational arithmetic. It independently evaluates every nonidentity Reid--Tai age in both heavy charts on a finite box for each \(2\le r\le25\), confirms the stated canonical-region criterion there, and then checks the exact ratio bounds and unique equality cases for every canonical pair in that box. It also checks the closed endpoint formulas for \(2\le r\le500\). These finite computations are regression checks only; the infinite theorem follows from the symbolic proof above.

## Relationship to prior work
Dolgachev's foundational treatment establishes weighted projective varieties as a basic algebraic-geometric class. Bahri--Franz--Ray study integral equivariant cohomology and give Chern-class formulas for weighted projective bundles. El Haloui records the weighted Euler sequence for the tangent sheaf of a weighted projective stack. Those ingredients provide the standard characteristic-class background. The sharp two-sided range above additionally imposes the exact canonical-singularity region for the two-heavy family and optimizes the normalized second-Chern ratio over that region. Searches for the formula, both equality cases, and equivalent Chern-ratio formulations did not locate this extremal statement in the inspected sources.

## Limitations
The result concerns only the family with exactly two non-unit weights and uses characteristic zero for the Reid--Tai argument. It is a statement about the smooth weighted projective stack attached to a canonical coarse space; it does not identify the stack Chern numbers with an arbitrary singular-coarse-space Chern theory. The literature comparison cannot exclude an uncatalogued or differently phrased prior statement.

## References
1. I. Dolgachev, *Weighted projective varieties*, in *Group Actions and Vector Fields*, Lecture Notes in Mathematics 956, Springer, 1982, pp. 34--71. DOI: 10.1007/BFb0101508.
2. A. Bahri, M. Franz, N. Ray, *The equivariant cohomology of weighted projective space*, arXiv:0708.1581; Math. Proc. Cambridge Philos. Soc. 146 (2009), 395--405.
3. K. El Haloui, *Ample tangent bundle on smooth projective stacks*, arXiv:1611.01809. In Theorem 13 the weighted Euler sequence is displayed.
