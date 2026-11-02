# The five point-free fields of the line-free Fermat cubic

## Finding

Let \(q\) be a prime power of characteristic \(p\ne3\), and let \(X\subset\mathbb P^3_{\mathbb F_q}\) be the smooth Fermat cubic
\[
 X:\quad X_0^3+X_1^3+X_2^3+X_3^3=0.
\]
Let \(L\) be the *reduced geometric union* of all twenty-seven lines on \(X_{\overline{\mathbb F}_q}\); it descends to a closed subscheme over \(\mathbb F_q\), even when its individual components do not. Put \(U=X\setminus L\). Then, without any restriction on the extension degree defining \(q\),
\[
\#U(\mathbb F_q)=
\begin{cases}
 (q-7)(q-13),&p\ne2,3,\ q\equiv1\pmod3,\\
 (q-1)^2,&p\ne2,3,\ q\equiv2\pmod3,\\
 (q-4)(q-16),&p=2,\ q\equiv1\pmod3,\\
 q(q-2),&p=2,\ q\equiv2\pmod3.
\end{cases}
\]
In particular,
\[
 U(\mathbb F_q)=\varnothing\quad\Longleftrightarrow\quad q\in\{2,4,7,13,16\}.
\]
These are all the prime-power fields in characteristic other than three for which every rational point of the Fermat cubic lies on some *geometric* line. The same formula with \(q\) replaced by \(q^n\) counts \(U(\mathbb F_{q^n})\) for every positive integer \(n\).

