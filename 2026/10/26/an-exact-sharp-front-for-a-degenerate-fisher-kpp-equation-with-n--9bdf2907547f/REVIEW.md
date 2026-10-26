# Review summary

## Correctness

**PASS.** The traveling-wave substitution reduces to two polynomial coefficients. The condition \(2c_k^2-kc_k-1=0\) cancels the quadratic term, and the remaining coefficient equals \(c_k^2\). The front flux \(\phi_k\phi_k'\) vanishes at the interface from both sides, so the piecewise profile satisfies the equation distributionally.

## Originality

**PASS, with residual risk recorded.** The closest primary source is Sánchez-Garduño and Pérez-Velázquez (2016), which treats the same general nonlinear-advection model but presents numerical critical-speed fits for \(D(u)=u+eta u^2\), \(eta>0\), rather than this exact \(D(u)=u\) profile. Sherratt and Marchant (1996) and Sattar (2026) are no-advection comparisons; the latter is post-cutoff and supports only the \(k=0\) baseline. The exact formula was not found in the inspected sources, but failed searches are not treated as novelty proof.

## Value

**PASS.** This gives a closed-form, all-real-parameter benchmark for a sharp traveling front in a natural degenerate reaction–diffusion–advection model, motivated by prior numerical study of the speed dependence and the difficulty of computing sharp fronts.

## Limitations and closest literature

The claim establishes one weak traveling wave only. It does not prove uniqueness, minimality, spectral stability, or global convergence. The full 1996 PDF could not be retrieved, so no conclusion is drawn from its inaccessible sections.

References: DOI 10.1155/2016/5620839; DOI 10.1016/0893-9659(96)00069-9; arXiv:2608.23489.

Self-review: passed. Independent audit: not yet performed.
