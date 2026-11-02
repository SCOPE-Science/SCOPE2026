# The complete symmetry census of simple four-dimensional binary evolution algebras

## Finding
Let \(E_A\) range over four-dimensional evolution algebras over \(\mathbb F_2\) with natural basis \(e_0,e_1,e_2,e_3\) and products \(e_i e_j=0\) for \(i\ne j\) and \(e_i^2=\sum_{j=0}^3 a_{ij}e_j\). Require \(A=(a_{ij})\in\operatorname{GL}_4(\mathbb F_2)\) and that \(E_A\) be simple. There are exactly \(11{,}658\) such labeled structure matrices and \(516\) isomorphism classes. Their **complete abstract automorphism-group spectrum** is:

| \(\operatorname{Aut}(E_A)\) | Labeled matrices | Isomorphism classes |
| --- | ---: | ---: |
| Trivial | 11,064 | 461 |
| \(C_2\) | 540 | 45 |
| \(C_3\) | 24 | 3 |
| \(C_4\) | 12 | 2 |
| \(C_2\times C_2\) | 6 | 1 |
| \(S_3\) | 8 | 2 |
| \(D_8\) (order eight) | 3 | 1 |
| \(S_4\) | 1 | 1 |
| **Total** | **11,658** | **516** |

The alternating group \(A_4\) cannot occur as the full automorphism group in this family, although it is a subgroup of \(S_4\). Every other abstract subgroup type of \(S_4\) occurs. Exactly \(461\) of the \(516\) isomorphism classes are automorphism-rigid. One representative in each row, encoded by \(m=\sum_{i,j} a_{ij}2^{4i+j}\), is respectively \(4699,4698,14686,4740,31725,31711,47085,31710\).

## Assumptions and scope
Only the coefficient field \(\mathbb F_2\) and dimension four are considered. Matrices are *labeled*, meaning they are written relative to the ordered natural basis. A perfect evolution algebra satisfies \(E_A^2=E_A\), equivalently \(\det(A)\ne0\). An algebra is *simple* when its only two-sided ideals are \(0\) and itself. Isomorphisms and automorphisms are \(\mathbb F_2\)-linear algebra maps. Group names in the table are abstract isomorphism types, not conjugacy classes of subgroup embeddings in \(S_4\).

## Proof
**Step 1: intrinsic description of all automorphisms.** Let \(f:E_A\to E_B\) be an algebra isomorphism, with both structure matrices nonsingular. Write \(f(e_i)=\sum_k t_{ki}e'_k\). Because \(f(e_i)f(e_j)=0\) for \(i\ne j\), and the vectors \((e'_k)^2\) are linearly independent, \(t_{ki}t_{kj}=0\) for all \(k\) and \(i\ne j\). Thus the supports of distinct columns of the invertible matrix \(T=(t_{ki})\) are disjoint; four nonempty disjoint supports in four rows must each be singletons. Hence \(T\) is monomial. Over \(\mathbb F_2\) its nonzero entries are all \(1\); consequently, \(f\) permutes the natural basis. The relation \(f(e_i^2)=f(e_i)^2\) says precisely that the two binary structure matrices are simultaneous row-and-column permutations. Therefore \(\operatorname{Aut}(E_A)\) is the stabilizer of \(A\) under \(S_4\) acting on its two indices.

**Step 2: simplicity criterion.** Draw the directed graph with vertices \(0,1,2,3\) and arrow \(i\to j\) when \(a_{ij}=1\). If it is not strongly connected, the vertices in any terminal strongly connected component form a nonempty proper set closed under outgoing arrows. Their basis span is then a proper nonzero ideal. Conversely, if the graph is strongly connected and \(I\) is a nonzero ideal, choose \(x=\sum_j x_je_j\in I\) with \(x_i=1\). Then \(xe_i=e_i^2\in I\). Each arrow \(i\to j\) gives \(e_i^2e_j=e_j^2\in I\); strong connectivity propagates this to every \(e_j^2\). Because \(A\) is invertible, these four squares form a basis, so \(I=E_A\). Thus **simple is equivalent to nonsingular plus strongly connected**.

