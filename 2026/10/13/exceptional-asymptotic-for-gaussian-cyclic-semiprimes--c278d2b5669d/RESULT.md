# Exceptional asymptotic for Gaussian-cyclic semiprimes
## Finding
Let \(\Phi(n)\) denote the Gaussian analogue of Euler's totient introduced for the norm-one group over Gaussian integers, and call \(n\) G-cyclic when
\[
\gcd(n,\Phi(n))=1.
\]
For \(X\ge1\), define
\[
E(X)=\#\{pq\le X: 3\le p<q\text{ are primes and }\gcd(pq,\Phi(pq))>1\}.
\]
Then
\[
E(X)\sim C\,\frac{X}{\log X},
\]
where
\[
C=\sum_{\substack{p\ge3\\p\ {\rm prime}}}\frac1{p(p-1)}.
\]
A certified finite summation gives
\[
0.2731566631<C<0.2731567632,
\]
so
\[
C=0.273157\ldots
\]
to six decimal places.

Consequently, almost every odd squarefree semiprime is G-cyclic: the proportion of G-cyclic members in that stratum tends to \(1\).

There is also an exact local description. If \(3\le p<q\) are primes and
\[
\beta(q)=\left(\frac{-1}{q}\right),
\]
then
\[
pq\text{ is not G-cyclic}
\quad\Longleftrightarrow\quad
p\mid q-\beta(q).
\]
For fixed \(p\), the exceptional primes \(q\) therefore lie in exactly two reduced residue classes modulo \(4p\), and their relative density among primes is
\[
\frac1{p-1}.
\]

## Assumptions and scope
The Gaussian Euler function is
\[
\Phi(n)=|\mathcal G_n|,
\]
where
\[
\mathcal G_n=\{a+bi\in\mathbb Z[i]/n\mathbb Z[i]:a^2+b^2\equiv1\pmod n\}.
\]
For an odd prime \(r\), put
\[
\beta(r)=\left(\frac{-1}{r}\right)
=
\begin{cases}
1,&r\equiv1\pmod4,\\
-1,&r\equiv3\pmod4.
\end{cases}
\]
The primary paper proves that for odd squarefree \(n\),
\[
\Phi(n)=\prod_{r\mid n}\bigl(r-\beta(r)\bigr).
\]

The asymptotic proof uses two standard analytic inputs: the prime number theorem in arithmetic progressions for each fixed modulus, and the Brun--Titchmarsh inequality in the form
\[
\pi(Y;m,a)\le
\frac{2Y}{\varphi(m)\log(Y/m)}
\]
for reduced \(a\) and \(Y>m\).

Only odd squarefree semiprimes are counted in \(E(X)\). Even semiprimes and prime squares are excluded from its definition.

## Proof
Let
\[
n=pq
\]
with odd primes
\[
3\le p<q.
\]
The squarefree formula from the primary source gives
\[
\Phi(pq)=\bigl(p-\beta(p)\bigr)\bigl(q-\beta(q)\bigr).
\]
Neither \(p\) nor \(q\) divides its own factor. Hence \(pq\) is not G-cyclic exactly when at least one of
\[
p\mid q-\beta(q),
\qquad
q\mid p-\beta(p)
\]
holds.

The second divisibility is impossible. Since \(p\) and \(q\) are odd distinct primes,
\[
q\ge p+2>p+1\ge p-\beta(p).
\]
Therefore
\[
pq\text{ is not G-cyclic}
\quad\Longleftrightarrow\quad
p\mid q-\beta(q).
\tag{1}
\]

Because \(q\) is odd, condition (1) has two cases:
\[
q\equiv1\pmod4,\qquad q\equiv1\pmod p,
\]
or
\[
q\equiv3\pmod4,\qquad q\equiv-1\pmod p.
\]
By the Chinese remainder theorem these are exactly two distinct reduced residue classes modulo \(4p\). Denote them by \(a_p\) and \(b_p\). Since
\[
\varphi(4p)=2(p-1),
\]
the prime number theorem in arithmetic progressions gives, for every fixed odd prime \(p\),
\[
\pi(Y;4p,a_p)+\pi(Y;4p,b_p)
\sim
\frac{\operatorname{Li}(Y)}{p-1}.
\tag{2}
\]
This proves the fixed-\(p\) density statement.

Now sum over the smaller prime. Formula (1) gives exactly
\[
E(X)
=
\sum_{\substack{3\le p<\sqrt X\\p\ {\rm prime}}}
\left(
\pi(X/p;4p,a_p)+\pi(X/p;4p,b_p)
\right).
\tag{3}
\]
No correction for primes \(q<p\) is needed: an odd prime below \(p\) cannot be congruent to \(1\) or \(-1\) modulo \(p\).

Fix a real cutoff \(P\). For the finitely many primes
\[
3\le p\le P,
\]
equation (2) yields
\[
\sum_{\substack{3\le p\le P\\p\ {\rm prime}}}
\left(
\pi(X/p;4p,a_p)+\pi(X/p;4p,b_p)
\right)
\sim
\frac{X}{\log X}
\sum_{\substack{3\le p\le P\\p\ {\rm prime}}}
\frac1{p(p-1)}.
\tag{4}
\]

