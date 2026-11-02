# Exact denominator clearing for power GCD–LCM quotients on coatom-deleted divisor lattices

## Finding
Let \(N>1\) and \(e\ge1\) be integers. Write \(\mathcal P(N)\) for the set of prime divisors of \(N\), and choose any \(P\subseteq\mathcal P(N)\). Form the *coatom-deleted divisor set*
\[
S(N,P)=\{d\in\mathbb Z_{>0}:d\mid N\}\setminus\{N/p:p\in P\}.
\]
Order \(S\) by increasing numerical value. On this set define the power GCD matrix \(G_e=(\gcd(x,y)^e)_{x,y\in S}\) and the power LCM matrix \(L_e=(\operatorname{lcm}(x,y)^e)_{x,y\in S}\). The matrix \(G_e\) is invertible over the rationals. Define \(\Lambda_e(N,P)\) to be the **least positive integer** such that \(\Lambda_e(N,P)G_e^{-1}L_e\) has all entries in \(\mathbb Z\).

**Theorem (exact denominator).** The value of \(\Lambda_e(N,P)\) equals \(1\) if \(P=\varnothing\), if \(N\) is a prime power, or if \(N=pq\) for two distinct primes and \(P=\{p,q\}\). In all remaining cases, for each \(p\in P\) define
\[
d_p=\begin{cases}p^e,&p^2\mid N,\\ p^e-1,&p^2\nmid N,\end{cases}
\qquad D=\operatorname{lcm}_{p\in P}d_p,\qquad
T=D+\sum_{p\in P}\frac{D}{d_p},
\]
and
\[
b_p=\begin{cases}D/d_p,&p^2\mid N,\\ p^eD/d_p,&p^2\nmid N.\end{cases}
\]
Then the exact least multiplier is
\[
\boxed{\Lambda_e(N,P)=\frac{T}{\gcd\bigl(T,\{b_p:p\in P\}\bigr)}.}
\]
The notation \(\gcd(T,\{b_p:p\in P\})\) means the gcd of the integer \(T\) and all the listed integers \(b_p\).

In particular, if \(N\) has at least two distinct prime divisors and precisely the coatom \(N/p\) is deleted, then
\[
\boxed{\Lambda_e(N,\{p\})=\begin{cases}p^e+1,&p^2\mid N,\\1,&p^2\nmid N.\end{cases}}
\]
Apart from the explicit squarefree-semiprime chain exception, the formula depends only on the deleted primes and whether they occur to exponent at least two in \(N\); unselected prime factors and all larger exponents are irrelevant.

## Assumptions and scope
The exponent \(e\) is an arbitrary **positive integer**. Prime powers and the two-element set \(S=\{1,pq\}\) are handled separately. The set \(S(N,P)\) is GCD-closed, but usually not factor-closed. All gcds and lcms are ordinary positive-integer operations; matrix divisibility means the left quotient \(G_e^{-1}L_e\) is integral.

## Proof
Write \(J_e(m)=\sum_{d\mid m}\mu(m/d)d^e=m^e\prod_{p\mid m}(1-p^{-e})\), the Jordan totient, and put \(J_e(1)=1\). It is a strictly positive integer. Suppose first that \(N\) has at least two distinct prime factors, and let \(R=S\setminus\{N\}\). The set \(R\) is factor-closed: a deleted maximal proper divisor \(N/p\) cannot divide any smaller proper divisor that remains. Consequently the GCD matrix \(A\) on \(R\) factors as \(A=E\operatorname{diag}(J_e(d):d\in R)E^{\mathsf T}\), where \(E_{x,d}=1\) if \(d\mid x\), and is zero otherwise. In increasing order \(E\) is unitriangular.

