# Exact avoidance polynomials for scattered two-ended run patterns in binary Parikh classes

## Finding
Fix integers \(A\ge 2\), \(B\ge 0\), and \(r\ge1\). For each \(0\le C\le AB\), let \(N_{A,B,r}(C)\) count binary words containing exactly \(A\) copies of \(a\), \(B\) copies of \(b\), and \(C\) scattered occurrences of \(ab\), but **no** scattered occurrence of \(ab^ra\) (here \(b^r\) denotes \(r\) repeated letters). Their complete generating polynomial is

\[
G_{A,B,r}(z)=\sum_{C=0}^{AB}N_{A,B,r}(C)z^C
=\sum_{k=0}^{\min(B,r-1)}z^k
\begin{bmatrix}A+k-2\\k\end{bmatrix}_{z}
\sum_{e=0}^{B-k}z^{Ae}.
\]

The Gaussian polynomial is defined by
\[\begin{bmatrix}n\\k\end{bmatrix}_{z}=\prod_{j=1}^{k}\frac{1-z^{n-k+j}}{1-z^j}\quad(0\le k\le n),\]
with the empty product equal to one; the displayed ratio denotes its unique polynomial expansion. The polynomial \(G_{A,B,r}\) is palindromic of degree \(AB\). For \(r=2\) it is exactly \(1+z+\cdots+z^{AB}\), while for \(r>B\) it is the Gaussian polynomial \(\begin{bmatrix}A+B\\A\end{bmatrix}_z\). Thus the avoidance probability inside a nonempty binary Parikh-matrix class is exactly
\[
1-p_{ab^ra}(A,B,C)=\frac{[z^C]G_{A,B,r}(z)}{[z^C]\begin{bmatrix}A+B\\A\end{bmatrix}_z}.
\]

For the natural two-\(a\) slice \(A=2\), put \(K_C=\min(r-1,C,2B-C)\). For \(0\le C\le2B\),
\[
N_{2,B,r}(C)=\#\{k\in\mathbb Z:0\le k\le K_C,\ k\equiv C\pmod2\}.
\]
For all \(B\ge2\) and \(2\le r\le B\), the full coefficient sequence of \(G_{2,B,r}\) is unimodal **if and only if \(r\) is even**. In particular, every odd \(r\ge3\) and every \(B\ge r\) give a non-unimodal, nevertheless symmetric and positive, avoidance polynomial. For example, \(G_{2,3,3}\) has coefficient sequence \((1,1,2,1,2,1,1)\).

## Assumptions and scope
A scattered occurrence uses strictly increasing letter positions; it need not be contiguous. The parameters \(A,B,r,C\) are integers in the ranges above. The pattern \(ab^ra\) is fixed as written; its two \(a\) letters must be distinct. The coefficient variable \(z\) tracks occurrences of the scattered two-letter word \(ab\), not the length of the ambient word. When \(A=0\) or \(A=1\), the pattern is automatically absent and the generating polynomial is the unrestricted Gaussian polynomial; these elementary boundary cases are not part of the main formula.

## Proof
**1. Canonical decomposition.** Every word with at least two \(a\)'s has a unique expression
\[
 b^{h}a b^{x_1}a b^{x_2}\cdots a b^{x_{A-1}}a b^{e},
\]
where \(h,e,x_i\ge0\), and \(h+e+\sum_{i=1}^{A-1}x_i=B\). Let \(k=\sum_{i=1}^{A-1}x_i\) be the number of \(b\)'s strictly between the first and last \(a\). A scattered \(ab^ra\) occurs exactly when \(k\ge r\): one can take the first and last \(a\)'s, and conversely any two \(a\)'s enclose at most \(k\) copies of \(b\). Thus avoidance is equivalent to \(k\le r-1\).

**2. Pair count and polynomial.** Every terminal \(b\) has \(A\) earlier \(a\)'s, and a \(b\) in the \(i\)-th internal gap has exactly \(i\) earlier \(a\)'s. Consequently the scattered \(ab\) count is \(C=Ae+\sum_{i=1}^{A-1}i x_i\). For fixed \(k\), the internal configurations contribute the complete homogeneous polynomial \(h_k(z,z^2,\ldots,z^{A-1})\). Subtracting one from each selected gap index gives partitions inside a \(k\)-by-\((A-2)\) rectangle, so their polynomial is \(z^k\begin{bmatrix}A+k-2\\k\end{bmatrix}_z\). Each \(e\in\{0,\ldots,B-k\}\) fixes \(h=B-k-e\) uniquely. Summing over admissible \(k,e\) proves the claimed polynomial with no multiplicities omitted or duplicated. All sums are finite, including the case \(k=0\).

