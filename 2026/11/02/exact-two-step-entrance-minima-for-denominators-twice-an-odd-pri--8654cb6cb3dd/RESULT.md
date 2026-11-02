# Exact two-step entrance minima for denominators twice an odd prime
## Finding
Consider the rational iteration \(T(x)=\lfloor x\rfloor(1+\{x\})\), where \(\{x\}=x-\lfloor x\rfloor\). For every integer \(M\ge2\), let \(\mu(M,2)\) be the least positive integer \(a\ge2M\) with \(\gcd(a,M)=1\) such that \(T(a/M)\) is nonintegral and \(T^{\circ2}(a/M)\) is integral. For every odd prime \(p\), the exact value is
\[
\boxed{\mu(2p,2)=\begin{cases}
17,&p=3,\\
p^2+3p-3,&p\equiv3\pmod4,\ p\ge7,\\
p^2+5p-7,&p=5,\\
p^2+5p-9,&p\in\{13,17,29\},\\
p^2+5p-11,&p\equiv1\pmod4,\ p\ge37.
\end{cases}}
\]
Moreover every minimal numerator has integer quotient \(q_0=2\lceil(p+1)/4\rceil\) on division by \(2p\). The five exceptional small primes \(3,5,13,17,29\) arise from the integer rounding and coprimality at the first admissible quotient.
## Assumptions and scope
Here \(p\) ranges over all odd primes, \(M=2p\), and \(a/M\) is in lowest terms with \(a/M\ge2\). An exact order of two means the first iterate is not integer, and the next is; it does not mean period two. The theorem addresses the first squarefree two-prime denominator family, not denominators with higher prime powers or orders above two.
## Proof
Write \(a=qM+r\), where \(q\ge2\), \(1\le r<M\), and \(\gcd(r,M)=1\). Since \(\gcd(M+r,M)=1\), the first iterate \(q(M+r)/M\) has reduced denominator \(d=M/\gcd(q,M)\). Its integer part is \(Q=q+\lfloor qr/M\rfloor\). Repeating the map shows that the second iterate is integral exactly when \(d\mid Q\). Thus the exact-two criterion is \(d>1\) and \(d\mid q+\lfloor qr/M\rfloor\).

Put \(q_0=2\lceil(p+1)/4\rceil\). This is the least even integer not smaller than \((p+1)/2\). If \(2\le q<q_0\), then \(Q\le2q-1\). When \(q\) is even, necessarily \(q<p\), so \(d=p\) and \(Q<p\), impossible. When \(q\) is odd, \(q<p\) and \(d=2p>Q\), also impossible. At \(q=q_0\), we have \(\gcd(q_0,2p)=2\), hence \(d=p\) and \(q_0\le Q\le2q_0-1<2p\), so the exact-two criterion is simply \(Q=p\). Equivalently the reduced remainder must obey
\[
\left\lceil\frac{2p(p-q_0)}{q_0}\right\rceil\le r<\frac{2p(p+1-q_0)}{q_0},\qquad 1\le r<2p,\qquad\gcd(r,2p)=1.
\]

If \(p\equiv3\pmod4\), then \(q_0=(p+1)/2\). The lower real threshold equals \(2p-4+4/(p+1)\). For \(p\ge7\), its least admissible odd remainder is \(2p-3\), and the upper endpoint is exactly \(2p\). At \(p=3\), the smallest odd integer above the lower threshold is \(3\), which is divisible by \(p\), so the least coprime remainder is \(5\). These give \(\mu(2p,2)=2pq_0+r=p^2+3p-3\) for the former and \(17\) for the latter.

If \(p\equiv1\pmod4\), then \(q_0=(p+3)/2\). The lower real threshold is \(2p-12+36/(p+3)\), while the upper endpoint is \(2p-8+24/(p+3)\). For all primes \(p\ge37\) in this congruence class, the first eligible odd remainder is \(r=2p-11\); it lies strictly below the upper endpoint and is coprime to \(2p\). The only smaller primes in the class are \(5,13,17,29\): direct substitution into the exact displayed interval gives the least eligible remainders \(3,17,25,49\), respectively. The corresponding numerators are \(43\), \(225\), \(365\), and \(977\). Since all smaller quotients are impossible, the displayed minima are globally minimal, proving every case.
## Verification
The accompanying `verify.py` reproduces two independent arithmetic routes. It checks the quotient/remainder divisibility criterion for every odd prime below \(500\), and for each odd prime below \(110\) exhausts every smaller reduced numerator using exact `fractions.Fraction` iteration. No floating-point arithmetic is used. This finite corroboration is not needed for the infinite proof.
## Relationship to prior work
Carvalho [1, Question 3.5] asks for the least numerator at a given exact entrance order in this map, after establishing order-class counts. A previously reported exact theorem for prime-power denominators addresses a different family; the present classification handles the first denominator family having two distinct primes, \(2p\), and has its own mod-four and small-prime branches. Azevedo--Carvalho--Machiavelo [2] treat a different rational map, \(x\mapsto x\lceil x\rceil\). Their results are not transferred here. The equivalence between an exact-two entrance and a reduced-denominator divisibility condition is elementary and should not itself be regarded as a new result.
## Limitations
This determines only the exact order-two minimum for denominators \(2p\). It does not classify mixed prime powers, arbitrary squarefree denominators, or higher entrance orders. Earlier implicit derivations of these small closed forms remain a priority risk; published database indexing and literature searches are not exhaustive. Computer checks are finite and independent audit has not been performed.
## References
1. André Carvalho, *Rational dynamics of a prime-representing map*, arXiv:2605.21802v1 (first public 2026-05-20), especially Section 3 and Question 3.5, https://arxiv.org/abs/2605.21802.
2. Assis Azevedo, Maria Carvalho and António Machiavelo, *Dynamics of a quasi-quadratic map*, arXiv:1210.0042v1 (2012), https://arxiv.org/abs/1210.0042.