Write \(Z(U,T)=\exp(\sum_{n\ge1}\#U(\mathbb F_{q^n})T^n/n)\). Its four rational forms are, respectively,
\[
\begin{array}{c|c}
 \text{field case}&Z(U,T)\\\hline
 p\ne2,3,\ q\equiv1\pmod3&\displaystyle\frac{(1-qT)^{20}}{(1-q^2T)(1-T)^{91}}\\
 p\ne2,3,\ q\equiv2\pmod3&\displaystyle\frac{(1-qT)^{11}(1+qT)^9}{(1-q^2T)(1-T)^{46}(1+T)^{45}}\\
 p=2,\ q\equiv1\pmod3&\displaystyle\frac{(1-qT)^{20}}{(1-q^2T)(1-T)^{64}}\\
 p=2,\ q\equiv2\pmod3&\displaystyle\frac{(1-qT)^{11}(1+qT)^9}{(1-q^2T)(1-T)^{32}(1+T)^{32}}.
\end{array}
\]

## Assumptions and scope

The characteristic-three Fermat equation is the cube of a linear form; that case is excluded. The open subset removes *every* geometric line, including lines not defined over the ground field. A point of \(X(\mathbb F_q)\) is removed if it lies on at least one such line after extension of scalars. The assertion is about the ordinary reduced complement, not an infinitesimal line scheme or a generalized diagonal cubic.

## Proof

**1. The lines and surface point counts.** Let \(\zeta\) be a primitive cube root of unity in an algebraic closure. For each of the three pairings \((ab\mid cd)\) of four indices and each \((i,j)\in\{0,1,2\}^2\), the equations
\[
 X_a+\zeta^i X_b=0,\qquad X_c+\zeta^j X_d=0
\]
cut out a line on \(X\). These are the classical twenty-seven geometric lines; their completeness for a smooth cubic surface is also standard. If \(q\equiv1\pmod3\), all are rational and their divisor classes span the geometric Picard group, so the Frobenius trace on \(\mathrm{Pic}\) is seven and \(\#X(\mathbb F_q)=q^2+7q+1\). Equivalently, contract six disjoint rational exceptional curves to obtain the rational split blowup of \(\mathbb P^2\). If \(q\equiv2\pmod3\), the cube map on \(\mathbb F_q\) is bijective; solving for one cube gives a bijection \(X(\mathbb F_q)\simeq\mathbb P^2(\mathbb F_q)\), hence \(\#X(\mathbb F_q)=q^2+q+1\).

**2. The split incidence census, uniformly in the characteristic.** Any two different lines meet if and only if the determinant of their four linear equations vanishes. Three lines meet at one point if and only if all \(4\times4\) minors of their six equations vanish. We carry out these tests over the integral Eisenstein ring \(\mathbb Z[\zeta]\), where \(\zeta^2+\zeta+1=0\), and take integer norms \(N(a+b\zeta)=a^2-ab+b^2\). Among the \(\binom{27}{2}=351\) unordered line pairs, the determinant norms have distribution
\[
\begin{array}{c|rrr}\text{norm}&0&3&9\\\hline\text{pairs}&135&162&54\end{array}.
\]
Among the \(\binom{27}{3}=2925\) line triples, take the greatest common divisor of the norms of all their maximal minors. Its distribution is
\[
\begin{array}{c|rrrrr}\text{norm gcd}&0&1&3&4&9\\\hline\text{triples}&18&702&1944&27&234\end{array}.
\]
The sums are exhaustive, and the computation is replayable in the standalone verifier. In particular, all potential new pair intersections or triple concurrences under reduction are restricted to characteristics two and three. Checking the integral zero patterns, or equivalently the configuration over \(\mathbb F_7\), gives 18 distinct triple points and 81 distinct double points in every odd characteristic other than three. No higher coincidence is possible, as it would force additional vanishing minors. Since each of the twenty-seven projective lines has \(q+1\) points and the triple and double overlaps have excess multiplicities two and one, respectively,
\[
\#L(\mathbb F_q)=27(q+1)-2\cdot18-81=27q-90
\]
whenever \(p\ne2,3\) and \(q\equiv1\pmod3\).

When \(p=2\), the twenty-seven lines and all their intersections are defined over \(\mathbb F_4\). Here the Fermat cubic is the Hermitian surface over \(\mathbb F_4\); the forty-five geometric intersection points are the forty-five \(\mathbb F_4\)-rational points, each lying on precisely three lines. This is also checked directly by enumerating \(\mathbb P^3(\mathbb F_4)\), obtaining forty-five triple points and no double points; the coefficients and the incidence relations already lie in \(\mathbb F_4\), so the result is unchanged over every extension of characteristic two. Thus for \(q\equiv1\pmod3\) in characteristic two,
\[
\#L(\mathbb F_q)=27(q+1)-2\cdot45=27q-63.
\]

**3. Nonsplit descent of the whole geometric union.** If \(q\equiv2\pmod3\), Frobenius sends \(\zeta\mapsto\zeta^{-1}\), and among the twenty-seven lines only the three with \(i=j=0\) are individually rational. A rational point on any other geometric line also lies on its Frobenius conjugate. If both exponents are nonzero, those two lines are skew. If exactly one exponent is nonzero, their intersection is a rational point lying on the corresponding \((i,j)=(0,0)\) line. Therefore the ground-field points on the *entire* geometric union coincide with the union of the three rational lines. Those form a triangle with three distinct pairwise intersection points in odd characteristic, but concur in one point in characteristic two. Hence
\[
\#L(\mathbb F_q)=\begin{cases}3q,&p\ne2,\\3q+1,&p=2.\end{cases}
\]

**4. Subtraction, zeros, and zeta functions.** Subtract the three displayed union counts from the two surface counts in Step 1. This yields the four polynomials in the finding. In the split odd case, only the permitted prime powers \(q=7,13\) are zeros; in the split characteristic-two case the zeros are \(q=4,16\); in the nonsplit characteristic-two case only \(q=2\) is a zero, and the nonsplit odd case has no zeros. This proves the sharp five-field classification. For every \(n\), apply the same result over \(\mathbb F_{q^n}\). Finally, the elementary identity \(\exp(\sum_{n\ge1}a^nT^n/n)=(1-aT)^{-1}\) and its alternating-sign version give the four stated zeta functions.

## Verification

Run `python3 verify.py` (Python 3, standard library only); expected final marker: `VERIFY_OK`. The checker reconstructs the Eisenstein determinants exactly, checking all 351 unordered pairs and all 2,925 unordered triples; it enumerates projective points and the full geometric-line membership on thirteen finite fields of sizes 2 through 49. For three nonsplit prime fields it independently embeds rational points into the quadratic field and checks membership on all twenty-seven lines, confirming the descent argument. It also compares coefficients of the four zeta functions with the counting formulas for twelve extension degrees of every enumerated base field. `verify_output.txt` records the actual completed run. The integer determinant-norm test controls infinitely many characteristics; finite enumerations alone do not make that claim.

## Relationship to prior work

The explicit twenty-seven-line presentation appears in Polo-Blanco and Top (2009), §5.2, and is not new. Debarre's notes give the characteristic-two line field of definition, and Massarenti (2026), Corollary 8.3, computes the *whole Fermat cubic's* finite-field point count. Cooley (2013) studies rational points and generation on smooth cubic surfaces with rational lines. The present result instead classifies the rational points of the open surface obtained by removing *all geometric lines*, including the sharp five-field nonexistence and its four rational zeta functions. Its formulas follow from the known surface count combined with a characteristic-sensitive incidence and descent census; no claim is made that either ingredient is new.

## Limitations

No statement is made in characteristic three, or for arbitrary smooth or diagonal cubic surfaces. The novelty assessment concerns the explicit combined line-complement arithmetic classification, not the classical line configuration or the full-surface zeta function; it is possible that older incidence treatments implicitly imply the result. The independent scientific audit has not been performed.

## References

1. I. Polo-Blanco and J. Top, *A remark on parameterizing nonsingular cubic surfaces*, Computer Aided Geometric Design **26** (2009), 842–849; first available online 2009-06-06. DOI: 10.1016/j.cagd.2009.06.001. Full text: https://www.math.rug.nl/~top/potop.pdf.
2. J. Cooley, *Cubic surfaces with one rational line over finite fields*, arXiv:1312.5905, posted 2013-12-20. https://arxiv.org/abs/1312.5905.
3. O. Debarre, *Around cubic hypersurfaces*, notes dated 2015-06-23, §4.1. https://www.math.ens.psl.eu/~debarre/Duesseldorf2014.pdf.
4. A. Massarenti, *Rational points on even-dimensional Fermat cubics*, Transactions of the London Mathematical Society **13** (2026), e70028; first published 2026-03-20, Corollary 8.3. https://doi.org/10.1112/tlm3.70028.
