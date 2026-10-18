# Three-point Fourier-minor rank incidence and a sharp singularity law on odd prime-power cycles

## Finding
Fix a prime \(p\ge5\) and an integer \(m\ge3\). Put \(N=p^m\), \(\zeta=e^{2\pi i/N}\), and consider the cyclic Fourier matrix
\[
F_N=(\zeta^{rc})_{r,c\in\mathbb Z_N}.
\]
For three distinct residues \(r_1,r_2,r_3\), define their **valuation type** \((u,v)\) by
\[
u=\min_{i<j}\nu_p(r_i-r_j),\qquad v=\max_{i<j}\nu_p(r_i-r_j),
\]
where nonzero differences are interpreted modulo \(N\), with valuations in \(\{0,\ldots,m-1\}\). The three pair valuations are exactly \((u,u,v)\), including the possibility \(u=v\). Let the row type be \((u,v)\) and column type \((s,t)\).

**Rank classification.** Every three-by-three minor has exactly the rank
\[
\operatorname{rank}F_N[R,C]=
\begin{cases}
1,&u+s\ge m,\\
2,&u+s<m\ \text{and}\ (v+s\ge m\ \text{or}\ u+t\ge m),\\
3,&\text{otherwise}.
\end{cases}
\]
In particular a three-by-three minor is singular **if and only if** its restricted matrix has two proportional rows or two proportional columns. For primes at least five, three-term cyclotomic cancellation creates no additional singular configurations.

**Complete rank census.** For \(0\le u\le v<m\), the number of three-element subsets of type \((u,v)\) is
\[
B_m(u,v)=\begin{cases}
\dfrac{(p-1)(p-2)}6p^{3m-2u-2},&u=v,\\[3pt]
\dfrac{(p-1)^2}2p^{3m-u-v-2},&u<v.
\end{cases}
\]
Define \(\kappa_m(u,v,s,t)\) by the displayed rank rule and \(C_{m,j}\) as the number of minors of rank \(j\), indexed by an unordered three-set of rows and an unordered three-set of columns. Then the exact finite formula
\[
C_{m,j}=\sum_{0\le u\le v<m}\ \sum_{0\le s\le t<m}
B_m(u,v)B_m(s,t)\,\mathbf1_{\{\kappa_m(u,v,s,t)=j\}},
\qquad j=1,2,3,
\]
counts all \(\binom N3^2\) minors by rank with integer arithmetic only.

**Sharp asymptotic law.** For every fixed prime \(p\ge5\), as \(m\to\infty\),
\[
\boxed{\lim_{m\to\infty}\frac{C_{m,1}+C_{m,2}}{N^5}=\frac{1}{6p}},
\qquad
\boxed{\lim_{m\to\infty}
N\frac{C_{m,1}+C_{m,2}}{\binom N3^2}=\frac6p}.
\]
Furthermore \(C_{m,1}=o(N^5)\): almost all singular minors have rank two. The result distinguishes the prime-dependent leading singularity probability within the family of prime-power Fourier matrices.

## Assumptions and scope
The ground field is \(\mathbb C\), the character exponent is understood modulo \(N\), all row and column sets contain exactly three distinct residues, and each minor is counted once per unordered choice of each index triple. The prime \(p\) is fixed when taking the limit. The hypothesis \(p\ge5\) is essential to the short cyclotomic cancellation argument below; no rank classification for the excluded ternary case is asserted. The classification and counting identities also hold at exponents one and two, but those instances are used only as checks and are not proposed as new discoveries here.

## Proof
**1. Three-point valuation geometry.** For any three distinct residues modulo a prime power, the minimum of their three pair-difference valuations is attained at least twice. Indeed, if one difference has valuation strictly greater than another, their difference has valuation equal to the smaller one. The type is consequently \((u,u,v)\). Translation of row indices and translation of column indices multiply selected rows and columns by nonzero scalars, and hence preserve rank. Normalize the triples to \(R=\{0,a,b\}\), \(C=\{0,c,d\}\).

