# Sharp two-step entrance minima for prime-power denominators
## Finding
Let \(T(x)=\lfloor x\rfloor(1+\{x\})\) for rational \(x\ge2\). Let \(\operatorname{ord}(x)\) be the least nonnegative integer \(j\) for which \(T^{\circ j}(x)\) is an integer, if such a \(j\) exists. For integers \(M\ge2\), define the exact-order-two entrance minimum
\[
\mu(M,2)=\min\{a\in\mathbb Z:a\ge2M,\ \gcd(a,M)=1,\ \operatorname{ord}(a/M)=2\}.
\]
**Theorem.** For every prime \(p\) and integer \(k\ge1\), put \(M=p^k\). Then
\[
\boxed{\displaystyle
\mu(p^k,2)=
\begin{cases}
7,&p=2,\ k=1,\\
Mp^s+1,&k=2s,\ s\ge1,\\
M2^{s+1}+1,&p=2,\ k=2s+1,\ s\ge1,\\
\displaystyle Mp^s\frac{p+1}{2}+\left\lceil\frac{M(p-1)}{p+1}\right\rceil,&p\ge3\text{ prime},\ k=2s+1,\ s\ge0.
\end{cases}}
\]
In particular the least integer quotient \(\lfloor \mu(p^k,2)/p^k\rfloor\) has a sharp even/odd prime-power-exponent transition. The special value \(\mu(2,2)=7\) is already implied by Carvalho's published denominator-two classification and is included to make the formula complete; its rediscovery is not claimed.

## Assumptions and scope
The minimum is over *reduced* rationals \(a/M\ge2\), and order exactly two means the first iterate is nonintegral and the second is integral. There is no assumption that every rational orbit eventually reaches an integer. The theorem classifies the minimum for prime-power denominators and precisely two iterations; it makes no claim about composite denominators with multiple distinct prime factors or orders exceeding two. The defining rational map, distinct from the older map \(x\mapsto x\lceil x\rceil\), is the one studied by Carvalho.

## Proof
Write \(a=qM+r\), with \(q\ge2\), \(1\le r<M\) and \(\gcd(r,M)=1\). A direct substitution gives
\[
T(a/M)=\frac{q(M+r)}M,
\qquad
Q:=\lfloor T(a/M)\rfloor=q+\left\lfloor\frac{qr}{M}\right\rfloor.
\]
Put \(g=\gcd(q,M)\), \(d=M/g\). Since \(\gcd(M+r,M)=1\), the first iterate has reduced denominator exactly \(d\). It is an integer exactly when \(d=1\). Otherwise, writing the first iterate in reduced form \(Q+R/d\) with \(1\le R<d\) and \(\gcd(R,d)=1\), the second iterate equals \(Q(d+R)/d\) and is integral precisely when \(d\mid Q\). Hence the exact two-step criterion is
\[
\boxed{d>1\quad\text{and}\quad d\mid Q},\qquad q\le Q\le2q-1.\tag{1}
\]
When \(M=p^k\) and \(h=\nu_p(q)<k\), this becomes \(d=p^{k-h}\). We first show the smallest possible quotient \(q\) and then minimize the coprime remainder \(r\) at that quotient.

**Even exponent.** Let \(k=2s\) with \(s\ge1\). If \(2\le q<p^s\), then \(h\le s-1\), so \(d\ge p^{s+1}\), whereas \(Q\le2q-1<2p^s\le p^{s+1}\). Thus (1) is impossible. At \(q=p^s\) and \(r=1\), we have \(d=p^s\) and \(Q=p^s\), since \(q<M\). This proves \(\mu(p^{2s},2)=p^{2s}p^s+1\).

**Odd exponent at an odd prime.** Let \(k=2s+1\), \(p\ge3\), and \(t=(p+1)/2\). Put \(q_0=p^st\). If \(q<q_0\) and \(h\le s-1\), then \(d\ge p^{s+2}\) and \(Q<2q_0=p^s(p+1)\le p^{s+2}\), so (1) fails. If \(h=s\), then \(q=p^su\) with \(u<t\), and thus \(Q\le2q-1\le p^s(p-1)-1<p^{s+1}=d\). The case \(h\ge s+1\) is impossible for \(q<q_0\), as \(p^{s+1}>q_0\). Therefore every exact-two-step numerator has \(q\ge q_0\).

