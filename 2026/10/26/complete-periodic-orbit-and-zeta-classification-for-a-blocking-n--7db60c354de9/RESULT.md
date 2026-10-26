# Complete periodic-orbit and zeta classification for a blocking number-conserving cellular automaton

## Finding
Let \(N\ge1\) and let \(F_N\) be the cyclic binary four-input cellular automaton with local truth-table rule 56528, explicitly defined below. Put \(\mathcal A_N\) for the words on the cyclic \(N\)-site ring containing no cyclic occurrence of `101`, and \(\mathcal B_N\) for those containing no cyclic occurrence of `00`. Then the entire recurrent set is
\[
\boxed{\operatorname{Per}(F_N)=\mathcal A_N\cup\mathcal B_N.}
\]
All points of \(\mathcal A_N\) are fixed. Every point of \(\mathcal B_N\) evolves by a one-site cyclic shift, and \(\mathcal A_N\cap\mathcal B_N=\{1^N\}\). Every remaining state reaches a fixed point in at most \(N\) time steps.

Write \(A_N=|\mathcal A_N|\), and write \(L_1=1\), \(L_2=3\) and \(L_n=L_{n-1}+L_{n-2}\) for \(n\ge3\) (cyclic binary no-`00` counts, the Lucas sequence). The fixed-point counts are
\[
A_1=A_2=2,\quad A_3=5,\quad A_n=2A_{n-1}-A_{n-2}+A_{n-3}\quad(n\ge4).
\]
For every integer \(t\ge1\), the exact number of states fixed by the \(t\)-th iterate is
\[
\boxed{|\operatorname{Fix}(F_N^t)|=A_N-1+L_{\gcd(N,t)}.}
\]
Let \(\mu\) be the number-theoretic Möbius function. For each divisor \(d>1\) of \(N\), the number of primitive temporal cycles of length \(d\) is
\[
\boxed{c_d=\frac1d\sum_{e\mid d}\mu(d/e)L_e.}
\]
There are exactly \(A_N\) fixed cycles and no cycles whose lengths fail to divide \(N\). Consequently the complete Artin–Mazur zeta function of the finite ring is the rational function
\[
\boxed{Z_N(z)=(1-z)^{-A_N}\prod_{\substack{d\mid N\\ d>1}}(1-z^d)^{-c_d}.}
\]
In particular the number of all recurrent states is exactly \(A_N+L_N-1\). If \(\lambda\approx1.754877666\) denotes the real root of \(\lambda^3-2\lambda^2+\lambda-1=0\), then \(A_N\sim\lambda^N\), whereas \(L_N\sim\varphi^N\) with \(\varphi=(1+\sqrt5)/2\); frozen states therefore constitute an asymptotically full proportion of the recurrent set.

## Assumptions and scope
All indices are taken modulo \(N\), including for \(N=1,2\). For \(x\in\{0,1\}^N\), define
\[
(F_Nx)_i=x_i-x_i(1-x_{i+1})x_{i+2}+x_{i-1}(1-x_i)x_{i+1}.
\]
The right-hand side is always zero or one and agrees with the local four-bit truth table that gives output one for `0100`, `0110`, `0111`, `1010`, `1011`, `1100`, `1110`, `1111`, with neighborhood ordered as \((x_{i-1},x_i,x_{i+1},x_{i+2})\). The cyclic word `101` means a zero with two one-neighbors (an isolated zero). The cyclic word `00` means adjacent zeros; this includes a zero on a one-site ring, because indices wrap. The left shift is \((Sx)_i=x_{i+1}\).

## Proof
**Local particle lemma.** In every cyclic occurrence of `101`, the isolated middle zero swaps with the one immediately to its left. These swaps are simultaneous and pairwise disjoint, because isolated zeros cannot be adjacent. The stated polynomial identity is exactly the coordinatewise accounting of such swaps. A zero in an adjacent pair `00` never moves, because it cannot be the isolated center of `101`. Hence adjacent zero pairs are permanent, while every isolated zero moves one site to the left per step until it joins a zero cluster. The number of zeros is conserved.

**Classification of recurrence.** If a state contains no `101`, no swap occurs, so it is fixed. If it contains no `00`, every zero is isolated and all zeros move left one site; the ones consequently occupy the complementary sites, giving \(F_Nx=Sx\). Thus every such state is periodic with period dividing \(N\). The only word free of both `101` and `00` is the all-ones word. Finally suppose a cyclic state contains `00`. A fixed zero pair remains at its original sites for all time. Track each initially isolated zero: while isolated it advances left by one site each step; after encountering a permanent zero cluster it stays there. Other isolated zeros cannot obstruct the motion because they advance at the same speed until captured, whereupon the resulting cluster is itself permanent. Each isolated zero lies at cyclic leftward distance at most \(N\) from the initial permanent pair and therefore is captured within \(N\) updates. The resulting word has no `101` and is fixed. This excludes all additional periodic states.

