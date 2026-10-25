# Scientific review

## Correctness — PASS
For a regular polygon with \(n=2m+1\ge5\), each edge has a unique opposite support vertex. The corresponding edge-vertex triangle contains exactly the points whose generic affine diameter uses that edge. Outside a finite union of segments, multiplicity is the sum of the triangle indicators. Along a generic ray from the center, the triangle count begins at \(n\), ends at \(1\), and drops by two at each longest-diagonal boundary, since each such boundary is shared by exactly two triangles on the same side. This proves the odd support \(\{1,3,\ldots,n\}\) and that each level has positive area. Intersecting all triangles gives the central regular polygon bounded by the longest-diagonal lines. The chord-distance calculation gives inradius \(R\sin(\pi/(2n))\), and dividing by \(\cos(\pi/n)\) gives the circumradius. The area ratio is therefore exact.

## Originality — PASS, with residual risk
The primary paper by Bárány, Hug, and Schneider gives the mean affine-diameter multiplicity and the planar triangle decomposition, but does not state this pointwise all-odd-\(n\) support classification or the maximal-locus area fraction. The closest published pentagon result covers \(n=5\); the constant-width parity theorem has different hypotheses and does not cover regular odd polygons with \(n\ge5\). published-finding corpus queries for regular odd polygons, maximal affine-diameter multiplicity, central longest-diagonal regions, and the exact area fraction returned no equivalent all-\(n\) claim. This does not establish exhaustive historical priority.

## Mathematical value — PASS
The maximal-multiplicity locus is a natural level set of a classical geometric incidence invariant. Its exact area fraction quantifies the proportion of points through which every affine diameter passes and shows a quadratic \(n^{-2}\) decay as the regular polygon approaches the circular regime. The result also supplies an infinite-family parity and support classification beyond the isolated pentagon case. It is not a full distribution theorem: the intermediate-level probabilities remain open here.

## Sources and limitations
The primary text inspected was arXiv:1403.7158v1, including Theorem 1.2, equation (1.4), and the planar triangle decomposition in Section 3. Related public records were available as search summaries only. The result is limited to regular odd polygons with \(n\ge5\); independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
