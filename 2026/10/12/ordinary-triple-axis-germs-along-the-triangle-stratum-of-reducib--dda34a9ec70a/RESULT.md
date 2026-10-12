# Ordinary triple-axis germs along the triangle stratum of reducible plane cubics

## Finding

Let \(S_j=\mathbb C[x,y,z]_j\), and let \(X\subset\mathbb P(S_3)=\mathbb P^9\) be the reduced projective variety of cubics divisible by a nonzero linear form. For **every** three linearly independent nonzero linear forms \(\ell_1,\ell_2,\ell_3\), put \(p=[\ell_1\ell_2\ell_3]\). There is an isomorphism of complete local \(\mathbb C\)-algebras
\[
\widehat{\mathcal O}_{X,p}\cong
R:=\mathbb C[[t_1,\ldots,t_6,u,v,w]]/(uv,uw,vw).
\]
The smooth six-dimensional stratum \(Z\) of triangles (three unordered, linearly independent line factors) is given formally by \((u,v,w)\). The germ consists of three smooth seven-dimensional analytic branches, meeting pairwise precisely along \(Z\), with three independent normal tangent lines.

Consequently, \(\dim\mathcal O_{X,p}=7\), its embedding dimension is \(9\), its Hilbert--Samuel multiplicity is \(3\), it is Cohen--Macaulay of type \(2\) but not Gorenstein, and its associated graded Hilbert series is
\[
\sum_{q\ge0}\dim_{\mathbb C}(\mathfrak m^q/\mathfrak m^{q+1})T^q
=\frac{1+2T}{(1-T)^7}.
\]
Equivalently, for each integer \(q\ge0\),
\[
\operatorname{length}(R/\mathfrak m^{q+1})
=\binom{q+7}{7}+2\binom{q+6}{7},
\]
with the usual convention that a binomial coefficient vanishes when its upper index is smaller than its lower index.

The completed normalization is \(\overline R=\prod_{i=1}^3\mathbb C[[t_1,\ldots,t_6,s_i]]\). Its inclusion identifies \(R\) with the triples whose evaluations at \(s_i=0\) all coincide. The quotient \(\overline R/R\) is, as an \(R\)-module, the direct sum of two copies of \(\mathbb C[[t_1,\ldots,t_6]]\), and the conductor is exactly \(\mathfrak c=(u,v,w)R\). In particular, the local germ is nonnormal along a codimension-one stratum.

## Assumptions and scope

Everything is over \(\mathbb C\). The cubic is squarefree and its three factors are *linearly independent*; geometrically, the three distinct lines form a nonconcurrent triangle in \(\mathbb P^2\). The ambient variety is the factorization locus of type \((2,1)\), not the smaller locus of completely split cubics. No assertion is made at three concurrent lines, double lines, or general points of other singular strata. Completed branches need not be global irreducible components: \(X\) is globally irreducible.

## Proof

**1. Normalization and branches.** Consider the multiplication map
\[
\nu:\mathbb P(S_1)\times\mathbb P(S_2)\longrightarrow X,
\qquad ([L],[Q])\longmapsto[LQ].
\]
Every nonzero cubic has at most three distinct projective linear factors, so \(\nu\) has finite fibers. It is projective, hence finite. For a generic cubic with an irreducible quadratic factor the factor \(L\) is unique, so the finite map is birational. Its smooth normal source is therefore the normalization. At \(xyz\), its fiber consists of \(([x],[yz]),([y],[xz]),([z],[xy])\). In each branch the differential is the injective map
\[
(\delta L,\delta Q)\longmapsto Q\delta L+L\delta Q
\]
modulo the one projective scaling relation: when \(L\) and \(Q\) are coprime, reducing the equality \(Q\delta L+L\delta Q=0\) modulo \(L\) forces \(\delta L\) to be a scalar multiple of \(L\). The three images are thus smooth local branches of dimension \(2+5=7\).

**2. Tangent directions.** Linear changes of coordinates carry every allowed triple to \(xyz\). Before projectivizing, the three branch tangent vector spaces are
\[
T_x=yzS_1+xS_2,\qquad
T_y=xzS_1+yS_2,\qquad
T_z=xyS_1+zS_2.
\]
In the ten-dimensional space \(S_3\), these are respectively the spans of all cubic monomials except \(y^3,z^3\), except \(x^3,z^3\), and except \(x^3,y^3\). Each has dimension \(8\); every pair intersects in the seven-dimensional span of the monomials except \(x^3,y^3,z^3\), while their sum is all of \(S_3\).

The triangle stratum \(Z\) is smooth of dimension \(6\). Indeed, the product map from three copies of \(\mathbb P(S_1)\) has six-dimensional injective derivative at three distinct factors, and the unordered factorization is unique, up to the free permutation action near such a triple. Its projective tangent space is precisely the common six-dimensional intersection of the three branch tangents. Consequently the images of the normal tangent lines of the three branches in the three-dimensional normal space to \(Z\subset\mathbb P^9\) are independent.

**3. Pairwise intersections as schemes.** Two different local branches correspond to two different linear factors of the cubic. Every cubic near \(xyz\) possessing two such factors is a product of three linear forms, so the *support* of each pairwise intersection is \(Z\). The intersection tangent space is the intersection of their tangent spaces, hence has dimension \(6\) by Step 2. The local scheme-theoretic intersection has Krull dimension \(6\) and embedding dimension \(6\), hence is regular and reduced; therefore it equals the smooth \(Z\) scheme-theoretically. Writing \(I_x,I_y,I_z\) and \(I_Z\) for their completed ideals in the regular ambient completion, this gives
\[
I_x+I_y=I_x+I_z=I_y+I_z=I_Z.
\]

