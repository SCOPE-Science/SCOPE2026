# The shortest third-binomial collision in the period-doubling word

## Finding

Let \(p=\lim_{r\to\infty}\sigma^r(0)\), where \(\sigma(0)=01\) and \(\sigma(1)=00\). Two finite words are *third-binomially equivalent* if they have the same counts of every nonempty scattered binary subsequence of length at most three.

**Theorem.** The length of the shortest pair of distinct third-binomially equivalent factors of \(p\) is ten. At length ten, there are sixteen factors and fifteen equivalence classes. The sole nonsingleton class is
\[
\{0101010001,\ 1000101010\}.
\]

The occurrence and equivalence of this pair were already known. The assertion here is that no shorter pair exists and that no other length-ten pair collides.

## Assumptions and scope

A factor is a contiguous finite word occurring in the one-sided fixed point. A scattered occurrence of \(v=v_1\cdots v_j\) in \(w=w_1\cdots w_n\) is a strictly increasing tuple \((i_1,\ldots,i_j)\) such that \(w_{i_s}=v_s\) for every \(s\); its positions need not be consecutive. The theorem is an exhaustive statement for \(1\le n\le10\), not a formula for the complexity at longer lengths.

## Proof

**Complete factor sets.** The two-letter factors of \(p\) are exactly \(00,01,10\): every substitution block starts with zero, neither block contains \(11\), and \(\sigma^3(0)=01000101\) exhibits all three allowed pairs. In the decomposition \(p=\sigma^4(p)\), each aligned block has length sixteen. A window of length at most ten lies within two successive blocks, so the complete set of length-\(n\) factors is
\[
L_n=\{\sigma^4(ab)[i:i+n]:ab\in\{00,01,10\},\ 0\le i<16\}.
\]
Here the slice uses zero-based indices and excludes the right endpoint. Each such slice occurs because its underlying pair occurs. The braces remove duplicate slices before counting.

**Exact class counts.** For each \(w\in L_n\), count all increasing position tuples of sizes one, two and three by the sequence of letters they read. The signature is the list of these counts, including zeros, in order by pattern length and then lexicographically. The following pseudocode specifies the finite enumeration; no bound on the search prefix is assumed beyond the block argument above.

```text
for n = 1,...,10:
    L = set of the 48 slices specified above (duplicates removed)
    classes = empty map from signature to list of factors
    for w in L:
        counts = zero for each of the 14 patterns
        for j = 1,2,3:
            for each j-element subset of {0,...,n-1}:
                v = letters of w at the selected positions, in increasing order
                counts[v] += 1
        append w to classes[signature(counts)]
    record len(L), len(classes), and all lists of length > 1
```

| \(n\) | Factors | Classes |
|---:|---:|---:|
| 1 | 2 | 2 |
| 2 | 3 | 3 |
| 3 | 5 | 5 |
| 4 | 6 | 6 |
| 5 | 8 | 8 |
| 6 | 10 | 10 |
| 7 | 11 | 11 |
| 8 | 12 | 12 |
| 9 | 14 | 14 |
| 10 | 16 | 15 |

The two previously known factors occur in \(\sigma^4(0)=0100010101000100\) at respective offsets four and one. Both have signature \((6,4;15,12,12,6;20,19,22,10,19,16,10,4)\). The factor and class counts exclude every shorter collision and leave room for only this one class of size two at length ten.

## Verification

Run `python3 verify.py` alongside this report. The script implements the same exhaustive factor cover and computes signatures by updating a prefix count when one letter is appended. It groups the factors through length ten and checks the unique class. Its additional checks of order-four separation and the first four substitution iterates corroborate the previously known witness results, not the novelty of the finite census.

## Relationship to prior work

The earlier result *Explicit infinite third-order binomial collisions in the period-doubling word* [1] gives the identical pair, the same signature and its separation by the scattered pattern `0001` at order four. It also proves that the images under every \(\sigma^r\) remain equivalent and distinct, giving deficits at lengths \(10\cdot2^r\). Neither the witness itself nor its propagation is claimed here as new. The earlier record does not classify all third-binomial equivalence classes through length ten.

Lejeune [2, §4.5, pp. 115–117] reports computed order-three complexity values through length seventy, plotted in Figure 4.2, and gives conjectural higher-order behavior. Rigo, Stipulanti and Whiteland [3, §7.1] report experimental strictness of third-binomial complexity against factor complexity. The finite certificate here makes the precise first length and classification at that length explicit; it does not claim the first computation of the low-order complexity values or of the existence of a deficit.

## Limitations

The proof does not classify later collisions or decide fourth-binomial reconstruction. Earlier computational work may already reflect the deficit at ten in plotted or unpublished numerical data; the inspected material does not supply an exact discrete census of the first nonsingleton class. Historical priority beyond the compared sources is not established.

## References

1. *Explicit infinite third-order binomial collisions in the period-doubling word*, Resultary record `2026/10/13/SCOPE-explicit-infinite-third-order-binomial-collisions-in-the-period--4e783b08b718`.
2. M. Lejeune, *On the k-binomial equivalence of finite words and their applications*, doctoral thesis, Université de Liège (2021), https://hdl.handle.net/2268/259266.
3. M. Rigo, M. Stipulanti and M. A. Whiteland, *Characterizations of families of morphisms and words via binomial complexities*, arXiv:2201.04603, §7.1, https://arxiv.org/abs/2201.04603.
