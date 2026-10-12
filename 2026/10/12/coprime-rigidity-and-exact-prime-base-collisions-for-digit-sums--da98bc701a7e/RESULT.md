# Coprime rigidity and exact prime-base collisions for digit sums
## Finding
For an integer base \(b\ge2\), let \(S_b(n)\) denote the sum of the base-\(b\) digits of the positive integer \(n\). If \(a,c\in\mathbb N\) satisfy
\[
\gcd(a,b)=\gcd(c,b)=1
\]
and
\[
S_b(an)=S_b(cn)\qquad\text{for every }n\ge1,
\]
then
\[
a=c.
\]

Consequently, if \(p\) is prime and \(a,c\in\mathbb N\) are arbitrary, then
\[
S_p(an)=S_p(cn)\quad\text{for every }n\ge1
\]
holds if and only if
\[
\frac{a}{p^{\nu_p(a)}}=\frac{c}{p^{\nu_p(c)}}.
\]
Equivalently,
\[
\frac ac\in p^{\mathbb Z}.
\]
Thus in every prime base the only multiplier collisions are the positional-shift symmetries obtained by multiplying by powers of the base. In every base, even composite bases, two multipliers that are both coprime to the base cannot collide.

## Assumptions and scope
All variables are positive integers unless stated otherwise. The valuation \(\nu_p(m)\) is the exponent of the prime \(p\) in \(m\). A leading block of zero base-\(b\) digits is allowed when comparing fixed-length blocks; it does not affect \(S_b\).

The theorem does not classify arbitrary collisions in composite bases when one or both multipliers share a nontrivial factor with the base. It does completely classify arbitrary collisions in prime bases.

## Proof
Assume first that \(\gcd(a,b)=\gcd(c,b)=1\) and that \(S_b(an)=S_b(cn)\) for every \(n\ge1\). Put
\[
g=\gcd(a,c),\qquad a=gq,\qquad c=gr,
\]
so that \(\gcd(q,r)=1\). We prove \(q=1\), hence \(a\mid c\); symmetry will then give \(c\mid a\).

Suppose for contradiction that \(q>1\). Since \(q\mid a\) and \(\gcd(a,b)=1\), the base \(b\) is invertible modulo both \(a\) and \(q\). Let
\[
\lambda=\operatorname{ord}_a(b),\qquad \ell=\operatorname{ord}_q(b).
\]
Because \(q\mid a\), one has \(\ell\mid\lambda\). For every sufficiently large multiple \(m\) of \(\lambda\), define
\[
n_m=\frac{b^m-1}{a}.
\]
Then \(n_m\in\mathbb N\) and
\[
a n_m=b^m-1,
\]
whose base-\(b\) expansion consists of \(m\) digits equal to \(b-1\). Hence
\[
S_b(a n_m)=(b-1)m. \tag{1}
\]

Write \(r=hq+s\) with \(h\ge0\) and \(1\le s\le q-1\); the remainder is nonzero because \(\gcd(q,r)=1\). Put
\[
B=b^\ell,\qquad A=\frac{s(B-1)}{q}.
\]
Since \(q\mid B-1\), the number \(A\) is an integer. Moreover,
\[
1\le A\le B-2. \tag{2}
\]
Write \(m=K\ell\). Then
\[
X_K:=\frac{s(b^m-1)}{q}
   =A(1+B+\cdots+B^{K-1}). \tag{3}
\]
Thus, viewed in base \(B\), the integer \(X_K\) has exactly \(K\) identical blocks equal to \(A\). Expanding each base-\(B\) block into exactly \(\ell\) base-\(b\) digits gives
\[
S_b(X_K)=K S_b(A). \tag{4}
\]