At \(q=q_0\), the reduced denominator is \(d=p^{s+1}\), and \(q_0\le Q\le2q_0-1<2d\), so the only possible nonzero multiple of \(d\) is \(Q=d\). Writing \(u=(p-1)/2=t-1\), the equation \(Q=d\) is equivalent to
\[
\left\lfloor\frac{q_0r}{M}\right\rfloor=p^su,
\qquad
r\ge r_0:=\left\lceil\frac{Mu}{t}\right\rceil
=\left\lceil\frac{M(p-1)}{p+1}\right\rceil.
\]
Because \(q_0<M\), the floor at \(r=r_0\) is exactly \(p^su\), rather than a larger integer. We must also check the *required reducedness* at the smallest remainder. Since \(p\equiv-1\pmod t\), \(M=p^{2s+1}\equiv-1\pmod t\), and \(u\equiv-1\pmod t\), we have \(Mu\equiv1\pmod t\). Thus
\[
r_0=\frac{Mu+t-1}{t},
\qquad
r_0\equiv(t-1)t^{-1}\not\equiv0\pmod p.
\]
Here \(t\) is invertible modulo \(p\) and \(1\le t-1<p\). Therefore \(r_0\) is admissible and is the least remainder for the least admissible quotient, proving the odd-prime formula.

**Odd exponent at two.** Let \(k=2s+1\) with \(s\ge1\). For any \(q<2^{s+1}\), either \(h\le s-1\), in which case \(d\ge2^{s+2}>Q\), or \(h=s\), in which case necessarily \(q=2^s\) and \(d=2^{s+1}>Q\). Thus no smaller quotient works. At \(q=2^{s+1}\) and \(r=1\), the first denominator is \(d=2^s>1\) and \(Q=q\) is a multiple of \(d\), so \(\mu(2^{2s+1},2)=2^{2s+1}2^{s+1}+1\).

**Exceptional denominator two.** When \(M=2\), the reduced numerator has odd remainder \(r=1\). The first allowable quotient \(q=2\) gives an integral first iterate, while \(q=3\) gives \(T(7/2)=9/2\) and \(T(9/2)=6\). Hence \(\mu(2,2)=7\), completing the proof.

## Verification
A standalone finite checker in `verify.py` uses exact rational arithmetic to recompute the first two iterates. It exhausts all smaller coprime numerators for \(43\) prime powers \(p^k\le2200\), rejecting \(583945\) smaller candidates, and checks the formula's selected numerator for \(377\) larger prime-power parameters. The executable output is in `VERIFY.stdout`. These computations are corroboration only; every prime and exponent is covered by the proof, not by finite enumeration.

## Relationship to prior work
Carvalho [1, Lemma 2.1 and Theorem 3.1] establishes the rational transition and counts congruence classes of prescribed order, and [1, Proposition 3.3] treats denominator two; [1, Question 3.5] explicitly asks for the least numerator \(\mu(M,n)\). The present theorem determines this invariant for the first nontrivial order \(n=2\) and every prime-power denominator, with a proof based on minimizing the quotient and the coprime remainder. The class-count formulas of [1] do not, by themselves, specify this minimum. Azevedo--Carvalho--Machiavelo [2] studies a different map, \(x\mapsto x\lceil x\rceil\), and its entry-time congruences; those statements do not give the present entrance minima. Fridman and coauthors [3] introduce the prime-representing iteration without this minimization theorem.

## Limitations
The result does not settle rational-orbit termination, does not calculate \(\mu(M,n)\) for \(n\ge3\), and does not classify general composite \(M\). No claim is made of independent audit or complete exclusion of unindexed equivalent prior work. The finite checks cannot establish the universal theorem without the proof.

## References
1. A. Carvalho, *Rational dynamics of a prime-representing map*, arXiv:2605.21802v1 (first publicly posted 2026-05-20), https://arxiv.org/abs/2605.21802.
2. A. Azevedo, M. Carvalho, and A. Machiavelo, *Dynamics of a quasi-quadratic map*, arXiv:1210.0042v1 (2012), https://arxiv.org/abs/1210.0042.
3. D. Fridman, J. Garbulsky, B. Glecer, J. Grime, and M. Tron Florentin, *A Prime-Representing Constant*, arXiv:2010.15882v1 (2020), https://arxiv.org/abs/2010.15882.
