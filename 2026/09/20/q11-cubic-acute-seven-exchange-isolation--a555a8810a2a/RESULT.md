# Seven-exchange isolation of a 24-point cubic acute set in the 11-cube

## Statement

Write \(Q_{11}=\{0,1\}^{11}\), with graph distance equal to Hamming distance. A set \(S\subseteq Q_{11}\) is in **general position** if no three distinct vertices of \(S\) lie on a common shortest path. Equivalently, regarding the vertices as points in \(\mathbb R^{11}\), \(S\) is a **cubic acute set** if every angle determined by three of its points is acute.

Consider the following 24-point configuration \(B\), published by Dmitry Kamenetsky as the current lower-bound witness for \(a(11)\) in OEIS A089676:

```text
11000000000
00110100111
00001100000
01111100010
11010101010
10100001001
10011000111
11010110111
10001111111
11101011011
01111011101
01000101100
10101100101
10010010100
10100110110
10110001110
00001010110
00111011010
10011111000
00110010001
11111110001
00000101011
11101000110
01000010011
```

**Theorem.** If \(A\subseteq Q_{11}\) is a general-position set with \(|A|=25\), then
\[
|A\cap B|\le 16.
\]
Equivalently, every hypothetical 25-point cubic acute set differs from \(B\) in at least eight deletions and at least nine insertions, so
\[
|A\triangle B|\ge 17.
\]
In particular, \(B\) cannot be improved to 25 points by deleting at most seven of its vertices and adding one more vertex than was deleted.

The same statement holds for every image of \(B\) under an automorphism of the hypercube.

## Binary geometry behind the test

For \(x,y,z\in\{0,1\}^{11}\),
\[
(x-y)\cdot(z-y)
=\#\{i:x_i=z_i\ne y_i\}.
\]
Hence every angle spanned by cube vertices is acute or right, never obtuse. The angle at \(y\) is right exactly when there is no coordinate with \(x_i=z_i\ne y_i\), which is equivalent to
\[
y_i\in\{x_i,z_i\}\qquad\text{for every }i.
\]
That condition is exactly \(y\in I_{Q_{11}}(x,z)\), the Hamming-geodesic interval between \(x\) and \(z\). Thus cubic acute sets, general-position sets in \(Q_{11}\), and binary \((2,1)\)-separating systems are the same objects under the standard translations.

## Exhaustive verification

Fix \(r\in\{0,1,\ldots,7\}\) and a removed subset \(R\subseteq B\) with \(|R|=r\). Put \(T=B\setminus R\), so \(|T|=24-r\). If a 25-point general-position set contains \(T\), it must contain \(r+1\) further vertices.

The verifier in `artifacts/verify_exchange.cpp` performs the following exact finite search for every such \(R\):

1. It forms the complete candidate set \(C(T)\subseteq Q_{11}\setminus T\) of vertices \(v\) such that every triple \(\{v,t_1,t_2\}\), with \(t_1,t_2\in T\), is in general position.
2. For every pair of candidates it records whether adjoining that pair is compatible with every retained vertex of \(T\).
3. It uses exhaustive backtracking over \((r+1)\)-subsets of \(C(T)\), checking both the pair-with-\(T\) conditions and every triple consisting solely of newly chosen vertices.

These checks are jointly necessary and sufficient for \(T\) together with the chosen \(r+1\) vertices to be a general-position set. Removed vertices of \(B\) are allowed to reappear among the candidates, so the search does not assume that the final intersection with \(B\) is exactly \(T\).

The verified output is:

```text
base_valid 24
removed=0 add=1 improvement=NONE relevant_masks=0 max_candidates=0
removed=1 add=2 improvement=NONE relevant_masks=0 max_candidates=0
removed=2 add=3 improvement=NONE relevant_masks=4 max_candidates=6
removed=3 add=4 improvement=NONE relevant_masks=100 max_candidates=28
removed=4 add=5 improvement=NONE relevant_masks=1273 max_candidates=86
removed=5 add=6 improvement=NONE relevant_masks=11332 max_candidates=91
removed=6 add=7 improvement=NONE relevant_masks=70894 max_candidates=96
removed=7 add=8 improvement=NONE relevant_masks=280824 max_candidates=101
conclusion: no size-25 general-position set intersects the displayed size-24 set in 17 or more vertices
```

Here `relevant_masks` counts removal sets having at least \(r+1\) individually admissible candidates; masks with fewer candidates cannot possibly yield a 25-point extension. The output file is reproduced verbatim in `artifacts/verify_exchange.out`.

The program is standard C++17 and uses only the standard library. The displayed output was obtained with GCC 14.2.0. The search is exhaustive over all vertices of \(Q_{11}\), all removal subsets of \(B\) of size at most seven, and all candidate completions meeting the necessary pair and triple conditions.

## Context and originality boundary

OEIS A089676 currently records 24 as the best known lower bound for the 11-dimensional cubic acute problem and supplies the explicit configuration \(B\) above. The same problem is the hypercube general-position problem; Korže and Vesel (2023) give SAT-based partial results for hypercubes and report only lower bounds beyond the dimensions where exact values were certified. The coding-theoretic translation is the \((2,1)\)-separating-system problem studied, among others, by Randriambololona.

Searches were made under the equivalent vocabularies “cubic acute set”, “general position in the hypercube”, “(2,1)-separating system”, and “binary 2-frameproof code”, together with local/exchange/maximal/overlap terminology. No source located in those searches states the 17-point symmetric-difference obstruction, or an equivalent seven-exchange isolation result, for the explicit 24-point \(Q_{11}\) configuration. The originality claim is therefore only **to the best of our knowledge**.

## Scientific value

The theorem does not raise the lower bound \(gp(Q_{11})\ge24\), but it rules out a large and natural improvement neighborhood around the strongest currently recorded 24-point witness. Any 25-point improvement, if one exists, must abandon at least one third of the vertices of this configuration rather than arise from a small repair. This gives a concrete structural constraint for future exact or heuristic searches at the first unresolved dimension above the known exact range.

## Limitations

- This is a local isolation theorem for one explicit 24-point configuration and all of its hypercube-automorphic images; it is not a global upper bound on \(gp(Q_{11})\).
- It does **not** prove that 24 is optimal. A 25-point set with at most 16 vertices in common with \(B\) remains possible.
- The exhaustive certificate reaches deletion radius seven only. Nothing is asserted for exchanges deleting eight or more vertices.
- The result is computationally certified rather than formally verified in a proof assistant.
- No independent audit has yet been performed.

## References

1. OEIS Foundation, **A089676**, “maximal size of a cubic acute subset of \(\{0,1\}^n\)”: https://oeis.org/A089676
2. D. Kamenetsky, **Lower bounds and their solutions for a(11-15)** (2018), explicit 24-point witness for \(n=11\): https://oeis.org/A089676/a089676_1.txt
3. D. Korže and A. Vesel, **General Position Sets in Two Families of Cartesian Product Graphs**, *Mediterranean Journal of Mathematics* 20, 203 (2023): https://doi.org/10.1007/s00009-023-02416-z
4. H. Randriambololona, **(2,1)-Separating systems beyond the probabilistic bound**, *Israel Journal of Mathematics* 195 (2013), 171–186: https://doi.org/10.1007/s11856-012-0126-9
5. P. Erdős and Z. Füredi, **The greatest angle among n points in the d-dimensional Euclidean space**, *Annals of Discrete Mathematics* 17 (1983), 275–283: https://doi.org/10.1016/S0304-0208(08)73398-X
