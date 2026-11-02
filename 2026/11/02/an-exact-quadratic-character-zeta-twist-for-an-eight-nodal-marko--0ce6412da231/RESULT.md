# An exact quadratic-character zeta twist for an eight-nodal Markoff K3 double cover

## Finding
Let \(q\) be an odd prime power satisfying \(q\equiv1\pmod 8\). Choose \(i\in\mathbb F_q\) with \(i^2=-1\), let \(\chi_q\) be the quadratic character with \(\chi_q(0)=0\), and put \(\varepsilon_q=\chi_q(1+i)\). This is independent of the choice of \(i\), because \((1+i)(1-i)=2\) and \(2\) is a square in \(\mathbb F_q\).

Let \(W\subset(\mathbb P^1)^3\) be the trihomogeneous closure of
\[
x^2+y^2+z^2+x^2y^2z^2=4xyz.
\]
Let \(X\to W\) be the normalization of \(W\) in the quadratic function-field extension obtained by adjoining a square root of
\[
S(y,z)=y(1-z^2)+iz(1-y^2).
\]
The class of this rational function is interpreted on any affine chart; its homogeneous counterpart has bidegree \((2,2)\), so its square class is unambiguous. This is the same quadratic extension used in the Markoff-orbit partition of O'Dorney [1].

**Theorem.** The surface \(W\) has exactly eight geometric singularities, all rational ordinary double points. The normalization \(X\) is a smooth, geometrically connected K3 surface. The covering involution has precisely eight fixed points and is symplectic. For every \(n\ge1\),
\[
\#X(\mathbb F_{q^n})-\#W(\mathbb F_{q^n})
=8(\varepsilon_q q)^n.
\]
Equivalently, the Hasse--Weil zeta functions satisfy the **exact identity**
\[
\boxed{\frac{Z(X/\mathbb F_q,T)}{Z(W/\mathbb F_q,T)}
=(1-\varepsilon_q qT)^{-8}.}
\]
In particular, for every prime \(\ell\ne2,\operatorname{char}\mathbb F_q\), Frobenius acts on the eight-dimensional anti-invariant summand of \(H^2_{\mathrm{\acute et}}(X_{\overline{\mathbb F}_q},\mathbb Q_\ell)\) as the scalar \(\varepsilon_q q\).

