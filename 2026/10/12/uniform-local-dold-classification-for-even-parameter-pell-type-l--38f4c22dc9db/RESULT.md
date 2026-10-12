# Uniform local Dold classification for even-parameter Pell-type Lucas sequences

## Finding
For every even integer \(P\ge2\), the first-kind Lucas sequence \(U_n=U_n(P,-1)\) has a complete local Dold classification at **every** prime, including the prime \(2\) and primes dividing its discriminant. Its local Möbius transforms are nonnegative and supported on a single rank-of-apparition tower. The exact least repair factors and prime densities are explicit. This gives a uniform Pell-type family complementary to the classical Fibonacci member studied in recent work.

**Theorem.** Define \(U_0=0\), \(U_1=1\), and \(U_{n+2}=P U_{n+1}+U_n\). For a prime \(p\), define \(A_p(n)=p^{\nu_p(U_n)}\) and \(D_p(n)=\sum_{d\mid n}\mu(n/d)A_p(d)\) for all \(n\ge1\). For odd \(p\), let \(z_p=\min\{n\ge1:p\mid U_n\}\) and \(e_p=\nu_p(U_{z_p})\). Then

\[
D_p(n)=\begin{cases}
1,&n=1,\\
p^{e_p}-1,&n=z_p,\\
p^{e_p+j-1}(p-1),&n=z_pp^j,\ j\ge1,\\
0,&\text{otherwise}.
\end{cases}
\]

For \(p=2\), writing \(s=\nu_2(P)\),

\[
D_2(n)=\begin{cases}
1,&n=1,\\
2^s-1,&n=2,\\
2^{s+j-2},&n=2^j,\ j\ge2,\\
0,&\text{otherwise}.
\end{cases}
\]

All these values are nonnegative. The least positive repair multiplier \(\operatorname{Fail}(A_p)\), characterized by \(n\mid\operatorname{Fail}(A_p)D_p(n)\) for every \(n\ge1\), is

\[
\operatorname{Fail}(A_p)=\begin{cases}
2,&p=2,\\
\dfrac{z_p}{\gcd(z_p,p-1)},&p\text{ odd}.
\end{cases}
\]

Consequently, \(A_p\) satisfies the Dold congruences if and only if it is realizable, and this occurs precisely when \(p\) is odd and \(\bigl(\frac{P^2+4}{p}\bigr)=+1\) (Legendre symbol). Every \(A_p\) is almost Dold and almost realizable. For fixed even \(P\ge2\), the four relative natural prime densities, in the order Dold, realizable, almost Dold, almost realizable, are \((1/2,1/2,1,1)\).

## Assumptions and scope
The parameter \(P\) is any even integer at least \(2\). The recurrence parameter corresponding to the usual Lucas notation is \(Q=-1\). The prime \(p\) is arbitrary, including primes dividing \(P^2+4\). All indices \(n\) are positive integers. Since every \(U_n\) for \(n\ge1\) is positive, all valuations and prime parts are defined. An integer sequence \(a(n)\) is *Dold* when \(n\mid\sum_{d\mid n}\mu(n/d)a(d)\) for every \(n\ge1\). It is *realizable* when, additionally, all these sums are nonnegative. These are the standard periodic-point realizability criteria. *Almost* means that multiplication by one fixed positive integer achieves the respective property. Relative prime density is the limit of the prime-counting proportion as the cutoff increases, when the limit exists.

## Proof
**1. Odd-prime valuation.** Put \(\Delta=P^2+4\). For an odd prime \(p\), \(p\nmid Q=-1\), so the rank \(z_p\) exists and the standard Lucas valuation formula applies: for every \(n\ge1\),

\[
\nu_p(U_n)=\begin{cases}
e_p+\nu_p(n/z_p),&z_p\mid n,\\
0,&z_p\nmid n.
\end{cases}
\tag{1}
\]

