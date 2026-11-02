# Sharp early square-failure law and a full rigidity class for reciprocal-sum sequences

## Finding

For every integer \(h\ge 1\) and starting integer \(x_0\ge1\), define the positive-rational sequence
\[
x_{n+1}=\frac{h^2}{x_0+\cdots+x_n},\qquad x_n=\frac{a_n}{b_n}\quad(\gcd(a_n,b_n)=1),
\]
and let \(E_j(x_0;h)\) be \(1\) if \(b_j+2a_j/h\) is **not** the square of an integer, and \(0\) otherwise, for \(j\ge2\).

For each prime \(p\), define
\[
\kappa_1(p)=\begin{cases}1&p=2,\\2&p\equiv1\pmod4,\\0&p\equiv3\pmod4,\end{cases}
\quad
\kappa_2(p)=\begin{cases}
2&p=5,\\
4&p\equiv1,9\pmod{20}\ (p\ne5),\\
0&\text{otherwise}.
\end{cases}
\]
When \(p^a\parallel h\), put \(m_p=p^{a+1}\), and use empty products equal to \(1\). Define
\[
A_h=\prod_{p^a\parallel h}\left(1-\frac{\kappa_1(p)}{m_p}\right),\quad
B_h=\prod_{p^a\parallel h}\left(1-\frac{\kappa_2(p)}{m_p}\right),\quad
C_h=\prod_{p^a\parallel h}\left(1-\frac{\kappa_1(p)+\kappa_2(p)}{m_p}\right).
\]

**Theorem (joint law).** The two failure indicators are periodic as functions of \(x_0\), with period dividing \(L_h=h\operatorname{rad}(h)\). Their joint natural densities, with the first coordinate \(E_2\) and second \(E_3\), are exactly
\[
\begin{array}{c|cc}
 & E_3=0&E_3=1\\\hline
E_2=0&C_h&A_h-C_h\\
E_2=1&B_h-C_h&1-A_h-B_h+C_h
\end{array}.
\]
For each of these four events its count among \(1\le x_0\le X\) is the displayed rational density times \(X\), with error \(O_h(1)\).

**Theorem (sharp all-index rigidity).** The following are equivalent:

1. For **every** \(x_0\ge1\), every index \(j\ge3\) has \(E_j(x_0;h)=0\).
2. No prime factor of \(h\) is \(5\) or belongs to a residue class \(1\) or \(9\) modulo \(20\).

In this class, the distribution of the total number of failures across **all** \(j\ge2\) is exactly: zero failures with density \(A_h\), one failure (necessarily at \(j=2\)) with density \(1-A_h\), and no other counts. The necessity is strong: whenever condition 2 fails, some positive integer \(x_0\) has \(E_3=1\).

In particular, choosing \(h\) as a product of arbitrarily many distinct primes congruent to \(13\) modulo \(20\) gives unbounded \(\omega_1(h)\) but at most one exceptional index for every starting value, whereas the published universal bound allows \(\omega_1(h)\) exceptional indices.

## Assumptions and scope

All integers \(h\) and \(x_0\) are positive. A *perfect square* means the square of an integer, not merely a rational square. The notation \(p^a\parallel h\) means \(a\ge1\) is the exact exponent of \(p\) in \(h\), and \(\operatorname{rad}(1)=1\). Natural density is taken over starting integers \(1\le x_0\le X\) with \(h\) fixed. The theorem does not give the complete failure-count distribution for arbitrary \(h\) containing a prime \(5\) or congruent to \(1\) or \(9\) modulo \(20\).

## Proof

