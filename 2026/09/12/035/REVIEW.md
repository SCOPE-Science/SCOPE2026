# Review status

Fresh independent audit: **PASS**. The finding is accepted without a substantive research-file change.

- Correctness: **PASS** — The six positive atoms force exactly the six supporting facets. Their normals split into two complementary coordinate 2-planes, so every origin-interior realizer is the Cartesian product of two right-isosceles triangles. For a triangle with supports h_1,h_2,k and leg length L=h_1+h_2+k sqrt(2), the normalized 2D cone-volume weights are h_1/L,h_2/L,k sqrt(2)/L; product facets halve these weights. Matching the given alpha=(2-sqrt(2))/4 and beta=(sqrt(2)-1)/2 forces h_1=h_2=k in each factor. The centroid coordinate is p(1-sqrt(2))/3, hence nonzero for every p>0. Fresh exact symbolic arithmetic reproduced the normalization, barycenter, weights and centroid. Thus the stated measure has origin-interior realizers but none with centroid at the origin.
- Originality: **PASS** — The closest primary literature gives the subspace-concentration necessity for centroided polytopes and characterizes important symmetric cases, but does not state or imply this explicit non-even six-atom non-realizability example. The exact product classification and centroid obstruction require the record’s support geometry.
- Scientific value: **PASS** — This is a natural low-support boundary example for the discrete logarithmic Minkowski problem: it satisfies probability, zero-barycenter and sharp subspace-concentration constraints yet fails the stronger centroid-at-origin realization condition, and the audit classifies all origin-interior realizers. The obstruction is structural rather than a random finite computation.

See `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json` for the complete assessment.
