# Exact size of binary (2,1)-separating systems of length eight

## Result

Let \(m_2(8,2)\) denote the largest size of a binary 2-frameproof code of length 8. Equivalently, let \(S_{2,1}(8)\) denote the largest size of a binary \((2,1)\)-separating system of length 8. Then

\[
\boxed{m_2(8,2)=S_{2,1}(8)=10.}
\]

Under the standard identification of \(\{0,1\}^8\) with the vertices of the 8-dimensional hypercube \(Q_8\), this is equivalently

\[
\boxed{\operatorname{gp}(Q_8)=10.}
\]

Thus the first hypercube dimension beyond the previously known exact range \(Q_1,\ldots,Q_7\) has exact general-position number 10.

## Equivalent formulations

For three distinct binary words \(x,y,z\), the word \(z\) lies in the descendant of \(\{x,y\}\) exactly when, at every coordinate where \(x\) and \(y\) agree, \(z\) has that same value. Hence a binary code \(C\) is 2-frameproof exactly when, for every three distinct words \(x,y,z\in C\), there is a coordinate at which

\[
x_i=y_i\ne z_i,
\]

and likewise after permuting the roles of the three words. This is precisely the binary \((2,1)\)-separating condition.

In \(Q_8\), a vertex \(z\) is on a shortest \(x\)-\(y\) path exactly when it belongs to the coordinatewise subcube spanned by \(x\) and \(y\), which is the same condition as belonging to their binary descendant. Therefore a set of vertices is in graph general position exactly when the corresponding binary words form a 2-frameproof code.

## Lower bound

The following ten words form a binary 2-frameproof code of length 8:

```text
00000000
00000011
11101010
11100110
11010010
10100001
10011101
01110001
01001101
00111110
```

Direct verification checks the separating condition for every triple, so \(m_2(8,2)\ge 10\). A size-10 general-position set in \(Q_8\) was already reported as a lower bound by Korže and Vesel (2023); the contribution here is the matching upper bound.

## Upper bound

Assume for contradiction that a binary 2-frameproof code \(C\subseteq\{0,1\}^8\) has at least 11 words. The property is hereditary, so it suffices to exclude a code of exactly 11 words. Let \(d\) be its minimum Hamming distance.

### Distances 1 and at least 5 are impossible

If \(d=1\), normalize a closest pair to \(0^8\) and \(e_1\). For any third word \(z\), separating \(0^8\) from the pair \(\{e_1,z\}\) forces \(z_1=1\), while separating \(e_1\) from \(\{0^8,z\}\) forces \(z_1=0\), a contradiction. Thus a code with at least three words has \(d\ne1\).

If \(d\ge5\), sum the Hamming distances over all \(\binom{11}{2}=55\) pairs. The sum is at least \(275\). On the other hand, if a coordinate contains \(s\) ones, that coordinate contributes \(s(11-s)\le30\) to the pair-distance sum. Across eight coordinates the total is therefore at most \(8\cdot30=240\), a contradiction.

Consequently any hypothetical 11-word code has

\[
d\in\{2,3,4\}.
\]

### Symmetry reduction

Choose a closest pair. Translation by a binary word and coordinate permutations preserve all relevant properties, so normalize it to

\[
0^8,\qquad a_d=1^d0^{8-d}.
\]

For any third word \(w\), let \(\alpha\) be its number of ones in the first \(d\) coordinates and \(\beta\) its number of ones in the remaining \(8-d\) coordinates. The separating condition for the normalized pair gives

\[
1\le \alpha\le d-1,
\]

while the minimum-distance conditions give

\[
\alpha+\beta\ge d,
\qquad
(d-\alpha)+\beta\ge d,
\]

or equivalently \(\beta\ge\alpha\). The stabilizer \(S_d\times S_{8-d}\) is transitive on words with the same pair \((\alpha,\beta)\), so it is enough to examine one canonical third word for each feasible orbit.

The feasible orbit types are

- \(d=2\): \((1,1),(1,2),\ldots,(1,6)\);
- \(d=3\): \((1,2),(1,3),(1,4),(1,5),(2,2),(2,3),(2,4),(2,5)\);
- \(d=4\): \((1,3),(1,4),(2,2),(2,3),(2,4),(3,3),(3,4)\).

### Exact completion search

For each normalized distance and orbit representative, form the set of possible additional words that

1. have distance at least \(d\) from both words of the closest pair, and
2. form a valid separating triple with that pair.

Put an edge between two candidate words when they are mutually at distance at least \(d\) and, together with each member of the normalized pair, satisfy the separating condition. Any completion must be a clique in this compatibility graph. During an exact branch-and-bound search, every newly added candidate is additionally checked against every pair of already selected candidates, so the full three-word condition is enforced, not merely pairwise compatibility. Greedy graph coloring is used only as a valid upper bound for pruning.

