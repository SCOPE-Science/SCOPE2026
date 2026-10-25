# Exact binary-digit formula for least-significant-digit-first Thue–Morse shift automata

## Finding
Let \(t(n)\) be the parity of the number of ones in the binary expansion of a nonnegative integer \(n\). For a fixed shift \(c\ge0\), let \(N_{\mathrm{LSD}}(c)\) be the number of states in a minimal deterministic automaton with output (DFAO) that computes \(t(n+c)\), with the binary digits of \(n\) read **least-significant digit first**. All finite binary words, the empty word, and extra trailing zeroes are admitted.

For \(c=0,1,2,3\), respectively, the exact numbers are \(2,3,5,6\). For any \(c\ge4\), define \(m=\lfloor\log_2c\rfloor\) and \(r_e=c\bmod 2^e\), and for \(2\le e<m\) let
\[
v_e(c)=\begin{cases}2,&r_e=0,\\3,&r_e\in\{1,2^e-1\},\\4,&2\le r_e\le2^e-2.\end{cases}
\]
Then, with an empty sum when \(m=2\),
\[
\boxed{N_{\mathrm{LSD}}(c)=7+\sum_{e=2}^{m-1}v_e(c)+2\mathbf1_{\{c\ge3\cdot2^{m-1}\}}+\mathbf1_{\{c=3\cdot2^{m-1}-1\}}.}
\]
For every \(m\ge2\) the exact sharp bounds on the dyadic interval \(2^m\le c<2^{m+1}\) are
\[
2m+3\le N_{\mathrm{LSD}}(c)\le4m+1.
\]
The lower and upper endpoints are attained, respectively, by \(c=2^m\) and \(c=2^{m+1}-2\). These are statements about **LSD-first** automata, not MSD-first automata.

## Assumptions and scope
A binary word \(b_0b_1\dots b_{e-1}\) has value \(\sum_{i=0}^{e-1}b_i2^i\). Every finite word is allowed, including the empty word of value zero and an arbitrary string of zeroes at its right end. State equivalence means equality of outputs on **all** possible continuations. The output function must be defined at every state. The result uses binary alphabet and the Thue–Morse parity map; nothing is asserted for other numeral bases or another automatic sequence.

