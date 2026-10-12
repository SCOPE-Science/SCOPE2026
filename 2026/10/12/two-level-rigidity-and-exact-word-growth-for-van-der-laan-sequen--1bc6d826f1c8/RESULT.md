# Two-level rigidity and exact word growth for Van der Laan sequences

## Finding

A *Van der Laan sequence* is a one-sided infinite sequence of nonnegative integers in which, in every block of four consecutive entries, the largest entry equals the sum of the two smallest entries, **counting repeated entries separately**.

**Theorem (complete two-level classification and complexity).** Fix integers \(0\le u<v\). Every Van der Laan sequence with entries in \(\{u,v\}\) belongs to precisely one of the following cases.

1. If \(u>0\), such a sequence exists if and only if \(v=2u\). In that case the sequence is admissible if and only if **every** length-four block has exactly two or three entries equal to \(u\). All these sequences use both values.
2. If \(u=0\), the only admissible sequences are the identically zero sequence and the four translates of the period-four sequence \((0,v,v,v,0,v,v,v,\ldots)\). Thus all nonconstant two-level sequences involving zero are periodic.

For \(u>0\) and \(v=2u\), let \(C_n\) be the number of length-\(n\) words in \(\{u,2u\}\) satisfying the four-term condition at every available window. Set \(C_0=1\); for \(0\le n\le3\) the condition is vacuous. Then
\[
\sum_{n\ge0}C_n z^n
=\frac{1+z+2z^2+3z^3-z^4-2z^6-2z^7+z^9}
{1-z-z^3-z^4+z^6}.
\]
In particular \(C_n=C_{n-1}+C_{n-3}+C_{n-4}-C_{n-6}\) for every \(n\ge10\), and
\[
\lim_{n\to\infty} C_n^{1/n}=\lambda,
\qquad \lambda=1.56361069559191\ldots,
\]
where \(\lambda\) is the unique Perron root of \(x^6-x^5-x^3-x^2+1\). The associated positive two-level shift has topological entropy \(\log\lambda=0.446997695276\ldots>0\), and therefore uncountably many nonperiodic sequences.

## Assumptions and scope

Every term is a nonnegative **integer** and the four-term condition is applied in the usual order-free way: sort the four terms as \(w_1\le w_2\le w_3\le w_4\), then require \(w_4=w_1+w_2\). There is no assumption of monotonicity or eventual periodicity. The classification concerns infinite sequences whose values are **contained** in a fixed two-element set; an admissible sequence need not use both symbols unless expressly stated. The word counts \(C_n\) concern all finite locally admissible words, including the short lengths with no complete four-term window.

## Proof

**Local rigidity.** In a block over \(\{u,v\}\), let \(j\in\{0,1,2,3,4\}\) be the number of occurrences of \(u\). If \(u>0\), the choices \(j=0\) and \(j=4\) give the impossible equations \(v=2v\) and \(u=2u\). The choice \(j=1\) gives \(v=u+v\), again impossible. For \(j=2\) or \(j=3\), the two smallest terms are both \(u\) and the largest is \(v\), so the condition is equivalent to \(v=2u\). Every admissible infinite sequence must contain at least one window, proving part 1 in both directions.

If \(u=0\), a direct examination shows that a four-block is admissible precisely when it contains either four zeros or exactly one zero. An all-zero window cannot coexist in the same infinite sequence with a window containing \(v\): as the window moves one place at a time, its number of zeros changes by at most one, and it cannot pass from four to one without a forbidden intermediate count of two or three. If all windows are zero, the sequence is constant zero. Otherwise, every window has exactly one zero. Define \(e_i\) to be \(1\) if the \(i\)-th term is zero and \(0\) otherwise. Subtracting \(e_i+e_{i+1}+e_{i+2}+e_{i+3}=1\) from the next window sum gives \(e_{i+4}=e_i\). The first four terms have exactly one zero, so there are exactly four possible phases, proving part 2.

**Transfer matrix.** For \(u>0\), encode the lower value \(u\) by the digit \(1\), and \(2u\) by \(0\). A length-four word is allowed precisely when it has either two or three ones. Use the three-bit suffix as the state. The complete directed transitions, written in lexicographic state order, are

```
000 -> (none)
001 -> 011
010 -> 101
011 -> 110, 111
100 -> 001
101 -> 010, 011
110 -> 100, 101
111 -> 110
```

