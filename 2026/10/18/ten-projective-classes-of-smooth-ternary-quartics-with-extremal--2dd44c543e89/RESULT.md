# Ten projective classes of smooth ternary quartics with extremal nontrivial blocking sets

## Finding
Let \(C\subset\mathbf P^2_{\mathbf F_3}\) be a geometrically smooth plane quartic for which \(C(\mathbf F_3)\) is a **nontrivial blocking set**: it meets every rational line but contains no full rational line. The smallest possible number of rational points is six, and the extremal case is attained. Among quartics satisfying
\[
\#C(\mathbf F_3)=6,\qquad C(\mathbf F_3)\text{ nontrivially blocking},
\]
there are **exactly ten** equivalence classes under \(\operatorname{PGL}_3(\mathbf F_3)\), or equivalently ten \(\mathbf F_3\)-isomorphism classes of the associated nonhyperelliptic genus-three curves.

There are exactly **51,948** distinct geometrically smooth projective quartic equations over \(\mathbf F_3\) with these properties (equations are identified under multiplication by \(\mathbf F_3^\times\)). Nine projective-equivalence classes have \(5,616\) equations and trivial rational projective stabilizer, and the tenth has \(1,404\) equations and stabilizer order four. The ten equation representatives, coefficient ordering, and orbit sizes are supplied in `ORBIT_TABLE.json`.

## Assumptions and scope
All curves are homogeneous quartic zero loci in \(\mathbf P^2\), geometrically smooth over \(\overline{\mathbf F}_3\); the rational point count refers specifically to \(\mathbf F_3\). A blocking set meets all thirteen rational lines in \(\operatorname{PG}(2,3)\), and nontrivial means containing no complete four-point rational line. Projective equations are counted modulo nonzero scalar, while projective orbits are modulo \(\operatorname{PGL}_3(\mathbf F_3)\). Six is the previously known sharp combinatorial minimum for a nontrivial blocking set in this plane, by the prime-field bound of Blokhuis; the new contribution is the complete **smooth-quartic** realization census and its projective-orbit structure.

## Proof
**(1) Reduction to one rational point configuration.** There are thirteen rational projective points and thirteen rational lines, each line consisting of four points. Directly enumerating all subsets of these thirteen points shows that no subset of size below six is nontrivially blocking, and that there are exactly \(234\) nontrivially blocking six-point sets. All \(234\) lie in one orbit of \(\operatorname{PGL}_3(\mathbf F_3)\), which has order \(5,616\). Their stabilizer thus has order \(5,616/234=24\). Fix the representative
\[
B=\{[0:0:1],[0:1:0],[0:1:1],[1:0:0],[1:0:1],[1:1:1]\}.
\]
Every extremal curve has rational point set projectively equivalent to \(B\).

**(2) Exhaustion of quartics with exact rational zero locus \(B\).** All ternary quartics form the fifteen-dimensional space with monomial basis \(X^aY^bZ^{4-a-b}\), indexed by \(0\le a\le4\), \(0\le b\le4-a\). The six evaluations at the points of \(B\) are independent and give a nine-dimensional kernel. Row reduction over \(\mathbf F_3\) computes a basis; the proof enumerates each of its \(3^9\) coefficient vectors, retains the forms nonvanishing at all seven rational points outside \(B\), and quotients by the two nonzero scalars. There are precisely \(1,134\) eligible nonzero vectors, or \(567\) projective equations with exact rational point set \(B\). This is a complete enumeration of a finite vector space, not sampling.

**(3) Geometric smoothness.** The stabilizer of \(B\) acts on all \(567\) projective forms. Explicit substitution into the fifteen monomials partitions the equations into exactly thirty orbits. For a homogeneous equation \(F\), geometric singularity is equivalent to the existence of a common zero of \(F\) and its two affine partial derivatives on at least one of the charts \(X=1\), \(Y=1\), \(Z=1\). On each chart a Gröbner-basis computation over \(\mathbf F_3\) checks whether the corresponding ideal is the unit ideal. By the algebraic-closure Nullstellensatz, the unit-ideal test is equivalent to absence of geometric singularities, including at nonrational points. Exactly ten of the thirty orbits are geometrically smooth: nine have stabilizer-orbit size \(24\), and one has size \(6\). Their total is \(9\cdot24+6=222\) geometrically smooth projective equations with point set exactly \(B\). The other twenty orbits, totaling \(345\) equations, are singular; each excluded orbit in fact has a singular rational point.

