# A harmonic counting law for two-prime arithmetic-derivative–totient coincidences

## Finding
Fix an odd prime \(p\) and write \(D\) for the arithmetic derivative (defined by \(D(r)=1\) for primes \(r\) and the Leibniz rule), and \(\varphi\) for Euler's totient. Define
\[
N_p(X)=\#\{p^a q^b\le X:\ q>p\text{ prime},\ a,b\in\mathbb Z_{\ge1},\ D(p^a q^b)=\varphi(p^a q^b)\}.
\]
Let \(H_m=\sum_{c=1}^m 1/c\). For every fixed odd prime \(p\), as \(X\to\infty\),
\[
\boxed{N_p(X)\sim \frac{pH_{p-2}}{p-1}\,\frac{\log X}{(\log\log X)^2}.}
\]
In particular the leading constant is \(3/2\) when \(p=3\), and \(55/24\) when \(p=5\).

## Assumptions and scope
The prime \(p\) is fixed, odd, and is the **smaller** of precisely two distinct prime factors. The integers \(a,b\) are positive and \(q>p\) varies over primes. The logarithms are natural. No assertion is made about counting solutions with unboundedly varying least prime factor, three or more distinct prime factors, or primes \(q\le p\).

## Proof
**Step 1: exact algebra.** For any distinct primes \(p,q\) and positive integers \(a,b\), the Leibniz rule and multiplicativity of the totient give
\[
D(p^a q^b)=p^{a-1}q^{b-1}(aq+bp),\qquad
\varphi(p^a q^b)=p^{a-1}q^{b-1}(p-1)(q-1).
\]
The equality is therefore equivalent to
\[
aq+bp=(p-1)(q-1),\qquad
p(b+1)=(p-a-1)q+1.\tag{1}
\]
As \(b\ge1\), the right side of (1) must be at least \(2p\), so \(p-a-1>0\). Thus \(1\le a\le p-2\). Reducing (1) modulo \(p\) gives
\[
(a+1)q\equiv1\pmod p.\tag{2}
\]
For each \(a\in\{1,\dots,p-2\}\), the unique permitted nonzero residue is \(r_a\equiv(a+1)^{-1}\pmod p\). Conversely, if \(q>p\) is prime in residue \(r_a\) and
\[
b=\frac{(p-a-1)q+1}{p}-1\ge1,\tag{3}
\]
then \(b\) is an integer and (1) holds, so the required equality holds. For fixed \(p,a\), inequality \(b\ge1\) fails for at most finitely many \(q\). Residues \(r_a\) are distinct as \(a\) varies, so there is no double counting.

**Step 2: invert the size restriction.** Put \(c=p-a-1\in\{1,\dots,p-2\}\). For the permitted primes in a fixed residue class, (3) yields
\[
b=\frac{c}{p}q+O_p(1),\qquad
\log(p^a q^b)=\frac{c}{p}q\log q+O_p(\log q).
\]
The latter expression is strictly increasing for all sufficiently large \(q\). If \(Q_{p,c}(X)\) denotes the real size threshold determined by this expression, the elementary inversion of \(t\log t\) gives
\[
Q_{p,c}(X)\sim\frac{p}{c}\frac{\log X}{\log\log X},\qquad
\log Q_{p,c}(X)\sim\log\log X.\tag{4}
\]
For clarity, setting \(L=\log X\) and \(t=(p/c)L/\log L\), one has \((c/p)t\log t=L(1+o(1))\); monotonicity sandwiches the exact threshold between \((1-\epsilon)t\) and \((1+\epsilon)t\), for any fixed positive \(\epsilon\).

**Step 3: count permitted primes.** The prime number theorem in arithmetic progressions applies because \(p\) is fixed and \(\gcd(r_a,p)=1\). It gives, with \(c=p-a-1\),
\[
\#\{q\le Q_{p,c}(X):q\equiv r_a\pmod p,\ q\text{ prime}\}
\sim \frac{Q_{p,c}(X)}{(p-1)\log Q_{p,c}(X)}
\sim\frac{p}{c(p-1)}\frac{\log X}{(\log\log X)^2}.\tag{5}
\]
Excluding the finitely many primes for which \(q\le p\) or \(b<1\) changes this by at most \(O_p(1)\). Summing the finitely many disjoint classes \(a=1,\dots,p-2\) gives
\[
N_p(X)\sim\frac{p}{p-1}\left(\sum_{c=1}^{p-2}\frac1c\right)
\frac{\log X}{(\log\log X)^2}
=\frac{pH_{p-2}}{p-1}\frac{\log X}{(\log\log X)^2}.
\]
This completes the proof.

## Verification
Run `python3 verify.py` using standard Python 3. The supplied exact-arithmetic regression independently factors each integer through \(500000\), checks its arithmetic derivative and totient on exact two-prime supports, and compares all qualifying integers to the residue-class construction. It also verifies rational identities for the first nineteen odd-prime constants. Its observed first instances are \(15,1225,3993,218491\). These finite checks establish only finite consistency; the infinite asymptotic rests on the exact classification and the classical prime number theorem in arithmetic progressions.

## Relationship to prior work
OEIS A166374 (2009) records the equation \(D(n)=\varphi(n)\). Its August 21, 2014 comment by Robert Israel gives existence of a positive-exponent solution for a broad class of prime pairs by solving a linear Diophantine equation. That comment already supplies **existence**, so existence or the elementary two-prime equation is not claimed as novel. The present result instead gives a fixed-least-prime counting asymptotic with an explicit harmonic leading constant. Ufnarovski and Åhlander's 2003 paper establishes the arithmetic-derivative factorization formula used here; it does not provide this counting law. Other arithmetic-derivative counting theorems for \(D(n)=kn\), with \(k\) a fixed integer, do not imply this equality with \(\varphi(n)\), for which \(D(n)/n\) varies with the two primes. The precise counting law was not identified in the checked published sources.

## Limitations
The leading asymptotic is for each **fixed** odd prime \(p\), not uniformly over growing \(p\). The theorem does not count all solutions of \(D(n)=\varphi(n)\), does not classify larger prime supports, and does not assert a density inside the full integer sequence. The literature comparison cannot rule out an unindexed earlier calculation. Exact regression is not a substitute for the PNT-in-progressions argument.

## References
1. Paolo P. Lava and Giorgio Balzarotti, OEIS A166374, “Numbers whose arithmetic derivative is equal to Euler totient function,” entry originated October 13, 2009; Robert Israel, comment dated August 21, 2014. https://oeis.org/A166374
2. Victor Ufnarovski and Bo Åhlander, “How to Differentiate a Number,” *Journal of Integer Sequences* **6** (2003), Article 03.3.4, Theorem 1. https://cs.uwaterloo.ca/journals/JIS/VOL6/Ufnarovski/ufnarovski.pdf
3. Prime number theorem in arithmetic progressions (classical Dirichlet-modulus asymptotic, applied here only for fixed prime modulus).
