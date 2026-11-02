# Exact one-edit sum-channel capacity via binary distance-three codes

## Finding
Let \(A_2(\ell,3)\) be the maximum size of a length-\(\ell\) binary code of minimum Hamming distance at least three, where a one-word code is permitted. Let \(M_{\mathrm{SID}}(\ell,n)\) and \(M_{\mathrm S}(\ell,n)\) denote the largest code cardinalities correcting, respectively, at most one substitution/insertion/deletion or at most one substitution in the binary sum channel defined below. For all integers \(\ell\ge1\) and \(n\ge1\),

\[
M_{\mathrm{SID}}(\ell,n)=M_{\mathrm S}(\ell,n)=2^{\ell(n-1)}A_2(\ell,3).
\]

A maximum code is obtained by requiring that the vector of parities of the \(\ell\) data rows belong to any optimum binary distance-three code. Moreover, in **every** maximum sum-channel code, fixing all data columns but any chosen one leaves exactly \(A_2(\ell,3)\) possible values for the remaining column. Thus every coordinate section of every optimum is itself an optimum classical binary distance-three code.

As a concrete consequence of the classical optimum \(A_2(8,3)=20\), when \(\ell=8\), for every \(n\ge1\) the exact maximum size is \(20\cdot2^{8(n-1)}\), with optimal redundancy \(3\) bits under the conventional \(\ell n-\lceil\log_2 M\rceil\) definition. This exceeds the size \(16\cdot 2^{8(n-1)}\) supplied by the shortened-Hamming instance of the previously published construction by \(25\%\). The original channel paper considers the regime \(\ell<n\); the proof works also outside that regime under the same row-wise edit definition.

## Assumptions and scope
The alphabet is \(\mathbb F_2\). A channel input is \(X=(x_1,\ldots,x_\ell)\in\mathbb F_2^{\ell\times n}\). The noiseless output is the ordered tuple \(X^+=(x_1,\ldots,x_\ell,z)\), where \(z=x_1\oplus\cdots\oplus x_\ell\) is computed coordinatewise. One edit means at most one insertion, deletion, or substitution of a single bit in exactly one output row, with row identities preserved. The receiver observes the length of every output row. In particular, no row permutation and no deletion of an entire row are allowed. Two inputs are confusable if these error balls intersect.

Write \(A_2(\ell,3)=\max\{|B|:B\subseteq\mathbb F_2^\ell,\ d_H(u,v)\ge3\text{ for }u\ne v\}\). The natural optimal redundancy is \(\ell n-\lceil\log_2 M_{\mathrm{SID}}(\ell,n)\rceil=\ell-\lceil\log_2 A_2(\ell,3)\rceil\). The theorem is exact even where classical \(A_2(\ell,3)\) has no simple known closed formula.

## Proof
**1. Edits other than substitutions never produce a collision between distinct inputs.** An output with a deleted bit has a single row of length \(n-1\); an output with an inserted bit has a single row of length \(n+1\). These patterns do not coincide with the unedited or substituted lengths, or with an edit in a different row. If two inputs produced the same deletion output in the same row, their other \(\ell\) rows would be identical. Any \(\ell\) of the \(\ell+1\) rows of a sum matrix determine all rows via XOR, so the two original sum matrices would coincide. The same argument applies to an insertion output. Similarly, an unedited output cannot be a one-substitution output because every unedited column has even overall parity whereas one substitution makes exactly one column odd. Therefore all confusability between distinct inputs in the one-edit channel is substitution confusability.

**2. Exact substitution-conflict criterion.** For two inputs \(X,Y\), let \(u_j,v_j\in\mathbb F_2^\ell\) be their data columns. Their extended output columns differ in exactly

\[
d_H(u_j,v_j)+\bigl(d_H(u_j,v_j)\bmod2\bigr)\]

bits, an even number. The sum matrices have Hamming distance at most two if and only if exactly one data column differs and its two values have Hamming distance one or two. Since two radius-one Hamming balls intersect exactly when their centers have distance at most two, this is necessary and sufficient for two inputs to be substitution-confusable. This criterion is valid for all positive row and column counts.

**3. Matching upper bound.** Fix the first \(n-1\) data columns. Within the resulting section, distinct allowed final-column vectors must have mutual Hamming distance at least three by Step 2. Hence at most \(A_2(\ell,3)\) inputs may lie in each of the \(2^{\ell(n-1)}\) sections. This proves \(M_{\mathrm S}(\ell,n)\le 2^{\ell(n-1)}A_2(\ell,3)\), and hence the same upper bound for the one-edit capacity.

**4. Matching construction.** Choose a length-\(\ell\) code \(B\subseteq\mathbb F_2^\ell\) with \(|B|=A_2(\ell,3)\) and minimum distance at least three, and define

\[
\mathcal C_B=\{X\in\mathbb F_2^{\ell\times n}: (\bigoplus_{j=1}^n X_{1j},\ldots,\bigoplus_{j=1}^n X_{\ell j})\in B\}.
\]

