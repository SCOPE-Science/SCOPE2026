# Exact transition-refined census of periodic binary antisquare-avoiding words

## Finding
For a binary word \(w=w_0\cdots w_{n-1}\) of length \(n\ge1\), write \(w^{\mathbb Z}\) for its two-sided periodic extension. Call \(w\) *periodically good* when the only antisquares occurring as contiguous factors of \(w^{\mathbb Z}\) are the two length-two words `01` and `10`. An antisquare is a word \(v\overline v\), where the bar complements every binary symbol. Define \(c_{n,t}\) as the number of indexed length-\(n\) binary words that are periodically good and have exactly \(t\) cyclic changes \(w_i\ne w_{i+1\bmod n}\).

The complete transition-refined census is

\[
\boxed{\displaystyle
\sum_{n\ge1}\sum_{t\ge0}c_{n,t}z^nu^t
= -2z\,\partial_z\log(1-z-u^2z^4-u^4z^6)
=\frac{2z(1+4u^2z^3+6u^4z^5)}{1-z-u^2z^4-u^4z^6}.}
\]

In particular \(c_{n,0}=2\) and \(c_{n,t}=0\) for odd \(t\). For positive even \(t\), the explicit finite formula is

\[
\boxed{\displaystyle c_{n,t}=2n\!\!\sum_{\substack{r\ge1,\;0\le s\le r\\t=2r+2s,\;n\ge t+2r}}
\frac1r\binom rs\binom{n-t-r-1}{r-1}.}
\]

At \(u=1\), let \(g_n=\sum_t c_{n,t}\). Then

\[
\sum_{n\ge1}g_nz^n=\frac{2z(1+4z^3+6z^5)}{1-z-z^4-z^6},
\]

so \(g_1,\ldots,g_{16}\) are \(2,2,2,10,12,26,30,42,56,92,134,202,288,422,612,906\), and \(g_n=g_{n-1}+g_{n-4}+g_{n-6}\) for \(n\ge7\). The number of aperiodic cyclic rotation classes of circumference \(n\) is exactly

\[
\boxed{\displaystyle a_n=\frac1n\sum_{d\mid n}\mu(d)g_{n/d},}
\]

with \(\mu\) the classical Möbius function; all rotation classes, including imprimitive ones, number \(\frac1n\sum_{d\mid n}\varphi(d)g_{n/d}\). If \(\psi>1\) is the real root of \(\psi^3=\psi^2+1\), then \(g_n=2\psi^n+O(1)\) and \(a_n\sim 2\psi^n/n\).

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\); source positions are indexed, so rotations are counted separately in \(g_n\) and \(c_{n,t}\). The avoidance condition applies to the entire **two-sided infinite periodic extension**, not merely to factors shorter than the displayed finite word. The cyclic change count compares the last and first symbols too. The empty word is excluded. Source-level avoidance of antisquares of order one is not required.

The result uses two published structural facts about *good* infinite binary words from Baranwal--Currie--Mol--Ochem--Rampersad--Shallit [1]: (i) their Theorem 11 classifies all minimal forbidden antisquares, and (ii) their Proposition 18 shows that a bi-infinite good word containing `001011` has a nonperiodic one-defect form. Reversal and complementation cover `110100`. Neither external fact is asserted as a new result here.

## Proof
**1. An infinite forbidden language becomes a finite-type condition on periodic points.** The minimal antisquares of order two are `0011`, `0110`, `1001`, `1100`; those of order three are `010101`, `101010`. Every larger minimal antisquare contains `001011` or `110100` [1, Theorem 11]. Thus every periodic word avoiding the eight factors

`0011, 0110, 1001, 1100, 010101, 101010, 001011, 110100`

is good. Conversely, a periodically good word already avoids the first six, while [1, Proposition 18] and symmetry exclude the last two: their presence in a good bi-infinite word forces an eventually constant/alternating one-defect arrangement, which cannot be periodic and contain the triggering factor. Therefore these eight forbidden factors are a necessary and sufficient criterion for periodically good words, irrespective of circumference.

**2. A cyclic difference map makes parity automatic.** Write \(p_i=1\) if \(w_i\ne w_{i+1\bmod n}\) and \(p_i=0\) otherwise. The eight factors above induce exactly the four forbidden patterns

`010, 101, 11111, 01110`

in the cyclic difference word \(p\): this follows directly by taking consecutive exclusive-or differences. Conversely, any occurrence of one of these four patterns lifts to one of the eight original forbidden factors (with its bitwise complement). The forbidden-pattern assertion holds also for small \(n\), since it is interpreted in the periodic extension, with repetitions allowed across a wrap.

If \(p\) contains a `1`, absence of `010` and `101` forces every circular zero-run and one-run to have length at least two. Absence of `11111` bounds every one-run by four, and absence of `01110` forbids one-run length three. Thus all one-runs have length either two or four; all zero-runs have length at least two. The exceptional permitted difference word is all zeros. This proves that every permitted difference word contains an even number of `1` symbols. Consequently it closes around the circle and lifts to **exactly two** indexed binary words, obtained from either choice of \(w_0\). The number of cyclic changes in either lift equals the number of ones in \(p\).

