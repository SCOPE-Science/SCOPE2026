# Exact fibers and uniquely reconstructible profiles for cyclic four-gram reads under a binary run-length constraint

## Finding

Let \(\mathcal N_n\) be the necklaces (oriented cyclic words modulo rotation, **not** reflection) of length \(n\ge1\) over \(\{0,1\}\) with no cyclic occurrence of \(11\). Observe each word through the multiplicities of its oriented cyclic length-four factors, counting wraparound windows even when \(n<4\). The eight permitted factors, in order, are
\[
0000,\ 0001,\ 0010,\ 0100,\ 0101,\ 1000,\ 1001,\ 1010.
\]
All other four-gram counts are zero. For a profile, set
\[
A=N_{0000},\quad B=N_{0001},\quad G=N_{1001},\quad E=N_{0101}.
\]

**Exact feasibility.** A nonnegative integer vector is realized by an element of \(\mathcal N_n\) if and only if
\[
N_{1000}=B,\quad N_{0010}=N_{0100}=B+G,\quad N_{1010}=E,\quad n=A+4B+3G+2E,
\]
and one of the following disjoint cases holds:

1. \(B\ge1\), with arbitrary \(A,G,E\ge0\);
2. \(B=A=0\), with \(G+E\ge1\);
3. \(B=G=E=0\), with \(A\ge1\) (the all-zero word).

**Exact ambiguity fibers.** Let \(F(A,B,G,E)\) count distinct necklaces realizing the profile, and let \(\varphi\) be Euler's totient function. For \(B\ge1\) and \(t=B+G+E\),
\[
F(A,B,G,E)=\frac1t\sum_{d\mid\gcd(A,B,G,E)}\varphi(d)
\frac{(t/d)!}{(B/d)!(G/d)!(E/d)!}
\binom{A/d+B/d-1}{B/d-1}.
\]
For \(B=A=0\) and \(t=G+E\ge1\),
\[
F(0,0,G,E)=\frac1t\sum_{d\mid\gcd(G,E)}\varphi(d)\binom{t/d}{G/d}.
\]
The all-zero case has fiber size one.

**Complete uniqueness classification.** A realizable profile has fiber size exactly one precisely in these cases:

1. \(B=0\), either the all-zero case, or \(A=0\) and \(\min(G,E)\le1\);
2. \(B=1\) and \(GE=0\), with arbitrary \(A\);
3. \(B\ge2, A=0\), and either \(G=0,E\le1\) or \(E=0,G\le1\);
4. \(B\ge2,A=1,G=E=0\).

Let \(C_n\) be the number of realizable profiles and \(U_n\) the number of uniquely reconstructible profiles. Their exact ordinary generating functions are
\[
\begin{aligned}
\sum_{n\ge1}C_nz^n={}&\frac{z}{1-z}+\frac{z^2}{1-z^2}
+\frac{z^3}{(1-z^3)(1-z^2)}
+\frac{z^4}{(1-z^4)(1-z)(1-z^3)(1-z^2)},\\
\sum_{n\ge1}U_nz^n={}&\frac{z}{1-z}+\frac{z^2}{1-z^2}
+\frac{z^3+z^5}{1-z^3}+\frac{z^7}{1-z^2}
+\frac{z^4}{(1-z)(1-z^3)}
+\frac{z^6}{(1-z)(1-z^2)}+\frac{z^8}{1-z}.
\end{aligned}
\]
Thus \(C_n\) is a degree-three quasipolynomial of **least period twelve**, while \(U_n\) is a degree-one quasipolynomial of **least period six**. In particular,
\[
C_n=\frac{n^3}{144}+O(n^2),\qquad
U_n=\frac{5n}{6}+O(1),\qquad
\frac{U_n}{C_n}=\frac{120}{n^2}+O(n^{-3}).
\]
The exact counts for \(n=1,\ldots,12\) are
\[
(C_n)=(1,2,2,3,3,5,5,8,9,12,14,19),\quad
(U_n)=(1,2,2,3,3,5,5,8,8,9,10,11).
\]
Consequently, **all profiles reconstruct their necklace uniquely through length eight**, but the first ambiguity occurs at length nine. The two distinct gap necklaces \((1,2,3)\) and \((1,3,2)\) share the same length-nine profile \((A,B,G,E)=(0,1,1,1)\).

