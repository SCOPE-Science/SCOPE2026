# The least three-prime squarefree integer with an integral reciprocal-gcd sum

## Finding
For every positive integer \(n\), define
\[
\mathcal H(n)=\sum_{j=1}^{n}\frac{1}{\gcd(n,j)}.
\]
Among squarefree positive integers with exactly three distinct prime factors, the **unique smallest** integer for which \(\mathcal H(n)\) is an integer is
\[
\boxed{N_0=349\cdot121453\cdot9710803=411612748708891.}
\]
Its value is \(\mathcal H(N_0)=410433300314317\). Uniqueness refers to the integer attaining the minimum; the proof actually enumerates every qualifying three-prime integer \(n\le N_0\).

## Assumptions and scope
All primes are positive rational primes. Squarefree means that no square of a prime divides \(n\); "exactly three prime factors" refers to three distinct primes, each of exponent one. The theorem makes no assertion about the smallest element of the unrestricted integrality set, about four-prime integers, or about all qualifying integers greater than \(N_0\).

Write \(F(t)=t^2-t+1\). For distinct primes \(a,b\), write \(a\longrightarrow b\) if \(b\mid F(a)\). A directed three-cycle \(a\longrightarrow b\longrightarrow c\longrightarrow a\) must have three distinct prime vertices.

## Proof
**1. An exact integrality criterion.** The divisor-sum identity
\[
\mathcal H(n)=\frac{h(n)}{n},\qquad
h(n)=\prod_{p^e\parallel n}\frac{p^{2e+1}+1}{p+1}
\]
can be obtained by grouping the summands by their gcd with \(n\) and using multiplicativity. For a squarefree integer \(n=abc\) with distinct primes,
\[
\mathcal H(abc)=\frac{F(a)F(b)F(c)}{abc}.
\]
Because \(F(t)\equiv1\pmod t\), integrality requires each prime vertex to receive an arrow from one of the other two vertices. Choose one incoming arrow at each vertex. A finite directed graph on three vertices in which every vertex has an incoming arrow contains a directed cycle (reverse the arrows and follow the unique chosen outgoing edge). There are no loops, since \(t\nmid F(t)\) for \(t>1\).

**2. Two-cycles cannot occur.** More generally, there are no integers \(a,b>1\) satisfying simultaneously \(a\mid F(b)\) and \(b\mid F(a)\). For if such exist, choose one with the smallest possible maximum, and assume \(1<a<b\) (equality is excluded by \(F(a)\equiv1\pmod a\)). Put \(c=F(a)/b\). Then \(1\le c<a\) and \(c\mid F(a)\). Also, \(bc\equiv1\pmod a\), so
\[
c^2F(b)=c^2(b^2-b+1)\equiv1-c+c^2=F(c)\pmod a.
\]
Thus \(a\mid F(c)\). If \(c=1\), this would imply \(a\mid F(1)=1\), impossible. Otherwise \(1<c<a\), giving another mutual-divisibility pair \((a,c)\) with smaller maximum, a contradiction. Consequently the three selected arrows form a directed three-cycle, and conversely a directed three-cycle makes \(abc\mid F(a)F(b)F(c)\). Hence **three-prime squarefree integrality is equivalent to the existence of such a directed three-cycle on its prime factors**.

**3. A witness.** The integers \(349\), \(121453\), \(9710803\) are prime, as certified by exact trial division in `certificate.py`. Direct arithmetic gives
\[
121453\mid F(349),\quad
9710803\mid F(121453),\quad
349\mid F(9710803).
\]
Their product is \(N_0\). Computing the full product gives \(F(349)F(121453)F(9710803)/N_0=410433300314317\), an integer.