It remains to control the primes above \(P\) uniformly. First suppose
\[
P<p\le X^{1/3}.
\]
For sufficiently large \(X\),
\[
\log\!\left(\frac{X}{4p^2}\right)\ge\frac14\log X.
\]
Applying Brun--Titchmarsh to each of the two classes modulo \(4p\) gives
\[
\pi(X/p;4p,a_p)+\pi(X/p;4p,b_p)
\le
\frac{8X}{p(p-1)\log X}.
\]
Consequently,
\[
\sum_{\substack{P<p\le X^{1/3}\\p\ {\rm prime}}}
\left(
\pi(X/p;4p,a_p)+\pi(X/p;4p,b_p)
\right)
\le
\frac{8X}{\log X}
\sum_{\substack{p>P\\p\ {\rm prime}}}
\frac1{p(p-1)}.
\tag{5}
\]

Finally consider
\[
X^{1/3}<p<\sqrt X.
\]
A bad prime \(q\) lies in one of two residue classes modulo \(p\), so even without imposing primality there are at most
\[
\frac{2X}{p^2}+2
\]
possible integers \(q\le X/p\). Hence the contribution from this range is at most
\[
2X\sum_{m>X^{1/3}}\frac1{m^2}+2\sqrt X
=
O(X^{2/3}),
\tag{6}
\]
which is
\[
o\!\left(\frac{X}{\log X}\right).
\]

The series
\[
C=\sum_{\substack{p\ge3\\p\ {\rm prime}}}\frac1{p(p-1)}
\]
converges absolutely. Equations (4)--(6) imply
\[
\liminf_{X\to\infty}\frac{E(X)\log X}{X}
\ge
\sum_{\substack{3\le p\le P\\p\ {\rm prime}}}\frac1{p(p-1)},
\]
while
\[
\limsup_{X\to\infty}\frac{E(X)\log X}{X}
\le
\sum_{\substack{3\le p\le P\\p\ {\rm prime}}}\frac1{p(p-1)}
+
8\sum_{\substack{p>P\\p\ {\rm prime}}}\frac1{p(p-1)}.
\]
Letting \(P\to\infty\) forces both limits to equal \(C\). Thus
\[
E(X)\sim C\,\frac{X}{\log X}.
\]

By Landau's semiprime theorem, the number of odd squarefree semiprimes at most \(X\) is
\[
(1+o(1))\frac{X\log\log X}{\log X}.
\]
The exceptional proportion is therefore
\[
\frac{C+o(1)}{\log\log X},
\]
which tends to \(0\). This proves the density-one conclusion.

For the numerical constant, summing the prime series through \(10^7\) gives
\[
0.2731566631897197.
\]
The omitted prime tail is smaller than the full integer tail
\[
\sum_{m>10^7}\frac1{m(m-1)}=10^{-7}.
\]
This yields the certified interval stated above.

## Verification
The attached checker performs three independent finite stress tests.

First, for every odd squarefree semiprime
\[
pq\le2\,000\,000,
\]
it computes the Gaussian Euler factorization directly and confirms that
\[
\gcd(pq,\Phi(pq))>1
\]
is equivalent to
\[
p\mid q-\beta(q).
\]

Second, it counts all odd squarefree semiprimes and all exceptional ones at the same cutoff. This is not used as evidence for the asymptotic, but it checks that the exact local classification is implemented consistently.

Third, it sums
\[
\sum_{3\le p\le10^7}\frac1{p(p-1)}
\]
over primes and certifies the displayed interval using the telescoping integer-tail bound.

The infinite asymptotic is proved analytically above; no finite enumeration is treated as an infinite proof.

## Relationship to prior work
Grau, Oller-Marcén, Rodríguez, and Sadornil introduced G-cyclic numbers by the condition
\[
\gcd(\Phi(n),n)=1
\]
and proved the squarefree product formula for \(\Phi\). Their G-cyclic section studies the relation with Gaussian Carmichael numbers and congruence criteria, but does not give a semiprime counting law or an exceptional-density constant.

The exact OEIS entry A235866 records G-cyclic numbers, notes that all terms are odd and squarefree, and supplies computational formulas. It contains neither the two-residue-class semiprime classification nor an asymptotic count.

Targeted searches for G-cyclic semiprime density, Gaussian-cyclic asymptotics, the residue condition
\[
p\mid q-\beta(q),
\]
and the constant
\[
\sum_{p\ge3}\frac1{p(p-1)}
\]
found the primary paper and the exact sequence entry, but no published statement implying the theorem above.

## Limitations
The theorem counts only the two-prime squarefree layer. It does not determine the density of G-cyclic integers among all integers, nor does it address the primary paper's question of whether every odd G-cyclic number has a Gaussian Carmichael multiple.

The proof invokes the prime number theorem in arithmetic progressions, Brun--Titchmarsh, and Landau's semiprime theorem as established inputs rather than reproving them.

The literature search covered the primary full text, the exact sequence database, direct phrase searches, equivalent residue formulations, and statement-level searches of a mathematical-results index. An equivalent result in unindexed notes or unpublished work remains a residual risk.

## References
1. J. M. Grau, A. M. Oller-Marcén, M. Rodríguez, and D. Sadornil, “Fermat test with Gaussian base and Gaussian pseudoprimes,” arXiv:1401.4708v1, first public 19 January 2014; later *Czechoslovak Mathematical Journal* 65 (2015), 969–982.
2. OEIS Foundation, A235866, “G-cyclic numbers: numbers \(n\) such that \(\gcd(n,\Phi(n))=1\).”
3. H. L. Montgomery and R. C. Vaughan, “The large sieve,” *Mathematika* 20 (1973), 119–134.