## Assumptions and scope

A necklace identifies rotations but not reversals. A cyclic factor of length four is read with indices modulo \(n\), so windows are well-defined at lengths below four. The source is restricted to binary words avoiding cyclic adjacent \(11\). Equality of observations means equality of all **multiplicities**, not merely equality of the support of the set of factors. Every zero-error code for this noiseless read-multiset observation contains at most one necklace from each fiber, and therefore has maximum size exactly \(C_n\). This is a constrained read channel, not the unconstrained binary four-gram channel.

## Proof

**Step 1: gap-necklace normal form.** Any admissible necklace with at least one \(1\) admits a gap representation by a cyclic sequence of positive integers \((\ell_1,\ldots,\ell_t)\), the numbers of zeros between successive ones. Conversely, a positive integer gap necklace uniquely determines an admissible binary necklace. Rotating the binary word permutes the choice of the starting one and hence corresponds exactly to cyclic rotation of the gap list. In particular the argument holds for imprimitive necklaces.

**Step 2: every window is accounted for locally.** A gap of length one contributes exactly one window each of \(0101\) and \(1010\); a gap of length two contributes one each of \(1001,0010,0100\); a gap of length \(3+r\), \(r\ge0\), contributes one each of \(1000,0001,0010,0100\) and \(r\) occurrences of \(0000\). To verify these assertions, anchor the windows at the unique junctions with a one and count windows lying entirely in the gap interior. Each cyclic window has a unique placement relative to the immediately preceding and following ones, and all cases are disjoint. It follows that \(E\) counts the gaps of length one, \(G\) the gaps of length two, \(B\) the gaps of length at least three, and \(A\) is the sum of the excess lengths above three among those \(B\) long gaps. This proves the linear identities and the length equation. If \(B=0\), no gap contributes \(0000\), forcing \(A=0\). If no ones occur, the sole word is all zero. Every listed feasible tuple has an explicit gap composition, proving sufficiency.

**Step 3: orbit enumeration.** The fiber for \(B\ge1\) consists of necklaces of \(t=B+G+E\) gaps with \(E\) entries equal to one, \(G\) entries equal to two and \(B\) entries \(3+r_j\) with \(r_j\ge0\) and \(\sum_jr_j=A\). Apply Burnside's lemma to cyclic rotations of the \(t\) gap indices. A rotation with repetition number \(d\) fixes a gap sequence only when \(d\) divides all four parameters. Then the reduced period has \(B/d,G/d,E/d\) entries of the three types, so the number of type orders is the displayed multinomial coefficient. Stars and bars assigns the remaining \(A/d\) excess zeroes among \(B/d\) long gaps in \(\binom{A/d+B/d-1}{B/d-1}\) ways. Exactly \(\varphi(d)\) rotations have repetition number \(d\). Dividing by \(t\) proves the first fiber formula. If \(B=0\), only one- and two-zero gaps remain, yielding the binary-necklace Burnside formula. The separate all-zero case is immediate.

**Step 4: singleton fibers.** For a cyclic word over two distinct gap types, there is a single necklace if and only if at least one type appears once: a unique minority symbol fixes the rotation, while if both types appear at least twice, grouped and split arrangements have respectively two and at least four type boundaries. With three distinct gap types, arrangements whose three type blocks have opposite cyclic orders yield two distinct necklaces. These observations settle \(A=0\). If \(B=1\), the one long gap has fixed length \(3+A\), so at most one short-gap type may appear for uniqueness. If \(B\ge2\) and \(A=1\), exactly one long gap has length four and the others length three: uniqueness persists only when no short gaps appear. If \(B\ge2\) and \(A\ge2\), the excess distributions \((A,0,\ldots,0)\) and \((A-1,1,0,\ldots,0)\) give distinct unordered multisets of gap lengths, hence different necklaces. This proves all and only the stated singleton cases.

