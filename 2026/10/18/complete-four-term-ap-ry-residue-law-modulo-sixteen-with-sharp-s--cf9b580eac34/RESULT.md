# Complete four-term Apéry residue law modulo sixteen with sharp square-root discrepancy

## Finding
For \(n\ge0\), define the Apéry number
\[
 A_n=\sum_{k=0}^{n}\binom nk^2\binom{n+k}{k}^2.
\]
For an integer \(m\ge0\), let \(b_j(m)\in\{0,1\}\) denote its \(j\)-th binary digit, with \(b_j(m)=0\) for sufficiently large \(j\), and put
\[
 r(m)=\sum_{j\ge0}b_{j+1}(m)(1-b_j(m))\pmod2.
\]
The symbol \(\oplus\) denotes addition in \(\mathbb F_2\). For arbitrary \(p,u,v,w\in\{0,1\}\), define four-term residue words
\[
 E(p,u,v)=\bigl(1+8(u\oplus p),\;5+8u,\;1+8(v\oplus(1-p)),\;5+8v\bigr)
\]
and
\[
 O(p,u,v,w)=\bigl(5+8u,\;1+8(v\oplus(1-p)),\;5+8v,\;1+8(w\oplus p)\bigr).
\]
**Theorem.** The four-consecutive-term residue vector \((A_n,A_{n+1},A_{n+2},A_{n+3})\bmod16\) belongs to exactly 24 possible words. Eight are the mutually distinct words \(E(p,u,v)\) and sixteen are the mutually distinct words \(O(p,u,v,w)\). Every \(E\)-word has natural density \(1/16\) and every \(O\)-word has natural density \(1/32\). No other word occurs. More precisely, for every fixed word \(z\), its number of occurrences with \(0\le n<N\) is \(\mu(z)N+O(\sqrt N)\), where \(\mu(z)\) is the preceding rational density (zero for forbidden words).

The square-root exponent cannot be improved for all words: for each \(m\ge1\),
\[
 \#\{0\le n<2^{4m+1}:(A_n,A_{n+1},A_{n+2},A_{n+3})\equiv(1,5,9,5)\pmod{16}\}
 =2^{4m-3}-(-4)^{m-1}.
\]
Thus the discrepancy in this cell has absolute value \(2^{2m-2}\) along an unbounded sequence of cutoffs.

## Assumptions and scope
All indices are nonnegative integers. Ordinary natural density is defined using all cutoffs \(N\to\infty\), not merely powers of two. Each tuple entry is reduced modulo 16. There are only 32 quadruples compatible with the known alternation of the residue classes \(\{1,9\}\) and \(\{5,13\}\); exactly eight of those 32 are forbidden. The asymptotic implied constant may depend on the fixed word but is independent of \(N\). No claims are made about longer blocks or congruences modulo 32.

## Proof
**1. Binary formula.** The binomial identity
\[
 \binom nk\binom{n+k}k=\binom{2k}k\binom{n+k}{2k}
\]
and the classical formula \(\nu_2\!\left(\binom{2k}k\right)=s_2(k)\) imply that, modulo 16, only \(k=0\) and \(k=2^j\) can contribute to the Apéry sum. For \(k=2^j\), the square of the central binomial factor is congruent to 4 modulo 16. By Lucas's theorem, \(\binom{n+2^j}{2^{j+1}}\) is odd exactly when \(b_j(n)\oplus b_{j+1}(n)=1\). Therefore
\[
 A_n\equiv1+4\sum_{j\ge0}\bigl(b_j(n)\oplus b_{j+1}(n)\bigr)\pmod{16}.
\]
Counting transitions from the least significant digit up to the eventual zero digit yields \(\sum_j(b_j\oplus b_{j+1})=b_0+2\sum_j b_{j+1}(1-b_j)\), so
\[
 \boxed{A_n\equiv1+4(n\bmod2)+8r(n)\pmod{16}.}\tag{1}
\]
This congruence is a rederivation of the pointwise congruence of Rowland and Yassawi, Theorem 3.28, and is **not** asserted to be new.

