# Mathematical review: collective multipartite negative-type thresholds

## Correctness — PASS
For each zero-sum vector \(\alpha\), separating its part-sum vector \(u\) and within-part zero-sum residuals \(v\) gives the exact identity
\[
\alpha^{\mathsf T}D_p\alpha=(2^p\sum_i(1-1/n_i)u_i^2-\sum_i u_i^2)-2^p\sum_i\|v_i\|_2^2.
\]
This identity implies the stated complete negative-type threshold without any enumerative assumption. The Rayleigh–Ritz characterization proves the repeated-maximum and unique-secular-root cases, including the top-eigenspace multiplicities. Centered-distance Gram rank gives the affine embedding dimension. For the nonlocal obstruction, the two-valued compression computes the strict interval and an explicit rational witness gives quadratic value \(3/8\) at \(p=\log_2(3/2)\). The standalone exact-rational checker completed 315 generic quadratic-identity tests and the critical rational comparisons. The mathematical proof, rather than these finite tests, establishes all sizes and exponents.

## Originality — PASS, qualified
The closest directly relevant prior work is Nobuaki Obata, *Complete Multipartite Graphs of Non-QE Class* (arXiv:2206.05848v1, Sections 1 and 3–4). It already gives the exact quadratic-embedding constant and classification of complete multipartite graphs at the **fixed exponent \(p=1\)**, using an adjacency-matrix secular equation. That fixed-exponent result and its consequences are not new here. Sánchez (arXiv:1108.0451v1) supplies a general finite-distance-matrix threshold method and the bipartite case; Robertson (arXiv:2309.16070v1, Section 4.1) works out bipartite negative-type embeddings; Das and Mohanty (arXiv:2012.04341 and arXiv:2311.01069v1) treat multipartite squared-distance matrices at the fixed exponent two. None of the inspected relevant statements establishes the all-exponent compressed formula, the rank changes at the variable threshold, or a specific interval in which all two-part induced subgraphs have strict negative type while the full multipartite graph fails it.

General finite-metric determinant criteria and Obata's finite-dimensional compression method can be adapted or specialized; they create genuine residual priority risk. A new theorem that is merely a restatement of the \(p=1\) classification is explicitly excluded. The reviewed claim is the complete all-exponent threshold and collective-obstruction classification, not ownership of the original methods.

## Mathematical value — PASS
The finding identifies the precise Hilbert-embeddability exponent and affine rank for a natural infinite graph class. Its nonpairwise obstruction explains why inspecting only complete bipartite induced subgraphs misses the sharp threshold. The dimension drop and the concrete strict counterexample are structural results not implied by the mere numerical value of the known \(p=1\) quadratic embedding constant.

## Limitations and priority risks
The graphs are finite, unweighted and complete multipartite. Optimal Hilbert distortion beyond the negative-type threshold is not determined. Comparable explicit formulas in broader generalized-roundness or Euclidean-distance-matrix literature could narrow originality. The 2020 multipartite squared-distance study was inspectable only through its bibliographic abstract and later related article, not its full paper. Independent assessment is outstanding.

Self-review: passed. Independent audit: not yet performed.
