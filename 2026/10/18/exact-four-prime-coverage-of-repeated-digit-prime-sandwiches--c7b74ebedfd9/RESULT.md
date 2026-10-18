# Exact four-prime coverage of repeated-digit prime sandwiches

## Finding

Let \(R_m=(10^m-1)/9\). For each positive integer \(n\) of decimal length \(t\), each digit \(1\le d\le9\), and \(m\ge1\), form the repeated-digit sandwich
\[
F(d,m,n)=dR_m10^{t+m}+n10^m+dR_m.
\]
Let \(\mathcal C\) comprise the positive integers \(n\) for which **every** \(F(d,m,n)\) has a prime factor in the fixed set \(\{2,3,5,7,11,13\}\). Write \(L=3003=3\cdot7\cdot11\cdot13\).

**Exact classification.** An integer \(n\) belongs to \(\mathcal C\) if and only if either

* \(t\) is even and \(11\mid n\); or
* \(t\) is odd and the pair \((t\bmod6,n\bmod L)\) lies in
\[
\{(1,2499),(3,231),(3,420),(3,759),(5,651)\}.
\]

In particular, the part \(\mathcal E=\{n\in\mathcal C:t\text{ odd},\ 11\nmid n\}\) contains **exactly one residue class modulo \(L\) in each odd decimal length**: residues \(2499\), \(420\), and \(651\) for lengths congruent to \(1\), \(3\), and \(5\) modulo \(6\), respectively.

