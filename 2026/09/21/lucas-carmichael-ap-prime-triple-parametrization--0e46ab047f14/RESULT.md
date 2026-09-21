# Lucas–Carmichael triples whose prime factors form an arithmetic progression

## Statement

A **Lucas–Carmichael number** here means a squarefree odd composite integer \(n\) such that
\[
p+1\mid n+1\qquad\text{for every prime }p\mid n.
\]

Let
\[
p<q<r,\qquad q-p=r-q=d>0
\]
be three odd primes in arithmetic progression, and put \(n=pqr\). Then \(n\) is Lucas–Carmichael if and only if there are unique integers
\[
u>v\ge1,\qquad (u,v)=1,\qquad u\not\equiv v\pmod2,\qquad w\ge1,
\]
such that
\[
\boxed{
(p,q,r)=\bigl(uw(u-v)-1,\ u^2w-1,\ uw(u+v)-1\bigr)
}
\]
and
\[
\boxed{u^2-v^2\mid 2v^2w-3.}
\]

Equivalently, for every reduced opposite-parity shape \(u:v\), all candidate triples lie on one congruence ray
\[
\boxed{w\equiv 3(2v^2)^{-1}\pmod{u^2-v^2}.}
\]
If \(u\) is odd (and hence \(v\) is even), primality additionally forces \(w\) to be even; because \(u^2-v^2\) is odd, this selects one residue class modulo \(2(u^2-v^2)\).

Thus the arithmetic-progression subproblem is completely reduced to simultaneous primality of three linear forms on one explicitly determined ray for each reduced shape.

## Proof

Write
\[
h=q+1,
\]
so that
\[
p=h-d-1,\qquad q=h-1,\qquad r=h+d-1.
\]
The three Lucas–Carmichael divisibilities can be reduced separately.

Modulo \(p+1=h-d\), one has \(p\equiv-1\), and
\[
q\equiv d-1,\qquad r\equiv2d-1.
\]
Hence
\[
p+1\mid n+1
\iff h-d\mid d(2d-3).
\]
Modulo \(q+1=h\),
\[
pr=(h-d-1)(h+d-1)\equiv1-d^2\pmod h,
\]
so
\[
q+1\mid n+1\iff h\mid d^2.
\]
Finally, modulo \(r+1=h+d\),
\[
p\equiv-2d-1,\qquad q\equiv-d-1,
\]
which gives
\[
r+1\mid n+1
\iff h+d\mid d(2d+3).
\]
Therefore
\[
\tag{1}
h-d\mid d(2d-3),\qquad h\mid d^2,\qquad h+d\mid d(2d+3)
\]
is exactly equivalent to the Lucas–Carmichael condition.

Now put
\[
g=(h,d),\qquad h=gu,\qquad d=gv,\qquad (u,v)=1.
\]
Since \(h\mid d^2\),
\[
gu\mid g^2v^2.
\]
Coprimality gives \(u\mid g\); write \(g=uw\). Then
\[
h=u^2w,\qquad d=uvw,
\]
and hence the three primes have the displayed form.

After cancelling the common factor \(uw\) in the first and third divisibilities in (1), they become
\[
u-v\mid v(2uvw-3),\qquad u+v\mid v(2uvw+3).
\]
Since \((u-v,v)=(u+v,v)=1\), these are equivalent to
\[
u-v\mid 2v^2w-3,
\qquad
u+v\mid 2v^2w-3.
\]
If \(u,v\) had the same parity, coprimality would force them both odd, so \(u-v\) and \(u+v\) would be even while \(2v^2w-3\) is odd, impossible. Thus \(u,v\) have opposite parity. Consequently \(u-v\) and \(u+v\) are coprime, and the two divisibilities combine to
\[
(u-v)(u+v)=u^2-v^2\mid2v^2w-3.
\]
This proves necessity.

Conversely, suppose \((u,v)=1\), \(u>v\), the parities are opposite, and
\[
u^2-v^2\mid2v^2w-3.
\]
Set \(h=u^2w\) and \(d=uvw\). Then \(h\mid d^2\), while the divisibility by \(u-v\) and \(u+v\) reverses the preceding argument and yields the first and third conditions in (1). If the three displayed integers are prime, they are distinct odd primes in arithmetic progression and their product is therefore Lucas–Carmichael.

Uniqueness follows directly from
\[
\frac{h}{d}=\frac{u}{v}
\]
in lowest terms; once \(u,v\) are fixed, \(w=h/u^2=d/(uv)\) is fixed.

## A fixed-shape ray and an admissibility corollary

Let
\[
D=u^2-v^2.
\]
Because \(u,v\) have opposite parity, \(D\) is odd, and because \((v,D)=1\),
\[
(2v^2,D)=1.
\]
Thus
\[
D\mid2v^2w-3
\]
selects exactly one class of \(w\pmod D\). If \(u\) is odd, primality of \(u^2w-1>2\) forces \(w\) even, which combines with the class modulo \(D\) into one class modulo \(2D\).

The resulting three linear forms are **admissible** in the prime-tuples sense. To see this, let \(M=D\) when \(u\) is even and \(M=2D\) when \(u\) is odd, and write \(w=w_0+Mt\) for the allowed class.

