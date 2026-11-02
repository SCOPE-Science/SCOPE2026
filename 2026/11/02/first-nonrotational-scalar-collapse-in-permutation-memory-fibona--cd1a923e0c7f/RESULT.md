# First nonrotational scalar collapse in permutation-memory Fibonacci recurrences

## Finding
For each \(k\in\{2,3,4,5\}\) and each permutation \(\pi=(\pi_0,\ldots,\pi_{k-1})\) of \(\{2,3,\ldots,k+1\}\), define an integer sequence by
\[
R_0=0,\quad R_1=1,\qquad R_n=\sum_{j=1}^{\pi_{n\bmod k}}R_{n-j}\quad(n\ge2),
\]
where \(R_m=0\) for \(m<0\). A pattern has *scalar period collapse* when there are real \(c\) and integer \(N\) such that \(R_{n+k}=cR_n\) for every \(n\ge N\).

**Classification.** For \(k=2,3,4\), precisely the cyclic rotations of \((2,3,\ldots,k+1)\) have scalar period collapse. For \(k=5\), precisely the cyclic rotations of \((2,3,4,5,6)\) and of \((2,4,5,6,3)\) have it. The numbers of successful permutations are, respectively, \(2,3,4,10\) out of \(2,6,24,120\). In every successful case the multiplier is uniquely \(c=3\cdot2^{k-2}\).

In particular, the first successful ordering not obtained by cyclic rotation of the increasing cycle is the period-five pattern \((2,4,5,6,3)\), for which \(R_{n+5}=24R_n\) holds for every \(n\ge6\), and does not hold at \(n=5\).

## Assumptions and scope
The memory pattern uses each of the consecutive lengths \(2,3,\ldots,k+1\) exactly once during a period of length \(k\). The recurrence, zero extension to negative indices, and the initial values are fixed as above; the permutations are indexed by \(n\bmod k\), with \(\pi_0\) used when \(k\mid n\). The classification covers every such permutation for periods \(2\) through \(5\), but only the *single scalar* collapse \(R_{n+k}=cR_n\). It does not classify reductions to higher-order constant-coefficient recurrences or all periods.

## Proof
**Lemma (a finite necessary-and-sufficient test).** Let \(k\ge2\), \(d=k+1\), \(Q=2d\), and let \(\pi\) be any periodic memory pattern with lengths at most \(d\). Set
\[
c_* = \frac{R_{(Q+1)k}}{R_{Qk}}.
\]
Then eventual scalar period collapse is equivalent to the following \(dk\) *exact* equalities:
\[
R_{(q+1)k+r}=c_*R_{qk+r}
\quad\text{for every}\quad Q\le q<Q+d,\quad 0\le r<k.
\]
When these equalities hold, the collapse holds for **all** \(n\ge Qk\). (All denominators above are positive, since \(R_n>0\) for \(n\ge1\).)

*Proof of the lemma.* Put \(v_n=(R_n,R_{n-1},\ldots,R_{n-d+1})^{\mathsf T}\). At every sufficiently large index the recurrence is \(v_n=T_{\pi_{n\bmod k}}v_{n-1}\), where \(T_\ell\) is the integer companion matrix with first row consisting of \(\ell\) ones followed by zeros and with ones on the first subdiagonal. For each fixed \(r\), one entire period has a fixed matrix \(M_r\) with \(v_{(q+1)k+r}=M_rv_{qk+r}\) for \(q\ge d\).

For any scalar \(c\), consider the phase-\(r\) defect \(E_q=R_{(q+1)k+r}-cR_{qk+r}\). For \(q\ge d\), it is a matrix coefficient of powers of \(M_r\). Cayley–Hamilton makes it satisfy the degree-\(d\) recurrence given by \(\chi_{M_r}\). Thus \(d\) consecutive zero defects imply every subsequent defect is zero.

For the converse, a degree-\(d\) matrix has a stabilized image \(\operatorname{im}(M_r^d)\) on which \(M_r\) is invertible. Write \(\chi_{M_r}(t)=t^hP_r(t)\), with \(P_r(0)\ne0\) and \(h\le d\). Cayley–Hamilton implies that \(E_q\), once \(q\ge d+h\), satisfies the recurrence \(P_r\), which has a nonzero constant coefficient. Hence an eventually zero defect must vanish backward through this invertible recurrence for every \(q\ge d+h\), in particular for every \(q\ge Q\). Since every \(R_n\) with \(n\ge1\) is positive, eventual equality uniquely forces \(c=c_*\). This proves necessity, and the preceding Cayley–Hamilton argument proves sufficiency. \(\square\)

