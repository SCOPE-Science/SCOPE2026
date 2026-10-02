# Sharp diameter three for compatible basis pairs in arbitrary rank-3 matroids

## Result

Let \(M\) be any matroid of rank 3. Consider ordered compatible pairs of bases, where one move is a symmetric exchange of one element between the two bases. Within every fixed compatibility class, every two ordered basis pairs are connected by at most three moves. The bound is sharp, for example for the disjoint swap in \(U_{3,6}\).

This quantitative statement includes rank-3 matroids with loops or parallel classes. For simple rank-3 matroids, an upper bound of three is already covered by prior exchange-distance results for paving matroids; the new point retained here is the all-rank-3 bound. The finite simple-type census on 3 through 6 elements is retained as exact calibration data: the global maxima are 0, 1, 2, 3 respectively, with the committed per-type witnesses and shortest paths.

## Proof and finite certificate

For any two compatible ordered basis pairs, the union of their entries has at most six elements. Restricting the matroid to this support preserves the bases and every symmetric exchange relevant to the pair. If the support has fewer than six elements, add loops to obtain a six-label rank-3 matroid without changing the exchange graph.

A rank-3 matroid on six labels is determined by its family of 3-element bases. The committed finite checker enumerates all \(2^{20}\) such families, retains exactly those satisfying the basis-exchange axiom, and computes the compatible-pair exchange components by BFS. There are 2053 nonempty rank-3 base families in this labeled enumeration, and every compatible-pair diameter is at most three.

Sharpness is witnessed in the uniform matroid \(U_{3,6}\): swapping two disjoint ordered bases requires at least three single-element symmetric exchanges and an explicit three-step path is committed.

## Prior coverage

Kashiwabara proved the relevant rank-3 White-connectivity result. Bérczi and Schwarcz proved strong exchange-distance bounds for split matroids, including paving matroids; since every simple rank-3 matroid is paving, their work already supplies the simple rank-3 upper bound of three. This repaired statement therefore does not claim that upper bound as new for simple rank-3 matroids.

## Limitations

The all-rank-3 diameter bound is certified by exhaustive finite computation after the six-element reduction rather than by a hand classification. The per-type simple census is complete only through six elements.