**2. Eight-state transfer.** The digit statistic has exact recursions
\[
 r(2t)=r(t)\oplus(t\bmod2),\qquad r(2t+1)=r(t).
\]
Attach to each integer \(t\) the state \(s(t)=(t\bmod2,r(t),r(t+1))\). From a state \((p,u,v)\), appending one binary digit gives
\[
 s(2t)=(0,u\oplus p,u),\qquad s(2t+1)=(1,u,v\oplus(1-p)).\tag{2}
\]
Order the eight states lexicographically as \((0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0),(1,1,1)\). The transfer matrix (each column has its two destinations as ones) is
\[
 M=\begin{pmatrix}
1&1&0&0&0&0&0&0\\
0&0&0&0&0&0&1&1\\
0&0&0&0&1&1&0&0\\
0&0&1&1&0&0&0&0\\
0&1&0&0&1&0&0&0\\
1&0&0&0&0&1&0&0\\
0&0&0&1&0&0&1&0\\
0&0&1&0&0&0&0&1
\end{pmatrix}.
\]
A direct integer-matrix multiplication establishes the annihilating polynomial
\[
 M^2(M-2I)(M-I)(M^2-2M+2I)=0.\tag{3}
\]
In addition, \(M\mathbf1=2\mathbf1\), and \(2\) is a simple eigenvalue (the characteristic polynomial is \(x^3(x-2)(x-1)^2(x^2-2x+2)\)). Thus for every basis vector \(e_s\),
\[
 M^Le_s=\frac{2^L}{8}\mathbf1+O\bigl((\sqrt2)^L\bigr),\tag{4}
\]
entrywise, since all other nonzero eigenvalues have modulus at most \(\sqrt2\) and are semisimple by (3); the nilpotent part disappears after at most two iterations. The stationary projection has coefficient \(1/8\) because \(M\) has column sums two and the initial vector sums to one.

For any \(q\ge0\), the states \(s(q2^L+t)\) as \(0\le t<2^L\) are produced by appending the \(L\) arbitrary lower bits of \(t\) to the fixed binary prefix \(q\); hence their exact count vector is \(M^Le_{s(q)}\). Formula (4) therefore gives \(2^L/8+O(2^{L/2})\) for each state, **uniformly over all aligned dyadic blocks**. Decomposing \([0,N)\) into disjoint aligned dyadic intervals, whose lengths decrease geometrically, yields
\[
 \#\{0\le t<N:s(t)=s\}=N/8+O(\sqrt N)\tag{5}
\]
for every state \(s\). This also proves ordinary natural density.

**3. Four consecutive residues.** For even starting positions \(n=2t\), equations (1) and (2) give exactly
\[
 (A_{2t},A_{2t+1},A_{2t+2},A_{2t+3})\equiv E(t\bmod2,r(t),r(t+1))\pmod{16}.\tag{6}
\]
For odd starting positions \(n=2t+1\), the analogous formula is
\[
 (A_{2t+1},A_{2t+2},A_{2t+3},A_{2t+4})\equiv O(t\bmod2,r(t),r(t+1),r(t+2))\pmod{16}.\tag{7}
\]
The eight \(E\)-words are distinct. For odd positions the four-bit parameter ranges over all 16 possibilities, since if \(t=2h\), then
\[
 (t\bmod2,r(t),r(t+1),r(t+2))=(0,r(h)\oplus p,r(h),r(h+1)\oplus(1-p)),
\]
and if \(t=2h+1\), this parameter equals
\[
 (1,r(h),r(h+1)\oplus(1-p),r(h+1)),
\]
where \(p=h\bmod2\). For each parity this is a bijective mapping from the eight \(s(h)\)-states to its eight four-bit parameters. All 16 \(O\)-words are distinct, and their first residues lie in \(\{5,13\}\), whereas all \(E\)-words start in \(\{1,9\}\). Formula (5) now gives density \(\frac12\cdot\frac18=\frac1{16}\) for each \(E\)-word and \(\frac12\cdot\frac1{16}=\frac1{32}\) for each \(O\)-word, with the inherited \(O(\sqrt N)\) counting error. As (6)–(7) are exhaustive, no other four-term residue word occurs.

