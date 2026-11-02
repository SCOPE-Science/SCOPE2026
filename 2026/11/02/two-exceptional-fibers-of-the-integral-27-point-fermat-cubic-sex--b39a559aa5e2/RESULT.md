# Two exceptional fibers of the integral 27-point Fermat-cubic sextactic divisor

## Finding

Consider the projective intersection over the integers
\[
\mathscr Z=V(F,G)\subset\mathbb P^2_{\mathbb Z},\qquad
F=X^3+Y^3+Z^3,\quad
G=(X^3-Y^3)(Y^3-Z^3)(Z^3-X^3).
\]
The structural morphism \(\mathscr Z\to\operatorname{Spec}\mathbb Z\) is finite flat of degree \(27\). For each algebraically closed residue field \(k\) of characteristic \(p\), the geometric fiber has exactly these possibilities:

* For \(p\ne2,3\), there are \(27\) distinct reduced points, the transverse intersections of the smooth cubic with the three cubics defined by equalities of coordinate cubes.
* For \(p=2\), the fiber is the triple Cartier divisor of the nine reduced flex points of the smooth Fermat cubic. Each completed local algebra is \(k[[t]]/(t^3)\). Three support points are rational over \(\mathbb F_2\); the other six are in three conjugate pairs over \(\mathbb F_4\). Upon choosing any flex as elliptic origin, this divisor is exactly the residual effective Cartier divisor \(E[6]-E[3]\) of the multiplication-by-six kernel minus the multiplication-by-three kernel, where \(E[6]\) and \(E[3]\) mean the full finite group schemes.
* For \(p=3\), the fiber has the unique geometric support point \([1:1:1]\), whose completed local algebra is \(k[[u,v]]/(u^3,v^9)\). It is a Gorenstein length-\(27\) complete intersection with local Hilbert function \((1,2,3,3,3,3,3,3,3,2,1)\).

Consequently \(2\) and \(3\) are the only exceptional rational primes for geometric reducedness of this fixed integral intersection.

## Assumptions and scope

All equations are the primitive integer polynomials displayed above. In characteristic zero, their common geometric zero scheme is the classical configuration of \(27\) proper sextactic points of the Fermat cubic; this identification and the original equations are earlier work of Szemberg and Szpond. The statements in positive characteristic concern the base change of these fixed equations, **not** an intrinsically reconstructed positive-characteristic 2-Hessian or a characteristic-three elliptic curve. Scheme-theoretic fiber and local length refer to the complete intersection, rather than to the reduced support.

## Proof

**Flatness and the degree.** For every field \(k\), \(F\) and \(G\) have no common irreducible curve component in \(k[X,Y,Z]\). If the characteristic is not \(3\), the cubic \(F\) is smooth and geometrically irreducible, and is not any factor of \(G\). In characteristic \(3\), \(F=(X+Y+Z)^3\), while \(G=((X-Y)(Y-Z)(Z-X))^3\); the displayed linear form \(X+Y+Z\) is not a factor of \(G\). Thus \(G\) is a non-zero-divisor on each geometric fiber of the relative Cartier hypersurface \(V(F)\subset\mathbb P^2_{\mathbb Z}\). Fiberwise regularity of these two relative effective Cartier divisors gives flatness of their intersection over \(\mathbb Z\). Every geometric fiber is a zero-dimensional complete intersection of degrees \(3\) and \(9\), hence has length \(27\) by Bézout. Properness and zero-dimensional fibers imply finiteness. This proves finite flatness of degree \(27\).

**Characteristics other than \(2\) and \(3\).** At a common zero, at least one of the three conditions \(X^3=Y^3\), \(Y^3=Z^3\), \(Z^3=X^3\) holds. For example, \(X^3=Y^3\) and \(F=0\) imply \(Z^3=-2X^3\). Since \(p\ne2,3\), all three coordinates are nonzero; there are exactly \(3\) choices of \(Y/X\) and \(3\) choices of \(Z/X\), totaling \(9\) points. The other two equality conditions likewise contribute \(9\) points each. Their supports are disjoint: satisfying two equalities forces equality of all three cubes and thus \(3X^3=0\), impossible. At a point with \(X^3=Y^3\), the gradient of \(X^3-Y^3\) has zero \(Z\)-component while the gradient of \(F\) has nonzero \(Z\)-component, so the intersection is transverse. Thus all \(27\) points are geometrically reduced.

**Characteristic two.** In the coordinate ring of \(E=V(F)\) one has \(X^3+Y^3=Z^3\), \(Y^3+Z^3=X^3\), and \(Z^3+X^3=Y^3\). Hence \(G|_E=(XYZ)^3\) exactly. The cubic \(E\) is smooth because the partial derivatives are \(X^2,Y^2,Z^2\), which have no common projective zero. Each coordinate line meets \(E\) in three distinct points: for instance \(Z=0\) means \((X/Y)^3=1\). Altogether these are nine reduced points, all defined over \(\mathbb F_4\); none is an intersection of two coordinate axes. Their local equations are simple parameters on \(E\), giving complete local quotient \(k[[t]]/(t^3)\). The three points with both nonzero coordinates equal to one are \(\mathbb F_2\)-rational; the remaining six have minimal field \(\mathbb F_4\).

