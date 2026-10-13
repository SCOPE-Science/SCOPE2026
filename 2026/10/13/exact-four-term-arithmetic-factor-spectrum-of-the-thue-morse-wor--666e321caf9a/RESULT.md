# Exact four-term arithmetic factor spectrum of the Thue–Morse word
## Finding
Write the Thue–Morse word as
\[
t(n)=s_2(n)\bmod 2\qquad(n\ge0),
\]
where \(s_2(n)\) is the sum of the binary digits of \(n\). For every integer \(d\ge1\), define the **fixed-difference four-term arithmetic factor set**
\[
\mathcal P_d=\{t(n)t(n+d)t(n+2d)t(n+3d):n\ge0\}\subseteq\{0,1\}^{4}.
\]
Let \(d_{\mathrm{odd}}\) denote the odd part of \(d\). Then
\[
|\mathcal P_d|=
\begin{cases}
10,&d_{\mathrm{odd}}=1,\\
14,&d_{\mathrm{odd}}=3,\\
16,&d_{\mathrm{odd}}\ge5.
\end{cases}
\]
This is a complete *fixed-difference* classification, not the ordinary arithmetical complexity obtained by taking a union over all differences.

When \(d_{\mathrm{odd}}=3\), precisely the words \(0110\) and \(1001\) fail to occur. When \(d_{\mathrm{odd}}=1\), precisely the six words
\[
0000,\quad1111,\quad0001,\quad1110,\quad0111,\quad1000
\]
fail to occur. For every other odd part, **all sixteen** binary words of length four occur along arithmetic progressions with that *same prescribed difference*.

## Assumptions and scope
Every factor is read in the chronological order of the four positions \(n,n+d,n+2d,n+3d\), which need not be consecutive positions of the ambient word. Both the starting position \(n\ge0\) and the difference \(d\ge1\) are arbitrary integers subject to those ranges.

The exact infinite classification is certified by a finite automaton constructed from the elementary binary-addition carry equations. The checker constructs all states and transitions algorithmically; it does not extrapolate a finite list of differences or a finite Thue–Morse prefix.

The source literature studies monochromatic arithmetic progressions in this word and their maximal lengths at fixed differences. A later result already establishes the existence of monochromatic four-term progressions for every difference not a power of two. The present conclusion classifies *all* four-term binary patterns, including the exceptional non-monochromatic pair at odd part three.

## Proof
**1. Reduction to odd differences and relative colors.** Every nonnegative integer has a unique decomposition \(m=2^kq+s\) with \(0\le s<2^k\), and
\[
t(2^kq+s)=t(q)\oplus t(s),
\]
where \(\oplus\) is addition modulo two. Thus arithmetic factors at difference \(2^kd\) are exactly factors at difference \(d\), possibly complemented in all four positions. Conversely, given any factor at difference \(d\), taking \(s=0\) realizes that factor at difference \(2^kd\). Therefore \(\mathcal P_{2^kd}=\mathcal P_d\), and it suffices to consider odd \(d\).

For every \(n,d\), choose \(2^K>n+3d\). The progression beginning at \(n+2^K\) has all four symbols complemented, because binary addition introduces a new leading one without carrying. Therefore \(\mathcal P_d\) is closed under bitwise complement. It is enough to classify the attainable **relative masks**
\[
r(n,d)=\sum_{j=1}^{3}\big(t(n+jd)\oplus t(n)\big)2^{j-1}\in\{0,\ldots,7\}.
\]
Every attainable mask generates exactly two complementary length-four words, and two distinct relative masks generate disjoint pairs. Consequently \(|\mathcal P_d|\) is twice the number of attainable masks.

**2. A 192-state binary-addition machine.** Read the binary digits of \(d\) from least significant to most significant. Guess the corresponding digits of \(n\). Maintain a state
\[
(c_1,c_2,c_3,p),\qquad 0\le c_j\le j,\quad0\le p<8,
\]
with \(c_j\) the carry when computing \(n+jd\), and with the three bits of \(p\) the parity of the digit differences accumulated so far. Initially all coordinates are zero. For current digits \(x\) of \(d\) and \(y\) of \(n\), put
\[
w_j=y+jx+c_j,\qquad
c'_j=\lfloor w_j/2\rfloor,\qquad
p'=p\oplus\sum_{j=1}^{3}((w_j\bmod2)\oplus y)2^{j-1}.
\]
This gives a deterministic transition once both \(x\) and \(y\) are fixed, with \(2\cdot3\cdot4\cdot8=192\) possible states. The carry ranges are invariant: if \(c_j\le j\), then \(\lfloor(y+jx+c_j)/2\rfloor\le j\).

After all digits of \(d\) are processed, all higher digits of \(d\) are zero, while higher digits of \(n\) may still be chosen arbitrarily before eventually becoming zero. A state is terminal for mask \(r\) if and only if finitely many such \(x=0\) transitions reach \((0,0,0,r)\). This condition is decided exactly by reverse reachability in the 192-state directed graph. It includes all remaining high bits and carry propagation, so no bound on \(n\) is imposed.

**3. Exhaustive finite-state quotient.** Forget the guessed digits \(y\) of \(n\) using subset transitions: for a subset \(S\) and a digit \(x\) of \(d\), take the union of all successors of states in \(S\) under both choices \(y=0,1\). Because \(d\) is odd, its first least-significant digit is \(1\). Starting from the resulting subset, exhaustive graph closure has **exactly 195** reachable subsets. Classify each subset by the eight-bit mask indicating its possible terminal relative parities. Direct enumeration of the exact transition graph gives the following three classes:

