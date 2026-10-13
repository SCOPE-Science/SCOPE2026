# Near-perfect integers with \(\Omega(n)\le4\)
## Finding
A positive integer \(n\) is called near-perfect when there is a proper divisor \(d\mid n\) such that
\[
\sigma(n)=2n+d.
\]
Let \(\Omega(n)\) count prime factors with multiplicity. The complete classification in the range \(\Omega(n)\le4\) is
\[
\{12,18,20,24,40,56,88,104,196,234,650\}.
\]
The corresponding redundant divisors \(d=\sigma(n)-2n\), in the same order, are
\[
4,3,2,12,10,8,4,2,7,78,2.
\]
In particular, the only members in this multiplicity range having three distinct prime factors are
\[
234=2\cdot3^2\cdot13,\qquad 650=2\cdot5^2\cdot13.
\]

## Assumptions and scope
Only elementary multiplicativity of \(\sigma\), positivity of the redundant divisor, and divisibility \(d\mid n\) are used. The statement is unconditional and has no numerical search bound. A near-perfect integer is necessarily abundant, so every excluded factorization shape is first tested against the exact inequality \(\sigma(n)>2n\).

## Proof
Write \(d=\sigma(n)-2n\). We require \(0<d<n\) and \(d\mid n\).

For \(\Omega(n)\le2\), no integer is abundant: a prime power with at most two prime factors counted with multiplicity has abundancy at most \(7/4\), while among squarefree products the maximum is attained at \(6\), which is perfect rather than abundant.

Now let \(\Omega(n)=3\). The exponent partitions are \(3\), \(2+1\), and \(1+1+1\). Prime cubes are deficient. For the shape \(4p\), with \(p\) odd prime,
\[
d=\sigma(4p)-8p=7-p,
\]
so positivity gives \(p\in\{3,5\}\), yielding \(12\) and \(20\). For the shape \(2p^2\),
\[
d=3(p^2+p+1)-4p^2=-p^2+3p+3,
\]
and positivity forces \(p=3\), yielding \(18\). Odd shapes are deficient. For a squarefree shape \(2pq\), if \(p=3\) then \(d=12\), which cannot divide \(6q\) for odd prime \(q\); the only remaining abundant possibility is \(2\cdot5\cdot7\), for which \(d=4\nmid70\). Hence the \(\Omega=3\) layer is exactly \(\{12,18,20\}\).

Let \(\Omega(n)=4\). Prime fourth powers are deficient. For the partition \(3+1\), the only abundant possibilities of shape \(8p\) satisfy \(p<15\), and
\[
d=15-p.
\]
For \(p=3,5,7,11,13\), this gives exactly \(24,40,56,88,104\). The opposite shape \(2p^3\) is abundant only for \(p=3\), where \(d=12\nmid54\); odd shapes are deficient.

For the partition \(2+2\), odd numbers are deficient, and for \(4p^2\)
\[
d=-p^2+7p+7.
\]
Positivity restricts \(p\) to \(3,5,7\); the divisibility test succeeds only at \(p=7\), giving \(196\) with redundant divisor \(7\).

It remains to treat the partition \(2+1+1\). An odd integer of this shape has abundancy at most
\[
\frac{13}{9}\frac65\frac87=\frac{208}{105}<2,
\]
so it is deficient. A squarefree even number has shape \(2pqr\) with odd primes \(p,q,r\). Here \(\sigma(2pqr)\) is divisible by \(8\), while \(2(2pqr)\equiv4\pmod8\). Hence
\[
\nu_2\bigl(\sigma(2pqr)-4pqr\bigr)=2,
\]
whereas \(\nu_2(2pqr)=1\); therefore its positive excess can never divide \(n\).

There are two remaining even shapes.

First take \(n=4rs\) with distinct odd primes \(r<s\). Then
\[
d=7(r+s+1)-rs.
\]
If \(r=3\), divisibility would give \(s+7\mid21\), impossible for prime \(s>3\). If \(r=5\), it gives \(s+21\mid210\), whose possible positive divisors yield no prime \(s>5\). If \(r=7\), then \(d=56\), which cannot divide \(28s\). For \(r\ge11\), positivity is equivalent to
\[
(r-7)(s-7)<56.
\]
This leaves only \((r,s)=(11,13),(11,17),(11,19)\), giving \(d=32,16,8\), respectively, none of which divides \(4rs\).

Finally take \(n=2r^2s\) with distinct odd primes \(r,s\), where \(r\) is the squared prime. If \(s=3\), then
\[
d=12(r+1),
\]
and \(d\mid6r^2\) would imply \(2(r+1)\mid r^2\), impossible because \(\gcd(r+1,r)=1\). If \(s=5\), positivity leaves only \(r=3\) or \(7\), and direct substitution gives redundant candidates \(54\) and \(46\), neither dividing the corresponding integer. If \(s\ge7\) and \(r>s\), then the abundancy is at most its value at \(2\cdot11^2\cdot7\), which is below \(2\), so this branch is deficient. We may therefore assume \(r<s\). If \(r=3\), then
\[
d=3(s+13).
\]
The divisibility condition becomes \(s+13\mid78\), and the unique prime solution is \(s=13\), giving \(234\). If \(r=5\), positivity leaves \(s\in\{7,11,13\}\); the corresponding excesses are \(44,16,2\), and only \(s=13\) works, giving \(650\). If \(r\ge7\), then \(s\ge11\), and the abundancy is at most its value at \(2\cdot7^2\cdot11\), again below \(2\). This completes the classification.

Every displayed integer is checked directly from \(d=\sigma(n)-2n\), and every listed \(d\) is a proper divisor.

## Verification
The accompanying checker independently recomputes \(\sigma(n)\), \(\Omega(n)\), and the redundant divisor for all eleven values, checks the exact branch identities used above, and performs a regression enumeration through \(10^6\). It returns

`VERIFY_OK expected=11 scan_limit=1000000 max=650`

The finite scan is not used to prove exhaustiveness; exhaustiveness comes from the symbolic factorization-shape analysis above.

## Relationship to prior work
Ren and Chen classified all near-perfect numbers having exactly two distinct prime factors. Their theorem is broader in exponent size on that two-support slice, and their paper explicitly lists \(234\) and \(650\) among early examples having three distinct prime factors, but it does not classify by total multiplicity \(\Omega\) and does not prove that these are the only three-support examples with \(\Omega\le4\). Hasanalizade later summarized the two-support classification and emphasized that classifying all even near-perfect numbers remains open. The present result cuts across support size: it gives a complete boundary by total prime-factor multiplicity and includes the two three-support cases.

A current OEIS table for near-perfect numbers contains all eleven values in the claimed list, which is a useful numerical consistency check but not an implication of the classification theorem.

## Limitations
The result stops at \(\Omega(n)=4\). It does not classify near-perfect integers with five or more prime factors counted with multiplicity, nor does it settle finiteness for a fixed number of distinct prime factors. The database and finite computation are corroborating evidence only.

## References
E. Hasanalizade, *On near-perfect numbers of special forms*, arXiv:2206.10353v1 (2022); Bulletin of the Australian Mathematical Society 108 (2023), 366--372, DOI 10.1017/S0004972723000072.

X.-Z. Ren and Y.-G. Chen, *On near-perfect numbers with two distinct prime factors*, Bulletin of the Australian Mathematical Society 88 (2013), 520--524, DOI 10.1017/S0004972713000178.

N. J. A. Sloane et al., OEIS A181595, near-perfect numbers.
