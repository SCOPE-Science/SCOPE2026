# A mod-8 obstruction for odd divisor power means

## Statement

For an integer \(r\ge 1\), write
\[
\sigma_r(n)=\sum_{d\mid n} d^r,\qquad \tau(n)=\sigma_0(n),\qquad
M_r(n)=\frac{\sigma_r(n)}{\tau(n)}.
\]
When \(n\) is odd and \(r\) is even, \(M_r(n)\) is a 2-adic unit even when it is not an ordinary integer, so its residue modulo \(8\) is well defined in \(\mathbf Z_2\).

**Theorem.** Let \(n\) be odd and let \(r\) be a positive even integer.

1. If \(r\equiv0\pmod4\), then
   \[
   M_r(n)\equiv1\pmod8.
   \]
2. If \(r\equiv2\pmod4\), then
   \[
   M_r(n)\equiv
   \begin{cases}
   1\pmod8,&n\equiv1,7\pmod8,\\
   5\pmod8,&n\equiv3,5\pmod8.
   \end{cases}
   \]
   Equivalently,
   \[
   M_r(n)\equiv 3-2\left(\frac2n\right)\pmod8,
   \]
   where \((2/n)\) is the Jacobi symbol.

**Corollary.** Suppose \(r\equiv2\pmod4\) and \(n\) is odd. If
\[
M_r(n)=c^t
\]
for integers \(c\ge1\) and even \(t\ge2\), then
\[
\boxed{n\equiv\pm1\pmod8}.
\]
In particular, in the terminology recorded in OEIS A140480/A003601, every odd \(\sigma_r\)-number with \(r\equiv2\pmod4\) is congruent to \(\pm1\pmod8\). For \(r=2\), every odd RMS number is therefore congruent to \(1\) or \(7\pmod8\).

The oddness qualifier is essential: even RMS numbers are known and are tabulated separately in OEIS A224988.

## Proof

Factor
\[
n=\prod_i p_i^{e_i}
\]
with all \(p_i\) odd. Multiplicativity gives
\[
M_r(n)=\prod_i F_{e_i+1}(p_i^r),
\qquad
F_N(x)=\frac{1+x+\cdots+x^{N-1}}{N}.
\]
We first record a local 2-adic congruence.

### Lemma

If \(x=1+8h\) with \(h\in\mathbf Z\) and \(N\ge1\), then \(F_N(x)\in\mathbf Z_2^\times\) and
\[
F_N(x)\equiv 1+4h(N-1)\pmod8.
\]
Thus
\[
F_N(x)\equiv
\begin{cases}
1\pmod8,&N\text{ odd},\\
(x+1)/2\pmod8,&N\text{ even}.
\end{cases}
\]

**Proof of the lemma.** Expanding \(x^j=(1+8h)^j\) and summing the binomial coefficients gives in \(\mathbf Q_2\)
\[
F_N(1+8h)
 =\sum_{k=0}^{N-1}(8h)^k\frac{\binom{N-1}{k}}{k+1}.
\]
The \(k=0\) term is \(1\), and the \(k=1\) term is \(4h(N-1)\). For every \(k\ge2\),
\[
v_2\!\left(\frac{8^k}{k+1}\right)
\ge 3k-\lfloor\log_2(k+1)\rfloor\ge3,
\]
so every remaining term vanishes modulo \(8\). The displayed residue is always odd, proving at the same time that \(F_N(x)\) is a 2-adic unit. \(\square\)

Since \(r\) is even, \(p_i^r\equiv1\pmod8\), so the lemma applies to every local factor.

If \(r\equiv0\pmod4\), then \(p_i^r\equiv1\pmod{16}\) for every odd prime \(p_i\). Hence \(h\) is even in every local factor, so all local factors are \(1\pmod8\). This proves the first part.

