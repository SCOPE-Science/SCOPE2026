# Exact dimensions and census of binary linear two-list single-insertion codes through length nine

## Finding

For each integer \(1\le n\le9\), define \(K(n)\) to be the maximum dimension of a binary linear code \(C\subseteq\mathbb F_2^n\) for which every binary received word \(y\) of length \(n+1\) has at most two **distinct** parents in \(C\) under exactly one insertion. The exact dimension profile is
\[
(K(1),K(2),\ldots,K(9))=(1,1,2,2,3,4,4,5,6).
\]
The respective numbers of *distinct linear subspaces* attaining these dimensions, with coordinate positions labeled and no quotient by coordinate permutations, are
\[
(1,3,4,29,49,17,3238,5534,1786).
\]
In particular, among the \(788035\) six-dimensional binary subspaces of length nine, exactly \(1786\) satisfy the two-list insertion criterion. No seven-dimensional subspace of length nine does. Thus length nine is the first blocklength at which six information bits can be carried in a binary linear code with this insertion-list guarantee.

## Assumptions and scope

An insertion adds exactly one bit (either zero or one) at any one of the \(n+1\) positions. A codeword \(c\in\mathbb F_2^n\) is a parent of \(y\in\mathbb F_2^{n+1}\) if deleting *some* coordinate of \(y\) gives \(c\). Repeated deletion positions producing the same parent are counted once. No substitutions or deletions are allowed by the channel. Codes are linear over \(\mathbb F_2\), not necessarily systematic, with fixed coordinate order; both the empty and all-zero words are treated according to these definitions. The theorem concerns only \(1\le n\le9\) and list size at most two.

For reproducibility, the integer mask \(u\) denotes the vector \((u_0,\ldots,u_{n-1})\) with \(u_i\) its bit at \(2^i\). An explicit optimal \([9,6]_2\) generator, in row order, is
\[
G=\begin{pmatrix}
1&0&0&0&0&0&1&0&0\\
0&1&0&0&0&0&0&1&0\\
0&0&1&0&0&0&1&1&0\\
0&0&0&1&0&0&0&0&1\\
0&0&0&0&1&0&1&0&1\\
0&0&0&0&0&1&0&1&1
\end{pmatrix},
\]
corresponding to row masks \((65,130,196,264,336,416)\). For this witness the \(1024\) length-ten received words have parent multiplicities \((N_0,N_1,N_2)=(432,480,112)\).

## Proof

**Canonical representation.** Each \(k\)-dimensional subspace of \(\mathbb F_2^n\) has a unique reduced-row-echelon \(k\times n\) generator matrix. Choose pivots \(0\le p_1<\cdots<p_k<n\). In row \(i\), the pivot entry at \(p_i\) is one, all other pivot columns are zero, all entries left of \(p_i\) are zero, and each nonpivot column to its right is a freely chosen bit. Taking the Cartesian product of these free choices over all pivot selections enumerates each \(k\)-subspace **exactly once**. The number enumerated is independently checked against the Gaussian binomial coefficient
\[
{n\brack k}_2=\prod_{j=0}^{k-1}\frac{2^{n-j}-1}{2^{k-j}-1}.
\]

**Complete membership test.** For each received \(y\) there are \(n+1\) ways to delete a position. The resulting **set** \(D(y)\) contains the distinct length-\(n\) parents. A candidate code \(C\) is valid precisely if \(\lvert C\cap D(y)\rvert\le2\) for every \(y\in\{0,1\}^{n+1}\). Every parent set is constructed exactly by deleting each coordinate, and every candidate subspace is constructed as all XOR sums of the generator rows. Thus this finite Boolean test is both necessary and sufficient; no probabilistic or heuristic inference is used.

**Exhaustion.** The accompanying `verify_insertion_linear.py` performs that Boolean test for all \({n\brack K(n)}_2\) optimal-dimensional subspaces and verifies the counts above. It also exhausts all \({n\brack K(n)+1}_2\) subspaces in the next dimension (when this dimension exists), accepting none. The excluded counts for \(n=2,\ldots,9\) are, respectively,
\[
1,1,15,31,63,2667,10795,43435.
\]
A valid subspace of dimension strictly larger than \(K(n)+1\) would contain a valid subspace of dimension \(K(n)+1\), because discarding codewords cannot increase any received-word parent count. Hence exclusion in the next dimension also excludes all larger dimensions. Each claimed dimension is attained by an explicit valid generator found during the canonical scan; the checker prints every witness. This proves the full finite profile and the census.

**Independent forward-channel cross-check.** For each printed witness, a separate routine constructs every possible received word by inserting either bit at every position of every codeword, accumulates sets of *distinct* parents, and computes the multiplicity histogram. This routine does not use the inverse-deletion masks of the exhaustion test. The length-nine witness yields exactly \((432,480,112)\), proving the displayed construction satisfies the list bound.

## Verification

Run `python3 verify_insertion_linear.py` with Python 3.9 or newer. It requires only the Python standard library. A successful run ends with `VERIFY_OK`. The test checks every enumerated subspace count against \({n\brack k}_2\), every optimal census count against its stated integer, the nonexistence of admissible codes in the next dimension, and each witness by independent forward insertion. At the largest bound it exhausts \(43435\) seven-dimensional length-nine subspaces; at the largest census it exhausts \(788035\) six-dimensional length-nine subspaces. `verification_output.txt` contains the output of the included checker. Integer operations are exact.

## Relationship to prior work

Kiah, Wei, and Zeng, *Constant-List Insertion--Deletion Codes: New Bounds and an Improvement of Levenshtein's Lower Bound*, arXiv:2609.21395 (first posted September 18, 2026), study fixed-list coding tradeoffs and distinguish insertion from deletion behavior. Their principal results concern general alphabets and asymptotic rate bounds, not this finite-dimensional census for linear single-insertion codes. Con, Doron, and Ribeiro, arXiv:2607.03989, establish asymptotic insertion list-decoding capacity with polynomially bounded lists, also distinct from the finite numerical list bound and linearity here. Xie, Chen, Qu, and Liu, DOI 10.3934/amc.2023008, study insdel-distance upper bounds for linear codes, a pairwise/unique-decoding invariant rather than triple-parent list multiplicities. Neither its accessible abstract nor the accessible results provide this census; the full paper was not available for a decisive whole-document exclusion.

## Limitations

The theorem makes no assertion for \(n\ge10\), for larger lists, for nonlinear codes, or for channels permitting deletions. The exhaustive subspace enumeration is a finite proof only in the displayed range; it is not evidence of a general formula outside it. The accessible literature search and results comparisons did not identify the same finite-dimensional census, but the inaccessible 2024 full text and possible unindexed computations leave residual originality risk. No independent external audit is claimed.

## References

1. H. M. Kiah, H. Wei, and R. Zeng, *Constant-List Insertion--Deletion Codes: New Bounds and an Improvement of Levenshtein's Lower Bound*, arXiv:2609.21395v1 (September 18, 2026), https://arxiv.org/abs/2609.21395.
2. R. Con, D. Doron, and J. Ribeiro, *The Insertion List-Decoding Capacity and an Improved Bound on the Deletion List-Decoding Capacity*, arXiv:2607.03989v1 (July 4, 2026), https://arxiv.org/abs/2607.03989.
3. C. Xie, H. Chen, L. Qu, and L. Liu, *New dimension-independent upper bounds on linear insdel codes*, Advances in Mathematics of Communications 18 (2024), 1575--1589, https://doi.org/10.3934/amc.2023008.
