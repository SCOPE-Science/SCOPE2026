# The complete constructible-totient slice of the unit commutator equation
## Finding
Let \(\varphi(n)\) be Euler's totient, \(\sigma(n)\) the sum of positive divisors, and
\[
T(n)=\varphi(\sigma(n))-\sigma(\varphi(n)).
\]
For every integer \(n>1\) such that \(\varphi(n)\) is a power of \(2\), one has
\[
T(n)=1
\]
if and only if
\[
n\in\{2,6,8,24,128,384,32768,98304,2147483648,6442450944\}.
\tag{1}
\]

Equivalently, the full intersection of OEIS A116083 with the Gauss–Wantzel class of constructible regular polygons is exactly its ten previously known members. Every hypothetical additional member of A116083 must have an odd prime dividing \(\varphi(n)\).

## Assumptions and scope
A positive integer is called **totient-dyadic** if \(\varphi(n)=2^k\) for some integer \(k\ge0\). By the Gauss–Wantzel classification, these are precisely the indices of constructible regular polygons, allowing the conventional degenerate indices \(1,2\). In prime-factor notation, a totient-dyadic integer has the form
\[
n=2^a\prod_{q\in S}q,
\]
where \(a\ge0\), \(S\) is a finite set of **distinct Fermat primes**, and each Fermat prime is of the form
\[
F_j=2^{2^j}+1.
\]
The theorem is unconditional: it does not assume that the known five Fermat primes are the only Fermat primes. It is about the totient-dyadic stratum only and does not resolve the full conjecture that A116083 has no further terms.

## Proof
**Step 1: The totient-dyadic obstruction.** Suppose \(\varphi(n)=2^k\) and \(T(n)=1\). Then
\[
\sigma(\varphi(n))=2^{k+1}-1,
\]
so
\[
\varphi(\sigma(n))=2^{k+1}.
\tag{2}
\]
In particular, the totient of the integer \(\sigma(n)\) must itself be a power of \(2\). If \(d\mid\sigma(n)\), then \(\varphi(d)\mid\varphi(\sigma(n))\), as follows directly by comparing prime-power factorizations.

**Step 2: Fermat prime factors at least \(17\) cannot occur.** Let \(q=F_j\) be a Fermat prime with \(j\ge2\). Put \(t=2^j-1\), so \(t\) is odd and at least \(3\), and
\[
q+1=2(2^t+1).
\]
We claim that \(\varphi(2^t+1)\) is not a power of \(2\). Otherwise every prime divisor of \(2^t+1\) would be a Fermat prime and would occur with exponent one. A Fermat prime \(F_i\) with \(i\ge1\) has multiplicative order \(2^{i+1}\) for base \(2\); it therefore cannot divide \(2^t+1\), since \(t\) is odd and its order would need to divide \(2t\). Thus the only possible prime divisor would be \(F_0=3\). The squarefreeness just established would then force \(2^t+1=3\), impossible for \(t\ge3\). The claim follows.

Because a Fermat prime appears to the first power in \(n\), its divisor sum contributes the factor \(q+1\) to \(\sigma(n)\). Then \(\varphi(q+1)\mid\varphi(\sigma(n))\), contrary to (2). Therefore no Fermat prime factor of \(n\) is at least \(17\).

Every candidate is consequently
\[
n=2^a3^\varepsilon5^\delta,
\quad a\ge0,
\quad \varepsilon,\delta\in\{0,1\}.
\tag{3}
\]

**Step 3: Odd candidates.** For \(a=0\), the integers \(n>1\) in (3) are \(3,5,15\). Their differences are
\[
T(3)=-1,\qquad T(5)=-5,\qquad T(15)=-7.
\]
So \(a\ge1\) in every solution.

**Step 4: The factors \(5\) and \(15\).** Put
\[
M=2^{a+1}-1
\qquad(a\ge1).
\]
For \(n=5\cdot2^a\), multiplicativity gives
\[
\sigma(n)=6M,\qquad \varphi(n)=2^{a+1},
\]
so (2) requires \(\varphi(6M)=2^{a+2}=2(M+1)\). But \(6M\) is divisible by \(2\) and \(3\), whence
\[
\varphi(6M)\le(6M)\left(1-\frac12\right)\left(1-\frac13\right)
=2M<2(M+1),
\]
a contradiction.

For \(n=15\cdot2^a\), one has
\[
\sigma(n)=24M,\qquad \varphi(n)=2^{a+2},
\]
so (2) requires
\[
\varphi(24M)=2^{a+3}.
\tag{4}
\]
If \(a+1\) is even, \(3\mid M\), so \(9\mid24M\), and \(3\mid\varphi(24M)\), contradicting (4). If \(a+1\) is odd, then \(3\nmid M\), so \(\gcd(24,M)=1\) and
\[
\varphi(24M)=8\varphi(M).
\]
Equation (4) would force
\[
\varphi(2^{a+1}-1)=2^a.
\tag{5}
\]
The following lemma excludes this whenever \(a+1\) is odd and greater than one.

**Step 5: The exact Fermat-prefix lemma.** For an integer \(m\ge2\),
\[
\varphi(2^m-1)=2^{m-1}
\quad\Longleftrightarrow\quad
m\in\{2,4,8,16,32\}.
\tag{6}
\]
To prove necessity, suppose the equality holds. Every odd prime divisor \(r\) of \(2^m-1\) must have \(r-1\) a power of \(2\), hence \(r\) is a Fermat prime. If \(m\) had an odd prime divisor \(\ell\), any prime \(r\mid2^\ell-1\) would have multiplicative order exactly \(\ell\) for base \(2\). Therefore the odd prime \(\ell\) would divide \(r-1\), contradicting the Fermat-prime requirement. So \(m=2^s\) with \(s\ge1\).

