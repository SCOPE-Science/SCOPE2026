# The first binary nonlinear advantage in second-order radius-one covering

## Finding

Let \(K_2(n,1)\) denote the smallest cardinality of a binary code \(C\subseteq\mathbb F_2^n\) for which every ordered pair of binary target words \((x,y)\) has codewords \(u,v\in C\) and a coordinate \(i\) such that \(u_j=x_j\) and \(v_j=y_j\) for every \(j\ne i\). Equivalently, the product set \(C^2\) has covering radius at most one for the Hamming metric on two-row columns. Then

\[
K_2(n,1)=2^{n-1}\quad(1\le n\le5),\qquad K_2(6,1)\le29<32.
\]

Moreover, for every integer \(n\ge1\), the smallest **affine-linear** binary code with the same covering property has cardinality exactly \(2^{n-1}\). Consequently, length six is the first blocklength at which nonlinear codes strictly outperform every affine-linear code for this product-form covering problem. The exact unrestricted optimum at length six is not determined here.

## Assumptions and scope

The alphabet is exactly \(\mathbb F_2\). The covering order is exactly two: different codewords \(u,v\) can serve the two target rows, but the exceptional coordinate must be the **same** in both rows. The radius is one whole column, not one erroneous bit per row at independent coordinates. All codes are sets without multiplicity. Coordinates are indexed from zero in verification programs; integer \(z\) encodes a binary word by bit \(i\) at coordinate \(i\).

## Proof

**All affine-linear codes.** Let \(C=w+L\) be an affine subspace of codimension \(r\) in \(\mathbb F_2^n\), with parity-check map \(H:\mathbb F_2^n\to\mathbb F_2^r\) of rank \(r\). If two arbitrary targets \(x,y\) can be matched outside a single coordinate \(i\), then the two syndromes \(H(x-w)\) and \(H(y-w)\) are both multiples of column \(H_i\) and therefore span a space of dimension at most one. If \(r\ge2\), choose targets with linearly independent syndromes, a contradiction. Thus \(r\le1\), giving \(|C|\ge2^{n-1}\). The coordinate hyperplane \(\{z:z_0=0\}\), of size \(2^{n-1}\), meets every two-row target outside coordinate zero, proving equality for every \(n\ge1\).

**Finite unrestricted lower bounds.** The preceding coordinate hyperplane also gives \(K_2(n,1)\le2^{n-1}\). A complete elementary subset enumeration in `verify.py` proves that no smaller binary code works for each \(1\le n\le4\). The finite check enumerates every subset of the \(2^n\) words having cardinality below \(2^{n-1}\), and evaluates all \(2^{2n}\) ordered target pairs by the exact two-row projection criterion.

For length five an independently implemented exhaustive, symmetry-reduced search proves the lower bound. Write \(S=\mathbb F_2^5\setminus C\) for the forbidden words, and for \(x\in S\) define \(B_S(x)=\{i\in\{0,1,2,3,4\}:x+e_i\in S\}\). The covering property is equivalent to

\[
B_S(x)\cup B_S(y)\ne\{0,1,2,3,4\}\quad\text{for all }x,y\in S.
\]

Indeed, for any \(x\in S\) the only possible codeword matching it outside position \(i\) is \(x+e_i\), whereas if \(x\in C\), then \(x\) itself matches outside every position. Thus failures can occur only for pairs in \(S\). The property displayed above is hereditary under passage to smaller forbidden sets. If a code of size at most fifteen existed, its forbidden set would contain at least seventeen words. Translate every word by a fixed member of that forbidden set so the zero word belongs to it, and retain a seventeen-element forbidden subset containing zero. The precise exhaustive depth-first search in `finite_check.cpp` enumerates all potential such subsets: at each state it tries including and excluding the next word, rejecting an inclusion only if the displayed pair condition already fails, because subsequent inclusions can never repair a failure. It visits exactly 16,829,638 recursion nodes and finds no valid seventeen-element subset containing zero. Hence \(K_2(5,1)\ge16\), matching the coordinate hyperplane upper bound.

**The length-six witness.** Let \(C\subseteq\mathbb F_2^6\) consist of the 29 distinct binary words represented by the following integers:

```
0, 3, 4, 7, 9, 12, 14, 15, 17, 18, 20, 23, 25, 26, 29,
32, 33, 37, 38, 42, 43, 45, 50, 53, 55, 56, 59, 60, 62
```

For each of the \(2^{12}=4096\) ordered target matrices, `verify.py` checks the precise shared-coordinate matching condition. An independent literal center-and-exception enumeration in `direct_center.py` constructs the set of matrices covered by all \(29^2\) codeword pairs and confirms that this set has cardinality 4096. Therefore \(K_2(6,1)\le29\), strictly smaller than the optimal affine-linear size 32.

## Verification

From a directory containing the supplied standalone files, run `python3 verify.py`, `python3 direct_center.py`, `c++ -O3 -std=c++17 finite_check.cpp -o finite_check`, and `./finite_check`. All four commands were executed successfully. The outputs include `VERIFY_OK`, the full number 4096 of length-six target matrices, and 16,829,638 recursion nodes in the length-five finite enumeration. `finite_check.cpp` is an exhaustive finite proof only for length five. The affine-linear comparison is a general mathematical proof independent of the computation.

## Relationship to prior work

The second-order football-pool formulation and generalized covering radius of codes were studied by Elimelech and Schwartz (arXiv:2210.00531, initially public 2022-10-02); their accessible description concerns an asymptotic rate. Li, Shangguan, and Wei (arXiv:2608.24856, initially public 2026-08-25) establish that product restrictions and linearity do not change the **asymptotic** optimal covering rate. The present claim concerns instead the smallest **finite blocklength** at which a strict nonlinear-versus-affine separation occurs at fixed two-row radius one; the asymptotic statements do not logically imply this finite threshold. Neither manuscript was available in complete readable form for a line-by-line earlier-results comparison; possible unpublished or unindexed finite-length data remain a risk.

## Limitations

No claim is made that 29 is the exact length-six minimum, that this separation persists at a specified rate for growing length, or that there is a corresponding theorem for more than two rows or nonbinary alphabets. The short-length unrestricted lower bounds rely on exhaustive code enumeration, whose search program and pruning logic are supplied. The prior-literature comparison is limited by incomplete access to the full originating and antecedent manuscripts. Independent mathematical audit has not occurred.

## References

1. D. Elimelech and M. Schwartz, *The Second-Order Football-Pool Problem and the Optimal Rate of Generalized-Covering Codes*, arXiv:2210.00531 (first public 2022-10-02); Journal of Combinatorial Theory, Series A **203** (2024), 105834.
2. H. Li, C. Shangguan, and H. Wei, *The Optimal Asymptotic Rate of Generalized Covering Codes*, arXiv:2608.24856 (first public 2026-08-25).
