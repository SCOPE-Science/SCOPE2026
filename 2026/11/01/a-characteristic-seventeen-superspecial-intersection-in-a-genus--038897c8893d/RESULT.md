# A characteristic-seventeen superspecial intersection in a genus-two elliptic-quotient pencil

## Finding

Let \(k=\overline{\mathbb F}_{17}\). For every \(t\in k\setminus\{0,1\}\), let \(C_t\) denote the smooth projective curve with affine model
\[
 C_t:\qquad y^2=(x^2-1)(x^4-t).
\]
The curve has genus two. Its Jacobian has the following complete geometric Newton, \(17\)-rank and \(a\)-number stratification, with the parameters understood as **marked coefficient values**:

| Exact condition on \(t\) | Geometric \(17\)-rank | \(a\)-number | Newton slopes |
| --- | ---: | ---: | --- |
| \(t^2-t+1=0\) | \(0\) | \(2\) | \((1/2,1/2,1/2,1/2)\) |
| \(t\in\{5,7,11,14\}\) | \(1\) | \(1\) | \((0,1/2,1/2,1)\) |
| All remaining smooth parameters | \(2\) | \(0\) | \((0,0,1,1)\) |

The two distinct roots of \(t^2-t+1\) are defined over \(\mathbb F_{17^2}\), are interchanged by Frobenius, and are not in \(\mathbb F_{17}\). At each such root **both elliptic quotients are supersingular and have the same \(j\)-invariant \(8\)**. The four rank-one values are rational over \(\mathbb F_{17}\). Consequently the marked smooth-parameter rank counts are \((0,4,11)\) over \(\mathbb F_{17}\), and \((2,4,281)\) over \(\mathbb F_{17^2}\), in rank order \((0,1,2)\).

Moreover, among odd primes for which this integral pencil has smooth fibers, \(17\) is the smallest prime with a smooth geometrically superspecial fiber: the simultaneous Hasse-zero locus is empty for \(p=3,5,7,11,13\).

## Assumptions and scope

All rank and Newton-polygon assertions are geometric, over an algebraically closed field of characteristic \(17\). The parameter condition \(t\notin\{0,1\}\) is necessary and sufficient for the sextic to be squarefree. The count is of **parameters in the chosen equation**, not of distinct unmarked genus-two isomorphism classes. Indeed inversion \(x\mapsto1/x\), accompanied by an appropriate rescaling of \(y\), gives \(C_t\cong C_{1/t}\) geometrically. In particular the four rank-one parameter values pair as \((5,7)\) and \((11,14)\), and the two rank-zero values are also related by inversion. No count of all genus-two curves or of all superspecial curves is asserted.

The first-prime assertion concerns only this family at odd primes; the displayed equation does not supply a smooth hyperelliptic double-cover model in characteristic two.

## Proof

**1. Smoothness and complementary elliptic quotients.** For characteristic different from two, \((x^2-1)(x^4-t)\) has six distinct roots exactly when \(t\neq0,1\), hence \(C_t\) has genus two. The involutions \((x,y)\mapsto(-x,y)\) and \((x,y)\mapsto(-x,-y)\) yield elliptic quotients
\[
 E_{1,t}:v^2=(u-1)(u^2-t),\qquad
 E_{2,t}:w^2=u(u-1)(u^2-t),
\]
with maps \((u,v)=(x^2,y)\) and \((u,w)=(x^2,xy)\). Their differential pullbacks are \(2x\,dx/y\) and \(2\,dx/y\). These span the two-dimensional space of holomorphic differentials on \(C_t\), so the maps induce an isogeny \(\operatorname{Jac}(C_t)\sim E_{1,t}\times E_{2,t}\). Therefore Newton slopes and \(17\)-rank are obtained from the two elliptic factors.

**2. Cartier–Manin matrix.** Put \(f_t(x)=(x^2-1)(x^4-t)\) and expand \(f_t(x)^8=\sum c_j(t)x^j\) in characteristic \(17\). On the standard hyperelliptic differential basis \((dx/y,x\,dx/y)\), the Cartier–Manin coefficient matrix (up to the usual Frobenius-root convention) has entries \(c_{17i-j}\) for \(1\le i,j\le2\). Because \(f_t\) is even, both off-diagonal entries vanish. The diagonal polynomials are
\[
 A(t):=c_{16}(t)=t^4(t+3)(t-5)(t^2-t+1),
\]
\[
 B(t):=c_{32}(t)=2(t+6)(t-7)(t^2-t+1).
\]
The exact expansions in \(\mathbb F_{17}[t]\) are
\[
 A=t^8-3t^7+5t^6-4t^5+2t^4,
 \quad B=2t^4-4t^3+5t^2-3t+1.
\]
The matrix is diagonal, hence iterated Frobenius has stable rank equal to the number of nonzero diagonal entries (over the algebraic closure). Therefore the geometric \(17\)-rank is \(0\), \(1\), or \(2\) according as both, exactly one, or neither of \(A,B\) vanish. The \(a\)-number is \(2-\operatorname{rank}(M)\).

