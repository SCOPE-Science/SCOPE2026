# A binary digit proof of Rowland's second binomial-coefficient conjecture

## Finding

For every **odd prime** \(p\) and every positive integer \(n\), set \(m=2p\), \(L=1+\lfloor\log_2m\rfloor\), and let \(n_1=\lfloor n/p\rfloor\bmod p\) be the second base-\(p\) digit of \(n\). Define
\[
E_p(n)=\frac{2}{n}\binom{n}{2p}-\frac{(p+1)(n_1-1)}{p}\mathbf1_{p\mid n}.
\]
Then \(E_p(n)\) is an integer, and
\[
\boxed{E_p(n)\equiv\binom{n-1}{2p-1}\pmod2,\qquad
E_p(n)\ \text{odd}\iff ((n-1)\mathbin{\&}(2p-1))=2p-1.}
\]
Here \(\mathbin{\&}\) denotes bitwise binary AND. **This criterion equals, for every \(p\), exactly the residue-class parametrization in Conjecture 2 of Rowland (2011), and hence proves that conjecture in its entirety.** In particular, there are exactly \(2^z\) exceptional residue classes modulo \(2^L\), where \(z=L-s_2(2p)\) and \(s_2\) denotes the number of binary ones.

As a compact consequence, writing \(\{x\}=x-\lfloor x\rfloor\), for all \(n\ge1\) one has
\[
\left\{\frac1n\binom n{2p}\right\}=\left\{\frac{(p+1)(n_1-1)}{2p}\mathbf1_{p\mid n}+\frac12\mathbf1_{((n-1)\mathbin{\&}(2p-1))=2p-1}\right\}.
\]
Unlike a search over Rowland's parameter, the exceptional-class test requires just a single binary mask comparison.

## Assumptions and scope

The integer \(n\) is arbitrary and positive, \(p\ge3\) is prime, and \(\binom{a}{b}=0\) for nonnegative integers \(a<b\). The standard \(L\)-digit binary expansion of \(m\) is \(m=\sum_{i=0}^{L-1}m_i2^i\); it ends in \(m_1m_0=10\). The number \(z\) counts zero bits **within these \(L\) positions**, not leading zeros. The bit-mask formula depends only on the low \(L\) bits of \(n-1\). The term \(\mathbf1_{p\mid n}\) is an indicator.

The original parametrization is as follows. For \(1\le i<L\) with \(m_i=1\), let \(z_i\) be the number of zero digits in the ordinary binary expansion of \(m\bmod 2^{i+1}\), and put \(w_i=z_i-\mathbf1_{i=1}\). For each \(0\le j<2^z\), define
\[
R_m(j)\equiv m+\sum_{\substack{1\le i<L\\m_i=1}}2^i\left\lfloor\frac{j}{2^{w_i}}\right\rfloor\pmod{2^L}.
\]
The omitted \(i=0\) summand in the printed conjecture is identically zero since \(m_0=0\). The new claim includes **equality of this entire set** \(\{R_m(j):0\le j<2^z\}\) with the binary-mask exceptional set, not merely a proof of a related parity test.

## Proof

**1. Integrality and arithmetic parity.** Put \(C=\binom{n-1}{2p-1}\) and \(A=(p+1)(n_1-1)\mathbf1_{p\mid n}\). The elementary binomial identity gives
\[
E_p(n)=\frac{C-A}{p}.
\]
Since \(2p-1=p+(p-1)\) in base \(p\), Lucas's theorem modulo \(p\) implies \(C\equiv0\pmod p\) if \(p\nmid n\): the last digit of \(n-1\) is then at most \(p-2\). If \(p\mid n\), the two lowest digits of \(n-1\) are \((n_1-1)\bmod p\) and \(p-1\), so \(C\equiv n_1-1\pmod p\). Thus in every case \(C\equiv A\pmod p\), proving that \(E_p(n)\) is integral.

Because \(p\) is odd and \(A\) is even, reduction of \(C-A=pE_p(n)\) modulo two yields \(E_p(n)\equiv C\pmod2\). Lucas's theorem modulo two now gives
\[
C\text{ odd}\iff ((n-1)\mathbin{\&}(m-1))=m-1.
\]
This equivalence also handles \(n<m\): an integer smaller than \(m-1\) cannot contain all of its one-bits.

**2. Exact digit-deposition identity for the printed parametrization.** List the positions of the binary ones of \(m\) as
\[
1=i_1<i_2<\cdots<i_k=L-1.
\]
For these positions the exponents in the preceding definition are exactly
\[
w_{i_1}=0,\qquad w_{i_a}=i_a+1-a\quad(2\le a\le k).
\]
Indeed, the first two binary digits are \(10\), and for every higher one-bit position \(i_a\), the prefix ending at that position has \(i_a+1-a\) zero-bits.

