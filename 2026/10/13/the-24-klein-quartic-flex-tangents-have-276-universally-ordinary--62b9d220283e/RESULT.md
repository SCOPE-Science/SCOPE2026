# The 24 Klein-quartic flex tangents have 276 universally ordinary intersections

## Finding

For the Klein quartic
\[
C:\quad X^3Y+Y^3Z+Z^3X=0
\]
over \(\mathbb Q\), let \(\mathcal T\) denote its 24 geometric inflection tangent lines. The following single arithmetic-incidence classification holds.

For every prime \(p\ge5\) with \(p\ne7\), the reduction of \(C\) is smooth, its 24 inflection tangent lines are distinct and no three are concurrent. Consequently the union of the tangents has exactly \(\binom{24}{2}=276\) distinct ordinary geometric double points.

As an absolute-Galois set over \(\mathbb Q\), the 276 points decompose into exactly three orbits of size one, seven orbits of size three and 42 orbits of size six. Their minimal common field of definition is \(K=\mathbb Q(\zeta_7)\). For every prime \(p\ge5\), \(p\ne7\), the number of its intersection points rational over \(\mathbb F_p\) is
\[
N_p=\begin{cases}
276,&p\equiv1\pmod7,\\
24,&p\equiv6\pmod7,\\
3,&p\equiv2,3,4,5\pmod7.
\end{cases}
\]
The corresponding natural densities of primes are respectively \(1/6\), \(1/6\) and \(2/3\).

## Assumptions and scope

We use the fixed integral plane model displayed above, and count geometric **intersection points of distinct inflection tangent lines**, not rational points of the original quartic and not the tangent contact points. Write \(\zeta=\zeta_7\) for a primitive seventh root of unity and \(R=\mathbb Z[\zeta]\). Reduction of coefficients means reduction along any prime of \(R\) above \(p\); the final incidence statements are independent of this choice. The theorem covers precisely all prime characteristics \(p\ge5\), \(p\ne7\).

## Proof

**1. The 24 flex points.** A classical explicit list (Fisher, 2001, §2.1) comprises the three rational points
\[
[1:0:0],\quad[0:1:0],\quad[0:0:1]
\]
and, for \(j\in\{0,1,\ldots,6\}\), the cyclic coordinate permutations of
\[
P_j=\left[\zeta^{3j}(\zeta-\zeta^6):
\zeta^j(\zeta^2-\zeta^5):\zeta^4-\zeta^3\right].
\]
These 24 projective points satisfy both \(F=0\) and its normalized Hessian \(h=0\), where
\[
h=X^5Z-5X^2Y^2Z^2+XY^5+YZ^5,
\quad \det\operatorname{Hess}(F)=-54h.
\]
The tangent to \(C\) at \(P=[x:y:z]\) has coefficient vector
\[
\ell(P)=(3x^2y+z^3,\ x^3+3y^2z,\ y^3+3z^2x).
\]
For the 21 nonrational displayed points, all three entries of \(\ell(P)\) lie in \(7R\). Divide each such vector by \(7\); for the three rational points retain \(\ell(P)\). This yields 24 explicit vectors \(\ell_1,\ldots,\ell_{24}\in R^3\) defining the same lines in every characteristic \(p\ne7\). The accompanying verifier reconstructs this list directly, checks the curve and Hessian equations, and checks tangency.

**2. Exact determinant certificate and universal good reduction.** For every unordered triple \(i<j<k\) from \(\{1,\ldots,24\}\), put
\[
\Delta_{ijk}=\det(\ell_i,\ell_j,\ell_k)\in R.
\]
The following is the **complete** census of all \(\binom{24}{3}=2024\) exact nonzero cyclotomic determinant norms, computed by determinants of the six-dimensional integral multiplication matrices for \(R\):

| \(\lvert N_{K/\mathbb Q}(\Delta_{ijk})\rvert\) | Frequency |
|:--|--:|
| \(1\) | 1 |
| \(7\) | 63 |
| \(343\) | 441 |
| \(2401\) | 63 |
| \(2744\) | 126 |
| \(117649\) | 735 |
| \(823543\) | 378 |
| \(941192\) | 210 |
| \(40353607\) | 7 |

Every displayed norm has prime divisors only in \(\{2,7\}\). If \(p\ge5\), \(p\ne7\), every \(\Delta_{ijk}\) is therefore nonzero modulo every prime of \(R\) above \(p\). Thus no three tangent lines concur and no two coincide after reduction. All 276 pairwise intersection points are consequently distinct and ordinary.

