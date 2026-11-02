# Review of the exact Haar truncated-octahedron section law

## Correctness — PASS

The proposed theorem concerns the 24-vertex regular truncated octahedron, Haar-uniform **central** planes, and generic orientations. The vertex-radius identity \(\|v\|^2=5\) and edge-endpoint identity \(v\cdot w=4\) are verified by enumerating the actual facets and 36 edges. On each of five chambers within \(a>b>c>0\), edge-crossing signs give respectively \(8,10,6,8,6\) sides. The only possible chamber boundaries are the three vertex-orthogonality planes \(a=2b\), \(a=2c\), and \(b=2c\). The decagon cone is a spherical triangle of exact solid angle \(2\arctan(1/B)\), with \(B=11+3\sqrt{14}+4\sqrt6+2\sqrt{21}\). The expected side count follows exactly by integrating one edge's two endpoint signs. Normalization then determines the other two probabilities. The standard-library verifier reproduces the arithmetic and a separate finite Monte Carlo consistency check. Finite computation is not used in place of the all-orientation chamber argument.

## Originality — PASS, with bounded historical-priority risk

The closest inspected full text is Brandenburg–De Loera–Meroni, arXiv:2304.14239v1, which treats the same solid as a three-dimensional permutahedron and studies slicing chambers, all affine section types, and extremizers. Neither Theorem 1.1 nor Example 5.1 states the Haar distribution of central section types or the exact decagon spherical solid angle. Published findings on central sections of the cube, icosahedron, and octahedron concern different solids and do not imply the central truncated-octahedron distribution. The De Leo preprint concerns a periodically extended truncated-octahedron surface; only its abstract was available here. Older specialized stereological tables remain an explicit priority risk and are not represented as ruled out.

## Mathematical value — PASS

The truncated octahedron is both the regular three-dimensional permutahedron and an Archimedean space-filling parallelohedron. A complete, exact orientation probability distribution for central polygonal sections is a natural geometric statistic, not an arbitrary finite parameter. The positive decagon probability \(0.185440454502106\ldots\) is not determined by knowing merely that decagonal sections are possible. The elementary solid-angle calculation provides a reusable, independently checkable benchmark for stereological geometric sampling.

## Limitations and closest work

The classification holds for the regular solid only, under central orientation sampling. It does not cover affine offsets, general 14-faced polyhedra, or complete metric shape statistics of sections. Source comparison is bounded and incomplete for older specialized literature. The theorem has not received an independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