**2. A six-term cyclotomic rigidity lemma.** For a primitive \(p^m\)-th root \(\zeta\), with \(p\ge5\), suppose
\[
\zeta^{e_1}+\zeta^{e_2}+\zeta^{e_3}
=\zeta^{f_1}+\zeta^{f_2}+\zeta^{f_3}.
\]
Then the two three-element **multisets of exponent residues modulo \(p^m\)** are equal, including multiplicities. To prove this, make the integer polynomial \(Q(X)=\sum X^{e_j}-\sum X^{f_j}\), using representatives from \(0\) through \(p^m-1\). Since \(Q(\zeta)=0\), the cyclotomic polynomial \(\Phi_{p^m}(X)=\sum_{k=0}^{p-1}X^{k p^{m-1}}\) divides \(Q\). As \(\deg Q<p^m\), division forces coefficients of \(Q\) at each group of indices \(r+k p^{m-1}\) to be equal. If any such common integer is positive, that group requires at least \(p\ge5\) positive monomials, but there are only three. If negative, at least \(p\) negative monomials are required. Every common coefficient is therefore zero and the multisets coincide.

**3. Determinant and rank.** With \(A=ac\), \(B=ad\), \(C=bc\), and \(D=bd\) modulo \(N\), the determinant vanishes precisely if
\[
\zeta^{A+D}+\zeta^B+\zeta^C=\zeta^{B+C}+\zeta^A+\zeta^D.
\]
By the lemma, \(A+D\) must match one of \(B+C,A,D\). If it matches \(B+C\), matching the remaining two terms either gives \(B=A,C=D\), so the columns at \(c,d\) are equal on all selected rows, or \(B=D,C=A\), so the rows at \(a,b\) are equal on all selected columns. If \(A+D=A\), then \(D=0\), and matching \(B,C\) with \(B+C,0\) forces \(B=0\) or \(C=0\), so respectively the column at \(d\) or the row at \(b\) equals the zero-index column or row. The case \(A+D=D\) is symmetric. Thus any singular three-by-three minor has a duplicate restricted row or column. Conversely either duplication makes the determinant zero.

