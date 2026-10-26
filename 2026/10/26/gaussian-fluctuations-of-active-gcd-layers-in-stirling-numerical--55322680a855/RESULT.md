# Gaussian fluctuations of active gcd layers in Stirling numerical semigroups

## Finding
For each integer \(n\ge4\), let \(\bigl[{n\atop k}\bigr]\) denote an unsigned Stirling number of the first kind and set
\[
a_n=\binom n2,\qquad b_{n,j}=\Bigl[{n\atop n-2j}\Bigr],\qquad
1\le j\le J_n=\Bigl\lfloor\frac{n-1}{2}\Bigr\rfloor.
\]
Put \(d_{n,0}=a_n\) and \(d_{n,j}=\gcd(a_n,b_{n,1},\ldots,b_{n,j})\). The *active-layer count* of this canonical gcd filtration is
\[
T(n)=1+\#\{1\le j\le J_n:d_{n,j}<d_{n,j-1}\}.
\]
For uniformly sampled integers \(n\in\{4,\ldots,\lfloor X\rfloor\}\), as \(X\to\infty\),
\[
\boxed{\frac{T(n)-2\log\log X}{\sqrt{2\log\log X}}\Longrightarrow N(0,1).}
\]
For every \(n\ge4\), writing \(a_n=n(n-1)/2\), the stronger quantitative comparison is
\[
\boxed{|T(n)-\omega(n(n-1))|\le2+\Omega(a_n)-\omega(a_n),}
\]
where \(\omega\) counts distinct prime factors and \(\Omega\) counts them with multiplicity. Moreover, the mean of \(\Omega(a_n)-\omega(a_n)\) over integers \(4\le n\le X\) is \(O(1)\). Consequently \(T(n)=\omega(n(n-1))+O_{\mathbb P}(1)\) for a uniformly sampled \(n\).

## Assumptions and scope
The canonical filtration is the specific sequence defined above, not an arbitrary presentation of a numerical semigroup. Its strict drops correspond to nonunit gcd quotients in the reduced telescopic representation of the Stirling semigroup, as established in Komatsu–Song [1]. No assertion is made that \(T(n)\) equals the **minimal embedding dimension**; a telescopic generating sequence need not be minimal [2]. The limiting distribution uses the uniform counting measure on integer indices, with a fixed asymptotic normal variance \(2\log\log X\).

## Proof
**1. Arithmetic sandwich.** The gcd-filtration theorem in [1] gives
\[
d_{n,j}=\frac{a_n}{\gcd(a_n,M_j)},\qquad
M_j=\tfrac12\operatorname{lcm}\{m\ge1:\varphi(m)\le2j\}.
\]
For every prime \(p\ge5\) dividing \(a_n\), an integer divisible by \(p\) has Euler totient divisible by \(p-1\). Therefore \(p\) first appears in the lcm defining \(M_j\) at the unique threshold \(j=(p-1)/2\), where \(m=p\) qualifies. Division by 2 does not change its \(p\)-adic valuation. Distinct primes \(p\ge5\) produce distinct strict gcd drops. The threshold lies in \(1\le j\le J_n\) because any prime divisor of \(a_n=n(n-1)/2\) divides either \(n\) or \(n-1\), and \(p\ge5\) cannot equal an even \(n\). Hence
\[
T(n)\ge1+\omega_{\ge5}(a_n)\ge\omega(a_n)-1.
\]
Set \(q_{n,j}=d_{n,j-1}/d_{n,j}\). These are positive integers and \(\prod_{j=1}^{J_n}q_{n,j}=a_n\), since \(d_{n,J_n}=1\) by the complete gcd-filtration theorem [1]. Every strict drop has \(q_{n,j}\ge2\). Thus
\[
T(n)\le1+\Omega(a_n).
\]
Since the squarefree prime support changes by at most one when \(n(n-1)\) is divided by two, combining these inequalities proves
\[
|T(n)-\omega(n(n-1))|\le2+\Omega(a_n)-\omega(a_n).
\]

**2. Bounded mean of repeated prime factors.** Write \(R(n)=\Omega(a_n)-\omega(a_n)\), so
\[
R(n)=\sum_p\sum_{k\ge2}{\bf1}_{p^k\mid a_n}.
\]
For odd \(p\), \(p^k\mid a_n\) means \(n\equiv0\) or \(1\pmod{p^k}\), because \(n,n-1\) are coprime. For \(p=2\), the corresponding modulus is \(2^{k+1}\). Every relevant odd prime power divides \(n\) or \(n-1\), hence is at most \(X\); the same holds for relevant powers of two after allowing the extra factor two. Among \(n\le X\), each event has probability at most \(2/p^k+O(1/X)\), with a harmless sharper bound for two. The sum \(\sum_p\sum_{k\ge2}p^{-k}\) converges. There are \(O(\sqrt X\log X)\) relevant prime-power pairs, so the total residue-count errors are \(O(\log X/\sqrt X)\). Thus
\[
\frac1{\lfloor X\rfloor-3}\sum_{n=4}^{\lfloor X\rfloor}R(n)=O(1).
\]
By Markov's inequality, \(R(n)=O_{\mathbb P}(1)\) under uniform sampling. The arithmetic sandwich yields \(T(n)-\omega(n(n-1))=O_{\mathbb P}(1)\).

