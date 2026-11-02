# A complete local density criterion for diagonal ternary cubic quotient sets

## Finding
Let \(p\ne3\) be a prime, and let \(a,b,c\) be nonzero integers. Define
\[
F(X,Y,Z)=aX^3+bY^3+cZ^3,
\qquad
R(F)=\{F(\mathbf x)/F(\mathbf y):\mathbf x,\mathbf y\in\mathbb Z^3,\ F(\mathbf y)\ne0\}.
\]
Then \(R(F)\) is dense in \(\mathbb Q_p\) **if and only if** either \(p\equiv2\pmod3\), or at least two of \(\nu_p(a),\nu_p(b),\nu_p(c)\) are congruent modulo three. In particular, for \(p\equiv1\pmod3\), having exactly two coefficient valuations congruent modulo three always forces density; this includes the nonsplit case in which the binary subform made from those two coefficients has a non-dense quotient set.

When \(p\equiv1\pmod3\) and all three coefficient valuations are pairwise incongruent modulo three, the exact complementary statement is
\[
\overline{R(F)}^{\mathbb Q_p}=\{0\}\cup\bigcup_{i,j=1}^3 (a_i/a_j)(\mathbb Q_p^\times)^3,
\quad (a_1,a_2,a_3)=(a,b,c).
\]
This non-dense closure occupies exactly three of the nine nonzero cubic cosets when \(abc\) is a cube in \(\mathbb Q_p\), and exactly seven of the nine otherwise. The distinct-valuation closure statement is also an instance of an earlier general local coset theorem; it is included here to state the complete ternary criterion, not as the principal new contribution.

## Assumptions and scope
The prime is arbitrary except \(p\ne3\). All three coefficients are nonzero integers, with no coprimality or positivity assumptions. The normalized valuation satisfies \(\nu_p(p)=1\). Variables in \(R(F)\) are integral. A stronger equality \(R(F(\mathbb Q_p^3))=\mathbb Q_p\) holds in every dense case; this does **not** assert that every target quotient is attained using ordinary integer coordinates.

## Proof
**Normalization and approximation.** Because \(F\) is homogeneous of degree three, multiplying all numerator and denominator variable coordinates by the same sufficiently large power of \(p\) shows
\[
R(F(\mathbb Q_p^3))=R(F(\mathbb Z_p^3)).
\]
Since \(\mathbb Z^3\) is dense in \(\mathbb Z_p^3\) and the quotient map is continuous wherever the denominator is nonzero, every quotient of \(p\)-adic vectors lies in the closure of \(R(F)\). Conversely, \(R(F)\) lies in the local quotient set. We may freely replace variables by nonzero rational \(p\)-power multiples and divide all coefficients by a common nonzero scalar when analyzing the local quotient set.

**A binary unit-surjectivity lemma.** Let \(p\equiv1\pmod3\), so \(p\ge7\), and let \(\alpha,\beta\in\mathbb Z_p^\times\). If \(-\beta/\alpha\) is *not* a cube modulo \(p\), then
\[
\{\alpha x^3+\beta y^3:x,y\in\mathbb Z_p\}\supseteq\mathbb Z_p^\times.
\]
Indeed, fix any \(t\in\mathbb Z_p^\times\). The smooth plane cubic
\[
\alpha X^3+\beta Y^3=tZ^3
\]
over \(\mathbb F_p\) is a genus-one curve; its smoothness follows from \(p\ne3\) and the unit coefficients. The Hasse bound gives at least \(p+1-2\sqrt p>0\) projective \(\mathbb F_p\)-points. On the line at infinity \(Z=0\), a point would require \(-\beta/\alpha=(X/Y)^3\), contrary to the hypothesis. Therefore at least one point has \(Z\ne0\). It yields \(\alpha x^3+\beta y^3\equiv t\pmod p\), with a nonzero partial derivative \(3\alpha x^2\) or \(3\beta y^2\) modulo \(p\). Holding the other coordinate fixed, Hensel's lemma lifts this to equality with the prescribed \(p\)-adic unit \(t\). This proves the lemma.

**Exactly two valuation residues agree.** Suppose, after relabeling, \(\nu_p(a)\equiv\nu_p(b)\not\equiv\nu_p(c)\pmod3\). An invertible \(\mathbb Q_p\)-diagonal change of variables followed by a common scalar makes the form
\[
\alpha X^3+\beta Y^3+p^k\gamma Z^3,
\qquad \alpha,\beta,\gamma\in\mathbb Z_p^\times,
\quad k\in\{1,2\}.
\]
If \(-\beta/\alpha\) is a cube modulo \(p\), the binary subform \(\alpha X^3+\beta Y^3\) has a simple nonzero zero over \(\mathbb Z_p\). Varying one coordinate near that zero gives a whole open additive neighborhood of zero among its values, by the one-variable \(p\)-adic inverse-function/Hensel principle. Indeed, fix any nonzero binary value as a denominator and scale its input by sufficiently high powers of \(p\) so that multiplication by an arbitrary target belongs to the open ball of represented values around zero. Thus its quotient set is all of \(\mathbb Q_p\), and so is that of the ternary form.

