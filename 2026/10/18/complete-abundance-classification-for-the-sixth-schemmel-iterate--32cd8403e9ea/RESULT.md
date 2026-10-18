# Complete abundance classification for the sixth Schemmel iterate sum on prime powers

## Finding

For every prime \(p\) and every integer \(a\geq1\), the prime power \(p^a\) is abundant with respect to Defant's sixth Schemmel iterate sum precisely when
\[
 (p=19\ \text{and}\ a=1)\quad\text{or}\quad
 (p\geq23,\ p\ne83,\ \gcd(p-6,15)=1).
\]
Every other prime power is strictly deficient; there are no perfect prime powers for this iterate sum. In particular, \(D_6(19)=21>19\), whereas \(D_6(19^a)<19^a\) for every \(a\geq2\). The prime \(83\) is the unique prime at least \(23\) with \(\gcd(p-6,15)=1\) that fails abundance.

## Assumptions and scope

For positive integers \(n\), define the sixth Schemmel totient \(L_6(1)=1\) and, for \(n>1\),
\[
 L_6(n)=\begin{cases}
 0,&\text{if some prime }q\leq6\text{ divides }n,\\
 \displaystyle\prod_{q^b\parallel n}q^{b-1}(q-6),&\text{otherwise}.
 \end{cases}
\]
Set \(L_6(0)=0\). For \(n>1\), iterate \(n_0=n\), \(n_{j+1}=L_6(n_j)\), stopping at the first \(n_r\in\{0,1\}\). Define \(D_6(n)=\sum_{j=1}^r n_j\) and \(D_6(1)=0\). Since \(0\leq L_6(n)<n\) for \(n>1\), termination is guaranteed. The terms *abundant*, *deficient*, and *perfect* mean, respectively, \(D_6(n)>n\), \(D_6(n)<n\), and \(D_6(n)=n\). All quantified prime powers, including small primes and all exponents, are covered. This classification makes no claim for integers with two or more distinct prime factors.

## Proof

**Step 1 (immediate deficiency).** For \(p\leq5\), \(L_6(p^a)=0\), hence \(D_6(p^a)=0<p^a\). For \(p>6\), write \(t=p-6\). Then
\[
 L_6(p^a)=t p^{a-1}.
\]
If \(3\mid t\) or \(5\mid t\), this first iterate contains a prime at most \(6\); its next iterate vanishes. Thus \(D_6(p^a)=t p^{a-1}<p^a\) for every \(a\geq1\).

**Step 2 (the small primes).** If \(p=7\), successive positive iterates are \(7^{a-1},7^{a-2},\ldots,7,1\), so
\[
 D_6(7^a)=\frac{7^a-1}{6}<7^a.
\]
If \(p=13\), the iterates are \(7\cdot13^{a-1},7\cdot13^{a-2},\ldots,7,1\), giving
\[
 D_6(13^a)=\frac{7\cdot13^a+5}{12}<13^a.
\]
At \(p=17\), one has \(17\mapsto11\mapsto5\mapsto0\), so \(D_6(17)=16<17\). For \(a\geq2\), the positive iterates are precisely \(11\cdot17^{a-1}\) and \(55\cdot17^{a-2}\). Therefore
\[
 D_6(17^a)=11\cdot17^{a-1}+55\cdot17^{a-2}<17^a
\]
because \(11\cdot17+55=242<289=17^2\).

At \(p=19\), the successive factors \(19\mapsto13\mapsto7\mapsto1\) yield, for every \(a\geq1\),
\[
 D_6(19^a)=13\cdot19^{a-1}+91\sum_{j=0}^{a-2}19^j+8
 =\frac{325\cdot19^{a-1}+53}{18},
\]
with an empty sum interpreted as \(0\). Thus
\[
 D_6(19^a)-19^a=\frac{53-17\cdot19^{a-1}}{18},
\]
which is positive exactly for \(a=1\). These cases exhaust primes below \(23\) not already covered by the preceding divisibility test.

**Step 3 (a rough-cofactor lemma).** Suppose \(p\geq23\) and \(\gcd(p-6,15)=1\); put \(t=p-6\geq17\). As \(t\) is odd and has no factor \(3\) or \(5\), all its prime factors are at least \(7\). If \(h=L_6(t)<7\), the product formula implies that every prime factor of \(t\) belongs to \(\{7,11\}\). Each factor \(7\) contributes \(1\) and each factor \(11\) contributes \(5\), but any repeated factor of \(7\) or \(11\) contributes at least \(7\) or \(11\), respectively, through its prime-power factor. Therefore \(L_6(t)<7\) occurs only for \(t\in\{1,7,11,77\}\). Since \(t\geq17\), this forces \(t=77\), or \(p=83\). Hence \(h\geq7\) for every admissible \(p\geq23\) other than \(83\).

