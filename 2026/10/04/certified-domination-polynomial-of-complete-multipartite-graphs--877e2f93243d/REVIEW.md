# Review of Certified domination polynomial of complete multipartite graphs

## Correctness
PASS. In \(K_{n_1,\ldots,n_r}\), a selected vertex in part \(X_i\) has exactly \(q-c_i\) neighbors outside the selected set. Therefore the certified condition is exactly the exclusion of \(q-c_i=1\) on every selected part. The domination condition is independently characterized by support on at least two parts or by selecting one entire part. The polynomial follows by starting from the domination polynomial, removing all size-\(N-1\) sets, removing every half-shadowed-part family for complements of size at least two, and restoring the only possible pairwise overlaps. Definition-level enumeration agrees through order ten, and the formula matches the published \(K_{3,n}\) coefficients in tested cases.

## Originality
PASS. The foundational source gives certified domination numbers for complete bipartite graphs, not an arbitrary complete-multipartite set enumerator. The highly relevant 2025 paper gives the polynomial only for \(K_{3,n}\); its full theorem was inspected, and the present formula specializes to it while covering all part numbers and sizes. Targeted semantic searches found no arbitrary complete-multipartite certified-domination polynomial. The closest indexed certified-domination result concerns extremal gaps on connected graphs and does not imply this enumeration.

## Value
PASS. The 2025 special-case paper demonstrates that counting certified dominating sets is a studied object, while the current theorem replaces a family-specific piecewise count by a uniform arbitrary-multipartite formula. The all-set profile criterion also exposes the exact half-shadowed obstruction and can be used directly for coefficient extraction and random-set questions.

Same-model review: passed. Independent audit: not yet performed.
