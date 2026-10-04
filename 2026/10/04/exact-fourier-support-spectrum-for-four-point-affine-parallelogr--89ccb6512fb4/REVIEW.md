# Same-model review

## Correctness
**PASS.** Affine normalization reduces the transform to \\(P(X,Y)=a+bX+cY+dXY\\) on \\(\\mu_5^2\\), with each local frequency repeated \\(5^{d-2}\\) times. The factorable case \\(ad=bc\\) gives zero counts \\(0,5,9\\). In the nonfactorable case each row contains at most one zero. Five zeros would make the induced fractional-linear map permute the regular pentagon; exact Möbius rigidity then forces a rotation or reflection, each incompatible with four nonzero bilinear coefficients. Explicit exact cyclotomic witnesses realize zero counts \\(0,1,2,3,4,5,9\\). The verifier independently checks all seven witnesses and the complete pentagon Möbius-permutation lemma.

## Originality
**PASS.** The closest inspected source, Delvaux--Van Barel TW 477, gives the unrestricted Hamming number \\(H_{F_5\\otimes F_5}(4)=10\\), not the complete spectrum for a fixed four-column affine parallelogram. Bonami--Ghobber Proposition 21 gives the same global minimum and Theorem 23 classifies its equality cases as line-supported, which excludes the present support geometry from the global extremizers but does not determine the value \\(16\\) or the remaining attainable sizes. Searches also used fixed-support, bilinear-polynomial, fifth-root, Möbius, and rank-deficient-submatrix formulations. No inspected source gave the seven-value spectrum or the forbidden band. Residual risk remains that an equivalent fixed-column result is buried in specialized Fourier-minor or cyclotomic literature.

## Value
**PASS.** This is a natural complete classification for the smallest two-dimensional four-point product geometry over \\(\\mathbb F_5\\). It sharpens the unrestricted four-sparse minimum \\(10\\) to the geometry-sensitive minimum \\(16\\), identifies every attainable Fourier-support size, and proves a three-value forbidden interval. The proof isolates a reusable structural mechanism: factorization versus Möbius rigidity of the root-of-unity grid.

The result is deliberately limited to this support geometry and prime \\(5\\); it is not presented as a general prime-field classification.

Same-model review: passed. Independent audit: not yet performed.
