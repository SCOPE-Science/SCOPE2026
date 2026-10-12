# Exact one-edit capacity of the binary sum channel

## Finding

**Theorem.** Let \(n>\ell\ge2\) be integers. Let \(A_2(\ell,3)\) denote the largest size of a binary code of length \(\ell\) and minimum Hamming distance at least \(3\), without a linearity restriction. The largest binary sum-channel input code correcting **at most one total** substitution, insertion, or deletion, and the largest one correcting at most one substitution, have the same exact cardinality:

\[
A_n^{\mathrm{SID}}(\ell;1)=A_n^{\mathrm S}(\ell;1)=2^{\ell(n-1)} A_2(\ell,3).
\]

An optimal code is obtained by prescribing that its vector of input-row parities belongs to any maximum binary length-\(\ell\), distance-at-least-\(3\) seed code. The equality holds for nonlinear seeds and nonlinear sum-channel codes.

For \(\ell=8\), the established classical value \(A_2(8,3)=20\) yields the exact maximum \(20\cdot2^{8(n-1)}\) for every \(n>8\). Compared to the shortened-Hamming seed of size \(16\) used for the general construction in [1], this is a \(25\%\) gain in code cardinality. The twenty length-eight seed words are supplied as independently checked decimal bit patterns in the accompanying verifier; their existence and classical optimality are credited to [2,3].

## Assumptions and scope

Let \(X=(x_{ij})\in\mathbb F_2^{\ell\times n}\) be an input matrix. Define \(X^+\) to have the same first \(\ell\) rows and an additional row given in every column by their XOR. Exactly one edit, if any, acts on an entry of one of the \(\ell+1\) output rows. Insertion or deletion changes that row's length by one, whereas substitution changes one binary symbol in place. A code corrects an error class when the sets of outputs reachable by at most one allowed edit from distinct codewords are disjoint. The maxima \(A_n^{\mathrm{SID}}\) and \(A_n^{\mathrm S}\) refer to arbitrary subsets of the \(\ell n\)-bit input space. The restriction \(n>\ell\) matches the channel model in [1]; the combinatorial argument itself needs only positive \(n\).

## Proof

**Upper bound, including nonlinear codes.** Fix the first \(n-1\) complete input columns in any code \(\mathcal C\) correcting one substitution. For every codeword in this fiber, let \(a\in\mathbb F_2^\ell\) be its last input column. Distinct columns \(a,b\) differ in \(t=d_H(a,b)\) positions, and the corresponding last columns of the transmitted sum matrices differ in precisely \(t+(t\bmod2)\) positions. In particular, for \(t=1\) or \(t=2\) this distance is exactly \(2\). Two binary words at Hamming distance \(2\) have intersecting radius-one substitution balls: change one of the differing positions in one word and the other position in the second word. Here all other columns of the sum matrices agree, so the same conclusion holds for the full matrices. Therefore the final columns in any fiber form a length-\(\ell\) binary code of minimum distance at least \(3\). Its size is at most \(A_2(\ell,3)\). Summing over the \(2^{\ell(n-1)}\) choices of the fixed prefix gives

\[
|\mathcal C|\le 2^{\ell(n-1)}A_2(\ell,3).
\]

This bound applies to every one-substitution code, hence to every one-edit code.

**Attaining the bound.** Take any seed \(B\subseteq\mathbb F_2^\ell\) with \(|B|=A_2(\ell,3)\) and minimum distance at least \(3\). For a matrix \(X\), write \(b(X)\in\mathbb F_2^\ell\) for its vector of input-row XOR parities and set

\[
\mathcal C_B=\{X:b(X)\in B\}.
\]

For each of the \(|B|\) parity vectors there are exactly \(2^{\ell(n-1)}\) input matrices, giving the claimed size. We verify single-edit correction directly, following the decoder concept in [1]. An insertion or deletion produces one row of length \(n+1\) or \(n-1\), uniquely identifying the altered row. The other \(\ell\) rows of \(X^+\) remain intact. If the altered row was an input row, XOR the intact parity row with the other intact input rows to reconstruct it; if the altered row was the parity row, the original input rows are already intact. Thus either length-changing edit is corrected without even invoking \(B\).

