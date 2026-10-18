# Exact ternary BWT run amplification for every length \(81\le n\le160\)

## Finding
For an ordered alphabet \(\Sigma_k=\{0,1,\ldots,k-1\}\) of size \(k\ge3\), let \(U_k(n)\) be the least *cyclic* number of constant-letter runs of a primitive necklace \([u]\) of length \(n\) whose ordinary, sentinel-free Burrows--Wheeler transform \(\operatorname{BWT}([u])\) has exactly \(n\) *linear* runs. The cyclic run number is the number of positions at which neighboring letters differ when the first and last positions are also neighbors.

**Theorem.** For every integer \(n\) with \(81\le n\le160\) and every \(k\ge3\),
\[
U_k(n)=\left\lceil\frac{n}{2}\right\rceil.
\]
The file `BWT_WITNESSES.tsv` supplies one explicit ternary last-column word for each of the 80 lengths. The result is an exact finite determination, not an asymptotic assertion or a proof for all lengths.

## Assumptions and scope
All strings are finite and indexed from zero. The alphabet is ordered \(0<1<2<\cdots<k-1\). A primitive necklace is the equivalence class under cyclic rotation of a word of least period equal to its full length. The BWT sorts all cyclic rotations lexicographically and takes their last column, with **no unique end marker**. Its run count is linear, whereas the input run count is cyclic. This distinction is essential.

Write \(L=L_0\cdots L_{n-1}\) for a last column and \(F=\operatorname{sort}(L)\). Set
\[
\pi_L(i)=\sum_{b<L_i}|L|_b+\#\{j<i:L_j=L_i\}.
\]
The sum uses only the ordered letters present in \(L\). The stable-rank permutation \(\pi_L\) is a permutation of \(\{0,\ldots,n-1\}\).

## Proof
The existing factor-two BWT run-amplification bound, in the cyclic-input form established by Kumallagov (2026, Proposition 3.2), gives \(U_k(n)\ge\lceil n/2\rceil\) for each \(k\ge3\).

For the reverse inequality, read the 80 rows of `BWT_WITNESSES.tsv`. Each row provides a word \(L\in\{0,1,2\}^n\) for one integer \(n\in[81,160]\). Check the following three finite predicates for every row:

1. \(L_i\ne L_{i+1}\) for each \(0\le i<n-1\).
2. The permutation \(\pi_L\) defined above consists of a single cycle of length \(n\).
3. \(\#\{i:L_i\ne F_i\}=\lceil n/2\rceil\).

Predicate 1 means the BWT last column has exactly \(n\) runs. By the standard one-cycle criterion for a last column (Fici, Gabory, Romana and Sciortino, 2025, Lemma 3), predicate 2 gives a *primitive* inverse necklace \([u]\) whose BWT is exactly \(L\). The number of cyclic run boundaries in \([u]\) equals the number of indices at which the character immediately preceding a sorted rotation, \(L_i\), differs from its first character, \(F_i\). Equivalently, as Kumallagov (2026, Proposition 4.3) shows,
\[
\rho_\circ([u])=d_H(L,F).
\]
Predicate 3 therefore says that this primitive necklace has exactly \(\lceil n/2\rceil\) cyclic runs. Because each witness uses only \(0,1,2\), it is also a witness over *every* ordered alphabet of size at least three. Hence \(U_k(n)\le\lceil n/2\rceil\), which matches the lower bound simultaneously for all 80 lengths and all \(k\ge3\).

All three predicates are checked directly in the provided standalone code. In addition, it reconstructs the inverse necklace, recomputes the entire BWT from sorted cyclic rotations, checks primitivity, and counts the necklace's cyclic runs independently of the Hamming formula. Thus the finite upper bound does not depend on an unverified search log or a claim of exhaustive enumeration.

## Verification
Place `check_bwt_witnesses.py` next to `BWT_WITNESSES.tsv` and execute `python3 check_bwt_witnesses.py` with Python 3. Only the standard library is used. The checker asserts a contiguous set of exactly 80 lengths, one verified BWT word per length, single-cycle stable LF permutations, exact run counts and direct BWT inversion. The complete witness table is human-readable; random-search procedures used to discover possible candidates are not needed to verify the theorem.

## Relationship to prior work
Fici, Gabory, Romana and Sciortino (2025) established the existence of completely unclustered BWT outputs over every alphabet of at least three symbols, but did not minimize input cyclic runs. Kumallagov (2026) introduced \(U_k(n)\), proved its general lower bound, presented small sharp examples through length 12 (with an exception at length 6), and conjectured sharpness for every length at least 7. The same paper also supplies prime/primitive-root constructions for certain special lengths. The present certificate gives *consecutive* exact sharpness for every length from 81 through 160, including lengths such as 128 and 160 not covered by the displayed prime constructions. It does not settle the unrestricted conjecture.

## Limitations
The claim is restricted to \(81\le n\le160\). It does not determine exact values at larger lengths, count all extremal necklaces, or provide a simple parametric construction. The proof is finite and computer-checkable, not an infinite-family induction. No independent external scientific audit is asserted. Publication-priority searches cannot rule out all unindexed work.

## References
1. David Kumallagov, *An extremal problem for completely unclustered Burrows--Wheeler images*, arXiv:2606.01267, first submitted 31 May 2026. In particular Proposition 3.2, Proposition 4.3, Section 6, Conjecture 7.1, and Section 10.
2. Gabriele Fici, Esteban Gabory, Giuseppe Romana and Marinella Sciortino, *Unclustered BWTs of any Length over Non-Binary Alphabets*, arXiv:2508.20879, first submitted 28 August 2025. In particular Lemma 3 and Theorem 15.
