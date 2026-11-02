# The thirteen nonordinary genus-four dihedral-quintic parameters in characteristic \(23\)

## Finding
Let \(k\) be algebraically closed of characteristic \(23\). In the smooth hyperelliptic genus-four family
\[
C_\lambda:\quad y^2=(x^5-1)(x^5-\lambda),\qquad \lambda\in k\setminus\{0,1\},
\]
there are **exactly thirteen** distinct coefficient parameters for which the Jacobian is nonordinary. Each has \(23\)-rank zero and \(a\)-number two; all other smooth members are ordinary. One exceptional parameter is \(\lambda=-1\in\mathbb F_{23}\); the other twelve are defined over \(\mathbb F_{23^2}\) but not \(\mathbb F_{23}\). Under geometric isomorphism \(\lambda\sim\lambda^{-1}\), there are **exactly seven** exceptional isomorphism classes. Their coarse invariant \(t=\lambda+\lambda^{-1}\) is characterized by the squarefree degree-seven polynomial
\[
R_{23}(t)=(t+2)(t+3)(t+7)(t^2-t+7)(t^2-6t+11)
\quad\in\mathbb F_{23}[t].
\]
Three of these classes have \(t\in\mathbb F_{23}\); four have \(t\in\mathbb F_{23^2}\setminus\mathbb F_{23}\).

More generally, for any odd prime \(p\ge7\), the precise geometric parameter counts by \(a\)-number in this family are determined by two explicit separable coefficient polynomials: let \(e=(p-1)/2\), let \(r_i\in\{1,2,3,4\}\) be the residue of \(pi\) modulo five, and put
\[
d_i=p-1-\frac{pi-r_i}{5}\quad(i=3,4),\qquad
P_{e,d}(z)=\sum_{j=0}^{d}{e\choose j}{e\choose d-j}z^j,
\]
\[
A_p=P_{e,d_3},\quad B_p=P_{e,d_4},\quad
D_p=d_3+d_4=\left\lfloor\frac{3(p-1)}5\right\rfloor,\quad
g_p=\deg\gcd(A_p,B_p).
\]
The number of marked geometric parameters with \(a=4\) is \(g_p\); the number with \(a=2\) is \(D_p-2g_p\). There are no \(a=1\) or \(a=3\) parameters, and every exceptional parameter is outside \(\{0,1\}\). The common-root condition for superspeciality and the parameter identification \(\lambda\sim\lambda^{-1}\) are already established in Ohashi--Kudo; the new assertions here are the full nonordinary and \(a\)-number parameter strata, together with the explicit characteristic-23 classification and moduli polynomial.

## Assumptions and scope
All geometric counts concern parameters in an algebraically closed field, not finite-field models or twists. Curves are smooth because \(p\ne2,5\) and \(\lambda\notin\{0,1\}\): the ten roots of the defining polynomial are distinct. The characteristic-23 parameter and moduli counts are literal geometric roots and geometric isomorphism classes, respectively. The term \(a\)-number means \(\dim_k\operatorname{Hom}(\alpha_p,J[p])\), equivalently four minus Cartier rank. The \(p\)-rank is the stable rank of Frobenius on first cohomology. The standard genus-four Cartier basis is \((dx/y,x\,dx/y,x^2\,dx/y,x^3\,dx/y)\).

## Proof
**1. Four sparse Cartier coefficients and their paired vanishing.** Set \(e=(p-1)/2\), write
\[
((z-1)(z-\lambda))^e=\sum_{m=0}^{2e}c_m(\lambda)z^m,
\]
and expand \(((x^5-1)(x^5-\lambda))^e=\sum_m c_m(\lambda)x^{5m}\). The standard hyperelliptic Cartier--Manin coefficient rule says that the entry in row \(i\), column \(j\) is the coefficient of \(x^{pi-j}\), up to field automorphism on scalars. Thus it is zero unless \(j\equiv pi\pmod5\), and there is exactly one potentially nonzero entry per row, with \(i,j\in\{1,2,3,4\}\). For \(i=3,4\) these entries have coefficient indices \(k_i=(pi-r_i)/5\) satisfying \(e<k_i\le2e\), with \(d_i=2e-k_i\in\{1,\ldots,e\}\).

