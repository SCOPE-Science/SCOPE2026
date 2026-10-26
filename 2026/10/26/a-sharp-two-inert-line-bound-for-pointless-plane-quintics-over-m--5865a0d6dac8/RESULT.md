# A sharp two-inert-line bound for pointless plane quintics over \(\mathbf F_2\)

## Finding
For a geometrically smooth plane quintic \(C\subset\mathbf P^2_{\mathbf F_2}\) satisfying \(C(\mathbf F_2)=\varnothing\), let \(I(C)\) count the \(\mathbf F_2\)-lines whose scheme-theoretic intersection with \(C\) is a closed point of degree five (equivalently, the restricted binary quintic is irreducible). Then \(2\le I(C)\le7\), and both bounds occur. Exactly one \(\operatorname{PGL}_3(\mathbf F_2)\)-orbit attains \(I(C)=2\). Among all \(15{,}792\) smooth point-free ternary quintic equations in fixed coordinates, the exact distribution is

| \(I(C)\) | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Number of equations | 168 | 1120 | 2352 | 5208 | 4928 | 2016 |

All these curves are smooth projective genus-six curves. The figures count equations, not abstract curve-isomorphism classes.

## Assumptions and scope
The base field is exactly \(\mathbf F_2\). A quintic form has \(21\) homogeneous monomial coefficients. The zero locus is required to be geometrically smooth and to contain none of the seven \(\mathbf F_2\)-rational projective points. Each of the seven rational projective lines is considered exactly once. Two equations are projectively equivalent when related by \(\operatorname{PGL}_3(\mathbf F_2)\); since the only nonzero scalar is one, no scalar quotient adjustment occurs. No assertion concerns all genus-six curves, larger finite fields, or embedded curves with rational points.

## Proof
Index monomials in lexicographic exponent order \((a,b,5-a-b)\), with \(0\le a\le5\) and \(0\le b\le5-a\). For each nonzero vector \(p\in\mathbf F_2^3\), the constraint that \(p\) is not on the curve is \(F(p)=1\). The seven evaluation functionals have rank seven: exact row reduction of the seven-by-twenty-one binary matrix gives seven pivots. Therefore the space of point-free degree-five forms is an affine \(14\)-space containing precisely \(2^{14}=16{,}384\) equations. The complete affine solution basis and the seven-point evaluation tests are computed independently in the two accompanying scripts.

For each nonzero linear form \(\ell\), the kernel is an \(\mathbf F_2\)-line. Choose two distinct nonzero vectors \(u,v\) in that kernel and substitute \(P(s,t)=su+tv\) into \(F\). Its restriction is a degree-five binary form nonvanishing at all three rational points on the line, hence has no factor of degree one. If reducible, the binary quintic must have an irreducible quadratic factor: with degrees at least two, a proper factorization of five can only have degrees two and three. Thus the restriction is irreducible precisely when it has no quadratic root in \(\mathbf F_4\), equivalently when its one-variable dehomogenization is coprime to \(t^4+t\). These are two independently implemented exact tests.

The transformation group \(\operatorname{GL}_3(\mathbf F_2)=\operatorname{PGL}_3(\mathbf F_2)\) has order \(168\). Explicit elementary generators partition all \(16{,}384\) point-free forms into \(104\) orbits. An independent implementation enumerates all \(168\) invertible matrices and checks the orbit partition and sizes. Geometric smoothness is an invariant of each orbit and is equivalent to the absence of common geometric zeros of the dehomogenized equation and its first partial derivatives on each of the three standard affine charts. This is equivalent, by the weak Nullstellensatz over the algebraic closure, to each chart's Jacobian ideal containing \(1\). Gröbner bases over \(\mathbf F_2\) decide the ideal condition exactly. Two separate implementations, one using a computer-algebra Gröbner basis and one using a standalone binary polynomial Buchberger implementation, agree on all \(104\) orbit labels. Exactly \(98\) orbits, accounting for \(15{,}792\) equations, are smooth.

For each of those \(98\) orbit representatives, test all seven rational line restrictions and multiply the invariant's indicator by the orbit size. The resulting distribution is the displayed six-bin table; its entries sum to \(15{,}792\). The smallest observed value is \(2\), and its only orbit has size \(168\), proving the sharp lower bound and uniqueness up to projective change of coordinates. The maximum \(7\) is also realized. This is an exhaustive proof for the stated finite family; the complete orbit certificate records every representative and its tested line statistic.

An explicit lower-bound extremizer is
\[
F=X^5+XY^4+XYZ^3+XZ^4+Y^5+YZ^4+Z^5.
\]
Its coefficient bit mask in the specified order is \(1049827\); among line masks \(1,\ldots,7\) in coordinates \(X,Y,Z\), precisely masks \(3\) and \(7\) have irreducible restrictions. Its projective orbit has size \(168\), so its stabilizer is trivial.

## Verification
Run `python scripts/census.py` and `python scripts/independent_check.py` from the containing directory. The first constructs the affine solution basis, enumerates all point-free forms, computes their seven line restrictions, determines elementary-generator projective orbits and performs algebraic smoothness tests with `sympy` Gröbner bases. The second scans all \(2^{21}\) coefficient masks, tests line-factorization with a binary-polynomial gcd, enumerates projective transformations independently and calculates smoothness via its own Buchberger algorithm. Both use and check the self-contained `certificates/orbits.json` certificate. The verified outputs in `certificates/census_output.json` and `certificates/independent_output.json` supply the numerical checks. The explicit algorithms, rather than those logged outputs alone, support the theorem.

## Relationship to prior work
Huang–Kedlaya–Lau's census classifies genus-six curves over \(\mathbf F_2\), including the smooth plane-quintic locus. Its public plane-quintic class records contain point counts, group labels and function-field polynomial representations; they do not directly tabulate the distribution of irreducible rational line sections, the bound of two, or uniqueness of the minimal orbit. Recalculating those geometric line-section invariants from class records requires additional computations and distinctions between abstract isomorphism and projective embedded equivalence. Entin's theorem gives asymptotic distributions of Frobenius cycle types of hyperplane sections as the field size grows, not the exact characteristic-two seven-line spectrum here. A related finite census of irreducible sections of smooth plane quartics over \(\mathbf F_2\) is a different degree and allows zero irreducible lines; it does not imply the present bound or distribution.

## Limitations
The determination is restricted to a finite embedded family; it gives no classification of abstract genus-six curves or general field-size theorem. Earlier comprehensive genus-six class data may permit this distribution to be recovered by additional factorization analysis, so indirect publication priority cannot be excluded. The computational proof requires independently reviewing and/or rerunning the provided source code and certificate; no external independent mathematical audit is claimed.

## References
- W. Huang, K. Kedlaya and J. Lau, *A census of genus 6 curves over \(\mathbf F_2\)*, arXiv:2402.00716 (first public 2024-02-01), https://arxiv.org/abs/2402.00716 ; companion data https://github.com/junbolau/genus-6/tree/main/Census/plane_quintic .
- A. Entin, *Monodromy of Hyperplane Sections of Curves and Decomposition Statistics over Finite Fields*, arXiv:1805.05454 (first public 2018), https://arxiv.org/abs/1805.05454 .