**Fixed-word enumeration.** The four-state de Bruijn transfer matrix for cyclic avoidance of `101`, in the pair-state order `00`, `01`, `10`, `11`, is
\[
M=\begin{pmatrix}1&1&0&0\\0&0&1&1\\1&0&0&0\\0&0&1&1\end{pmatrix}.
\]
Its trace \(\operatorname{tr}(M^N)\) counts cyclic length-\(N\) words avoiding `101`, including repeated small-ring indices. Its characteristic polynomial is \(u(u^3-2u^2+u-1)\); direct traces for the first three positive powers are \(2,2,5\). Cayley–Hamilton therefore gives the displayed recurrence. Cyclic binary words with no `00` are counted by the corresponding two-state transfer matrix \(Q=\left(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\right)\), hence \(L_N=\operatorname{tr}(Q^N)\), with the stated initial values and Fibonacci-type recurrence.

**Exact iterates and cycles.** In the recurrent set, all \(A_N\) fixed points stay fixed. The remaining points lie in \(\mathcal B_N\setminus\{1^N\}\), where \(F_N\) is the shift \(S\). A cyclic length-\(N\) no-`00` word is fixed by \(S^t\) if and only if it repeats a cyclic word of length \(\gcd(N,t)\) avoiding `00`; there are exactly \(L_{\gcd(N,t)}\) such words, including the all-ones intersection. This proves the iterate formula. Möbius inversion of \(L_d=\sum_{e\mid d}e c_e\), with the all-ones orbit accounting for \(c_1=1\), gives all nontrivial primitive cycle counts. The finite-map Euler product defining \(Z_N(z)\) gives the displayed zeta factorization.

**Asymptotics.** The transfer matrix \(M\) is nonnegative and has a unique dominant eigenvalue \(\lambda\), the positive root of its cubic factor, with all other eigenvalues strictly smaller in modulus. Thus \(A_N=\operatorname{tr}(M^N)\sim\lambda^N\). Similarly \(L_N=\varphi^N+(-\varphi)^{-N}\). Since \(\lambda>\varphi\), the ratio of traveling recurrent states to all recurrent states tends to zero exponentially.

## Verification
The accompanying `verify.py` implements the eight output-one neighborhoods independently of the polynomial conservation identity. It exhaustively checks ring sizes \(1\le N\le12\), comparing single-step truth-table and polynomial updates, conservation, the absence-of-`101` fixed-state criterion, no-`00` shift behavior, absorption within \(N\) steps, fixed-point recurrences, and \(|\operatorname{Fix}(F_N^t)|\) for the tested times. It reports 24,676 successful exact-integer assertions. Finite checking does not establish the unrestricted statements; those follow from the local swap argument and transfer-matrix proof above.

## Relationship to prior work
Formenti and Kamilya (first posted June 11, 2026) establish finite-support temporal periodicity for a **different reversible second-order** cellular automaton, rule 115, motivating a precise comparison of periodic spectra. The four-input **irreversible number-conserving** rule studied here was introduced and analyzed much earlier by Fukś and Jin (2020), who explain its isolated-zero motion, absorbing clusters, blocking word and finite-block probability laws. Those qualitative particle rules are acknowledged prior knowledge. The present exact ring-by-ring recurrent-set classification, all-iterate periodic-point counts, Möbius cycle census and zeta product have not been located in the inspected sources. The de Bruijn and necklace enumeration techniques are classical; the claim is their complete exact specialization to the dynamical decomposition of this rule.

## Limitations
The result concerns one specific four-input rule on finite cyclic rings and gives no uniform convergence theorem for arbitrary bi-infinite initial states. The \(N\)-step freezing bound is a universal upper bound, not claimed optimal. The explicit exact orbit formulas have not been independently audited, and their historical priority beyond the literature inspected here remains uncertain. The 2020 source is not represented as a recent discovery; the new finite-periodicity context is supplied by the 2026 publication.

## References
- E. Formenti and S. Kamilya, *The Curious Case of Reversible Elementary Second Order Cellular Automaton 115*, EPTCS 445 (2026), 95–103. First arXiv posting 2026-06-11. DOI: 10.4204/EPTCS.445.12; arXiv:2606.13159.
- H. Fukś and Y. Jin, *Approximating dynamics of a number-conserving cellular automaton by a finite-dimensional dynamical system*, International Journal of Modern Physics C 31 (2020), 2050172. DOI: 10.1142/S0129183120501727. The later arXiv:2601.00479 posting does not change this earliest known publication date.