Define \(E(X)=\#\{n\le X:n\in\mathcal E\}\). Then
\[
\liminf_{X\to\infty}\frac{E(X)}X=\frac1{33033},\qquad
\limsup_{X\to\infty}\frac{E(X)}X=\frac{10}{33033},
\]
and \(\mathcal E\) has logarithmic density
\[
\lim_{X\to\infty}\frac1{\log X}\sum_{\substack{n\le X\\n\in\mathcal E}}\frac1n=\frac1{6006}.
\]
Thus a positive proportion in the lower-density sense of decimal integers are certified to have **no prime sandwich** even after excluding the previously known even-length divisibility-by-\(11\) obstruction.

## Assumptions and scope

All decimal lengths are those of standard base-ten expansions, with no leading zero. The digit \(d\) lies in \(\{1,\ldots,9\}\), and the same positive number \(m\) of repeated copies is placed on both sides. This result classifies the **fixed small-prime covering certificate** \(\mathcal C\), not every core for which all sandwiches are composite. The four nontrivial covering primes \(3,7,11,13\) divide the six-digit repunit \(R_6=3\cdot7\cdot11\cdot13\cdot37\); the additional primes \(2,5\) handle the terminal digit. The four primes \(3,7,11,13\) are irredundant for certifying the original core \(231\) using factors of \(R_6\): the sandwiches at \((d,m)=(1,3),(7,1),(1,2),(1,1)\), respectively, have greatest common divisor with \(R_6\) equal to \(3,7,11,13\).

## Proof

**1. Reduction to a finite modular test.** The last decimal digit of \(F(d,m,n)\) is \(d\). For even \(d\) the sandwich is divisible by \(2\), and for \(d=5\) it is divisible by \(5\). It therefore suffices to consider the four remaining digits \(D=\{1,3,7,9\}\) and primes \(P=\{3,7,11,13\}\).

Every prime in \(P\) divides \(R_6=111111\) and is coprime to \(10\). From
\[
R_{m+6}=R_m+10^mR_6
\]
and \(10^6\equiv1\pmod p\), the residue of \(F(d,m,n)\) modulo any \(p\in P\) depends only on \(d\), \(m\bmod6\), \(t\bmod6\), and \(n\bmod p\). Consequently the universal quantifier over \(m\ge1\) reduces exactly, not approximately, to \(m\in\{1,2,3,4,5,6\}\). The four simultaneous prime tests depend only on \(n\bmod L\).

**2. Exact complete residue classification.** For \(0\le j<6\), let \(C_j\subseteq\{0,\ldots,3002\}\) contain exactly those \(r\) for which all \(24\) pairs \((d,m)\in D\times\{1,\ldots,6\}\) satisfy
\[
\prod_{p\in P}\mathbf 1_{p\nmid F(d,m,r)}=0
\quad\text{with }t\equiv j\pmod6.
\]
The exhaustive finite evaluation gives the complete table

| \(j=t\bmod6\) | \(C_j\) | Cardinality |
|---|---|---:|
| \(0\) | All \(r\equiv0\pmod{11}\) | 273 |
| \(1\) | \(\{2499\}\) | 1 |
| \(2\) | All \(r\equiv0\pmod{11}\) | 273 |
| \(3\) | \(\{231,420,759\}\) | 3 |
| \(4\) | All \(r\equiv0\pmod{11}\) | 273 |
| \(5\) | \(\{651\}\) | 1 |

Here is fully specified arithmetic sufficient to reproduce *every* table entry, including all exclusions: enumerate \(j\in\{0,\ldots,5\}\), \(r\in\{0,\ldots,L-1\}\), \(d\in D\), and \(m\in\{1,\ldots,6\}\); for each \((j,r)\), retain it if and only if each \((d,m)\) has at least one zero residue modulo \(P\). For \(j=0\), take exponent \(t=6\) in the displayed integer expression; otherwise take \(t=j\). No test relies on a bounded range of *core integers* or on probabilistic primality. The standalone `check.py` executes this complete enumeration using exact integers. It also independently builds four local \(24\)-bit divisibility masks modulo the individual primes and combines them using the Chinese remainder theorem. Both methods give the displayed table. The earlier periodicity proof elevates the finite table to all positive lengths and padding sizes.

**3. Density.** Each odd digit length \(t\) has exactly one allowed class modulo \(L\) in \(\mathcal E\). Therefore its number of eligible integers equals
\[
\frac{9\cdot10^{t-1}}L+O(1),
\]
with an absolute error bounded independently of \(t\); no even digit length contributes. Summing over odd lengths gives
\[
E(10^{2k})=\frac{10^{2k}}{11L}+O(k),\qquad
E(10^{2k+1})=\frac{10^{2k+2}}{11L}+O(k).
\]
Inside an odd-length block the count increases with asymptotic slope \(1/L\), which is greater than its initial ratio to \(X\), while inside the following even-length block the count remains fixed. Uniform errors of order \(O(\log X)\) show that the asymptotic minimum and maximum proportions occur at the two displayed endpoint sequences. This yields the stated liminf and limsup. Finally the harmonic sum from one residue class in each odd-digit interval is \((\log 10)/L+O(10^{-t})\), so averaging over the lengths gives logarithmic density \(1/(2L)=1/6006\).

Every \(F(d,m,n)\) with \(n\in\mathcal C\) has at least three decimal digits, hence exceeds \(13\). Its certified prime factor is therefore proper, and it is composite.

## Verification

Run `python3 check.py` using only the Python standard library. The first independent implementation checks all \(6\cdot3003\cdot24=432432\) residue/position combinations via the integer expression for the sandwich. The second implementation constructs local divisibility bitmasks by modular recurrences and compares its complete six-row residue spectrum with the first. It also verifies that \(3,7,11,13\) are each necessary to cover the core \(231\) using prime factors of \(R_6\). Both procedures terminate and assert the exact table and the three exceptional non-\(11\) classes. The density step is an analytic consequence of the exact classification and requires no finite numerical approximation.

## Relationship to prior work

Chai Wah Wu, *On a conjecture regarding primality of numbers constructed from prepending and appending identical digits* (2015), introduced the repeated-digit sandwich operation, proved that even-digit-length cores divisible by \(11\) yield only composite sandwiches, exhibited individual exceptions such as \(231,420,759\), and developed a general finite-repunit gcd covering **sufficient test**. Those contributions are prior results, not new claims here. The present theorem **evaluates a specific irredundant four-prime covering spectrum completely for all core lengths**, including new explicit arithmetic progressions among odd-digit cores not divisible by \(11\), and derives sharp natural-density extremal constants and the logarithmic density. The OEIS A090287 notes the original problem and Wu's examples; its prime-search data are not used as proof. The existence of Wu's general covering test alone should not be mistaken for a published complete residue classification or density computation; equivalence with any differently formulated prior classification remains an originality risk.

## Limitations

The classification is of the explicitly defined small-prime certificate, not of all cores with no prime sandwich; a core outside \(\mathcal C\) may still yield only composites, perhaps for reasons involving primes larger than \(13\). No assertion of infinitely many prime sandwiches for such cores is made. The density constants apply to the certified non-\(11\), odd-digit subfamily, not to the unknown full exceptional set. Originality is subject to literature coverage outside the inspected sources, and no independent audit has been conducted.

## References

1. Chai Wah Wu, *On a conjecture regarding primality of numbers constructed from prepending and appending identical digits*, arXiv:1503.08883, first submitted 2015-03-31, https://arxiv.org/abs/1503.08883.
2. OEIS A090287, *Smallest prime obtained by sandwiching n between a number with identical digits*, original sequence author dated 2003-11-29; https://oeis.org/A090287 (original-sequence problem and published examples).