**1. Exact square criterion.** Let \(S_n=\sum_{j=0}^n x_j\), and reduce \(t_n=S_n/h=u_n/v_n\) to positive coprime integers. With \(g=\gcd(x_0,h)\), we have \((u_0,v_0)=(x_0/g,h/g)\) and
\[
(u_{n+1},v_{n+1})=(u_n^2+v_n^2,\,u_nv_n).
\]
The two coordinates stay coprime, as a common prime would divide exactly one of \(u_n,v_n\) and consequently could not divide their sum of squares. Since \(x_{n+1}=hv_n/u_n\), one obtains, for \(n\ge1\),
\[
b_{n+1}+\frac{2a_{n+1}}h
=\frac{(u_{n-1}+v_{n-1})^2}{\gcd(h,u_n)}.
\]
Proposition 4.1 of Matijasevick–Rodríguez–Salazar proves that the displayed number is an integer square if and only if \(\gcd(h,u_n)=1\). The critical valuation argument is as follows. If an odd prime \(p\) divides \(u_n=u_{n-1}^2+v_{n-1}^2\), it does not divide \(u_{n-1}+v_{n-1}\) (otherwise it divides both their sum and difference, contradicting coprimality). The expression thus has negative \(p\)-adic valuation. If \(p=2\), the preceding coordinates are both odd, the denominator has \(2\)-adic valuation one, and the square numerator has even valuation; the quotient has odd valuation. Conversely, a unit denominator leaves an integer square. Therefore
\[
E_j(x_0;h)=1\quad\Longleftrightarrow\quad \exists p\mid h:\ p\mid u_{j-1},\qquad j\ge2.
\]

**2. Local reduction and two disjoint polynomials.** Fix \(p^a\parallel h\). If \(v_p(x_0)<a\), then \(p\mid v_0\) and \(p\nmid u_0\); if \(v_p(x_0)>a\), the reverse holds. In either case \(u_1\not\equiv0\pmod p\), \(v_1\equiv0\pmod p\), and all later numerators remain units modulo \(p\). The only relevant starting values therefore satisfy \(v_p(x_0)=a\). Such values are precisely the \(p-1\) residue classes
\[
x_0\equiv p^a c\pmod{p^{a+1}},\qquad c\in\mathbb F_p^\times.
\]
For these classes \(v_0\) is a unit modulo \(p\) and \(t=u_0v_0^{-1}\pmod p\) runs bijectively through \(\mathbb F_p^\times\). The first two numerators give the exact local conditions
\[
p\mid u_1\Longleftrightarrow t^2+1=0,\qquad
p\mid u_2\Longleftrightarrow t^4+3t^2+1=0
\quad\text{in }\mathbb F_p.
\]
These conditions are disjoint: if \(p\mid u_1\), then \(p\nmid v_1\) and \(u_2\equiv v_1^2\ne0\pmod p\).

**3. Root census.** For \(p=2\), only \(t=1\) is available, and it satisfies the first but not the second polynomial. For odd \(p\equiv3\pmod4\), neither polynomial has a nonzero root, because each equation means a primitive sum of two squares vanishes after one or two steps. For odd \(p\equiv1\pmod4\), fix \(i\in\mathbb F_p\) with \(i^2=-1\). The first polynomial has exactly two roots. The second factors as
\[
t^4+3t^2+1=(t^2-it+1)(t^2+it+1).
\]
The factors have no common roots. Their discriminants both equal \(-5\). At \(p=5\), each has one double root, giving two distinct roots in total. For other primes \(p\equiv1\pmod4\), quadratic reciprocity gives \(\left(\frac{-5}{p}\right)=\left(\frac5p\right)\), which is \(+1\) exactly for \(p\equiv1,9\pmod{20}\) and \(-1\) exactly for \(p\equiv13,17\pmod{20}\). Thus the two local root counts are precisely \(\kappa_1(p)\) and \(\kappa_2(p)\).

**4. Joint densities and periodicity.** The local events depend only on \(x_0\bmod p^{a+1}\). Exactly \(\kappa_1(p)\) residue classes trigger the first failure and exactly \(\kappa_2(p)\) trigger the second, disjointly. The Chinese remainder theorem makes the local residue classes independent over \(L_h=\prod_{p^a\parallel h}p^{a+1}\). Multiplying local avoidance probabilities gives \(A_h,B_h,C_h\); inclusion–exclusion gives the displayed table. Any event is a union of residue classes modulo \(L_h\), so counting to \(X\) incurs error at most \(L_h\).

**5. All-index rigidity.** If \(p\equiv3\pmod4\), coprimality and the sum-of-two-squares criterion exclude \(p\mid u_n\) for every \(n\ge1\). If \(p=2\), the pair \((u_0,v_0)\) either has opposite parities, so all \(u_n\) for \(n\ge1\) are odd, or both coordinates are odd, so \(u_1\) is even and all \(u_n\) for \(n\ge2\) are odd.