**3. Gaussian limit for the two adjacent factors.** Put \(L=\log\log X\) and \(Y=X^{L^{-1/3}}\). For each odd prime \(p\le Y\), set \(I_p(n)={\bf1}_{p\mid n(n-1)}\). The two forbidden/complementary residue classes show that \(\mathbb P(I_p=1)=2/p+O(1/X)\). For any fixed number \(r\) of distinct odd primes, the Chinese remainder theorem gives the joint frequency
\[
\mathbb P(I_{p_1}=\cdots=I_{p_r}=1)
=\prod_{i=1}^{r}\frac2{p_i}+O(2^r/X).
\]
For each fixed integer moment order \(r\), expanding the moment of \(\sum_{3\le p\le Y}I_p(n)\) and using CRT shows its moments differ from those of a sum of independent Bernoulli variables with respective means \(2/p\) by at most \(O_r((1+\pi(Y))^r/X)=X^{-1+o(1)}\). This also holds for centered moments: the centering constants have polynomial size in \(L\), so multiplication preserves a negligible error.

By the classical prime harmonic sum, the independent model has mean \(2\log\log Y+O(1)=2L+O(\log L)\) and variance \(2L+O(\log L)\). It obeys the central limit theorem by boundedness and diverging variance (or the moment/cumulant method), hence so does the CRT-dependent finite-prime count by moment convergence and the moment determinacy of the Gaussian. The prime \(2\) always divides \(n(n-1)\) and contributes just one. Every prime larger than \(Y\) which divides \(n(n-1)\le X^2\) consumes more than \(\log Y\) of its logarithm, so there are at most \(2L^{1/3}=o(\sqrt L)\) such factors. Consequently
\[
\frac{\omega(n(n-1))-2L}{\sqrt{2L}}\Longrightarrow N(0,1).
\]
Finally the difference between \(T(n)\) and \(\omega(n(n-1))\) is tight by Step 2. Slutsky's theorem proves the claimed limit.

## Verification
The included standalone `verify.py` constructs Stirling rows by their recurrence and independently computes the strict-drop filtration directly by repeated integer gcd. For every \(4\le n\le100\), it checks that each prime divisor \(p\ge5\) of \(a_n\) has its stipulated distinct threshold, and checks the stated deterministic comparison. For \(4\le n\le28\), it additionally checks the candidate active generators for redundancy using exact residue shortest paths; this auxiliary finite observation is not needed for the theorem. Execution yielded `VERIFY_OK`. The proof of the infinite distribution is the CRT/moment argument above, not the finite test.

## Relationship to prior work
Komatsu–Song [1], submitted October 2, 2026, established the exact gcd filtration and a telescopic Apéry-rectangle representation, but did not state a distributional limit for the number of strict gcd drops. Here their algebraic identity is combined with prime-threshold separation, squarefull-factor moment control, and a two-linear-factor Gaussian argument. Shor [2] establishes in general that telescopic sequences need not be minimal, explaining the deliberate distinction between active-layer count and embedding dimension. Searches for a Gaussian law or normal order of this specific active-layer invariant found no explicit prior statement. Known Erdős–Kac theory for additive prime-factor counts is compatible with, but does not alone contain, the semigroup-to-prime-factor comparison established here.

## Limitations
The result is an asymptotic in the index \(n\), not an asymptotic as a generator size grows within one fixed semigroup. It does not determine the exact limiting distribution of the bounded difference \(T(n)-\omega(n(n-1))\), prove a rate of Gaussian convergence, or assert that every active generator is minimal. Earlier unindexed or unstated consequences of [1] and general number-theoretic limit theorems remain possible.

## References
[1] Takao Komatsu and Kyunghwan Song, *Telescopic Structure of Numerical Semigroups Generated by Unsigned Stirling Numbers of the First Kind*, arXiv:2610.03070v1, first submitted 2026-10-02, https://arxiv.org/abs/2610.03070.

[2] Caleb M. Shor, *On Free Numerical Semigroups and the Construction of Minimal Telescopic Sequences*, Journal of Integer Sequences 22 (2019), Article 19.2.4, https://cs.uwaterloo.ca/journals/JIS/VOL22/Shor/shor3.html.

[3] P. Erdős and M. Kac, *The Gaussian law of errors in the theory of additive number theoretic functions*, American Journal of Mathematics 62 (1940), 738–742. The needed special two-linear-factor CLT is proved directly above.