Let \(u=(x^e)_{x\in R}\), the column connecting \(N\) to \(R\) in \(G_e\). Since \(u=E(J_e(d))_{d\in R}\), the Schur complement of \(A\) is
\[
\Delta=N^e-u^{\mathsf T}A^{-1}u
=J_e(N)+\sum_{p\in P}J_e(N/p)>0.\tag{1}
\]
For any positive integer \(y\), put
\[
H_e(d,y)=\sum_{c\mid d}\mu(d/c)\operatorname{lcm}(c,y)^e.
\]
Multiplicative separation of the divisors gives the exact local identity
\[
H_e(d,y)=\begin{cases}
J_e(d)\bigl(y/\gcd(d,y)\bigr)^e,&v_p(y)<v_p(d)\text{ for every prime }p\mid d,\\
0,&\text{otherwise}.
\end{cases}\tag{2}
\]
For \(d=1\), the first case has an empty condition and equals \(y^e\). Indeed, for each prime \(p^a\Vert d\), the local Möbius difference is \(p^{ea}-p^{e(a-1)}\) if \(v_p(y)<a\), and zero otherwise; factors of \(y\) outside \(d\) are retained in the first case. Thus \(H_e(d,y)/J_e(d)\) is always an integer.

Let \(\ell_y=(\operatorname{lcm}(x,y)^e)_{x\in R}\). Möbius inversion on the factor-closed set \(R\) gives \(E^{-1}\ell_y=(H_e(d,y))_{d\in R}\). It follows from (2) that \(A^{-1}\ell_y=E^{-\mathsf T}(H_e(d,y)/J_e(d))_{d\in R}\) is an integral vector for **every** positive integer \(y\). Similarly \(A^{-1}u\) is integral. Applying the block inverse formula to \(G_e\), the entry of the bottom row of \(Q=G_e^{-1}L_e\) corresponding to the column indexed by \(y\in S\) is
\[
Q_{N,y}=\frac{N^e-u^{\mathsf T}A^{-1}\ell_y}{\Delta}
=\frac{H_e(N,y)+\sum_{p\in P}H_e(N/p,y)}{\Delta}.\tag{3}
\]
The other rows are \(Q_{R,y}=A^{-1}\ell_y-(A^{-1}u)Q_{N,y}\). Both displayed coefficient vectors are integral, so an integer clears **all entries** of \(Q\) if and only if it clears the bottom row in (3).

Write \(a_p=v_p(N)\). Since \(y\mid N\), (2) determines the numerator \(K_y\) in (3). If \(y\) saturates no prime exponent of \(N\) (i.e. \(v_p(y)<a_p\) for all \(p\mid N\)), then
\[
K_y=\Delta-\sum_{\substack{p\in P,\ a_p\ge2\\v_p(y)=a_p-1}}J_e(N/p).\tag{4}
\]
If exactly one prime \(p\) is saturated, then \(K_y=p^eJ_e(N/p)\) when \(p\in P\) and \(a_p=1\), and otherwise \(K_y=0\). If at least two primes are saturated, \(K_y=0\). Thus all \(K_y\) belong to the integer span of
\[
\Delta,\quad\{J_e(N/p):p\in P,\ a_p\ge2\},\quad
\{p^eJ_e(N/p):p\in P,\ a_p=1\}.\tag{5}
\]
Conversely, \(K_1=\Delta\). For each selected \(p\) with \(a_p\ge2\), the permitted column \(y=p^{a_p-1}\) has \(K_y=\Delta-J_e(N/p)\). For each selected \(p\) with \(a_p=1\), the permitted column \(y=p\) has \(K_y=p^eJ_e(N/p)\), except in the sole case where \(N=pq\) is squarefree and both its coatoms are deleted. Hence, outside that explicitly excluded case, the gcd of **all** numerators \(K_y\) equals the gcd of the integers in (5). Equation (3) proves that the least denominator-clearing integer is \(\Delta\) divided by that gcd.

