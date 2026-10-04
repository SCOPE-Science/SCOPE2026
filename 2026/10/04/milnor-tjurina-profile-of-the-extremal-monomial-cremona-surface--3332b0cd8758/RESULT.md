# Milnor–Tjurina profile of the extremal monomial Cremona surface
## Finding
For every integer \(d\ge 3\), let
\[
f_d=x_0^d+x_0^{d-1}x_1+x_1^{d-1}x_2+x_2^{d-1}x_3
\]
and let \(D_d=V(f_d)\subset\mathbb P^3_\mathbb C\). The surface has the unique singular point \(p=[0:0:0:1]\). Its multiplicity at \(p\) is \(d-1\), and its isolated hypersurface germ has
\[
\mu_p(D_d)=(d-2)(d^2-2d+2),\qquad
\tau_p(D_d)=(d-2)(d^2-3d+5).
\]
Hence
\[
\mu_p(D_d)-\tau_p(D_d)=(d-2)(d-3).
\]
By Saito's criterion, the cubic member is analytically quasihomogeneous, while every member with \(d\ge4\) is not quasihomogeneous.

The family \(f_d\) is the polynomial attached by Fassarella–Medeiros to the monomial Cremona maps that attain the sharp inverse-degree bound \(d^2-d+1\). Thus the formulas give a local-singularity profile for the extremal family itself, rather than for an arbitrary auxiliary slice.

## Assumptions and scope
Everything is over \(\mathbb C\), and \(d\) is an integer with \(d\ge3\). Set \(n=d-1\). On the affine chart \(x_3=1\) centered at \(p\), the germ is
\[
g_n(x,y,z)=x^{n+1}+x^n y+y^n z+z^n.
\]
The Milnor number is \(\dim_\mathbb C\mathbb C\{x,y,z\}/(g_x,g_y,g_z)\), and the Tjurina number is \(\dim_\mathbb C\mathbb C\{x,y,z\}/(g_n,g_x,g_y,g_z)\). The claim concerns this local germ and does not assert a classification of all surface singularities arising from monomial Cremona maps.

## Proof
The projective partial derivative with respect to \(x_3\) is \(x_2^n\), so every singular point has \(x_2=0\). Then the derivative with respect to \(x_2\) forces \(x_1=0\), and the derivative with respect to \(x_1\) forces \(x_0=0\). Thus \(p\) is the unique singular point. In the chart \(x_3=1\), the term of least total degree is \(z^n\), so the multiplicity is \(n=d-1\).

For the Milnor number,
\[
g_x=x^{n-1}((n+1)x+ny),\quad
g_y=x^n+n y^{n-1}z,\quad
g_z=y^n+n z^{n-1}.
\]
Write \(L=(n+1)x+ny\), \(B=x^n+n y^{n-1}z\), and \(C=y^n+n z^{n-1}\). Since the critical point is isolated, local intersection multiplicity is additive across the factorization \(g_x=x^{n-1}L\), giving
\[
\mu=(n-1)I_0(x,B,C)+I_0(L,B,C).
\]
On \(x=0\), one has \(B=n y^{n-1}z\), and therefore
\[
I_0(x,B,C)=(n-1)I_0(y,C)+I_0(z,C)=(n-1)^2+n=n^2-n+1.
\]
On \(L=0\), write \(y=-((n+1)/n)x\). Then, up to nonzero constants,
\[
B=x^{n-1}(x+\kappa z),\qquad C=\lambda x^n+n z^{n-1},
\]
with \(\kappa,\lambda\ne0\). Thus
\[
I_0(L,B,C)=(n-1)I_0(x,C)+I_0(x+\kappa z,C)=(n-1)^2+(n-1)=n(n-1).
\]
Consequently
\[
\mu=(n-1)(n^2+1)=(d-2)(d^2-2d+2).
\]