Each member \(b\in B\) admits exactly \(2^{\ell(n-1)}\) matrices with that row-parity vector, so \(|\mathcal C_B|=2^{\ell(n-1)}A_2(\ell,3)\). If two such matrices could be confused by one substitution, Step 2 says they differ in a single column by a vector of weight one or two. Then their row-parity vectors, which lie in \(B\), also differ by weight one or two, a contradiction. Step 1 rules out all remaining one-edit collisions. This proves both equalities and the optimal construction. This lower construction is the tensor-product row-parity construction of Abboud and Yaakobi [1, Construction 4 and Theorem 4]; the contribution here is the matching all-parameter converse in Step 3 and the resulting equality.

**5. Rigidity of coordinate sections at equality.** Repeat Step 3 with any column \(j\) held free. Every section has size at most \(A_2(\ell,3)\). A maximum sum-channel code has exactly \(2^{\ell(n-1)}A_2(\ell,3)\) words, so all sections must meet this upper bound. Their free-column sets therefore are optimal binary codes. This is a necessary condition, not a classification of all maximum sum-channel codes.

**6. Eight-row example.** The exact classical identity \(A_2(8,3)=20\) is recorded both in the optimal binary-code tables [2,3] and the published classification's online list of five representatives [3]. The first 20-word representative is transcribed literally in the standalone checker; all its distinct codewords have Hamming distance at least three. Its optimality relies on the independent established classification/table, not on the finite minimum-distance check alone. Inserting this value into the theorem proves the quoted exact cardinality and redundancy.

## Verification
The accompanying standard-library-only program `verification/check.py` reconstructs one published 20-word length-eight classical code, checks all 190 pairwise Hamming distances and verifies that the minimum is exactly three. It independently computes \(A_2(\ell,3)\) for \(1\le\ell\le4\) via complete branch-and-bound, directly builds all sum-channel output spheres (no edit, all single substitutions, deletions, and insertions) for \(n\in\{1,2\}\), compares every input pair with the column-confusability criterion, and checks that every word in the row-parity construction has disjoint full error balls. The output is in `verification/check-output.txt` and ends with `VERIFY_OK`.

The finite tests illustrate Steps 1–4 but do not replace the all-parameter proof; the program does not independently certify the known optimality of \(A_2(8,3)=20\). No claim is made about the computational complexity of finding general optimal classical codes.

## Relationship to prior work
Abboud and Yaakobi [1], publicly posted January 15, 2026, introduced the binary sum channel. Their Section V-B, Construction 4 and Theorem 4 already establish the lower construction for **any** length-\(\ell\) one-substitution-correcting classical code. Their Theorem 5 bounds the capacity above by \(\lfloor2^{\ell n}/(\ell+1)\rfloor\), while Corollary 6 highlights a shortened-Hamming choice with redundancy at most \(\lceil\log_2(\ell+1)\rceil\). They give exact optimality for \(\ell=2\) separately. Their general statements do not give the exact maximum \(2^{\ell(n-1)}A_2(\ell,3)\) for arbitrary \(\ell\), nor do they characterize each coordinate section of a maximum code. The new converse partitions by all-but-one fixed columns and compares exact confusability, not just sphere volumes.

Standard finite-alphabet coding theory already defines and tabulates \(A_2(\ell,3)\). For \(\ell=8\), [2,3] establish the number 20, which is **not** claimed new. The connection to the sum-channel optimum and the per-section rigidity are the present claims. Neither the older classical packing tables alone nor the previously published tensor-product construction by itself implies a matching upper bound without the new section argument.

## Limitations
This is an exact capacity reduction, not a closed elementary formula for every classical \(A_2(\ell,3)\); some longer classical-code optima remain unknown. The model assumes an ordered row-wise one-edit channel with the appended XOR row and fully observable row lengths. No statement covers two edits, unlabeled rows, burst edits, or arbitrary noise processes. A necessary optimal-section condition does not classify all optimal sum-channel codes. The ell-eight numerical corollary uses a published classical optimality result as a lemma and is not independently re-proved by the supplied code. Literature priority beyond the cited works remains subject to the limits of searchable and accessible publications.

## References
[1] L. Abboud and E. Yaakobi, *Error-Correcting Codes for the Sum Channel*, arXiv:2601.10256, first submitted January 15, 2026, Section V, https://arxiv.org/abs/2601.10256 .

[2] A. E. Brouwer, *Table of general binary codes*, https://aeb.win.tue.nl/codes/binary-1.html . The table states \(A_2(n-1,2e-1)=A_2(n,2e)\), and its \((9,4)\) entry is \(20\).

[3] P. R. J. Östergård, T. Baicheva and E. Kolev, *Optimal binary one-error-correcting codes of length 10 have 72 codewords*, IEEE Transactions on Information Theory 45 (1999), 1229–1231; electronic optimal-code listing https://users.aalto.fi/~pat/72.html and explicit \((8,20,3)\) representatives https://users.aalto.fi/~pat/opt/20.txt .
