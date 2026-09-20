# Two-prime rigidity for the multiplier-four iterate of the unitary divisor sum

Let \(\sigma^*(n)\) denote the sum of the unitary divisors of \(n\). For a prime-power factorization
\[
n=\prod_i p_i^{\alpha_i},
\qquad
\sigma^*(n)=\prod_i (p_i^{\alpha_i}+1).
\]

Sitaramaiah and Subbarao (1998) studied the equation
\[
\sigma^*(\sigma^*(n))=2n
\]
and, in an appendix, tabulated all \(n\le 10^8\) satisfying
\[
\sigma^*(\sigma^*(n))=kn.
\]
For \(k=4\) their table contains only \(n=18\). The following gives an infinite-range structural theorem for the natural two-prime-power slice and a complete classification when the odd prime has exponent \(2\).

## Theorem 1: odd-prime rigidity

Let \(a,b\ge 1\) and let \(p\) be an odd prime. If
\[
\sigma^*(\sigma^*(2^a p^b))=4\cdot 2^a p^b,
\]
then
\[
\boxed{p=3\quad\text{and}\quad b\ \text{is even}.}
\]

### Proof

Put
\[
N=2^a p^b,\qquad M=\sigma^*(N)=(2^a+1)(p^b+1).
\]
Since \(2^a+1\) is odd, if
\[
s=v_2(M),
\]
then
\[
s=v_2(p^b+1).
\]
Write \(M=2^sR\) with \(R\) odd. By multiplicativity of \(\sigma^*\) on coprime arguments,
\[
\sigma^*(M)=(2^s+1)\sigma^*(R).
\]
The assumed equation therefore implies
\[
2^s+1\mid 2^{a+2}p^b.
\]
The left side is odd and greater than \(1\), so for some \(1\le c\le b\),
\[
2^s+1=p^c. \tag{1}
\]

If \(b\) is even, then \(p^b\equiv1\pmod 8\), hence \(s=1\). Equation (1) becomes
\[
3=p^c,
\]
so \(p=3\) and \(c=1\).

It remains to exclude odd \(b\). For odd \(b\),
\[
s=v_2(p^b+1)=v_2(p+1).
\]
If \(c=1\), then \(p=2^s+1\). For \(s=1\) this gives \(p=3\), but \(v_2(p+1)=2\ne1\); for \(s\ge2\),
\[
v_2(p+1)=v_2(2^s+2)=1\ne s.
\]
Thus \(c\ge2\). Equation (1) then forces \(s\ge2\). Since
\[
p\equiv-1\pmod{2^s}
\]
while \(p^c\equiv1\pmod{2^s}\), the exponent \(c\) must be even. Set
\[
x=p^{c/2}.
\]
Then
\[
(x-1)(x+1)=p^c-1=2^s.
\]
The two factors on the left are consecutive even integers and have gcd \(2\). Since their product is a power of \(2\), both are powers of \(2\), and their difference is \(2\). Hence
\[
x-1=2,\qquad x+1=4,
\]
so \(x=3\), \(p=3\), \(c=2\), and \(s=3\). But then
\[
s=v_2(p+1)=v_2(4)=2,
\]
a contradiction. Therefore \(b\) cannot be odd. This proves the theorem. \(\square\)

## Theorem 2: complete square-exponent slice

Let \(a\ge1\) and let \(p\) be an odd prime. Then
\[
\boxed{\sigma^*(\sigma^*(2^a p^2))=4\cdot2^a p^2
\iff (a,p)=(1,3).}
\]
Equivalently,
\[
\boxed{18\text{ is the unique solution of the form }2^a p^2.}
\]

### Proof

By Theorem 1, any solution has \(p=3\). Thus
\[
N=2^a3^2
\]
and
\[
\sigma^*(N)=10(2^a+1).
\]

First suppose \(5\nmid 2^a+1\). Then \(10\) and \(2^a+1\) are coprime, so
\[
\sigma^*(\sigma^*(N))
=\sigma^*(10)\sigma^*(2^a+1)
=18\,\sigma^*(2^a+1).
\]
The multiplier-four equation is therefore equivalent to
\[
\sigma^*(2^a+1)=2^{a+1}. \tag{2}
\]

We show that (2) forces \(a=1\). Factor
\[
2^a+1=\prod_{i=1}^r q_i^{e_i}.
\]
Because the product
\[
\prod_i(q_i^{e_i}+1)
\]
is a power of \(2\), every factor \(q_i^{e_i}+1\) is a power of \(2\). This forces \(e_i=1\): if \(e_i\) is even, then \(q_i^{e_i}+1\equiv2\pmod8\) and is greater than \(2\); if \(e_i>1\) is odd, then \((q_i^{e_i}+1)/(q_i+1)\) is an odd integer greater than \(1\). Consequently
\[
q_i+1=2^{d_i},\qquad q_i=2^{d_i}-1,
\]
with distinct integers \(d_i\ge2\). Equation (2) gives
\[
\sum_i d_i=a+1. \tag{3}
\]

