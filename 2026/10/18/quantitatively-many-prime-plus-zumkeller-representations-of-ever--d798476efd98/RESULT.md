# Quantitatively many prime-plus-Zumkeller representations of every sufficiently large odd integer

## Finding
For a positive integer \(N\), let \(R(N)\) count primes \(q<N\) for which \(N-q\) is a Zumkeller number, meaning that the **complete set of positive divisors** of \(N-q\) admits a partition into two subsets of equal sum. There exists an absolute \(N_0\) such that for every odd integer \(N\ge N_0\),
\[
R(N)\ge \frac{N}{100(\log N)^5}.
\]
Consequently, every sufficiently large odd integer is a sum of a prime and a Zumkeller integer; the quantitative result yields unboundedly many distinct representations for each growing odd integer.

## Assumptions and scope
All logarithms are natural. Primes are positive rational primes. A Zumkeller number has an equal-sum bipartition of **all** its positive divisors, not merely a large selected subset. No unproved conjecture is assumed. The proof uses the classical prime number theorem and the uniform Siegel–Walfisz theorem for arithmetic progressions with polylogarithmic moduli. Accordingly, the existence threshold is **ineffective**, and this work does not identify it numerically.

## Proof
**1. A small Zumkeller seed for every odd prime.** Let \(p\ge3\) be prime and choose the unique integer \(a\ge1\) with
\[2^a<p<2^{a+1}.\]
Set \(z=2^a p\) and \(T=2^{a+1}-1\). The divisors of \(z\) are exactly
\[\{2^j:0\le j\le a\}\ \sqcup\ \{p2^j:0\le j\le a\}.\]
For every odd integer \(w\) in \([-T,T]\), the integer \((T+w)/2\) belongs to \([0,T]\), hence its binary digits define signs \(\varepsilon_j\in\{-1,1\}\) with \(\sum_{j=0}^a\varepsilon_j2^j=w\). Since \(p\le T\), choose one sign assignment giving \(-p\) and a second sign assignment giving \(1\). Assigning these signs to the two respective columns of divisors produces signed total
\[(-p)+p\cdot1=0.\]
The positive and negative signs therefore partition every divisor of \(z\) into equal-sum classes. Thus \(z\) is Zumkeller.

**2. A complete congruence progression of Zumkeller numbers.** If \(z\) is Zumkeller and \(u\ge1\) satisfies \(\gcd(u,z)=1\), then \(zu\) is Zumkeller. Indeed every divisor of \(zu\) has a *unique* expression \(de\) with \(d\mid z\) and \(e\mid u\); for each fixed \(e\) multiply the equal-sum divisor partition of \(z\) by \(e\) and unite the classes over all \(e\mid u\). In particular \(\gcd(z,1+tz)=1\) for all integers \(t\ge0\), hence
\[z+z^2t=z(1+tz)\quad(t\ge0)\]
are all Zumkeller numbers.

**3. An admissible polylogarithmic modulus for every odd input.** For an odd \(N\ge3\), choose \(p=p(N)\) to be the *least odd prime not dividing \(N\)*. By the prime number theorem, Chebyshev's function \(\vartheta(x)=\sum_{p\le x}\log p\) satisfies \(\vartheta(x)\sim x\). For all sufficiently large \(N\), if every odd prime \(p\le2\log N\) divided \(N\), then
\[\log N\ge \sum_{3\le p\le2\log N}\log p=\vartheta(2\log N)-\log2>\log N,\]
a contradiction. Thus \(p\le2\log N\). For \(z=2^a p\) from step 1, \(z<p^2\), so, with \(m=z^2\),
\[m<p^4\le16(\log N)^4.\]
As \(N\) is odd and \(p\nmid N\), its difference \(N-z\) is coprime to \(m\); the only prime divisors of \(m\) are \(2\) and \(p\). For sufficiently large \(N\), we also have \(m\le(\log(N/3))^5\) and \(N/3\ge z\).

