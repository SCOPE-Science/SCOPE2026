# Exact integer Fourier support of the type-\(A_3\) root polytope

## Finding

Let \(P=\operatorname{conv}\{e_i-e_j:1\le i\ne j\le4\}\subset\mathbb R^4\), with \(e_i\) the coordinate unit vectors. This three-dimensional root polytope is a cuboctahedron. Write \(x_4=-x_1-x_2-x_3\) and equip \(P\) with the lattice-coordinate volume \(d\mu=d\mathcal H^3/2=dx_1\,dx_2\,dx_3\). For any \(k=(k_1,k_2,k_3)\in\mathbb Z^3\), put
\[
C(k)=\int_P e^{-2\pi i(k_1x_1+k_2x_2+k_3x_3)}\,d\mu(x).
\]
Let \(M_k\) denote the multiset \(\{0,k_1,k_2,k_3\}\). The coefficient \(C(k)\) is nonzero **if and only if** \(M_k\) has a repeated value. More precisely, \(C(0,0,0)=10/3\). For \(k\ne0\), its value is completely determined by the multiplicity pattern of \(M_k\):

* Four distinct values: \(C(k)=0\).
* Exactly one double value \(r\), with distinct remaining values \(s,t\): \(C(k)=-1/[2\pi^2(s-r)(t-r)]\).
* Two double values \(r,s\): \(C(k)=-1/[\pi^2(s-r)^2]\).
* One triple value \(r\) and a singleton \(s\): \(C(k)=1/[2\pi^2(s-r)^2]\).

Consequently, for **every** integer \(N\ge0\), the number of nonzero integer Fourier coefficients in the symmetric frequency cube is exactly
\[
\#\{k\in\mathbb Z^3:|k_j|\le N\ (1\le j\le3),\ C(k)\ne0\}=24N^2+2N+1.
\]
Thus the integer-frequency Fourier support of this lattice root polytope has exact quadratic rather than cubic growth.

A stronger geometric identity underlies the result. If \(Q\subset\mathbb R^3\) is the projection of \(P\) to its first three coordinates and \(W(y)=\sum_{m\in\mathbb Z^3}\mathbf1_Q(y+m)\), then for almost every \(y\in[0,1]^3\), with \(t=y_1+y_2+y_3\),
\[
W(y)=3+\mathbf1_{\{t<1\}}+\mathbf1_{\{t>2\}}.
\]
In particular, the lattice translates cover the cube with multiplicity three on its middle diagonal slab and multiplicity four on its two corner simplices.

## Assumptions and scope

All coordinates and frequencies are defined in the fixed root-lattice basis \(e_1-e_4,e_2-e_4,e_3-e_4\). Accordingly, \(d\mu=d\mathcal H^3/2\), not unnormalized ambient three-dimensional Hausdorff measure. Equivalently, \(Q\) has vertices the first-three-coordinate projections of the twelve roots \(e_i-e_j\). There are no restrictions on the signs or magnitudes of the integer frequencies and no generic-position assumption. Membership and periodicity identities are understood almost everywhere, so boundary counting conventions do not affect Fourier integrals.

## Proof

**1. Polytope description.** In the hyperplane \(\sum_{i=1}^4x_i=0\), the convex hull of all \(e_i-e_j\) is exactly
\[
P=\left\{x:\sum_{i=1}^4x_i=0,\quad\sum_{i=1}^4(x_i)_+\le1\right\},\qquad (u)_+=\max\{u,0\}.
\]
The inclusion from left to right is immediate. Conversely, for a vector with positive mass \(a\le1\), transport the mass from its negative coordinates to its positive coordinates: the resulting coupling expresses \(x\) as a convex combination of roots with total weight \(a\), plus weight \(1-a\) at the origin, itself in the convex hull of opposite roots. This proves equality. In particular every coordinate lies in \([-1,1]\).

**2. Periodization.** Fix \(y\in(0,1)^3\). Any projected translate \(y+m\in Q\) must have \(m_j\in\{0,-1\}\). For a subset \(S\subseteq\{1,2,3\}\) take \(x_j=y_j-\mathbf1_{j\in S}\) and \(x_4=|S|-t\). Its total positive mass is
\[
\sum_{j\notin S}y_j+(|S|-t)_+.
\]
For \(0<t<1\), exactly \(S=\varnothing\) and the three singleton subsets satisfy the inequality \(\le1\). For \(1<t<2\), only subsets of sizes one or two can qualify. For each \(j\), the singleton \(\{j\}\) qualifies precisely when \(y_j\ge t-1\), whereas its complementary two-set qualifies precisely when \(y_j\le t-1\). Outside a finite union of hyperplanes, exactly one qualifies, making three total. For \(2<t<3\), exactly the three two-subsets and the full set qualify. Therefore \(W\) equals four, three, four in the three respective slabs, proving the stated almost-everywhere identity. Integrating shows \(\operatorname{vol}(Q)=3+2/6=10/3\).

