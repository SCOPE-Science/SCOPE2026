# Sharp two-orbit conductor for three consecutive return lengths

## Finding
For each integer \(a\ge2\), consider the two-sided binary \(S\)-gap shift \(X_a\) in which the number of zeros between consecutive occurrences of \(1\) belongs to \(\{a-1,a,a+1\}\). Let \(Q_a(n)\) count distinct shift orbits of **exact least period** \(n\), counting each orbit once. Define
\[
M(a)=\begin{cases}
6,&a=2,\\
\frac{(a+1)(a+2)}2,&a\ge3\text{ odd},\\
\frac{a(a+2)}2+1,&a\ge4\text{ even}.
\end{cases}
\]
Then
\[
Q_a(M(a))=1,\qquad Q_a(n)\ge2\quad\text{for every integer }n>M(a).
\]
Thus \(M(a)\) is precisely the largest integer period admitting fewer than two distinct primitive shift orbits; the conductor has a sharp parity-sensitive quadratic formula, with the exceptional smallest case \(a=2\).

## Assumptions and scope
We take the shift as the compact two-sided subshift obtained from concatenating return blocks \(10^{g-1}\) of lengths \(g\in\{a,a+1,a+2\}\), including every compatible limit point. Periodic sequences containing a \(1\) correspond bijectively to cyclic ordered lists (necklaces) of these return lengths; a cyclic list has least binary period equal to its total length exactly when it is primitive (not a nontrivial repetition). Any isolated all-zero orbit, under a convention that includes it, has least period \(1\) and does not affect the asserted range. A necklace is counted only once under cyclic rotation; reversal is **not** identified.

## Proof
**1. Two primitive necklaces at interior weights.** Write each return length as \(a+e_i\), where \(e_i\in\{0,1,2\}\). For every integer \(\ell\ge3\) and every \(e\) with \(2\le e\le2\ell-2\), there exist at least two inequivalent primitive cyclic words \((e_1,\ldots,e_\ell)\) of sum \(e\). Reflection \(e_i\mapsto2-e_i\) reduces to \(2\le e\le\ell\).

For \(2\le e<\ell\), use the following two cyclic words, written as their consecutive blocks:
\[
U_e=(2,1^{e-2},0^{\ell-e+1}),\qquad
V_e=(1^e,0^{\ell-e}).
\]
Both have sum \(e\). The first contains a unique symbol \(2\), and thus is primitive; the second has one nonempty run each of \(1\)'s and \(0\)'s, and is primitive. Their distinct symbol content makes them inequivalent. This includes \(e=2\). For the central value \(e=\ell\), take
\[
U_\ell=(0,2,1^{\ell-2}),\qquad
V_\ell=(0,1,2,1^{\ell-3}).
\]
Each has one \(0\) and one \(2\), hence is primitive. They are inequivalent since the symbol immediately after the unique \(0\) is \(2\) in one and \(1\) in the other. The expressions remain valid for \(\ell=3\). Reflection then proves the entire interior-weight lemma.

Consequently every period in
\[
I_\ell=[\ell a+2,\,\ell(a+2)-2]\cap\mathbb Z,\qquad\ell\ge3,
\]
supports at least two distinct primitive binary periodic orbits.

**2. Odd \(a\).** Write \(a=2k+1\), \(k\ge1\), and put \(L=k+2\). Then \(M(a)=La+1\) and the intervals \(I_\ell\), \(\ell\ge L\), cover every integer \(n\ge La+2=M(a)+1\). Indeed the number of integers strictly between successive intervals is
\[
(\ell+1)a+2-[\ell(a+2)-2]-1=a+3-2\ell\le0
\]
for \(\ell\ge L\). At \(n=M(a)\), the only possible primitive necklace has \(L\) return blocks with total excess \(1\), hence is the unique cyclic necklace \((1,0^{L-1})\). The shortest possible total with \(L+1\) blocks is \((L+1)a>M(a)\). With at most \(L-1=k+1\) blocks, the largest possible total is \((k+1)(a+2)=M(a)\); equality would require a constant all-\(2\) necklace, which is not primitive because \(k+1\ge2\). Therefore \(Q_a(M(a))=1\).

