# Dyadic two-Abelian ambiguity spectra of Thue–Morse factors

## Finding

Let \(\tau\) be the one-sided Thue–Morse word fixed by \(\mu(0)=01\), \(\mu(1)=10\). For every integer \(k\ge2\), let \(N=2^k\) and let \(\mathcal F_N\) consist of the **distinct** contiguous factors of length \(N\) occurring anywhere in \(\tau\). Two factors are *two-Abelian equivalent* when their first and last symbols and the counts of all four adjacent binary pairs agree. For a factor \(w\), put

\[
\mathsf S(w)=\bigl(w_1,w_N,|w|_{00},|w|_{11}\bigr).
\]

This shorter signature determines its entire two-Abelian class, since the counts of \(01\) and \(10\) follow from the length and endpoints.

**Even levels.** If \(k\) is even, set \(H=(N+2)/6\) and \(J=(N-1)/3\). Exactly the following eight signatures occur, with the indicated **numbers of distinct factors**, not occurrence frequencies:

| Endpoints | \(|w|_{00}\) | \(|w|_{11}\) | Class size |
|:--:|--:|--:|--:|
| 00 | \(H-1\) | \(H\) | \(J\) |
| 00 | \(H\) | \(H-1\) | \(N/2\) |
| 01 | \(H-1\) | \(H-1\) | \(J\) |
| 01 | \(H\) | \(H\) | \(J\) |
| 10 | \(H-1\) | \(H-1\) | \(J\) |
| 10 | \(H\) | \(H\) | \(J\) |
| 11 | \(H-1\) | \(H\) | \(N/2\) |
| 11 | \(H\) | \(H-1\) | \(J\) |

**Odd levels.** If \(k\) is odd (so \(k\ge3\)), set \(H=(N-2)/6\). The exact eight classes are:

| Endpoints | \(|w|_{00}\) | \(|w|_{11}\) | Class size |
|:--:|--:|--:|--:|
| 00 | \(H-1\) | \(H\) | \(H\) |
| 00 | \(H\) | \(H+1\) | \(H\) |
| 00 | \(H+1\) | \(H\) | \(N/2\) |
| 01 | \(H\) | \(H\) | \(N/2+H\) |
| 10 | \(H\) | \(H\) | \(N/2+H\) |
| 11 | \(H\) | \(H-1\) | \(H\) |
| 11 | \(H\) | \(H+1\) | \(N/2\) |
| 11 | \(H+1\) | \(H\) | \(H\) |

Thus, although there are eight classes at every dyadic length \(N\ge4\), their size multiset oscillates with \(k\): at even levels it is \(\{J\text{ (six times)},N/2\text{ (twice)}\}\), while at odd levels it is \(\{H\text{ (four times)},N/2\text{ (twice)},N/2+H\text{ (twice)}\}\). Upon division by \(N\), these multisets converge along even and odd levels to different multisets, respectively \(\{1/3\text{ (six)},1/2\text{ (two)}\}\) and \(\{1/6\text{ (four)},1/2\text{ (two)},2/3\text{ (two)}\}\). This is an exact two-phase reconstruction-ambiguity phenomenon.

## Assumptions and scope

Positions in a finite word are zero-based in the proof, while \(w_1\) and \(w_N\) denote the usual first and last symbols of \(w\). Pair counts are **overlapping** counts of adjacent pairs, without wrapping the factor around a circle. The factors themselves are distinct strings: repeated occurrences of one factor are counted once. The alphabet is exactly \(\{0,1\}\); \(k\) is any integer at least two. Only the canonical fixed point and powers-of-two lengths are considered.

The proof uses the established Thue–Morse factor-complexity identity \(|\mathcal F_{2^k}|=3\cdot2^k-2\) for \(k\ge2\), recalled explicitly in Greinecker [1, Introduction, factor-complexity formula]. No unproved computational extrapolation is used.

## Proof

### 1. Exhaustive and nonredundant factor parameterization

Write \(P=\mu^k(0)=p_0\cdots p_{N-1}\) and \(\bar P=\mu^k(1)\), the bitwise complement. Since \(\tau\) decomposes into successive \(k\)-level blocks equal to \(P\) or \(\bar P\), every length-\(N\) factor is

\[
W_{ab,r}=P_a[r:N]P_b[0:r],\qquad a,b\in\{0,1\},\quad 0\le r<N,
\]

where \(P_0=P\) and \(P_1=\bar P\); both substrings use half-open indices. Every two-letter block type \(ab\) occurs in \(\tau\), so all these words are genuine factors. Since \(P=U\bar U\) for \(U=\mu^{k-1}(0)\), \(P\) and \(\bar P\) are conjugate. Consequently, \(W_{00,r}\) and \(W_{11,r}\) range over the same \(N\) rotations of \(P\). These \(N\) rotations are distinct: a nontrivial circular period of length dividing \(N\) would divide \(N/2\), contradicting the second half of \(P\) being the complement of its first half.