Direct expansion gives, for each \(0\le d\le e\),
\[
c_{2e-d}=(-1)^dP_{e,d}(\lambda),\qquad
c_d=\lambda^{e-d}c_{2e-d}.
\]
The coefficient index in row \(5-i\) is \(2e-k_i\), because the corresponding column is \(5-r_i\). Thus the four nonzero-position entries split into two pairs, whose vanishing loci, for \(\lambda\ne0\), are exactly \(A_p=0\) and \(B_p=0\). Each vanished polynomial kills two distinct nonzero-position entries. The Cartier rank is therefore four, two, or zero according as neither, exactly one, or both vanish. Hence the \(a\)-number is zero, two, or four; common zeros are precisely superspecial members. This does not assume that the two polynomials are coprime.

**2. Universal geometric squarefreeness.** For \(1\le d\le e<p\), the polynomial \(P=P_{e,d}\) satisfies the second-order polynomial identity over \(\mathbb F_p\)
\[
z(1-z)P''+(e-d+1+(e+d-1)z)P'-edP=0.
\]
Indeed the ratio of successive coefficients of \(P\) equals \((e-j)(d-j)/((j+1)(e-d+j+1))\), which gives precisely the displayed recurrence when the differential equation is expanded. Its constant and leading coefficients equal \({e\choose d}\), which is nonzero modulo \(p\), so \(\deg P=d\) and \(P(0)\ne0\). Vandermonde's identity gives \(P(1)={2e\choose d}={p-1\choose d}\equiv(-1)^d\ne0\). If \(z_0\notin\{0,1\}\) were a multiple root, the differential equation would inductively force all derivatives (equivalently all Taylor coefficients, since \(d<p\)) to vanish there. This contradicts \(\deg P=d\). Thus both \(A_p\) and \(B_p\) are squarefree and have no roots at the excluded parameters. Their product has degree \(d_3+d_4=\lfloor3(p-1)/5\rfloor\). Intersection of the two reduced root sets has cardinality \(g_p=\deg\gcd(A_p,B_p)\), proving the asserted counts by \(a\)-number.

**3. Characteristic \(23\).** Here \(e=11\), \(d_3=9\), \(d_4=4\). Elementary binomial expansion gives the following identities in \(\mathbb F_{23}[\lambda]\):
\[
\begin{aligned}
A_{23}(\lambda)&=9(\lambda+1)(\lambda^2+3\lambda+1)(\lambda^2+4\lambda-10)\\
&\hspace{1em}\cdot(\lambda^2+7\lambda+1)(\lambda^2-5\lambda-7),\\
B_{23}(\lambda)&=8(\lambda^2+8\lambda+6)(\lambda^2+9\lambda+4).
\end{aligned}
\]
All six displayed quadratic factors are irreducible over \(\mathbb F_{23}\): their discriminants, in order, are \(5,10,22,7,17,19\), none of which is a square modulo \(23\). They are distinct and have no common factors. The two products have degree nine and four, hence their union consists of exactly thirteen simple geometric roots, one in \(\mathbb F_{23}\) and twelve in \(\mathbb F_{23^2}\setminus\mathbb F_{23}\), all outside \(\{0,1\}\). By Step 1, every such curve has \(a=2\), and no member is superspecial.

Because \(23\equiv3\pmod5\), multiplication by \(23\) on \(\{1,2,3,4\}\) modulo five is a single four-cycle. The semilinear Cartier iterate around this cycle is invertible when all four entries are nonzero, and nilpotent when any one is zero. Thus the \(23\)-rank is four on the ordinary locus and zero at all thirteen exceptional parameters. This p-rank dichotomy, without the new characteristic-23 enumeration, was already known for this pencil and is not asserted as an original result here.

