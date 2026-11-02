# The first three-prime-square layer of odd exactly \(3\)-deficient-perfect numbers

## Finding
An integer \(n\) is *exactly \(3\)-deficient-perfect* if there are three distinct proper positive divisors \(d_1,d_2,d_3\) such that
\[
\sigma(n)=2n-(d_1+d_2+d_3).
\]
For any three odd primes \(p<q<r\), the integer \(n=p^2q^2r^2\) is exactly \(3\)-deficient-perfect **if and only if**
\[
\boxed{n\in\{27225,38025,53361\}.}
\]
Moreover, all unordered triples of deficient divisors are as follows.

| \(n\) | prime factorization | all deficient-divisor triples |
|---|---|---|
| \(27225\) | \(3^2\cdot5^2\cdot11^2\) | \(\{1,25,825\}\) and \(\{11,15,825\}\) |
| \(38025\) | \(3^2\cdot5^2\cdot13^2\) | \(\{195,585,1521\}\) |
| \(53361\) | \(3^2\cdot7^2\cdot11^2\) | \(\{7,539,7623\}\) |

This is also the complete \(\Omega(n)=6\) layer among odd exactly \(3\)-deficient-perfect integers with \(\omega(n)=3\): odd exactly \(3\)-deficient-perfect integers are necessarily squares (proof below).

## Assumptions and scope
Here \(\sigma(n)\) is the sum of all positive divisors; \(\omega(n)\) counts distinct prime factors and \(\Omega(n)\) counts prime factors with multiplicity. All divisor sums use **three distinct proper positive divisors**: \(d_i<n\). The primes \(p,q,r\) are distinct, odd and strictly increasing. There is no upper bound on the primes in the theorem; the proof reduces all possibilities to a finite exact certificate.

## Proof
**1. Parity and the natural exponent layer.** If \(n\) is odd and exactly \(3\)-deficient-perfect, every proper divisor \(d_i\) in its defining equation is odd, so \(\sigma(n)=2n-\sum_i d_i\) is odd. If \(n=\prod_j p_j^{a_j}\) with odd primes, then \(\sigma(n)\equiv\prod_j(a_j+1)\pmod2\). Thus every exponent \(a_j\) is even. With three distinct prime factors, the smallest multiplicity is six, necessarily \(n=p^2q^2r^2\).

**2. Bounding the smallest prime factors.** Put \(S(t)=1+t^{-1}+t^{-2}\). For any deficient-divisor triple define \(D_i=n/d_i\); these are distinct divisors of \(n\) larger than one. The defining identity is equivalent to
\[
S(p)S(q)S(r)+D_1^{-1}+D_2^{-1}+D_3^{-1}=2.
\]
Order the \(D_i\) increasingly. Because \(S\) is strictly decreasing and the reciprocal sum is maximized by the three smallest eligible divisors, the following exact strict inequalities exclude the indicated ranges:
\[
S(7)S(11)S(13)+\frac17+\frac1{11}+\frac1{13}=\frac{34666}{20449}<2
\]
whenever \(p\ge7\), since the three denominators are at least \(7,11,13\); and
\[
S(5)S(7)S(13)+\frac15+\frac17+\frac1{13}=\frac{410266}{207025}<2
\]
whenever \(p=5\), \(r\ge13\), since the denominators are at least \(5,7,13\). The only remaining \(p=5\) case is \((p,q,r)=(5,7,11)\). Finally, if \(p=3\) and \(q\ge37\), then \(r\ge41\) and the three smallest eligible divisors are at least \(3,9,37\), whence
\[
S(3)S(37)S(41)+\frac13+\frac19+\frac1{37}=\frac{41280322}{20711601}<2.
\]
Thus the only infinite-looking portion has \(p=3\) and
\[
q\in Q=\{5,7,11,13,17,19,23,29,31\},\quad r>q\text{ prime}.
\]

