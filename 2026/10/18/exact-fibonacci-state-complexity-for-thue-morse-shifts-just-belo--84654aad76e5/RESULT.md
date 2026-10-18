# Exact Fibonacci state complexity for Thue–Morse shifts just below powers of two

## Finding

Let \(t(n)\) be the parity of the number of ones in the binary expansion of the nonnegative integer \(n\). For an integer \(c\ge 0\), let \(N(c)\) be the smallest number of states in a complete deterministic finite automaton with output (DFAO) which, reading an arbitrary finite binary word \(w\) most-significant digit first, outputs \(t([w]_2+c)\). The empty word represents zero; leading zeroes are permitted and must not affect the answer.

**Theorem.** For every integer \(k\ge 1\),

\[
\boxed{N(2^k-1)=2F_{k+4}-6},
\]

where \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\). The exact state counts at the first eleven Mersenne shifts, for \(k=1,\ldots,11\), are

\[
4,\ 10,\ 20,\ 36,\ 62,\ 104,\ 172,\ 282,\ 460,\ 748,\ 1214.
\]

This is an all-parameter exact classification for the natural shifts immediately preceding powers of two, not an interpolation from those eleven cases.

## Assumptions and scope

Every state is required to be reachable in a minimal DFAO, and input is binary, most-significant digit first. Write \(\oplus\) for Boolean exclusive-or. The relevant Nerode equivalence compares all finite continuations, including the empty continuation. No claims are made for arbitrary non-Mersenne shifts or for other input radices.

For \(c\ge1\), define the **carry-offset set**

\[
I_c=\{c\}\cup\bigcup_{\ell\ge1}
\left(\left\{\left\lfloor\frac{c}{2^\ell}\right\rfloor\right\}
\cup\begin{cases}
\left\{\left\lfloor\frac{c}{2^\ell}\right\rfloor+1\right\},&2^\ell\nmid c,\\
\varnothing,&2^\ell\mid c.
\end{cases}\right).
\]

This set is finite. For a prefix value \(m\ge0\), its carry fingerprint is the tuple \(\Phi_c(m)=(t(m+j))_{j\in I_c}\), in increasing index order. Define also

\[
Q_k=\{0,1\}\cup\{2^i:1\le i\le k-1\}
\cup\{2^j-1:2\le j\le k\}.
\]

Thus \(I_{2^k-1}=Q_k\), with \(Q_1=\{0,1\}\).

## Proof

**1. Residuals are exactly carry fingerprints.** Fix \(c\ge1\). After reading a prefix with value \(m\) and then a continuation of length \(\ell\) with value \(u\), the required output is \(t(2^\ell m+u+c)\). Write \(c=2^\ell q+r\), with \(0\le r<2^\ell\). Binary digit-parity additivity across disjoint blocks gives

\[
t(2^\ell m+u+c)=
 t\!\left(m+q+\left\lfloor\frac{u+r}{2^\ell}\right\rfloor\right)
 \oplus t((u+r)\bmod 2^\ell).
\]

For fixed \(\ell\), the first term uses the offset \(q\), and also \(q+1\) precisely when \(r>0\). The low-digit term is independent of \(m\). Both offsets, when present, are separately testable: choose \(u=0\) for \(q\), and \(u=2^\ell-r\) for \(q+1\). For \(\ell=0\), the empty continuation directly tests offset \(c\). Consequently two reachable prefixes yield identical outputs after every continuation if and only if their fingerprints agree. Every integer \(m\) is a reachable prefix value (also under the leading-zero convention), so the Myhill–Nerode principle for DFAOs proves

\[
N(c)=\left|\{\Phi_c(m):m\ge0\}\right|.
\]

Taking quotients and remainders of \(2^k-1\) by powers of two gives the stated explicit set \(I_{2^k-1}=Q_k\).

**2. Exact count for the dyadic power-offset profile.** For \(r\ge0\), consider the profile

\[
P_r(m)=\big(t(m),t(m+1),t(m+2),t(m+4),\ldots,t(m+2^r)\big).
\]

Let \(d_i(m)=t(m)\oplus t(m+2^i)\) for \(0\le i\le r\). If the binary digits of \(m\), starting at position \(i\), contain a run of \(R_i\) consecutive ones before the next zero, adding \(2^i\) changes the parity by \(1-R_i\). Hence \(d_i=1\oplus(R_i\bmod2)\). A zero at \(d_i\) means \(R_i\) is odd; then \(R_{i+1}=R_i-1\) is even, so \(d_{i+1}=1\). Therefore the difference vector \((d_0,\ldots,d_r)\) cannot have two consecutive zeroes.

Conversely take any length-\((r+1)\) binary vector without consecutive zeroes. Choose the low \(r+1\) binary digits of \(m\) to be one exactly where the prescribed vector has zero, set digit \(r+1\) to zero, and set all other digits initially to zero. Each chosen one is isolated, so the actual difference vector agrees with the prescribed one. The independent bit at position \(r+2\) flips \(t(m)\) without changing these lower run lengths or differences. Thus both possible values of \(t(m)\) occur for every admissible difference vector. There are \(F_{r+3}\) binary vectors of length \(r+1\) without consecutive zeroes; we have proved

\[
\left|\{P_r(m):m\ge0\}\right|=2F_{r+3}.
\]

This dyadic count is included for a self-contained argument; it is not asserted as new (see Biswas in the references).