This includes the ramified case \(p\mid\Delta\), where \(z_p=p\). To see the latter rank, the characteristic polynomial has a nonzero repeated root \(P/2\) modulo \(p\), giving \(U_n\equiv n(P/2)^{n-1}\pmod p\); hence the first zero is \(p\). Formula (1) is Corollary 1.6 of Sanna (2016) specialized to \(Q=-1\): in the ramified case it reads \(\nu_p(U_n)=\nu_p(n)+\nu_p(U_p)-1\); in the unramified case the rank divides \(p-1\) or \(p+1\), and thus is prime to \(p\). In both cases this is (1).

Consequently the *entire* prime-part sequence has the divisibility-indicator expansion

\[
A_p(n)=1+(p^{e_p}-1)\mathbf1_{z_p\mid n}
+\sum_{j\ge1}p^{e_p+j-1}(p-1)\mathbf1_{z_pp^j\mid n}.
\tag{2}
\]

At any fixed \(n\) this sum is finite, and (1) proves (2) by telescoping the successive prime powers.

**2. The prime \(2\).** Let \(V_0=2\), \(V_1=P\), and \(V_{n+2}=PV_{n+1}+V_n\) be the companion recurrence. The identities \(U_{2m}=U_mV_m\) and \(V_{2m}=V_m^2-2(-1)^m\) hold by the characteristic roots. Since \(P\) is even, induction gives \(U_m\) odd whenever \(m\) is odd, \(\nu_2(V_m)=s\) for odd \(m\), and \(\nu_2(V_m)=1\) for even \(m\). For clarity, the even terms satisfy \(V_{2m}\equiv2\pmod4\); the odd terms satisfy \(V_{2m+1}\equiv P\pmod{2P}\), the latter also following from the recurrence and \(V_{2m}\) even. Thus, writing \(n=2^tm\) with \(m\) odd and \(t\ge1\), successive use of \(U_{2m}=U_mV_m\) yields

\[
\nu_2(U_n)=s+t-1=s+\nu_2(n)-1.
\tag{3}
\]

For odd \(n\), the valuation is zero. Therefore

\[
A_2(n)=1+(2^s-1)\mathbf1_{2\mid n}
+\sum_{j\ge2}2^{s+j-2}\mathbf1_{2^j\mid n}.
\tag{4}
\]

**3. Möbius inversion and positivity.** For each fixed positive integer \(m\), the Möbius transform of \(\mathbf1_{m\mid n}\) is the Kronecker delta \(\mathbf1_{n=m}\):

\[
\sum_{d\mid n}\mu(n/d)\mathbf1_{m\mid d}=\mathbf1_{n=m}.
\]

Applying this identity coefficientwise to the locally finite expansions (2) and (4) proves both displayed formulas for \(D_p(n)\), including all zero cases. Every coefficient is nonnegative, so the only obstruction to realizability is the Dold divisibility condition.

**4. Exact repair.** For odd \(p\) and \(p\nmid\Delta\), \(p\nmid z_p\). The coefficient at \(n=z_pp\) is \(p^{e_p}(p-1)\). Therefore any repair multiplier \(k\) must satisfy \(z_p\mid k(p-1)\), or equivalently \(z_p/\gcd(z_p,p-1)\mid k\). This lower bound works for every supported index because \(p-1\mid p^{e_p}-1\), while the remaining coefficients contain sufficient powers of \(p\). For \(p\mid\Delta\), \(z_p=p\), and the coefficient \(p^{e_p}-1\) at \(n=p\) forces \(p\mid k\); multiplication by \(p\) works at all higher supported indices. Thus the same formula holds even at ramified odd primes. At \(p=2\), the coefficient \(2^s-1\) at \(n=2\) is odd, so \(2\mid k\), and doubling every coefficient in (4) makes it divisible by its index. These establish the stated *least* repair factors, not merely upper bounds.