Now let \(p\equiv13,17\pmod{20}\) and suppose, toward a contradiction, that \(p\mid u_n\) for some \(n\ge2\). The previous pair must have both coordinates nonzero modulo \(p\), and the ratio \(s=u_{n-1}v_{n-1}^{-1}\) satisfies \(s=\pm i\), where \(i^2=-1\). Since \(n-1\ge1\) and the earlier pair also has both coordinates nonzero modulo \(p\), there is \(t\in\mathbb F_p^\times\) with \(t+1/t=s\). The quadratic equation \(t^2-st+1=0\) would have discriminant \(s^2-4=-5\), a quadratic nonresidue for these primes. Contradiction. Consequently, under condition 2, no prime divisor of \(h\) divides a numerator \(u_n\) at \(n\ge2\), and there are no failures at \(j\ge3\).

Conversely, if \(h\) has a prime \(p=5\) or \(p\equiv1,9\pmod{20}\), the root census gives a nonzero \(t\in\mathbb F_p\) with \(t^4+3t^2+1=0\). Choose a positive integer \(t_0\equiv t\pmod p\) and set \(x_0=ht_0\); then \(v_0=1\), \(p\mid u_2\), and the third term fails. This establishes equivalence. In the rigid class only \(E_2\) can be one, and its density is \(1-A_h\). Infinitely many distinct primes congruent to \(13\pmod{20}\) exist by Dirichlet's theorem, giving the claimed unbounded contrast with \(\omega_1(h)\). \(\square\)

## Verification

Run `python3 verify.py` using the Python standard library; no data download or external dependency is needed. The checker enumerates all local roots for the 62 primes below 300, exact CRT counts for 19 sample moduli (75,293 starting residue classes), and independent rational-sequence checks. Expected first line:

`VERIFY_OK local_primes=62 crt_examples=19 starting_residues=75293 direct_rational_checks=yes classification_checks=yes`

The exact finite calculations independently exercise the formulas at small parameters. They do not establish the infinite prime classification or the all-parameter theorem; those follow from the proofs above and quadratic reciprocity.

## Relationship to prior work

Matijasevick, Rodríguez and Salazar, arXiv:2610.00765v1 (September 30, 2026), provide the reduced-coordinate recurrence and exact square criterion (Lemmas 2.2 and Proposition 4.1), and their Theorem B bounds the number of failures along any one sequence by \(\omega_1(h)\). Their Section 7, Question (1), specifically asks for proportions of starting values with prescribed failure counts; Remark 4.2 identifies finite-field preimage trees as the relevant framework. They do not state the above mod-\(20\) all-index rigidity classification or the exact two-index joint distribution. In particular, an upper bound of \(\omega_1(h)\) does not imply the much smaller maximum \(1\) for the claimed infinite family.

Jones and Manes, *Galois theory of quadratic rational functions* (2014), study the same quadratic rational map within the general theory of preimage trees; their Figure 2 depicts the first two preimage levels. The present statement does **not** claim new preimage polynomials or a new factorization, but translates finite-field splitting and all-depth obstructions into precise starting-value frequencies and a sharp integer-modulus classification. The general Galois results and diagram do not state these integer-sequence densities. The possible derivability as an unrecorded specialization remains a priority risk.

## Limitations

The result solves the full failure-count distribution only in the stated rigid class of \(h\) and gives the first two failure indicators for all \(h\); it does not determine later failures for general \(h\). Finite checks are corroborative, not a proof. The literature comparison cannot guarantee historical uniqueness, particularly relative to a 2026 companion preprint cited but not located in accessible full text. No independent mathematical audit has been performed.

## References

1. Mateo Matijasevick, Santiago Rodríguez and Gregorio Salazar, *Perfect squares in reciprocal-sum sequences and primes that are inert in quadratic fields*, arXiv:2610.00765v1, first submitted September 30, 2026. https://arxiv.org/html/2610.00765v1
2. Rafe Jones and Michelle Manes, *Galois theory of quadratic rational functions*, Comment. Math. Helv. 89 (2014), 173–213; arXiv:1101.4339. https://arxiv.org/abs/1101.4339
3. Mateo Matijasevick, *Arithmetic dynamics of z+k/z: Galois groups, prime divisors of orbits, and zeros of iterates*, cited as a 2026 preprint in Reference 2 of arXiv:2610.00765v1; full text not located in this comparison.
