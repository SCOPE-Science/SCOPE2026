# Sharp 2-adic preperiods for the Bala sequence A158690

## Finding

Define the integer sequence \(a(n)\), for \(n\ge0\), by
\[
 \sum_{n\ge0}a(n)\frac{t^n}{n!}=1+\sum_{m\ge1}\prod_{i=1}^{m}(1-e^{-(2i-1)t}).
\]
For every integer \(e\ge2\), the smallest index \(s_e\ge0\) at which the residue sequence \((a(n)\bmod 2^e)_{n\ge s_e}\) is periodic is **exactly**
\[
 \boxed{s_e=e}.
\]
The sharp obstruction is explicit. Write \(L_e=\lambda(2^e)\) for the Carmichael exponent (\(L_2=2\), \(L_e=2^{e-2}\) for \(e\ge3\)). Then
\[
 a(n+L_e)\equiv a(n)\pmod{2^e}\qquad(n\ge e),
\]
but at the immediately preceding index,
\[
 \boxed{a(e-1+L_e)-a(e-1)\equiv2^{e-1}\pmod{2^e}}.
\]
Modulo \(2\), every \(a(n)\) is \(1\), and \(s_1=0\).

The claim is **optimal onset**, not minimal eventual period. The general existence of the Carmichael eventual period, including the upper starting index \(e\), was established earlier. A previously obtained stronger least-period theorem for powers \(2^e\) with \(e\ge5\) is also not claimed here as new. This finding supplies the missing global lower bound on when *any* periodic tail can begin.

## Assumptions and scope

All exponential identities are formal power series over the integers or rationals as appropriate. The index \(n\) runs over nonnegative integers; powers \(2^e\) have exponent \(e\ge1\). A periodic tail beginning at \(s\) means there exists some positive integer \(P\) such that \(a(n+P)\equiv a(n)\pmod{2^e}\) for every \(n\ge s\). No assumption is made that the putative period \(P\) equals the Carmichael exponent.

Set \(y=e^t-1\) and
\[
 G(y)=1+\sum_{m\ge1}\prod_{i=1}^{m}(1-(1+y)^{-(2i-1)})=\sum_{k\ge0}g_ky^k.
\]
The infinite sum belongs to \(\mathbb Z[[y]]\): each factor is divisible by \(y\), so coefficients are finite sums of integers. Direct expansion through degree three gives
\[
 g_0=1,\quad g_1=1,\quad g_2=2,\quad g_3=7.
\]

## Proof

**1. A finite power-spectrum identity.** The Stirling-number transform gives, for every nonnegative integer \(n\),
\[
 a(n)=\sum_{k=0}^n g_k\,k!\left\{\begin{matrix}n\\k\end{matrix}\right\}.
\]
Fix \(e\ge2\) and let \(K\) be the least positive integer with \(2^e\mid K!\). Since \(2^e\mid k!\) for all \(k\ge K\), the inclusion–exclusion identity for Stirling numbers yields, whenever \(n\ge1\),
\[
 a(n)\equiv\sum_{j=1}^{K-1}c_jj^n\pmod{2^e},\qquad
 c_j=\sum_{k=j}^{K-1}(-1)^{k-j}\binom{k}{j}g_k.
\]
No infinite interchange is involved after reduction: this is a finite identity modulo \(2^e\), with all coefficients integral.

**2. An eventual period beginning at \(e\).** Take \(L_e=\lambda(2^e)\). For every odd integer \(j\), Carmichael's exponent theorem gives \(j^{L_e}\equiv1\pmod{2^e}\). For each even integer \(j\), both \(j^n\) and \(j^{n+L_e}\) vanish modulo \(2^e\) as soon as \(n\ge e\). Thus
\[
 a(n+L_e)\equiv a(n)\pmod{2^e}\quad\text{for all }n\ge e.
\]
This agrees with the earlier general Stirling-transform periodicity theorem, and records the upper bound needed here.

