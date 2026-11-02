# Scientific review: four-permutation universal cycles

## Correctness (PASS)

The claim is an exact all-integer identity for each labeled alphabet of size \(n\ge5\), with cyclic rotations identified and reversal/relabeling retained as distinct. The proof identifies universal cycles with cyclic Euler tours of a regular transition digraph on injective ordered triples. The nontrivial computation is the characteristic polynomial. The rank reduction \(A=JD-R\), the \(R^3=I\) determinant identity, and the decomposition of pair functions into zero-row/column and additive components are derived explicitly. Each invariant piece has a stated dimension and scalar or two-by-two determinant; their products account for every eigenvalue. Substitution at the outdegree and the directed matrix-tree and BEST theorems finish the exact enumeration, without numerical extrapolation. Standalone integer elimination recomputes rooted arborescences for \(5\le n\le8\) and direct characteristic determinants for \(5\le n\le7\). Every test passed. The code is a finite cross-check, not a substitute for the algebraic proof.

## Originality (PASS, with residual literature risk)

The closest full-text comparison is Chang and Xue, *Enumerations of Universal Cycles for \(k\)-Permutations* (https://arxiv.org/abs/2111.13814), first available 2021-11-27. It identifies the generic BEST/matrix-tree method and evaluates \(k=2,3\), but the inspected Sections 1–4 do not give the \(k=4\) factorization or the resulting explicit product. The present calculation supplies the missing spectrum rather than merely restating their general counting principle. OEIS A120061 (https://oeis.org/A120061) covers shorthand cycles \(k=n-1\), hence the \(n=5,k=4\) boundary but not the all-\(n\) fixed-window theorem. Chen–Ghorbani–Wong's arrangement-graph article (https://doi.org/10.37236/3711) studies a different adjacency rule, and Kitaev–Potapov–Vajnovszki (https://doi.org/10.1016/j.dam.2019.01.025) studies shortened/relative-order cycles. Searches for the exact fixed-four-permutation spectrum and product formula did not uncover an equivalent published theorem. The residual risk is that a less discoverable general spectral theorem might specialize to this case; lack of search hits is not itself a proof of novelty.

## Value (PASS)

A 2021 study explicitly solved window lengths two and three while leaving general window length open for exact enumeration. The four-letter case is the natural next structural step, for all alphabet sizes, and its closed factorization turns an \(n(n-1)(n-2)\)-dimensional determinant into a fixed collection of small polynomial factors. In particular the first non-shorthand case \(n=6\) has an exact new candidate count, \(2^{171}3^{43}5^8 7^{16}\), while the already known \(n=5\) count serves as a separate check. The result is a complete infinite-family enumeration rather than an arbitrary numerical slice or general-method restatement.

## Limitations and closest literature

The classification concerns literal four-letter permutations over a fixed labeled alphabet and counts rotation classes. It does not apply to order-isomorphic pattern cycles, arbitrary forbidden languages, or all window sizes. The arXiv primary text, OEIS entry, and the relevant distinct-graph and shortened-cycle articles were examined at the levels described above. These comparisons support, but cannot establish, universal priority. No independent external scientific audit is claimed.

Self-review: passed. Independent audit: not yet performed.