**3. Reduction to one simplex.** Let \(T=\{y\in\mathbb R^3:y_j\ge0,\ y_1+y_2+y_3\le1\}\). Fourier coefficients of the periodization are those of \(\mathbf1_Q\). The opposite corner simplex is \(\mathbf1-T\); for integer \(k\), its Fourier integral is the complex conjugate of the integral over \(T\). Thus, for all \(k\in\mathbb Z^3\),
\[
C(k)=3\mathbf1_{\{k=0\}}+2\operatorname{Re}I(k),\qquad I(k)=\int_Te^{-2\pi i k\cdot y}\,dy.
\]

**4. Exact residue evaluation.** Put \(b=2\pi i\) and \(\lambda=(0,k_1,k_2,k_3)\). For \(\operatorname{Re}z>0\), the Laplace transform, in the simplex-size parameter \(u\), of \(\int_{\sum y_j\le u,\ y_j\ge0}e^{-b k\cdot y}\,dy\) is
\[
\frac1{\prod_{j=0}^3(z+b\lambda_j)}.
\]
Partial fractions and inverse Laplace transformation at \(u=1\) give
\[
I(k)=\sum_{r\in\operatorname{supp}M_k}\operatorname*{Res}_{z=-br}
\frac{e^z}{\prod_{j=0}^3(z+b\lambda_j)}.
\]
Because each \(r\) is integral, \(e^{-br}=1\). Simple-pole contributions have a factor \(b^{-3}\) and are purely imaginary. At a double pole \(r\), with other values \(s,t\), the real part of the residue is \(b^{-2}/[(s-r)(t-r)]\). If the other two entries coincide at \(s\), the corresponding real part is \(b^{-2}/(s-r)^2\); there are then two such double poles. At a triple pole \(r\), with singleton \(s\), differentiating twice gives real part \(-b^{-2}/(s-r)^2\). If all four values agree then \(k=0\). Since \(b^{-2}=-1/(4\pi^2)\), substitution into the expression for \(C(k)\) yields precisely the four cases above. Their nonzero cases have manifestly nonzero denominators and numerators, so the vanishing criterion is exact.

**5. Count.** There are \((2N+1)^3\) frequency triples in the box. To make \(0,k_1,k_2,k_3\) all distinct, choose an ordered triple of distinct values among the \(2N\) nonzero integers in the box. The number is \((2N)(2N-1)(2N-2)\). Subtraction gives \(24N^2+2N+1\) identically, including \(N=0\).

## Verification

The accompanying `verify.py` uses Python's standard library only. It checks the almost-everywhere periodization identity at 471 rational test points, independently integrates thirteen Fourier modes over the simplex by tensor Gauss–Legendre quadrature, and exhaustively verifies the support counts for the seven boxes \(0\le N\le6\). All checks passed. The finite tests support but do not replace the universal symbolic argument in the proof. Run `python verify.py` alongside this file.

## Relationship to prior work

General formulas for polyhedral Fourier transforms and non-generic frequency directions are developed by Diaz, Le and Robins [2], particularly their combinatorial Stokes formula. That theorem could in principle be applied to this polytope, but it does not itself give the two-level lattice periodization, the complete coefficient table, or the exact frequency-box support count. Montagard and Ressayre [1] provide root-polytope/lattice context. Ardila et al. [3] specifically triangulate the type-\(A_n\) root polytopes, but neither paper provides this exact Fourier support calculation. Related exact Fourier-support calculations for other lattice polytopes use different geometry and do not entail this cuboctahedral identity without the new periodization step. The arithmetic coincidence hyperplanes here are rooted in the four coordinate phases \(0,k_1,k_2,k_3\), not the signed absolute-frequency collisions of the three-dimensional cross-polytope.

## Limitations

The result concerns this one lattice realization of the type-\(A_3\) root polytope, not all root systems, arbitrary affine maps, arbitrary real frequencies, or general dilates. A change in Fourier normalization or ambient measure rescales the displayed constants. Existing broad polytope Fourier methods are not a proof of novelty, and an equivalent specialized lattice-tiling calculation might exist outside the inspected sources. Independent mathematical validation has not been performed.

## References

[1] P.-L. Montagard and N. Ressayre, *Regular Lattice Polytopes and Root Systems*, arXiv:math/0609809, first public version 2006-09-28, https://arxiv.org/abs/math/0609809.

[2] R. Diaz, Q.-N. Le and S. Robins, *Fourier transforms of polytopes, solid angle sums, and discrete volume*, arXiv:1602.08593, first public version 2016-02-27, https://arxiv.org/abs/1602.08593.

[3] F. Ardila, M. Beck, S. Hoşten, J. Pfeifle and K. Seashore, *Root polytopes and growth series of root lattices*, arXiv:0809.5123, first public version 2008-09-30, https://arxiv.org/abs/0809.5123.
