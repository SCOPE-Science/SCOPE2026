# Exact small-field insertion–deletion spectra of full-length dimension-two Reed–Solomon codes

## Finding

For each prime power \(q\in\{2,3,4,5,7,8,9,11\}\), let \(\mathbb F_q\) be the field of order \(q\), and let \(\alpha=(\alpha_0,\ldots,\alpha_{q-1})\) be an ordering of all field elements. Define the full-length, dimension-two Reed–Solomon code
\[
C_\alpha=\{(a\alpha_i+b)_{i=0}^{q-1}:a,b\in\mathbb F_q\}.
\]
Let \(\tau(\alpha)\) be the largest number of adversarial insertion and deletion operations that this code can uniquely correct. Each code has precisely one representative satisfying \(\alpha_0=0\) and \(\alpha_1=1\). The following table gives the **exact number of distinct codes** with each value of \(\tau\), among the \((q-2)!\) normalized orderings:

| Field size \(q\) | \(\tau=0\) | \(\tau=1\) | \(\tau=2\) | \(\tau=3\) | \(\tau=4\) | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 1 | 0 | 0 | 0 | 0 | 1 |
| 3 | 1 | 0 | 0 | 0 | 0 | 1 |
| 4 | 2 | 0 | 0 | 0 | 0 | 2 |
| 5 | 5 | 1 | 0 | 0 | 0 | 6 |
| 7 | 5 | 92 | 23 | 0 | 0 | 120 |
| 8 | 12 | 234 | 474 | 0 | 0 | 720 |
| 9 | 8 | 324 | 3566 | 1142 | 0 | 5040 |
| 11 | 9 | 714 | 20942 | 213170 | 128045 | 362880 |

The first finite-field size admitting strict improvement over the **classical Hamming substitution-error correction radius** in this full-length, dimension-two family is \(q=13\). Specifically, over \(\mathbb F_{13}\), the evaluation order
\[
\alpha=(0,1,5,6,12,7,11,9,8,3,4,10,2)
\]
has \(\tau(\alpha)=6\), while its Hamming error-correction radius is \(5\). For \(q\le11\), the table shows \(\tau\le\lfloor(q-2)/2\rfloor\), which is the Hamming correction radius of every \([q,2,q-1]_q\) Reed–Solomon code.

## Assumptions and scope

The alphabet is a finite field and the code is an ordinary (unweighted) full-length Reed–Solomon code with dimension exactly two, evaluated at every field element once in an arbitrary fixed coordinate order. Insertions and deletions count one operation each; the receiver must uniquely recover from any mixture of at most \(\tau\) operations. The distribution counts codes with fixed coordinate positions and fixed field, not equivalence classes under coordinate permutations or field automorphisms. The canonical affine normalization identifies precisely those evaluation orders defining the *same* dimension-two code. No claim concerns a full census at \(q=13\), higher dimensions, or larger fields.

For reproducibility, \(\mathbb F_4=\mathbb F_2[z]/(z^2+z+1)\), \(\mathbb F_8=\mathbb F_2[z]/(z^3+z+1)\), and \(\mathbb F_9=\mathbb F_3[z]/(z^2+1)\); elements are encoded by their polynomial coefficients in ascending degree. For prime \(q\), use integers modulo \(q\).

## Proof

**1. Codes and normalized evaluation orders.** Every nonconstant evaluation vector \(\alpha\) is affine-equivalent to the unique vector \(\beta\) given by
\[
\beta_i=(\alpha_i-\alpha_0)/(\alpha_1-\alpha_0).
\]
The generator rows \((1,\ldots,1)\) and \(\alpha\) span the same space as \((1,\ldots,1)\) and \(\beta\). Conversely, if two normalized orderings generate the same dimension-two code, one is an affine transform of the other; their first two entries force the transform to be the identity. Hence normalized representatives are in bijection with codes, and their number is \((q-2)!\).

**2. Exact error-radius reduction.** For equal-length strings of length \(q\), the insertion–deletion distance equals \(2(q-\operatorname{LCS}(x,y))\). Two codewords consisting of distinct constants have no common symbol; a constant and a nonconstant affine evaluation vector have longest common subsequence at most one. For two *distinct* nonconstant codewords, apply the same invertible affine relabeling of symbols to both. They become \(\alpha\) and \(u\alpha+v\) with \(u\ne0\) and \((u,v)\ne(1,0)\), and every such affine pair occurs. Consequently,
\[
L(\alpha)=\max_{u\in\mathbb F_q^*,\,v\in\mathbb F_q,\,(u,v)\ne(1,0)}
\operatorname{LCS}(\alpha,u\alpha+v),
\qquad \tau(\alpha)=q-1-L(\alpha).
\]
Here \(L(\alpha)\ge1\) for every field size considered; all codeword types are thus included in the maximum. The distance formula implies unique correction of \(t\) operations exactly when \(2t<2(q-L(\alpha))\).

