# Exact p-rank and point-count strata of bidegree \(2,3\) genus-two curves over \(\mathbf F_2\)

## Finding
Among all nonzero binary bihomogeneous equations of bidegree \( (2,3) \) on the split surface \(Q=\mathbf P^1_{\mathbf F_2}\times\mathbf P^1_{\mathbf F_2}\), exactly \(1116\) define geometrically smooth curves. Each such curve has genus two. Their joint distribution by \(\mathbf F_2\)-rational point count and Jacobian \(2\)-rank is exactly:

| \(\#C(\mathbf F_2)\) | p-rank \(0\) | p-rank \(1\) | p-rank \(2\) | Total |
| ---: | ---: | ---: | ---: | ---: |
| 0 | 0 | 0 | 6 | 6 |
| 1 | 18 | 0 | 18 | 36 |
| 2 | 0 | 36 | 72 | 108 |
| 3 | 108 | 0 | 60 | 168 |
| 4 | 0 | 180 | 216 | 396 |
| 5 | 162 | 0 | 162 | 324 |
| 6 | 0 | 0 | 78 | 78 |
| **Total** | **288** | **216** | **612** | **1116** |

Thus \(288\) equations give \(2\)-rank zero, \(216\) give rank one, and \(612\) are ordinary (rank two). The possible point counts at rank zero are \(1,3,5\); at rank one, \(2,4\); and at rank two, every integer from \(0\) to \(6\). These count **equations in fixed bihomogeneous coordinates**, not abstract isomorphism classes of curves.

## Assumptions and scope
Work over \(k=\mathbf F_2\), with fixed coordinates \(([U_0:U_1],[V_0:V_1])\) on \(Q\). For every coefficient vector \(e=(e_{ij})\in k^{12}\setminus\{0\}\), define
\[
F_e(U,V)=\sum_{i=0}^2\sum_{j=0}^3e_{ij}U_0^{2-i}U_1^iV_0^{3-j}V_1^j.
\]
Index \(e_{ij}\) by bit position \(4i+j\), so every integer mask from \(1\) through \(4095\) specifies exactly one distinct nonzero form. The characteristic is \(2\), hence there is no nontrivial scalar identification. Exclude geometrically singular divisors. The \(2\)-rank is \(\dim_{\mathbf F_2}\operatorname{Jac}(C)[2](\overline k)\).

## Proof
**1. Exhaustive finite domain and geometric smoothness.** On each of the four standard affine charts of \(Q\), dehomogenize \(F_e\) to \(f(u,v)\). A geometric singular point exists on the chart if and only if the ideal \(\langle f,f_u,f_v\rangle\subset\mathbf F_2[u,v]\) is proper (a common zero exists over \(\overline k\)). Reduced Gröbner bases over \(\mathbf F_2\) decide whether this ideal contains \(1\). The direct checker performs all four tests for all \(4095\) masks and returns exactly \(1116\) smooth masks. The bidegree \( (2,3) \) class is ample, so a smooth member is geometrically connected, hence geometrically integral, and the adjunction formula gives \(g=(2-1)(3-1)=2\).

**2. Structural computation of the \(2\)-rank.** Write \(F_e=A(V)U_0^2+B(V)U_0U_1+C(V)U_1^2\). For every smooth member, \(B\neq0\), so projection to the \(V\)-factor is a separable degree-two cover of \(\mathbf P^1\). Its geometric branch points are precisely the *distinct* zeros of the homogeneous binary cubic \(B(V)\), including infinity. For an Artin–Schreier quadratic cover, the Deuring–Shafarevich \(p\)-rank formula yields \(f_2=\#\operatorname{Supp}(B=0)-1\). Factor \(B(1,t)\) over \(\mathbf F_2\), sum degrees of its distinct irreducible factors, and add one when the coefficient of \(V_1^3\) vanishes (the point at infinity). All ranks are \(0,1,2\).

**3. Rational-point count.** Evaluate \(F_e\) at the nine points of \(Q(\mathbf F_2)\), taking \(\mathbf P^1(\mathbf F_2)=\{[1:0],[0:1],[1:1]\}\). The total number of zeros gives \(N_1=\#C(\mathbf F_2)\). Counting each smooth mask and \((N_1,f_2)\) pair once produces the displayed table, whose entries sum to \(1116\).

**4. Independent checks.** A separate implementation enumerates the whole domain directly, calculates four-chart geometric smoothness, factors \(B\), and counts \(\mathbf F_2\)-points, producing the same twelve nonzero cells. Independently, the first checker partitions all nonzero forms into \(165\) orbits under \(\operatorname{PGL}_2(\mathbf F_2)^2\) (order \(36\)); \(39\) orbits are smooth and their weighted table agrees. A third procedure enumerates \(C(\mathbf F_4)\) on all \(39\) smooth orbit representatives, using the exact field defined by \(z^2+z+1=0\). For their genus-two zeta numerators \(L(T)=1+a_1T+a_2T^2+2a_1T^3+4T^4\), the integer coefficients are \(a_1=N_1-3\) and \(a_2=(N_2-5+a_1^2)/2\). The degree of \(L(T)\bmod 2\) gives the same \(2\)-rank on every representative, independently of factoring \(B\).

## Verification
The embedded scripts require Python 3 and SymPy. Execute from the directory containing the scripts: `python bideg23.py`, `python prank.py`, `python prank_branch.py`, and `python independent_all_forms.py`. The first enumerates the complete \(36\)-element coordinate group action and geometric-smoothness orbits; the second checks \(\mathbf F_4\)-point counts and zeta ranks; the third checks branch-support ranks; the fourth scans all \(4095\) masks separately. Reference outputs and exact orbit representatives are included. Exact arithmetic and exhaustive finite loops are used; no probabilistic tests are needed.

## Relationship to prior work
Zobernig (2021), *Genus 2 Curves in Small Characteristic*, studies p-rank strata in coarse moduli and records \(2,2,4\) characteristic-two coarse-moduli strata counts at \(q=2\), but does not count coordinate-fixed bidegree-\((2,3)\) equations or cross-tabulate their point counts. Cardona–Nart–Pujolàs (2002), *Curves of genus two over fields of even characteristic*, classifies abstract genus-two curves and ramification-divisor types (Theorems 17–18), not this equation-weighted embedding census. A separate previously recorded calculation enumerates smooth pencils in the same linear system, but does not give these joint p-rank/point-count frequencies. The underlying genus-two classification, structural p-rank formula, and mere total \(1116\) are not claimed as novel.

## Limitations
The counts depend on the chosen embedded linear system and fixed coordinates, and must not be interpreted as counts of distinct abstract genus-two curves. The finite exhaustive proof does not assert analogous formulas over larger fields. Earlier or unindexed tabulations and indirect computations from complete genus-two classifications could contain equivalent arithmetic frequencies; publication priority is not independently certified. Only the present calculation and the stated literature comparisons have been reviewed; no external independent mathematical audit is claimed.

## References
1. Lukas Zobernig, *Genus 2 Curves in Small Characteristic* (first public 14 Nov 2021), arXiv:2111.07270v1, https://arxiv.org/html/2111.07270v1. Primary MSC 14H10.
2. Gabriel Cardona, Enric Nart and Jordi Pujolàs, *Curves of genus two over fields of even characteristic* (2002), arXiv:math/0210105, https://arxiv.org/html/math/0210105v1; especially §1.2, §1.4 and Theorems 17–18.
