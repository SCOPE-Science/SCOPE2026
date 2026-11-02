# Complete affine-square orbit spectrum of three-shift quadratic-residue covers

## Finding
Let \(q\) be an odd prime power and \(Q_0=\{z^2:z\in\mathbb F_q\}\), including zero. A *covering triple* is a set \(A\subseteq\mathbb F_q\) of three distinct elements for which \(A+Q_0=\mathbb F_q\). Let \(\mathcal C_q\) be the set of covering triples and let \(\Gamma_q\) act by \(A\mapsto sA+b\), where \(b\in\mathbb F_q\) and \(s\in Q_0\setminus\{0\}\).

The orbit-size multiset of \(\Gamma_q\) on \(\mathcal C_q\) is completely determined by this table:

| \(q\) | Orbit sizes | Number of covering triples |
| --- | --- | ---: |
| 3 | 1 | 1 |
| 5 | 5, 5 | 10 |
| 7 | 7, 21 | 28 |
| 9 | 6, 6, 36 | 48 |
| 11 | 55 | 55 |
| 13 | 26, 39 | 65 |
| 17 | 68 | 68 |
| 25 | 100 | 100 |

For every other odd prime power \(q\), \(\mathcal C_q\) is empty. For \(q\in\{3,5\}\), fewer than three translates already cover the field; for the other six admissible field sizes, three is minimal. The classification of domination numbers and the \(q=25\) single orbit were already known; the principal result here is the complete *affine-square orbit spectrum* for all sizes, including unequal orbit splits and the two different size-six orbits at \(q=9\).

## Assumptions and scope
The field has odd characteristic, and \(Q_0\) always contains zero. An orbit is taken under translations and nonzero-square dilations, not under the entire semilinear automorphism group. For the extension fields, an element \(i\theta+j\), where \(0\le i,j<p\), is encoded by the integer \(pi+j\); the basis element satisfies \(\theta^2=-1\) at \(q=9\) and \(\theta^2=-2\) at \(q=25\). These quotient polynomials are irreducible over the indicated prime fields.

## Proof
Let \(\chi\) be the quadratic character of \(\mathbb F_q\), extended by \(\chi(0)=0\). For three distinct shifts \(a,b,c\) put \(U=|\mathbb F_q\setminus(A+Q_0)|\). The identity
\[
8U=q-3-\sum_{x\in\mathbb F_q}\chi((x-a)(x-b)(x-c))
-\sum_{t\in A}\prod_{v\in A\setminus\{t\}}(1-\chi(t-v))
\]
follows by expanding the product of the three complement indicators \((1-\chi(x-t)-\mathbf1_{x=t})/2\). Each of the three pair-character sums is \(-1\), accounting for the term \(-3\). Because the cubic has three distinct roots, its character sum is the deviation of the point count of the nonsingular elliptic curve \(y^2=(x-a)(x-b)(x-c)\), and Hasse's bound gives absolute value at most \(2\sqrt q\).

Every product in the final sum is either zero or four. When \(q\equiv3\pmod4\), at most one product can equal four, because \(\chi(v-t)=-\chi(t-v)\). Therefore \(8U\ge q-7-2\sqrt q>0\) for every \(q\ge19\) in that congruence class. When \(q\equiv1\pmod4\), their sum is at most twelve, so \(8U\ge q-15-2\sqrt q>0\) for \(q\ge29\). Thus every admissible order belongs to \(\{3,5,7,9,11,13,17,25\}\).

The remaining classification is an *exhaustive finite proof*, not an inference from sampling. The accompanying standalone script constructs each field with exact arithmetic; forms the complete set \(Q_0\); visits all \(\binom q3\) unordered triples; retains precisely those whose three translates cover all \(q\) elements; then partitions that entire set into orbits under the explicitly enumerated group \(\Gamma_q\). It checks that every generated orbit belongs to the covering set and that the orbits partition it with exactly the sizes in the table. There are at most \(\binom{25}{3}=2300\) triples per field. A separate bit-set union implementation verifies the covering predicate independently. Thus the finite component is an exhaustive exact certificate of all cases left by the infinite Hasse argument.

For the smaller-number-of-translates assertion, \(|Q_0|=(q+1)/2\), and for every nonzero \(t\),
\[
|Q_0\cap(Q_0+t)|=\frac{q+1+\chi(t)+\chi(-t)}4.
\]
This shows that two translates can cover only for \(q=3\) or \(q=5\), where explicit translates do cover. One translate never suffices.

## Verification
Run `python3 verification.py` using only the Python standard library. It prints the exact orbit sizes and representatives for each of eight fields and exits with `VERIFY_OK`. The field multiplication rules and the complete enumeration are included in the package. The direct-set and bit-mask implementations must agree for all triples. An executable certificate proves each finite assertion, while the Hasse character-sum argument proves that the finite list is exhaustive among all odd prime powers.

## Relationship to prior work
Zhou and Wu study the covering number \(\tau(q,d)\) for general multiplicative subgroups and give broad bounds, without the present orbit-spectrum classification. Existing Paley-graph and Paley-tournament domination tables already establish the admissible orders and minimum cover sizes, and a separate earlier exact classification establishes the single \(q=25\) orbit and its 100 covering triples. These facts are credited rather than claimed as new. The additional contribution is a simultaneous orbit-by-orbit classification of *all* three-center covers across the full admissible field range, with nontrivial multiple-orbit phenomena for \(q=5,7,9,13\). The affine-square action matters because it preserves \(Q_0\), unlike arbitrary nonsquare dilations.

## Limitations
No higher covering numbers or larger shift-set sizes are classified. The finite census is tied to the Hasse-reduced field sizes, and no assertion is made about full automorphism-group orbits rather than affine-square orbits. The priority assessment is not independent; further historical sources may contain equivalent orbit counts.

## References
1. J. Zhou and H. Wu, *Covering finite fields by translates of multiplicative subgroups*, arXiv:2610.25228v1 (18 October 2026), https://arxiv.org/html/2610.25228v1.
2. A. E. Brouwer, *Paley graphs* (dominating-set table), https://aeb.win.tue.nl/graphs/Paley.html.
3. *Restrained Domination in Self-Complementary Graphs*, Discussiones Mathematicae (2025), https://bibliotekanauki.pl/articles/32083901.pdf.
4. A. Abyzov, S. Cohen, P. Danchev and D. Tapkin, *Rings and finite fields whose elements are sums or differences of tripotents and potents*, Turkish Journal of Mathematics 48 (2024), https://journals.tubitak.gov.tr/math/vol48/iss5/2/.
