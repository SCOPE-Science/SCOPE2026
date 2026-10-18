# Six-level singular-minor incidence for the order-ten Fourier matrix

## Finding

Let \(\zeta=\exp(2\pi i/10)\) and \(F=(\zeta^{rc})_{0\le r,c<10}\). For every four-element row set \(R\subset\mathbb Z_{10}\), define its singular-column degree
\[
d(R)=\#\{C\subset\mathbb Z_{10}: |C|=4,\ \det F[R,C]=0\}.
\]
Among the \(\binom{10}{4}=210\) row sets, the **complete degree distribution** is
\[
\begin{array}{c|rrrrrr}
d(R)&0&10&20&30&110&130\\ \hline
\#R&20&100&50&20&10&10
\end{array}.
\]
No other singular-column degrees occur. Consequently exactly \(5000\) of the \(210^2=44100\) ordered row/column four-subset pairs determine singular four-by-four minors, so the exact uniform incidence probability is \(50/441\). Here ordered means the pair \((R,C)\) is distinguished from \((C,R)\), while entries within each set are naturally in increasing order.

## Assumptions and scope

All indices lie in \(\{0,1,\ldots,9\}\), and both row and column selections are four-element subsets with no repetition. Determinants are computed over the complex numbers; the Fourier matrix is unnormalized, which does not affect vanishing. The degree refers to all column choices for a *fixed* row set, and the frequency-zero incidence count counts both coordinates of each pair. The result is finite and exhaustive only at Fourier order ten and minor size four.

## Proof

**Exact cyclotomic arithmetic.** The minimal polynomial of a primitive tenth root is \(\Phi_{10}(z)=z^4-z^3+z^2-z+1\). Consequently every \(z^k\), for \(0\le k<10\), has a unique representative in the basis \(1,z,z^2,z^3\) of \(\mathbb Q[z]/(\Phi_{10})\). Multiplication by \(z\) acts on coefficient vectors by
\[
(a,b,c,d)\longmapsto(-d,a+d,b-d,c+d).
\]
The starting vector \((1,0,0,0)\) therefore gives all ten powers exactly. For each increasing four-subset pair \((R,C)\), expand its determinant by the \(24\) permutations:
\[
D(R,C)=\sum_{\pi\in S_4}\operatorname{sgn}(\pi)
 z^{\sum_{j=0}^3 R_jC_{\pi(j)}\bmod10}.
\]
Reducing each summand by the displayed recurrence gives a four-component integer vector. **This vector vanishes if and only if the original complex determinant vanishes**, since \(\Phi_{10}\) is the minimal polynomial over \(\mathbb Q\).

**Exhaustive finite proof.** The bundled independent, standalone `verify_fourier10.py` enumerates, without sampling, all \(210\) row sets and \(210\) column sets using `itertools.combinations`; it performs the above exact signed \(24\)-term sum for each pair. For each fixed \(R\), it increments the count exactly when all four integer coefficients vanish, then tabulates the row-degree multiplicities. Its explicit assertions check that the full resulting degree counter equals \(\{0:20,10:100,20:50,30:20,110:10,130:10\}\), that precisely \(44100\) determinants were decided, and that \(5000\) are singular. All loops, the exact arithmetic, the degree tally, and the complete incidence digest are included; no floating-point comparisons, uninspected database, heuristic bounds, or incomplete exploration are involved. This proves the finite claim by a reproducible exhaustive certificate.

**Independent representation check.** A second bundled program, `fourier10_modcheck.py`, uses Gaussian elimination over the three unrelated finite fields of prime orders \(101\), \(181\), and \(241\), selecting a primitive tenth root in each and computing the same ordered bit string. The three modular results exactly match the cyclotomic bit-string SHA-256 \(`4a51a0450edaf31bc19e2a0701b5f01e600fa279602fdaae736fda59d8a9df2e`\). Equality with the cyclotomic certificate checks independent implementation choices; no inference from modular vanishing alone to complex vanishing is used.

## Verification

Run `python3 verify_fourier10.py` and `python3 fourier10_modcheck.py` with Python 3; both require only its standard library. Expected output is saved in `verification_output.txt`. The cyclotomic checker computes the exact determinant coefficient vectors and the full \(210\)-by-\(210\) incidence; the modular checker independently reproduces the entire zero/nonzero pattern. The main finite certificate itself is the exact enumeration, not a finite trial extrapolated to an infinite conjecture. Comparing all \(44100\) entries, instead of just totals, detects errors invisible to agreement of a single aggregate number.

## Relationship to prior work

Sui Tang, in arXiv:1702.05345 (first publicly posted 2017-02-17), explains how finite Fourier full-spark matrices govern universal dynamical sampling and emphasizes the composite-order difficulty. Alexeev, Cahill and Mixon supply the familiar uniform-distribution criterion and the order-ten counterexample. The published *Complete order-10 full-spark classification for harmonic Fourier row sets* determines precisely which four-row sets have **zero** singular maximal minors, yielding the previously determined \(20\) zero-degree rows. It does not specify the number of singular four-column choices for any of the other \(190\) rows. The published result *Exact singular minors for the near-consecutive four-row harmonic frame* gives \(10\) singular column choices for the particular row set \(\{0,1,2,4\}\) at order ten, but not the all-row six-level census. The present result provides the complete incidence-degree distribution and the exact full singular-pair count, not a restatement of full-spark yes/no classification or of a single-row minor formula.

## Limitations

No closed-form classification of which individual row/column pairs are singular is asserted beyond the exact executable decision procedure. The result concerns only the indicated finite dimension and does not imply a formula for higher Fourier orders or larger minors. The historical originality comparison is best knowledge and cannot exclude an unindexed incidence table or equivalent computation. The modular cross-checks corroborate the exact cyclotomic certificate but are not used as an independent formal proof of complex vanishing. An independent scientific audit has not been performed.

## References

1. S. Tang, *Universal Spatiotemporal Sampling Sets for Discrete Spatially Invariant Evolution Systems*, arXiv:1702.05345 (first posted 2017-02-17), §2 on full-spark Fourier sampling.
2. B. Alexeev, J. Cahill and D. G. Mixon, *Full Spark Frames*, arXiv:1110.3548 (2011); *J. Fourier Anal. Appl.* 18 (2012), 1167–1194.
3. *Complete order-10 full-spark classification for harmonic Fourier row sets*, published result, `https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-complete-order-10-full-spark-classification-for-harmonic-fourier--579f4b382450`.
4. *Exact singular minors for the near-consecutive four-row harmonic frame*, published result, `https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-singular-minors-for-the-near-consecutive-four-row-harmonic--bb8a5601ae6d`.
