# An unbounded infinitesimal symmetry excess for truncated complete intersections in characteristic two

## Finding

Let \(k\) be any field of characteristic \(2\) and \(n\ge3\) an integer. For the unital commutative Artin algebra
\[
R_n(k)=k[x,y]/(x^2,y^n),
\]
every unital \(k\)-algebra automorphism has the **unique** generator images
\[
\varphi(x)=h(y)+xj(y),\qquad \varphi(y)=f(y)+xg(y),
\]
where, in \(k[y]/(y^n)\),
\[
 h\in y^{\lceil n/2\rceil}k[y]/(y^n),\quad j(0)\ne0,\quad
 f\in yk[y]/(y^n),\quad f'(0)\ne0,
\]
and \(g\in yk[y]/(y^n)\) when \(n\) is odd, whereas \(g\in k[y]/(y^n)\) is arbitrary when \(n\) is even. Conversely every such choice defines an automorphism.

Set
\[
 d_n=3n-4+\lfloor n/2\rfloor+\mathbf1_{2\mid n}.
\]
The reduced automorphism variety is geometrically
\[
 \underline{\operatorname{Aut}}_k(R_n)_{\mathrm{red}}\cong
 (\mathbb G_m)^2\times\mathbb A_k^{d_n}.
\]
The full derivation space and hence the tangent space of the automorphism scheme at the identity has dimension
\[
\dim_k\operatorname{Der}_k(R_n)=
\begin{cases}4n-2,&n\text{ odd},\\4n,&n\text{ even}.\end{cases}
\]
Thus the tangent dimension exceeds the dimension of the reduced algebraic group, which is \(d_n+2\), by exactly
\[
 \boxed{\lfloor n/2\rfloor+1}.
\]
In particular these automorphism group schemes are non-smooth, with unbounded excess as \(n\) grows. Over every finite field \(\mathbb F_q\) of characteristic two,
\[
\#\operatorname{Aut}_{\mathbb F_q}(R_n)=(q-1)^2q^{d_n}.
\]

## Assumptions and scope

The algebra is associative, commutative, unital and finite-dimensional, with \(\dim_k R_n=2n\). Homomorphisms fix the ground field and the identity. The parameter \(n\) satisfies \(n\ge3\); the boundary \(n=2\) has a different generator symmetry and is not included. The field may be finite, infinite or imperfect, provided its characteristic is two. The geometric assertion describes the **reduced** automorphism variety only. No assertion about a product decomposition of the full possibly nonreduced automorphism scheme is made.

## Proof

**1. Generator normal form.** The monomials \(y^i,xy^i\), \(0\le i<n\), are a \(k\)-basis. The unique maximal ideal \(\mathfrak m=(x,y)\) is characteristic under every algebra automorphism. Therefore both generator images have zero constant term and admit uniquely determined expansions \(X=h(y)+xj(y)\) and \(Y=f(y)+xg(y)\), with \(h,f\in yk[y]/(y^n)\) and \(j,g\in k[y]/(y^n)\).

**2. Relation \(X^2=0\).** In characteristic two \(X^2=h(y)^2\), because \(x^2=0\). If \(h\ne0\), its lowest term has degree \(s\), and its square has lowest term of degree \(2s\) with nonzero coefficient. Thus \(X^2=0\) is equivalent to \(2s\ge n\), or \(h\in y^{\lceil n/2\rceil}k[y]/(y^n)\), with the zero polynomial allowed. This uses only that \(k\) is a field.