Let \(U\) be the image of \(X(\mathbb F_q)\) in \(W(\mathbb F_q)\), including the eight nodes, and let \(V=W(\mathbb F_q)\setminus U\). Then
\[
\boxed{\#U-\#V=8+8\varepsilon_q q,}\qquad
\boxed{\#U=\frac{\#W(\mathbb F_q)+8+8\varepsilon_q q}{2},\quad
\#V=\frac{\#W(\mathbb F_q)-8-8\varepsilon_q q}{2}.}
\]
The invariance of \(U,V\) under the previously specified Markoff symmetry group is established in [1]. The new exact formulas sharpen its \(O(q^{3/2})\) estimates to an explicit linear bound: every orbit lies in a set of size at most
\[
\frac{q^2+9}{2}+11q.
\]
The assertion concerns the sets arising from this particular quadratic cover, not the number or transitivity of individual orbits.

## Assumptions and scope
All geometry is over fields of odd characteristic. The arithmetic equalities require \(q\equiv1\pmod8\), which supplies \(i\) and a square root \(s\) of \(2\) in \(\mathbb F_q\). The curve-counting symbol \(\chi_q\) is multiplicative on nonzero elements and is zero at zero. The singular surface \(W\), rather than its minimal resolution, appears in the displayed zeta quotient. Both zeta functions count rational points of the indicated complete varieties, including singular points on \(W\). The result applies to all extensions \(\mathbb F_{q^n}\), not only prime fields.

## Proof
**1. The eight nodes and the K3 surface downstairs.** Write \(F=x^2+y^2+z^2+x^2y^2z^2-4xyz\). Away from zero and infinity, multiplication of the three gradient equations by the respective coordinates gives \(x^2=y^2=z^2=u\) and \(u+u^3=2xyz\). Substitution into \(F=0\) gives \(u-u^3=0\); since the coordinates are nonzero, \(u^2=1\). Squaring \(u+u^3=2xyz\) and using \((xyz)^2=u^3\) eliminates \(u=-1\) in odd characteristic. Thus \(u=1\), \(xyz=1\), producing the four sign triples with product one. If a finite coordinate vanishes, the gradient equations leave only \((0,0,0)\). In a chart with one coordinate infinite, the derivative in that reciprocal coordinate is nonzero on the surface; with two coordinates infinite, the remaining coordinate must be zero. This adds the three permutations of \((0,\infty,\infty)\). No point with three infinite coordinates lies on \(W\).

At \((0,0,0)\), the quadratic tangent cone is \(x^2+y^2+z^2\). At a sign triple its diagonal Hessian has nonzero entries \(4\), with zero off-diagonal entries. At a two-infinity point, reciprocal coordinates give the same quadratic cone as at zero. Hence all eight singularities are \(A_1\) nodes and there are no others. The trihomogeneous equation has multidegree \((2,2,2)\), so adjunction gives \(\omega_W\cong\mathcal O_W\). Its isolated rational double points are crepant and rational. The exact hypersurface sequence in \((\mathbb P^1)^3\), together with Künneth, gives \(H^1(W,\mathcal O_W)=0\). Therefore the minimal resolution \(Y\to W\) is a K3 surface.

**2. The quadratic extension is locally the smooth canonical cover of each node.** Put
\[
A=1+y^2z^2,\qquad
S=y(1-z^2)+iz(1-y^2),\qquad
S'=y(1-z^2)-iz(1-y^2).
\]
Direct expansion, using \(i^2=-1\), gives the polynomial identity
\[
A F=(Ax-2yz)^2+SS'.
\]
Consequently, on \(W\), the element \(w=i(Ax-2yz)\) satisfies \(w^2=SS'\). At each finite node \(A\) is a unit and the differentials of \(S,S'\) in \(y,z\) are independent: at zero they begin with \(y+iz,y-iz\); at a sign triple they begin, up to units, with \(dz+i\,dy,dz-i\,dy\). Thus the completed local equation is \(w^2=st\). Adjoining \(\sqrt{s}\) and normalizing yields \(s=u^2,t=v^2,w=uv\), a regular two-dimensional local ring; the involution acts by \((u,v)\mapsto(-u,-v)\). Inverting the appropriate one or two projective coordinates puts each node at infinity into the same local form; the displayed square class changes only by square units and possibly by exchanging \(S,S'\), which generate the same extension because \(SS'=w^2\). This proves smoothness above every node and exactly one fixed geometric point there.

Elsewhere the extension is unramified: at least one of the six ordered discriminant factors from [1] is a nonzero unit, and all represent the same square class. The extension is nontrivial geometrically, since restriction of \(S\) to the line \((x,y,z)=(iy,y,0)\) is \(y\), not a square in its rational function field. Thus \(X\) is geometrically connected, smooth, projective, and the involution has exactly eight fixed points.

The finite map \(X\to W\) is étale in codimension one. The dualizing sheaf of \(W\) is trivial, so \(\omega_X\cong\mathcal O_X\). The smooth locus of \(W\) has \(\ell\)-adic Euler characteristic \(24-8\cdot2=8\), because \(Y\) is K3 and its eight exceptional curves are disjoint projective lines. Its étale double cover has Euler characteristic \(16\); adjoining the eight isolated preimages gives \(c_2(X)=24\). Noether's formula yields \(\chi(\mathcal O_X)=2\); connectedness and the trivial canonical sheaf give \(h^0(\mathcal O_X)=h^0(\omega_X)=1\), hence \(h^1(\mathcal O_X)=0\). Therefore \(X\) is K3. The involution has local differential \(-I\) at each fixed point, and so acts trivially on a local generator of the canonical sheaf; it is symplectic.

**3. A fiberwise character identity.** Homogenize \(S,S'\) to bidegree \((2,2)\) forms on \(B=\mathbb P^1_y\times\mathbb P^1_z\). The projection \(W\to B\) has nonzero binary quadratic fibers; its discriminant is \(-4SS'\). For a base point \(b\in B(\mathbb F_q)\), the following identity holds, with \(\#X_b\) denoting rational points mapping to \(b\):
\[
\#X_b-\#W_b=\chi_q(S(b))+\chi_q(S'(b)).
\]
If both factors are nonzero, the binary quadratic has two rational roots precisely when their characters agree (because \(-1\) is a square); on each root the double cover splits precisely when their common character is \(+1\). If exactly one factor vanishes, the quadratic has one repeated rational root; the other, nonzero factor represents the square class of the cover there, giving difference \(+1\) or \(-1\). If both vanish, the point is one of the eight nodes, with one point in each fiber and difference zero. There is no identically zero binary quadratic fiber, as is immediate from its three coefficient forms. The homogeneous bidegree ensures that these character evaluations do not depend on projective representatives.

**4. Evaluation of the character sum.** For fixed finite \(z\ne0\), the first factor is the polynomial
\[
S(y,z)=-iz\,y^2+(1-z^2)y+iz.
\]
Its discriminant in \(y\) is
\[
D(z)=z^4-6z^2+1
=\bigl(z^2-(1+s)^2\bigr)\bigl(z^2-(1-s)^2\bigr),\quad s^2=2.
\]
The elementary quadratic-character sum over finite \(y\), augmented by the point \(y=\infty\), is zero when \(D(z)\ne0\), and is \(q\chi_q(-iz)\) when \(D(z)=0\). The values \(z=0\) and \(z=\infty\) contribute zero. The four distinct discriminant roots are \(\pm(1+s),\pm(1-s)\); their character factors agree because \((1+s)(1-s)=-1\) and \(-1\) is a square. Consequently,
\[
\sum_{b\in B(\mathbb F_q)}\chi_q(S(b))=4q\chi_q(-i(1+s)).
\]
The analogous sum for \(S'\) is equal, by replacing \(z\) by \(-z\). Finally,
\[
\left(\frac{i(1+s)-1}{2}\right)^2
=\frac{-i(1+s)}{1+i},
\]
so \(\chi_q(-i(1+s))=\chi_q(1+i)=\varepsilon_q\). Summing the fiberwise identity proves \(\#X(\mathbb F_q)-\#W(\mathbb F_q)=8q\varepsilon_q\). Applying the same argument over every extension and using \(\chi_{q^n}(1+i)=\varepsilon_q^n\) proves the claimed point-count identity and zeta quotient.

**5. Anti-invariant Frobenius and orbit bounds.** Let \(\iota\) be the deck involution and take \(\ell\ne2,\operatorname{char}\mathbb F_q\). The quotient identity \(H^*(W,\mathbb Q_\ell)\cong H^*(X,\mathbb Q_\ell)^\iota\), together with K3 cohomology, identifies the difference of point counts with Frobenius traces on the anti-invariant part of degree-two cohomology. The Lefschetz fixed-point formula for \(\iota\), whose fixed locus is eight points, gives \(\operatorname{Tr}(\iota\mid H^2(X))=6\). Since \(\dim H^2(X)=22\), the invariant and anti-invariant dimensions are \(14\) and \(8\). Equality of power traces for every \(n\) identifies all eight anti-invariant Frobenius eigenvalues as \(\varepsilon_q q\).

The eight rational nodes have one rational preimage each, and every other rational point of \(W\) has either two or zero rational preimages. Thus \(\#X(\mathbb F_q)=2\#U-8\), giving the two exact partition formulas. Weil's weight-two bound on the fourteen-dimensional invariant cohomology gives \(\lvert\#W(\mathbb F_q)-(q^2+1)\rvert\le14q\). Substituting this bound into the partition formulas gives \(\#U\le(q^2+9)/2+11q\) and \(\#V\le(q^2-7)/2+11q\), completing the effective orbit-size consequence.

## Verification
The standalone file `verify_markoff_cover.py` enumerates the projective triples and homogeneous discriminant factors without symbolic packages. Running `python verify_markoff_cover.py` checks the exact identity \(\#X-\#W=8q\chi_q(1+i)\), the eight-branch-point count, the absence of conflicting nonzero square classes, and the K3 Weil bound for prime fields of orders \(17,41,73,89,97,113\) and quadratic-extension fields of orders \(9,25,49\). The direct enumeration reconstructs \(\#X=2\#U-8\) rather than assuming a precomputed cover point count. Representative results are \((q,\#W,\#U,\#X)=(17,496,184,360),(41,2128,1232,2456),(9,176,56,104)\). These finite checks are corroboration; the preceding proof establishes all odd prime powers with \(q\equiv1\pmod8\).

## Relationship to prior work
O'Dorney [1] constructs the same quadratic extension and the invariant orbit partition. Theorem 2 therein obtains only \(q^2/2+O(q^{3/2})\) for the two parts and explicitly does not determine the topology of the covering surface. Fuchs--Litman--Silverman--Tran [2] supply the motivating orbit computations; their Section 13 does not give the exact character imbalance. Peters [3] explains the general K3 double-cover construction from an even set of eight nodal curves: this general principle is prior work, and its abstract consequence alone is not the new arithmetic theorem. The present additional calculations are the **explicit cover geometry in this model**, the all-extension character-sum identity, the quadratic-twist zeta quotient, and the scalar eight-dimensional anti-invariant Frobenius action. The proof does not assert an original general theorem about Nikulin involutions.

## Limitations
The formula does not give a closed expression for \(\#W(\mathbb F_q)\), individual orbit sizes, or transitivity within either invariant part. The arithmetic statement is restricted to \(q\equiv1\pmod8\); the geometric cover may be described after adjoining the necessary eighth roots of unity in other characteristics. Its novelty relative to inaccessible or unindexed arithmetic descriptions of this particular K3 cover has not been independently established. No independent mathematical audit has been carried out.

## References
1. E. M. O'Dorney, *Large orbits on Markoff-type K3 surfaces over finite fields*, arXiv:2209.10436 (first version 2022-09-21), especially Theorem 2 and its proof, pp. 2--3; published in *International Mathematics Research Notices* (2023), DOI 10.1093/imrn/rnac341.
2. E. Fuchs, M. Litman, J. H. Silverman, A. Tran, *Orbits on K3 surfaces of Markoff type*, arXiv:2201.12588 (2022), especially Section 13 and Table 6.
3. C. Peters, *On the maximal number of du Val singularities for a K3 surface*, *Geometriae Dedicata* 214 (2021), Lemma 4.1 and Remark 4.2, DOI 10.1007/s10711-021-00620-3.
