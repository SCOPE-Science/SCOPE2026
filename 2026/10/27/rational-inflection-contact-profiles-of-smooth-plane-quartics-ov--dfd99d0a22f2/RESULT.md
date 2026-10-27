# Rational inflection-contact profiles of smooth plane quartics over \(\mathbf F_2\)

## Finding
Let \(C=V(F)\subset\mathbf P^2_{\mathbf F_2}\) be a geometrically smooth plane quartic. At a rational point \(P\in C(\mathbf F_2)\), write \(m(P)=I_P(C,T_PC)\) for its tangent intersection multiplicity. Smoothness and Bézout give \(m(P)\in\{2,3,4\}\). Put \(N=|C(\mathbf F_2)|\) and \(a_j=|\{P\in C(\mathbf F_2):m(P)=j\}|\). Contact three gives an ordinary rational inflection and contact four a rational hyperinflection.

**The complete joint arithmetic contact profile** \((N,a_2,a_3,a_4)\) assumes **exactly 34 values** among the **10,920** geometrically smooth nonzero ternary quartic equations over \(\mathbf F_2\). These equations form 78 projective orbits, all represented in `representatives.tsv`. The exhaustive frequencies, counting equations rather than isomorphism classes, are:

| \(N\) | \(a_2\) | \(a_3\) | \(a_4\) | Equations |
|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 165 |
| 1 | 0 | 0 | 1 | 504 |
| 1 | 1 | 0 | 0 | 504 |
| 2 | 0 | 0 | 2 | 252 |
| 2 | 0 | 1 | 1 | 672 |
| 2 | 1 | 0 | 1 | 672 |
| 2 | 1 | 1 | 0 | 504 |
| 2 | 2 | 0 | 0 | 546 |
| 3 | 0 | 0 | 3 | 28 |
| 3 | 0 | 1 | 2 | 168 |
| 3 | 0 | 2 | 1 | 252 |
| 3 | 0 | 3 | 0 | 224 |
| 3 | 1 | 0 | 2 | 168 |
| 3 | 1 | 1 | 1 | 336 |
| 3 | 1 | 2 | 0 | 504 |
| 3 | 2 | 0 | 1 | 504 |
| 3 | 2 | 1 | 0 | 840 |
| 3 | 3 | 0 | 0 | 336 |
| 4 | 0 | 4 | 0 | 168 |
| 4 | 1 | 1 | 2 | 168 |
| 4 | 1 | 2 | 1 | 336 |
| 4 | 1 | 3 | 0 | 168 |
| 4 | 2 | 1 | 1 | 168 |
| 4 | 2 | 2 | 0 | 672 |
| 4 | 3 | 0 | 1 | 168 |
| 4 | 3 | 1 | 0 | 504 |
| 4 | 4 | 0 | 0 | 189 |
| 5 | 2 | 2 | 1 | 84 |
| 5 | 2 | 3 | 0 | 336 |
| 5 | 3 | 2 | 0 | 168 |
| 5 | 4 | 0 | 1 | 84 |
| 5 | 4 | 1 | 0 | 336 |
| 6 | 4 | 2 | 0 | 168 |
| 7 | 7 | 0 | 0 | 24 |

The table sums to 10,920 equations and, for each entry, \(N=a_2+a_3+a_4\). It provides an exact refinement by *ordinary inflection points*, which are not recovered merely from bitangent-line or point-count statistics.

The number of rational ordinary flexes never exceeds **four**, and the number of rational hyperflexes never exceeds **three**. Both bounds occur. The 28 quartic equations having three rational hyperflexes form a single orbit; their three rational points are all hyperflexes. Every smooth quartic containing all seven Fano-plane points has no rational flex (24 such equations, one orbit). The weighted first moments are
\[
\sum_F a_2(F)=16\,464,\quad \sum_F a_3(F)=10\,920,\quad \sum_F a_4(F)=5\,376.
\]
In particular, the average number of rational ordinary flexes among all smooth ternary quartic equations over \(\mathbf F_2\) is exactly one.

## Assumptions and scope
The base field is precisely \(\mathbf F_2\); the curve is a closed degree-four plane subscheme that is smooth over an algebraic closure. Equations differing by a nonzero scalar are identified, which introduces no identifications because \(\mathbf F_2^\times=\{1\}\). Projective equivalence means the natural action of \(\operatorname{PGL}_3(\mathbf F_2)\) of order 168. Only **rational contact points** are counted; no assertion classifies flexes over extensions or nonrational inflection lines. For a smooth quartic, the tangent line is never a component.

## Proof
**1. Finite polynomial space and complete projective orbit partition.** Fix the ordered monomial basis \((X^aY^bZ^c)_{a+b+c=4}\), sorted by increasing \(a\), then increasing \(b\). It contains 15 monomials, so every nonzero coefficient mask \(1\le M<2^{15}\) defines a unique quartic. Enumerate the 168 invertible binary \(3\times3\) matrices. Substitute their three linear forms into the 15 monomials using exact addition and multiplication modulo two. For each nonzero mask, the set of all 168 images is its orbit. Partitioning all 32,767 nonzero masks yields **279 polynomial orbits**, with integer sizes obtained by direct counting. Their disjoint union is the full space because each image is an invertible linear coordinate substitution.