**3. Exhaustion and Newton polygons.** The polynomial gcd is
\[
 \gcd(A,B)=t^2-t+1.
\]
Its discriminant is \(-3=14\in\mathbb F_{17}\), a nonsquare, and neither of its roots is a singular parameter. Its two roots are therefore the complete common-zero locus. After removing these common roots and the excluded parameter \(t=0\), the remaining simple roots are exactly \(t=-3,5,-6,7\), i.e. \(t=14,5,11,7\). No further roots occur. A product of two elliptic curves with ranks \(0,0\), \(0,1\), or \(1,1\) has respectively the three slope patterns displayed above. At a common zero the Cartier operator itself vanishes, so the abelian surface is superspecial, not merely supersingular.

**4. Elliptic \(j\)-invariants and arithmetic.** Direct cubic and quartic invariant calculations give
\[
 j(E_{1,t})=\frac{64(3t+1)^3}{t(t-1)^2},\qquad
 j(E_{2,t})=\frac{64(t+3)^3}{(t-1)^2}.
\]
Reduction modulo the ideal \((17,t^2-t+1)\) sends both fractions to \(8\); their denominators are units there. Thus the two elliptic quotients are isomorphic over \(k\) at each superspecial parameter, and their common \(j\)-invariant is \(8\). The quadratic has precisely two roots in \(\mathbb F_{17^2}\) and none in \(\mathbb F_{17}\). Since the other four exceptional values are rational, the stated counts follow by subtraction from \(17-2=15\) and \(17^2-2=287\).

**5. First odd prime.** For each \(p\in\{3,5,7,11,13\}\), form the same two diagonal Hasse polynomials by extracting the coefficients of \(x^{p-1}\) and \(x^{2p-2}\) in \(f_t(x)^{(p-1)/2}\) modulo \(p\). Exact Euclidean division shows that their gcd is \(1\), so no parameter of this pencil has Cartier matrix zero in these characteristics. The characteristic-seventeen factorization supplies such parameters, proving the qualified first-prime statement.

## Verification

The standalone script `verify_bielliptic.py` requires only Python's standard library. It forms the bivariate expansion of \(f_t(x)^{(p-1)/2}\) over each finite field, checks the characteristic-seventeen factorization and polynomial gcd, checks the nonsquare quadratic discriminant, enumerates all prime-field smooth parameters, certifies the two quotient \(j\)-invariant congruences modulo \(t^2-t+1\), and checks that the gcd is one for the five preceding odd primes. Its successful execution output is included as `verification_output.txt`. A separate symbolic-algebra calculation independently reproduced both displayed Hasse polynomials and their factorizations. These are exact finite polynomial calculations; the geometric extension-field classification follows from the proof and is not inferred from sample point counts.

## Relationship to prior work

The existence of complementary degree-two elliptic quotients on genus-two curves with an extra involution, their normal forms, and the corresponding elliptic \(j\)-invariants are classical; see Shaska–Völklein (2001), especially Sections 1–2, and Shaska (2012), Section 5. The genus-two superspeciality criterion from the Cartier matrix is also standard. Harashita–Yamamoto (2024/2025) prove a general multiplicity-one property of the superspecial ideal in the three-dimensional Rosenhain parameter space; this does not specify the characteristic-seventeen intersections in the present one-dimensional equation. Ando (2025) counts superspecial members of a different special family with larger reduced symmetry, rather than determining these marked parameters. The contribution here is the **specific arithmetic collision of the two Hasse factors in this one-dimensional pencil**, its precise Newton stratification and extension-field arithmetic, the common elliptic \(j\)-invariant, and its first occurrence at prime \(17\). These data were not found in the relevant full-text sections inspected; absence from those sources is not proof of historical uniqueness.

## Limitations

This is an exact result about the marked pencil, not a classification of superspecial genus-two moduli points. The two superspecial coefficient values are geometrically isomorphic by inversion. The claimed first-prime property is restricted to odd primes and this fixed equation. A priority risk remains from specialized classifications or databases of superspecial genus-two curves and unindexed explicit tables. The proof does not give an integral isogeny classification or determine all endomorphism rings. Independent scientific validation has not been performed.

## References

1. T. Shaska and H. Völklein, *Elliptic subfields and automorphisms of genus 2 function fields*, first publicly posted 2001-07-19, arXiv:math/0107142, https://arxiv.org/abs/math/0107142 .
2. T. Shaska, *Genus two curves covering elliptic curves: a computational approach*, first publicly posted 2012-09-14, arXiv:1209.3187, https://arxiv.org/abs/1209.3187 .
3. S. Harashita and Y. Yamamoto, *The multiplicity-one theorem for the superspeciality of curves of genus two*, first publicly posted 2024-09-20, arXiv:2409.13212, https://arxiv.org/html/2409.13212v2 .
4. C. Ando, *The Lang–Trotter conjecture on average for genus-2 curves with Klein-4 reduced automorphism group*, 2025, DOI:10.1007/s40993-025-00665-3, https://link.springer.com/article/10.1007/s40993-025-00665-3 .
