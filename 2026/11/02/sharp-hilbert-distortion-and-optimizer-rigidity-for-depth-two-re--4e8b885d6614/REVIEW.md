# Scientific review

## Correctness — PASS

The claim is the exact unrestricted real-Hilbert distortion and rigidity for every integer \(r,s\ge2\). A direct variance decomposition of **arbitrary** Hilbert embeddings supplies the lower bound without any assumption of equivariance. The within-branch and different-branch leaf distance inequalities imply \(W\ge2u\) and \(Y/a+W\ge8\); two upper edge constraints give the monotone inequality (3) in `RESULT.md`, whose unique solution is the candidate exact constant. The centered-coordinate-simplex construction independently realizes it. All seven pair types are enumerated and bounded. Equality conditions force the complete Gram matrix, hence uniqueness and dimension \(rs-1\). The branching monotonicity is a direct derivative check. The attached exact-rational program independently reconstructs all pair distances for \(2\le r,s\le17\), while the proof is valid for every admissible pair. Boundary checks include \(r=s=2\), \(r\to\infty\), and \(s\to\infty\).

## Originality — PASS (best-knowledge, residual risk)

Robertson's 2023 paper states the general Hilbert distortion/negative-type equivalence and calculates complete-bipartite and Hamming cases, not the rooted tree here. Linial--Saks (2003) proves asymptotic complete-binary-tree lower bounds, and Babilon--Matoušek--Maxová--Valtr (2003) studies planar target bounds and fans, not this sharp unrestricted value. Searches included depth-two, double-branching, binary seven-vertex, centroid, regular-simplex, Euclidean-distortion, Gram-rigidity and distorted-negative-type formulations. The nearest accessible previous exact result for the *same tree* concerns the negative-type exponent of its snowflakes; that does not imply its least unpowered Hilbert distortion. The nearest prior exact Hilbert-distortion formula for double-stars concerns a different tree. published-finding corpus published findings and both accessible current ledgers were compared by actual claims, not title matching. The 1998 Linial--Magen--Saks paper could not be read in full; its general bound in the abstract neither establishes nor rules out a hidden finite formula. This unresolved priority risk remains expressly recorded, rather than being treated as proof of novelty.

## Mathematical value — PASS

Exact least-distortion constants for growing tree metrics are finer than asymptotic embedding bounds. This complete two-branching-parameter family contains the canonical seven-vertex complete binary tree, gives a sharp dimension-minimal optimizer, and reveals that *every* optimal embedding has forced simplex/orthogonality structure. The limit \(\sqrt{8/3}\) quantifies the large-degree, fixed-depth obstruction and distinguishes it from large-depth asymptotic phenomena. A full exact family and rigidity theorem are not a textbook substitution or numerical table recomputation.

## Closest literature and limitations

Robertson, arXiv:2309.16070v1 (2023), Theorems 2.3--2.4 and Section 4; Linial and Saks, DOI:10.1007/s00454-002-2827-z (2003), complete three-page text; Babilon et al., DOI:10.7155/jgaa.00076 (2003), Sections 1--4. The 1998 general tree-embedding article DOI:10.1007/BF02773475 was abstract-level only due to inaccessible full text. The theorem applies to vertex graph distances on unit-edge depth-two regular trees and real Hilbert targets of arbitrary dimension, not fixed-dimensional embeddings or nonregular trees. The independent scientific audit has not occurred.

Self-review: passed. Independent audit: not yet performed.