**5. Prime classification and densities.** For an odd prime \(p\nmid\Delta\), reduce the characteristic roots modulo \(p\). Their ratio \(\alpha/\beta\) has order exactly \(z_p\). If \(\bigl(\frac{\Delta}{p}\bigr)=+1\), both roots lie in \(\mathbb F_p\), hence \(z_p\mid p-1\) and the repair is \(1\). If the symbol is \(-1\), Frobenius swaps the roots, hence \(z_p\mid p+1\). The only possible common orders dividing \(p-1\) are \(1\) and \(2\). The rank cannot be \(1\) because \(U_1=1\), and rank \(2\) means \(p\mid P\), which forces \(\Delta\equiv4\pmod p\) and contradicts nonsplitting. Thus the repair is greater than \(1\). A ramified odd prime has rank \(z_p=p\) and repair \(p\), while \(p=2\) has repair \(2\). These observations prove the exact Dold/realizability criterion.

For \(P\ge2\), \(P^2<P^2+4<(P+1)^2\), so \(\Delta\) is nonsquare. Its quadratic Dirichlet character is nontrivial; the prime number theorem in arithmetic progressions, equivalently the elementary Chebotarev splitting-density statement for \(\mathbb Q(\sqrt\Delta)\), gives density \(1/2\) for odd primes with Legendre symbol \(+1\). The finitely many ramified primes and \(2\) have density zero. Since all primes have finite positive repair and nonnegative transforms, both almost-sets are the entire prime set and have density \(1\). This completes the proof.

## Verification
The accompanying independent-of-proof integer check `artifacts/verify.py` computes the recurrence exactly, recomputes the Möbius sum directly (without relying on the claimed closed form), and compares all coefficients for even \(P\in\{2,4,\dots,18\}\), all primes \(p\le53\), and all \(1\le n\le120\). It separately checks the odd-prime valuation formula, coefficient nonnegativity, and repair divisibility. Run with `python3 artifacts/verify.py` and compare the terminal result with `artifacts/verification_output.txt`. These bounded experiments are evidence for the computation, not a proof of the quantified theorem.

## Relationship to prior work
Chuysurichay, Jaidee, Panraksa and Ward (2026) analyze local Dold congruences, realizability, repair, and prime densities for the *classical Fibonacci* \(U(1,-1)\) and companion Lucas sequence; they motivate extending the analysis to more general Lucas families. The present theorem treats the natural complementary entire parity class \(U(P,-1)\) with even \(P\ge2\), including its uniform density, its exact binary obstruction, and its ramified exceptional primes. Sanna (2016), Corollary 1.6, supplies the odd-prime Lucas valuation law that is used as a cited input, not newly asserted here. Neither inspected primary text states this even-parameter Möbius transform, exact repair, and density classification. The latter is deduced from those inputs, and equivalently phrased work may exist.

## Limitations
No claim is made for odd parameters \(P\ge3\), for \(Q\ne-1\), for the companion \(V\) family, or for prime-density error terms. The classification is not asserted to be independent of all unpublished or unindexed work. Numerical verification is finite; correctness of the infinite statement rests on the stated algebraic and valuation arguments, including the published valuation theorem. Independent audit has not been performed.

## References
1. S. Chuysurichay, S. Jaidee, C. Panraksa, T. Ward, *The local Dold congruence for Fibonacci and Lucas sequences*, arXiv:2609.24544v1 (first posted September 21, 2026), https://arxiv.org/abs/2609.24544.
2. C. Sanna, *The \(p\)-adic valuation of Lucas sequences*, Fibonacci Quarterly 54 (2016), Corollary 1.6; freely accessible author-hosted PDF at https://sites.oxy.edu/lengyel/originals/papers/hivatkozo/C.%20Sanna%20-%20The%20p-adic%20valuation%20of%20Lucas%20sequences.pdf.
3. S. Jaidee, D. Moss, T. Ward, *A local study of realizability*, arXiv:2508.11054v2 (2025), https://arxiv.org/abs/2508.11054.