**3. Symmetry and endpoint regimes.** Reversal preserves the palindrome \(ab^ra\) and sends the number of scattered \(ab\)'s from \(C\) to \(AB-C\); this is a bijection between the counted classes, proving \(N_{A,B,r}(C)=N_{A,B,r}(AB-C)\). At \(r=2\), the summand \(k=0\) supplies exponents \(Ae\), \(0\le e\le B\), and \(k=1\) supplies \(Ae+i\), \(0\le e<B\), \(1\le i<A\), each exactly once. The exponents together are exactly the integers \(0,\ldots,AB\). If \(r>B\), no word can contain \(r\) interior copies of \(b\), so the sum enumerates the entire fixed-composition family; the standard binary-word/rectangle-partition bijection yields the unrestricted Gaussian polynomial.

**4. The exact two-\(a\) unimodality boundary.** If \(A=2\), there is only one internal gap: \(C=2e+k\) with \(k\ge0\), \(e\ge0\), \(k+e\le B\), and \(k\le r-1\). Eliminating \(e\) gives the displayed parity-and-cutoff formula for every \(C\). Reversal gives symmetry around \(B\). Suppose \(2\le r\le B\). For \(0\le C\le B\), the cutoff reduces to \(K_C=\min(r-1,C)\). If \(r=2s\) is even, the coefficient increases in paired steps \(1,1,2,2,\ldots,s,s\) up to \(C=r-1\), then stays equal to \(s\) through the midpoint. Symmetry makes it nonincreasing afterwards, proving unimodality. If \(r=2s+1\) is odd, the three consecutive coefficients at \(C=r-1,r,r+1\) are \(s+1,s,s+1\), because \(B\ge r\) keeps the cutoff equal to \(r-1\) at all three positions. This strict valley violates unimodality. These cases exhaust \(2\le r\le B\).

**5. Exact conditional probability.** The generating polynomial for all fixed-composition words is \(\begin{bmatrix}A+B\\A\end{bmatrix}_z\), since the \(ab\) count is the area of a partition in an \(A\)-by-\(B\) rectangle. Every coefficient with \(0\le C\le AB\) is positive (choose a balanced partition). Dividing the avoidance count by the class size yields the asserted exact probability.

## Verification
A standalone Python checker reconstructs both sides by independent routes. It enumerates all binary words of fixed composition for \(2\le A\le7\), \(0\le B\le7\), and \(1\le r\le B+2\), directly tests subsequence avoidance using the number of internal \(b\)'s, and compares the resulting \(ab\)-count histogram with the polynomial from the disjoint gap decomposition. This checks 264 parameter cases. It also checks palindromicity, the \(r=2\) flat regime, and the \(r>B\) Gaussian regime; a separate parity-count implementation checks the two-\(a\) formulas. Run `python3 artifacts/check.py` from the directory containing this result and compare with `artifacts/check_output.txt`. These finite tests are supplementary; the proof establishes all parameter ranges.

## Relationship to prior work
Fazekas, Huang, and Mercaş (2026, arXiv:2610.06717, first publicly posted October 5, 2026) study binary Parikh-matrix languages and prove arithmetic endpoint tests and a fixed-pattern additive probability approximation scheme. Their Section 5 leaves explicit intermediate probabilities as a natural refinement, and does not state the present uniform coefficient law or unimodality classification. Richomme (arXiv:2510.07159, first posted October 8, 2025) establishes the general partition model and canonical extremal representatives of binary 2-binomial equivalence classes. That model and the classical Gaussian identity are used as background here; in particular the \(r=2\) singleton case is an explanatory boundary, not asserted to be new. The separately parameterized \(r\ge3\) avoidance polynomial and sharp two-row non-unimodality phenomenon require the additional scattered-pattern/gap analysis above.

## Limitations
The result concerns scattered occurrences, not contiguous-factor avoidance. It determines an exact coefficient formula, not a logarithmic-input-time coefficient algorithm. The unrestricted Gaussian denominator is well known. Existing descriptions of partitions and canonical class representatives overlap the endpoint special cases, and unlocated equivalent bounded-spread enumerations remain an originality risk.

## References
1. Szilárd Zsolt Fazekas, Xinhao Huang, Robert Mercaş, *Subsequence Analysis Problems for Binary Parikh Matrices*, arXiv:2610.06717 (October 5, 2026), especially Sections 2, 4, 5. https://arxiv.org/abs/2610.06717
2. Gwénaël Richomme, *On some 2-binomial coefficients of binary words: geometrical interpretation, partitions of integers, and fair words*, arXiv:2510.07159 (October 8, 2025), especially Section 4. https://arxiv.org/abs/2510.07159
3. Adrian Atanasiu, *Binary Amiable Words* (2007), Section 2, an earlier description of binary Parikh equivalence classes and rewriting. https://paperzz.com/doc/8039966/january-26--2007-8-31-wspc-instruction-file-amiabile