**3. Count marked cyclic runs.** For any permitted nonzero difference word, choose a start of a one-run. Its circular runs decompose into \(r\ge1\) successive blocks, each consisting of a zero-run of length at least two followed by a one-run of length two or four. With \(z\) marking circumference and \(u\) marking changes, the generating function of one block is

\[
B(z,u)=\frac{z^2}{1-z}(u^2z^2+u^4z^4).
\]

An ordered list of \(r\) such blocks contributes \(B(z,u)^r\). Among all indexings of a circular word there are \(n\) possible choices of the position labeled zero but exactly \(r\) starts of one-runs, so the standard double count of pairs (indexed word, marked one-run) contributes the factor \(n/r\). This factor remains correct for periodic tuples with rotational stabilizers because markings, not orbit representatives, are counted. There are two binary lifts. The all-zero difference word contributes two constant source words for each \(n\ge1\). Hence

\[
\begin{aligned}
F(z,u)&=\frac{2z}{1-z}
+2\sum_{r\ge1}\sum_{n\ge1}\frac nr[z^n]B(z,u)^r\,z^n\\
&=\frac{2z}{1-z}-2z\,\partial_z\log(1-B(z,u))\\
&=-2z\,\partial_z\log(1-z-u^2z^4-u^4z^6),
\end{aligned}
\]

where the last identity uses \(1-B=(1-z-u^2z^4-u^4z^6)/(1-z)\). Differentiation gives the stated rational function. Extracting \(u^t z^n\) after expanding \(B^r\), choosing \(s\) four-one-runs and distributing the nonmandatory zeros over \(r\) zero-runs, gives the binomial sum exactly.

**4. Cyclic classes and growth.** Rotation preserves periodic goodness. Möbius inversion of \(g_n=\sum_{d\mid n}d a_d\) yields the primitive-necklace formula, and Burnside's lemma gives the all-necklace count. At \(u=1\), the denominator factors as

\[
1-z-z^4-z^6=(1+z^3)(1-z-z^3).
\]

Its reciprocal roots consist of the unique positive root \(\psi>1\) of \(\lambda^3-\lambda^2-1\), two cubic conjugates of modulus \(\psi^{-1/2}<1\), and three unit-modulus roots coming from \(1+z^3\). The logarithmic derivative therefore gives \(g_n=2\psi^n+O(1)\). The proper divisors in Möbius inversion contribute exponentially less, proving \(a_n\sim2\psi^n/n\).

## Verification
Execute `python3 verify_cyclic_good.py` in the same directory. The script independently checks (a) the full periodic antisquare definition against the four-pattern difference criterion for all \(65{,}534\) binary source words of lengths \(1\) through \(15\), (b) the exact transition histogram against the rational recurrence, (c) a separate sixteen-state closed-walk transfer computation through length \(60\), and (d) the binomial-coefficient formula against the rational recurrence through length \(120\). The expected success line is:

`CYCLIC_ANTISQUARE_PASS exhaustive_n=1..15 test_words=65534 trace_n=1..60 rational_and_formula_n=1..120`

These finite checks are consistency tests; the all-length proof is the run decomposition and cyclic marking argument above.

## Relationship to prior work
Baranwal et al. [1] introduce good binary words, classify the infinite minimal antisquare basis, prove the key exceptional-factor rigidity, and determine the exponential growth rate of ordinary **linear** good words. The periodic-point bivariate transition census, exact circumference sequence and primitive-necklace formulas above are not stated in the inspected sections of [1]. The proof deliberately uses those foundational structural results rather than claiming a new forbidden-basis classification. The same-paper ingredients make a derivation conceivable; the contribution lies in the exact cyclic and marked-run formulas and the separate all-period spectral constant. The related complement-avoidance paper [2] imposes a distinct condition (avoiding complementary factors in arbitrary positions) and does not yield this antisquare census.

## Limitations
The result concerns infinite periodic extensions; arbitrary finite good words, eventually periodic one-sided words, and more general alphabets are not counted. It does not solve the nonperiodic linear-word counting problem beyond the published results. The literature comparison is not an exhaustive theorem-prover search, and an independently published equivalent symbolic-dynamics formulation may exist. No claim of independent audit or external certification is made.

## References
[1] A. Baranwal, J. Currie, L. Mol, P. Ochem, N. Rampersad, and J. Shallit, *Antisquares and Critical Exponents*, arXiv:2209.09223, first publicly posted 19 September 2022; DMTCS 25:2 (2023), especially Theorem 11, Proposition 18 and Theorem 19. https://arxiv.org/html/2209.09223v3

[2] J. Currie, L. Dvořáková, P. Ochem, D. Opočenská, N. Rampersad and J. Shallit, *Complement Avoidance in Binary Words*, arXiv:2209.09598, 2022, especially introduction and the distinctions among complement-avoidance conditions. https://arxiv.org/html/2209.09598v2
