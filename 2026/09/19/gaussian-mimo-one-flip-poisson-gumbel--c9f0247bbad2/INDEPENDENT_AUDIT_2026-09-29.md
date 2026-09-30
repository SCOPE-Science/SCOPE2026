    # Independent audit — 2026-09-29

    **Record:** `2026/09/19/gaussian-mimo-one-flip-poisson-gumbel--c9f0247bbad2`  
    **Title:** Poisson and Gumbel laws for one-flip instability in Gaussian binary MIMO  
    **Repository:** `SCOPE-Science/SCOPE2026`  
    **Audited tree:** `cf67040ca39472a167f02c9b9fa72607d54b838f`  
    **Disposition:** **PASSED**

    ## Correctness

    **PASS** — The one-bit gap is exactly 4[(rho/N)||h_i||^2+sqrt(rho/N) h_i^T w]. Conditioning on w makes the N improvement events independent because the columns h_i are independent. Uniform chi-square concentration permits sandwiching the conditional probability by Q((1+o(1))sqrt(alpha_N rho_N)) with errors exponentially smaller than 1/N. Mills' ratio at alpha_N rho_N=2 log N-log log N+c gives Np_N -> e^{-c/2}/(2 sqrt(pi)), hence conditional binomial-to-Poisson convergence. The no-improving probability, Gumbel centering, and uniform-prior MAP/minimax lower bound then follow. The local-stability event is monotone in rho because each gap has at most one positive crossing as a function of sqrt(rho).

    ## Originality

    **PASS** — Papailiopoulos' current preprint proves the one-bit ML converse only below 2 log N-log log N-s_N with s_N->infinity and identifies the same first-order heuristic scale; it does not state the O(1)-window Poisson law, the Gumbel one-flip stability threshold, or the bounded-rectangular alpha*rho formulation. Hu–Lu's older Poisson/Gumbel theorem concerns errors of the box-relaxation decoder at a different threshold/statistic. Targeted searches found no equivalent one-flip critical-window theorem. Because the proof is short once conditional independence is exposed, folklore/near-simultaneous risk remains material.

    ## Scientific value

    **PASS** — The result sharpens a divergent-slack one-bit converse to the exact constant window, identifies the full limiting distribution of the planted word's one-flip stability SNR, and extends the obstruction to bounded rectangular aspect ratios. It cleanly isolates what remains unresolved for the full ML threshold: competitors at Hamming distance at least two.

    ## Findings

    - At alpha_N rho_N=2 log N-log log N+c, the exact limiting mean is e^{-c/2}/(2 sqrt(pi)).
- Conditioning on the common Gaussian noise is sufficient to recover iid Bernoulli structure across channel columns.
- The Gumbel centering follows from setting alpha_N rho=b_N-log(4 pi)+2x in the zero-count limit.
- The theorem is only a one-flip obstruction and does not establish the complete ML critical window.

    ## Independent checks

    - Re-derived the one-bit objective gap and its monotonicity in sqrt(rho).
- Rechecked the conditional tail sandwich including dependence between a column norm and its projection.
- Applied Mills' ratio independently to recover the exact Poisson constant.
- Compared with the current Papailiopoulos preprint and the Hu–Lu box-relaxation Poisson law.

    ## Sources

    - https://arxiv.org/abs/2609.19405 — Papailiopoulos current Gaussian binary MIMO preprint; its converse uses a diverging lower-order slack.
- https://arxiv.org/abs/2006.08416 — Hu–Lu Poisson/Gumbel law for box relaxation, a different decoder statistic and threshold.

    ## Limitations

    - Only Hamming-distance-one competitors are controlled; multi-bit competitors may change the full ML lower-order threshold.
- The model is iid real Gaussian with Gaussian noise and bounded aspect ratio.
- The extreme-value refinement is short enough that folklore or near-simultaneous priority cannot be excluded completely.

    This audit is independent of the repository's pre-existing same-model review. GitHub was read only as evidence; no repository changes were made by this audit run.
