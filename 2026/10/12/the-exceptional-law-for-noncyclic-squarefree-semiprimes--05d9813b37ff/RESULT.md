# The exceptional law for noncyclic squarefree semiprimes
## Finding
Let \(E(x)\) count squarefree semiprimes
\[
n=pq\le x,\qquad p<q,
\]
for which
\[
\gcd(n,\varphi(n))>1.
\]
Equivalently, \(E(x)\) counts squarefree semiprimes that are not cyclic numbers in the group-theoretic sense: there exists a noncyclic group of order \(n\).

Then
\[
E(x)\sim \mathcal A\,\frac{x}{\log x},
\]
where
\[
\mathcal A=\sum_{p\ \mathrm{prime}}\frac{1}{p(p-1)}=0.7731566\ldots.
\]

More precisely, for \(p<q\),
\[
pq\ \text{is noncyclic}\quad\Longleftrightarrow\quad p\mid q-1.
\]
If \(S_2(x)\) denotes the number of squarefree semiprimes up to \(x\), then the classical Landau estimate
\[
S_2(x)\sim \frac{x\log\log x}{\log x}
\]
therefore gives
\[
\frac{E(x)}{S_2(x)}\sim \frac{\mathcal A}{\log\log x}.
\]
Hence almost every squarefree semiprime is a cyclic group order.

This differs sharply from the unrestricted population, for which the classical counting function of cyclic numbers has relative density tending to \(0\).

## Assumptions and scope
A positive integer \(n\) is called cyclic here when every group of order \(n\) is cyclic. The standard arithmetic criterion is
\[
\gcd(n,\varphi(n))=1.
\]
Equivalently, \(n\) is squarefree and no prime divisor of \(n\) divides one less than another prime divisor.

Only squarefree semiprimes are counted. Prime squares are excluded from \(S_2(x)\), and in any case they are never cyclic because
\[
p\mid\varphi(p^2).
\]

The constant
\[
\mathcal A=\sum_p\frac1{p(p-1)}
\]
is absolutely convergent because its summand is \(O(p^{-2})\).

## Proof
For distinct primes \(p<q\),
\[
\varphi(pq)=(p-1)(q-1).
\]
Since \(q>p\), the prime \(q\) cannot divide \(p-1\), and neither prime divides its own predecessor. Thus
\[
\gcd(pq,\varphi(pq))>1
\]
holds exactly when
\[
p\mid q-1.
\]
Consequently
\[
E(x)=\sum_{p<\sqrt x}\pi\!\left(\frac{x}{p};p,1\right),
\]
where \(\pi(y;m,a)\) counts primes at most \(y\) congruent to \(a\pmod m\).

Fix \(z\ge2\). For every fixed prime \(p\le z\), the prime number theorem in arithmetic progressions gives
\[
\pi\!\left(\frac{x}{p};p,1\right)\sim\frac{x}{p(p-1)\log x}.
\]
Therefore
\[
\sum_{p\le z}\pi\!\left(\frac{x}{p};p,1\right)
=\frac{x}{\log x}\sum_{p\le z}\frac1{p(p-1)}+o_z\!\left(\frac{x}{\log x}\right).
\]

It remains to control the primes \(p>z\) uniformly. Split them at \(x^{1/3}\).

For
\[
z<p\le x^{1/3},
\]
Brun--Titchmarsh gives
\[
\pi\!\left(\frac{x}{p};p,1\right)
\le\frac{2x}{p(p-1)\log(x/p^2)}
\le\frac{6x}{p(p-1)\log x}.
\]
Hence this part is at most
\[
\frac{6x}{\log x}\sum_{p>z}\frac1{p(p-1)}.
\]