For the Tjurina number, Euler's identity in this nonhomogeneous affine form gives the exact relation
\[
(n+1)g_n-xg_x-yg_y-zg_z=z^n.
\]
Hence the Tjurina ideal equals \((g_x,g_y,g_z,z^n)\). For lexicographic order \(x>y>z\), it has the Gröbner basis
\[
\begin{aligned}
G_1&=x^n+n y^{n-1}z,\\
G_2&=x^{n-1}y-(n+1)y^{n-1}z,\\
G_3&=x^{n-1}z^{n-1},\\
G_4&=x y^{n-1}z,\\
G_5&=y^n+n z^{n-1},\\
G_6&=z^n.
\end{aligned}
\]
Membership follows directly from \(G_1=g_y\), \(G_5=g_z\), the Euler relation for \(G_6\), and the identities obtained from \(g_x-(n+1)G_1=nG_2\), from \(xG_2-yG_1+nzG_5-n^2G_6=-(n+1)G_4\), and from a combination of \(y^{n-1}G_2-x^{n-1}G_5\), \(y^{n-2}zG_5\), and \(y^{n-2}G_6\) for \(G_3\). Buchberger reductions of the remaining non-coprime leading-term pairs vanish; the supplied verifier checks these reductions exactly for \(2\le n\le10\), while the displayed identities and reductions are symbolic in \(n\).

The initial ideal is
\[
(x^n,x^{n-1}y,x^{n-1}z^{n-1},xy^{n-1}z,y^n,z^n).
\]
Among the \(n^3\) monomials \(x^a y^b z^c\) with \(0\le a,b,c<n\), the excluded monomials consist of \(n(n-1)\) with \(a=n-1,b\ge1\), one additional monomial with \(a=n-1,b=0,c=n-1\), and \((n-2)(n-1)\) additional monomials with \(1\le a\le n-2,b=n-1,1\le c\le n-1\). Therefore
\[
\tau=n^3-n(n-1)-1-(n-2)(n-1)=(n-1)(n^2-n+3),
\]
which is \((d-2)(d^2-3d+5)\). Subtraction gives \((n-1)(n-2)=(d-2)(d-3)\). Saito's criterion \(\mu=\tau\) for isolated hypersurface germs then yields the quasihomogeneity statement.

## Verification
The package contains `artifacts/verify.py`, using only Python's standard library. It reconstructs the sparse polynomials, verifies the affine Euler identity, checks the proposed Tjurina Gröbner basis by exact Buchberger reduction for \(2\le n\le10\), counts its standard monomials, and verifies the closed formulas and defect arithmetic. Its finite range is a regression check, not a replacement for the symbolic proof for all \(n\ge2\).

The unique-singular-point argument and the local-intersection computation for \(\mu\) are independent of the finite checker. The critical use of characteristic zero is explicit: coefficients such as \(n\) and \(n+1\) must be nonzero.

## Relationship to prior work
Fassarella and Medeiros introduce the same family in Example 3.2 of arXiv:2206.04847, state that \(V(f_d)\) is smooth for \(d=2\) and has the unique singular point \([0:0:0:1]\) for \(d\ge3\), and use the family to attain inverse degree \(d^2-d+1\). Their Theorem 3.3 states that equality is attained only by this map up to permutations of variables or coordinates. The inspected discussion computes the Milnor sum of a general linear section, which is zero because that section is smooth; it does not give the local Milnor or Tjurina number of the unique surface singularity.

Johnson's earlier construction arXiv:1105.1188 gives the same extremal monomial Cremona family and inverse degree, but the inspected example does not provide these local singularity invariants. The later toric-polar work arXiv:2205.03957 develops characteristic-class formulas and broader toric-polar geometry; it does not imply the displayed local formulas for this germ in the material inspected. Targeted searches for the exact family together with Milnor and Tjurina terminology, plus a semantic database comparison, did not locate the formulas above.

## Limitations
The result concerns the complex analytic germ of this one extremal family. It does not classify singularities for all monomial Cremona maps, and it does not assert that the polynomial expression itself is weighted homogeneous when \(d=3\); the conclusion is analytic quasihomogeneity via \(\mu=\tau\). The literature comparison is targeted rather than exhaustive, so an unindexed computation of the same local invariants remains a residual originality risk.

## References
1. T. Fassarella and N. Medeiros, *Monomial Cremona transformations and toric polar maps*, arXiv:2206.04847; Communications in Algebra 51 (2023), 1900–1906, DOI 10.1080/00927872.2022.2145609.
2. P. Johnson, *Inverses of monomial Cremona transformations*, arXiv:1105.1188.
3. T. Fassarella, N. Medeiros, and R. Salomão, *Toric polar maps and characteristic classes*, arXiv:2205.03957.
4. K. Saito's criterion for isolated hypersurface singularities: \(\mu=\tau\) if and only if the germ is quasihomogeneous; see, for example, the discussion in J. Wahl, *Milnor and Tjurina numbers for smoothings of surface singularities*, Algebraic Geometry 2 (2015), 315–331.
