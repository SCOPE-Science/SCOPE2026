# Order-four rigidity for three-term power-sum congruences

## Finding
Let \(q,e\) be integers with \(q\ge2\), \(e\ge2\), \(\gcd(q,e)=1\), and multiplicative order \(\operatorname{ord}_e(q)=4\). Define \(m(q,e)\) to be the least positive integer \(t\) for which
\[
q^{a_1}+\cdots+q^{a_t}\equiv0\pmod e
\]
for nonnegative integer exponents \(a_1,\ldots,a_t\), with repetition permitted. Then
\[
\boxed{m(q,e)=3\quad\Longleftrightarrow\quad e=15\ \text{and}\ q\equiv7\text{ or }13\pmod{15}.}
\]
Equivalently, exactly one cyclic unit subgroup of multiplicative order four in a ring \(\mathbb Z/e\mathbb Z\) has *minimum* additive zero-sum length three: \(\{1,4,7,13\}\subset(\mathbb Z/15\mathbb Z)^\times\).

## Assumptions and scope
Both integers are unrestricted in size subject to the hypotheses. The exponents are arbitrary nonnegative integers; reducing them modulo four does not alter the residues, and cyclic shifts of all exponents multiply a sum by a unit. The theorem classifies **only the case \(m(q,e)=3\)** among pairs of multiplicative order four. It does not assert that \(m(q,e)\le4\) for every such pair.

## Proof
Write \(u\equiv q\pmod e\). The assumption \(\operatorname{ord}_e(q)=4\) gives \(u^4=1\) and \(u^2\ne1\) in \(\mathbb Z/e\mathbb Z\). Suppose a sum of three powers vanishes. Reduce the three exponents modulo four; since multiplication by any power of \(u\) is invertible, we may translate all exponents together modulo four. Up to translation and permutation, a three-element multiset of exponents in \(\mathbb Z/4\mathbb Z\) is one of
\[
(0,0,0),\quad(0,0,1),\quad(0,0,2),\quad(0,1,1),\quad(0,1,2).
\]
Indeed, three equal exponents give the first type. With exactly two equal, the circular separation is one or two, yielding the next three types. With all exponents distinct, their complement consists of one residue, giving the fifth type.

For type \((0,0,0)\), we obtain \(e\mid3\), incompatible with order four. For type \((0,0,2)\), the congruence \(2+q^2\equiv0\pmod e\), together with \(q^4\equiv1\pmod e\), yields \(e\mid3\) because
\[
(q^2+2)(q^2-2)-(q^4-1)=-3.
\]
For type \((0,1,2)\), divisibility of \(1+q+q^2\) yields \(q^3\equiv1\pmod e\); combining this with \(q^4\equiv1\pmod e\) forces \(q\equiv1\pmod e\), again impossible.

For type \((0,0,1)\), we have \(q\equiv-2\pmod e\), so \(e\mid((-2)^4-1)=15\). For type \((0,1,1)\), we have \(2q\equiv-1\pmod e\). Hence \(e\mid((2q)^4-1)\) as well as \(e\mid(q^4-1)\), and subtraction shows \(e\mid15\):
\[
((2q)^4-1)-16(q^4-1)=15.
\]
Therefore a three-term vanishing sum under the order-four assumption requires \(e\mid15\). The only positive divisors of \(15\) supporting a unit of order four are \(e=5\) and \(e=15\).

At modulus \(5\), each element of order four has square \(-1\), and thus \(1+q^2\equiv0\pmod5\). The minimum is therefore \(m(q,5)=2\), not three.

At modulus \(15\), the residues of exact multiplicative order four are \(2,7,8,13\). The residues \(7\) and \(13\) generate the same subgroup \(\{1,4,7,13\}\). The two sums
\[
1+7+7=15,\qquad1+1+13=15
\]
show that three terms suffice for both generators. Their squares are \(4\pmod{15}\), not \(-1\pmod{15}\), so two-term sums do not vanish: if two powers summed to zero then a power of \(q\) would equal \(-1\), which for an order-four element is possible only when \(q^2\equiv-1\pmod e\). One term cannot vanish because powers of a unit remain units. Thus \(m(7,15)=m(13,15)=3\).

For completeness, the other order-four generators \(2,8\pmod{15}\) form the subgroup \(\{1,2,4,8\}\). Its three-term sums are nonzero modulo \(15\), as follows either from the five orbit types above or a four-residue direct check; this also follows because neither generator is congruent to \(-2\) nor satisfies \(1+2q\equiv0\pmod{15}\). They therefore do not give further \(m(q,e)=3\) cases. This proves the stated equivalence.

## Verification
The proof is unrestricted and uses exact integer identities and a classification of five cyclic exponent patterns, not a finite search. Run the standalone standard-library verifier with `python3 verify.py`. It checks all unit residues of exact order four at moduli \(2\le e\le3000\), independently enumerates sums of one, two, and three powers, and confirms that the only cases with minimum length three occur at \(e=15\), \(q\equiv7,13\pmod{15}\). It also tests the two exceptional sums and an order-four example where the minimum exceeds four. The computation is a finite diagnostic, not a proof of the universal theorem.

## Relationship to prior work
The function \(m(q,e)\) and its digit-sum interpretation were introduced in the work of Breuer, Héthelyi, Horváth, and Külshammer [1]. Their characterization of \(m(q,e)=2\) supplies a useful comparison; their Part II supplies tables for bounded moduli and further results under distinct hypotheses [2]. Jacob and Külshammer [3] ask for a general understanding of the case \(m(q,e)=3\), and supply bounds and classifications for other regimes. The present theorem answers that question **within the entire multiplicative-order-four stratum**, including unbounded composite moduli; the finite tables do not imply the necessary global exclusion \(e\mid15\). The displayed exceptional list in [3, Corollary 8] does not enumerate the residues \(q\equiv7,13\pmod{15}\) at modulus \(15\), whereas their three-term witnesses here are explicit. This comparison does not require using the classification in Corollary 8.

## Limitations
This theorem does not classify \(m(q,e)\) for larger multiplicative orders or determine every value of \(m(q,e)\) for order four. Indeed, an order-four subgroup need not possess a four-term vanishing sum: \(\operatorname{ord}_{30}(7)=4\) and \(m(7,30)=6\). Mathematical originality has been checked against the relevant inspected texts and indexed records, not against every possible unindexed or unpublished proof.

## References
[1] T. Breuer, L. Héthelyi, E. Horváth, and B. Külshammer, “The Loewy Structure of Certain Fixpoint Algebras, Part I,” *Journal of Algebra* **558** (2020), 199–220, §6. Lawful author-posted full text: https://www.math.rwth-aachen.de/~Thomas.Breuer/gapdays2021/BHHK20.pdf.

[2] T. Breuer, L. Héthelyi, E. Horváth, and B. Külshammer, “The Loewy Structure of Certain Fixpoint Algebras, Part II,” *International Electronic Journal of Algebra* **30** (2021), 16–65, §2 and tables. DOI: 10.24330/ieja.969577; lawful full text: https://www.ieja.net/files/papers/volume-30/2-V30-2021.pdf.

[3] L. Jacob and B. Külshammer, “Congruences for Sums of Powers of an Integer,” arXiv:2204.09403v1, first public version dated 2022-04-20, §§1–3, Corollary 8. Full text: https://arxiv.org/pdf/2204.09403.