List the **zero-bit positions of \(m-1\) among positions \(0,\ldots,L-1\)** as \(f_0<f_1<\cdots<f_{z-1}\). These are exactly position \(1\) and the zero positions of \(m\) at indices at least two; in particular \(f_0=1\). If \(j=\sum_{h=0}^{z-1}e_h2^h\), with \(e_h\in\{0,1\}\), we claim the exact integer identity
\[
\boxed{\sum_{a=1}^{k}2^{i_a}\left\lfloor\frac{j}{2^{w_{i_a}}}\right\rfloor
=\sum_{h=0}^{z-1}e_h2^{f_h}.}
\]
To prove it, expand each quotient as \(\lfloor j/2^w\rfloor=\sum_{h\ge w}e_h2^{h-w}\). Fix an index \(h\). Among the positions \(i_a\), exactly the first \(r=f_h-h\) have \(w_{i_a}\le h\). For \(a\ge2\), this inequality is equivalent to \(i_a<f_h\), since \(w_{i_a}\) counts the zeros of \(m\) through position \(i_a\) (the lowest zero at position zero included). The position \(i_1=1\) is always included. The number of one positions not exceeding \(f_h\) is indeed \(r=f_h-h\). The coefficient of \(e_h\) in the left side is therefore
\[
2^{h+1}+\sum_{a=2}^{r}2^{h+a-1}=2^{h+r}=2^{f_h};
\]
when \(r=1\), the empty sum gives the same equality. Summing over all \(h\) proves the identity.

**3. Exhaustion of the conjectured classes.** Since \(m\equiv2\pmod4\), the binary ones of \(m-1\) are at position zero and at precisely the higher one-bit positions of \(m\). Thus the positions \(f_h\) from Step 2 are exactly the complementary zero-bit positions of \(m-1\) within its \(L\)-bit representation. The digit-deposition identity now says
\[
R_m(j)-1\equiv (m-1)+\sum_he_h2^{f_h}\pmod{2^L}.
\]
The two addends have disjoint one-bit supports, so their addition has no carries. As \(j\) runs over its \(2^z\) possible values, the expression runs **bijectively** over all \(L\)-bit integers containing every one-bit of \(m-1\). These are exactly the residues satisfying \(((n-1)\mathbin{\&}(m-1))=m-1\), completing the proof of the printed Conjecture 2 and the fractional-part formula. \(\square\)

## Verification

A standalone exact-arithmetic program, `verify.py`, reconstructs Rowland's original floor-sum parametrization and independently enumerates the mask solutions. It checks equality over all residue classes for every odd prime \(p\le3000\), and directly forms the relevant binomial coefficients to check integer divisibility and parity for all one-period positive indices when \(p\le197\). The replay result is

`VERIFY_OK: 429 odd primes <=3000, all residues of Rowland parametrizations; 44 odd primes <=197 and 11816 exact integer-binomial checks`.

For \(p=3\), the mask gives precisely \(n\equiv6,0\pmod8\), the two classes written in the original paper. All infinite assertions follow from the algebraic/digit argument, not the finite tests.

To replay from this package, run `python verify.py` using Python 3 (standard library only).

## Relationship to prior work

Rowland's *Two binomial coefficient conjectures* (arXiv:1102.1464v1, 7 February 2011), Section 3, explicitly states the **same floor-sum parametrization as Conjecture 2** without a proof. Its preceding proposition establishes a fractional-part reduction; that proposition and the classical Lucas theorem make the **arithmetic bit-mask condition** elementary. The additional new step required to settle the **actual printed conjecture** is the exact digit-deposition identity that identifies its unusual floor-sum parametrization with the bit-mask set for every odd prime. The original paper observes that the feasibility of testing membership in its floor-sum residue set is unclear; the mask identity gives a direct test.

The Lu–Tsai periodicity theorem cited by Rowland establishes periodicity, not the exceptional-class parametrization. Earlier general congruence formulas modulo prime powers and Rowland's separate work on row counts concern different statements. Targeted searches of published mathematical literature did not locate the same digit-deposition identity or a proof of the exact conjecture. Non-discovery in those searches does **not** establish uniqueness.

## Limitations

This proves only Conjecture 2 in Rowland's paper, not its unrelated Conjecture 1 on residue-class counts modulo \(16\). The proof requires \(p\) odd and prime for the arithmetic integrality reduction. The binary digit-deposition lemma itself applies to any \(m\equiv2\pmod4\), without primality. No assertion is made for \(\binom n{pq}\) with arbitrary distinct primes. Earlier equivalent arguments in unlocated literature remain a possibility; independent scholarly validation has not been performed.

## References

1. E. Rowland, *Two binomial coefficient conjectures*, arXiv:1102.1464v1 (7 February 2011), Section 3, Conjecture 2. https://arxiv.org/html/1102.1464v1 ; author's PDF: https://ericrowland.github.io/papers/Two_binomial_coefficient_conjectures.pdf .
2. É. Lucas, *Sur les congruences des nombres eulériens et les coefficients différentiels des fonctions trigonométriques suivant un module premier*, Bulletin de la Société Mathématique de France **6** (1878), 49–54. Lucas's congruence modulo primes, cited as Reference 15 in Rowland (2011).
3. C.-J. Lu and S.-C. Tsai, *The periodic property of binomial coefficients modulo m and its applications*, 10th SIAM Conference on Discrete Mathematics (2000). Periodicity result quoted in Rowland (2011), Section 3.