**3. Relation \(Y^n=0\).** The binomial theorem, \(x^2=0\), and \(f(0)=0\) give
\[
Y^n=f(y)^n+(n\bmod 2)\,x f(y)^{n-1}g(y).
\]
The first summand is zero. If \(n\) is even the second coefficient is zero. If \(n\) is odd and \(f'(0)\ne0\), then
\(f(y)^{n-1}=f'(0)^{n-1}y^{n-1}\) modulo \(y^n\), and \(Y^n=0\) is exactly \(g(0)=0\).

**4. Invertibility.** Since \(n\ge3\), Step 2 implies that \(h\) has no term of degree one. On \(\mathfrak m/\mathfrak m^2\), with ordered basis \((x,y)\), the two images have respective linear parts \(j(0)x\) and \(g(0)x+f'(0)y\). The induced determinant is \(j(0)f'(0)\). A local endomorphism of this finite-dimensional nilpotent local algebra is surjective and hence bijective exactly when it is invertible on \(\mathfrak m/\mathfrak m^2\) (successive products/Nakayama). Therefore Step 2 and Step 3 together with \(j(0),f'(0)\ne0\) are necessary and sufficient. The uniquely displayed coefficients give uniqueness.

**5. Reduced geometry and finite-field count.** The free coefficients comprise \(\lfloor n/2\rfloor\) in \(h\), \(n\) in \(j\), \(n-1\) in \(f\), and \(n-1+\mathbf1_{2\mid n}\) in \(g\). Exactly two of these, \(j(0)\) and \(f'(0)\), must be nonzero. Thus after scalar extension to any algebraically closed field, the reduced automorphism variety is the indicated split torus times affine space; this also follows by taking the radical of the coefficient relations. The same free-coefficient description holds over \(\mathbb F_q\), yielding precisely \((q-1)^2q^{d_n}\) points.

**6. Tangent space and non-smoothness.** A derivation \(D\) is determined by its freely selected values \(D(x),D(y)\in R_n\), subject to the two defining relation derivatives. In characteristic two \(D(x^2)=2xD(x)=0\) imposes no restriction. Moreover \(D(y^n)=(n\bmod2)y^{n-1}D(y)\). This vanishes identically when \(n\) is even. When \(n\) is odd, it is equivalent to the vanishing of the two coefficients of \(1\) and \(x\) in \(D(y)\), giving codimension two. Thus the tangent dimensions are as stated. The reduced group has dimension \(d_n+2\), as both torus factors have dimension one; subtraction yields \(\lfloor n/2\rfloor+1\) for both parities, which is positive and unbounded. A finite-type group scheme over a field whose identity tangent dimension exceeds its geometric dimension cannot be smooth.

## Verification

A separate dependency-free program, `verify.py`, independently multiplies polynomials in the standard monomial basis, checks the relations \(X^2=Y^n=0\), and uses the full tangent-linear determinant to exhaust all generator-image pairs over \(\mathbb F_2\) for \(n=3,4\), and over \(\mathbb F_4\) for \(n=3\). Its exact measured counts are \(64\), \(2048\), and \(36864\), agreeing with the theorem. It separately exhausts the defining derivation constraints for \(n=3,4\) over \(\mathbb F_2\), obtaining \(1024\) and \(65536\) derivations, or dimensions \(10\) and \(16\). Running `python3 verify.py` prints the final marker `ASYMMETRIC_TRUNCATION_OK`. These finite computations check small cases, not the unrestricted theorem; the proof above covers all \(n\) and fields.

## Relationship to prior work

Deo and Maitra (1997) analyze **graded** automorphisms of tensor products of truncated polynomial algebras in characteristic zero; their Theorem 3.2 does not count the unrestricted ungraded automorphisms in characteristic two or their infinitesimal defects. Ceken–Palmieri–Wang–Zhang (arXiv:1401.0793v1) give discriminant-based automorphism criteria for filtered, predominantly noncommutative algebras with associated graded domains, not this nonreduced local complete intersection. Geiß–Voigt (2004) give a nonreduced-automorphism-scheme criterion via gradings in finite-dimensional algebras; no exact parity-dependent automorphism census or tangent-dimension excess for this family is established by its accessible abstract. Díaz–Liendo–Manzano-Flores–Regeta (arXiv:2408.02197) give broad automorphism structure for finite-dimensional monomial algebras **in characteristic zero**; their stated hypothesis excludes the characteristic-two result here. Known examples of non-smooth schemes and separate classifications for algebras in which all variables are square-zero do not imply the growing defect formula for the asymmetric truncation \((x^2,y^n)\), \(n\ge3\).

## Limitations

This theorem does not compute the structure or nilpotent thickness of the **whole** automorphism scheme; it computes its reduced variety and its full tangent dimension. The parameter \(n=2\) is explicitly excluded. The historical 1997 and 2004 references establish related frameworks; specialist or unindexed results may have independently obtained particular pieces of the normal form or group counts. Self-review do not constitute independent validation.

## References

1. S. Deo and J. K. Maitra, *Automorphism groups of truncated polynomial algebras*, National Academy Science Letters 20 (1997), 74–80. Available full paper: https://www.researchgate.net/publication/266354814_Automorphism_groups_of_truncated_polynomial_algebras . The source confirms 1997 as publication year but no specific public calendar day.
2. C. Geiß and D. Voigt, *Non-reduced automorphism schemes*, Journal of Pure and Applied Algebra 193 (2004), 123–127, https://doi.org/10.1016/j.jpaa.2004.03.004 . Abstract consulted; full text was not accessible.
3. S. Ceken, J. H. Palmieri, Y. Wang and J. Zhang, *The discriminant controls automorphism groups of noncommutative algebras*, arXiv:1401.0793v1, first public 2014-01-04, https://arxiv.org/abs/1401.0793 . Complete primary HTML examined.
4. R. Díaz, A. Liendo, G. Manzano-Flores and A. Regeta, *The Automorphism groups of zero-dimensional monomial algebras*, arXiv:2408.02197v1, first public 2024-08-05, https://arxiv.org/abs/2408.02197 . Primary HTML inspected, including main result and characteristic-zero hypothesis.
