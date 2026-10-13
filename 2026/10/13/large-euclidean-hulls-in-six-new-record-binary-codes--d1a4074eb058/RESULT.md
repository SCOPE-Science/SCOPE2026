# Large Euclidean hulls in six new record binary codes
## Finding

Seddas--Shashkov--Viazovska--Abbe give six record binary codes with complete quasi-cyclic descriptions:
\[
[172,21,66],\ [173,20,68],\ [176,21,68],\ [181,21,70],\ [184,21,72],\ [189,22,72].
\]
For these exact printed constructions, the Euclidean hull dimensions are
\[
17,\ 2,\ 20,\ 19,\ 21,\ 21,
\]
respectively.

More precisely, their hulls have parameters
\[
[172,17,68],
\]
\[
[173,2,104],
\]
\[
[176,20,68],
\]
\[
[181,19,72],
\]
\[
[184,21,72],
\]
and
\[
[189,21,72].
\]
The numbers of minimum-weight words in these hulls are, respectively,
\[
1360,\ 3,\ 2992,\ 6358,\ 9826,\ 2394.
\]

Thus the record \([184,21,72]\) code is self-orthogonal. The record \([176,21,68]\) and \([189,22,72]\) codes have hull codimension one, and \([181,21,70]\) has hull codimension two. The six codes therefore have a sharply non-LCD structural profile that is not visible from their minimum-distance records alone.

## Assumptions and scope

For a binary linear code \(C\), its Euclidean hull is
\[
\operatorname{Hull}(C)=C\cap C^\perp.
\]
If \(G\) is a full-rank binary generator matrix of dimension \(k\), then
\[
\dim\operatorname{Hull}(C)=k-\operatorname{rank}(GG^{\mathsf T}).
\]

Each of the six codes is reconstructed directly from the block length, divisor polynomial, multiplier polynomials, and tail-coordinate patterns printed in the source appendix. The seventh headline code \([200,21,77]\) is excluded because the manuscript does not print its generator data.

The minimum distance quoted for each hull is the exact minimum Hamming weight among its nonzero words, not a lower bound inferred from containment.

## Proof

The source specifies a quasi-cyclic core as follows. For block length \(m\), a divisor \(h\mid x^m-1\) of degree \(k\),
\[
g=(x^m-1)/h,
\]
and multipliers \(f_1,\ldots,f_\ell\), messages
\[
b=\sum_{j<k}b_jx^j
\]
map to
\[
(bg f_1,\ldots,bg f_\ell)\pmod{x^m-1}.
\]
The printed tail rules are linear functions of
\[
r=b\bmod(x^5-1).
\]
Taking \(b=x^j\) for \(0\le j<k\) therefore gives the full generator matrix without any search or choice.

For every reconstructed generator matrix \(G\), exact row reduction confirms the published dimension. Exhaustive Gray-code enumeration of all \(2^k\) words independently reproduces the source minimum distance and the published minimum-shell multiplicity:
\[
(66,2720),\ (68,1156),\ (68,2992),\ (70,3502),\ (72,9826),\ (72,2394).
\]
This anchors the reconstruction to the six printed codes.

Next form the binary Gram matrix
\[
M=GG^{\mathsf T}.
\]
Its ranks are
\[
4,\ 18,\ 1,\ 2,\ 0,\ 1.
\]
Subtracting these from the corresponding code dimensions gives hull dimensions
\[
17,\ 2,\ 20,\ 19,\ 21,\ 21.
\]

A basis of the kernel of \(M\) gives coefficient vectors for a basis of the hull. Exhaustive enumeration of those hull bases gives exact minimum distances
\[
68,\ 104,\ 68,\ 72,\ 72,\ 72
\]
and minimum-shell multiplicities
\[
1360,\ 3,\ 2992,\ 6358,\ 9826,\ 2394.
\]
In the fifth case \(M=0\), so the whole \([184,21,72]\) code lies in its dual.

## Verification

`artifacts/verify.py` uses only the Python standard library. It implements binary polynomial multiplication and exact division, reconstructs all six quasi-cyclic codes from the appendix data, and verifies every published pair \((d,A_d)\) by exhaustive enumeration.

The script then forms each exact Gram matrix, computes its rank and nullspace, maps a nullspace basis back into codewords, and exhaustively enumerates every hull. It checks the complete six-code hull profile and the stated hull minimum distances and minimum-shell multiplicities.

Successful replay prints `VERIFY_OK`.

## Relationship to prior work

The primary paper optimizes and certifies minimum distance and minimum-shell size. Its full text contains no discussion of Euclidean hulls, LCD structure, or self-orthogonality. The appendix supplies enough algebraic data to reconstruct six of the seven record parents exactly.

General work on one-generator quasi-cyclic and circulant codes gives formulas and asymptotic results for hull dimensions, showing that hull structure is a natural invariant of quasi-cyclic codes. Those results do not state the hulls of these newly published record constructions, whose appended tail coordinates also change the Gram matrix.

One component of the present profile deserves a qualification: if an accompanying complete weight distribution shows that every word of the \([184,21,72]\) code has weight divisible by four, then self-orthogonality follows as a standard corollary. The novelty claim therefore does not rest on that isolated observation. It rests on the exact six-code hull dimensions together with the exact minimum distances of the hull subcodes, including the nontrivial codimension-one and codimension-two cases.

Focused searches by arXiv identifier, exact parameters, “hull”, “Euclidean hull”, “self-orthogonal”, and the individual hull dimensions found no prior publication of this six-code profile.

## Limitations

The result concerns the six record codes whose quasi-cyclic constructions are fully printed in the source. It says nothing about the manuscript's \([200,21,77]\) code because the required generator matrix is not supplied there.

The computations establish exact hull parameters for these specific representatives. Hull dimension is not invariant under every possible binary code equivalence that allows arbitrary coordinate scalings over larger fields; here the field is binary and the printed coordinate-permutation model is fixed.

No claim is made that the hull subcodes themselves improve the best-known distance tables at their reduced dimensions.

## References

1. Amal Seddas, Vladyslav Shashkov, Maryna Viazovska, and Emmanuel Abbe, *Evolving Towards Better Codes: LLM-Guided Search for High-Distance Binary Linear Codes*, arXiv:2609.37056v1, 2026.
2. Zohreh Aliabadi, Cem Güneri, and Tekgül Kalaycı, *On the hull and complementarity of one generator quasi-cyclic codes and four-circulant codes*, arXiv:2307.05449.
3. Zohreh Aliabadi, Tekgül Kalaycı, and Mohammad Zadehdabbagh, *Asymptotic performance of double circulant and four circulant codes with small hull dimension*, Cryptography and Communications, 2026.