**4. Exact sharpness.** Let \(c_L=(M^Le_{(0,0,0)})_{(0,0,0)}\). Direct multiplication gives \(c_4=1\), \(c_8=36\), \(c_{12}=496\). From (3), the matrix \(M^4\) is annihilated by \(x(x-16)(x-1)(x+4)\). Thus for \(m\ge1\), \(c_{4m}\) satisfies the cubic scalar recurrence with characteristic roots \(16,1,-4\). The three displayed initial values therefore prove
\[
 c_{4m}=2^{4m-3}-(-4)^{m-1}\qquad(m\ge1).\tag{8}
\]
The word \(E(0,0,0)=(1,5,9,5)\) occurs at even positions \(n=2t\) precisely when \(s(t)=(0,0,0)\). Up to \(n<2^{4m+1}\), its count is \(c_{4m}\). Its limiting-density prediction is \(2^{4m+1}/16=2^{4m-3}\), leaving signed discrepancy \(-(-4)^{m-1}\), whose size grows as a constant multiple of the square root of the cutoff. This proves sharpness.

## Verification
The standalone script `verify.py` checks (1) against exact Apéry sums, (2) and the transfer matrix, (3) by exact integer arithmetic, the complete 24-word classification and density-compatible finite counts, and (8) at multiple exponents. Run `python3 verify.py`; success prints `VERIFY_OK`. These finite checks support reproducibility; the infinite claim follows from the algebraic proof above.

## Relationship to prior work
Rowland and Yassawi, *Automatic congruences for diagonals of rational functions* (arXiv:1310.8635, Section 3.6, Theorem 3.28), prove the pointwise formula \(A_n\equiv4\beta(n)+1\pmod{16}\) with \(\beta\) the number of binary runs and prove nonperiodicity. Their theorem implies the digit identities used here, but does not state the evaluated joint four-term densities, the 24-word transition classification, or the sharp discrepancy formula. These are the asserted new outcomes. Their earlier Section 3.3 discusses **single-residue** densities for other sequences, not the four-term Apéry statistic. Rampersad and Shallit, *Congruence properties of combinatorial sequences via Walnut and the Rowland–Yassawi–Zeilberger automaton* (arXiv:2110.06244, inspected Introduction and Motzkin/Catalan sections), analyze automatic congruences for Catalan/Motzkin sequences rather than the stated Apéry four-block invariant. Malik and Straub, *Divisibility properties of sporadic Apéry-like numbers* (2016), treat Lucas congruences and periodicity, not a published four-term Apéry density matrix. General finite-state machinery supplies a route to such calculations but does not itself give the explicit 24-word classification and its sharp error.

## Limitations
The pointwise congruence modulo 16 is previously known and **not** claimed as a new theorem. The finding concerns only consecutive blocks of length four modulo 16; it does not describe blocks of other lengths, modulo higher powers of two, or limiting joint distributions beyond this fixed word length. The exact scalar discrepancy formula is established only along specified power-of-two cutoffs. Earlier unindexed evaluations of automatic-sequence four-block frequencies could still overlap the present result.

## References
1. E. Rowland and R. Yassawi, *Automatic congruences for diagonals of rational functions*, arXiv:1310.8635, Section 3.6, Theorem 3.28. https://arxiv.org/pdf/1310.8635 (first posted 2013-10-31).
2. N. Rampersad and J. Shallit, *Congruence properties of combinatorial sequences via Walnut and the Rowland–Yassawi–Zeilberger automaton*, arXiv:2110.06244. https://arxiv.org/pdf/2110.06244.
3. A. Malik and A. Straub, *Divisibility properties of sporadic Apéry-like numbers*, Research in Number Theory 2 (2016), article 5, https://doi.org/10.1007/s40993-016-0036-8.
