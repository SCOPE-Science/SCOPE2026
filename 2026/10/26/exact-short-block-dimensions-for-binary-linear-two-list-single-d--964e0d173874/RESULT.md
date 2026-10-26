# Exact short-block dimensions for binary linear two-list single-deletion codes

## Finding

For an integer \(n\ge 1\), let \(K_2(n)\) be the largest dimension of a binary linear subspace \(C\subseteq\mathbb F_2^n\) such that **each** binary word \(y\) of length \(n-1\) occurs as a scattered subsequence of **at most two distinct codewords** of \(C\). Then

\[
\bigl(K_2(1),K_2(2),\ldots,K_2(10)\bigr)
=(1,1,2,2,3,3,4,5,5,6).
\]

In particular, **length ten is the shortest possible blocklength for a six-dimensional binary linear code with a one-deletion decoding list of size at most two**. At length nine, the seemingly plausible dimension six is impossible; at length ten, a six-dimensional example exists. The profile is for *exactly one deletion*, not insertion/deletion balls of mixed output lengths.

## Assumptions and scope

A binary linear code is an \(\mathbb F_2\)-subspace of \(\mathbb F_2^n\). Deleting coordinate \(j\in\{1,\ldots,n\}\) from a codeword produces a length-\(n-1\) binary received word; deletion positions giving identical outputs from the **same codeword** count only once. Define

\[
\lambda_C(y)=\bigl|\{c\in C:\text{some coordinate deletion of }c\text{ equals }y\}\bigr|.
\]

The two-list property is \(\max_{y\in\mathbb F_2^{n-1}}\lambda_C(y)\le2\). No assumption on minimum Hamming distance or the presence of the all-ones word is imposed. Linear subcodes inherit this property.

## Proof

**Exhaustive upper bounds.** Every \(k\)-dimensional subspace of \(\mathbb F_2^n\) has exactly one reduced-row-echelon \(k\)-by-\(n\) generator matrix. Choose increasing pivot columns \(p_1<\cdots<p_k\). In row \(i\), the pivot entry is one, all other pivot-column entries are zero, entries before \(p_i\) are zero, and every nonpivot entry strictly to the right of \(p_i\) is independently zero or one. Enumerating all pivot sets and these free entries visits **every** dimension-\(k\) subspace exactly once.

For each generated subspace, enumerate its \(2^k\) codewords by row subsets. Form the set of distinct one-deletion outputs of each codeword, increment one incidence counter for each received word, and reject the subspace as soon as a counter exceeds two. The complete exact-integer enumerations, reproduced by the accompanying `verify.cpp`, are:

| \(n\) | Tested dimension \(k=K_2(n)\) | Subspaces at \(k\) | Passing subspaces at \(k\) | Subspaces at \(k+1\) | Passing at \(k+1\) |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | — | — |
| 2 | 1 | 3 | 3 | 1 | 0 |
| 3 | 2 | 7 | 3 | 1 | 0 |
| 4 | 2 | 35 | 27 | 15 | 0 |
| 5 | 3 | 155 | 28 | 31 | 0 |
| 6 | 3 | 1,395 | 715 | 651 | 0 |
| 7 | 4 | 11,811 | 1,406 | 2,667 | 0 |
| 8 | 5 | 97,155 | 286 | 10,795 | 0 |
| 9 | 5 | 3,309,747 | 438,503 | 788,035 | 0 |
| 10 | 6 | not enumerated | explicit witness | 6,347,715 | 0 |

For \(1\le n\le9\), the nonzero passing counts establish the stated lower bounds; all next-dimension tests establish the upper bounds. In length ten, the exhaustive test rules out dimension seven. Because every higher-dimensional binary subspace contains a seven-dimensional subspace, dimensions greater than seven are also ruled out.

**Length-ten witness.** A generator matrix for dimension six is

\[
G=\begin{pmatrix}
1&0&0&0&0&0&0&0&0&1\\
0&1&0&0&0&0&0&0&1&1\\
0&0&1&0&0&0&1&1&1&0\\
0&0&0&1&0&0&1&0&1&0\\
0&0&0&0&1&0&1&1&1&0\\
0&0&0&0&0&1&0&1&1&1
\end{pmatrix}.
\]

Its first six columns form the identity, so its rank is six. For its \(64\) distinct codewords, exhaustive one-deletion counting over all \(512\) received words of length nine gives exactly \(220\) received words with zero parents, \(232\) with one parent, and \(60\) with two parents, and none with three or more. This proves \(K_2(10)\ge6\), completing the theorem.

## Verification

Compile and run the standalone verifier with a C++17 compiler:

```sh
c++ -O2 -std=c++17 verify.cpp -o verify
./verify
```

It generates every reduced-row-echelon generator at the enumerated boundary dimensions; recomputes each received-word parent count directly; checks exact subspace census totals; tests the explicit length-ten generator and its complete incidence histogram; and terminates with `VERIFY_OK` only if all comparisons hold. Every arithmetic operation is over integers or individual bits; no randomized tests, numerical optimization, or external libraries are required. The enumeration is finite and exhaustive only in the precisely stated dimensions and lengths; it is not claimed to prove an all-length formula.

## Relationship to prior work

Verma, Hollanti and Tajeddine's 2026 generalized half-Singleton paper supplies rate restrictions for linear list-decodable insertion/deletion codes over alphabets of size at least three and explicitly describes complications in the binary case (Remark 9). Its proof covers some binary cases with minimum Hamming distance greater than one, but it does not give this short-block binary exact dimension table or decide dimension six at length nine. The present theorem isolates a finite-length binary **deletion-only** subproblem and supplies exact thresholds. Liu, Tjuawinata and Xing study random and explicit list-decodable insertion/deletion codes, mainly through asymptotic rates and constructions; they do not state this binary finite-dimensional census. The distinction between the exact-deletion output length here and general insertion/deletion decoding must be preserved.

## Limitations

The conclusion is restricted to binary *linear* codes, lists of at most two codewords, and exactly one deletion, at lengths at most ten. It gives neither an all-length optimum nor an exhaustive count of the length-ten optimal codes. The proof of nonexistence for the listed boundary dimensions relies on reproducible complete finite enumeration, rather than on a closed-form obstruction valid for all lengths. No algorithmic efficiency claim is made for decoding the witness beyond its finite exhaustive decoder.

## References

1. N. Verma, C. Hollanti, R. Tajeddine, *A Generalized Half-Singleton Bound for List Decoding of Insertion/Deletion Errors*, arXiv:2610.23270v1, first submitted 16 October 2026, https://arxiv.org/html/2610.23270v1.
2. S. Liu, I. Tjuawinata, C. Xing, *On List Decoding of Insertion and Deletion Errors*, arXiv:1906.09705v6, https://arxiv.org/html/1906.09705v6.
3. R. Gabrys, V. Guruswami, J. Ribeiro, K. Wu, *Beyond Single-Deletion Correcting Codes: Substitutions and Transpositions*, arXiv:2112.09971, https://arxiv.org/abs/2112.09971.