There are another \(2(N-1)\) mixed words \(W_{01,r}\), \(W_{10,r}\) with \(1\le r<N\). Their union with the same-block rotations covers \(\mathcal F_N\) and contains at most \(3N-2\) words. The established factor-complexity identity gives exactly \(3N-2\) distinct length-\(N\) factors [1]. Therefore **all** these representatives are distinct and exhaust \(\mathcal F_N\). This conclusion includes the disjointness of the mixed families and the rotation family.

### 2. Circular pair counts

Let \(H_k\) denote the circular number of \(00\) edges in \(P=\mu^k(0)\). Half-turn complementation gives the same circular number of \(11\) edges. Every binary circular word has equally many \(01\) and \(10\) edges. Since each \(\mu\)-block has one unequal edge internally and a boundary edge associated to the next input letter, direct inspection of the four possible input pairs gives, for \(k\ge4\),

\[
H_k=2^{k-3}+H_{k-2},\qquad H_2=1,\quad H_3=1.
\]

Indeed, circular \(00\) edges in \(\mu(P_{k-1})\) correspond to circular \(10\) edges of \(P_{k-1}\), the latter consisting of \(2^{k-3}\) internal edges of \(\mu(P_{k-2})\) and \(H_{k-2}\) boundary edges. Thus

\[
H_k=\frac{2^k+2(-1)^k}{6},\qquad
K_k=\frac N2-H_k,
\]

where \(K_k\) is each of the circular counts of \(01\) and \(10\). Let \(e\in\{0,1\}\) denote \(k\bmod2\). The first symbol of \(P\) is zero, its last symbol is \(e\), and its **linear** counts of \(00\) and \(11\) are respectively

\[
E_{00}=H_k-(1-e),\qquad E_{11}=H_k.
\]

Cutting the circle immediately before a symbol removes one circular edge. Hence the \(N\) distinct rotations of \(P\) contribute \(H_k\) factors of signature \((0,0,H_k-1,H_k)\), \(H_k\) of \((1,1,H_k,H_k-1)\), and \(K_k\) each of signatures \((0,1,H_k,H_k)\) and \((1,0,H_k,H_k)\).

### 3. The mixed-block signatures

Set \(Q=\mu^{k-1}(0)=q_0q_1\cdots q_{N/2-1}\), so \(P=\mu(Q)\) and \(q_0=0\). For \(1\le r<N\), let

\[
D_r=\#\{0\le i\le r-2:p_ip_{i+1}=00\}
-\#\{0\le i\le r-2:p_ip_{i+1}=11\}.
\]

Every internal \(\mu\)-block edge is unequal. The edge between consecutive blocks \(\mu(q_j)\) and \(\mu(q_{j+1})\) adds \(q_j-q_{j+1}\) to this difference. The sum telescopes, yielding

\[
D_r=-q_{\lfloor(r-1)/2\rfloor}.
\]

For \(W_{01,r}=P[r:N]\bar P[0:r]\), the first and last bits are \(p_r\) and \(1-p_{r-1}\). Removing the cut edge, complementing the old prefix edges, and inserting the seam edge \((p_{N-1},1)\) gives exactly

\[
\begin{split}
|W_{01,r}|_{00}&=E_{00}-D_r-\mathbf1_{p_{r-1}p_r=00},\\
|W_{01,r}|_{11}&=E_{11}+D_r-\mathbf1_{p_{r-1}p_r=11}+e.
\end{split}
\]

This is an algebraic identity of finite edge counts, including both boundaries. Write \(z_{ab}\) for the **linear** number of adjacent occurrences of \(ab\) in \(Q\). At odd offsets \(r=2j+1\), the cut pair is \((q_j,1-q_j)\), and exactly \(N/4\) choices of \(j\) have each value of \(q_j\), because \(Q\) is balanced. At even offsets \(r=2j\) with \(1\le j<N/2\), the cut pair is \((1-q_{j-1},q_j)\). Substitution yields this exhaustive six-row tally for \(W_{01,r}\):

| Offset / condition | Endpoints | \(|w|_{00}\) | \(|w|_{11}\) | Number |
|:--|:--:|--:|--:|--:|
| odd, \(q_j=0\) | 11 | \(E_{00}\) | \(E_{11}+e\) | \(N/4\) |
| odd, \(q_j=1\) | 00 | \(E_{00}+1\) | \(E_{11}-1+e\) | \(N/4\) |
| even, \(q_{j-1}q_j=00\) | 00 | \(E_{00}\) | \(E_{11}+e\) | \(z_{00}\) |
| even, \(q_{j-1}q_j=01\) | 10 | \(E_{00}\) | \(E_{11}-1+e\) | \(z_{01}\) |
| even, \(q_{j-1}q_j=10\) | 01 | \(E_{00}\) | \(E_{11}-1+e\) | \(z_{10}\) |
| even, \(q_{j-1}q_j=11\) | 11 | \(E_{00}+1\) | \(E_{11}-1+e\) | \(z_{11}\) |

