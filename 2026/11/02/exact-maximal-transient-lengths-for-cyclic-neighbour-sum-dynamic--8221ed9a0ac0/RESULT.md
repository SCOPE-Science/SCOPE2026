# Exact maximal transient lengths for cyclic neighbour-sum dynamics

## Finding

For integers \(m,n\ge1\), write \(D_{m,n}\) for the endomorphism of \((\mathbb Z/m\mathbb Z)^n\) given by
\[
D_{m,n}(x_0,\ldots,x_{n-1})=(x_0+x_1,x_1+x_2,\ldots,x_{n-1}+x_0).
\]
For a vector \(v\), let \(\ell(v)\) be the least nonnegative integer \(t\) such that \(D_{m,n}^{t}(v)\) lies on a periodic orbit. Define \(L_m(n)=\max_v\ell(v)\). Put \(L_1(n)=0\).

**Theorem (exact maximal transient).** For every \(m\ge2\) and \(n\ge1\), factor \(m=\prod_{p}p^{a_p}\), and let \(d_p=\nu_p(n)\). Then
\[
L_m(n)=\max_{p\mid m} \lambda(p,a_p,n),
\]
where
\[
\lambda(p,a,n)=
\begin{cases}
 a,&p=2,\ d_p=0,\\
 2^{d_p-1}(a+1),&p=2,\ d_p\ge1,\\
 0,&p\text{ odd},\ n\text{ odd},\\
 1,&p\text{ odd},\ n\text{ even},\ d_p=0,\\
 p^{d_p}+(a-1)(p-1)p^{d_p-1},&p\text{ odd},\ n\text{ even},\ d_p\ge1.
\end{cases}
\]
Moreover, the basic vector \((0,\ldots,0,1)\) has transient length exactly \(L_m(n)\), so the bound is attained for every \(m,n\).

In particular, for every odd prime \(p\), \(a\ge1\), and even \(n\) divisible by \(p\),
\[
L_{p^a}(n)=p^{\nu_p(n)-1}\bigl(a(p-1)+1\bigr).
\]
The equality confirms the upper-bound equality conjectured by Lewis and Tefft in their 2024 manuscript and retained as a conjecture in their 2026 published article. The genuinely unresolved part of that conjecture includes odd \(p\) and \(a\ge2\); special cases for prime modulus, odd tuple length, and powers of two were already treated in the literature.

## Assumptions and scope

The sum map is the *modular cyclic neighbour-sum* map above, without absolute values or subtraction. Arithmetic is performed in the indicated finite residue ring. The period need not equal one; transient length means the number of iterates before first entering any periodic cycle. All \(m,n\) are positive integers, and \(\nu_p(n)\) is the usual prime exponent. An empty maximum is replaced by zero when \(m=1\). No hypothesis on the period or the starting vector is imposed. We use only elementary polynomial rings, the Chinese remainder theorem, and binomial congruences.

## Proof

**1. Reduction to nilpotent blocks.** Identify the module of vectors with
\[
 A_{m,n}=(\mathbb Z/m\mathbb Z)[X]/(X^n-1),
\]
where \(D_{m,n}\) acts as multiplication by \(1+X\), up to reversing the orientation of the cyclic coordinates. The basic vector is a unit monomial, which generates the full module as a module over the ring and is interchangeable with \(1\).

For any endomorphism of a finite module, the images of its iterates eventually stabilize. There is then a direct decomposition into a nilpotent component \(K\) and an invertible component \(U\): the map is nilpotent on \(K\) and a permutation on \(U\). Its maximum transient length is precisely the nilpotency index on \(K\), with value zero when \(K=0\). The cyclic basic vector attains that length: after projecting the ring element \(1\) to the direct summand \(K\), its component is the identity of the corresponding invariant ring factor, whose iterates vanish exactly when multiplication itself vanishes. The Chinese remainder theorem independently reduces \(m\) to its prime-power factors and takes the maximum of the local lengths.

Fix a prime \(p\), exponent \(a\ge1\), and write \(n=p^d u\), with \(p\nmid u\). As cyclic groups, \(C_n\cong C_{p^d}\times C_u\), with generators \(g,h\). The group ring is the tensor product of the two cyclic group rings, and the relevant operator is \(1+gh\). Modulo \(p\), the first generator \(g\) has only eigenvalue \(1\); the roots of \(h^u=1\) are distinct. Consequently the only potentially noninvertible factor is the simple \(h=-1\) factor (equivalently \(h=1\) in characteristic two). The corresponding factor exists precisely when \(p=2\) or \(n\) is even. Because \(p\nmid u\), its linear factor \(h+1\) (or \(h-1\) for \(p=2\)) is coprime modulo \(p\) to the complementary factor of \(h^u-1\); Chinese-remainder idempotents lift modulo \(p^a\). All complementary factors are invertible under \(1+gh\).