For
\[
x^{1/3}<p<\sqrt x,
\]
any counted prime has the form
\[
q=kp+1
\]
with
\[
k\le\frac{x}{p^2}.
\]
Ignoring primality only enlarges the count, so this range contributes at most
\[
\sum_{x^{1/3}<p<\sqrt x}\frac{x}{p^2}
\le x\sum_{m>x^{1/3}}\frac1{m^2}=O(x^{2/3}).
\]
Since
\[
x^{2/3}=o\!\left(\frac{x}{\log x}\right),
\]
we obtain
\[
\limsup_{x\to\infty}\frac{\log x}{x}\sum_{z<p<\sqrt x}\pi\!\left(\frac{x}{p};p,1\right)
\le6\sum_{p>z}\frac1{p(p-1)}.
\]
The right-hand side tends to \(0\) as \(z\to\infty\). Letting first \(x\to\infty\) and then \(z\to\infty\) proves
\[
E(x)\sim\left(\sum_p\frac1{p(p-1)}\right)\frac{x}{\log x}.
\]

Finally, the standard squarefree-semiprime estimate
\[
S_2(x)\sim\frac{x\log\log x}{\log x}
\]
immediately yields
\[
\frac{E(x)}{S_2(x)}\sim\frac{\mathcal A}{\log\log x}.
\]

## Verification
The accompanying checker performs two independent finite checks.

First, for every squarefree semiprime up to \(200000\), it compares the arithmetic test
\[
\gcd(n,\varphi(n))>1
\]
with the claimed local criterion
\[
p\mid q-1.
\]
They agree in every case.

Second, it counts exceptional semiprimes up to several cutoffs and prints
\[
E(x)\frac{\log x}{x}.
\]
It also evaluates a partial sum for \(\mathcal A\) and gives an elementary tail enclosure using
\[
\sum_{n>N}\frac1{n(n-1)}=\frac1N.
\]
These finite checks are corroborative only; the asymptotic proof is the argument above.

## Relationship to prior work
The arithmetic characterization of cyclic numbers is classical: a cyclic number is squarefree and no prime factor divides one less than another prime factor. In the semiprime case this immediately reduces to
\[
p\nmid q-1.
\]
That local criterion is not claimed as new.

Grau, Rodríguez, Oller-Marcén and Sadornil explicitly recall ordinary cyclic numbers and their criterion while developing Gaussian analogues. Their first public arXiv version was submitted on 19 January 2014.

Pollack's later full treatment of ordinary cyclic numbers has primary classification \(11N37\). It studies the unrestricted counting function
\[
C(x)=\#\{n\le x:\gcd(n,\varphi(n))=1\}
\]
and refines Erdős's global asymptotic series. Its proof uses divisibility relations
\[
p\mid q-1
\]
inside a much broader sieve, but it does not state a semiprime-conditioned asymptotic.

OEIS A003277 records the exact cyclic-number criterion and the classical unrestricted asymptotic, but it does not state the exceptional semiprime count or the constant \(\mathcal A\).

Thus the new content here is the sharp first-order asymptotic for the noncyclic squarefree-semiprime layer, including its explicit constant and the resulting relative exceptional law
\[
\mathcal A/\log\log x.
\]

## Limitations
The theorem is restricted to squarefree semiprimes. It does not describe cyclic numbers with three or more prime factors, where several divisibility interactions
\[
p_i\mid p_j-1
\]
can overlap.

The proof uses the prime number theorem in fixed arithmetic progressions and Brun--Titchmarsh. No effective error term for
\[
E(x)-\mathcal A x/\log x
\]
is claimed.

Szele's 1947 criterion and Erdős's 1948 global asymptotic are historically earlier than the date stored in metadata, but the inspected records did not supply an exact public calendar day for those works. The metadata date is the earliest exact public date verified here from an archival electronic source.

## References
1. J. M. Grau, M. Rodríguez, A. Oller-Marcén and D. Sadornil, "Fermat test with gaussian base and Gaussian pseudoprimes", arXiv:1401.4708v1, submitted 19 January 2014.
2. P. Pollack, "Numbers which are orders only of cyclic groups", arXiv:2007.09734v1; later *Proceedings of the American Mathematical Society* 150 (2022), 515--524. Primary MSC 11N37.
3. T. Szele, "Über die endlichen Ordnungszahlen, zu denen nur eine Gruppe gehört", *Commentarii Mathematici Helvetici* 20 (1947), 265--267.
4. P. Erdős, "Some asymptotic formulas in number theory", *Journal of the Indian Mathematical Society* (N.S.) 12 (1948), 75--78.
5. OEIS Foundation, A003277, "Cyclic numbers".