For the group-scheme interpretation, choose any one of these flex points as the origin of the smooth plane cubic \(E\). The nine points are the complete three-torsion divisor \(E[3]\): each is a flex because its tangent meets \(E\) to order \(3\), and \(3\) is invertible. The cubic has exactly nine \(\mathbb F_4\)-rational points, since every nonzero element of \(\mathbb F_4\) has cube one and \(F=0\) requires precisely two nonzero coordinates. In characteristic \(2\), an ordinary elliptic curve has a unique nonzero geometric two-torsion point, necessarily defined over \(\mathbb F_4\); such a point cannot occur in this group of order nine. Hence \(E\) is supersingular, its \(E[2]\) has a single geometric support point and length four, and \(E[6]=E[2]\times E[3]\) is the length-four Cartier thickening at each of the nine flexes. Subtracting the reduced divisor \(E[3]\) yields the triple Cartier divisor \(3E[3]=V(G|_E)\), as claimed.

**Characteristic three.** We have \(F=(X+Y+Z)^3\) and \(G=((X-Y)(Y-Z)(Z-X))^3\). The only common geometric point of the reduced line \(X+Y+Z=0\) with the three equality lines is \([1:1:1]\): for example, \(X=Y\) makes \(Z=X\) on that line. On the affine chart \(X=1\), choose local coordinates \(u=1+y+z\) and \(v=1-y\). Then \(F=u^3\) and direct expansion gives \(G\equiv v^9\pmod{u^3}\). Thus the local ideal is exactly \((u^3,v^9)\). Its standard monomial basis \(u^iv^j\), for \(0\le i<3\) and \(0\le j<9\), has cardinality \(27\). The stated Hilbert function is the coefficient list of \((1+t+t^2)(1+t+\dots+t^8)\). The quotient is a zero-dimensional complete intersection and hence Gorenstein. These calculations also prove the unique-support assertion.

## Verification

The accompanying `verify_sextactic27.py` uses exact integer and finite-field polynomial arithmetic (SymPy), rather than numerical approximations. Run `python verify_sextactic27.py`. It checks the degree conditions, characteristic-two coordinate-ring congruence, characteristic-three local ideal congruence, and exhaustive \(\mathbb F_4\)-rational support and Frobenius counts; it reports `FERMAT_CUBIC_27_SEXTACTIC_BAD_FIBERS_2_3_EXACT_OK`. Symbolic arguments above, not finite-field sampling, prove the all-prime classification.

## Relationship to prior work

Szemberg and Szpond, *Sextactic points on the Fermat cubic curve and arrangements of conics* (first public arXiv version 2022-11-01), establish the characteristic-zero 27-point sextactic configuration and give the relevant defining equations and sixth-division interpretation. Maugesten and Moe develop the corrected 2-Hessian and sextactic-point theory over the complex numbers. Merta and Zięba reproduce precisely the second-Hessian product \(G\) while studying complex sextactic points, type-nine points, and associated line/conic configurations; their results do not describe the arithmetic bad fibers. Moe and Toft subsequently investigate complex Fermat osculation arrangements. Prior literature on the Fermat arrangement of lines studies the factorization of \(G\) but does not imply the relative integral intersection or its local characteristic-two and characteristic-three algebras. The present claim is a characteristic-by-characteristic scheme-theoretic calculation for the fixed integral equations, not a rediscovery of the 27 complex points or the classical group structure on smooth cubics.

## Limitations

The characteristic-three fiber is a nonreduced plane cubic, so no elliptic-group-scheme interpretation is asserted there. The characteristic-two group-scheme interpretation requires a chosen flex as origin and refers to finite subgroup **schemes**, not merely their geometric points. No intrinsic positive-characteristic 2-Hessian or moduli-flatness assertion is made. Historical priority is assessed from available indexed mathematical literature and accessible records; an unindexed equivalent calculation cannot be ruled out. Independent mathematical audit has not been performed.

## References

- T. Szemberg and J. Szpond, *Sextactic points on the Fermat cubic curve and arrangements of conics*, arXiv:2211.00494, first posted 2022-11-01. https://arxiv.org/abs/2211.00494
- P. A. Maugesten and T. K. Moe, *The 2-Hessian and sextactic points on plane algebraic curves*, arXiv:1709.01698 (2017). https://arxiv.org/abs/1709.01698
- Ł. Merta and M. Zięba, *Sextactic and type-9 points on the Fermat cubic and associated objects*, arXiv:2406.13802 (2024). https://arxiv.org/abs/2406.13802
- T. K. Moe and I. Toft, *The Fermat curves, arrangements of lines, and intersections of osculating curves*, arXiv:2412.16993 (2024). https://arxiv.org/abs/2412.16993
- M. Dumnicki, T. Szemberg, and H. Tutaj-Gasińska, *A counter-example to a question by Huneke and Harbourne*, arXiv:1301.7440 (2013), for the classical Fermat line arrangement. https://arxiv.org/abs/1301.7440