The Fermat factorization gives
\[
2^{2^s}-1=\prod_{j=0}^{s-1}(2^{2^j}+1).
\]
If \(s\ge6\), the factor \(F_5=2^{32}+1=641\cdot6700417\) occurs. Since \(641\) is prime and \(5\mid640=641-1\), Euler's totient of the product is divisible by \(5\), contradicting its being a power of \(2\). Hence \(s\le5\). Conversely \(F_0,F_1,F_2,F_3,F_4\) are prime, and for each \(1\le s\le5\), multiplicativity gives
\[
\varphi(2^{2^s}-1)
=\prod_{j=0}^{s-1}(F_j-1)
=2^{\sum_{j=0}^{s-1}2^j}
=2^{2^s-1}.
\]
This proves (6). In particular (5) is impossible if \(a+1\) is odd, so no candidate involving the factor \(5\) survives.

**Step 6: The remaining dyadic rays.** If \(n=2^a\) with \(a\ge1\), then
\[
\sigma(n)=M,\quad \varphi(n)=2^{a-1},
\quad \sigma(\varphi(n))=2^a-1,
\]
and hence
\[
T(n)=1\iff\varphi(M)=2^a.
\]
If \(n=3\cdot2^a\), then
\[
\sigma(n)=4M,\quad \varphi(n)=2^a,
\quad \sigma(\varphi(n))=M,
\quad \varphi(4M)=2\varphi(M),
\]
so again
\[
T(n)=1\iff\varphi(M)=2^a.
\]
By (6), these two rays give exactly \(a=1,3,7,15,31\), and therefore exactly the ten numbers in (1). This also proves sufficiency and completes the theorem.

## Verification
The self-contained `verify.py` uses exact integer factorizations and independently evaluates \(\varphi(\sigma(n))-\sigma(\varphi(n))\) for every \(2\le n\le300000\) whose totient is a power of \(2\). It also checks both dyadic rays through exponent \(35\), and all \(562\) tested combinations of the five known Fermat-prime support factors and moderate powers of two within the stated large-integer cap. The output is

`VERIFY_OK phi_power2_candidates_le_300000=175 hits_le_300000=[2, 6, 8, 24, 128, 384, 32768, 98304] dyadic_rays_exponents=0..35 all_ten=[2, 6, 8, 24, 128, 384, 32768, 98304, 2147483648, 6442450944] fermat_support_cases=562 F5_has_prime_factor=641`

It also checks the primality of the first five Fermat numbers and the exact factorization \(2^{32}+1=641\cdot6700417\). These checks are corroborative; the unrestricted result rests on the arguments above, not on the finite bounds.

## Relationship to prior work
OEIS A116083, first made public on 12 March 2006, asks for all \(n\) with \(\varphi(\sigma(n))-\sigma(\varphi(n))=1\). Its 2006 comments prove that both rays \(2^{2^s-1}\) and \(3\cdot2^{2^s-1}\), for \(1\le s\le5\), are solutions and conjecture no others. The present result settles that conjecture **only** inside the separate, natural constructible-totient class.

The all-dyadic subcase is already substantially covered by Solomon Golomb's 1992 manuscript and by the 2025 comments on OEIS A092591. Those sources provide the Fermat-prefix mechanism for pure powers of two, so the dyadic portion is **not** claimed as independently new. The contribution here is the global exclusion, without assumptions about unknown Fermat primes, of every additional totient-dyadic shape containing factors \(5\), \(15\), or any Fermat prime at least \(17\).

OEIS A003401 identifies the indices of constructible regular polygons with \(\varphi(n)\) a power of \(2\). OEIS A019434 lists the five known Fermat primes. The 2007 paper by De Koninck and Luca studies the quotient \(\sigma(\varphi(n))/\varphi(\sigma(n))\), its orders and density, rather than a unit difference on constructible indices. Its primary Mathematics Subject Classification is \(11A25\).

## Limitations
The theorem applies only when \(\varphi(n)\) is a power of \(2\). It does not prove that the ten known numbers exhaust A116083 without that condition. Equivalently, it does not exclude possible new solutions whose totients have an odd prime divisor.

The finite verifier is not a substitute for the unbounded proof. The strongest originality risk is an unindexed elementary argument combining the classical Gauss–Wantzel classification with the 2006 sequence comment; no equivalent whole-class statement was found in the inspected sources.

## References
1. OEIS Foundation, A116083, “Numbers \(n\) such that \(\varphi(\sigma(n))-\sigma(\varphi(n))=1\),” first authored 12 March 2006.
2. OEIS Foundation, A003401, constructible regular polygons; comment relating constructibility to dyadic totients dated 15 February 1999.
3. OEIS Foundation, A092591, exponents of powers of two associated with the commutator; M. Alekseyev's analysis dated 14 June 2025.
4. OEIS Foundation, A001229, the equation \(\varphi(\sigma(n))=n\); and A019434, Fermat primes.
5. S. W. Golomb, “Equality Among Number-Theoretic Functions,” unpublished manuscript, updated 29 December 1992, digitized via OEIS A006872.
6. J.-M. De Koninck and F. Luca, “On the composition of the Euler function and the sum of divisors function,” *Colloquium Mathematicum* 108 (2007), 31–51, DOI 10.4064/cm108-1-4.
