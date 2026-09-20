# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The construction is explicit. The invariant circle and its period-four base dynamics follow immediately from the definition. Along that circle, the fiber derivative product telescopes exactly to
\[
R_{\theta+L\pi/2}D^L R_{-\theta}.
\]
For odd L its square, after orthogonal similarity, is -I; for even L it is ±D^L. This proves the exact parity formula for the spectral radius. Left/right rotations preserve singular values, giving singular-value growth s^L for every horizon and Lyapunov exponents log s, 0, -log s. The coordinate change H(theta,v)=(theta,R_{-theta}v) exactly conjugates the fiber dynamics to the constant diagonal map D. These identities also explain why the strict Lyapunov gap does not rescue the spectral-radius limit.

The verification artifact numerically checks the product identity, parity formula, constant singular-value rate, non-normality, and conjugacy for representative horizons. These computations support but are not needed for the algebraic proof.

## Originality

**PASS, narrowly scoped.** General nonconvergence of normalized spectral radii of cocycle products is prior art. Martínez Ramos (arXiv:2507.19624v2; IMRN 2026) explicitly states that the full limit can fail in general, cites Avila–Bochi and Morris for the limsup theory, and proves convergence only under additional irreducibility hypotheses. The source paper arXiv:2609.18017v1 cites Oseledets and covariant-Lyapunov-vector literature for its convergence statement but does not cite this spectral-radius cocycle literature.

No priority claim is made for the general fact that spectral-radius cocycle limits may fail, for cohomologous cocycle transformations, or for periodic monodromy theory. The claimed contribution is the source-specific explicit smooth counterexample with exact alternating h_L, strict top gap, genuinely non-normal one-step maps, exact singular-value growth, and the smooth-conjugacy comparison that isolates endpoint-frame mismatch in the proposed diagnostic.

A residual originality risk remains that an equivalent rotating-frame example appears elsewhere in the extensive linear-cocycle literature under different notation. That would reduce novelty of the particular example, but not the validity or usefulness of the source-specific correction.

## Value

**PASS.** The corrected statement concerns the mathematical foundation of the source paper's newly introduced diagnostic. The example shows that the proposed h_L is neither universally convergent to the top Lyapunov exponent nor invariant under smooth changes of coordinates, even in a particularly regular hyperbolic periodic setting. It also pinpoints the failure of the stated eigenvector-alignment rationale and distinguishes spectral-radius growth from the standard singular-value/Oseledets quantity. The result leaves the source paper's empirical fixed-coordinate calculations intact while specifying what additional theorem would be needed to justify a general asymptotic interpretation.

## Literature checked

- Sornette, Saiprasad and Troude, arXiv:2609.18017v1: definition of h_L and the unrestricted convergence/eigenvector-alignment statement were inspected in the primary source.
- Martínez Ramos, arXiv:2507.19624v2 / IMRN 2026: introduction, Theorem 1.1, and the discussion of Morris and Avila–Bochi were inspected. The paper explicitly distinguishes a general limsup theorem from full convergence under extra hypotheses.
- Bibliographic entries for Morris (2012) and Avila–Bochi (2002) were checked through Martínez Ramos's primary-source reference list and discussion. Their full texts were not needed to establish the narrower source correction because Martínez Ramos states the relevant prior-results relationship explicitly.

## Limitations

The result does not disprove convergence for the particular Hénon and Ikeda trajectories studied numerically in arXiv:2609.18017v1, nor does it assess the paper's chaos-control experiments. It does not provide necessary and sufficient conditions for convergence of h_L. The example lives on a smooth cylinder with a globally trivialized tangent bundle; this is sufficient to test the source's general smooth-cocycle assertion, but it is not itself a chaotic attractor.
