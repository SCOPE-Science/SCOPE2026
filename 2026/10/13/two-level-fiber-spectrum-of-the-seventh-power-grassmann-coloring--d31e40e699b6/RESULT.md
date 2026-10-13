# Two-level fiber spectrum of the seventh-power Grassmann coloring

## Finding

Let \(K=\mathbb F_{64}\), regarded as a six-dimensional vector space over \(\mathbb F_2\), and let \(\mathcal G\) be its \(1395\) three-dimensional binary linear subspaces. For each \(U\in\mathcal G\), color \(U\) by the nonzero field element
\[
\omega(U)=\sum_{u\in U}u^7\in K^\times.
\]
Then the complete color-fiber spectrum is
\[
\bigl|\omega^{-1}(z)\bigr|=
\begin{cases}
29,&z^9=1,\\
21,&z^9\ne1,
\end{cases}
\qquad z\in K^\times.
\]
Consequently, exactly nine color classes contain \(29\) three-spaces and the other \(54\) contain \(21\), accounting for all \(9\cdot29+54\cdot21=1395\) vertices. The nine larger colors are precisely the norm-one elements for \(N_{K/\mathbb F_8}(z)=z^9\). Every color class is a binary constant-dimension code with minimum subspace distance at least \(4\).

## Assumptions and scope

This statement concerns this *specific* degree-three power-function coloring of the Grassmann graph \(J_2(6,3)\). Field multiplication and seventh powers are those of \(K\); addition is of characteristic two. The assertion concerns labeled binary subspaces and exact fiber cardinalities, not the optimal chromatic number or the maximum possible constant-dimension code size. A concrete realization used for the finite certificate is
\[
K=\mathbb F_2[t]/(t^6+t+1).
\]
The conclusion itself is independent of the choice of field isomorphism, since every such isomorphism preserves seventh powers, sums, and the relative norm.

## Proof

**1. The witness is a Moore determinant.** For any binary basis \(a,b,c\) of a three-space \(U\), polynomial polarization in characteristic two gives
\[
\omega(U)=\sum_{\sigma\in S_3}a_{\sigma(1)}a_{\sigma(2)}^2a_{\sigma(3)}^4
=\det\!\begin{pmatrix}a&b&c\\a^2&b^2&c^2\\a^4&b^4&c^4\end{pmatrix},
\]
where \((a_1,a_2,a_3)=(a,b,c)\). Indeed, writing \(7=1+2+4\), summation over the eight binary combinations kills all monomials omitting a basis variable; the only surviving terms assign the three distinct powers \(1,2,4\) to the three variables. The Moore determinant is nonzero on a binary independent triple. It is basis-independent because \(\det\operatorname{GL}_3(\mathbb F_2)=\{1\}\). Thus all \(1395\) color values lie in \(K^\times\).

**2. Scalar orbits constrain the fibers.** The multiplicative group \(K^\times\) has order \(63\). If \(\lambda\in K^\times\), then \(\omega(\lambda U)=\lambda^7\omega(U)\). The seventh-power subgroup
\[
H=(K^\times)^7=\{z\in K^\times:z^9=1\}
\]
has order \(9\), so all fiber sizes are constant on each of seven cosets of \(H\). There are exactly nine scalar multiples of the unique subfield \(\mathbb F_8\), each a binary three-space: this is one orbit of size \(9\), with stabilizer \(\mathbb F_8^\times\). For \(U=\lambda\mathbb F_8\),
\[
\omega(U)=\lambda^7\sum_{x\in\mathbb F_8}x^7=\lambda^7,
\]
so these nine exceptional three-spaces map bijectively onto \(H\). Every other three-space has trivial scalar stabilizer: any nontrivial stabilizer would make the binary three-space a vector space over a proper subfield of \(K\), forcing that subfield to have binary degree dividing both \(3\) and \(6\), hence degree \(3\), the case already accounted for. The remaining \(1386\) three-spaces therefore form exactly \(22\) free scalar orbits of size \(63\); each such orbit contributes exactly seven three-spaces to each color of a single coset of \(H\).

