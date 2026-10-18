# Review of the pentagonal-generator symmetry classification

## Correctness
PASS. The standard three-generator symmetry/gluing equivalence is stated as Theorems 9–10 of García-Sánchez–Viola (2015). The proof reduces possible pair gcds to at most two or a divisor of 35 and gives explicit strict inequalities excluding all n at least 71; its modular identity for the nonadjacent pair then contradicts that bound. The finite interval 3–70 (excluding the separately resolved redundant index 5) is exhausted by exact integer arithmetic in `verify.py`. Independent Apéry shortest paths reproduce the symmetric indices 2, 3, 5, 40 and the stated Frobenius values. The argument covers every integer n at least two and all three possible gluing pairs.

## Originality
PASS on the inspected-source comparison. OEIS A069757 is the closest exact-object resource; it tabulates Frobenius values but gives no all-index symmetry criterion. The full García-Sánchez–Viola paper covers the general three-generator structural characterization and hence supplies a proof ingredient, not the arithmetic pentagonal specialization or four exceptions. The full Lepilov–O'Rourke–Swanson paper addresses consecutive squares/cubes. The Fel preprint concerns powers of consecutive integers. An indexed-result comparison returned only results about different semigroup families, pentagonal exponent maps, or complete-intersection geometry. Residual risk: an uncatalogued classification or an alternative encoding could cover the same four-index statement; lack of a match cannot establish absolute novelty.

## Value
PASS. The family is a natural, previously tabulated Frobenius problem. Symmetry detects its Gorenstein/complete-intersection cases, a structural property not recoverable from the displayed Frobenius values alone. The classification identifies a notably isolated nontrivial 35-gluing at index 40 and proves that no further exceptions occur, providing a complete answer rather than a finite table or an arbitrary parameter slice. Its method exploits arithmetic rigidity of consecutive pentagonal differences.

## Sources, risks, and scope
Primary comparisons: OEIS A069757 (public revision May 16, 2003); García-Sánchez and Viola (2015), full Sections 2.2–2.4; Lepilov, O'Rourke, and Swanson (2015), full introduction and squares/cubes results; Fel (2016), abstract. The result does not classify centered polygonal families or arbitrary figurate degrees. The accompanying computation is finite and supplies no independent infinite proof beyond the displayed inequalities.

Self-review: passed. Independent audit: not yet performed.