**4. Simultaneous formal straightening.** Choose regular ambient parameters \(t_1,\ldots,t_6,a,b,c\) so that \(I_Z=(a,b,c)\). Renaming \(a,b,c\) according to the independent normal tangents, the linear ideals of the three branches relative to \(Z\) are \((b,c)\), \((a,c)\), and \((a,b)\). We show there are formal parameters \(u,v,w\), with linear parts \(a,b,c\), for which these are the *exact* ideals.

For the desired \(u\), choose \(g_y\in I_y\) and \(g_z\in I_z\), each with linear part \(a\). Their difference belongs to \(I_Z\cap\mathfrak m^2=\mathfrak m I_Z=\mathfrak m I_y+\mathfrak m I_z\). Correcting \(g_y\) by a term in \(\mathfrak m I_y\), or equivalently \(g_z\) by a term in \(\mathfrak m I_z\), yields an element \(u\in I_y\cap I_z\) still having linear part \(a\). Similarly obtain \(v\in I_x\cap I_z\) with linear part \(b\), and \(w\in I_x\cap I_y\) with linear part \(c\). Their linear parts together with those of the \(t_i\) are independent; hence \((t_1,\ldots,t_6,u,v,w)\) is a regular system of formal parameters. Nakayama's lemma and the pairwise-intersection identities imply
\[
I_x=(v,w),\quad I_y=(u,w),\quad I_z=(u,v).
\]
Because the reduced local variety is the union of these three branches,
\[
I_X=I_x\cap I_y\cap I_z=(uv,uw,vw).
\]
This is an isomorphism of complete local rings, not merely a tangent-cone approximation.

**5. Local invariants.** The monomial quotient above has basis consisting of arbitrary monomials in the six \(t_i\), multiplied by either a pure power of \(u\), a pure power of \(v\), a pure power of \(w\), or \(1\); a monomial involving two different normal variables vanishes. Its Hilbert series is
\[
\frac{1+3T/(1-T)}{(1-T)^6}=\frac{1+2T}{(1-T)^7}.
\]
The variables \(t_i\) form a regular sequence. Modding them out and then modding out by the additional nonzerodivisor \(u+v+w\) gives
\[
\mathbb C[[u,v]]/(u^2,uv,v^2).
\]
This zero-dimensional ring has two-dimensional socle, so the original seven-dimensional local ring is Cohen--Macaulay of type \(2\). Its multiplicity is the Hilbert numerator evaluated at \(T=1\), namely \(3\); the other invariants and the length formula follow from the series. The normalization is the product of the three completed smooth branches. Describing an element by its three branch restrictions shows that its constant restrictions along \(Z\) must agree, and conversely any such triple comes from \(R\). Thus \(\overline R/R\simeq\mathcal O_{Z,p}^{\oplus2}\), and its annihilator, the conductor, is the ideal of \(Z\), \((u,v,w)\).

## Verification

The independent exact-arithmetic checker `cubic_factorization_checker.py` uses SymPy to calculate the tangent-space ranks at \((x,y,z)\) and a general invertibly transformed triple, and to check the distinct concurrent triple \((x,y,x+y)\) as a boundary. It obtains branch ranks \((8,8,8)\), common triangle tangent dimension \(7\) before projectivization, pairwise sum ranks \((9,9,9)\), and total sum rank \(10\) for nonconcurrent triples; the concurrent boundary instead has total sum rank \(9\). It checks the Hilbert-series identity symbolically. Run `python cubic_factorization_checker.py` after installing SymPy. These finite computations are corroboration and do not replace the all-point proof in Steps 1–5.

## Relationship to prior work

Factorization-type varieties were studied classically by Mammana (1954). Catalisano–Geramita–Gimigliano–Shin (first public preprint 2014) and Catalisano–Geramita–Gimigliano–Harbourne–Migliore–Nagel–Shin (first public preprint 2015) describe the varieties and determine many secant dimensions, using tangent-space information at general points. The present result instead determines the *completed analytic local ring* at the special three-linear-factor stratum, together with its normalization, conductor, multiplicity and Cohen–Macaulay type. Secant dimensions, global degrees and Euler characteristics do not by themselves determine this local structure. The original Italian sources have not all been completely excluded as sources of an equivalent specialized statement.

## Limitations

This is a statement about the open nonconcurrent triangle stratum, not a complete singular-locus classification. The concurrent distinct-line locus has a different tangent-space configuration, and repeated factors are not treated. The old literature contains difficult-to-access discussions of singularities; a historically equivalent description could remain unrecognized. The proof is a mathematical argument with reproducible finite checks, not an independently audited or machine-formalized certification.

## References

1. M. V. Catalisano, A. V. Geramita, A. Gimigliano and Y.-S. Shin, *The secant line variety to the varieties of reducible plane curves*, arXiv:1404.3911, first submitted 15 April 2014, https://arxiv.org/abs/1404.3911.
2. M. V. Catalisano, A. V. Geramita, A. Gimigliano, B. Harbourne, J. Migliore, U. Nagel and Y.-S. Shin, *Secant Varieties of the Varieties of Reducible Hypersurfaces in \(\mathbb P^n\)*, arXiv:1502.00167, first submitted 31 January 2015, https://arxiv.org/abs/1502.00167.
3. C. Mammana, *Sulla varietà delle curve algebriche piane spezzate in un dato modo*, Ann. Sc. Norm. Super. Pisa (3) **8** (1954), 53–75, https://numdam.org/item/ASNSP_1954_3_8_1-2_53_0/.
