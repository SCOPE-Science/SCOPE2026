# Exact base-and-length rigidity for affine digit reversal

## Finding

For each integer base \(b\ge4\), write the base-\(b\) digits of \(N\) from most to least significant, and let \(r_b(N)\) be their reversal as an integer. For every length \(L\ge2\), among the integers having exactly \(L\) base-\(b\) digits and a nonzero units digit, the equation
\[
r_b(N)=2N-4
\]
has exactly one solution if \(b\ge10\) and \(b\equiv1\pmod3\), and no solutions otherwise. The unique solution is
\[
N=\frac{b+5}{3}b^{L-1}-\frac{b-7}{3}.
\]
Its digits, from most to least significant, are
\[
\left(\frac{b+2}{3},\underbrace{b-1,\ldots,b-1}_{L-2\text{ digits}},\frac{2b+7}{3}\right)_b.
\]
For length two the middle block is empty.

One consequence addresses the semiprime-reversal subcase of prime \(v\)-palindromes. If \(p\) and \(q\) are odd primes and \(r_b(p)=2q\) with \(v(r_b(p))=v(p)=p\), then \(q=p-2\). The classification above shows that such a pair exists at a given base and length if and only if its unique displayed candidate \(p\) and \(p-2\) are both prime. No odd base can give such a prime \(p\). The only possible bases are even integers \(b\ge10\) with \(b\equiv4\pmod6\). For two-digit candidates, writing \(b=6k+4\), \(k\ge1\), gives precisely the twin-prime candidates
\[
(p-2,p)=(12(k+1)^2-1,\ 12(k+1)^2+1).
\]
For instance, in base \(16\), the candidates \(p=109\) (two digits) and \(p=1789\) (three digits) have \(r_{16}(p)=2(p-2)\), and each corresponding pair is prime. The former base-\(16\) example is already in the cited literature and is not claimed as new.

## Assumptions and scope

All quantifiers in the theorem range over integers \(b\ge4\), \(L\ge2\), and \(b^{L-1}\le N<b^L\) with \(b\nmid N\). Reversal uses the original \(L\) digits. The units-digit assumption ensures the reversal also has exactly \(L\) digits. A notation such as \( (a,b-1,\ldots,b-1,c)_b\) denotes an ordinary base-\(b\) expansion, not multiplication. The prime consequence treats only the special class in which a prime reverses to twice a prime; it does not classify every prime \(v\)-palindrome. The standard arithmetic function \(v\) assigns \(v(p)=p\) to primes and is additive on products of coprime prime powers, with \(v(2q)=2+q\) for odd primes \(q\).

## Proof

Write \(N=\sum_{i=0}^{L-1}a_i b^i\) with \(a_0,a_{L-1}\in\{1,\ldots,b-1\}\) and the other digits in \(\{0,\ldots,b-1\}\). Computing \(2N-4\) by digitwise multiplication and subtraction, the asserted reversal equality is equivalent to the existence of integer carries \(c_0,\ldots,c_L\) satisfying
\[
c_0=-4,\qquad c_L=0,\qquad 2a_i+c_i=a_{L-1-i}+bc_{i+1}\quad(0\le i<L).
\]
Indeed, summing these equations multiplied by \(b^i\) telescopes to \(2N-4=r_b(N)\), while the standard unique quotient/remainder algorithm supplies their necessity. For \(i\ge1\), every carry belongs to \(\{-1,0,1\}\); once a nonnegative carry occurs, all later carries are in \(\{0,1\}\).

Set \(t=a_0\) and \(s=a_{L-1}\). The first and final equations give
\[
s=2t-4-bc_1,\qquad t=2s+c_{L-1},\qquad
3s=4+bc_1-2c_{L-1}.
\]
If \(c_1=-1\), then \(2t-4<0\), forcing \(t=1\) and \(s=b-2\). But the last equation forces \(1=2(b-2)+c_{L-1}\ge2b-5>1\) for \(b\ge4\), a contradiction. Thus \(c_1\in\{0,1\}\), and all later carries are in \(\{0,1\}\). If \(c_1=0\), then \(3s=4-2c_{L-1}\in\{2,4\}\), impossible. Therefore \(c_1=1\).

Suppose \(c_{L-1}=0\). The case \(L=2\) is immediately impossible because \(c_{L-1}=c_1\). Otherwise \(b+4=3s\), so \(b\equiv2\pmod3\). Put \(u=a_1\), \(z=a_{L-2}\); equations at these positions yield
\[
z=2u+1-bc_2,\qquad u=2z+c_{L-2},\qquad
3u=2bc_2-2-c_{L-2}.
\]
If \(c_2=0\), the last right-hand side is negative. If \(c_2=1\), it is congruent to \(2-c_{L-2}\in\{1,2\}\pmod3\), also impossible. Hence \(c_{L-1}=1\).

