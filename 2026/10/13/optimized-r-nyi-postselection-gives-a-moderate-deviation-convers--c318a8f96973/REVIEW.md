# Self-review

## Correctness
**PASS.** The final claim is derived from the exact postselection factor and the uniform \(\alpha\downarrow1\) expansion proved in arXiv:2610.02176v1. Retaining \(t=\alpha-1\) gives an explicit finite-\(n\) inequality. The coherent-information corollary uses only \(-S\le-\widetilde H^\uparrow_{{1+t}}\). The code-fidelity inequality follows from the source's equation (31) with \(f=F^2\), followed by exact algebra. The two parameter choices satisfy \(0<t\le1/2\) under the written hypotheses. The standalone verifier checks the new substitutions and elementary inequalities; it is corroborative, not a substitute for the source's operator-theoretic proof.

## Originality
**PASS.** The closest source, arXiv:2610.02176v1, states an \(O(\log n/\sqrt n)\) coherent-information correction and a strong converse only for a fixed asymptotic rate gap. Inspection of its relevant full text shows that it fixes \(\alpha=1+n^{{-1/2}}\). The exact factor \(g_{{n,d}}\) and uniform Taylor expansion are present, but their optimization to \(O(\sqrt{{\log n/n}})\) and the shrinking-gap fidelity bound are not. Targeted searches for coherent-information, postselection, permutation-symmetric codes, optimized Rényi order, and moderate-deviation aliases found no covering statement. The de Finetti hierarchy result arXiv:2607.23689 and classical-communication moderate-deviation result arXiv:1701.03114 concern different objectives.

## Value
**PASS.** The theorem materially changes the finite-block conclusion: the source's vanishing correction is improved by a factor \(\sqrt{{\log n}}\), and a fixed-gap converse becomes a converse for \(\Delta_n\to0\) whenever \(\Delta_n=\omega(\sqrt{{\log n/n}})\). This directly sharpens the asymptotic benchmark for permutation-symmetric quantum-code searches. It does not claim unrestricted capacity, achievability, or optimality.

## Closest literature and limitations
The decisive comparison is arXiv:2610.02176v1, especially Sections II--III, equations (19)--(23) and (31)--(35), and Appendix Lemma 15. arXiv:2607.23689 is broader in de Finetti hierarchy structure but not in this coding objective. arXiv:1701.03114 develops moderate deviations for classical communication, not this quantum coherent-information converse. Residual novelty risk is a contemporaneous or differently indexed equivalent optimization. Scientific limitations are full permutation invariance, the pure-source/isometric-encoder code class, and unevaluated channel-dependent constants.

Self-review: passed. Independent audit: not yet performed.
