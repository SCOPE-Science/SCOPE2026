# Two-prime classification of exponential unitary perfect numbers

## Statement

For an integer
\[
n=\prod_i p_i^{a_i}>1,
\]
write \(d\mid^* a\) when \(d\mid a\) and \(\gcd(d,a/d)=1\). The sum of the exponential unitary divisors is
\[
\sigma^{(e)*}(n)=\prod_i\left(\sum_{d\mid^* a_i}p_i^d\right).
\]
An integer is **e-unitary perfect** when \(\sigma^{(e)*}(n)=2n\).

### Theorem

**The only e-unitary perfect integer with exactly two distinct prime factors is**
\[
\boxed{36=2^2 3^2}.
\]

Consequently, any e-unitary perfect number that is not e-perfect must have at least three distinct prime factors.

## Proof

A classical result for this notion is that no odd e-unitary perfect integer exists; this appears already in the 1971 abstract of Subbarao and Suryanarayana and is proved again as Theorem 6 of Minculete--Tóth (2011). Thus an e-unitary perfect integer with exactly two distinct prime factors has the form
\[
n=2^a q^b,
\]
where \(q\) is an odd prime and \(a,b\ge 1\).

Put
\[
U_a=\sum_{d\mid^* a}2^d,
\qquad
V_b=\sum_{e\mid^* b}q^e.
\]
The perfectness equation is
\[
U_aV_b=2^{a+1}q^b. \tag{1}
\]
Since \(1\mid^* a\) and every other unitary divisor of \(a\) is at least 2,
\[
A:=\frac{U_a}{2}=\sum_{d\mid^* a}2^{d-1}
\]
is odd. Similarly
\[
B:=\frac{V_b}{q}=\sum_{e\mid^* b}q^{e-1}\equiv1\pmod q.
\]
Dividing (1) by \(2q\) gives
\[
AB=2^a q^{b-1}. \tag{2}
\]
Because \(A\) is odd, every prime divisor of \(A\) is \(q\); because \(q\nmid B\), all of the \(q\)-power on the right of (2) lies in \(A\). Hence
\[
A=q^{b-1},\qquad B=2^a. \tag{3}
\]

Normalize (3) by setting
\[
S_a=\frac{A}{2^{a-1}}=\sum_{d\mid^*a}2^{d-a},
\qquad
R_b=\frac{B}{q^{b-1}}=\sum_{e\mid^*b}q^{e-b}.
\]
Then
\[
S_aR_b=2. \tag{4}
\]
Every proper unitary divisor \(e<b\) is among \(1,\dots,b-1\), so
\[
R_b
\le 1+\sum_{e=1}^{b-1}q^{e-b}
<1+\frac1{q-1}
\le\frac32.
\]
Therefore (4) forces
\[
S_a>\frac43. \tag{5}
\]

If \(a=1\), then \(S_a=1\), contradicting (5). Assume \(a\ge2\). Every proper divisor of \(a\), hence every proper unitary divisor of \(a\), is at most \(\lfloor a/2\rfloor\). Thus
\[
S_a\le 1+\sum_{d=1}^{\lfloor a/2\rfloor}2^{d-a}. \tag{6}
\]
If \(a=2k+1\), then the right side of (6) is
\[
1+2^{-k}-2^{-2k}\le \frac54<\frac43.
\]
If \(a=2k\) with \(k\ge3\), it is
\[
1+2^{1-k}-2^{1-2k}\le 1+\frac14-\frac1{32}=\frac{39}{32}<\frac43.
\]
Hence only \(a=2\) or \(a=4\) can survive (5).

For \(a=2\),
\[
A=1+2=3.
\]
Equation (3) gives \(q^{b-1}=3\), so \(q=3\) and \(b=2\). Then
\[
B=1+3=4=2^2,
\]
and indeed \(n=36\) is e-unitary perfect.

For \(a=4\), the unitary divisors of 4 are \(1,4\), so
\[
A=1+2^3=9.
\]
Equation (3) forces \(q=3\) and \(b=3\). But the unitary divisors of 3 are \(1,3\), giving
\[
B=1+3^2=10\ne16=2^4,
\]
a contradiction. This proves the theorem.

