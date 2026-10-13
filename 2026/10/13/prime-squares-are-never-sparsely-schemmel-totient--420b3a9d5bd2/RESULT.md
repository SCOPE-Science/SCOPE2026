# Prime squares are never sparsely Schemmel totient
## Finding
For every positive integer \(r\) and every prime \(p\), the square \(p^2\) is not a sparsely Schemmel totient number of order \(r\).

If \(p\le r\), then \(S_r(p^2)=0\), so \(p^2\) is outside the positive domain. If \(p>r\), there exists \(m>p^2\), with every prime divisor of \(m\) exceeding \(r\), such that
\[
S_r(m)\le S_r(p^2)=p(p-r).
\]
Hence \(p^2\) cannot be a strict suffix minimum of \(S_r\). This proves Conjecture 3.1 in Defant's 2014 paper.

## Assumptions and scope
For fixed positive integer \(r\), the Schemmel totient \(S_r\) is multiplicative and
\[
S_r(\ell^\alpha)=
\begin{cases}
0,&\ell\le r,\\
\ell^{\alpha-1}(\ell-r),&\ell>r
\end{cases}
\]
for prime powers. Put
\[
B_r=\{n\ge1:S_r(n)>0\}.
\]
An integer \(n\in B_r\) is sparsely Schemmel totient of order \(r\) if
\[
S_r(n)<S_r(m)
\]
for every \(m\in B_r\) with \(m>n\).

The prime-distribution input is the consecutive-prime ratio lemma proved in the source paper: for consecutive primes \(t<q\),
\[
\frac qt\le\frac75
\]
except for
\[
2\to3,\qquad3\to5,\qquad7\to11.
\]

## Proof
If \(p\le r\), then \(S_r(p^2)=0\), so \(p^2\notin B_r\). Assume \(p>r\).

For \(r=1\), if \(p=2\), take \(m=6\). Then
\[
S_1(6)=\varphi(6)=2=\varphi(4)=S_1(4).
\]
If \(p\) is odd, take \(m=2p^2\). Multiplicativity gives
\[
S_1(2p^2)=S_1(p^2).
\]

Now suppose \(r\ge2\). Let \(a\) be the least prime strictly exceeding \(r\), and set
\[
\delta=a-r.
\]
Bertrand's postulate gives \(a<2r\), so
\[
0<\delta<r.
\]

First suppose \(\delta=1\). If \(p\ne a\), then \(p>a\), and for
\[
m=ap^2>p^2
\]
we have \(S_r(a)=1\), hence
\[
S_r(m)=S_r(p^2).
\]
If \(p=a\), let \(b\) be the next prime after \(a\). Bertrand gives \(b<2a\), hence
\[
b\le2a-1=a+r.
\]
Thus \(m=ab>a^2\) and
\[
S_r(m)=(a-r)(b-r)=b-r\le a=S_r(a^2).
\]

It remains to treat \(\delta\ge2\). Put
\[
L=\frac{p^2}{a},
\]
and let \(q\) be the least prime strictly exceeding \(L\). Then \(m=aq>p^2\), and both prime factors of \(m\) exceed \(r\).

Define
\[
U=r+\frac{p(p-r)}{\delta}.
\]
It suffices to prove \(q\le U\), because then
\[
S_r(aq)=\delta(q-r)\le p(p-r)=S_r(p^2).
\]

Write \(p=a+x\), where \(x\ge0\). Direct expansion gives
\[
5\delta a\left(U-\frac75L\right)
=
\delta a(3r-2\delta)
+a(5r-4\delta)x
+(5r-2\delta)x^2.
\]
Since \(0<\delta<r\), every coefficient on the right is positive. Therefore
\[
U>\frac75L.
\tag{1}
\]

Let \(t\) be the prime immediately preceding \(q\). By minimality of \(q\), \(t\le L\). Outside the three exceptional transitions, the source lemma gives
\[
q\le\frac75t\le\frac75L<U.
\]
This proves the desired inequality in every nonexceptional case.

Because \(\delta\ge2\), one has \(a\ge5\), so \(2\to3\) and \(3\to5\) cannot occur. The transition \(7\to11\) can occur only when
\[
7\le L<11.
\]
Under \(\delta\ge2\), this forces exactly
\[
(r,p)=(3,7)\quad\text{or}\quad(r,p)=(5,7).
\]
For \((r,p)=(3,7)\), take \(m=55\):
\[
S_3(55)=(5-3)(11-3)=16<28=S_3(49).
\]
For \((r,p)=(5,7)\), take \(m=77\):
\[
S_5(77)=(7-5)(11-5)=12<14=S_5(49).
\]

All cases are exhausted. Hence
\[
p^2\notin F_r
\]
for every positive integer \(r\) and every prime \(p\).

## Verification
The attached checker independently performs three finite checks. It reproduces the finite part of the source's consecutive-prime ratio lemma below the stated cutoff and finds only
\[
2\to3,\qquad3\to5,\qquad7\to11
\]
above the \(7/5\) ratio. It then tests the proof's witness for every
\[
1\le r\le300
\]
and every prime
\[
p\le1000,
\]
checking
\[
m>p^2,\qquad S_r(m)>0,\qquad S_r(m)\le S_r(p^2).
\]
It also checks the positive-coefficient identity used in (1).

The finite computation is corroborative. The universal result follows from the proof and the published consecutive-prime ratio lemma.

## Relationship to prior work
Defant introduced the sparse Schemmel sets \(F_r\), proved several prime-power exclusion results, and then stated the universal prime-square assertion as Conjecture 3.1:
\[
p^2\notin F_r
\]
for every prime \(p\) and positive integer \(r\).

The source reports bounded computational verification but no proof. Its preceding theorem excludes a special family of prime squares and all prime cubes; those results do not imply the universal square case.

The proof here gives a uniform witness. Its main step is to multiply the least admissible prime \(a\) by a prime just above \(p^2/a\); the source's consecutive-prime ratio lemma then forces the Schemmel value below the prime-square value, with only two explicit small exceptional parameter pairs.

Targeted searches for the exact conjecture, its prime-square formulation, and equivalent sparse-Schemmel language found no later theorem proving the full claim.

## Limitations
The theorem concerns exponent \(2\) only. It does not classify all prime powers in \(F_r\) or determine complete sparse Schemmel sequences.

The proof relies on the published consecutive-prime ratio lemma. The finite replay checks the computational range used in that lemma, but the asymptotic prime-gap estimate beyond the cutoff is cited rather than reproved.

The literature comparison covered the primary full text, journal version, and targeted indexed and exact-phrase searches. An unindexed independent proof remains a residual originality risk.

## References
1. C. Defant, “On Sparsely Schemmel Totient Numbers,” arXiv:1412.3080v1, first public 9 December 2014; later *Integers* 15 (2015), A18.
2. P. Dusart, “Estimates of some functions over primes without R.H.,” arXiv:1002.0442, 2010.
