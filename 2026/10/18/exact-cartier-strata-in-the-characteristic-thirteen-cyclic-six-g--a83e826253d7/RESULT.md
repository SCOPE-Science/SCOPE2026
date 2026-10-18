# Exact Cartier strata in the characteristic-thirteen cyclic-six genus-three pencil

## Finding
Let \(k=\overline{\mathbf F}_{13}\), and for \(t\in k\setminus\{0,1\}\) let \(C_t\) be the smooth projective curve with affine model
\[
C_t:\qquad y^2=x(x^3-1)(x^3-t).
\]
Write \(f_{13}(C_t)\) for the \(13\)-rank of its Jacobian and \(a(C_t)\) for its \(a\)-number. Define polynomials in \(\mathbf F_{13}[T]\):
\[
\begin{aligned}
A(T)&=T^2+5T+1,\\
B(T)&=T^2+4T-4,\\
D(T)&=T^2-6T+1,\\
E(T)&=T^2-T+3.
\end{aligned}
\]
Then every \(C_t\) has genus three, and the complete geometric stratification is
\[
\bigl(f_{13}(C_t),a(C_t)\bigr)=
\begin{cases}
(1,2),& A(t)=0,\\
(2,1),& B(t)D(t)E(t)=0,\\
(3,0),&\text{otherwise}.
\end{cases}
\]
The four displayed quadratics are pairwise distinct and irreducible over \(\mathbf F_{13}\). Hence exactly two geometric parameters have \(13\)-rank one, exactly six have rank two, and all eight nonordinary parameters lie in \(\mathbf F_{13^2}\setminus\mathbf F_{13}\). No curve in the pencil has rank zero or \(a\)-number three. Every parameter in \(\mathbf F_{13}\setminus\{0,1\}\) is ordinary; more generally, no parameter defined over an odd-degree extension of \(\mathbf F_{13}\) is nonordinary. Under the explicit parameter involution \(t\mapsto t^{-1}\), the eight exceptional parameters form four two-element orbits (one of rank one and three of rank two). This last statement counts orbits of the parameter involution, **not** all abstract curve-isomorphism classes.

## Assumptions and scope
The ground field is algebraically closed of characteristic \(13\). Parameter restrictions \(t\ne0,1\) are essential: the degree-seven polynomial \(x(x^3-1)(x^3-t)\) then has seven distinct roots because \(13\ne3\), and its smooth projective hyperelliptic completion has genus \((7-1)/2=3\). The family is the hyperelliptic model of the cyclic-six four-branch cover \(Y^6=u(u-1)^3(u-t)^3\): taking \(x=Y^2/((u-1)(u-t))\) gives \(x^3=u\) and the displayed equation with \(y=Y\). All rank and count assertions are over the specified fields and refer to parameters, not necessarily distinct geometric isomorphism classes.

## Proof
For \(f(x)=x(x^3-1)(x^3-t)=x^7-(1+t)x^4+tx\), a basis of holomorphic differentials is \(\omega_j=x^{j-1}dx/y\) for \(1\le j\le3\). Write \(f(x)^6=\sum_k c_kx^k\). The standard hyperelliptic Cartier formula gives matrix coefficients (up to the coefficientwise inverse Frobenius, which preserves zero loci) \(H_{ij}=c_{13i-j}\). Every exponent in \(f^6\) is divisible by three, while \(13i-j\equiv i-j\pmod3\); thus \(H_{ij}=0\) unless \(i=j\). Direct binomial expansion gives
\[
H(t)=\operatorname{diag}\left(
2t^4 A(t),\quad B(t)D(t)E(t),\quad2A(t)
\right).
\]
Indeed, the middle entry is
\[
t^6-3t^5+4t^4-3t^3+4t^2-3t+1,
\]
which factors as \(BDE\) in \(\mathbf F_{13}[t]\). The other entries are \(2t^6-3t^5+2t^4\) and \(2t^2-3t+2\), respectively. Since \(t\ne0\), the first and third diagonal entries vanish simultaneously precisely when \(A(t)=0\).

