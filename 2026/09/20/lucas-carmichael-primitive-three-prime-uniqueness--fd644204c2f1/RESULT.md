# Uniqueness of the primitive three-prime Lucas-Carmichael number

## Statement

A **Lucas-Carmichael number** is a squarefree composite integer \(n\) such that
\[
p+1\mid n+1\qquad\text{for every prime }p\mid n.
\]

Let
\[
n=pqr,\qquad 2<p<q<r
\]
be a Lucas-Carmichael number with exactly three prime factors. Then
\[
\gcd(p+1,q+1,r+1)=2
\]
if and only if
\[
(p,q,r)=(5,13,31).
\]
Consequently,
\[
\boxed{n=2015}
\]
is the unique three-prime Lucas-Carmichael number whose three shifted prime factors have the minimal possible common gcd.

Equivalently, in the standard decomposition
\[
p=2ha-1,\qquad q=2hb-1,\qquad r=2hc-1
\]
with \(a,b,c\) pairwise coprime, the case \(h=1\) occurs only for
\[
(a,b,c)=(3,7,16).
\]

## Proof

Assume first that \(n=pqr\) is Lucas-Carmichael and
\[
\gcd(p+1,q+1,r+1)=2.
\]
Write
\[
p=2a-1,\qquad q=2b-1,\qquad r=2c-1,
\]
so that \(2\le a<b<c\) and \(\gcd(a,b,c)=1\).

We first show that \(a,b,c\) are pairwise coprime. If a positive integer \(d\) divides both \(a\) and \(b\), then \(2d\mid p+1\) and \(2d\mid q+1\). Since \(p+1\mid qr-1\), we have \(2d\mid qr-1\); and because \(q=2b-1\equiv-1\pmod{2d}\), reduction modulo \(2d\) gives
\[
0\equiv qr-1\equiv-r-1=-2c\pmod{2d}.
\]
Thus \(d\mid c\). Because \(\gcd(a,b,c)=1\), this forces \(d=1\). The other pairs are identical by symmetry.

Therefore
\[
\operatorname{lcm}(p+1,q+1,r+1)=\operatorname{lcm}(2a,2b,2c)=2abc.
\]
Each of \(p+1,q+1,r+1\) divides \(n+1\), so
\[
T:=\frac{n+1}{2abc}
\]
is a positive integer. Expanding \(n=(2a-1)(2b-1)(2c-1)\) gives
\[
T=4-2\left(\frac1a+\frac1b+\frac1c\right)
 +\left(\frac1{ab}+\frac1{ac}+\frac1{bc}\right).
\]
Since \(a,b,c\ge2\), the correction to 4 is strictly negative. Thus
\[
T\in\{1,2,3\}.
\]
Put \(\lambda=4-T\in\{1,2,3\}\). Multiplying by \(abc\) and solving for \(c\) yields
\[
 c\bigl(\lambda ab-2a-2b+1\bigr)=2ab-a-b. \tag{1}
\]
The right side is positive, so the factor multiplying \(c\) is positive.

### Case \(\lambda=3\)

The denominator in (1) exceeds the numerator, because
\[
(3ab-2a-2b+1)-(2ab-a-b)=(a-1)(b-1)>0.
\]
Hence \(c<1\), impossible.

### Case \(\lambda=2\)

Let
\[
D=2ab-2a-2b+1.
\]
Then
\[
bD-(2ab-a-b)=2b\bigl((a-1)b-2a+1\bigr)+a.
\]
As \(b\ge a+1\) and \(a\ge2\), the expression in parentheses is at least \(a(a-2)\ge0\). Hence \(bD>2ab-a-b\), so (1) gives \(c<b\), again impossible.

### Case \(\lambda=1\)

Now
\[
c=\frac{2ab-a-b}{ab-2a-2b+1}. \tag{2}
\]
The condition \(c>b\) is equivalent to
\[
F(a,b):=(a-2)b^2-(4a-2)b+a<0. \tag{3}
\]
For \(a\ge5\), the function \(F(a,b)\) is strictly increasing for \(b\ge a+1\), since
\[
F(a,b+1)-F(a,b)=2(a-2)b-3a>0.
\]
Moreover
\[
F(a,a+1)=a(a^2-4a-4)>0
\]
for \(a\ge5\). Hence \(a\le4\).

If \(a=2\), the denominator in (2) is \(-3\), impossible. If \(a=3\), then
\[
c=\frac{5b-3}{b-5}=5+\frac{22}{b-5}.
\]
Thus \(b-5\mid22\). Since \(b>3\), the denominator is positive, and \(c>b\) leaves only \(b-5=1\) or \(2\). The first gives \((a,b,c)=(3,6,27)\), contradicting pairwise coprimality. The second gives
\[
(a,b,c)=(3,7,16),
\]
hence
\[
(p,q,r)=(5,13,31).
\]

Finally, if \(a=4\), then
\[
c=\frac{7b-4}{2b-7}.
\]
Integrality implies \(2b-7\mid 41\), because
\[
2(7b-4)-7(2b-7)=41.
\]
Since \(b>4\), the only possible positive divisor is \(2b-7=41\), which gives \(b=24\) and \(c=4<b\), a contradiction.

This proves necessity. Conversely,
\[
2015=5\cdot13\cdot31,
\]
and
\[
6\mid2016,\qquad14\mid2016,\qquad32\mid2016,
\]
so 2015 is Lucas-Carmichael and \(\gcd(6,14,32)=2\). This proves the theorem.

## Context and comparison with prior work

Wright proved the infinitude of Lucas-Carmichael numbers. More recent structural work by Tamilvanan and Muthukrishnan proves that every three-prime Lucas-Carmichael number has a representation
\[
(2hr_1-1)(2hr_2-1)(2hr_3-1)
\]
with pairwise coprime \(r_i\), and gives polynomial bounds on the larger two factors. Einsele and Paterson also use the corresponding normalized gcd decomposition in their analysis of strong Lucas tests. The theorem above classifies the minimal common-gcd case \(h=1\) completely, rather than imposing a size cutoff.

To the best of our knowledge, the uniqueness of 2015 under
\(\gcd(p+1,q+1,r+1)=2\) has not previously been stated or proved. Exact and synonymous searches were checked against the standard sequence data and the cited three-prime structural treatments. The residual originality risk is that this elementary specialization may occur in older problem literature or in a differently indexed treatment of Lucas-Carmichael numbers.

## Verification

`artifacts/verify.py` independently enumerates all three-prime Lucas-Carmichael triples with smallest prime \(p<100\), using the known finite bound \(q<3p^2\) and direct divisor testing of \(r+1\mid pq-1\). It finds 190 such triples in that range and exactly one with shifted-factor gcd 2, namely \((5,13,31)\). This finite computation is supporting evidence only; the theorem is proved above without a cutoff.

## References

1. Thomas Wright, *There Are Infinitely Many Elliptic Carmichael Numbers*, Bull. London Math. Soc. 50 (2018), 791-800; arXiv:1609.00231. https://arxiv.org/abs/1609.00231
2. Sridhar Tamilvanan and Subramani Muthukrishnan, *A New Characterization for the Lucas-Carmichael Integers and Sums of Base-p Digits*, arXiv:2311.08012v3 (2024). https://arxiv.org/abs/2311.08012
3. Semira Einsele and Kenneth Paterson, *Average case error estimates of the strong Lucas test*, Designs, Codes and Cryptography 92 (2024), 1341-1378. https://doi.org/10.1007/s10623-023-01347-w
4. OEIS A006972, *Lucas-Carmichael numbers*. https://oeis.org/A006972