**Step 4 (the uniform abundance inequality).** For \(t\geq37\), the lemma gives
\[
 t h\geq7t>6(t+6)=6p.
\]
For \(17\leq t<37\), any positive integer all of whose prime factors are at least \(7\) must be prime: its least possible composite value is \(49\). Therefore \(h=t-6\), and
\[
 t h=t(t-6)>6(t+6)=6p
\]
(the last inequality already holds for \(t\geq17\)). Thus \(t h>6p\) in every admissible nonexceptional case. If \(a=1\), the first two iterates of \(p\) are \(t,h\), giving \(D_6(p)\geq t+h>p\); indeed the displayed bound \(th>6p\) implies \(h>6p/t>6\). If \(a\geq2\), coprimality of \(p\) and \(t\), plus multiplicativity, gives
\[
 L_6(p^a)+L_6^{(2)}(p^a)
 =p^{a-1}t+p^{a-2}t h
 =p^{a-2}t(p+h).
\]
By \(th>6p\), this is larger than \(p^{a-1}(t+6)=p^a\). All remaining iterates are nonnegative, proving abundance.

**Step 5 (the isolated exceptional prime).** For \(p=83\), \(t=77=7\cdot11\) and \(L_6(77)=5\). Hence \(83\mapsto77\mapsto5\mapsto0\), giving \(D_6(83)=82<83\). For \(a\geq2\), the first two iterates are \(77\cdot83^{a-1}\) and \(385\cdot83^{a-2}\); the next contains the factor \(5\) and maps to zero. Consequently,
\[
 D_6(83^a)=77\cdot83^{a-1}+385\cdot83^{a-2}
 =83^a-113\cdot83^{a-2}<83^a.
\]
All cases are strict; in particular no equality case exists. This completes the classification.

## Verification

The standalone checker `verify_prime_powers.py` uses exact integer factorization and iteration, independently of the classification proof. Run `python3 verify_prime_powers.py` from a directory containing the checker. It tests every prime \(p\leq1000\) and each integer exponent \(1\leq a\leq8\), checks the exceptional formulas to larger exponents, and asserts absence of equality within that finite range. The exact test yields \(1344\) prime powers: \(961\) abundant, \(383\) deficient, no perfect powers. These finite checks corroborate but do not establish the universal proof above.

## Relationship to prior work

The definition follows Colin Defant, *On Arithmetic Functions Related to Iterates of the Schemmel Totient Functions*, *Journal of Integer Sequences* **18** (2015), Article 15.2.1, particularly Definition 12 and Theorem 18. Theorem 18 proves the existence of infinitely many primes whose every positive power is abundant for every even Schemmel parameter; its proof uses a coarse two-iterate inequality. It does **not** provide an exact classification of all primes for the sixth parameter, nor isolate the prime \(19\) with an abundance-to-deficiency transition or the exceptional prime \(83\). The present proof provides a sharp complete natural slice using a bound for rough cofactors. Defant's separate work on *sparsely Schemmel totient numbers* concerns one-step extremal values, not iterate-sum abundance; his work on terminal iterates concerns a different function. OEIS A241667 and A241668 record summatory trajectories for parameters two and four, respectively, not the sixth-parameter prime-power classification.

## Limitations

This result classifies only prime powers for the sixth Schemmel parameter; it says nothing about arbitrary composite supports or other parameters. The threshold is specific to the sixth parameter. The integer checker is finite corroboration rather than an infinite proof. The literature comparison covers the named primary sources and related tables but cannot exclude every unpublished or unindexed independent discovery. 
## References

1. Colin Defant, "On Arithmetic Functions Related to Iterates of the Schemmel Totient Functions," *Journal of Integer Sequences* **18** (2015), Article 15.2.1, https://www.maths.tcd.ie/EMIS/journals/JIS/VOL18/Defant/defant5.pdf ; first public journal date January 13, 2015, https://www.maths.tcd.ie/EMIS/journals/JIS/VOL18/Defant/defant5.html .
2. Colin Defant, "On Sparsely Schemmel Totient Numbers," arXiv:1412.3080v1 (December 9, 2014), https://arxiv.org/html/1412.3080v1 .
3. Colin Defant, "A Note about Iterated Arithmetic Functions," arXiv:1501.06075v1 (January 24, 2015), https://arxiv.org/html/1501.06075v1 .
4. OEIS A241667 and A241668, https://oeis.org/A241667 and https://oeis.org/A241668 . The earliest verified public indexed iterate-sum source inspected was the May 10, 2014 approval of A241668: https://oeis.org/history?seq=A241668 .