**3. A universal obstruction one place earlier.** Put \(n=e-1\ge1\). Contributions from odd \(j\) cancel modulo \(2^e\). The terms divisible by four vanish because \(n\ge e-1\ge1\) and \(4^{e-1}\) is divisible by \(2^e\) for \(e\ge2\). For \(j\equiv2\pmod4\), \(j^{e-1}\equiv2^{e-1}\pmod{2^e}\) and \(j^{L_e}-1\) is odd. Therefore
\[
 a(e-1+L_e)-a(e-1)\equiv
 2^{e-1}\sum_{j\equiv2\pmod4}c_j\pmod{2^e}.
\]
Only the parity of the indicated sum is needed. By finite binomial inversion,
\[
 \sum_{j\equiv2\pmod4}c_j\equiv
 \sum_{k=0}^{K-1}g_k\sum_{j\equiv2\pmod4}\binom{k}{j}\pmod2.
\]
The inner sum is \(1\) exactly when \(k\in\{2,3\}\), and is \(0\) otherwise: in characteristic two, \(j\equiv2\pmod4\) forces the second binary digit of \(j\) to be one and the first zero; Lucas's parity criterion shows that all available higher binary-digit choices cancel in pairs unless \(k\) has no higher set bits. Equivalently, the period-four indicator has fourth forward difference zero modulo two, with initial differences \(0,0,1,1\). Consequently,
\[
 \sum_{j\equiv2\pmod4}c_j\equiv g_2+g_3\equiv2+7\equiv1\pmod2.
\]
This proves the exact claimed \(2^{e-1}\) obstruction.

**4. The least preperiod, independent of a choice of period.** Suppose a periodic tail began at some \(s\le e-1\), with period \(Q\). It would then also be periodic from \(e\) onward. The genuinely least period \(d\) of that tail from \(e\) divides both \(Q\) and \(L_e\) (a periodic one-sided infinite word admits this standard gcd property). The indices \(e-1+Q\) and \(e-1+L_e\) are both at least \(e\), so their residues coincide. Periodicity from \(s\) also equates \(a(e-1+Q)\) and \(a(e-1)\), contradicting Step 3. Hence no tail starts earlier than \(e\). Combined with Step 2 this proves \(s_e=e\).

For \(e=1\), every \(g_k\) contributes an integer Stirling term, and the direct binary expansion (or the finite power spectrum modulo \(2\)) shows \(a(n)\equiv1\pmod2\) for every \(n\ge0\), so \(s_1=0\). In detail, modulo two the threshold is \(K=2\), yielding \(a(n)\equiv g_1=1\) for all \(n\ge1\), while \(a(0)=1\).

## Verification

The standalone `verification/verify.py` performs independent integral expansions of the initial exponential generating function, exact Stirling-transform comparisons, and exhaustive checks of the finite periodic-indicator difference certificates. It confirms the sharp obstruction and periodicity for exponents \(2\le e\le12\), including the small powers and boundary residues. Its recorded execution is in `verification/output.txt`. These finite tests verify computation-sensitive ingredients; the proof above supplies the quantifiers over every \(e\ge2\).

## Relationship to prior work

Danesh (26 August 2026) and Kallat (7 September 2026) established eventual modular periodicity with Carmichael periods for the sequence, using the same integral Stirling-transform representation. Kallat's full seven-page arXiv preprint, Proposition 2.1 and Remark 2.2, proves the upper starting bound \(n\ge e\) for modulus \(2^e\) but expressly does not assert its sharpness; its application and concluding remarks likewise do not provide a lower-onset theorem. The OEIS entry records one isolated period/preperiod example modulo \(16\). The least eventual period for large powers of two was separately established earlier; this note neither redistributes nor reclaims that result. The new statement is the uniform **necessity** of starting at \(e\), certified by the residue obstruction at \(e-1\), across the entire two-power family.

## Limitations

The finding addresses the preperiod only, not all least period lengths, odd-prime powers, or arbitrary moduli. The accessible abstract of Danesh's 2026 preprint gives no sharp preperiod comparison, but its full manuscript was not materially inspected; an implicit equivalent statement there remains a residual originality risk. Kallat's complete arXiv preprint was inspected. Independent audit has not been performed.

## References

- Payam Danesh, *Eventual periodicity of weighted Stirling transforms and two conjectures of Bala*, Cambridge Open Engage, first posted 2026-08-26, DOI: 10.33774/coe-2026-4d6jr.
- Ahaan Kallat, *A Proof of Bala's Congruence Conjectures for A158690*, arXiv:2609.07238, first posted 2026-09-07, especially Proposition 2.1, Remark 2.2, and Sections 3–4.
- The On-Line Encyclopedia of Integer Sequences, entry A158690, https://oeis.org/A158690 (including Bala's 2021 conjectures and the isolated modulus-16 example).
