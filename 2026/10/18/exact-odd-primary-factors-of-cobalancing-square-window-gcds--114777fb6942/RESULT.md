# Exact odd-primary factors of cobalancing square-window gcds

## Finding
Let \(b_0=b_1=0\), \(b_{n+2}=6b_{n+1}-b_n+2\), and for each integer \(k\ge1\) put
\[
G(k)=\gcd_{n\ge0}\left(\sum_{i=1}^k b_{n+i}^2\right).
\]
For each odd prime \(p\), write \(o_p\) for the multiplicative order of \(3+2\sqrt2\) in the unit group of \((\mathbb F_p[t]/(t^2-2))\). Then the exact valuation of this positive integer is
\[
\nu_p(G(k))=\begin{cases}
1+\nu_5(k),&p=5\text{ and }6\mid k,\\
\nu_p(k),&p\ne5,\ p\mid k\text{ and }o_p\mid k,\\
0,&\text{otherwise}.
\end{cases}
\]
In particular, \(o_3=4\), \(o_5=6\), \(o_7=3\), and the prime \(5\) contributes to \(G(6)\) even though it does not divide the window length. The theorem determines **all odd-primary factors**, but not the power of \(2\) in \(G(k)\).

## Assumptions and scope
All indices are nonnegative integers. The sequence is the classical cobalancing sequence. The gcd runs over every starting index and is positive. For any odd prime, the displayed quotient ring is a finite étale algebra (a field or product of two fields), and \(3+2t\) has norm \(1\), hence is a unit. The order \(o_p\) is therefore finite. If \(p\ge11\), it is at least \(5\) and divides \(p-(2/p)\), where \((2/p)\) denotes the quadratic character; in particular \(p\nmid o_p\).

## Proof
**1. Five exponential modes.** Put \(u_n=b_n/2\). The defining recursion shows that all \(b_n\) are even, and \(u_0=u_1=0\), \(u_{n+2}=6u_{n+1}-u_n+1\). With \(\gamma=1+\sqrt2\) and \(\lambda=\gamma^2=3+2\sqrt2\), the closed expression is
\[
u_n=\frac{\gamma^{-1}\lambda^n+\gamma\lambda^{-n}}{8\sqrt2}-\frac14.
\]
Its square \(q_n=u_n^2\) is
\[
q_n=\frac{\gamma^{-2}}{128}\lambda^{2n}+\frac{\gamma^2}{128}\lambda^{-2n}
-\frac{\gamma^{-1}}{16\sqrt2}\lambda^n-\frac{\gamma}{16\sqrt2}\lambda^{-n}+\frac5{64}.
\]
The displayed expression is an identity of rational integers after conjugate terms are combined. Its characteristic polynomial is
\[
(T-1)(T^2-6T+1)(T^2-34T+1)
=T^5-41T^4+246T^3-246T^2+41T-1.
\]
Consequently the integer window-sum sequence satisfies the same fifth-order recurrence with invertible final coefficient, and its gcd over all starting indices equals the gcd of the first five windows. Since \(G(k)=4\gcd_{n\ge0}\sum_{i=1}^k q_{n+i}\), the odd-prime valuations are unchanged.

**2. The sharp residue period.** For every odd prime, the four coefficients of the nonconstant exponential modes are units in the unramified \(p\)-adic quadratic algebra (or its split analogue). The order \(o_p\ge3\). Indeed, the norms of \(\lambda^j-1\) for \(j=1,2,3,4\) have absolute values \(4,32,196,1152\): the only possible odd primes with order below five are \(3\) and \(7\), with orders \(4\) and \(3\) respectively. Direct reduction for these two gives \(q_n\bmod3=(0,0,1,1)\) and \(q_n\bmod7=(0,0,1)\), repeated; their least periods equal the corresponding orders. For every other odd prime the five eigenvalues \(\lambda^{-2},\lambda^{-1},1,\lambda,\lambda^2\) are distinct modulo \(p\). Their Vandermonde matrix is invertible, so a period \(h\) of \(q_n\bmod p\) forces \(\lambda^h=1\); conversely \(o_p\) is a period. In all cases the least period is precisely \(o_p\). In particular \(o_5=6\).

