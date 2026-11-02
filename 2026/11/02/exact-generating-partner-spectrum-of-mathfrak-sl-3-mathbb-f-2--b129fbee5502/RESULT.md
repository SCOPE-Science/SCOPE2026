# Exact generating-partner spectrum of \(\mathfrak{sl}_3(\mathbb F_2)\)

## Finding

Let \(L=\mathfrak{sl}_3(\mathbb F_2)\), an eight-dimensional Lie algebra with \(|L|=256\), and write
\[
N(X)=\#\{Y\in L:\langle X,Y\rangle_{\mathrm{Lie}}=L\}.
\]
There are seven similarity classes under \(\mathrm{GL}_3(\mathbb F_2)\). The complete conditional generation profile is

| Representative \(X\) | Class size | \(N(X)\) |
|---|---:|---:|
| \(0\) | 1 | 0 |
| \(E_{12}\) | 21 | 0 |
| \(E_{12}+E_{21}\) | 84 | 64 |
| \(E_{13}+E_{21}\) | 42 | 64 |
| \(\operatorname{diag}(1,1,0)\) | 28 | 0 |
| \(\begin{pmatrix}1&0&1\\0&1&0\\1&0&0\end{pmatrix}\) | 56 | 72 |
| \(\begin{pmatrix}1&1&1\\1&1&0\\1&0&0\end{pmatrix}\) | 24 | 56 |

In particular, a nonzero element has no generating partner **if and only if** it is either rank-one square-zero or rank-two idempotent. There are exactly 49 such nonzero elements. The total number of ordered generating pairs is
\[
21(0)+84(64)+42(64)+28(0)+56(72)+24(56)=13{,}440,
\]
so the generating-pair probability for independent uniform \(X,Y\) is exactly
\[
\Pr(\langle X,Y\rangle_{\mathrm{Lie}}=L)=\frac{105}{512}.
\]
The complete distribution of the dimension of the generated Lie subalgebra, over all \(65{,}536\) ordered pairs, is
\[
\begin{array}{c|rrrrrrrrr}
\dim&0&1&2&3&4&5&6&7&8\\\hline
\#&1&765&3618&7392&20160&20160&0&0&13440
\end{array}.
\]

## Assumptions and scope

The field is exactly \(\mathbb F_2\), not a general field of characteristic two. All matrices are \(3\times3\) with zero matrix trace. Generation is **Lie generation**, using linear combinations and brackets \([X,Y]=XY-YX=XY+YX\), not associative-algebra or group generation. Every ordered pair, including pairs containing zero or repeated elements, is counted once. The similarity group is \(\mathrm{GL}_3(\mathbb F_2)\).

## Proof

**The seven possible similarity classes.** Every traceless \(3\times3\) binary matrix has characteristic polynomial \(t^3+st+d\), where \(s,d\in\mathbb F_2\). Rational canonical form gives exactly the following seven cases: three nilpotent Jordan types (zero, type \((2,1)\), type \((3)\)); two types for \(t(t+1)^2\) (one size-two Jordan block and one semisimple); one type for \((t+1)(t^2+t+1)\); and one type for the irreducible cubic \(t^3+t+1\). The seven representatives above realize these cases.

The invertible centralizers of these representatives inside \(\mathrm{GL}_3(\mathbb F_2)\) have orders, in displayed order,
\[
168,\ 8,\ 2,\ 4,\ 6,\ 3,\ 7.
\]
These follow from the invertible units of the relevant truncated polynomial rings, the block-diagonal centralizer for the semisimple type, and \(\mathbb F_4^\times\), \(\mathbb F_8^\times\) for the last two types. Since \(|\mathrm{GL}_3(\mathbb F_2)|=168\), orbit-stabilizer yields sizes \(1,21,84,42,28,56,24\), totaling all 256 elements.

**Exact finite closure certificate.** For any pair \((X,Y)\), start with their linear span \(V_0\). Repeatedly enlarge the current span with brackets of its basis vectors and take the new linear span. Each strict enlargement increases dimension; dimensions never exceed eight, so the process terminates after at most eight independent-vector insertions. The final space is a Lie subalgebra containing \(X,Y\), and every Lie subalgebra containing \(X,Y\) contains each enlargement. Hence the final space is exactly \(\langle X,Y\rangle_{\mathrm{Lie}}\). In characteristic two, matrix entries and Gaussian elimination are exact bit operations, with no numerical approximation.