**3. Even \(a\ge4\).** Write \(a=2k\), \(k\ge2\), and put \(L=k+1\). Now \(M(a)=La+1\). The interval \(I_L\) starts at \(M(a)+1\). It covers through \((L+1)a\), and \(I_{L+1}\) begins at \((L+1)a+2\), leaving precisely the one period \(n_*=(L+1)a+1\). At this missing period are two different primitive necklaces: the \(L\)-block necklace of excess \(2L-1\), containing one \(1\) and \(L-1\) copies of \(2\), and the \((L+1)\)-block necklace of excess \(1\), containing one \(1\) and \(L\) copies of \(0\). They have different numbers of return blocks and both are primitive. For \(\ell\ge L+1\), the intervals \(I_\ell\) overlap or meet, since \(a+3-2\ell\le-1\). Thus every \(n>M(a)\) has at least two primitive orbits. At \(M(a)\), no necklace has \(L+1\) or more blocks because \((L+1)a>M(a)\), and none with at most \(k\) blocks reaches \(M(a)\), because \(k(a+2)=La=M(a)-1<M(a)\). Exactly one primitive \(L\)-block necklace remains: excess \(1\).

**4. Exceptional \(a=2\).** At length \(6\), the only primitive return necklace is \((2,4)\), so \(Q_2(6)=1\). At length \(7\) there are two inequivalent primitive necklaces, \((3,4)\) and \((2,2,3)\). The intervals \(I_\ell\) for \(\ell\ge3\) start at \(8\) and have no gaps, so every \(n>6\) has at least two primitive orbits. This completes all cases.

## Verification
An independently implemented exact-arithmetic diagnostic (`verify.py`) calculates the renewal coefficients \(c_0=1\), \(c_n=\sum_{g\in\{a,a+1,a+2\},\ g\le n}c_{n-g}\), and fixed-point counts
\[
F_n=\sum_{g\in\{a,a+1,a+2\},\ g\le n}g\,c_{n-g}.
\]
It computes the primitive orbit count by Möbius inversion,
\[
Q_a(n)=\frac1n\sum_{d\mid n}\mu(d)F_{n/d}.
\]
For every \(a\in\{2,\ldots,46\}\), all \(n\le M(a)+4(a+2)\) were checked, including the claimed boundary and every subsequent tested period. There were 27,550 exact-integer assertions, plus 308 comparisons against a separate brute enumeration of primitive necklaces for \(2\le a\le9\). The verifier is Python standard-library only, runnable with `python3 verify.py` and requiring no other files. These tests check arithmetic and coding, but the infinite statement follows from the proof above, not finite enumeration.

## Relationship to prior work
Haydarov, Kadyrov, Makhmudov and Mamayusupov (2026) study inducing and effective intrinsic ergodicity for renewal-type potentials on \(S\)-gap shifts, motivating attention to the finite-return-alphabet dynamics; their theorems concern pressure and equilibrium measures, not the two-primitive-orbit cutoff. De Jong (2025) classifies sets of **attainable least periods** for gap shifts, which does not classify the number of primitive orbits at each period. Dastjerdi and Jangjoo (2011) derive the finite-gap dynamical zeta function \(1/[1-\sum_g z^g]\); this prior result determines orbit counts coefficientwise, but does not itself give the parity-sensitive sharp conductor for all \(a\). The present claim is the uniformly sharp closed threshold and its necklace proof, not the known zeta identity or general existence classification.

## Limitations
The classification is restricted to precisely three **consecutive** return lengths and the multiplicity level two. It does not classify arbitrary three-gap sets, stronger multiplicity thresholds, or invariant-measure statistics. A general zeta formula is already known. Historical priority under other necklace or renewal-system formulations remains a risk; no independent external novelty audit was performed.

## References
1. F. Haydarov, S. Kadyrov, M. Makhmudov, K. Mamayusupov, *Effective Intrinsic Ergodicity for renewal-type potentials on S-gap shifts*, arXiv:2606.17031v1 (15 June 2026), primary MSC2020 37B10.
2. H. de Jong, *On Sets of Periodic Orbit Lengths in Finitely Presented Dynamical Systems*, arXiv:2510.10848v1 (2025), §3.3 and Theorem 3.19.
3. D. Ahmadi Dastjerdi, S. Jangjoo, *Computations on Sofic S-gap Shifts*, arXiv:1108.3414 (2011), dynamical zeta computation.
