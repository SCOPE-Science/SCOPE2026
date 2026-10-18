# Sharp spectra and three-point stabilization for shifted third-cyclotomic gcds

## Finding
For each integer \(d\ge1\) and \(n\ge1\), let \(F(n)=n^2+n+1=\Phi_3(n)\). For every \(r\ge2\), define
\[
G_{d,r}(n)=\gcd(F(n),F(n+d),\ldots,F(n+(r-1)d)).
\]
Define the pairwise-coprime integers
\[
A_d=\prod_{\substack{p^e\parallel d\\p\equiv1\pmod3}}p^e,\qquad
B_d=\prod_{\substack{p^e\parallel(d^2+3)\\p\ge5}}p^e,\qquad
E_d=\begin{cases}3,&3\mid d,\\1,&3\nmid d.\end{cases}
\]
Empty products equal one, and all products run over primes. Set \(B_{d,r}=B_d\) when \(r=2\) and \(B_{d,r}=1\) when \(r\ge3\), and put \(T_{d,r}=A_dB_{d,r}E_d\).

**Theorem (all shifts and all window lengths).** The exact pair-gcd formula is
\[
G_{d,2}(n)=\gcd(A_d,F(n))\,\gcd(B_d,2n+d+1)\,
\begin{cases}3,&3\mid d\ \text{and}\ n\equiv1\pmod3,\\1,&\text{otherwise}.\end{cases}
\]
For every \(r\ge3\), the gcd stabilizes after three positions and satisfies the especially simple identity
\[
\boxed{G_{d,r}(n)=G_{d,3}(n)=\gcd(F(n),d).}
\]
For each fixed \(d\ge1\) and \(r\ge2\), the **least positive period** of \(G_{d,r}(n)\) as \(n\) varies is exactly \(T_{d,r}\); its **maximum** is exactly \(T_{d,r}\); and its complete set of values is precisely the positive divisors of \(T_{d,r}\).