Let \(M\) be the corresponding \(8\times8\) zero-one adjacency matrix, with \(M_{s,t}=1\) if the displayed edge \(s\to t\) exists. Then, for \(n\ge3\),
\[
C_n=\mathbf1^{\mathsf T}M^{n-3}\mathbf1,
\qquad C_0=1,\quad C_1=2,\quad C_2=4.
\]
Equivalently, treating \(z\) as a formal indeterminate,
\[
\sum_{n\ge0}C_nz^n
=1+2z+4z^2+z^3\mathbf1^{\mathsf T}(I-zM)^{-1}\mathbf1.
\]
Direct integer polynomial computation from the eight displayed rows gives
\[
\det(xI-M)=x(x+1)(x^6-x^5-x^3-x^2+1),
\quad
\det(I-zM)=(1+z)(1-z-z^3-z^4+z^6).
\]
Expanding the displayed finite matrix resolvent and canceling the factor \(1+z\) gives the asserted generating function. Its denominator yields the stated recurrence for indices beyond the numerator degree, namely \(n\ge10\). For orientation its initial coefficients are
\[
(C_n)_{n=0}^{17}=(1,2,4,8,10,16,25,39,61,95,149,233,364,569,890,1392,2176,3402).
\]

**Exponential growth and aperiodicity.** State \(000\) has no outgoing edge. The remaining seven states form a strongly connected directed graph; for instance, all are reachable from \(001\) and can return to \(001\), as is checked directly from the transition list. It contains the cycle \(011\to110\to101\to011\) of length three and the cycle \(001\to011\to110\to100\to001\) of length four. Thus its adjacency matrix is primitive (the period divides \(\gcd(3,4)=1\)). The Perron–Frobenius theorem supplies a unique strictly dominant positive eigenvalue \(\lambda\). Since the graph has distinct return cycles, \(\lambda>1\). The characteristic polynomial above then identifies \(\lambda\) with the claimed real root. Because the all-ones endpoint vectors are positive on the essential component, \(C_n\sim K\lambda^n\) for some \(K>0\), proving the limit and entropy formula. A finite-alphabet shift with positive entropy has uncountably many infinite admissible sequences, whereas periodic sequences are countable; thus uncountably many are aperiodic.

## Verification

Run `python3 verify.py` with the standard Python interpreter. The checker constructs the \(8\times8\) matrix directly from the allowed four-bit words; it independently enumerates every binary word through length 13, computes the characteristic polynomial with integer Newton identities, checks 120 exact generating-function coefficients, verifies graph connectivity and explicit cycles, checks the local two-value cases, and exhaustively verifies the zero-case classification for word lengths 4 through 11. Its output is stored in `verify_output.txt`. The determinant and generating-function assertions are finite symbolic polynomial identities independently reproducible from the eight displayed rows; the infinite classification and growth conclusions follow from the written proof, **not** from bounded experiments.

## Relationship to prior work

D. Nacin, *Van der Laan Sequences and a Conjecture on Padovan Numbers* (publicly issued December 30, 2022), introduces this condition and studies increasing and certain permutation-increasing solutions. That paper records the particular periodic example \((1,1,1,2)^\infty\), so existence of that individual sequence is not new. It does not give the two-symbol all-sequence classification, the zero-versus-positive rigidity dichotomy, or the entire finite-word counting function and entropy. The same periodic example appears in OEIS A177704; the Padovan background is in OEIS A000931. This theorem identifies the complete minimal positive alphabet subshift rather than a single special orbit. Its transfer-matrix calculation uses standard finite-type methods, not a claim of novelty for the method itself.

## Limitations

No classification is asserted for alphabets with three or more distinct positive values, general bounded value sets, or unbounded Van der Laan sequences. The given growth constant counts locally valid finite words for the special positive two-level alphabet, not all Van der Laan sequences or all Padovan-like sequences. The checked published sources did not contain the complete statement, but an unindexed equivalent finite-type enumeration remains a bibliographic possibility. The numerical checks are finite and do not replace the symbolic proof.

## References

1. D. Nacin, *Van der Laan Sequences and a Conjecture on Padovan Numbers*, Journal of Integer Sequences **26** (2023), Article 23.1.2; publicly issued December 30, 2022. https://cs.uwaterloo.ca/journals/JIS/VOL26/Nacin/nacin5.pdf
2. OEIS A177704, *Period 4: repeat [1, 1, 1, 2]*. https://oeis.org/A177704
3. OEIS A000931, *Padovan sequence*. https://oeis.org/A000931