The mixed words \(W_{10,r}\) are exactly the bitwise complements of \(W_{01,r}\). Hence their contributions are obtained by complementing the two endpoint bits and interchanging the two pair-count coordinates.

For the prefix \(Q\) of length \(L=N/2\), put \(G=(L+2(-1)^{k-1})/6\) and \(f=(k-1)\bmod2\). Applying the circular calculation already proved to \(Q\) gives

\[
(z_{00},z_{11},z_{01},z_{10})
=\left(G-1+f,\ G,\ L/2-G,\ L/2-G-f\right).
\]

Thus every number in the six-row tally is explicit.

### 4. Complete summation and parity split

Add the six contributions for \(W_{01,r}\), their complemented contributions for \(W_{10,r}\), and the four rotation contributions from step 2. If \(k\) is even, \(H_k=(N+2)/6\), \(e=0\), and the two relevant numerical identities are \(z_{00}=z_{11}=(N-4)/12\) and \(z_{01}=H_k\), \(z_{10}=H_k-1\). The resulting eight signatures are precisely the even-level table above; six have size \((N-1)/3\) and two have size \(N/2\).

If \(k\) is odd, \(H_k=(N-2)/6\), \(e=1\), and \(z_{00}=(N-8)/12\), \(z_{11}=(N+4)/12\), \(z_{01}=z_{10}=H_k\). The eight entries become the odd-level table, with four sizes \(H_k\), two sizes \(N/2\), and two sizes \(N/2+H_k\). In either case the sizes sum to \(3N-2\), consistent with the exhaustive parameterization. Dividing these exact expressions by \(N\) gives the two stated limiting size multisets. \(\square\)

## Verification

The companion `checker.py` uses the standard library only. Run `python checker.py 10` after extracting both files into one directory. It constructs \(\mu^{k+3}(0)\), whose first eight \(k\)-level blocks contain each adjacent block type, so its distinct length-\(N\) windows exhaust the infinite-word factor set. It independently computes the full 2-Abelian signatures from **literal strings**, compares every class size with the tables, and separately checks the disjointness and coverage of the rotation/mixed representation. It passed for every \(2\le k\le10\), reaching \(N=1024\). The general proof is not conditional on these computations.

## Relationship to prior work

Greinecker [1] introduced a representation of 2-Abelian Thue–Morse classes and proved that their **number** is a 2-regular sequence; his introduction also recalls the exact ordinary factor-complexity formula used in step 1. Parreau, Rigo, Rowland and Vandomme [2] studied the number of 2-Abelian signatures via two-block coding and 2-regularity. Dekking [3] classified certain Thue–Morse factor sets via substitution descendants. None of the relevant examined primary-text results states the eight **individual class cardinalities** at all dyadic lengths or the alternating normalized class-size spectra. An equality of class counts does not imply equality of class sizes; these are distinct invariants.

The all-binary adjacent-pair multispectrum census is broader in input population, but supplies no count of which distinct Thue–Morse factors inhabit each signature. Likewise, the related period-doubling substitution has different factors and its two-Abelian multiplicity law does not imply the present Thue–Morse multiplicities by renaming letters. Historical priority beyond the materials inspected remains subject to independent literature review.

## Limitations

The theorem counts **distinct strings**, not their frequencies of occurrence along the infinite word. It applies only at lengths \(2^k\), \(k\ge2\), and only to two-Abelian equivalence; arbitrary lengths, longer-gram statistics and other fixed points are not classified. The use of a published ordinary factor-complexity theorem is explicit. Finite checker output supports but does not establish the infinite quantifier. The identified novelty is based on the inspected research record, not a proof that an equivalent result cannot appear in unsearched literature. Independent auditing has not been performed.

## References

[1] Florian Greinecker, *On the 2-Abelian Complexity of the Thue–Morse Word*, arXiv:1404.3906 (first public version 2014-04-15), especially Definitions 1.2–1.4, factor-complexity formula in the introduction, and Lemma 5.4. https://arxiv.org/abs/1404.3906

[2] Aline Parreau, Michel Rigo, Eric Rowland, Élise Vandomme, *A new approach to the 2-regularity of the \(\ell\)-abelian complexity of 2-automatic sequences*, arXiv:1405.3532 (first public version 2014-05-14), especially Sections 3, 6 and 7. https://arxiv.org/abs/1405.3532

[3] F. Michel Dekking, *On the structure of Thue–Morse subwords, with an application to dynamical systems*, arXiv:1405.2235 (first public version 2014-05-09), especially Section 2. https://arxiv.org/abs/1405.2235
