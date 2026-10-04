# Exact center and PI degree four for a characteristic-two Bell–Li Ore subfamily
## Finding
Let \(K\) be an algebraically closed field of characteristic \(2\), fix \(\gamma\in K^\times\), and define
\[
A_\gamma=K\langle x,y,z\rangle/([x,y]-z,[x,z]-\gamma y,[y,z]).
\]
Then
\[
Z(A_\gamma)=K[y^2,z^2,x^4+\gamma x^2].
\]
The algebra \(A_\gamma\) is free of rank \(16\) over this center, with central-module basis
\[
\{y^\epsilon z^\eta x^j:\epsilon,\eta\in\{0,1\},\ 0\le j<4\}.
\]
Consequently the central quotient division algebra has dimension \(16\) over its center field and the PI degree of \(A_\gamma\) is \(4\).

## Assumptions and scope
This is the \(f=0\), \(\gamma\ne0\), characteristic-two subfamily of Bell and Li's family \([x,y]=z\), \([x,z]=\gamma y\), \([y,z]=f(x)\). The field is assumed algebraically closed only to stay within the motivating paper's standing hypotheses; the center calculation itself uses only characteristic \(2\) and \(\gamma\ne0\). The claim does not cover \(\gamma=0\) or nonzero \(f\).

## Proof
Write \(R=K[y,z]\) and let \(\delta\) be the derivation of \(R\) given by \(\delta(y)=z\) and \(\delta(z)=\gamma y\). Bell and Li identify the \(f=0\) algebra as the Ore extension \(A_\gamma=R[x;\delta]\), so its PBW monomials form a basis and it is a domain.

Set \(c=x^4+\gamma x^2\). In characteristic \(2\), \((\operatorname{ad}x)^2(y)=\gamma y\) and \((\operatorname{ad}x)^2(z)=\gamma z\). Hence \((\operatorname{ad}x)^4+\gamma(\operatorname{ad}x)^2\) vanishes on \(y\) and \(z\), while it plainly vanishes on \(x\). Thus \(c\) is central. This is also the characteristic-two specialization of the central element constructed in Bell and Li's proof of their PI theorem for family (2).

Because \(x^4=c+\gamma x^2\), every element of \(A_\gamma\) has a unique expression
\[
t=r_0+r_1x+r_2x^2+r_3x^3,\qquad r_i\in R[c].
\]
Uniqueness follows from the PBW basis by comparing the largest exponent of \(x\) in each congruence class modulo \(4\).

For \(a\in R\), the Ore relation gives \([x,a]=\delta(a)\). In characteristic \(2\),
\[
[x^2,a]=\delta^2(a),\qquad [x^3,a]=\delta(a)x^2+\delta^2(a)x+\delta^3(a).
\]
If \(t\) commutes with \(y\), the coefficient of \(x^2\) in \([t,y]\) is \(r_3z\). Since \(A_\gamma\) is a domain, \(r_3=0\). The equations \([t,y]=[t,z]=0\) then reduce to
\[
r_1z+r_2\gamma y=0,\qquad r_1\gamma y+r_2\gamma z=0.
\]
Their determinant is \(\gamma(z^2+\gamma y^2)\), a nonzero element of the polynomial domain \(R[c]\). Therefore \(r_1=r_2=0\), and the centralizer of \(R\) is exactly \(R[c]\).

It remains to impose commutation with \(x\). Let \(B=K[y^2,z^2]\). Since characteristic is \(2\), \(R\) is a free \(B\)-module with basis \(1,y,z,yz\), and \(\delta\) kills \(B\). Writing
\[
r=a+by+dz+eyz,\qquad a,b,d,e\in B,
\]
we obtain
\[
\delta(r)=bz+d\gamma y+e(z^2+\gamma y^2).
\]
The four displayed \(B\)-basis components are independent, so \(\delta(r)=0\) forces \(b=d=e=0\). Hence \(R^\delta=B\), and therefore
\[
Z(A_\gamma)=B[c]=K[y^2,z^2,x^4+\gamma x^2].
\]

The three central generators are algebraically independent: their leading PBW monomials are respectively \(y^2\), \(z^2\), and \(x^4\). Reduction of exponents modulo \(2,2,4\) now gives the stated sixteen-element basis over the center, with linear independence again read from PBW leading monomials.

Let \(F=\operatorname{Frac}Z(A_\gamma)\). The central localization \(Q=A_\gamma\otimes_{Z(A_\gamma)}F\) is a \(16\)-dimensional domain over \(F\), hence a division algebra. Its center is exactly \(F\): if \(a/s\) is central in \(Q\), then \([a,b]=0\) for every \(b\in A_\gamma\), because localization is injective, so \(a\in Z(A_\gamma)\). Thus \(Q\) is central division of dimension \(16=4^2\), and the PI degree is \(4\).

## Verification
The proof is symbolic and does not infer an infinite statement from finite testing. The critical checks are: the Ore-extension PBW basis; centrality of \(x^4+\gamma x^2\); the four-term reduction in the \(x\)-exponent; the two-by-two centralizer determinant \(\gamma(z^2+\gamma y^2)\ne0\); the exact invariant-ring computation \(R^\delta=K[y^2,z^2]\); and the sixteen PBW residue classes modulo the central exponents. No external computation is needed for these steps.

## Relationship to prior work
Bell and Li introduce the three-variable filtered-deformation family containing \(A_\gamma\), record the \(f=0\) Ore-extension description, and prove that the family is PI in positive characteristic. In characteristic \(2\), their proof explicitly produces \(x^4+\gamma x^2\) as a central element. Their paper does not state the full center of this subfamily, its center rank, or its exact PI degree.

Brown and Zhang recall the general prime-characteristic fact that enveloping algebras are finite over their centers and study PI degrees of iterated Hopf Ore extensions, obtaining broad power-of-the-characteristic constraints. Those results do not determine this center or the exact degree \(4\). Work of de Jesus and Schneider gives explicit centers for small-dimensional nilpotent Lie algebras, but the Lie algebra here is nonnilpotent when \(\gamma\ne0\). The generalized-Weyl-algebra center results of Mamani-Velasco and Tikaradze cited in the search are formulated for characteristic \(p>2\), so they do not cover this characteristic-two case.

## Limitations
The theorem is restricted to \(f=0\), \(\gamma\ne0\), and characteristic \(2\). It does not classify centers for the full Bell–Li family, and it does not address representations or Azumaya loci. Older solvable-Lie enveloping-algebra literature may encode the same calculation under different classification notation; targeted relation, center, PI-degree, Ore-extension, and Lie-algebra searches did not locate such a statement. Independent audit has not been performed.

## References
1. J. Bell and B. Li, “Filtered deformations of three-variable polynomial algebras,” arXiv:2609.06710v1, 2026.
2. K. A. Brown and J. J. Zhang, “Iterated Hopf Ore extensions in positive characteristic,” Journal of Noncommutative Geometry 16 (2022), DOI 10.4171/JNCG/459.
3. I. de Jesus and H. Schneider, “The center of the universal enveloping algebras of small-dimensional nilpotent Lie algebras in prime characteristic,” arXiv:2111.13432.
4. D. Mamani-Velasco and A. Tikaradze, “Center and derivations of generalized Weyl algebras over \(\mathbb Z/p^n\mathbb Z\),” arXiv:2606.04183, 2026.
