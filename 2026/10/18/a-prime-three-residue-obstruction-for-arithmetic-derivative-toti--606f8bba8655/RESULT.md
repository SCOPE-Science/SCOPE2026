# A prime-three residue obstruction for arithmetic-derivative–totient coincidences

## Finding
For every positive integer \(n\) divisible by \(3\), the equality \(D(n)=\varphi(n)\) implies one of two cases: \(n=9\), or
\[
n=3m,\qquad m>1\text{ odd},\quad p\mid m\Longrightarrow p\equiv2\pmod3,\quad \omega(m)\equiv1\pmod2.
\]
These conditions completely exclude solutions with three distinct prime factors containing \(3\), **even when the other prime exponents are arbitrary**. In the support-two case the exact classification is
\[
D(3p^b)=\varphi(3p^b)\quad\Longleftrightarrow\quad p\equiv2\pmod3,\quad b=(p-2)/3,
\]
for odd primes \(p>3\) and integers \(b\ge1\). The support-two identity is included to exhibit the sharpness and usefulness of the residue restriction; the necessary conditions at higher support are not asserted sufficient.

## Assumptions and scope
The arithmetic derivative is defined by \(D(p)=1\) for all primes, \(D(1)=0\), and \(D(uv)=uD(v)+vD(u)\). The totient is \(\varphi\), and \(\omega(m)\) counts distinct prime factors. Prime exponents are unrestricted. The theorem makes a necessary congruence and support claim for **all** solutions divisible by \(3\), plus an exact classification when there is one other distinct prime factor. It does not classify integers not divisible by \(3\) or give sufficient conditions at larger supports.

## Proof
Write \(n=3^a m\) with \(a\ge1\) and \(\gcd(m,3)=1\). If \(m=1\), the prime-power formulas give \(D(n)=a3^{a-1}\) and \(\varphi(n)=2\cdot3^{a-1}\), so \(a=2\) and \(n=9\).

Assume \(m>1\). The exact arithmetic logarithmic derivative and totient product formulas imply
\[
\frac{D(n)}n=\frac a3+\sum_{p^e\parallel m}\frac ep,
\quad\frac{\varphi(n)}n=\frac23\prod_{p\mid m}\left(1-\frac1p\right)<\frac23.
\]
Thus \(a=1\). If \(2\mid m\), then \(D(n)/n\ge1/3+1/2>\varphi(n)/n\), so \(m\) must be odd.

Now \(n=3m\) and the Leibniz rule gives \(D(n)=m+3D(m)\equiv m\not\equiv0\pmod3\). The equality \(D(n)=\varphi(n)=2\varphi(m)\) forces \(3\nmid\varphi(m)\). If a prime divisor \(p\mid m\) were congruent to \(1\pmod3\), its factor \(p-1\) would divide \(\varphi(m)\) and be divisible by \(3\), a contradiction. Because \(m\) is odd and coprime to \(3\), every prime factor of \(m\) is therefore congruent to \(2\pmod3\).

Write \(m=\prod_{i=1}^k p_i^{e_i}\), with all \(p_i\equiv-1\pmod3\). Then modulo \(3\) the equality \(m=2\varphi(m)\) reads
\[
(-1)^{\sum_i e_i}=2(-1)^{\sum_i(e_i-1)}=-(-1)^{\sum_i e_i-k}.
\]
Canceling the invertible sign yields \((-1)^k=-1\), hence \(k=\omega(m)\) is odd. Thus the total support size \(\omega(n)=1+k\) is even, so in particular support size three is impossible.

Finally when \(m=p^b\) the equality becomes
\[
\frac13+\frac bp=\frac23\frac{p-1}{p},\quad\text{i.e.}\quad p=3b+2.
\]
For odd primes this holds exactly when \(p\equiv2\pmod3\) and \(b=(p-2)/3\), and conversely substitution proves equality. For example \(n=15\) at \(p=5\) and \(n=3993=3\cdot11^3\) at \(p=11\). All claims follow.

## Verification
The source-independent standard-library checker `artifacts/check_three_adic.py` enumerates every multiple of \(3\) through \(100000\), recomputes the arithmetic derivative and totient from factorizations, and checks all necessary prime-three congruences on each hit. It additionally checks seven exact two-support constructions. The checker passed. This finite computation is only diagnostic: the preceding prime-power bound and modulo-three identities prove the assertion for unbounded integers.

## Relationship to prior work
The 2009 sequence OEIS A166374 records the defining coincidence \(D(n)=\varphi(n)\) and examples \(9,15,3993\); a 2014 note provides general constructions with two prime factors, which cover the support-two portion of the theorem. The present claim is the **unrestricted-support local obstruction at the prime three**: forced single exponent, allowed residue classes and parity of the remaining distinct prime support, excluding all three-support integers divisible by three. Grau and Oller-Marcén (2011) address the different Giuga-number equation \(D(n)=an+1\); an indexed arithmetic-derivative/cototient result also concerns a different expression. Neither comparison yields this residue-support obstruction directly.

## Limitations
The two-support classification is a known consequence of the established two-prime parameterization and is not offered as independently original. The claimed new content is the simultaneous necessary constraints for arbitrary prime supports and exponents, especially the three-support exclusion. The restriction is not sufficient at larger support; a solution beyond the verified examples is not asserted. An implicit or unindexed equivalent argument may exist.

## References
- P. P. Lava and G. Balzarotti, OEIS A166374, created October 13, 2009, https://oeis.org/A166374 (equation, examples, construction comments).
- J. M. Grau and A. M. Oller-Marcén, "Giuga Numbers and the arithmetic derivative," arXiv:1103.2298, March 11, 2011, https://arxiv.org/abs/1103.2298 (background product-rule formulas; distinct equation).