Otherwise the binary unit-surjectivity lemma applies. The binary subform represents **every** value of valuation divisible by three (scale a unit representation by a cube of a power of \(p\)). The third coordinate represents nonzero values of valuation congruent to \(k\) modulo three. For any nonzero target \(w\in\mathbb Q_p\), if \(\nu_p(w)\equiv0\pmod3\), take a quotient of two binary values; if \(\nu_p(w)\equiv k\pmod3\), take a third-coordinate value divided by an appropriate binary value; if \(\nu_p(w)\equiv-k\pmod3\), reverse that quotient. In the latter two cases the binary unit-surjectivity lemma permits arbitrary matching of the unit factor. These are all three valuation classes because \(k\) is nonzero modulo three. Thus the local quotient set equals \(\mathbb Q_p\). When \(p\equiv2\pmod3\), every \(p\)-adic unit is a cube (the cube map is bijective modulo \(p\), and Hensel lifts it), so the split simple-zero argument instead applies to every equal-valuation pair.

**All three residues agree.** After an invertible local variable change, the coefficients are all units. The resulting diagonal cubic modulo \(p\) has a nonsingular projective zero for every \(p\ne3\) (the standard ternary cubic lemma, or the smooth genus-one Hasse bound, also valid at \(p=2\)). Hensel lifting gives a simple local zero, and the preceding open-neighborhood argument proves that the local quotient set equals \(\mathbb Q_p\). This case also follows from the established three-unit result of Antony--Barman--Miska.

**All three residues differ.** Let \(H=(\mathbb Q_p^\times)^3\). The valuations of the three nonzero summands in \(F\) lie in different classes modulo three, so their minimum is unique. Factoring the lowest-valuation term produces a factor in \(1+p\mathbb Z_p\), which is a cube because \(p\ne3\). Consequently every nonzero value lies in \(aH\cup bH\cup cH\), and the coordinate axes show that every element of each of these cosets is represented over \(\mathbb Q_p\). Therefore the nonzero quotient set is exactly \(\bigcup_{i,j}(a_i/a_j)H\). If \(p\equiv2\pmod3\), unit cubes exhaust all units and the three different coefficient valuations exhaust \(\mathbb Z/3\mathbb Z\); the quotient set is \(\mathbb Q_p\). If \(p\equiv1\pmod3\), the quotient group \(\mathbb Q_p^\times/H\) is \((\mathbb Z/3\mathbb Z)^2\). The three coefficient classes have distinct first (valuation) coordinates. Their pairwise differences occupy three classes if the points are collinear (equivalently their sum is zero, or \(abc\in H\)) and seven otherwise. Hence at least two of the nine clopen cubic cosets are omitted, proving non-density and the claimed exact closure. Zero lies in the closure by cubic scaling.

This exhausts every prime \(p\ne3\) and every possible valuation pattern.

## Verification
The included `verify.py` enumerates every nonsplit unit-coefficient pair modulo all fourteen primes \(p\le127\) with \(p\equiv1\pmod3\) (47,232 pairs) and verifies that the binary form represents every residue. It also checks all 27 cubic-coset configurations and the explicit \(p=7\) example \(X^3+2Y^3+7Z^3\). The all-prime conclusion depends on the Hasse bound, Hensel lifting and valuation arguments above, not finite enumeration. Run `python3 verify.py` using standard Python 3.

## Relationship to prior work
Antony--Barman--Miska (2022), Theorems 1.1 and 1.5 and Corollary 1.6, establish the binary split criterion and density when three coefficient valuations agree modulo three. Their Theorem 1.3 assumes \(\gcd(3,p(p-1))=1\), so it does not handle primes \(p\equiv1\pmod3\). The missing **exactly-two-equal** case with a nonsplit binary subform is supplied here. Antony--Barman et al. (2023, initial preprint) investigate broader forms and almost-all-prime density; their inspected stated results do not give this fixed-prime mixed-valuation classification. The distinct-valuation complement also follows from a previously recorded general local coset statement and is not asserted as a separately new result. Originality remains subject to possible unindexed equivalent literature.

## Limitations
No claim is made for \(p=3\), arbitrary nondiagonal cubics, or quotient sets formed by nonhomogeneous polynomials. The positive cases are exactly surjective only for \(p\)-adic variable coordinates, while the integer-coordinate quotient sets are proved dense. The finite checker is illustrative, not an infinite proof. Bibliographic priority has not been independently certified.

## References
Antony, D.; Barman, R., *\(p\)-Adic quotient sets: cubic forms*, arXiv:2110.05420, first posted 11 October 2021.

Antony, D.; Barman, R.; Miska, P., *\(p\)-Adic quotient sets: diagonal forms*, arXiv:2201.04372v1, first posted 12 January 2022; especially Theorems 1.1, 1.3, 1.5 and Corollary 1.6.

Antony, D.; Barman, R.; Gajović, S.; Širola, D., *On \(p\)-adic denseness of quotients of values of integral forms*, arXiv:2308.08907, first posted 17 August 2023; particularly Theorem 1.2 and Lemma 2.13 in the later accessible version.

Hasse's theorem on the number of rational points on a smooth genus-one curve over a finite field; and the classical Hensel lifting lemma.