**(4) Global count and isomorphism classes.** The rational zero locus is intrinsic to an equation, so quartic sets arising from distinct six-point blocking sets cannot be counted twice. Thus the global equation count is \(234\cdot222=51,948\). Every projective equivalence between two curves with rational locus \(B\) belongs to the stabilizer of \(B\), so its ten local orbits coincide with the ten full-projective orbits. Their sizes are \(234\cdot24=5,616\) in nine cases and \(234\cdot6=1,404\) in one case. Finally a geometrically smooth plane quartic is a nonhyperelliptic genus-three canonical model; every \(\mathbf F_3\)-isomorphism between such curves is induced by a rational projectivity of their canonical planes. Hence the ten projective orbits are exactly ten \(\mathbf F_3\)-isomorphism classes.

## Verification
Run `python3 verify_blocking_quartics.py` with Python 3 and SymPy. The standalone script constructs all thirteen points and lines, enumerates all \(\binom{13}{k}\) subsets for \(1\le k\le6\), enumerates all nonsingular three-by-three matrices over \(\mathbf F_3\) modulo scalars, computes the fixed-set stabilizer, exhausts the nine-dimensional quartic system, and decomposes the resulting \(567\) equations into thirty exact orbits. It performs Gröbner unit-ideal tests on all three standard affine charts for every orbit representative. The run successfully returned `VERIFY_OK` with all claimed counts; the complete list of ten orbit representatives and their coefficient ordering is in `ORBIT_TABLE.json`.

The test over an algebraic closure is **symbolic** via the affine Jacobian ideals; no conclusion about geometric smoothness is inferred solely from checking points over a bounded finite extension. The enumeration proves exactly the finite-field assertions above, without asserting any classification for higher fields, degrees, or arbitrary genus-three curves.

## Relationship to prior work
Asgarli–Ghioca–Yip, *Plane curves giving rise to blocking sets over finite fields* (arXiv:2208.13299; first publicly posted 2022-08-28), supplies the blocking-curve framework, the projective-triangle construction, and nonexistence results for smooth blocking quartics when the field has at least nineteen elements. Its construction does not classify the ten characteristic-three quartic realizations; the combinatorial six-point bound is explicitly pre-existing and is not a new claim here.

Asgarli–Ghioca–Yip, *Most plane curves over finite fields are not blocking* (arXiv:2211.08523), especially Section 7 and Example 7.2, calculates a density for **all** blocking equations of degree at least five over \(\mathbf F_3\), without conditioning on geometric smoothness and the extremal six-point configuration in degree four. Its exact density is not the present quartic orbit classification.

Coolsaet–Botteldoorn–Fack, *Classification of minimal blocking sets in small Desarguesian projective planes* (J. Combin. Designs 30 (2022), DOI 10.1002/jcd.21842), classifies finite point sets rather than smooth quartic equations with those point sets. The accessible abstract was inspected; its full text was not available during this comparison, so an unexpected additional algebraic-curve remark within it cannot be ruled out. Top's *Curves of genus 3 over small finite fields* (arXiv:math/0301264) gives extremal genus-three point counts, rather than a projective-orbit classification conditioned on nontrivial blocking incidence.

## Limitations
The ten classes are over \(\mathbf F_3\), not over its algebraic closure. The result does not classify all smooth quartics with larger blocking point sets or all genus-three curves with six rational points. The existing six-point blocking-set minimum, the finite projective-plane set orbit, and general large-degree blocking-curve densities are not independently new theorems. A separately published or unindexed isomorphism-class census may encode an equivalent ten-class classification; this residual priority risk is not a mathematical gap in the finite proof. No independent external mathematical audit has been performed.

## References
1. S. Asgarli, D. Ghioca, C. H. Yip, *Plane curves giving rise to blocking sets over finite fields*, arXiv:2208.13299 (first posted 2022-08-28), https://arxiv.org/abs/2208.13299.
2. S. Asgarli, D. Ghioca, C. H. Yip, *Most plane curves over finite fields are not blocking*, arXiv:2211.08523 (2022), https://arxiv.org/abs/2211.08523.
3. K. Coolsaet, A. Botteldoorn, V. Fack, *Classification of minimal blocking sets in small Desarguesian projective planes*, J. Combin. Designs 30 (2022), 561–580, https://doi.org/10.1002/jcd.21842.
4. J. Top, *Curves of genus 3 over small finite fields*, arXiv:math/0301264 (2003), https://arxiv.org/abs/math/0301264.