We need only a bounded-subtraction observation. Fix \(t\) with \(h<B^t\). For all sufficiently large \(K\), subtracting the fixed integer \(h\) from the base-\(B\) word \(AA\cdots A\) changes only its lowest \(t+1\) blocks: any borrow reaching block \(t\) stops there because \(A>0\). Therefore there is a constant \(C\), independent of \(K\), such that
\[
S_b(X_K-h)\le K S_b(A)+C. \tag{5}
\]
Also \(X_K-h<b^m\) for large \(K\), while
\[
c n_m=\frac{r(b^m-1)}{q}=h b^m+(X_K-h).
\]
The high base-\(b\) block and the lower \(m\) digits are disjoint, so (5) gives another constant \(C'\) with
\[
S_b(cn_m)\le K S_b(A)+C'. \tag{6}
\]

By (2), the \(\ell\)-digit base-\(b\) representation of \(A\) is not the all-\((b-1)\) word, so
\[
S_b(A)\le\ell(b-1)-1. \tag{7}
\]
Combining (6) and (7),
\[
S_b(cn_m)\le K(\ell(b-1)-1)+C'=(b-1)m-K+C'.
\]
For arbitrarily large admissible \(K\), this is strictly less than \((b-1)m\), contradicting (1) and the assumed equality of digit sums. Hence \(q=1\), so \(a\mid c\). Interchanging \(a\) and \(c\) gives \(c\mid a\), and therefore \(a=c\).

Now let the base be a prime \(p\). Write
\[
a=p^\alpha a_0,\qquad c=p^\gamma c_0,
\]
where \(p\nmid a_0c_0\). Multiplication by a power of \(p\) only appends zero digits in base \(p\), so
\[
S_p(an)=S_p(a_0n),\qquad S_p(cn)=S_p(c_0n)
\]
for every \(n\). Thus equality for all \(n\) is equivalent to equality for the coprime-to-\(p\) multipliers \(a_0,c_0\), and the first part gives \(a_0=c_0\). The converse is immediate from the same positional-shift identity. This proves the prime-base classification.

## Verification
The proof is symbolic and does not rely on finite computation. The accompanying checker performs three independent regression families: it searches coprime multiplier pairs in bases \(2\) through \(12\), verifies the prime-base classification for primes \(2,3,5,7,11\) over bounded multiplier ranges, and checks the repeated-block identity (3) over thousands of exact integer instances. Its output is stored in `VERIFY_OUTPUT.txt`.

The decisive infinite step is (7): a proper \(\ell\)-digit block has digit sum at most \(\ell(b-1)-1\), producing a linear deficit of one unit per repeated block, while subtracting the fixed integer \(h\) changes only boundedly many low blocks.

## Relationship to prior work
Pongsriiam introduced quasi-injectivity by asking whether \(f(an)=f(cn)\) for all positive \(n\) forces \(a=c\). In Question 20 of *Quasi-Injectivity of Some Arithmetic Functions*, the author asks this specifically for the decimal digit sum and then for \(S_b\) in arbitrary bases. That source does not provide a classification of digit-sum multiplier collisions.

The literal unrestricted question has the immediate positional obstruction
\[
S_b(bn)=S_b(n),
\]
so unrestricted quasi-injectivity fails in every base. The result here identifies a nontrivial rigidity statement that survives this obstruction and, for prime bases, proves that there are no others.

Noppakaew and Pongsriiam later study the different function \(H_b(n)=nS_b(n)\), proving noninjectivity examples and observing that multiplying both arguments by powers of \(b\) propagates those product-function collisions. Their statement concerns ordinary injectivity of \(H_b\), not equality of the two rays \(S_b(an)\) and \(S_b(cn)\) for every \(n\), and does not imply the theorem above.

## Limitations
No claim is made that ratios \(b^j\) are the only collisions for composite bases. The theorem proves rigidity only when both multipliers are coprime to a composite base. The prime-base case is complete because every multiplier splits uniquely into a power of the base prime times a coprime core.

The literature comparison found no statement implying this coprime-rigidity theorem or the prime-base if-and-only-if classification, but absence from the searched sources and index is not a proof that no unindexed equivalent result exists.

## References
1. P. Pongsriiam, *Quasi-Injectivity of Some Arithmetic Functions*, Journal of Integer Sequences 24 (2021), Article 21.10.1. Published November 8, 2021. Source: https://cs.uwaterloo.ca/journals/JIS/VOL24/Pongsriiam/pong23.html
2. P. Noppakaew and P. Pongsriiam, *Product of Some Polynomials and Arithmetic Functions*, Journal of Integer Sequences 26 (2023), Article 23.9.1. Source: https://cs.uwaterloo.ca/journals/JIS/VOL26/Pongsriiam/pong43.html
