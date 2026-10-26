# A Segre–Veronese singular locus for the binary-quartic discriminant in characteristic three

## Finding
Let \(k\) be algebraically closed of characteristic \(3\), and let \(\mathcal D\subset\mathbb P^4_k\) be the discriminant of binary quartics. Its **reduced** singular locus has exactly two irreducible surface components: a smooth degree-two Segre quadric \(Q\) of triple-root forms and a smooth degree-four Veronese surface \(V\) of squares of quadratics. Their scheme-theoretic intersection is a smooth rational quartic \(T\), the locus of fourth powers. The triple-root parametrization of \(Q\) factors through absolute Frobenius in one factor and is purely inseparable of degree \(3\). Under the Segre identification, \(T\) is the graph of Frobenius.

## Assumptions and scope
Throughout \(k\) is algebraically closed with \(\operatorname{char}(k)=3\). Coefficients \([A:B:C:D:E]\) denote the nonzero binary quartic \(f=AX^4+BX^3Y+CX^2Y^2+DXY^3+EY^4\), up to scalar. Write \(U=AE-BD\). The projective discriminant \(\mathcal D\) is cut out by the usual homogeneous discriminant polynomial \(\Delta\), reduced modulo \(3\). The singular locus is defined by the homogeneous Jacobian ideal; only its underlying reduced subscheme is classified here.

Define \(Q=V(C,U)\subset\mathbb P^4\). Define \(V\) as the square locus parametrized by \(q=sX^2+tXY+uY^2\):
\[
[s:t:u]\longmapsto[s^2:2st:t^2+2su:2tu:u^2].
\]

## Proof
**1. The discriminant and its two singular subvarieties.** Direct expansion of the Sylvester resultant gives, in characteristic \(3\),
\[
\Delta=U^3+C^2U^2-C^3(AD^2+B^2E)+AEC^4.
\]
Its partial derivatives vanish on \(Q\), since \(C=U=0\). On substituting the displayed parametrization of \(V\), all five derivatives vanish identically (and \(\Delta\) does too); this can be verified by expansion in the polynomial ring \(\mathbb F_3[s,t,u]\), as in the accompanying checker.

**2. There are no other singular points.** Over an algebraically closed field, each quartic on \(\mathcal D\) has a root partition of type \((2,1,1)\), \((3,1)\), \((2,2)\), or \((4)\). At a point of type \((2,1,1)\), the three distinct root supports admit disjoint étale local neighborhoods in the relative root divisor. Coprime factorization is therefore étale locally a product of one monic quadratic and two distinct linear factors. The product-discriminant identity says that the quartic discriminant is a unit times the discriminant of the quadratic. The latter has a simple zero along a double root, since its usual local form is \(b^2-4ac\) with \(4\ne0\) in characteristic \(3\). Thus every \((2,1,1)\) point is smooth on \(\mathcal D\). The other partitions belong respectively to \(Q\), \(V\), and \(Q\cap V\). Hence \(\operatorname{Sing}(\mathcal D)_{\rm red}=Q\cup V\) as closed reduced subsets, with no further components.

**3. The geometry of the components.** Write \(L=sX+tY\) and \(M=uX+vY\). The Frobenius identity gives
\[
L^3M=s^3uX^4+s^3vX^3Y+t^3uXY^3+t^3vY^4.
\]
Thus \([L],[M]\mapsto [L^3M]\) has image \(Q\); it is the standard Segre embedding preceded by Frobenius on its first \(\mathbb P^1\) factor, because the coefficient matrix \(\left(\begin{smallmatrix}A&B\\D&E\end{smallmatrix}\right)\) has rank one. Over \(k\), Frobenius is a degree-three purely inseparable morphism on \(\mathbb P^1\), so \(Q\cong\mathbb P^1\times\mathbb P^1\) is a smooth quadric surface of degree \(2\). The square map \([q]\mapsto[q^2]\) is a closed immersion in characteristic not two: it is injective on geometric points, its differential has no projective kernel because \(2q\,\delta q\) is proportional to \(q^2\) only if \(\delta q\) is proportional to \(q\), and the projective morphism is proper. Its hyperplane bundle is \(\mathcal O_{\mathbb P^2}(2)\); hence \(V\cong\mathbb P^2\) is a degree-four Veronese surface.

**4. The intersection is the Frobenius graph.** Substituting the square coordinates into \(C\) and \(U\), in characteristic \(3\), gives
\[
C|_V=t^2-su,\qquad U|_V=-su(t^2-su).
\]
Thus the pullback of the *scheme-theoretic* intersection ideal \((C,U)\) to \(V\) equals \((t^2-su)\). This equation defines a smooth plane conic. Its image in \(V\) under the degree-two Veronese embedding is a smooth rational quartic. Every point corresponds to a quadratic with repeated root, hence a fourth power \(L^4\). On \(Q\) its two Segre parameters are \(([L]^3,[L])\), so the intersection is the graph of absolute Frobenius, not merely a set-theoretic coincidence. This proves all assertions.

## Verification
The accompanying self-contained `quartic_verify.py` requires SymPy and performs exact polynomial reduction modulo \(3\): it recomputes \(\Delta\), verifies the displayed formula, all five partial-derivative vanishings on the parameterized components, and the scheme-intersection identities. Separately, it enumerates all \(121\) projective \(\mathbb F_3\)-points of \(\mathbb P^4\): the singular support has \(25\) points, with \(16\) on \(Q\), \(13\) on \(V\), and \(4\) on their intersection. This finite-field enumeration only cross-checks the geometric proof and is not used to infer exhaustiveness over \(k\).

## Relationship to prior work
Chipalkatti [1] studies coincident-root loci, including the binary-quartic discriminant, over \(\mathbb C\). Kurmann [2] develops equations and singularities of coincident-root loci in characteristic zero. Katz [3] studies discriminant geometry over \(\mathbb R\) and \(\mathbb C\). These treatments supply the root-partition perspective but do not establish the characteristic-three collapse of the triple-root surface to a Segre quadric, the Frobenius graph intersection, or the precise reduced singular-support union here. General characteristic-zero implications cannot simply be specialized across the characteristic-three inseparable degeneration.

## Limitations
The theorem identifies the reduced projective singular locus and the scheme-theoretic intersection of its two reduced components. It does not assert that the full Jacobian singular scheme is reduced, determine its embedded components or multiplicities, or compute normalization and conductor. Literature searches cannot rule out equivalent formulas under other modular-invariant coordinates; historical coverage may be incomplete. Independent verification has not been performed.

## References
[1] J. V. Chipalkatti, *On equations defining coincident root loci*, arXiv:math/0110224 (first posted 2001-10-19), https://arxiv.org/abs/math/0110224.

[2] S. Kurmann, *Some remarks about equations defining coincident root loci*, arXiv:1108.4532 (2011), https://arxiv.org/abs/1108.4532.

[3] G. Katz, *How tangents solve algebraic equations, or a remarkable geometry of discriminant varieties*, arXiv:math/0211281 (2002), https://arxiv.org/abs/math/0211281.
