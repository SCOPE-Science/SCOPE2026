# Review of An exact near-threshold relaxation crossover in the SEITFR conjunctivitis model

## Correctness
PASS. The proof separates the exact demographic eigenvalue using \(\dot N=\Pi-\mu N\), derives the constant-population tangent Jacobian from the published model and endemic equilibrium, and evaluates the shifted determinant with exact rational arithmetic. The odd-dimensional determinant-sign argument correctly implies that a positive value of \(\det(J_{\mathrm{tan}}+\mu I)\) is incompatible with every tangent eigenvalue lying in \(\operatorname{Re}z\le-\mu\). The standalone verifier reconstructs the determinant from the baseline fractions rather than trusting a stored coefficient.

Risk: the sign argument alone does not prove local stability throughout the entire interval below the crossover. The public claim is limited accordingly.

## Originality
PASS. The motivating article reports \(-\mu\) as the dominant eigenvalue only on its numerical grid \(1.01\le\mathcal R_0\le2.50\), and its center-manifold calculation gives qualitative near-threshold bifurcation information but no collision with the demographic mode and no exact crossover. Published-finding database searches for the exact title, SEITFR conjunctivitis aliases, dominant-eigenvalue language, and transcritical/demographic crossover terms returned no covering record. The closest general epidemic-bifurcation literature explains the existence of a critical mode but not this model-specific baseline value.

Risk: generic transcritical theory already predicts a mode tending to zero, so the novel content is the exact source-specific crossover and the proof that the published demographic-dominance observation cannot extend to the threshold, not the qualitative existence of critical slowing by itself.

## Value
PASS. The paper explicitly interprets the largest real part of the endemic Jacobian on a coarse supercritical grid and identifies \(-\mu\) as the dominant mode there. The exact value \(\mathcal R_\times\) identifies a natural, mathematically forced boundary layer missed by that grid and is directly relevant to relaxation-time interpretation near eradication. It is not an arbitrary parameter slice: it is the unique collision between the demographic eigenvalue and the constant-population tangent spectrum along the paper's own one-parameter endemic branch.

Risk: the interval is narrow and parameter-specific, so its significance is spectral and interpretive rather than a universal epidemiological threshold.

## Closest literature and limitations
The primary source is Al-Hdaibat et al., DOI 10.3934/math.20261069, especially its reproduction-number formula, endemic equilibrium, bifurcation analysis, and Figure 7 eigenvalue study. Van den Driessche and Watmough, DOI 10.1016/S0025-5564(02)00108-6, supplies general reproduction-number/center-manifold context but does not determine this crossover. No correction or erratum covering the claim was found. The exact number depends on the baseline parameter set and the \(\beta=\mathcal R_0\beta_c\) path.

Same-model review: passed. Independent audit: not yet performed.