\[
\begin{array}{c|c|c}
\text{class}&\text{terminal mask (hex)}&\text{number of subsets}\\\hline
A&\mathtt{6e}&5\\
B&\mathtt{f7}&6\\
C&\mathtt{ff}&184
\end{array}
\]

The exhaustive transition verification also gives: the initial subset after the first \(1\) is in \(A\); the further digit \(1\) sends that initial subset to \(B\); all \(0\)-edges in \(A\) remain in \(A\); all \(0\)-edges in \(B\) remain in \(B\); every \(1\)-edge in \(B\) enters \(C\); every \(1\)-edge from \(A\) other than the just-mentioned initial edge enters \(C\); and \(C\) is absorbing under both digits. Moreover, the \(0\)-orbits of the two exceptional initial subsets exhaust \(A\) and \(B\), respectively. These assertions are evaluated over the entire finite reachable graph by `verify.py`, rather than checked only up to a finite input length.

Hence reading an odd positive integer in least-significant-digit-first order leads to \(A\) exactly for the digit word \(1\), to \(B\) exactly for \(11\), and to \(C\) for every other canonical odd positive integer. Equivalently, the respective integers are \(d=1\), \(d=3\), and odd \(d\ge5\). (Optional extra zero digits after the leading represented bits leave the class unchanged.)

The hexadecimal masks have bit sets
\[
\mathtt{6e}:\{1,2,3,5,6\},\qquad
\mathtt{f7}:\{0,1,2,4,5,6,7\},\qquad
\mathtt{ff}:\{0,1,2,3,4,5,6,7\}.
\]
Therefore there are respectively \(5,7,8\) attainable relative masks, giving exactly \(10,14,16\) complementary four-symbol factors. The missing mask in the middle class is \(3\), corresponding to the complementary words \(0110,1001\). The missing masks in the first class are \(0,4,7\), giving the six words stated in the finding.

The finite-state construction, exhaustive reachability check, and reduction to odd differences prove the theorem for **every** positive difference.

## Verification
Run `python3 verify.py` in the same directory as `certificate.json`. It reconstructs all 192 carry states from the transition equations, computes reverse terminal reachability for each of eight relative masks, and exhausts the 195 reachable subset states for odd differences. It checks both the exact class sizes and every transition-closure identity on the entire finite graph. This finite graph enumeration, together with the proved carry correspondence, is an exhaustive certificate for unbounded \(n,d\).

In addition, for every \(1\le d\le511\), the verifier constructs an explicit starting-position witness for each accepted relative mask, checks the actual binary digit sums at all four positions, and verifies the complementary witness. Independently, it enumerates every four-term factor with \(1\le d\le128\) in an 80,000-symbol Thue–Morse prefix and checks all predicted factor counts. These latter tests are regression checks, not substitutes for the all-input finite-state proof.

The verifier uses only Python 3 and the standard library. On success it prints `VERIFY_OK` with the reachable-state count, class sizes, witness count, and finite cross-check ranges.

## Relationship to prior work
Aedo, Grimm, Nagai, and Staynova study long monochromatic progressions of a fixed difference in Thue–Morse and related binary substitution words. Their 2021 preprint and 2022 journal version provide the direct motivation and structural context, but they do not classify all length-four patterns for each prescribed difference.

Joshi and Rust subsequently use automatic methods to sharpen the fixed-difference **monochromatic** problem. In particular, their 2025 work shows that four-term monochromatic progressions exist at every difference not a power of two. That result is fully credited and is compatible with the presence of the mask \(0\) in both classes \(B\) and \(C\). It does not decide which of the other seven relative masks occur; notably it does not distinguish the odd part \(3\) from all larger odd parts by the absence of \(0110\) and \(1001\).

Earlier work of Avgustinovich, Fon-Der-Flaass, and Frid establishes the arithmetical complexity of Thue–Morse, allowing the progression difference to vary with the word. The union over *some* differences having all binary words does not imply that a prescribed difference \(d\) yields all patterns. The classification here controls that stronger fixed-difference quantifier.

## Limitations
Only arithmetic factors of length **four** in the binary Thue–Morse word are classified. No formula is asserted for longer factors, for generalized alphabets, or for the least starting index realizing a given pattern.

The proof uses an exact finite-state exhaustion as a certificate of reachability and quotient transitions; the supporting code is therefore an essential part of the constructive proof. A finite-prefix experiment alone would not suffice.

The literature comparison includes the full text of the principal monochromatic-progressions papers. The 2003 foundational arithmetical-complexity paper was corroborated through its bibliographic record, abstract, the author's publication page, and later papers' summaries; its complete text was not recovered in this review. An unindexed older fixed-difference factor table remains a residual originality risk.

## References
1. I. Aedo, U. Grimm, Y. Nagai, and P. Staynova, “On long arithmetic progressions in binary Morse-like words,” arXiv:2101.02056v1, first public 2021-01-06; journal version “Monochromatic arithmetic progressions in binary Thue–Morse-like words,” *Theoretical Computer Science* 934 (2022), 65–80, DOI 10.1016/j.tcs.2022.08.013.
2. G. Joshi and D. Rust, “Monochromatic arithmetic progressions in the Fibonacci, Thue–Morse, and Rudin–Shapiro words,” arXiv:2501.05830v2; *Theoretical Computer Science* (2025), DOI 10.1016/j.tcs.2025.115391.
3. S. V. Avgustinovich, D. G. Fon-Der-Flaass, and A. E. Frid, “Arithmetical complexity of infinite words,” *Words, Languages & Combinatorics III* (2003), 51–62, DOI 10.1142/9789812704979_0004.