If \(r\ge2\), let \(d=\min_i d_i\). Since the \(d_i\) are distinct, (3) gives \(a\ge d+1\). Reducing
\[
2^a+1=\prod_i(2^{d_i}-1)
\]
modulo \(2^d\) shows that \(r\) is even. Reducing modulo \(2^{d+1}\), the unique factor with exponent \(d\) is \(2^d-1\), while all other factors are \(-1\). Hence the right side is
\[
1-2^d\pmod{2^{d+1}},
\]
whereas the left side is \(1\pmod{2^{d+1}}\), a contradiction. Thus \(r=1\). Then (3) gives \(d_1=a+1\), and
\[
2^a+1=2^{a+1}-1,
\]
so \(a=1\).

Now suppose \(5\mid2^a+1\). Write
\[
2^a+1=5^c h,\qquad c\ge1,\qquad (h,5)=1.
\]
Then
\[
\sigma^*(N)=2\cdot5^{c+1}h,
\]
with the three factors pairwise coprime. Therefore
\[
\sigma^*(\sigma^*(N))
=3(5^{c+1}+1)\sigma^*(h).
\]
If this equals \(36\cdot2^a\), then \(5^{c+1}+1\) can have no prime divisor other than \(2\) or \(3\).

Set \(m=c+1\ge2\). If \(m\) is even, then
\[
5^m+1\equiv2\pmod8,\qquad
5^m+1\equiv2\pmod3.
\]
Thus its \(2\)-adic valuation is exactly \(1\), it is not divisible by \(3\), and it cannot be \(2\)-\(3\)-smooth because it is greater than \(2\).

If \(m\) is odd, then \(m\ge3\),
\[
v_2(5^m+1)=1,
\qquad
v_3(5^m+1)=1+v_3(m)
\]
by LTE. If no other prime divided \(5^m+1\), then
\[
5^m+1=2\cdot3^{1+v_3(m)}
\le 6m,
\]
which is impossible for \(m\ge3\). Hence the case \(5\mid2^a+1\) cannot occur.

Therefore \(a=1\). Directly,
\[
\sigma^*(18)=30,\qquad \sigma^*(30)=72=4\cdot18,
\]
so \(18\) indeed is a solution. \(\square\)

## Computational check

The accompanying exact-integer script evaluates the definition directly for
\[
1\le a\le16,\qquad 3\le p<500\text{ prime},\qquad 1\le b\le7.
\]
Among 10,528 tested triples, the only solution is
\[
(a,p,b,n)=(1,3,2,18).
\]
This bounded computation supports the proof but is not used in it.

## Literature context and originality

Sitaramaiah and Subbarao's 1998 paper is the primary starting point. Its main results concern the multiplier \(2\) equation, while its appendix records bounded data for general multipliers; for \(k=4\) it lists \(18\) as the sole example below \(10^8\). Guy's *Unsolved Problems in Number Theory* later repeats that \(k=4\) datum. Current OEIS A038843 tracks the multiplier \(2\) unitary-superperfect sequence, and recent literature located under “unitary superperfect” continues to cite the 1998 work in that multiplier-\(2\) setting.

Searches were made for exact and synonymous formulations involving
\(\sigma^*(\sigma^*(n))=4n\), “unitary superperfect” with multiplier \(4\), “(2,4)-unitary perfect”, two-prime-factor forms, and the slices \(2^a p^b\) and \(2^a p^2\). No located source states Theorem 1 or Theorem 2, or a stronger result that implies them. The originality claim is therefore **to the best of our knowledge**.

## Limitations

Theorem 1 does not finish the full two-prime-support classification: after the reduction, possible solutions with \(b\ge4\) even lie in the family
\[
2^a3^b.
\]
Theorem 2 closes only the first even-exponent slice \(b=2\). No claim is made about solutions with three or more distinct prime factors, nor about a global classification of \(\sigma^*(\sigma^*(n))=4n\).

The finite verification is not a substitute for the proofs and is not formal proof-assistant verification.

## References

1. V. Sitaramaiah and M. V. Subbarao, *On the equation \(\sigma^*(\sigma^*(n))=2n\)*, Utilitas Mathematica **53** (1998), 101–124.  
   https://www.math.ualberta.ca/~subbarao/documents/Sitaramaiah_Subbarao1998.pdf
2. R. K. Guy, *Unsolved Problems in Number Theory*, 3rd ed., Springer, 2004, §B.  
   https://doi.org/10.1007/978-0-387-26677-0
3. OEIS A038843, “Unitary superperfect numbers.”  
   https://oeis.org/A038843
4. H. Chehade, D. Miari, and Y. Alkhezi, *Bi-Unitary Superperfect Polynomials over \(\mathbb F_2\) with at Most Two Irreducible Factors*, Symmetry **15** (2023), 2134. Its introduction summarizes the integer unitary-superperfect literature and cites Sitaramaiah–Subbarao.  
   https://doi.org/10.3390/sym15122134