The discriminants of \(A,B,D,E\), respectively, are \(8,6,6,2\) modulo \(13\). The nonzero squares of \(\mathbf F_{13}\) are \(1,3,4,9,10,12\), so all four quadratics are irreducible. They are distinct, hence pairwise coprime. Their values at \(t=0,1\) are nonzero. Thus exactly two parameter values annihilate both outer diagonal entries, exactly six others annihilate only the middle entry, and no permissible parameter annihilates all three.

For a diagonal semilinear Cartier operator, each nonzero diagonal entry remains nonzero in every Frobenius-twisted iterate, while each zero entry stays zero. Therefore the stable Cartier rank (the Jacobian's \(13\)-rank) equals the ordinary matrix rank. The \(a\)-number equals genus minus Cartier rank. Applying these facts to the mutually disjoint zero loci above proves the three cases.

Each irreducible quadratic has its two distinct roots in \(\mathbf F_{13^2}\) and no root in \(\mathbf F_{13}\), giving the stated parameter counts and field-of-definition assertions. A quadratic extension is contained in \(\mathbf F_{13^n}\) exactly when \(2\mid n\), yielding the odd-extension assertion.

Finally, choose \(c\in k\) with \(c^3=t\), substitute \(x=cw\), and rescale \(y\) by a square root of \(ct^2\). Then \(C_t\cong C_{1/t}\) over \(k\), since
\[
(ct^2)^{-1}(cw)((cw)^3-1)((cw)^3-t)
=w(w^3-1)(w^3-t^{-1}).
\]
The reciprocal polynomials of \(A,D\) are themselves, while \(T^2B(T^{-1})=-4E(T)\); hence the exceptional locus is preserved by inversion. None of its parameters equals \(\pm1\), so all inversion orbits have size two. The rank-one roots form one such orbit; the other six roots form three.

## Verification
The standalone \(\texttt{verify.py}\) reconstructs \(f^6\) as a bivariate polynomial in \(x,t\) over \(\mathbf F_{13}\), checks the three Cartier entries and factorizations without relying on symbolic-factorization software, and evaluates all \(169\) elements of \(\mathbf F_{13^2}\) using the field \(\mathbf F_{13}[u]/(u^2-2)\). It verifies \(2\) rank-one and \(6\) rank-two parameters, \(159\) ordinary permitted parameters in that field, and four inversion orbits. These finite calculations check the explicit identities; the argument above proves the classification for all \(t\in k\setminus\{0,1\}\), not only for \(\mathbf F_{13^2}\).

## Relationship to prior work
Cavalieri and Pries, *Mass formula for non-ordinary curves in one dimensional families* (arXiv:2308.14891, first posted 28 August 2023), §8, introduce the even-degree cyclic covers with inertia \((1,d/2,d/2,d-1)\), give the mass formula, and explicitly state that the \(a\)-numbers of the curves in this family are not known in general. The present \(d=6\), characteristic-\(13\) case determines the full positive-rank stratification and its parameter zero loci; a weighted nonordinary mass does not specify these. Borges and Gonçalves, *The \(p\)-rank of curves of Fermat type* (arXiv:2212.03987), give a combinatorial formula for the different Fermat-type family \(y^m=x^n+1\); their general statements do not imply the four-polynomial parameter stratification of the four-branch pencil above. The Cartier coefficient formula used here is classical.

## Limitations
The theorem is for this particular one-parameter family and characteristic \(13\), and establishes neither Newton polygons nor full geometric automorphism/isomorphism classifications. The four inversion orbits are not asserted to exhaust geometric isomorphism classes. No claim is made that the cyclic-cover mass formula or the existence of positive-rank strata in genus three is new. Literature searches cannot rule out an unindexed equivalent computation; the proof and code have not undergone independent external validation.

## References
1. R. Cavalieri and R. Pries, *Mass formula for non-ordinary curves in one dimensional families*, arXiv:2308.14891 (initial version 2023-08-28), especially §8, Eq. (28), Corollary 8.1.
2. H. Borges and C. Gonçalves, *The p-rank of curves of Fermat type*, arXiv:2212.03987 (2022), Introduction and §2.
3. N. Yui, *On the Jacobian varieties of hyperelliptic curves over fields of characteristic p > 2*, J. Algebra 52 (1978), 378–410 (classical Cartier–Manin formula).