**2. Geometric smoothness is decided exactly.** For each of the 279 representatives, work in all three affine charts \(X=1\), \(Y=1\), \(Z=1\). If \(f(u,v)\) is the dehomogenized equation, the chart contains a geometric singular point exactly when \(f=f_u=f_v=0\) has a solution over \(\overline{\mathbf F}_2\). By the weak Nullstellensatz, this system has no such solution if and only if the ideal \(\langle f,f_u,f_v\rangle\) is the unit ideal. An exact characteristic-two Gröbner basis tests this condition on each chart. Exactly **78** orbits, containing **10,920** equations, pass in all three charts. Every other representative fails at least one chart. The group preserves geometric smoothness, so this is exhaustive over all masks. This independently reproduces the classical total number of 78 classes; that total is not asserted to be new.

**3. Rational tangent-contact calculation.** For each of the seven nonzero binary triples representing \(\mathbf P^2(\mathbf F_2)\), test \(F(P)=0\). At such a point the gradient \(\nabla F(P)\) is nonzero by geometric smoothness. The tangent is \(\nabla F(P)\cdot(X,Y,Z)=0\). Choose another binary point \(Q\ne P\) on that line. Substitute \(P+tQ\) into \(F\) over \(\mathbf F_2[t]\). Its constant and linear coefficients vanish. The least nonzero power \(t^j\) has exponent \(j=2,3,4\), and by a local parameter calculation it equals \(I_P(C,T_PC)\). This is independent of which admissible \(Q\) is chosen.

**4. Exact profile histogram.** Determine the triple \((a_2,a_3,a_4)\) for each of the 78 smooth orbit representatives, then weight it by its orbit cardinality. Tangent contact is preserved under projective coordinate changes. The resulting 34 weighted frequencies appear above. The full representative masks and profile frequencies are in `representatives.tsv` and `contact_profiles.tsv`; `flex_quartics.py` reconstructs both from the complete ambient coefficient space. A separately written polynomial-substitution implementation, `verify_contacts.py`, tests all seven rational points of each smooth representative and reproduces the same exact contact profiles.

**5. Structural checks.** A rational line has three rational points. If \(N=7\), every tangent at a rational point contains two other rational curve points, so its intersection multiplicity cannot be three or four by Bézout. If \(N\ge6\), every tangent line at a rational point contains at least one other rational curve point, excluding order-four contact. These constraints agree with every table entry. The sums of the 34 rows and of their orbit representatives prove the stated extremal and incidence identities without appealing to a statistical sample.

## Verification
Run `python flex_quartics.py` (Python 3 with SymPy installed). It exhausts 32,767 coefficient masks by 279 exact coordinate orbits, tests three Jacobian ideals for every representative, and writes `flex_quartics_data.json`. Then run `python verify_contacts.py` in the same directory; it evaluates each representative's contact order by a separate polynomial restriction procedure. Both executed successfully, with totals 279 polynomial orbits, 78 smooth orbits, 10,920 smooth equations and 34 profiles. The files `contact_profiles.tsv` and `representatives.tsv` provide the finite tables needed to check all 34 frequencies. Arithmetic is exact in characteristic two, not floating-point or a bounded extension-field heuristic.

## Relationship to prior work
Nart--Ritzenthaler (2004 preprint; 2006 journal version) gives the full classification of nonsingular plane quartics over fields of characteristic two, including the 78 abstract classes when the field has two elements. That count and the existence of explicit normal models are prior work. Pacini--Testa (2017 preprint, 2018 revision) studies inflection-line configurations and reconstructibility, with its main reconstruction theorem requiring characteristic coprime to six. Pacini--Testa (2020) develops general inflection and theta-hyperplane enumerative geometry in special characteristics. The present arithmetic 34-profile table distinguishes ordinary flexes from hyperflexes over the smallest field; it does not follow as a stated numerical table from the cited theorems without further finite specialization and contact calculations. The prior explicit quartic models may allow a different route to computing the table.

## Limitations
This is a finite-field classification and computationally exhaustive proof, not a theorem uniform in the field size and not a classification of all geometric flexes. Prior full moduli classifications make some enumerative derivation possible; publication priority of an independently computed, potentially unindexed contact table is unresolved. No independent human audit has been performed. The exact finite algorithms and complete catalogues are part of this package.

## References
1. M. Pacini and D. Testa, *Reconstructing general plane quartics from their inflection lines*, arXiv:1711.05776 (first public version 2017-11-15), https://arxiv.org/abs/1711.05776.
2. M. Pacini and D. Testa, *Complex and tropical counts via positive characteristic*, arXiv:2004.00955 (2020-04-02), https://arxiv.org/abs/2004.00955.
3. E. Nart and C. Ritzenthaler, *Non-hyperelliptic curves of genus three over finite fields of characteristic two*, arXiv:math/0312366 (2003); J. Number Theory 116 (2006), 443--473, https://arxiv.org/abs/math/0312366.
4. A. Betten, N. Kaplan and F. Karaoglu, *Classification of Quartic Curves Over Small Finite Fields* (2021), https://www.math.colostate.edu/~betten/mathdata/quartic_curves.html (a separate database not listing the two-element field's rational flex profiles).
