# The unique three-almost-prime alternating-divisor collision adjacent to twice a prime
## Finding
Let \(\beta\) denote the multiplicative alternating divisor-sum function:
\[
\beta(1)=1,\qquad
\beta(\ell^a)=\sum_{j=0}^{a}(-1)^j\ell^{a-j}
\]
for primes \(\ell\) and positive integers \(a\). Let \(\Omega(m)\) count prime factors with multiplicity. For every prime \(p\) and odd positive integer \(m\) satisfying
\[
m\in\{2p-1,2p+1\},\qquad \Omega(m)\le3,
\]
one has the complete classification
\[
\boxed{\beta(m)=\beta(2p)\quad\Longleftrightarrow\quad(p,m)=(97,195).}
\]
Consequently the only corresponding consecutive collision is
\[
\beta(194)=\beta(195)=96.
\]

## Assumptions and scope
The prime \(p\) may equal \(2\); that exceptional base is checked separately. The odd neighbor \(m\) is positive, and the bound \(\Omega(m)\le3\) is essential to the statement. In particular, no claim is made about the unrestricted equation \(\beta(n)=\beta(n+1)\), nor about the number of its solutions.

## Proof
When \(p=2\), the values are \(\beta(3)=2\), \(\beta(4)=3\), and \(\beta(5)=4\), so neither neighbor works. Assume henceforth \(p\ge3\). The multiplicativity of \(\beta\) gives
\[
\beta(2p)=p-1.
\]
Write \(m=2p+\varepsilon\) with \(\varepsilon\in\{-1,1\}\) and set \(c=\varepsilon+2\in\{1,3\}\). The desired equality is exactly
\[
2\beta(m)=m-c.\tag{1}
\]
Every odd integer \(m>1\) with \(\Omega(m)\le3\) has exactly one of the following prime-factorization shapes (letters denote odd primes, and letters occurring at different positions are distinct):
\[
q,\quad q^2,\quad q^3,\quad qr,\quad q^2r,\quad qrs.
\]
For a single prime \(q\), equation (1) yields \(2(q-1)=q-c\), hence \(q=2-c\), impossible for \(q\ge3\). For a square \(q^2\), it yields
\[
q^2-2q+2+c=0,
\]
whose left side is \((q-1)^2+1+c>0\). For a cube \(q^3\), it yields
\[
q\bigl((q-1)^2+1\bigr)+c-2=0,
\]
again impossible for \(q\ge3\), \(c\in\{1,3\}\).

For two distinct primes \(q<r\), the shape \(m=qr\) would imply
\[
(q-2)(r-2)=2-c.
\]
For \(c=3\), the right side is negative; for \(c=1\), it is \(1\), which would require \(q=r=3\), contradicting distinctness.

For \(m=q^2r\), with distinct primes \(q,r\), equation (1) becomes
\[
(q^2-2q+2)r=2q^2-2q+2-c.
\tag{2}
\]
If \(q=3\), this gives \(5r=14-c\in\{11,13\}\), impossible. If \(q\ge5\), it gives
\[
r=2+\frac{2q-2-c}{q^2-2q+2}<3,
\]
because \(q^2-4q+4+c=(q-2)^2+c>0\). This contradicts the fact that \(r\) is an odd prime.

It remains to consider \(m=qrs\) with \(3\le q<r<s\) distinct primes. Equation (1) becomes
\[
2(q-1)(r-1)(s-1)=qrs-c.
\tag{3}
\]
If \(q\ge5\), then \(r\ge7\), \(s\ge11\), and
\[
\frac{2(q-1)(r-1)(s-1)}{qrs}
\ge2\frac45\frac67\frac{10}{11}>1,
\]
contradicting (3), whose right side is strictly less than \(qrs\). If \(q=3\) and \(r\ge7\), the analogous lower bound is
\[
2\frac23\frac67\frac{10}{11}=\frac{240}{231}>1,
\]
again impossible. Therefore \((q,r)=(3,5)\). Equation (3) reduces to
\[
16(s-1)=15s-c,\qquad s=16-c.
\]
For \(c=1\), this gives the composite number \(s=15\); for \(c=3\), it gives the prime \(s=13\). Thus \(m=3\cdot5\cdot13=195\), and \(\varepsilon=1\), so \(p=(195-1)/2=97\), a prime. Finally,
\[
\beta(2\cdot97)=96,
\qquad
\beta(3\cdot5\cdot13)=2\cdot4\cdot12=96.
\]
This proves both necessity and sufficiency for all allowed primes and neighbors.

## Verification
The proof is an exhaustive symbolic treatment of the six possible factorization shapes; the sole surviving candidate has exact primality and function-value checks. The standalone script `verification/check.py` independently evaluates \(\beta\) via factorizations, checks the defining convolution on representative inputs, and searches primes up to an explicit finite bound for both neighboring directions; these finite tests are consistency checks and not the argument for the infinite quantifiers. To reproduce, run `python3 verification/check.py` in the package root.

## Relationship to prior work
Tóth's survey [1] defines \(\beta\), lists \(194\) among initial solutions of the unrestricted consecutive-equality equation, and asks whether infinitely many solutions exist (Problem 3). OEIS A206368 [2] similarly lists individual solutions, without the prime-neighbor and prime-complexity classification. The new statement establishes **uniqueness under a natural low-complexity constraint**, rather than rediscovering the numerical example. Existing low-prime-complexity classifications for the ordinary divisor sum or for the case in which both neighbors have at most two prime factors do not imply the present claim, whose unique solution has \(\Omega(195)=3\).

## Limitations
The original infinitude problem remains open. The result does not address \(\Omega(m)\ge4\), composite even neighbors not of the form \(2p\), or an asymptotic counting law for unrestricted collisions. No claim of independent review is made.

## References
[1] L. Tóth, *A survey of the alternating sum-of-divisors function*, Acta Univ. Sapientiae Mathematica **5** (2013), 93–107; arXiv:1111.4842 (first publicly available 2011-11-21), especially formula (1) and Section 7, Problem 3. https://arxiv.org/abs/1111.4842

[2] OEIS Foundation, A206368, integers with equal alternating-divisor sums at consecutive arguments. https://oeis.org/A206368
