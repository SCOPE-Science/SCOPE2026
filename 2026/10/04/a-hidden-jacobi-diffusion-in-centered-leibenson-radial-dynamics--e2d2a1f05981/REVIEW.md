# Same-model review

## Correctness
PASS. Starting from Braun's exact centered radial SDE and exact Barenblatt diffusivity, the logarithmic time change gives a time-homogeneous radial coefficient
\[
\bar a(y)=A y^{2-q}(C-\kappa y^q).
\]
The canonical map \(u=(\kappa/C)y^q\) then gives quadratic variation \(2K u(1-u)\) and drift \(K\{\alpha-(\alpha+\eta)u\}\). All constant identities were reconstructed from the source definitions. For \(1<q<2\), the only apparent Itô singularity at the origin is canceled by the exact \(y^{2-q}\) factor in \(\bar a\), so smooth approximation closes the boundary step. Braun's one-time self-similar density transforms exactly to \(\operatorname{Beta}(\alpha,\eta)\). The exact correlation follows from the linear drift by an integrating-factor martingale argument.

## Originality
PASS. The closest source, arXiv:2609.11558v1, gives the centered radial semimartingale and a time-independent one-time law for the self-similarly rescaled radius, but the inspected full text contains no Jacobi, Lamperti, stationary-diffusion, or autocorrelation identification. The foundational Leibenson paper arXiv:2508.12979v1 likewise constructs the nonlinear process without this scalar path reduction. Targeted searches covered radial-power, self-similar, Beta/Jacobi, logarithmic-time, and autocorrelation aliases. No implication-equivalent published theorem was located. Residual risk remains for older literature under different terminology.

## Value
PASS. The theorem is structural rather than a constant refinement: a nonlinear McKean--Vlasov radial observable becomes a classical reversible Jacobi diffusion under a canonical self-similar normalization. This turns a one-time Barenblatt scaling fact into explicit transition-level information and gives the exact correlation
\[
\operatorname{Corr}(Q_s,Q_t)=\left(\frac{s}{t}\right)^\Lambda.
\]
The transform is mathematically natural because the Barenblatt power is exactly the one that converts the degenerate radial coefficient into \(u(1-u)\).

## Closest literature and limitations
Braun's 2026 paper is the closest prior work and supplies all ambient radial formulas but stops at one-time self-similarity and stopped scaling estimates. Barbu--Grube--Rehmeier--Röckner and Barbu--Rehmeier--Röckner supply the underlying Leibenson and \(p\)-Brownian constructions. The result here is centered only, restricted to the slow-diffusion hypotheses, and concerns the normalized radial \(q\)-power rather than the full vector process or raw radius.

Same-model review: passed. Independent audit: not yet performed.