**3. Parity decomposition of the Mersenne fingerprints.** Put \(C_k=\left|\{(t(m+j))_{j\in Q_k}:m\ge0\}\right|\). For \(k\ge2\), using \(t(2a)=t(a)\) and \(t(2a+1)=1\oplus t(a)\), examine the prefixes \(m=2a\) and \(m=2a+1\) separately.

For an even prefix \(m=2a\), the coordinates of \(Q_k\) satisfy

\[
\begin{aligned}
t(2a)&=t(a), & t(2a+1)&=1\oplus t(a),\\
t(2a+2^i)&=t(a+2^{i-1})&&(1\le i\le k-1),\\
t(2a+2^j-1)&=1\oplus t(a+2^{j-1}-1)&&(2\le j\le k).
\end{aligned}
\]

The coordinates of \(Q_{k-1}\) at \(a\) appear, possibly complemented, and determine every displayed coordinate. Hence the even-prefix fingerprints are in bijection with \(Q_{k-1}\) fingerprints, contributing exactly \(C_{k-1}\) possibilities.

For an odd prefix \(m=2a+1\), the corresponding coordinates are

\[
\begin{aligned}
t(2a+1)&=1\oplus t(a), &t(2a+2)&=t(a+1),\\
t(2a+1+2^i)&=1\oplus t(a+2^{i-1})&&(1\le i\le k-1),\\
t(2a+1+2^j-1)&=t(a+2^{j-1})&&(2\le j\le k).
\end{aligned}
\]

These are exactly a redundant/complemented encoding of the power-offset profile \(P_{k-1}(a)\), containing the offsets \(0,1,2,4,\ldots,2^{k-1}\). They contribute \(2F_{k+2}\) distinct fingerprints by Step 2.

**4. The two parity families do not intersect.** Since \(\{0,1,2,3\}\subseteq Q_k\) for \(k\ge2\), the four consecutive-coordinate bits are visible in every fingerprint. For even \(m=2a\), both pairs of consecutive bits at offsets \((0,1)\) and \((2,3)\) are complementary. For odd \(m=2a+1\), these two pairs are complementary simultaneously only if \(t(a)=t(a+1)=t(a+2)\). That cannot occur: any three consecutive Thue–Morse terms contain one pair indexed by an even number and its successor, and such a pair is always complementary. Thus the even and odd fingerprint families are disjoint, proving

\[
C_k=C_{k-1}+2F_{k+2}\qquad(k\ge2).
\]

**5. Base case and summation.** The four length-two binary factors \(00,01,10,11\) all occur in the Thue–Morse word, so \(C_1=4\). Therefore

\[
C_k=4+2\sum_{j=2}^k F_{j+2}
=4+2(F_{k+4}-F_5)=2F_{k+4}-6,
\]

using \(F_5=5\). The exact residual lemma identifies \(N(2^k-1)=C_k\), completing the proof for every \(k\ge1\).

## Verification

The standalone program `checker.py` computes the carry-fingerprint sets for all Mersenne shifts \(2^k-1\) through \(k=11\), scanning \(2^{k+4}\) nonnegative prefix values in each case. Independently, it builds a complete (not initially minimized) binary DFAO from all reachable length-\((c+1)\) consecutive Thue–Morse blocks and minimizes it by successive output/transition partition refinement for \(1\le k\le7\). Both methods agree with the formula, and the exact recorded output is in `checker_output.txt`. These finite tests confirm implementations and small cases; the proof above, not an extrapolation from them, establishes all \(k\).

## Relationship to prior work

Moradi, Rampersad, and Shallit established a general linear upper bound and a Fibonacci-based lower-bound family for shifted Thue–Morse automata, and explicitly asked for exact state complexity as a function of the shift. OEIS A382296 contains exact finite values for shifts, including initial Mersenne shifts, but states an infinite closed formula only for power-of-two shifts. Biswas proved that power-of-two formula. The present theorem concerns the different infinite family of shifts immediately **below** powers of two; neither an upper bound, an infinite dyadic exact count, nor a finite table establishes its formula. Charlier, Cisternino, and Massuir treat the arithmetic family \(m\mathcal T+r\) with \(0\le r<m\), rather than arbitrary translates of \(\mathcal T\).

## Limitations

This is a statement about binary MSD-first DFAOs with correct outputs on all finite encodings, including leading zeroes. No formula is established here for all \(c\), other numeration systems, or other automatic sequences. The observed finite counts alone would not imply the all-parameter identity. Historical priority beyond the inspected papers, public sequence entry, and related manuscripts cannot be guaranteed; independent expert validation has not been performed.

## References

1. D. Moradi, N. Rampersad, and J. Shallit, *Complexity of Linear Subsequences of k-Automatic Sequences*, arXiv:2512.10017 (first submitted 2025-12-10), especially Section 4.2 and Open Problem 2. https://arxiv.org/abs/2512.10017
2. J. Shallit, *OEIS A382296*, first authored 2025-03-21. https://oeis.org/A382296
3. R. Biswas, *State Complexity of Thue-Morse Shifts by Powers of Two* (2026), manuscript and proof accompanying A382296. https://github.com/rnbguy/proofs/blob/main/A382296/A382296.typ
4. É. Charlier, C. Cisternino, and A. Massuir, *Minimal Automaton for Multiplying and Translating the Thue-Morse Set*, Electronic Journal of Combinatorics 28 (2021), #P3.12, doi:10.37236/9068.