More precisely, write each prime-power divisor of \(T_{d,r}\) as \(p^e\), and attach \(c_p=2\) if \(p\mid A_d\), or \(c_p=1\) if \(p\mid B_{d,r}E_d\). For every divisor \(h=\prod_{p\mid T_{d,r}}p^{j_p}\) of \(T_{d,r}\), the natural density of positive indices \(n\) for which \(G_{d,r}(n)=h\) is exactly
\[
\boxed{\prod_{p^e\parallel T_{d,r}}w_{p,e,c_p}(j_p)},
\qquad
w_{p,e,c}(j)=\begin{cases}
1-c/p,&j=0,\\
c(p-1)/p^{j+1},&1\le j<e,\\
c/p^e,&j=e.
\end{cases}
\]
Thus every divisor occurs with positive density. In particular the coprimality density is
\[
\boxed{\frac{\#\{1\le n\le N:G_{d,r}(n)=1\}}{N}\longrightarrow
\left(\frac23\right)^{[3\mid d]}
\prod_{\substack{p\mid d\\p\equiv1\pmod3}}\left(1-\frac2p\right)
\prod_{\substack{p\mid d^2+3\\p\ge5}}\left(1-\frac1p\right)^{[r=2]}.}
\]
Here the square brackets are indicator exponents. For example, at \(d=7\) and \(r=2\), the least period and greatest gcd are \(91\), every element of \(\{1,7,13,91\}\) occurs, and the coprimality density is \(60/91\). For \(r\ge3\) the least period is \(7\), and the gcd takes only \(1\) and \(7\).

## Assumptions and scope
The domain is exactly \(d,n\in\mathbb Z_{\ge1}\) and \(r\in\mathbb Z_{\ge2}\). The gcd is positive. The symbol \(p^e\parallel m\) means the indicated power exactly divides the positive integer \(m\). No claim about arbitrary polynomials or arbitrary tuples of shifts is made. Natural densities are limits along positive integer indices, and they exist because each sequence has the proved finite period.

## Proof
**1. Possible prime divisors.** The polynomial \(F(n)\) is always odd, excluding \(2\). The identities
\[
F(n+d)-F(n)=d(2n+d+1),\qquad 4F(n)=(2n+1)^2+3
\]
hold exactly. For any prime \(p\ge5\), the congruence \(F(x)\equiv0\pmod p\) has precisely two roots when \(p\equiv1\pmod3\) and none when \(p\equiv2\pmod3\): its roots are the nontrivial cube roots of unity. At a root, \(2x+1\not\equiv0\pmod p\), since otherwise \(4F(x)\equiv3\pmod p\). Thus both roots are simple and lift uniquely to roots modulo each \(p^e\).

**2. Prime powers from the shift.** Fix \(p\ge5\) with \(p^e\parallel d\). If \(p\equiv2\pmod3\), this prime divides no value of \(F\). Otherwise, at any root of \(F(n)\) modulo \(p\) the factor \(2n+d+1\) is a unit modulo \(p\). Hence
\[
\nu_p(F(n+d)-F(n))=e,
\qquad \nu_p(G_{d,2}(n))=\min\{\nu_p(F(n)),e\}.
\]
The formula also holds when \(p\nmid F(n)\), with both sides zero.

**3. Prime powers from the discriminant of the shift.** Suppose \(p\ge5\) and \(p\nmid d\). Put \(t=2n+d+1\). Because \(d\) and \(4\) are invertible modulo \(p^k\), the two identities in step 1 show the equivalence
\[
p^k\mid G_{d,2}(n)
\quad\Longleftrightarrow\quad
p^k\mid t\ \text{and}\ p^k\mid d^2+3
\qquad(k\ge1).
\]
Consequently
\[
\nu_p(G_{d,2}(n))=\min\{\nu_p(t),\nu_p(d^2+3)\}.
\]
A prime \(p\ge5\) dividing \(d^2+3\) cannot divide \(d\). Such a prime automatically satisfies \(p\equiv1\pmod3\), since it admits a root of \(F\) via the preceding congruences.

**4. The ramified prime.** Exactly the integers \(n\equiv1\pmod3\) have \(3\mid F(n)\), and for \(n=1+3u\),
\[
F(n)=3(1+3u+3u^2),
\]
so \(\nu_3(F(n))=1\). Both \(F(n)\) and \(F(n+d)\) are divisible by \(3\) precisely when \(n\equiv1\pmod3\) and \(3\mid d\). Combining steps 1--4 gives the exact pair formula, with mutually coprime prime-power channels \(A_d\), \(B_d\), and \(E_d\).

**5. Three-point stabilization.** Let a prime \(p\) divide \(G_{d,3}(n)\). The prime \(2\) is excluded. If \(p\nmid d\), the congruences from the differences
\[
F(n+d)-F(n)=d(2n+d+1),\quad
F(n+2d)-F(n)=2d(2n+2d+1)
\]
force both \(2n+d+1\equiv0\pmod p\) and \(2n+2d+1\equiv0\pmod p\), contradicting \(p\nmid d\). Hence only primes dividing \(d\) remain. Steps 2 and 4 show their valuations are exactly those of \(\gcd(F(n),d)\); conversely \(\gcd(F(n),d)\) divides every \(F(n+jd)\) because \(F(n+jd)\equiv F(n)\pmod d\). This proves the identity for \(r=3\) and every \(r\ge3\).

**6. Period, spectrum, and frequencies.** Each channel modulo \(p^e\) is the capped valuation of a polynomial with \(c_p\) simple roots modulo \(p\), with \(c_p=2\) for factors of \(A_d\) and \(c_p=1\) otherwise. Hensel lifting gives exactly \(c_p\) roots modulo \(p^j\) for each \(1\le j\le e\). Among residues modulo \(p^e\), the proportion with capped valuation \(0\) is \(1-c_p/p\); with valuation \(1\le j<e\) it is \(c_p/p^j-c_p/p^{j+1}\); with valuation \(e\) it is \(c_p/p^e\). These are the displayed weights and each is positive. The Chinese remainder theorem makes the channels independent, proving the exact density formula and realization of every divisor of \(T_{d,r}\), including its maximum.

Each channel has period dividing \(p^e\), so \(T_{d,r}\) is a period. It is minimal: for a one-root channel, translation by \(T_{d,r}/p\) changes the capped valuation at a suitable root (for \(e=1\), even the residue condition changes). For a two-root channel and \(e\ge2\), shifting a lifted root by a nonzero multiple of \(p^{e-1}\) destroys divisibility by \(p^e\) by the nonzero derivative. For \(e=1\), a nonzero translation modulo odd \(p\) cannot preserve a set of exactly two roots. Thus \(T_{d,r}/p\) is not a period for any \(p\mid T_{d,r}\). The set of all periods of a sequence forms an additive subgroup of \(\mathbb Z\), hence no proper divisor of \(T_{d,r}\) is a period. This proves minimality, including the case \(T_{d,r}=1\). \(\square\)

## Verification
The bundled `verify.py` uses Python standard-library exact integers and fractions. It compares the pair formula against direct gcd evaluations for \(300\) shifts and \(400\) positive indices per shift (\(120000\) cases), checks three-point stabilization and longer windows on \(30000\) shift-index cases, and enumerates all period residues for \(73\) shifts with tractable predicted periods. It independently checks least periods, all divisor values, and their exact rational frequencies, using \(162339\) full-period observations. It also enumerates the separate squared-prime shift \(d=49\), checking all six gcd values and their exact multiplicities over the \(29449\)-step period. Its captured output is `verification_output.txt`.

These computations are finite corroboration, **not** a substitute for the unbounded congruence, Hensel-lifting and Chinese-remainder proof above.

## Relationship to prior work
Bodin and Drouin [1], Theorem 2.5, prove resultant-controlled periodicity and prime-power decomposition for general coprime polynomial pairs; their Theorem 5.2 handles simple-root local patterns, and Proposition 6.1 discusses their maximal valuations and local periods. They provide a powerful framework, so periodicity and CRT reconstruction as general facts are **not** claimed new here. For the specific third-cyclotomic arithmetic-progression family, the theorem above supplies the explicit split between prime divisors of the shift and of its discriminant expression, a sharp three-point stabilization identity, closed least periods and maximal values for every shift and window length, and every exact rational frequency. Their inspected text does not state these specialized formulas or the three-point transition. Bodin and Dèbes [2] treat a more general coprime-values setting, without this displayed classification. A related earlier preprint of Drouin [3] was identified but its full text could not be accessed for a decisive comparison; equivalence with unpublished or unindexed work remains possible.

The resultant of \(F(x)\) and \(F(x+d)\) is \(d^2(d^2+3)\), typically much larger than the sharp period \(T_{d,2}\). This explains why a generic resultant bound alone does not give the claimed arithmetic data.

## Limitations
The result concerns this one cyclotomic polynomial, equal-step arithmetic progressions, and finite windows of at least two values. It does not give a general classification for arbitrary quadratic polynomials or for non-arithmetic selections of shifts. The novelty assessment is relative to inspected accessible literature, not a guarantee about unindexed results. Exact densities do not imply statistical independence of adjacent indices beyond the CRT factorization of a single index.

## References
[1] A. Bodin and C. Drouin, *Around the gcd of the values of two polynomials*, arXiv:2409.01224v1 (first public version 2024-09-02), https://arxiv.org/pdf/2409.01224.

[2] A. Bodin and P. Dèbes, *Coprime values of polynomials in several variables*, arXiv:2105.13883, https://arxiv.org/abs/2105.13883.

[3] C. Drouin, *PGCD des valeurs de deux polynômes : cas simples et algorithme* (2023), HAL:hal-04085948, https://hal.science/hal-04085948.