**4. Descending to isomorphism parameters.** Ohashi--Kudo, Proposition 3.3.4, proves that geometric isomorphism within this family is exactly \(\lambda\sim\lambda^{-1}\). All six quadratic factors and \(\lambda+1\) above are partitioned into inversion-stable factors or pairs. The three self-reciprocal quadratic factors \(\lambda^2+3\lambda+1\), \(\lambda^2+7\lambda+1\), and the linear fixed root \(\lambda=-1\) give \(t=-3,-7,-2\), respectively. The remaining factors pair according to
\[
(\lambda^2+4\lambda-10)(\lambda^2-5\lambda-7)
=\lambda^2\bigl(t^2-t+7\bigr),
\]
\[
(\lambda^2+8\lambda+6)(\lambda^2+9\lambda+4)
=\lambda^2\bigl(t^2-6t+11\bigr),
\]
where \(t=\lambda+\lambda^{-1}\). The resulting squarefree degree-seven equation is precisely \(R_{23}(t)=0\). The discriminants of its two quadratic factors are \(19\) and \(15\) modulo \(23\), both nonsquares. (The relevant three linear factors are pairwise distinct and are not roots of the quadratics.) Hence the moduli residue degrees and the count of seven classes follow.

## Verification
Run `python3 verify_d10_strata.py` in the same directory. This pure-Python program recomputes the binomial polynomials modulo each prime from seven through 151, verifies their hypergeometric differential equations, squarefreeness, excluded-boundary values, sparse coefficient reciprocity, and exact degree formula. In characteristic \(23\) it independently expands the displayed factorization, proves absence of shared roots using the Euclidean algorithm, checks irreducibility of all six quadratics by testing all base-field elements, verifies the two reciprocal product identities, and checks that the coarse polynomial has seven simple roots over the algebraic closure. Expected final output: `GENUS4_QUINTIC_D10_STRATA_PASS`. These finite checks corroborate, but do not substitute for, the arbitrary-prime symbolic proof.

## Relationship to prior work
Ohashi and Kudo, *Computing superspecial hyperelliptic curves of genus 4 with automorphism group properly containing the Klein 4-group*, arXiv:2312.16858, Section 3.3, already give the family, its sparse Cartier matrix, the common-zero test for superspeciality, and the identification \(\lambda\sim\lambda^{-1}\). Their Table 2 records superspecial enumeration for small primes, including no superspecial curves of the displayed dihedral type in characteristic \(23\). These known facts do not identify the thirteen **non-superspecial nonordinary** parameters, their \(a\)-number and \(23\)-rank, or the seven-class coarse polynomial above. The previously established four-or-zero \(p\)-rank dichotomy in characteristics congruent to two or three modulo five is acknowledged, not presented as new. Camacho-Navarro's arXiv:2012.08705 addresses \(a\)-numbers and \(p\)-ranks primarily in a different nonhyperelliptic genus-four setting, not this explicit family in characteristic \(23\).

## Limitations
The theorem determines the \(a\)-number, \(p\)-rank, and parameter/isomorphism-class counts, but not the complete Ekedahl--Oort types or all torsion group schemes. The all-prime formula depends on the computable gcd degree \(g_p\), not an explicit closed formula in \(p\). The characteristic-23 classification is exact. Novelty is based on inspected accessible sources and mathematical-record searches; an equivalent calculation in older or unindexed literature cannot be excluded. There has been no independent audit.

## References
1. Ryo Ohashi and Momonari Kudo, *Computing superspecial hyperelliptic curves of genus 4 with automorphism group properly containing the Klein 4-group*, arXiv:2312.16858, version 1, publicly submitted 2023-12-28; Section 3.3, Proposition 3.3.4, and Table 2. https://arxiv.org/pdf/2312.16858
2. Catalina Camacho-Navarro, *The a-number, p-rank and Cartier points of genus 4 curves*, arXiv:2012.08705, publicly submitted 2020-12-16. https://arxiv.org/abs/2012.08705
3. Standard hyperelliptic Cartier--Manin coefficient formula, used in Reference 1, Section 2 and Section 3.3.
