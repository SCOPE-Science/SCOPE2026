# Scientific assessment: two distinct pendant edges on a clique

## Correctness
**PASS.** Every pairwise shortest-path distance is specified; direct expansion gives the three independent zero-sum sectors in (1). The fluctuations have strictly negative quadratic form, the antisymmetric block is strictly negative for \(0<p<2\), and the symmetric block has determinant \(-kF_k(p)\) and positive top-left entry. Differentiation proves that \(F_k\) crosses zero exactly once in \((1,2)\). The endpoint kernel vector and the centered-Gram ranks follow directly. Li--Weston Theorem 5.4 proves exclusion of any later positive-type interval. The exact-arithmetic script checks 528 finite test cases, independently of the theorem's analytic proof.

## Originality
**PASS with residual literature risk.** The closest fully inspected primary records are Sánchez (arXiv:1108.0451, Corollary 2.4 and Sections 2--3) and Li--Weston (arXiv:0901.0695, Theorem 5.4). Sánchez supplies the general determinant algorithm and evaluated complete bipartite graphs and different five-vertex examples; it does not state the all-orders scalar equation and spectral kernel for leaves attached at distinct clique vertices. Li--Weston supplies negative-type interval theorems, not an evaluated clique-attachment family. Searches for the distinct-attachment family, its powered-distance determinant, and graph-synonym formulations did not identify direct coverage. Earlier adjacent families with a single shared attachment vertex or a shared clique of size two are not the same graph family. Nonetheless, lack of an indexed match is not priority proof, and other papers about pendant graph metrics may cover it implicitly.

## Value
**PASS.** The object is a minimal, natural two-articulation extension of the complete graph and gives a new parameter axis distinct from one-hub clique bouquets. Its nontrivial \(3^p\) coupling forces a sharp two-sector classification; the theorem determines the exact endpoint, unique degeneracy direction, Euclidean dimension loss, strict order monotonicity, and limiting exponent. These are infinite-family structural facts beyond a one-off determinant calculation. The exact limit and its first correction quantify the effect of increasing clique redundancy while keeping both attachments fixed.

## Limits and sources
The proof is specific to two leaves attached to different core vertices and unit graph shortest-path distances. The relevant general negative-type results are Sánchez 2011 (arXiv:1108.0451) and Li--Weston 2009 (arXiv:0901.0695); publication priority has not been independently certified. No formal proof assistant or third-party audit was used.

Self-review: passed. Independent audit: not yet performed.