Now assume \(r\equiv2\pmod4\). Then
\[
p_i^r\equiv p_i^2\pmod{16}.
\]
If \(e_i\) is even, then \(N=e_i+1\) is odd and the local factor is \(1\pmod8\). If \(e_i\) is odd, then the lemma gives
\[
F_{e_i+1}(p_i^r)\equiv
\begin{cases}
1\pmod8,&p_i\equiv\pm1\pmod8,\\
5\pmod8,&p_i\equiv\pm3\pmod8.
\end{cases}
\]
Let \(m\) be the number of prime factors \(p_i\equiv\pm3\pmod8\) that occur to an odd exponent. Therefore
\[
M_r(n)\equiv5^m\pmod8.
\]
On the other hand,
\[
\left(\frac2n\right)=(-1)^m,
\]
because \((2/p)=-1\) precisely for \(p\equiv\pm3\pmod8\), and only odd exponents matter. Since \(5^m\) is \(1\pmod8\) for even \(m\) and \(5\pmod8\) for odd \(m\), this is exactly
\[
M_r(n)\equiv 3-2\left(\frac2n\right)\pmod8.
\]
The standard supplementary law \((2/n)=1\) exactly for \(n\equiv\pm1\pmod8\) yields the stated residue classification.

For the corollary, \(M_r(n)\) is a 2-adic unit, so if it equals \(c^t\) with \(t\) even then \(c\) is odd. Every even power of an odd integer is \(1\pmod8\). The theorem therefore rules out \(n\equiv\pm3\pmod8\). \(\square\)

## Relation to prior work

OEIS A140480 defines RMS numbers by the condition that \(\sqrt{\sigma_2(n)/\tau(n)}\) is integral. A comment by T. D. Noe, first dated July 6, 2008, records the empirical observation that the displayed RMS terms appeared to be \(\pm1\pmod8\); the entry was later amended to point to the separate even sequence A224988. The same A140480 entry, and A003601, record C. O. Zizka's 2008 generalization: a \(\sigma_r\)-number satisfies \(\sigma_r(n)/\tau(n)=c^r\).

The theorem above supplies a proof for the odd RMS case and, more generally, a complete mod-8 formula for the divisor \(r\)-th-power mean of every odd integer when \(r\) is even. It also treats the weaker perfect-power condition \(M_r(n)=c^t\) whenever \(t\) is even.

Oller-Marcén's 2012 paper *On arithmetic numbers* studies the \(r=1\) mean \(\sigma(n)/\tau(n)\), including prime-power and general integrality criteria. Its accessible full text was checked as adjacent divisor-mean literature; it does not supply the even-\(r\) mod-8 statement above.

To the best of our knowledge, searches for RMS numbers, quadratic means of divisors, \(\sigma_2(n)/\tau(n)\), \(\sigma_r\)-numbers, and mod-8 variants did not locate a published proof of the odd RMS observation or the general 2-adic congruence. The main residual originality risk is informal or poorly indexed sequence discussion, because the RMS terminology appears primarily in OEIS-style computational records rather than in a well-developed paper literature.

## Verification

`artifacts/verify_sigma_r_mod8.py` performs exact bounded checks without third-party libraries. For every odd \(n\le200000\) and each
\[
r\in\{2,4,6,8,10\},
\]
it computes \(\sigma_r(n)\) and \(\tau(n)\) from the prime factorization, cancels powers of \(2\), and compares the resulting 2-adic residue modulo \(8\) with the theorem. It checks 500,000 \((n,r)\) pairs and reports zero mismatches. It also directly tests the RMS condition for odd \(n\le200000\), finding 21 values, all congruent to \(1\) or \(7\pmod8\).

The computation is supporting evidence only; the theorem is proved for all odd \(n\) above.

## Limitations

- The congruence theorem is restricted to odd \(n\). Even RMS numbers exist, and their 2-adic structure is different.
- For \(r\equiv0\pmod4\), the mod-8 mean is always \(1\), so this argument gives no residue obstruction on \(n\).
- Originality is asserted only to the best of our knowledge. No specific inaccessible paper emerged as a concrete coverage risk, but informal sequence material may be incompletely indexed.

## References

1. OEIS A140480, “RMS numbers: numbers n such that root mean square of divisors of n is an integer.” https://oeis.org/A140480
2. OEIS A224988, “Even RMS numbers.” https://oeis.org/A224988
3. OEIS A003601, arithmetic numbers; includes the recorded \(\sigma_r\)-number generalization. https://oeis.org/A003601
4. A. M. Oller-Marcén, “On arithmetic numbers,” arXiv:1206.1823 (2012). https://arxiv.org/abs/1206.1823