For the corollary, there is no one-prime e-unitary perfect integer: odd ones are excluded by the cited theorem, while for \(2^a\),
\[
\sigma^{(e)*}(2^a)\le\sum_{d=1}^a2^d=2^{a+1}-2<2^{a+1}.
\]
The unique two-prime example is 36, whose exponents are squarefree and hence whose e-unitary and ordinary exponential divisor sums coincide; thus 36 is e-perfect. Therefore any e-unitary perfect number that is not e-perfect has at least three distinct prime factors.

## Context and relation to earlier work

Subbarao and Suryanarayana's 1971 Notices abstract explicitly discusses exponentially unitary perfect numbers and proves that none is odd. Minculete and Tóth (2011) systematically develop exponential unitary divisors, prove the same parity theorem, and ask whether there is an e-unitary perfect number that is not e-perfect. Current OEIS data list 36 as the smallest primitive e-unitary perfect number and report that all known examples remain e-perfect.

There is a closely related but logically different older theorem for **e-perfect** numbers: Hanumanthachari, Subrahmanya Sastri and Srinivasan (1978), as summarized in Sándor--Crstici's *Handbook of Number Theory II*, proved that the only e-perfect number with two distinct prime factors is 36. The theorem above establishes the corresponding statement for e-unitary perfectness directly. This is not obtained merely by citing the e-perfect classification, because whether every e-unitary perfect number is e-perfect is itself an open question.

## Reproducibility

`artifacts/verify.py` independently implements unitary divisors of exponents and the exponential-unitary divisor sum using exact integer arithmetic. It checks all odd primes \(q<500\) and \(1\le a,b\le20\), finding only \((a,q,b,n)=(2,3,2,36)\), and verifies the elementary \(S_a\) upper-bound reduction through \(a=40\). This finite computation is only a consistency check; the theorem is proved for all exponents and primes above.

## Limitations

- The result classifies support size exactly two; it does not classify e-unitary perfect numbers with three or more distinct prime factors.
- It does not resolve whether every e-unitary perfect number is e-perfect; it only shows that any counterexample must have at least three distinct prime factors.
- Originality is asserted only to the best of our knowledge. Exact-phrase and synonymous searches, the 2011 primary paper, current OEIS records, and a 2025 paper using the same e-unitary terminology were checked. The 1971 Notices item was available through indexed text but its full issue could not be directly inspected; the 1978 e-perfect paper was identified and its two-prime theorem was checked through a standard secondary source. An unindexed theorem under older terminology remains the main residual originality risk.

## References

1. M. V. Subbarao and D. Suryanarayana, “Exponentially perfect and unitary perfect numbers,” *Notices Amer. Math. Soc.* 18 (1971), 798–799. Indexed issue: https://www.ams.org/journals/notices/197108/197108FullIssue.pdf
2. N. Minculete and L. Tóth, “Exponential unitary divisors,” *Annales Univ. Sci. Budapest., Sect. Comp.* 35 (2011), 205–216. https://doi.org/10.71352/ac.35.205 ; https://ac.inf.elte.hu/Vol_035_2011/doi/205_35.pdf
3. J. Hanumanthachari, V. V. Subrahmanya Sastri and V. Srinivasan, “On e-perfect numbers,” *Math. Student* 46(1) (1978), 71–80. Bibliographic link: https://schoolbooksarchive.azimpremjiuniversity.edu.in/handle/20.500.12497/11737
4. J. Sándor and B. Crstici, *Handbook of Number Theory II*, Kluwer, 2004, Chapter 1, pp. 51–53. https://link.springer.com/book/10.1007/1-4020-2547-9
5. OEIS A391281, “Primitive e-unitary perfect numbers.” https://oeis.org/A391281
6. OEIS A322858, “e-perfect numbers that are not e-unitary perfect.” https://oeis.org/A322858
7. J. Kalita and H. K. Saikia, “e-Zumkeller Numbers and e-Unitary Zumkeller Numbers,” *Palestine Journal of Mathematics* 14(3) (2025), 684–691. https://pjm.ppu.edu/sites/default/files/papers/PJM_14(3)_2025_684_to_691.pdf.pdf