Finally, by the Jordan-totient product,
\[
\frac{J_e(N)}{J_e(N/p)}=
\begin{cases}p^e,&a_p\ge2,\\ p^e-1,&a_p=1.\end{cases}
\]
Thus each \(d_p\) divides \(J_e(N)\), and with \(M=J_e(N)/D\) one has \(\Delta=MT\) and the other gcd generators in (5) equal \(Mb_p\). Cancelling \(M\) gives the boxed expression, proving both **sufficiency and minimality**.

If \(P=\varnothing\), the set is factor-closed, so formula (2) and the incidence factorization already show \(G_e^{-1}L_e\) integral. If \(N\) is a prime power, \(S\) is a divisibility chain. For any chain \(1=x_1\mid x_2\mid\cdots\mid x_k\), the successive-difference incidence factorization has diagonal increments \(x_i^e-x_{i-1}^e\); its Möbius differences of LCM columns are either zero or the corresponding increment. Hence \(G_e^{-1}L_e\) is integral. Finally, if \(N=pq\) with both coatoms deleted, then \(S=\{1,N\}\) is a chain. These exhaust the exceptions.

## Verification
The accompanying standalone standard-library Python program `verify.py` computes \(G_e^{-1}L_e\) independently using exact rational Gauss–Jordan elimination. For all tested \(2\le N<100\) with at most 18 divisors, every subset \(P\) of the distinct prime divisors and exponents \(e\in\{1,2,3\}\), it compared the least common multiple of all exact entry denominators with the displayed theorem. It also independently recomputed each applicable bottom-row entry using a divisor-sum Möbius convolution. All 1,062 matrix cases passed, including 261 nonintegral cases and 4,512 bottom-row entries. The finite checks support the proof; they are not an infinite certification.

Examples are \(\Lambda_1(12,\{2\})=3\), \(\Lambda_2(12,\{2\})=5\), \(\Lambda_1(30,\{2,3\})=5\), and \(\Lambda_1(30,\{2,3,5\})=11\).

## Relationship to prior work
Bourque–Ligh's factor-closed integrality theorem covers the case \(P=\varnothing\). Altınışık–Yıldız–Keskin (arXiv:1510.09101, posted 2015-10-29), especially its sections on GCD-closed nondivisibility and small-set classifications, motivates studying the defect when maximal proper divisors are removed; the paper does not state the least multiplier formula above. Zhao's 2013 work and Zhao–Wang–Fu's 2025 work develop **qualitative divisibility criteria**, the latter treating arbitrary GCD-closed sets and giving a general rational quotient representation. That broad 2025 theory already decides whether \(\Lambda=1\) and permits algorithmic determination of denominators. The present result does **not** claim to solve that known question anew. Its more specific contribution is the exact closed form for the **least multiplier** and the stronger prime-exponent locality statement, with no divisor enumeration or large matrix inversion.

## Limitations
This theorem treats only full divisor lattices with selected **maximal proper divisors** deleted, not arbitrary GCD-closed subsets. The positive-integer exponent restriction is necessary for the stated integrality interpretation. The new claim is quantitative, not a new general qualitative classification of divisibility. Although primary papers and searchable mathematical-result records were compared, unlocated treatments of least denominator multipliers remain a historical-priority risk. Independent mathematical audit has not been performed.

## References
- E. Altınışık, M. Yıldız, A. Keskin, *Non-divisibility of LCM Matrices by GCD Matrices on GCD-closed Sets*, 2015-10-29, arXiv:1510.09101, https://arxiv.org/abs/1510.09101.
- J. Zhao, *Divisibility of power LCM matrices by power GCD matrices on gcd-closed sets*, *Linear and Multilinear Algebra* 62 (2014), 735–748, DOI:10.1080/03081087.2013.786717.
- J. Zhao, C. Wang, Y. Fu, *Studying the divisibility of power LCM matrices by power GCD matrices on gcd-closed sets*, 2025-01-03, arXiv:2501.01794, https://arxiv.org/abs/2501.01794.
- J. Bourque and S. Ligh, *On GCD and LCM matrices*, *Linear Algebra and its Applications* 174 (1992), 65–74.
