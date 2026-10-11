# Same-model review

## Correctness
PASS. The published sweep-polytope normalization is used exactly. The chord identity \(a_i-a_j=2i\,e^{\pi i(i+j)/n}\sin(\pi(i-j)/n)\) shows that all generators fall into \(n\) equally spaced direction classes indexed by \(i+j\pmod n\). For odd \(n\), these classes form one rotation orbit and the exact sine sum gives common side length \(\cot(\pi/(2n))\), so the output is regular. For even \(n\), the two residue parities give side lengths \(2\cot(\pi/n)\) and \(2\csc(\pi/n)\). Solving the two adjacent support equations proves cyclicity and the stated area formula. The unequal alternating edge lengths also force the exact even-order symmetry group.

## Originality
PASS. The primary full text was inspected at the sweep-polytope definition, normal fan, permutahedral projection, and examples; it contains no regular-polygon specialization. Candidate-specific indexed and web searches covered sweep polytope, shellotope, chord zonotope, pairwise-difference zonotope, regular polygon, alternating edge lengths, area, and perimeter formulations. No covering statement was located. The older shellotope precursor was accessible only at abstract/metadata level and is carried as an explicit residual risk. A previously checked general zonotope-radius theorem concerns centered radii and tangent facets rather than the accepted side-orbit, regularity, symmetry-order, perimeter, and area theorem.

## Value
PASS. The result completely describes the Euclidean shape of a canonical two-dimensional sweep-polytope family. It exposes a genuine parity-driven symmetry transition: odd regular polygons produce regular \(2n\)-gons and double their Euclidean symmetry order, while even regular polygons produce nonregular cyclic equiangular \(2n\)-gons with two exact alternating edge orbits. The closed perimeter and area formulas make the classification quantitatively complete.

## Closest literature and limitations
Padrol--Philippe provide the construction and its combinatorial interpretations, while Gritzmann--Sturmfels provide the older shellotope context. The theorem is restricted to unit-circumradius regular planar inputs and does not classify arbitrary cyclic or affinely regular configurations. Older shellotope terminology remains the principal residual indexing risk.

Same-model review: passed. Independent audit: not yet performed.