For the claim that these remain *exactly* the inflection tangents, the gradient criterion proves smoothness: when \(XYZ\ne0\), multiplying \(F_X,F_Y,F_Z\) by \(X,Y,Z\) gives a linear system for \((X^3Y,Y^3Z,Z^3X)\) whose coefficient determinant is \(28\). It forces all three monomials to vanish if \(p\nmid28\), an impossibility on this torus; coordinate-axis points are visibly smooth. The 24 displayed points remain pairwise distinct because their tangent lines do. They lie on both \(F\) and \(h\) after reduction. These two forms share no component (for example, the specialization at \(X=0\) shows \(F\nmid h\)), so Bézout gives total intersection multiplicity \(4\cdot6=24\). Hence the 24 points exhaust the flex locus, with each flex ordinary.

**3. Galois orbits of the 276 intersections.** The complete coefficient list lies in \(K=\mathbb Q(\zeta_7)\), whose Galois automorphisms are \(\sigma_a(\zeta)=\zeta^a\) for \(a\in(\mathbb Z/7\mathbb Z)^\times\). The verifier compares transformed line vectors up to projective proportionality and derives the exact fixed counts:

| \(a\) | Fixed tangent lines | Fixed unordered line pairs |
|:--|--:|--:|
| \(1\) | 24 | 276 |
| \(2,3,4,5\) | 3 | 3 |
| \(6\) | 6 | 24 |

Because no three lines concur, each intersection point uniquely corresponds to an unordered pair of lines. A generator of the cyclic group of order six therefore fixes exactly three pair intersections. An element of order two fixes 24 and one of order three fixes only three. Hence exactly three intersections have orbit length one; \((24-3)/3=7\) orbits have length three; no length-two orbits exist; and \((276-3-21)/6=42\) orbits have length six. In particular some points have full degree six, so the common field is exactly \(K\), not a proper subfield.

For every \(p\ne7\), Frobenius acts on \(K\) by \(\zeta\mapsto\zeta^p\); its fixed intersection points are precisely the \(\mathbb F_p\)-rational intersections. The table yields the stated three counts. Dirichlet's theorem on primes in reduced residue classes modulo seven gives their natural densities.

## Verification

Run `python3 verify_klein_flex_tangents.py` with a standard Python 3 interpreter. The standalone script uses exact integer operations for \(R\), reconstructs all 24 points and tangents, verifies the defining equation and Hessian equation, evaluates all 2024 triple determinants, computes all nine norm frequencies by exact six-by-six Bareiss determinants, and independently enumerates every cyclotomic Galois permutation on tangent lines and unordered pairs. Its final assertion is `VERIFY_OK`. No finite collection of sampled primes is substituted for the universal norm-divisibility argument.

## Relationship to prior work

Fisher (2001, §2.1) explicitly lists the 24 Klein-quartic inflection points as modular cusps. In particular the cyclotomic field of the underlying flex points is **not** claimed as new here. Pacini–Testa (2018, Example 1.9) identify the degree-24 Klein inflection-line scheme as a complete intersection in the dual plane, but do not determine the mutual concurrency of its 24 lines or the arithmetic orbit structure of their 276 intersections. Pokora–Roé (2018) analyze the distinct 21-line Klein arrangement coming from reducible polar axes and explicitly count the 24 flex *points*; their incidence census is not that of the 24 flex tangents. Dimca–Ilardi–Pokora–Sticlaru (2023, §5) recall the 24 ordinary Klein flexes, but discuss the intersection patterns of different quartic tangent arrangements. The contribution proved here is precisely the complete good-characteristic 24-line intersection-lattice statement and the 276-point Galois/Frobenius spectrum. No claim of exhaustive literature novelty beyond these comparisons is made.

## Limitations

The classification concerns this specific integral projective model and excludes characteristics two, three and seven. Characteristic seven is genuinely singular for this model: \([1:2:4]\) is a singular point after reduction. This theorem does not classify the possibly nonreduced flex scheme in excluded characteristics, or claim a classification of arbitrary quartic inflection-line arrangements. The no-triple result is established by a finite but *complete* exact determinant certificate; the theorem would not follow from merely checking finitely many prime fields. The originality assessment is limited by incomplete access to some historical treatments of the Klein quartic and cannot rule out unindexed earlier computations.

## References

1. T. Fisher, *Some examples of 5 and 7 descent for elliptic curves over \(\mathbb Q\)*, J. Eur. Math. Soc. 3 (2001), §2.1, especially pp. 182–183. https://ems.press/content/serial-article-files/31488
2. M. Pacini and D. Testa, *Reconstructing general plane quartics from their inflection lines*, arXiv:1711.05776 (2017; revised 2018), Example 1.9. https://arxiv.org/abs/1711.05776
3. P. Pokora and J. Roé, *The 21 reducible polars of Klein's quartic*, arXiv:1803.06411 (2018), §§1–2 and appendix. https://arxiv.org/abs/1803.06411
4. A. Dimca, G. Ilardi, P. Pokora and G. Sticlaru, *Construction of free curves by adding lines to a given curve*, arXiv:2301.01117, first available 3 January 2023, §5. https://arxiv.org/abs/2301.01117