The exact maximum total code sizes for the orbit representatives are:

| \(d\) | \((\alpha,\beta)\) | maximum total size |
|---:|:---:|---:|
| 2 | (1,1) | 10 |
| 2 | (1,2) | 10 |
| 2 | (1,3) | 10 |
| 2 | (1,4) | 10 |
| 2 | (1,5) | 10 |
| 2 | (1,6) | 10 |
| 3 | (1,2) | 10 |
| 3 | (1,3) | 10 |
| 3 | (1,4) | 10 |
| 3 | (1,5) | 10 |
| 3 | (2,2) | 10 |
| 3 | (2,3) | 10 |
| 3 | (2,4) | 10 |
| 3 | (2,5) | 10 |
| 4 | (1,3) | 10 |
| 4 | (1,4) | 9 |
| 4 | (2,2) | 10 |
| 4 | (2,3) | 9 |
| 4 | (2,4) | 10 |
| 4 | (3,3) | 10 |
| 4 | (3,4) | 9 |

Every possible closest-pair distance and every orbit of a third word is therefore bounded by 10. Hence an 11-word code cannot exist. Together with the explicit lower bound,

\[
m_2(8,2)=10.
\]

## Reproducibility

`artifacts/verify_q8.cpp` is a standalone C++17 verifier. It checks the explicit ten-word code, performs the symmetry-reduced exact searches described above, and prints the orbit-by-orbit maxima. `artifacts/verification_output.txt` contains the verified output.

The exhaustive part does not infer nonexistence from a heuristic search: all feasible orbit representatives are enumerated, and each branch is pruned only by cardinality or a proper-coloring upper bound on the compatibility graph.

## Literature context and originality

Körner (1995) connected the hypercube problem with \((2,1)\)-separating systems. Korže and Vesel (2023) gave exact values through dimension 7 and reported the lower bound \(\operatorname{gp}(Q_8)\ge10\), while larger dimensions were presented only with lower bounds. The August 2026 survey by Ullas Chandran, Klavžar, and Tuite states that the only exact hypercube values known are those through \(Q_7\), and again records the equivalence with \((2,1)\)-separating systems.

In fingerprinting-code terminology, Panoui (2012) established structural results and exact small-length cases through length 5, and subsequent work by Zhou and Zhou (2020), Zhao and Zhang (2024), and Sun and Wang (2025) developed general upper bounds for wide-sense frameproof codes. For binary alphabets, ordinary and wide-sense frameproof codes coincide.

To the best of our knowledge, the exact value at binary length 8 / \(Q_8\) has not previously been established. The strongest direct current-status evidence is the August 2026 general-position survey, which explicitly lists exact hypercube values only through dimension 7.

## Limitations

The upper bound uses an exact finite verification after a rigorous symmetry and distance reduction; it is not presently a closed-form argument that generalizes automatically to higher dimensions. The full theorem text of Sun and Wang (2025) was not accessible from the inspected publisher page, so there remains residual originality uncertainty about consequences not visible in its abstract; however, the later August 2026 survey still identifies \(Q_8\) as beyond the known exact range.

## References

1. J. Körner, “On the extremal combinatorics of the Hamming space,” *Journal of Combinatorial Theory, Series A* 71 (1995), 112–126. https://doi.org/10.1016/0097-3165(95)90019-5
2. D. Korže and A. Vesel, “General Position Sets in Two Families of Cartesian Product Graphs,” *Mediterranean Journal of Mathematics* 20, 203 (2023). https://doi.org/10.1007/s00009-023-02416-z
3. U. Chandran S. V., S. Klavžar, and J. Tuite, “The General Position Problem: A Survey,” arXiv:2501.19385v5 (2026). https://arxiv.org/abs/2501.19385
4. A. Panoui, *Wide-Sense Fingerprinting Codes and Honeycomb Arrays*, Ph.D. thesis, Royal Holloway, University of London (2012). https://pure.royalholloway.ac.uk/en/publications/wide-sense-fingerprinting-codes-and-honeycomb-arrays/
5. Y. Zhou and X. Zhou, “Wide-Sense 2-Frameproof Codes,” *Designs, Codes and Cryptography* 88 (2020), 2507–2519. https://doi.org/10.1007/s10623-020-00797-w
6. Y. Zhao and X. Zhang, “Improved Upper Bounds for Wide-Sense Frameproof Codes,” *IEEE Transactions on Information Theory* 70 (2024), 8636–8646. https://doi.org/10.1109/TIT.2024.3411150
7. C. Sun and X. Wang, “New upper bounds for wide-sense frameproof codes,” *Designs, Codes and Cryptography* 93 (2025), 3069–3082. https://doi.org/10.1007/s10623-025-01631-x
