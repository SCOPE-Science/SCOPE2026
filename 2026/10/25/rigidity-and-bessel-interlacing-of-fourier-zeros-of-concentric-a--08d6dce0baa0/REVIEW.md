# Scientific review: annular Fourier-zero rigidity

## Correctness — PASS
The exact Fourier–Bessel formula follows by subtracting ball indicators. Differentiating \(E_\nu(t)=t^{2\nu}(J_{\nu-1}(t)^2+J_\nu(t)^2)\) gives \(E_\nu'(t)=(4\nu-2)t^{2\nu-1}J_{\nu-1}(t)^2\), strictly increasing in the integral sense when \(\nu\ge1\). The resulting strict inequality separates the endpoint signs of the scaled Bessel difference and forces a nonzero root derivative with the sign of \(J_{\nu-1}\). Thus every consecutive bracket contains precisely one simple root and no other positive root exists. Analytic dependence, both limiting cases, and the uniform counting bound then follow from that bracket and classical Bessel asymptotics. The one-dimensional trigonometric factorization gives the sharp arithmetic failure and exact double multiplicity. Independent quadrature and numerical checks agree on tested finite instances but are not used in the universal proof.

## Originality — PASS, qualified
Urcid–Padilla (2005) derives the annular optical Jinc-difference amplitude but does not provide the all-dimension strict-interlacing, simplicity, or analytic-motion theorem in its inspected discussion. DLMF 10.21.2 concerns separate contiguous Bessel functions, not their differently scaled difference. Ghobber–Jaming's Fourier–Bessel uncertainty statements and Gallatin's shape-transform formula also do not imply the root-by-root census. The proof therefore supplies an additional strict-energy comparison essential to the claim. Search absence alone cannot prove historical novelty, and older annular optical literature or Bessel inequalities may contain an equivalent lemma.

## Mathematical value — PASS
Real Fourier zeros determine annular aperture diffraction nulls and their nodal spheres. The theorem gives a complete, uniform classification in every dimension \(d\ge2\), a continuous interpolation of each null from the solid-ball limit to the thin-shell limit, and an exact one-dimensional obstruction to simplicity. These are natural structural invariants of the full annular family rather than arbitrary isolated computations.

## Sources, scope, and verification
Primary full text inspected: Urcid–Padilla, *Applied Optics* 44 (2005), 7677–7696, DOI 10.1364/AO.44.007677; Ghobber–Jaming, arXiv:1009.1710v1; Gallatin, arXiv:1109.5262v1, lawful NIST full text. DLMF §10.21 provides the classical interlacing premise. The numerical checker executed successfully on 112 positive-root instances and 12 direct radial Fourier quadratures. Remaining risk: an unindexed prior statement about scaled Bessel differences. No independent mathematical audit is claimed.

Self-review: passed. Independent audit: not yet performed.
