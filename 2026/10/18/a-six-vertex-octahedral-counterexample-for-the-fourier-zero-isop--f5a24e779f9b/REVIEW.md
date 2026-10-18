# Review of the six-vertex Fourier-zero obstruction

## Correctness: PASS
For every real axial frequency and every transverse frequency satisfying \(v^2+w^2\le2\), exact differentiation of the Fourier transform of a diamond cross-section gives \(\Phi''(r)\ge4(1-r^2)\), which is strictly positive for \(0\le r<1\). Two integrations by parts with the correct endpoint conditions express the axial Fourier transform as a strictly positive integral of \(g''(t)(1-\cos(aut))\); zero axial frequency is covered by \(g>0\). A separate exact integral along \((0,s,s)\) proves that some real Fourier zero exists. Closedness and bounded minimizer selection then justify the strict lower bound on the nearest-zero radius. The volume and ball transform use the stated Fourier normalization. The rational ninth-order sine/cosine certificate verifies \(\kappa(B_{101})<\sqrt2\) and the inequality for integral vertices without relying on a numerical root approximation. Independent audit remains unperformed.

## Originality: PASS, with documented priority risk
The motivating 2026 paper gives counterexamples with rotationally symmetric disk sections, not the six-vertex polyhedral cross-polytope considered here; the 2009 body-of-revolution example also has circular sections. Three published quantitative subsequent comparisons were read at their actual full RESULT texts and likewise treat circular sections, a Bessel kernel, or the asymptotic coefficient for that family. Their conclusions neither imply the present diamond-section curvature calculation nor guarantee a six-vertex integer-coordinate counterexample. Research-index queries for octahedra, cross-polytopes, Fourier zeros and minimal vertex complexity did not identify a dominating statement. This comparison is stronger than title or number matching, but hidden or unindexed priority remains a residual risk; lack of search hits is not treated as a proof of uniqueness.

## Mathematical value: PASS
The 2026 disproof established failure of equal-volume-ball extremality for arbitrary centrally symmetric convex bodies, but did not quantify the minimum vertex complexity of a polyhedral obstruction. Every full-dimensional centrally symmetric three-dimensional polytope has at least three antipodal vertex pairs. This construction attains that natural combinatorial minimum, provides explicit integer coordinates and a checkable analytic Fourier positivity cylinder, and illustrates that the obstruction persists on the smallest symmetric polytope. The sufficient parameter 101 and strip width are not claimed individually optimal; the value is the exact minimal-complexity witness rather than another parameter adjustment of a known circular example.

## Closest sources and limitations
- Gómez-Serrano, Levitin, Platt, Polterovich (2026), arXiv:2609.10517v1, Sections 1–2: circular-base bipyramids, qualitative general failure and disk sections.
- Benguria, Levitin, Parnovski (2009), arXiv:0801.1617v3, Remark 4.11: body of revolution with circular transverse geometry.
- *A Pólya–Bessel zero-free strip for Fourier bipyramids* (2026), identifier `72c1da0f9bb0`: circular-base explicit transverse Bessel strip.
- *A rationally certified width-two Fourier zero-free strip for three-dimensional bipyramids* (2026), identifier `7d5ef01cc46e`: stronger bound, still for circular sections.
- *Exact leading slope of Fourier-zero distance for elongated bipyramids* (2026), identifier `328d6e388fdc`: asymptotics of the same circular-section family.

The nearest Fourier zero of the octahedron is not evaluated exactly, and no optimal threshold over all six-vertex polytopes is claimed. Priority remains subject to undiscovered earlier treatment of anisotropic octahedra.

Self-review: passed. Independent audit: not yet performed.