**4. Count primes in the required residue class.** Put \(r\equiv N-z\pmod m\), \(\gcd(r,m)=1\). Uniform Siegel–Walfisz, in its weighted-prime form, applies for \(m\le(\log(N/3))^5\). At the two endpoints \(N/3\) and \(2N/3\), it gives
\[
\sum_{\substack{N/3<q\le2N/3\\q\text{ prime}\\q\equiv r\pmod m}}\log q
=\frac{N}{3\varphi(m)}+O\!\left(\frac{N}{(\log N)^8}\right),
\]
with an absolute (ineffective) implied constant. For sufficiently large \(N\), the error is at most \(N/(12\varphi(m))\), since \(\varphi(m)\le m<16(\log N)^4\). The prime-weight sum is therefore at least \(N/(4\varphi(m))\). Because each \(\log q\le\log N\), the number of these primes is at least
\[
\frac{N}{4\varphi(m)\log N}\ge \frac{N}{4m\log N}>\frac{N}{64(\log N)^5}\ge\frac{N}{100(\log N)^5}.
\]
For every such prime \(q\), the positive integer \(Z=N-q\) satisfies \(Z\ge N/3\ge z\) and \(Z\equiv z\pmod{z^2}\). Hence \(Z=z(1+tz)\) for some \(t\ge0\), so step 2 proves that \(Z\) is Zumkeller. Distinct \(q\)'s give distinct ordered representations. This proves the assertion.

## Verification
The standalone program `verify.py` checks the sign-partition identity for 46 odd primes through \(211\), direct divisor-subset-sum Zumkeller partitions for 9 small coprime products, and a finite modular-prime witness search on odd inputs from \(951\) to \(29999\). The finite search finds 14,005 inputs with a witness in the prescribed central interval and 520 inputs without a witness *of that particular form*. This is consistent with, but neither proves nor is required by, the eventual theorem. The prime number theorem and Siegel–Walfisz theorem are used as established infinite theorems rather than experimentally checked claims. Run `python3 verify.py` with Python 3 and only the standard library.

## Relationship to prior work
Somu, Kukla, and Tran, *Some Results on Zumkeller Numbers* (arXiv:2310.14149v1, 2023), Conjecture 4.20, propose that every odd integer greater than eight other than 21 is a prime plus a Zumkeller number. Their Proposition 4.12 already covers odd integers outside one residue class modulo 18, and their Theorem 4.19 gives infinitely many even counterexamples. **The present statement is an asymptotic partial result, not a proof of their entire conjecture**: it proves the existence and a quantitative lower bound for every sufficiently large odd integer, including the previously unresolved residue class, without determining the finite exceptions. Their results on all sufficiently large sums involving *practical* numbers are distinct because being practical is not the same as being prime.

Mahanta, Saikia, and Yaqubi (2020), Theorem 2.2, characterize the elementary \(2^a p\) Zumkeller seeds, while classical coprime-product closure supplies the progression construction. These ingredients are known; what is claimed here is their parameter-dependent combination with uniform distribution of primes in reduced residue classes to obtain *representations of every sufficiently large odd integer* and the stated multiplicity bound. The OEIS entry A368082 records finite examples of sums of a Zumkeller number and a prime, not an eventual quantitative theorem. No exact global uniqueness or exhaustive priority conclusion is asserted.

## Limitations
The bound is asymptotic with an ineffective threshold inherited from uniform Siegel–Walfisz. It does not establish Conjecture 4.20 for every odd integer \(N>8\) other than 21, identify any finite exceptions, or make a claim about all large even integers. The finite checks are illustrative, not certificates of the infinite prime-distribution step. Unindexed work that combines these known ingredients may overlap the present result; the literature comparison is necessarily bounded.

## References
1. Sai Teja Somu, Andrzej Kukla, Duc Van Khanh Tran, *Some Results on Zumkeller Numbers*, arXiv:2310.14149v1 (first posted 2023-10-22), especially Proposition 4.12, Theorem 4.19 and Conjecture 4.20. https://arxiv.org/pdf/2310.14149
2. Pankaj Jyoti Mahanta, Manjil P. Saikia and Daniel Yaqubi, *Some properties of Zumkeller numbers and k-layered numbers*, Journal of Number Theory 217 (2020), 218–236, Theorem 2.2 and Lemma 2.8. Open author's manuscript: https://orca.cardiff.ac.uk/id/eprint/134550/1/main.pdf ; doi:10.1016/j.jnt.2020.05.003.
3. The classical prime number theorem and the Siegel–Walfisz theorem (uniform prime distribution for moduli bounded by fixed powers of the logarithm).
4. OEIS A368082, *Positive integers which can be written as a sum of a Zumkeller number and a prime number*. https://oeis.org/A368082