A difference \(h\) between two rows yields proportional restricted rows precisely when \(\zeta^{h(c-c')}=1\) for every selected column difference, that is, \(\nu_p(h)+s\ge m\). There is some such row pair precisely when \(v+s\ge m\). Similarly, some two restricted columns coincide precisely when \(u+t\ge m\). The entire matrix has rank one precisely when **every** row pair coincides up to scalar, equivalently \(u+s\ge m\). If the determinant is zero but that last inequality fails, the rank is two, proving the displayed classification without numerical approximation.

**4. Exact number of each valuation type.** When \(u=v\), the three indices are congruent modulo \(p^u\), and their next base-\(p\) digits are all distinct. Choosing a lower-digit residue, three distinct next digits, and the higher digits gives
\[
p^u\binom p3 p^{3(m-u-1)}
=\frac{(p-1)(p-2)}6p^{3m-2u-2}.
\]
When \(u<v\), exactly one pair agrees modulo \(p^{u+1}\). Choose the common \(u\) lower digits, the repeated next digit, the distinct next digit for the singleton, the intermediate digits of the repeated pair, two distinct digits at valuation \(v\), and the unconstrained higher digits. This gives
\[
p^u p(p-1)p^{v-u-1}\binom p2p^{2(m-v-1)}p^{m-u-1}
=\frac{(p-1)^2}2p^{3m-u-v-2}.
\]
Every three-set has exactly one type, and multiplication of row and column type counts establishes the census formula.

**5. Sharp asymptotics.** Choose \(R,C\) independently and uniformly from all three-subsets. Write \(U=\min\nu_p(r_i-r_j)\), \(V=\max\nu_p(r_i-r_j)\) and write \(S,T\) similarly for columns. The singular event is the union
\[
E=\{U+T\ge m\},\qquad E'=\{V+S\ge m\}.
\]
For each fixed positive integer \(a\), elementary selection with replacement errors vanishing as \(m\to\infty\) gives
\[
\Pr(U=a)\longrightarrow(1-p^{-2})p^{-2a}.
\]
For \(1\le a\le m\), counting close pairs and applying inclusion--exclusion gives the **exact** identity
\[
\Pr(T\ge m-a)=\frac{3(p^a-1)}{N-1}
-\frac{2(p^a-1)(p^a-2)}{(N-1)(N-2)}.
\]
Hence for fixed \(a\), \(N\Pr(T\ge m-a)\to3(p^a-1)\). The bounds \(\Pr(U=a)\le K_p p^{-2a}\) and \(N\Pr(T\ge m-a)\le K'_p p^a\), with constants independent of \(a,m\), permit dominated convergence and imply
\[
\lim_{m\to\infty}N\Pr(E)
=3(1-p^{-2})\sum_{a\ge1}(p^{-a}-p^{-2a})
=\frac3p.
\]
By swapping row and column roles, \(\lim N\Pr(E')=3/p\).

The intersection has lower order. Fix \(L\). On \(U,S\le L\), membership in both events forces \(V,T\ge m-L\); independence of the row and column triples gives probability \(O_p(p^{2L}N^{-2})\). The complementary portions of \(E\cap E'\) are bounded by \(\Pr(E,U>L)+\Pr(E',S>L)\), each at most \(O_p(p^{-L}N^{-1})\), by the same summable bounds. First let \(m\to\infty\), then \(L\to\infty\), proving \(N\Pr(E\cap E')\to0\). Therefore \(N\Pr(E\cup E')\to6/p\). Since \(\binom N3^2\sim N^6/36\), this is equivalent to the asserted singular-count asymptotic \(1/(6p)\).

Finally the rank-one event \(U+S\ge m\) has probability \(O_p(m p^{-2m})=O_p(m/N^2)\), using the same geometric tails, and so its contribution to the \(N^{-1}\) singular probability is negligible. This completes the proof.

## Verification
The accompanying Python-3 standard-library program `verify_fourier_primepowers.py` directly reduces determinant exponent multisets modulo \(\Phi_{p^m}\) using integer coefficients. It checks all translation-normalized three-row and three-column minor pairs at orders \(25\) and \(49\), compares ranks against the valuation rule without floating-point tolerances, checks the exact type multiplicities and resulting rank census, checks selected higher-power configurations and tests the asymptotic formulas numerically for several primes and exponents. The successful execution marker is `VERIFY_OK 1354256 exact comparisons and integer checks`.

These finite checks do **not** prove the infinite-family statement; the cyclotomic, counting, and dominated-convergence arguments above do. The examples at prime-square order are calibration against a previously published rank classification and are not presented as new prime-square research.

## Relationship to prior work
Gu, Zhou, and Wang (2026, first public August 18) address **principal** nonsingularity of Fourier matrices of orders \(70\) and \(143\), motivating closer scrutiny of which arithmetic Fourier minors can be singular. Their theorem concerns different moduli and principal minors and does not imply the all-index, prime-power census or its asymptotic probability.

A published prime-square classification, *All singular three-by-three minors of prime-square Fourier matrices* (2026), already proves the valuation-zero pattern and exact count when the exponent is two; the present work credits that special case and extends the object to **every exponent at least three**, with a sharp all-order probability law. More general prime-power full-spark criteria classify whether some minors can vanish for a fixed row pattern, but not the count of all ranks across independent row and column triples.

Delvaux and Van Barel (2008) study rank-deficient blocks of prime-power Fourier matrices. The accessible abstract states the scope as maximal rank-deficient submatrices, so it is a significant possible source of a stronger structural result. Its full text could not be inspected. Consequently, the novelty comparison for its implications is provisional; no historical-priority certification is claimed.

## Limitations
The theorem treats exactly three-by-three submatrices of cyclic Fourier matrices with a **fixed** prime at least five. It says nothing about arbitrary bigger minors, the ternary prime, non-cyclic groups, or stability under approximate zeros. The exact counts use O(\(m^4\)) finite sums and may be algebraically reducible. The historical-priority risk from unavailable older prime-power rank-deficiency literature remains real. No independent external audit has been performed.

## References
1. J. Gu, L. Zhou, Y. Wang, *Principal nonsingularity of the Fourier matrices of orders 70 and 143*, arXiv:2608.17746v1 (2026-08-18), https://arxiv.org/abs/2608.17746.
2. W. Zhou, *Principal Non-singularity of Fourier Matrices on Zp×Zq and Z2^k×Zq*, arXiv:2505.01189 (2025-05-02), https://arxiv.org/abs/2505.01189.
3. *All singular three-by-three minors of prime-square Fourier matrices*, publicly available research result (2026-10-04), whose complete proof and enumeration were inspected for the exponent-two comparison.
4. S. Delvaux, M. Van Barel, *Rank-deficient submatrices of Fourier matrices*, Linear Algebra Appl. 429 (2008), 1587–1605, doi:10.1016/j.laa.2008.04.043 (abstract accessible, full text unavailable).
5. B. Alexeev, J. Cahill, D. G. Mixon, *Full Spark Frames*, arXiv:1110.3548 (2011-10-17), https://arxiv.org/abs/1110.3548.