For a single substitution, exactly one column of the received augmented matrix has odd column parity; call it \(j\). Let \(b'\) be the vector of the first \(\ell\) received row parities. Its distance from \(b(X)\in B\) is at most one. As \(B\) has minimum distance at least three, \(b(X)\) is uniquely recovered. If \(b'\ne b(X)\), their sole differing coordinate identifies the corrupted input row, and the entry at its intersection with column \(j\) is flipped. If \(b'=b(X)\), the substitution was in the appended parity row, so the first \(\ell\) received rows already equal \(X\). The no-edit case is immediate. Hence \(\mathcal C_B\) corrects every edit allowed by the statement, which proves equality.

## Verification

Run `python3 verify.py` using Python 3 and its standard library. The verifier independently (a) exhausts every pair of length-\(\ell\) columns for \(2\le\ell\le8\), checking the two-bit augmented-distance identity; (b) computes exactly \(A_2(\ell,3)\) for \(\ell=2,3,4\) by independent-set backtracking; (c) enumerates the complete edit balls, including insertions and deletions, and verifies pairwise disjointness for constructed instances \((\ell,n)=(2,3),(3,4),(4,2)\); and (d) checks all \(\binom{20}{2}\) distances for the established \((8,20,3)\) binary seed in [3]. Expected final output: `VERIFY_OK`. These finite tests support but do not replace the all-parameter proof.

## Relationship to prior work

Abboud and Yaakobi [1, Section V-B, Construction 4 and Theorem 4] supplied the universal row-parity-seed construction for any single-substitution-correcting classical seed, which is exactly the lower-bound construction above. Their subsequent Corollary 6 specifically selected a shortened Hamming seed and obtained a redundancy guarantee; Theorem 5 supplied the coarser sphere-packing upper bound \(A_n^{\mathrm S}(\ell;1)\le\lfloor2^{\ell n}/(\ell+1)\rfloor\). The **new assertion** is the matching fiberwise upper bound involving \(A_2(\ell,3)\), which establishes the exact maximum for every permitted \(n,\ell\), and proves that the preexisting construction is optimal when a maximum classical seed is used. The classical invariant and its numerical values, including \(A_2(8,3)=20\), are established mathematical coding-theory results [2,3], not new computations.

## Limitations

The theorem treats at most one edit **in total**, not arbitrary numbers of simultaneous edits or multiple corrupted rows. It reduces the exact sum-channel maximum to the classical function \(A_2(\ell,3)\); it does not give a new evaluation or efficient construction of that classical maximum at every length. The \(25\%\) improvement at \(\ell=8\) measures the number of admissible matrices, and should not be confused with a guaranteed improvement of one fixed-length binary message bit: a non-power-of-two code may waste messages under fixed-length indexing. The original paper's ceiling-based notion of redundancy differs from a floor-based fixed-message-capacity convention.

## References

[1] L. Abboud and E. Yaakobi, *Error-Correcting Codes for the Sum Channel*, arXiv:2601.10256 (first posted 2026-01-15), version 2, 2026. Full text: https://arxiv.org/html/2601.10256v2 .

[2] M. R. Best, A. E. Brouwer, F. J. MacWilliams, A. M. Odlyzko, and N. J. A. Sloane, *Bounds for binary codes of length less than 25*, IEEE Transactions on Information Theory 24 (1978), 81–93. Updated classical code table: https://aeb.win.tue.nl/codes/binary-1.html .

[3] P. R. J. Östergård, T. Baicheva, and E. Kolev, *Optimal binary one-error-correcting codes of length 10 have 72 codewords*, IEEE Transactions on Information Theory 45 (1999), 1229–1231. Electronic list of length-eight, twenty-word distance-three codes: https://users.aalto.fi/~pat/opt/20.txt .