**3. A quadratic integer certificate covers every \(r\), however large.** For fixed \(q\in Q\), write \(n=9q^2r^2\) and \(u=13(q^2+q+1)\). Every proper divisor has a unique signature
\[
d=3^{2-a}q^{2-b}r^{2-c},\quad (a,b,c)\in\{0,1,2\}^3\setminus\{(0,0,0)\}.
\]
There are exactly 26 signatures, and selecting three distinct proper divisors is equivalent to choosing an unordered three-element subset of them. Given such a selection \(T\), define
\[
v_c=\sum_{(a,b,c)\in T}3^{2-a}q^{2-b}\quad(c=0,1,2),
\]
and \(K=18q^2-u-v_0\), \(B=u+v_1\), \(E=u+v_2\). The deficient-perfect equation becomes **exactly**
\[
K r^2-B r-E=0.
\]
Here \(B,E>0\), so a positive root requires \(K>0\) and is uniquely
\[
r=\frac{B+\sqrt{B^2+4KE}}{2K}.
\]
Consequently an integer \(r\) exists only when the discriminant is a square and the numerator is divisible by \(2K\). Exhaustively applying these exact-integer tests to the \(9\binom{26}{3}=23400\) signatures yields 22620 choices with \(K>0\), of which 57 have square discriminant, of which nine produce an integer \(r>q\). Listed with multiplicity, these are:

| \(q\) | all integral \(r>q\) from the quadratic test |
|---|---|
| \(5\) | \(11,11,13,14,203,204,404\) |
| \(7\) | \(11\) |
| \(13\) | \(62\) |
| \(11,17,19,23,29,31\) | none |

Exactly four signature selections have **prime** \(r\). Their \(q,r\) pairs are \((5,11)\) twice, \((5,13)\) once, and \((7,11)\) once; evaluating the three selected proper divisors gives precisely the four triples in the Finding table. The complete standard-library checker `VERIFY.py` implements all 23400 selections and checks the output by exact integer arithmetic, including direct divisor-sum verification for each witness. No prime cutoff is used in this part of the proof.

**4. The isolated \(p=5\) case.** For \((p,q,r)=(5,7,11)\), \(n=148225\) and \(2n-\sigma(n)=61439\). The 26 distinct proper divisors are exactly the monomials \(5^a7^b11^c\) with \(0\le a,b,c\le2\), excluding the exponent triple \((2,2,2)\). Direct exact enumeration of all \(\binom{26}{3}=2600\) unordered triples shows none sums to 61439 (also checked by the independently constructed divisor set in `VERIFY.py`). This closes the last case and completes the classification. \(\square\)

## Verification
Run `python3 VERIFY.py` using Python 3.8 or later. No third-party packages, networks or data files are needed. The verifier checks the three rational exclusion inequalities exactly, constructs the 26 signatures per permitted \(q\), tests every quadratic discriminant and positive integral root, checks primality by trial division, reconstructs each deficient divisor in each positive case, and independently checks the remaining \(p=5\) case by enumerating its proper divisors. The observed output is:

`VERIFY_OK signatures=23400 positive_K=22620 square_discriminants=57 integral_roots=9 witness_triples=4 integers=3 excluded_p5_case=148225`

The infinite range is handled by the preceding inequalities and the quadratic reduction. The finite calculation is exhaustive only **after** that reduction; a bounded enumeration of the primes alone would not prove the theorem.

## Relationship to prior work
Aursukaree and Pongsriiam's arXiv manuscript (first public 20 January 2020) defines exactly \(3\)-deficient-perfect integers, proves a parity lemma for odd instances, and classifies odd instances with at most **two** distinct prime factors: only \(1521\). It does not provide the present three-prime-square classification. The 2014 work of Tang and Feng treats **one** deficient divisor, not three. OEIS A331629 records computational examples of exactly \(3\)-deficient-perfect integers, but a list of values does not establish the all-prime implication or the complete witness multiplicities proved here. Related indexed classifications of squarefree integers \(2pq\) also concern even integers and a different exponent pattern. The literature comparison is not a claim of absolute priority.

## Limitations
The theorem classifies the first, six-factor, three-distinct-prime **odd** exponent layer. It does not classify odd exactly \(3\)-deficient-perfect numbers with three prime factors and larger even exponents, nor even integers of unrelated exponent patterns. The exhaustive quadratic certificate is supplied as executable source, not as a formal proof-assistant development. An equivalent unindexed classification may exist.

## References
1. S. Aursukaree and P. Pongsriiam, *On Exactly 3-Deficient-Perfect Numbers*, arXiv:2001.06953v1, first submitted 2020-01-20; later *Fibonacci Quarterly* 59 (2021), 33–46. https://arxiv.org/abs/2001.06953 .
2. M. Tang and M. Feng, *On deficient-perfect numbers*, *Bulletin of the Australian Mathematical Society* 90 (2014), 186–194. https://doi.org/10.1017/S0004972714000082 .
3. OEIS Foundation, A331629, *Integers that are exactly 3-deficient-perfect numbers*. https://oeis.org/A331629 .