**Step 5: exact generating functions.** In the case \(B\ge1\), choosing \(A,G,E\ge0\) and \(B\ge1\) with weight \(A+4B+3G+2E\) gives the fourth summand of \(\sum C_nz^n\). The other three terms count the all-zero, all-one-zero-gap, and two-gap-type cases with \(B=0\). For \(U_n\), singleton profiles with no long gap contribute the two pure types and the two mixed cases with one exceptional short-gap type; \(B=1\) contributes the two rational products; and \(B\ge2\) gives exactly one profile at each length \(n\ge8\), producing \(z^8/(1-z)\). This yields the second rational function.

The reduced denominator of the first rational function is, up to a nonzero scalar,
\[(1-z)^4(1+z)^2(1+z^2)(1+z+z^2),\]
and the reduced denominator of the second is
\[(1-z)^2(1+z)(1+z+z^2).\]
Their numerators share no cyclotomic factor with these denominators (directly verified by substitution or polynomial division). The poles at primitive third and fourth roots in the first, and at primitive second and third roots in the second, force least quasipolynomial periods twelve and six respectively; partial fractions give the stated degrees and leading coefficients. Comparing coefficients shows equality \(C_n=U_n\) through \(n=8\); the explicit length-nine gap pair realizes \(C_9-U_9=1\). This completes the proof.

## Verification

Execute `python3 verify.py` from the package's extracted directory. The stdlib-only checker independently enumerates all admissible indexed binary words at every length \(1\le n\le20\), quotients by rotations, constructs literal cyclic four-gram vectors, and compares each observed fiber cardinality to the totient formula and each singleton decision to the structural classification. It checks exact feasible-vector counts through length sixty and the first ambiguous length, including \((C_{20},U_{20})=(69,18)\). The finite verifier is corroboration, not a proof for arbitrary \(n\); the five arguments above establish the universal statements.

## Relationship to prior work

Kiah, Puleo and Milenkovic [1] develop sequence-profile equivalence and restricted de Bruijn graphs and prove general quasipolynomial estimates for constrained read profiles. Those results motivate the observation model but do not state the exact fiber-by-fiber Burnside formula or the singleton reconstruction classification here. Chee and collaborators [2] study run-length-limited necklaces in de Bruijn graphs and maximum-length sequences with distinct windows; their counting targets differ from multiplicity-only read fibers. Chee and collaborators [3] study constrained de Bruijn codes defined by a separation restriction on *repeated* windows, rather than arbitrary repetitions and indistinguishability under a complete read multiset. Classical necklace enumeration is used as a method, not claimed as new. The claim is precisely the explicit feasibility, fiber, and singleton/capacity classification for the specified constrained cyclic read observation.

## Limitations

The theorem assumes exact noiseless cyclic counts, avoidance of cyclic \(11\), a binary alphabet and read length four. It does not give noisy decoding bounds, reconstruction from incomplete reads, or the unconstrained four-gram capacity. An equivalent expression could be implicit in earlier high-order Markov-type literature; this has not been independently ruled out. The proof is mathematical and the accompanying computational checks are finite. No independent scientific validation has been performed.

## References

1. H. M. Kiah, G. J. Puleo and O. Milenkovic, *Codes for DNA Sequence Profiles*, arXiv:1502.00517 (first public February 2, 2015). https://arxiv.org/abs/1502.00517
2. Y. M. Chee, T. Etzion, T. L. Nguyen, D. H. Ta, V. D. Tran and V. K. Vu, *Maximum Length RLL Sequences in de Bruijn Graph*, arXiv:2403.01454v1 (first public March 3, 2024). https://arxiv.org/html/2403.01454v1
3. Y. M. Chee, T. Etzion, H. M. Kiah, A. Vardy, V. K. Vu and E. Yaakobi, *Constrained de Bruijn Codes: Properties, Enumeration, Constructions, and Applications*, arXiv:2005.03102 (first public May 6, 2020). https://arxiv.org/abs/2005.03102
4. F. Bianconi and E. Brugnoli, *Enumerating Necklaces with Transitions*, Bulletin of the Australian Mathematical Society (published online May 11, 2021). https://www.cambridge.org/core/journals/bulletin-of-the-australian-mathematical-society/article/abs/enumerating-necklaces-with-transitions/E4C43D3F6F9DC9E6C6E9DEA1570C702D