**Exhaustive finite classification.** The accompanying `verify.py` enumerates all \(k!\) permutations for each \(2\le k\le5\). For each pattern it constructs the integer sequence by its defining recurrence, computes the forced rational \(c_*\), and checks precisely the \(dk\) equalities in the lemma by integer cross-multiplication. All checks are exact, with no floating-point tests. A separate companion-matrix computation checks that the block-transition representation agrees with the direct recurrence for every pattern. The program asserts that the successful sets equal the stated rotation classes and that all their multipliers equal \(3\cdot2^{k-2}\). It verifies \(152\) permutations, with successful counts \(2,3,4,10\). By the lemma, this finite enumeration proves the complete *eventual* classification rather than merely checking a finite initial segment.

**Direct infinite witness at the first exceptional period.** For \(\pi=(2,4,5,6,3)\), the defining recurrence gives
\[
(R_6,R_7,R_8,R_9,R_{10})=(13,26,52,91,143)
\]
and
\[
(R_{11},R_{12},R_{13},R_{14},R_{15})=(312,624,1248,2184,3432)=24(R_6,R_7,R_8,R_9,R_{10}).
\]
For each \(n\ge11\), all indices \(n-j\) occurring in its recurrence satisfy \(n-j\ge6\). Because \(\pi_{(n+5)\bmod5}=\pi_{n\bmod5}\), induction gives
\[
R_{n+5}=\sum_{j=1}^{\pi_{n\bmod5}}R_{n+5-j}
=24\sum_{j=1}^{\pi_{n\bmod5}}R_{n-j}=24R_n.
\]
The first five equalities were checked above. Moreover \(R_{10}=143\ne144=24R_5\), proving that the stated onset is sharp. \(\square\)

## Verification
Run `python3 verify.py` in the same directory. The expected final line is:

`VERIFY_OK permutations=152 counts=2,3,4,10 noncyclic_first=5 multiplier=24 matrix_checked=yes`

The program uses Python's standard library and exact integer/rational arithmetic; no external data files or libraries are required. It checks the complete finite reduction, not an arbitrary numerical horizon. The infinite conclusion relies on the stated matrix lemma and the recurrence induction, which are separately proved above.

## Relationship to prior work
Abdelaidoum, Mehiri and Belbachir (arXiv:2609.12569, first public September 11, 2026), Definition 1 and Theorem 1, establish the collapse factor \(3\cdot2^{k-2}\) for the **single increasing memory cycle** for arbitrary \(k\), and Problem 2 explicitly asks for classification of more general periodic memory patterns. That theorem does not entail the complete permutation classification given here or the second period-five family. The original factor itself is not claimed as new.

Emerson's variable-order meta-Fibonacci analysis (arXiv:math/0508522) gives growth bounds and local ratio results, but does not provide the exact permutation classification. McLellan's work on periodically signed fixed-order Fibonacci recurrences addresses a different coefficient model. General facts on periodic linear recurrences and Cayley–Hamilton are used as standard tools, not presented as new discoveries.

## Limitations
The theorem concerns the specified initial data, a single occurrence of each memory length, periods at most five, and scalar period collapse; it does not decide broader periodic patterns, higher-order constant-coefficient reductions or periods above five. The finite results are exhaustive only because the matrix lemma bridges eventual behavior to a fixed test window. Earlier uncatalogued equivalences or general theorems could affect priority; no independent mathematical audit is claimed.

## References
1. W. Abdelaidoum, E.-M. Mehiri, H. Belbachir, *Rotating-Memory Fibonacci Numbers and Periodic Tilings*, arXiv:2609.12569 (2026), especially Definition 1, Theorem 1, and Problem 2. https://arxiv.org/abs/2609.12569
2. N. D. Emerson, *A family of meta-Fibonacci sequences defined by variable order recursions*, arXiv:math/0508522 (2005), especially Sections 1–2. https://arxiv.org/abs/math/0508522
3. K. McLellan, *Periodic Coefficients and Random Fibonacci Sequences*, Electronic Journal of Combinatorics 20(4) (2013), P32. https://doi.org/10.37236/3204