For each of the seven class representatives, the standalone `checks/orbit_census.py` enumerates **all** 256 possible partners, computes this closure, and obtains the seven \(N(X)\) values in the table. It also enumerates all 168 invertible \(3\times3\) matrices, verifies seven pairwise disjoint conjugacy orbits of the displayed sizes, and checks that they cover the entire trace-zero space. Conjugation preserves the Lie bracket, so \(N(gXg^{-1})=N(X)\); thus the seven representative calculations prove the universal conditional table for every \(X\in L\).

For additional independent arithmetic routes, `checks/full_census.py` uses a fixed eight-element traceless matrix basis, bilinear structure constants, and an eight-bit echelon closure; `checks/full_census.cpp` instead uses nine-bit row-major matrices, direct binary matrix multiplication, and its own closure. Both exhaust all \(256^2=65{,}536\) ordered pairs and recover the complete dimension distribution. The computations are **exhaustive finite proofs for this finite algebra**, not samples from which an infinite-field theorem is inferred.

The statements about the 49 nonextendable nonzero elements and the rational probability follow immediately from the table and the orbit sizes. The dimension counts follow from the full enumerations.

## Verification

From the directory containing this document and the `checks` subdirectory, run

```sh
python3 checks/full_census.py
python3 checks/orbit_census.py
g++ -O3 -std=c++17 checks/full_census.cpp -o full_census
./full_census
```

Each prints `VERIFY_OK`. Reference outputs are provided as `checks/full_census_py.out`, `checks/orbit_census.out`, and `checks/full_census_cpp.out`. The programs use only Python's standard library or a GNU-compatible C++17 compiler. The two full enumerations use different matrix representations and bracket implementations. The third verification uses conjugacy-orbit reduction and independently checks orbit coverage.

## Relationship to prior work

Jezernik and Zozaya (arXiv:2606.31747, publicly posted June 30, 2026) establish an asymptotic random two-generation theorem for special linear Lie algebras, but the exact \(\mathbb F_2\), rank-three conditional spectrum is not part of the asymptotic claim inspected. Cantor, Jezernik, and Zozaya (arXiv:2404.11240, initially April 17, 2024) establish existence of two generators outside two exceptional parameter pairs; existence does not imply conditional counts or one-and-a-half generation. Chistopolskaya (arXiv:1804.09457, Example 3, pp. 5–6) demonstrates the special binary obstruction for \(E_{12}\) when **the second generator is required to be nilpotent**. The present exact result permits every traceless second generator and classifies the complete response for every first generator. A broader historical priority claim is not made.

## Limitations

The result is specific to \(\mathfrak{sl}_3(\mathbb F_2)\). It is not a formula for arbitrary field order or rank, and it is not an independent mathematical audit of the code or proof. The original full text of the 2024 two-generation paper was not accessible in this review; its abstract and the statements quoted by later papers were compared, so priority beyond the material read remains a residual risk. The detailed 2026 random-generation paper was inspected via its publicly accessible text, but coverage of every obscure older enumeration cannot be ruled out. A compiler/interpreter with ordinary integer semantics is assumed for replay.

## References

1. U. Jezernik and A. Zozaya, *Random generation of the special linear Lie algebra over finite fields*, arXiv:2606.31747, version 1, June 30, 2026. https://arxiv.org/abs/2606.31747
2. O. Cantor, U. Jezernik, and A. Zozaya, *Two-generation of traceless matrices over finite fields*, arXiv:2404.11240, initially April 17, 2024; *Linear Algebra and its Applications* 713 (2025), 1–17. https://arxiv.org/abs/2404.11240
3. A. Chistopolskaya, *On nilpotent generators of the Lie algebra* \(\mathfrak{sl}_n\), arXiv:1804.09457, Example 3 (2018). https://arxiv.org/abs/1804.09457
