# Scientific assessment

## Correctness — PASS
Qubit state-discrimination SDP duality is reconstructed as a smallest-enclosing-Euclidean-ball problem with \(P_{\rm guess}=(1+\mathcal R)/4\). The tetrahedral tight-frame identity fixes the mean square distance \(\|T\|_{\rm F}^2/3\) independently of input rotation; every enclosing radius is at least its square root. A proper eigenframe rotation makes all four output radii equal to that bound, and the explicit four-outcome POVM achieves the dual. The equality argument uses a separate Walsh sign comparison, not numerical evidence. Cases of zero, singular and degenerate \(T\), nonzero affine translation and equality of eigenvalues are included. Eight physical channels and 288 additional orientations were reproduced with an independent support-set enclosing-ball check; finite experiments do not prove a universal statement.

## Originality — PASS, subject to priority risk
Bae and Hwang's arXiv:1204.2313 fixed-ensemble geometric discrimination theorem is the closest enabling prior work and is explicitly credited. Rouhbakhsh N and Ghoreishi, Quantum Information Processing 22, 323 (2023), section 4.3/Appendix B, also solve arbitrary specified mixed-qubit state discrimination and include a regular-tetrahedral example, but do not state the minimization over tetrahedral input orientation through arbitrary anisotropic affine channels or the exact optimizer characterization. Clarke et al., Phys. Rev. A 64, 012303 (2001), treats ideal tetrahedral detection. The fixed-ensemble results encompass the output-POVM part, not the entire channel-orientation claim. Searching equivalent SIC, Bloch contraction, singular-value and minimum-enclosing-ball formulations did not reveal an exact covering theorem; this is not a proof of priority. The strongest residual risk is an equivalent sharp enclosing-ball-of-affine-regular-simplex theorem from convex geometry.

## Value — PASS
The minimum-over-input-rotations guessing probability is a natural worst-orientation invariant for tetrahedral qubit communication through a given noisy channel. A sharp formula depending only on \(\|T\|_{\rm F}\), accompanied by a complete eigenframe optimizer classification and explicit optimal receiver, answers this whole family exactly—including nonunital and rank-deficient cases. The contribution is the quantified orientation classification, not the standard noiseless tetrahedron value or an isolated numerical table entry.

## Limits
Single channel use, pure equal-prior tetrahedral input signals, common input unitary rotation, unconstrained decoding POVM. Not a claim about best-case encoding, multiple uses, unknown channels, or all possible spherical codes. Comparison with logically equivalent formulations in other fields remains a possible priority risk.

Self-review: passed. Independent audit: not yet performed.