If \(p\) is odd and \(n\) is odd, no noninvertible factor exists, so the local length is zero. If \(p\) is odd, \(n\) is even, and \(d=0\), the noninvertible factor is a rank-one ring on which \(1+gh=0\); its index is one. If \(p=2\) and \(d=0\), that factor is rank one and the operator is multiplication by \(2\), of index \(a\). It remains to determine the exact index of \(1-g\) for odd \(p\), and \(1+g\) for \(p=2\), in
\[
 R_{p,a,d}=(\mathbb Z/p^a\mathbb Z)[g]/(g^{p^d}-1),\qquad d\ge1.
\]

**2. Exact index at odd primes.** Let \(p\) be odd, \(d\ge1\), \(q=p^d\), \(t=p^{d-1}\), and \(\phi=(p-1)t\). Work first in the torsion-free integral ring \(R=\mathbb Z[X]/(X^q-1)\), and put \(S=1-X\). The endpoint terms \(1-X^q\) cancel in the binomial expansion of \(S^q\), while every interior coefficient is divisible by \(p\). Hence \(S^q=pR_1\) for a unique \(R_1\in R\).

Modulo \(p\), the identity \(\nu_p\binom{p^d}{j}=d-\nu_p(j)\) for \(0<j<p^d\) gives
\[
 R_1\equiv -\sum_{i=1}^{p-1}\frac{X^{it}}{i}\pmod p.
\]
Indeed, the surviving indices are \(j=it\), and their signed binomial coefficients divided by \(p\) are congruent to \(-i^{-1}\). Set \(H(Y)=-\sum_{i=1}^{p-1}Y^i/i\) over \(\mathbb F_p\). Then \(H(1)=0\) (the inverses sum to zero), while \(H'(1)=-(p-1)=1\). Because \(X^t-1=(X-1)^t\) in characteristic \(p\), this proves that \(R_1\bmod p\) has **exact** \(S\)-adic order \(t\) in \(\mathbb F_p[S]/(S^q)\). Equivalently, \(R_1\equiv S^t U_1\pmod p\) for an element \(U_1\) with \(U_1(1)\not\equiv0\pmod p\).

For every \(a\ge1\), define \(N_a=q+(a-1)\phi\). We show by induction that \(S^{N_a}\) is divisible by \(p^a\) in \(R\), and that the quotient
\[
 R_a=S^{N_a}/p^a
\]
has exact \(S\)-adic order \(t\) modulo \(p\). The case \(a=1\) was just established. If it holds for \(a\), lift the congruence to an integral equality \(R_a=S^t U_a+pV_a\), where \(U_a(1)\) is a unit modulo \(p\). Since \(t+\phi=q\),
\[
 S^{N_a+\phi}/p^{a+1}=R_1U_a+V_aS^\phi.
\]
This identity proves integrality of the quotient at stage \(a+1\). Its reduction modulo \(p\) has exact \(S\)-adic order \(t\), because \(R_1U_a\) has order \(t\) and \(\phi>t\) for every odd prime.

To prove minimality, for \(a=1\) the polynomial \(S^{q-1}\) is nonzero in \(\mathbb F_p[S]/(S^q)\). For \(a\ge2\), note that \(N_a-1=N_{a-1}+\phi-1\), and therefore
\[
 S^{N_a-1}/p^{a-1}=R_{a-1}S^{\phi-1}.
\]
Its reduction modulo \(p\) has exact \(S\)-adic order \(t+\phi-1=q-1\), hence is nonzero. Thus \(S^{N_a-1}\notin p^aR\), proving that the nilpotency index modulo \(p^a\) is exactly
\[
 N_a=p^d+(a-1)(p-1)p^{d-1}=p^{d-1}\bigl(a(p-1)+1\bigr).
\]

**3. Exact index at the prime two.** Let \(p=2\), \(d\ge1\), \(q=2^d\), \(t=q/2\), and work in the free integral ring \(R=\mathbb Z[X]/(X^q-1)\). Set
\[
 S=1+X,\quad B=S^t,\quad J=1+X^t,\quad W=(B-J)/2.
\]
The coefficients of \(W\) are integers, since the interior binomial coefficients of \(B\) are even. We have \(J^2=2J\) in \(R\) and \(B=J+2W\). For every \(a\ge1\), expanding \(B^{a+1}\), and using \(J^r=2^{r-1}J\) for \(r\ge1\), shows that \(B^{a+1}\) is divisible by \(2^a\), with
\[
 \frac{B^{a+1}}{2^a}\equiv
 J\sum_{j=0}^{a}\binom{a+1}{j}W^j\pmod2.
\]
The displayed sum evaluates to \(1\) at \(X=1\) modulo two. Indeed, \(W(1)=2^{t-1}-1\), which is \(0\) if \(t=1\) and \(1\) if \(t\ge2\), and the sum is \((1+W)^{a+1}-W^{a+1}\). Therefore it is a unit in \(\mathbb F_2[S]/(S^q)\), while \(J\equiv S^t\pmod2\). The quotient \(B^{a+1}/2^a\) has exact \(S\)-adic order \(t\) modulo two.

The preceding power has the opposite behavior: for \(a=1\), \(S^{q-1}\not\equiv0\pmod2\); for \(a\ge2\),
\[
 \frac{S^{t(a+1)-1}}{2^{a-1}}=
 \frac{B^a}{2^{a-1}} S^{t-1}
\]
has exact \(S\)-adic order \(t+(t-1)=q-1\) modulo two, so it is nonzero. Hence the exact nilpotency index modulo \(2^a\) is \(t(a+1)=2^{d-1}(a+1)\).

**4. Completion.** Insert the local indices of parts 2 and 3 into the root-factor decomposition in part 1; combine all prime powers of \(m\) by the Chinese remainder theorem. Every maximal length is realized by the basic vector since it generates the regular cyclic module. This proves every branch, the claimed attainment, and the complete theorem. \(\square\)

## Verification

The included standalone Python program `verify.py` performs two logically separate families of checks. It computes exact nilpotency indices of \(1\pm X\) in \((\mathbb Z/p^a\mathbb Z)[X]/(X^{p^d}-1)\) for \(65\) prime-power parameter triples, and independently constructs all functional graphs for \(87\) pairs \((m,n)\) with \(m^n\le50000\), comparing the maximum first-cycle-entry depth with the formula. The program reports:

`VERIFY_OK prime_power_cases=65 whole_state_cases=87 examples=8:12:8,9:6:5,12:5:2,25:10:9,16:8:20`

These finite checks are reproducibility tests, **not** an infinite certificate. The proof of every quantifier is the algebraic argument above.

## Relationship to prior work

Lewis and Tefft, *The Maximum Length for Ducci Sequences on Z_m^n when n is Even* (arXiv:2410.18204, first public 2024-10-23; subsequently *Integers* 26 (2026), A17), proved the matching general **upper bound** for even \(n\), established prime-modulus and relatively prime cases, and expressly conjectured equality in the general prime-power upper bound. The full-text 2026 publication retains that distinction between theorem and conjecture. The new result proves that equality uniformly, including odd-prime powers with exponent at least two, and gives the complete formula for arbitrary composite moduli.

The odd-length branch \(L_m(n)=\nu_2(m)\) was already established in Lewis and Tefft, *Ducci on Z_m^n and the Maximum Length for n Odd* (arXiv:2403.05319). Their *The Period of Ducci Cycles on Z_{2^l} for Tuples of Length 2^k* (arXiv:2401.17502) and related work already treat the pure two-power case. A previous separate result gives a finer transient **distribution** modulo four; our two-adic maximum is not claimed to originate here. The new structural contribution is the exact index calculation for **odd-prime powers** and its full composition with the known cases, which resolves the explicitly posed conjectural equality.

Tefft's 2025 dissertation, *Ducci Sequences on Z_m^n*, Theorem 7 and the introduction, also retain the bound and the proposed equality. Dular's *Cycles of Sums of Integers* (arXiv:1905.01765; *Fibonacci Quarterly*, 2020) studies the related cyclic sum dynamics and raises questions about the largest preperiod. No claim is made that earlier descriptions of the map, the prime-modulus case, or the separate two-adic cases are independently novel here.

## Limitations

This result is confined to the modular **sum** map, not the absolute-difference Ducci game on ordinary integer tuples, and it determines only the maximal transient, not the full distribution of transients or cycle periods. The originality assessment compares the accessible original preprints, the 2026 final published article, the dissertation's relevant statements, related work, and indexed mathematical records; a previously unindexed equivalence remains possible. The present review is not an independent scientific audit.

## References

1. M. L. Lewis and S. M. Tefft, *The Maximum Length for Ducci Sequences on* \(\mathbb Z_m^n\) *when* \(n\) *is Even*, arXiv:2410.18204 (initial submission 2024-10-23); *Integers* **26** (2026), A17, doi:10.5281/zenodo.18304994.
2. M. L. Lewis and S. M. Tefft, *Ducci on* \(\mathbb Z_m^n\) *and the Maximum Length for* \(n\) *Odd*, arXiv:2403.05319 (initial submission 2024-03-08).
3. M. L. Lewis and S. M. Tefft, *The Period of Ducci Cycles on* \(\mathbb Z_{2^l}\) *for Tuples of Length* \(2^k\), arXiv:2401.17502 (initial submission 2024-01-30).
4. S. M. Tefft, *Ducci Sequences on* \(\mathbb Z_m^n\), Ph.D. thesis, Kent State University, May 2025, OhioLINK accession kent1744887051430765.
5. B. Dular, *Cycles of Sums of Integers*, arXiv:1905.01765 (2019); *Fibonacci Quarterly* **58** (2020), 126–139.
6. F. Breuer, *Ducci Sequences over Abelian Groups*, *Communications in Algebra* **27** (1999), 5999–6013.