Consequently \(3s=b+2\) and \(t=2s+1=(2b+7)/3\). Integrality gives \(b\equiv1\pmod3\). The digit bound \(t\le b-1\) requires \(b\ge10\). Conversely, for such bases these endpoint digits are legal and the endpoint carries are \(c_1=c_{L-1}=1\).

To fix all intervening digits, induct inwards from both ends. Suppose the already determined outward carries at mirrored positions are \(c_i=c_{L-i}=1\). For \(1\le i< L-1-i\), write \(u=a_i\), \(z=a_{L-1-i}\), \(x=c_{i+1}\), and \(y=c_{L-1-i}\). The two carry equations give
\[
z=2u+1-bx,\quad u=2z+y-b,
\quad 3u=b(2x+1)-2-y.
\]
Here \(x,y\in\{0,1\}\). Since \(b\equiv1\pmod3\), integrality of \(u\) forces \(2x-1-y\equiv0\pmod3\), which among these four possibilities holds only for \(x=y=1\). Thus \(u=z=b-1\) and the two inward carries are again one. If a single central digit remains, its equation is \(2u+1=u+b\), hence \(u=b-1\). This proves every digit and uniqueness, including the empty middle block when \(L=2\).

For existence, put \(s=(b+2)/3\), \(t=(2b+7)/3\), and \(B=b^{L-1}\). The prescribed digits represent \(N=(s+1)B-b+t\), whereas their reversal represents \(r_b(N)=(t+1)B-b+s\). Since \(t=2s+1\) and \(b+s-2t+4=0\), direct subtraction yields \(r_b(N)=2N-4\).

For the prime consequence, \(v(p)=p\) and \(v(2q)=2+q\), so equality implies \(q=p-2\). For odd \(b=6k+1\) the endpoint digits \(s=2k+1\), \(t=4k+3\) are both odd and middle digits \(b-1\) even. As \(b\) is odd, their digit sum, and hence \(N\), is even and greater than two; such \(N\) cannot be prime. For even \(b=6k+4\) with \(k\ge1\), the length-two formula becomes \(N=12(k+1)^2+1\), completing the asserted reduction. This proves only equivalence to primality conditions, not existence at every eligible base or infinitely many such primes.

## Verification

The accompanying standalone `verify.py` reverses integers through independent base-digit extraction. It exhaustively searches every positive integer of each length \(2\le L\le5\) in every base \(4\le b\le14\), restricting to nonzero units digit. Each of its \(44\) domains agrees exactly with the symbolic classification. It also checks \(1980\) constructed identities in larger admissible bases and lengths, including \(L=12\), and verifies prime examples by exact trial division. These tests corroborate the formulas but do not replace the all-length proof above. Run `python3 verify.py` from the package directory; the expected terminal prefix is `VERIFIED`.

## Relationship to prior work

Boran, Choi, Miller, Purice and Tsai, *A characterization of prime v-palindromes* (first posted July 3, 2023), classify prime decimal \(v\)-palindromes and derive the decimal reversal equation \(r_{10}(p)=2(p-2)\) as a necessary condition. That paper proves the decimal all-nines pattern, which this theorem includes as its base-ten specialization. It does not give the simultaneous arbitrary-base, all-length classification or the obstruction for odd bases.

Bispels, Boran, Miller, Sosis and Tsai, *v-Palindromes: An Analogy to the Palindromes* (first posted April 24, 2024), introduce a systematic general-base framework, give the existing base-sixteen prime example \(109\), and ask in their Problem 1 which bases admit prime \(v\)-palindromes. The present theorem addresses the natural subclass with a reversal of the form \(2q\) for prime \(q\), not their complete problem. Earlier reversal-multiple literature such as Sutcliffe's \(r_b(N)=kN\) studies a different, zero-offset equation and does not directly imply the affine classification. An independent publication-priority claim is not made.

## Limitations

The theorem does not cover bases two or three, one-digit inputs, or inputs divisible by the base. It neither classifies general prime \(v\)-palindromes whose reversals have other factorizations, nor establishes infinitely many twin-prime candidates of the displayed special form. Related earlier literature or unindexed affine-palintiple results could weaken originality; no independent review has been performed.

## References

1. M. Boran, G. Choi, S. J. Miller, J. Purice, and D. Tsai, *A characterization of prime v-palindromes*, arXiv:2307.00770v1, first public July 3, 2023, https://arxiv.org/html/2307.00770v1 .
2. C. Bispels, M. Boran, S. J. Miller, E. Sosis, and D. Tsai, *v-Palindromes: An Analogy to the Palindromes*, arXiv:2405.05267, first public April 24, 2024, https://arxiv.org/abs/2405.05267 .
3. A. Sutcliffe, *Integers that are multiplied when their digits are reversed* (1966), discussed in the related-work sections of both cited preprints.