**Step 3: exhaustive finite calculation.** Every binary matrix is represented uniquely by the integer \(m\) in the range \(0\le m<2^{16}\), using the bit convention in the Finding. Define \(d(m)\in\{0,1\}\) as its determinant mod two and \(c(m)\in\{0,1\}\) as the indicator that every nonempty proper vertex set has an outgoing edge. By Steps 1–2, exactly those \(m\) satisfying \(d(m)c(m)=1\) contribute. There are precisely \(65{,}536\) candidate integers. For each qualifying \(m\), compute the full set of the \(24\) index permutations fixing all sixteen bits, classify this subgroup of \(S_4\), and use orbit-stabilizer: each isomorphism class with a stabilizer of order \(h\) contains exactly \(24/h\) labeled matrices. This explicitly finite sum gives the first table and \(11{,}658\) simple matrices.

The summation has **two independently realized exact algorithms** in the supplied source. `verify.py` uses binary Gaussian elimination, reachability, all stabilizers, and orbit-canonical representatives; it checks determinant parity and the proper-sink-set condition against the original predicates for every one of the \(65{,}536\) matrices. `verify_subgroups.py` instead generates the **thirty** subgroups of \(S_4\), forms each subgroup's orbits on sixteen matrix positions, enumerates its invariant zero-one matrices, evaluates determinant parity and the sink-set criterion, and obtains the counts with *exact* stabilizer by descending supergroup inclusion-exclusion. The independent labeled group-count vector is the same in both calculations.

There is also a separate Burnside check: the number of qualifying matrices fixed by one permutation of each cycle type \(1^4,2\,1^2,2^2,3\,1,4\) is respectively \(11658,72,62,9,6\). Hence the number of orbits is
\[
\frac{11658+6\cdot72+3\cdot62+8\cdot9+6\cdot6}{24}=516.
\]
Furthermore, \(A_4\) and \(S_4\) have the same orbits on ordered pairs of distinct vertices, because \(A_4\) is two-transitive. Therefore an \(A_4\)-invariant zero-one matrix is already \(S_4\)-invariant. This independently explains the absence of exact automorphism group \(A_4\).

## Verification
Execute `python3 verify.py` and `python3 verify_subgroups.py` from the directory containing the two scripts. Both print `VERIFY_OK`. Their recorded outputs are included. The first checker confirms the previously published \(908\) isomorphism classes of **all** four-dimensional perfect algebras over \(\mathbb F_2\), before restricting to simple ones. All computations use integer and Boolean arithmetic only, no random choices or external packages. The calculations are exhaustive *for the precisely bounded sixteen-bit universe*; no result for larger dimensions is extrapolated.

## Relationship to prior work
Wei and Zou (2023), Theorem 6.1 and Example 6.1, establish the aggregate count \(908\) of all four-dimensional perfect evolution-algebra classes over \(\mathbb F_2\); their all-perfect formula is used as an external check, **not claimed as new**. Their classification does not give the joint simplicity/automorphism-group distribution above. Kaygorodov, Martín González and Viruel (2026) motivate precise automorphism-realization questions for simple evolution algebras over arbitrary fields and survey graph methods, but the accessible material does not report this exact four-dimensional binary spectrum. A 2023 study of tensor-product evolution algebras classifies a restricted tensorially decomposable four-dimensional family, not every simple binary algebra here.

## Limitations
The result concerns all isomorphism classes inside the defined finite family, not a classification of algebras over larger fields or in other dimensions. The exhaustive computation and its independently coded subgroup-inclusion check support the finite counts; they are not independent human audits. A complete review of every historical classification is not available; historical priority for the refined table is not established beyond the reported source comparisons. The 2026 survey was accessible in abstract and indexed overview form, but not as complete primary full text during this review. The 2018 preprint on non-simple four-dimensional perfect evolution algebras was not available in full text; its possible implications for an aggregate simple count remain a priority risk, while the full automorphism-group refinement was not found there by accessible search.

## References
1. I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (first public October 15, 2026), https://arxiv.org/abs/2610.22248.
2. Y. Wei, Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368v1 (October 18, 2023), Theorem 6.1 and Example 6.1, https://arxiv.org/pdf/2310.12368.
3. Y. Cabrera Casado et al., *Tensor Product of Evolution Algebras*, Mediterranean Journal of Mathematics 20 (2023), article 43, https://doi.org/10.1007/s00009-022-02246-5.
4. Y. Cabrera Casado et al., *Classification of four dimensional perfect non-simple evolution algebras*, arXiv:1801.03856, https://arxiv.org/abs/1801.03856 (access limited).
