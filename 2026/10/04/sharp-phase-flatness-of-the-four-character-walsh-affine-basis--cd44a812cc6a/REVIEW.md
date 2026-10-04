# Review

## Correctness
**PASS.** The proof converts the eight Walsh samples into all signed sums of four unit vectors and identifies their maximum norm with the circumradius of the zonogon \(Z=\sum_j[-u_j,u_j]\). The zonogon has perimeter \(16\) and at most eight sides. The sharp perimeter bound for an \(m\)-gon in a radius-
\(R\) disk gives \(16\le16R\sin(\pi/8)\), hence \(R^2\ge4+2\sqrt2\). Equality in the polygon bound forces a regular octagon, and the edge directions of a four-generator zonogon give the stated complete phase classification. The exact verifier confirms the displayed equality case but is not used to infer the theorem.

## Originality
**PASS.** Neuwirth's full text treats maximum-modulus and Sidon-constant questions for three continuous Fourier characters and explicitly frames phase variation and unimodular multipliers. Seigner's full text treats finite Rademacher sums inside the proof that the infinite Rademacher Sidon constant is \(\pi/2\), including equal-modulus root-of-unity phases for asymptotic sharpness. Neither inspected source states or implies the exact four-term equal-modulus minimax \(4+2\sqrt2\) with the regular-octagon equality classification. published-finding corpus searches using Walsh, Rademacher, Sidon, unimodular-phase, and regular-octagon formulations returned no covering finding. The remaining risk is an equivalent older convex-geometry statement about circumradii of four-generator unit zonogons.

## Value
**PASS.** The equal-modulus problem is the natural phase-flatness slice of a classical Sidon/unconditionality question. The four-character affine Walsh basis is the first case in which four independent coefficient directions can realize an eight-sided zonogon, and the theorem gives both the exact peak floor and all equality cases. The regular-octagon mechanism is structural rather than a finite table or isolated numerical optimization.

## Closest literature and limitations
The closest harmonic-analysis references are Neuwirth's exact three-frequency maximum-modulus theory and Seigner's Rademacher Sidon-constant argument. The theorem does not claim the unrestricted four-character Sidon constant or any result for larger Walsh spectra. Equivalent convex-geometric prior art under different terminology remains the main residual originality risk.

Same-model review: passed. Independent audit: not yet performed.