**3. Exact finite orbit classification.** The attached self-contained verifier exhausts the \(1395\) binary three-spaces in two independently generated ways (unique reduced-row-echelon bases and unordered independent triples), computes the Moore determinant and seventh-power sum independently for each, and classifies all \(23\) scalar orbits. The seven cosets, represented in the displayed polynomial basis by the field-element bit integers \(1,2,3,4,5,8,9\), have the following numbers of *free* scalar orbits:

| Coset representative | Free orbits | Exceptional orbit | Fibers per color |
| --- | ---: | ---: | ---: |
| `1` | 4 | 1 | 29 |
| `2` | 3 | 0 | 21 |
| `3` | 3 | 0 | 21 |
| `4` | 3 | 0 | 21 |
| `5` | 3 | 0 | 21 |
| `8` | 3 | 0 | 21 |
| `9` | 3 | 0 | 21 |

Every free orbit contributes seven elements to each fiber within its coset; the exceptional orbit contributes one to each fiber of \(H\). Thus the displayed count proves the asserted formula, with \(4\cdot7+1=29\) and \(3\cdot7=21\). The total of free orbits is \(4+6\cdot3=22\), in agreement with the scalar orbit argument. This is an exhaustive finite classification, not extrapolation from sampling.

**4. Code distance.** If distinct three-spaces shared a binary two-space, their witnesses would differ by the nonzero third-order sum over the complementary three-flat; equivalently, by the Moore determinant nonvanishing. Hence equal colors imply intersection dimension at most one, and their subspace distance is at least \(4\). The verifier also checks directly that each of the \(651\) binary two-spaces is contained in \(15\) three-spaces bearing \(15\) distinct colors.

## Verification

Run `python3 artifacts/verify.py` in the unpacked file set using Python's standard library. The program first verifies the chosen polynomial ring is a field by checking every product of two nonzero elements and the nonzero multiplicative exponents. It generates all \(1395\) spaces both from RREF bases and independently from three-element independent subsets of \(K\), computes both formulae for \(\omega\), and classifies all seven cosets, \(23\) scalar orbits, and \(651\) binary two-spaces. Each asserted count is an exact integer equality; successful execution prints `VERIFY_OK`.

## Relationship to prior work

Carlet established the power-function sum-freedom and the Moore-determinant identity; these are used here as background rather than claimed as new. D'haeseleer and Taranchuk construct a Moore-determinant coloring of Grassmann graphs and prove a general chromatic upper bound. Heering, Kaspers, and Taranchuk explicitly describe the sum-free witness coloring and its coding-theoretic interpretation. Their stronger \(31\)-color upper bound for \(J_2(6,3)\) comes from a different, five-dimensional function; the present \(63\)-color partition does **not** improve that bound. The specific two-level fiber counts \(29\) and \(21\), their norm-one characterization, and the free-orbit allocation are not given or implied by those chromatic-number statements. The separate MRD-coloring work of D'haeseleer and coauthors treats a different construction.

## Limitations

The result fixes \(K\), exponent \(7\), and three-dimensional binary subspaces. It does not determine optimal chromatic number, classify all colorings, or generalize the \(21/29\) spectrum to other extension degrees. The exact orbit allocation is certified by complete finite enumeration, with structural reduction to \(22\) free orbits; no closed uniform formula for general extension degrees is asserted. Literature coverage cannot rule out every unindexed prior computation.

## References

1. J. D'haeseleer and V. Taranchuk, *On the Chromatic Number of Grassmann Graphs*, arXiv:2505.22055v1, 28 May 2025, especially Proposition 2.1 and Theorem 1.2.
2. P. Heering, C. Kaspers, and V. Taranchuk, *On Reed-Muller subcodes, Grassmannian partitions and sum-free functions*, arXiv:2605.22958v1, 21 May 2026, especially Propositions 2.6 and 2.17 and Section 6.
3. C. Carlet, *Two Generalizations of Almost Perfect Nonlinearity*, Journal of Cryptology 38 (2025), article 20, DOI:10.1007/s00145-025-09538-5, especially the power-function/Moore-determinant identity.
4. J. D'haeseleer, F. Pavese, P. Santonastaso, and V. Taranchuk, *Chromatic Number of Grassmann Graphs and MRD Codes*, arXiv:2602.10777 (2026).