**3. Finite exhaustive classification.** Fix the first two evaluation symbols to \((0,1)\) and iterate over every permutation of the remaining \(q-2\) distinct field elements. For each ordering, iterate over each of the \(q(q-1)-1\) nonidentity affine transformations. Every transformed word is a permutation of field elements. If \(\operatorname{pos}_\alpha(x)\) is the index at which \(x\) appears in \(\alpha\), the longest common subsequence is exactly the length of the strictly longest increasing subsequence of
\[
(\operatorname{pos}_\alpha(u\alpha_i+v))_{i=0}^{q-1}.
\]
This identity is immediate from the requirement that a common subsequence preserve both words' relative symbol order. The independent verifier `rs_independent.cpp` implements this transformation and strict longest-increasing-subsequence algorithm. The main verifier `rs_lcs_census.cpp` separately computes each longest common subsequence using a bit-parallel dynamic-programming recurrence, and for \(q\le7\) also compares with ordinary two-dimensional dynamic programming. Both return the exact table. At \(q=11\), the exhaustive classification tests exactly \(9!=362880\) normalized codes and \(109\) affine transformations per code, i.e., \(39,553,920\) transformation comparisons. The counts sum to \(362880\); each field row sums to \((q-2)!\). These loops are finite exhaustive proofs, not samples or extrapolations.

**4. Explicit first-field witness.** Apply the same finite reduction to the stated \(\mathbb F_{13}\) evaluation ordering. The 155 nonidentity affine transforms have longest-common-subsequence length histogram
\[
\#\{L=3\}=6,\quad \#\{L=4\}=37,\quad
\#\{L=5\}=73,\quad \#\{L=6\}=39.
\]
Thus \(L(\alpha)=6\), whence \(\tau(\alpha)=13-1-6=6\). Both a longest-increasing-subsequence implementation and a standard two-dimensional longest-common-subsequence algorithm agree on all 155 comparisons. The tabulation for all smaller prime-power field sizes proves minimality of the field size \(13\).

## Verification

Compile with a C++17 compiler, for example:

```sh
g++ -std=c++17 -O3 -Wall -Wextra rs_lcs_census.cpp -o rs_lcs_census
g++ -std=c++17 -O3 -Wall -Wextra rs_independent.cpp -o rs_independent
for q in 2 3 4 5 7 8 9 11; do ./rs_lcs_census "$q"; ./rs_independent "$q"; done
./rs_independent 13
```

Both programs must agree on the maximum-LCS histograms (convert via \(\tau=q-1-L\)); the independent program prints `VERIFY_OK`. The field multiplication is checked to permute the field under every nonzero multiplier. The ordinary dynamic-programming cross-check tests every transformation for \(q\le7\) in the main program and every transformation for the explicit \(q=13\) witness in the independent program. The machine-readable table `COUNTS.tsv` contains the expected exact output in error-radius order.

## Relationship to prior work

Beelen, Con, Gruica, Montanucci and Yaakobi [1] characterize full-length, dimension-two Reed–Solomon evaluation orders that **cannot correct even one** insertion/deletion; their Lemma 3 already implies the \(\tau=0\) strata, and these are not claimed as new. Their Proposition 1 and Table 1 address one-error existence and proportions, not the complete distribution across every larger correction radius. Their concluding discussion notes computational evidence that some orderings at field sizes starting with \(13\) can outperform Hamming correction, but does not specify the particular witness or establish the full smaller-field spectra. The 2026 journal abstract describes stronger asymptotic correction guarantees and still does not supply the exact finite table [2].

Con, Shpilka and Tamo [3] address the much stronger condition of correcting \(n-3\) insertions/deletions with field size asymptotically cubic in the code length; that does not give the enumerated full-length distributions. Zhang, Sun, Zhang and Ge [4] study randomized Reed–Solomon codes under synchronization and permutation errors, providing asymptotic results rather than this exact small-field classification. The finite table and explicit witness were also compared in meaning against publicly indexed coding and deletion-code records, including broad asymptotic deletion-code findings and full-field Galois-hull results, none of which determines them.

## Limitations

The proof uses an exhaustive finite computation for eight field sizes. It is not a closed-form family formula and makes no claim about other prime powers. The witness at \(q=13\) is a single explicitly checked ordering, not a distribution over that field. Source comparison does not exclude an unindexed earlier finite computation or a relevant table in the inaccessible full 2026 journal text; the 2025 preprint was inspected in full. No independent external scientific audit has been performed.

## References

1. P. Beelen, R. Con, A. Gruica, M. Montanucci and E. Yaakobi, *Reed–Solomon Codes Against Insertions and Deletions: Full-Length and Rate-1/2 Codes*, arXiv:2501.11371, first posted 2025-01-20. https://arxiv.org/abs/2501.11371
2. Same authors, journal version, *IEEE Transactions on Information Theory* 72(2) (2026), 1149–1160, DOI:10.1109/TIT.2025.3647216. https://doi.org/10.1109/TIT.2025.3647216
3. R. Con, A. Shpilka and I. Tamo, *Optimal Two-Dimensional Reed–Solomon Codes Correcting Insertions and Deletions*, arXiv:2311.02771 (2023), *IEEE Trans. Information Theory* 70(7) (2024), 5012–5016. https://arxiv.org/abs/2311.02771
4. Y. Zhang, Y. Sun, X. Zhang and G. Ge, *Random Reed–Solomon Codes Correcting Permutations, Insertions, and Deletions over Polynomial-Size Alphabets*, arXiv:2606.22344 (2026). https://arxiv.org/abs/2606.22344