## Proof
**1. Canonical residual automaton and minimality.** For \(j\ge0\) and \(s\in\{0,1\}\), denote by \(F_{j,s}\) the sequence-valued residual \(F_{j,s}(n)=t(n+j)\oplus s\). Starting from \((c,0)\), define for each input bit \(b\in\{0,1\}\)
\[
\delta_b(j,s)=\left(\left\lfloor\frac{j+b}{2}\right\rfloor,\ s\oplus((j+b)\bmod2)\right),
\qquad \tau(j,s)=t(j)\oplus s.
\]
The identity \(t(2n+j+b)=t(n+\lfloor(j+b)/2\rfloor)\oplus((j+b)\bmod2)\) proves correctness of every transition. Both possible successors have first coordinate no larger than \(\max\{j,1\}\); hence only finitely many states are reachable. Every residual \(F_{j,s}\) is distinct from every other residual with different \((j,s)\). Indeed, equality for \(j<k\) would say \(t(n+j)=t(n+k)\oplus(s\oplus s')\) for every \(n\ge0\), making \(t\) periodic with period \(k-j\) or with period \(2(k-j)\). Neither is possible. For completeness, if \(p\ge1\) were an eventual period, choose all sufficiently large \(h\) and evaluate at \(2^h-p\): the difference from \(2^h\) must vanish, whereas \(t(2^h-p)=h-\operatorname{popcount}(p-1)\pmod2\) alternates with \(h\), while \(t(2^h)=1\). The same argument excludes antiperiodicity by squaring its alleged period. When \(j=k\), the two values of \(s\) already disagree at the empty continuation. Consequently **the number of reachable pairs is the exact minimal DFAO state count**.

**2. Reachable pairs at a prescribed depth.** After any \(e\ge0\) digits whose represented low-order integer is \(u\in[0,2^e)\), the reached state is precisely
\[
\left(\left\lfloor\frac{c+u}{2^e}\right\rfloor,\quad t((c+u)\bmod2^e)\right).
\]
This follows either from repeated division with carry or directly from binary digit-sum additivity. At each \(e\ge1\), set \(a_e=\lfloor c/2^e\rfloor\) and \(r_e=c\bmod2^e\). The possible first coordinates are \(a_e\) and, if \(r_e>0\), \(a_e+1\). For coordinate \(a_e\), the possible parity bits are the Thue–Morse values of integers in \([r_e,2^e-1]\); for coordinate \(a_e+1\), they are the values on \([0,r_e-1]\). An interval containing two consecutive integers \(2^e-2,2^e-1\) has both parities; so does an interval containing \(0,1\). For \(e\ge2\) this yields exactly \(v_e(c)\) pairs when both first coordinates have not appeared at an earlier depth.

**3. Pairwise disjoint upper levels.** Fix \(c\ge4\) and \(m=\lfloor\log_2c\rfloor\). The starting depth contributes one state \((c,0)\). At depth \(1\) there are exactly two distinct states with first coordinate at least two. For depths \(2\le e\le m-2\), the first coordinates of consecutive levels are disjoint: if \(a_e\ge4\), then \(\lceil c/2^{e+1}\rceil\le\lceil(a_e+1)/2\rceil<a_e\), and no pair from a later level can return to a larger coordinate. At depth \(m-1\), the first coordinate \(a_{m-1}\) is either two or three, with the second coordinate at most four; it also does not intersect earlier levels. Thus depth \(1\) and depths \(2,\ldots,m-1\) contribute exactly \(2+\sum_{e=2}^{m-1}v_e(c)\) different states, in addition to the initial state. This argument also applies for \(m=2\), when the displayed sum is empty.

**4. Lower levels and the two exceptions.** At sufficiently large depth, both pairs at first coordinate zero and both at first coordinate one occur: the lower residue intervals contain \(0,1\), while the no-carry intervals contain \(2^e-2,2^e-1\). Thus the lower coordinates contribute **exactly four** eventual states and none overlaps any earlier coordinate (all earlier first coordinates are at least two). Coordinate two can occur after depth \(m-1\) only at depth \(m\); all later first coordinates are at most one. If \(c\ge3\cdot2^{m-1}\), the depth-\((m-1)\) first coordinates are at least three, whereas at depth \(m\) coordinate two appears with both parity bits because \(c-2^m\ge2^{m-1}\ge2\). This adds two states. If \(c<3\cdot2^{m-1}\), coordinate two already occurs at depth \(m-1\). Its no-carry interval has both parities except when \(c=3\cdot2^{m-1}-1\): then the interval has one element and depth \(m\) supplies the missing opposite parity. This adds exactly one state in that case, and zero otherwise. Combining steps 3–4 yields \(1+2+4=7\) plus the stated summands and corrections.

**5. Small shifts and sharp bounds.** Direct traversal from the initial pairs for \(c=0,1,2,3\) gives respectively \(2,3,5,6\) reachable states, all pairwise distinguishable by Step 1. For \(m\ge2\), every summand \(v_e\) lies in \([2,4]\), and the two correction indicators are mutually exclusive. Hence \(2m+3\le N_{\mathrm{LSD}}(c)\le4m+1\). With \(c=2^m\), all the residues \(r_e\) vanish and neither correction applies. With \(c=2^{m+1}-2\), all interior residues are \(2^e-2\) and the two-state correction applies. These attain the bounds.

## Verification
The accompanying standalone `verify.py` independently constructs the reachable pair automaton and checks the formula for every shift \(0\le c<16384\). It also refines output-equivalence partitions without using the closed formula and confirms all reachable pairs are pairwise distinguishable for \(0\le c\le512\). Finally it tests the two sharp dyadic endpoints for \(2\le m\le13\). The recorded output appears in `verification_output.txt`. The finite checks support, but do not replace, the all-shift argument above.

## Relationship to prior work
Moradi, Rampersad, and Shallit (2025/2026), *Complexity of Linear Subsequences of \(k\)-Automatic Sequences*, study state complexity for automatic subsequences, including shifts of Thue–Morse in **most-significant-digit-first** format (their Theorems 19 and 20). They also recall generic LSD-first constructions, but not the present exact per-shift LSD digit formula. Moradi, Popoli, Shallit, and Vukusic (2026), *State Complexity of Shifts of the Fibonacci Word*, calculate bounds for a different sequence and numeration system; they motivate sharp comparisons between input orientations. Charlier, Cisternino, and Massuir (2021) study recognizers for \(m\mathcal T+r\), a different transformation of the Thue–Morse set. The exact LSD-first state count here is neither the MSD-first count nor the size of those recognizers.

## Limitations
No claim of independent validation or priority certification is made. An equivalent formulation could exist in literature not indexed by the searches performed. The theorem requires all input encodings (including trailing zeroes); counts for a restricted canonical-input model need not match.

## References
1. D. Moradi, N. Rampersad, J. Shallit, *Complexity of Linear Subsequences of k-Automatic Sequences*, arXiv:2512.10017, first public 2025-12-10. https://arxiv.org/html/2512.10017v5
2. D. Moradi, P. Popoli, J. Shallit, I. Vukusic, *State Complexity of Shifts of the Fibonacci Word*, arXiv:2603.18858, first public 2026-03-19. https://arxiv.org/html/2603.18858v1
3. E. Charlier, C. Cisternino, A. Massuir, *Minimal Automaton for Multiplying and Translating the Thue-Morse Set*, Electronic Journal of Combinatorics 28 (2021), P3.12. https://www.combinatorics.org/ojs/index.php/eljc/article/view/v28i3p12