**3. Necessary divisibility.** Let \(W_n(k)=\sum_{i=1}^k q_{n+i}\). If \(p\mid G(k)\), the difference \(W_{n+1}(k)-W_n(k)=q_{n+k+1}-q_{n+1}\) vanishes modulo \(p\) for every \(n\). Thus \(k\) is a period of \(q_n\bmod p\) and \(o_p\mid k\). In this event \(\lambda^{\pm k}=1\pmod p\), and every nonconstant geometric sum vanishes modulo \(p\), since \(\lambda^e-1\) is a unit for \(e=\pm1,\pm2\) (because \(o_p\ge3\)). Therefore \(W_n(k)\equiv5k/64\pmod p\). For \(p\ne5\), the further condition \(p\mid k\) is necessary, and for \(p=5\), it is automatic.

**4. Exact valuation outside five.** Suppose \(p\ne5\), \(p\mid k\), and \(o_p\mid k\), and put \(a=\nu_p(k)\). Since \(o_p\) divides \(p-1\) or \(p+1\), it is prime to \(p\). The binomial lifting of \(\lambda^{o_p}\equiv1\pmod p\) yields \(\lambda^k-1\equiv0\pmod{p^{a+1}}\). Hence all nonconstant geometric sums over a length-\(k\) window vanish modulo \(p^{a+1}\). The constant component \(5k/64\) has valuation exactly \(a\); so every window has valuation exactly \(a\), giving \(\nu_p(G(k))=a\).

**5. The exceptional factor five.** For \(p=5\) and \(6\mid k\), one has \(\lambda^3=99+70\sqrt2\) and \(\lambda^6-1=19600+13860\sqrt2\), the latter having exact \(5\)-adic valuation one (the coefficient \(13860\) is divisible by \(5\) but not by \(25\)). Standard binomial lifting gives \(\nu_5(\lambda^k-1)=1+\nu_5(k)\). Thus every nonconstant geometric window sum and the constant term \(5k/64\) are divisible by \(5^{1+\nu_5(k)}\), proving the lower bound for the gcd. If all window sums were divisible by one more factor of five, their successive differences would force \(q_{n+k}-q_n\equiv0\pmod{5^{2+\nu_5(k)}}\) for all \(n\). Since the five eigenvalues are distinct modulo five and the coefficient of the \(\lambda^n\) mode is a five-adic unit, invertibility of their Vandermonde matrix over the integral five-adic algebra would force \(\lambda^k-1\equiv0\pmod{5^{2+\nu_5(k)}}\), contradicting its exact valuation. The lower bound is sharp. If \(6\nmid k\), the least-period test excludes five altogether. This finishes the proof.

## Verification
The included standalone `verify.py` independently calculates the first five exact integer window sums for each \(1\le k\le750\), removes the powers of two from their gcd, and compares their entire odd part against the theorem, using modular pair arithmetic in \(\mathbb F_p[\sqrt2]\) for prime factors of \(k\). All 750 cases passed. Examples: the odd parts for \(k=6,12,21,42,60,84,147\) are respectively \(5,15,7,35,75,105,49\). A finite test is not an infinite proof; the exact formulas follow from the arguments above.

## Relationship to prior work
Mbirika, Schrader, and Spilker (2023), Question 30, explicitly ask for classifications of consecutive-square-window gcds across Pell, balancing, and cobalancing families; their reported facts for the ordinary cobalancing family include divisibility by four but not its odd-prime valuations. Mbirika and Spilker (2022) treat square windows of the homogeneous generalized Fibonacci recurrence, not the affine cobalancing recurrence analyzed here. The present exact odd-primary classification provides the prime-local answer for one of the open families and is compatible with the distinct balancing/Lucas-balancing formulas. This does not establish any independent priority or exclude unindexed equivalent analyses.

## Limitations
The factor of two in \(G(k)\) is not determined here; even though \(4\mid G(k)\), no exact two-adic valuation formula is claimed. The theorem addresses the ordinary cobalancing sequence with the initial data above, and not arbitrary Pell-like initial conditions or higher powers. Novelty is assessed against the inspected sources and indexed results, not exhaustively certified.

## References
1. A. Mbirika, J. Schrader and J. Spilker, *Pell and Associated Pell Braid Sequences as GCDs of Sums of k Consecutive Pell, Balancing, and Related Numbers*, arXiv:2301.05758 (first posted 2023-01-13), Section 6.1 and Question 30. https://arxiv.org/html/2301.05758v3
2. A. Mbirika and J. Spilker, *GCD of sums of k consecutive squares of generalized Fibonacci numbers*, arXiv:2204.12626 (2022), Theorem 3.4. https://arxiv.org/html/2204.12626v2
