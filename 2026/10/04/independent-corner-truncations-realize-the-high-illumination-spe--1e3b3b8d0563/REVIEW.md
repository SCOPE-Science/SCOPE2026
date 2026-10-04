# Review

## Correctness

PASS. For an independent truncation set \(T\), distinct truncating hyperplanes cannot meet inside the cube, and each cut creates exactly the \(n\) expected edge vertices. Every surviving cube vertex retains its full cube tangent cone, so distinct surviving vertices require disjoint illuminating sign orthants and give the lower bound \(2^n-|T|\). Conversely, for a cut vertex on the edge from \(t\) toward its neighbor \(w\), independence guarantees \(w\notin T\). The direction \(-w\) strictly enters every active coordinate facet and the cut facet, since its derivative there is \(-(n-2)\). Thus the \(2^n-|T|\) directions attached to surviving vertices illuminate every polytope vertex and hence the whole boundary.

The exact cube sandwich proves the metric-nearness claim. The packaged checker replays all local inequalities with rational arithmetic and exhausts substantial finite subfamilies. The all-dimensional statement rests on the analytic proof, not the finite checks.

## Originality

PASS with a specific prior-covered endpoint. Livshyts--Tikhomirov's full primary text proves the common near-cube upper bound \(2^n-1\) and, in Remark 1.2, constructs a one-corner perturbation with exact illumination number \(2^n-1\). That endpoint is explicitly treated as prior work.

The same full text contains no corner-truncation family or illumination spectrum, and its general theorem does not imply exact values below \(2^n-1\). Targeted searches for simultaneous cube-corner truncation, deleted/truncated vertex families, parity classes, independent sets, and the exact count \(2^n-|T|\) did not locate an equivalent statement. The closest published indexed computation concerns isolated three-dimensional parallelohedron representatives, not an all-dimensional family arbitrarily close to the cube.

## Value

PASS. The primary source emphasizes that illumination is highly discontinuous under small boundary perturbations while proving only the first strict drop from the cube. The present family quantifies that discontinuity much more sharply: arbitrarily close to the cube, every illumination number in the entire interval from \(2^{n-1}\) to \(2^n\) occurs. The result also exposes a clean graph-geometric mechanism—independent cube corners correspond exactly to directions that can be removed while neighboring surviving directions illuminate the new cut vertices. This is a structural spectrum theorem rather than a routine one-parameter increment.

Same-model review: passed. Independent audit: not yet performed.