If an odd prime \(\ell\mid D\), then
\[
u^2\equiv v^2\pmod\ell,
\qquad
2v^2w_0\equiv3\pmod\ell.
\]
The middle form is therefore congruent to \(1/2\pmod\ell\). For either outer form, \(u\equiv v\) or \(u\equiv-v\pmod\ell\); its residue is respectively \(-1\) or \(2\), never zero. The prime \(2\) is also harmless because the selected forms are odd. If \(\ell\nmid M\), each of the three linear forms excludes at most one class of \(t\pmod\ell\); this cannot cover all classes for \(\ell\ge5\), while for \(\ell=3\) one can choose \(w\equiv0\pmod3\), making all three forms \(-1\pmod3\). Hence there is no fixed prime obstruction.

Consequently, **Dickson's conjecture for linear forms implies that every reduced opposite-parity shape \(u:v\) contains infinitely many Lucas–Carmichael triples whose prime factors are in arithmetic progression.** This conditional statement is only an application of the parametrization; no unconditional infinitude for any one fixed shape is claimed here.

## Examples and relation to known constructions

For \((u,v)=(2,1)\), one has \(D=3\) and the congruence gives \(w\equiv0\pmod3\). Writing \(w=3m\) gives
\[
(6m-1,\ 12m-1,\ 18m-1).
\]
This family is prior art: OEIS A290810 explicitly records that whenever these three numbers are prime, their product is Lucas–Carmichael. The parametrization above shows that it is the \(2:1\) shape inside a complete classification, rather than an isolated construction.

For \((u,v)=(3,2)\), \(D=5\) and \(w\equiv1\pmod5\); primality forces the even lift \(w\equiv6\pmod{10}\). Thus one obtains the ray
\[
(30t+17,\ 90t+53,\ 150t+89),
\]
whose first member is
\[
17\cdot53\cdot89=80189.
\]
Other early arithmetic-progression Lucas–Carmichael products include
\[
935=5\cdot11\cdot17,
\quad
76751=23\cdot47\cdot71,
\quad
152279=29\cdot59\cdot89,
\quad
1162349=29\cdot149\cdot269.
\]

## Verification

The standalone script `artifacts/verify_lucas_carmichael_ap.py` performs two independent bounded checks using only Python's standard library.

1. It enumerates every three-term arithmetic progression of odd primes with largest term at most 20000, tests the Lucas–Carmichael divisibilities directly, and compares them with the parametrization. Among 186647 prime progressions, 73 are Lucas–Carmichael and 73 satisfy the parametrization, with 0 mismatches.
2. For every coprime opposite-parity pair \(2\le u\le30\), \(1\le v<u\), it checks four complete periods of \(w\) against both the original three divisibilities and the single residue condition. This gives 226000 checks with 0 mismatches.

These computations are supporting evidence; the classification itself is proved above.

## Literature context and limitations

The definition and general infinitude of Lucas–Carmichael numbers are established prior art. Wright proved their infinitude in *There are infinitely many elliptic Carmichael numbers* (arXiv:1609.00231; later *Bull. London Math. Soc.* 50 (2018), 791–800). Current OEIS A006972 records the sequence and related constructions. OEIS A290810 (2017) explicitly records the \((6m-1)(12m-1)(18m-1)\) construction, and OEIS A262723 records products of three distinct primes in arithmetic progression.

A 2024 paper by Einsele and Paterson studies a fixed-discriminant Lucas–Carmichael notion and develops bounds for a three-prime subclass. Its accessible full text gives a gcd-normalization for three prime factors, but no arithmetic-progression specialization was located. Wright's accessible full text was also checked for the arithmetic-progression specialization and for the terms `three prime`, `6k`, and `Chernick`; no matching classification was found.

Exact and synonymous searches for Lucas–Carmichael numbers with prime factors in arithmetic progression, equally spaced prime factors, the divisibility \(q+1\mid d^2\), the normalized condition \(u^2-v^2\mid2v^2w-3\), and the displayed parametrization did not locate an equivalent theorem. The originality claim is therefore **to the best of our knowledge**.

Residual literature risk remains. Richard Guy's *Unsolved Problems in Number Theory*, 3rd ed. (2004), §A13, and J.-M. De Koninck's 2008 entry on 399 are cited by standard Lucas–Carmichael references but were not inspected in full here. Older recreational or sequence literature could also contain an equivalent parametrization under different notation. The known \(6m-1,12m-1,18m-1\) subfamily is explicitly excluded from the originality claim.

## References

- T. Wright, *There are infinitely many elliptic Carmichael numbers*, arXiv:1609.00231; Bull. London Math. Soc. 50 (2018), 791–800. https://arxiv.org/abs/1609.00231
- OEIS A006972, *Lucas-Carmichael numbers*. https://oeis.org/A006972
- OEIS A290810, *Numbers k such that 6k-1, 12k-1 and 18k-1 are all primes*. https://oeis.org/A290810
- OEIS A262723, *Products of three distinct primes that form an arithmetic progression*. https://oeis.org/A262723
- S. Einsele and K. Paterson, *Average case error estimates of the strong Lucas test*, Designs, Codes and Cryptography 92 (2024), 1341–1378. https://doi.org/10.1007/s10623-023-01347-w