**4. Complete finite exclusion below the witness.** Fix \(B=N_0\), and suppose a directed three-cycle has distinct prime vertices \(p,u,v\) with \(p\) its smallest vertex. Then \(p^3\le puv\le B\) and, orienting the cycle from \(p\),
\[
p\longrightarrow u\longrightarrow v\longrightarrow p,
\quad u\mid F(p),\quad v\mid F(u),\quad p\mid F(v).
\]
Both \(u\) and \(v\) are primes greater than \(p\). In particular
\[
p u(p+1)\le B,\qquad p<v\le \left\lfloor\frac B{pu}\right\rfloor.
\]
These inequalities give an *exhaustive* algorithm rather than an arbitrary search cutoff. Enumerate every prime \(p\le\lfloor B^{1/3}\rfloor\). Factor \(F(p)\) completely and enumerate every prime divisor \(u>p\) with \(pu(p+1)\le B\). Finally factor \(F(u)\) completely and retain its prime divisors \(v\) satisfying \(p<v\le\lfloor B/(pu)\rfloor\), \(v\ne u\), and \(p\mid F(v)\). Every possible integer \(n=puv\le B\) from the target class must appear in this search, in one of the two orientations of its three primes.

The exact integer-only certificate `certificate.py` enumerates \(7339\) possible smallest primes and \(1948\) viable first edges. Its largest intermediate prime is \(19771363\). It finds **exactly one** closing directed three-cycle, namely
\[
349\longrightarrow121453\longrightarrow9710803\longrightarrow349.
\]
The certificate uses the Sieve of Eratosthenes and trial division with all primes through the square root of each factored integer: the first sieve has bound \(75000\) with \(75000^3>B\), while the second sieve extends through the maximum \(u\), and \(\sqrt{F(u)}<u\) for every \(u>1\). Thus no prime factor, intermediate pair, or closing cycle can be missed. The output is independently reproducible by running `python3 certificate.py`; its exact expected output is included in `certificate_output.txt`. Combining this exhaustive finite exclusion with the witness proves the theorem. \(\square\)

## Verification
The package includes a self-contained Python 3 standard-library certificate. Its integer assertions verify the complete relevant factorization ranges, the \(7339\) smallest-prime cases, the \(1948\) eligible first edges, the unique closing cycle, primality of the three witness factors, and the exact value of \(\mathcal H(N_0)\). The script uses no floating-point approximations and no probabilistic primality tests.

The universal statement is proved by reduction to a **finite region bounded by the exhibited witness**. The script does not purport to enumerate cycles with product greater than \(N_0\).

## Relationship to prior work
De Koninck and Letendre (2026) introduce the reciprocal-gcd integrality set, its multiplicative formula, the directed prime-divisibility graph and constructions from closed cycles. They prove an upper bound for the counting function, not the least three-prime member. The related OEIS sequence A317480 records initial terms and a formula for membership but does not supply a full-product minimization certificate up to the very large bound \(N_0\).

An earlier least-vertex calculation shows that \(349\) is the smallest possible least prime on a directed three-cycle and exhibits the same witness. **That conclusion does not imply the present theorem:** a cycle whose least prime is greater than \(349\) could a priori have a smaller product. The new claim is the sharp global minimization of the product over every possible three-prime cycle, not the rediscovery of the witness or the least-vertex calculation.

## Limitations
The result is exact only for squarefree integers with precisely three prime factors. It does not show that \(N_0\) is the smallest nontrivial integer with an integral reciprocal-gcd sum; smaller known examples have four prime factors. No infinite family, density result, or structure theorem beyond the stated minimum is asserted. The finite certificate is exact subject to correct execution of the supplied deterministic elementary algorithms; independent third-party validation has not been performed.

## References
1. J.-M. De Koninck and P. Letendre, *The Integer Values of \(\sum_{i=1}^{n}1/\gcd(n,i)\)*, arXiv:2610.10572v1 (first public version 4 October 2026), especially Sections 1, 2, 4, 5, and 7. https://arxiv.org/html/2610.10572v1
2. OEIS Foundation, sequence A317480, *Numbers m such that Sum_{k=1..m} 1/gcd(k,m) is an integer*. https://oeis.org/A317480
