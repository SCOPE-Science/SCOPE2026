# Independent audit — 2026-09-29

**Record:** `2026/09/18/exact-triplet-cancellation-stuart-landau-bistability--be200ecdda00`  
**Audited source tree:** `5a7545df7ca1c7811a88a84da6b30581af1b98d1`  
**Repository snapshot:** `SCOPE-Science/SCOPE2026@253a0fe5d0217455660a277f9adb940030e567ad`  
**Disposition:** **PASSED**

## Correctness — PASS

PASS. I reconstructed the retained mixed-order three-oscillator Stuart–Landau phase equation from the source coefficient pattern. With eta=epsilon^2/(4a), the source's asymmetric physical motifs contribute minus the two emergent asymmetric coefficients, while the symmetric physical motif contributes with the opposite sign to the emergent coefficient -2 w12 w13; choosing motif weights (w12 w23, w13 w32, 2 w12 w13), cyclically, therefore cancels all three explicit triplet Fourier modes coefficient-by-coefficient. For the unweighted pairwise triangle, independent symbolic differentiation of the resulting pairwise kernel H(phi)=epsilon sin(phi+rho)+epsilon^2/(4a)[sin(2rho)+sin(2phi)+sin(phi+2rho)-sin(2phi+2rho)] gives lambda_sync=-(3 epsilon/(4a))F and Re(lambda_splay)=(3 epsilon/(8a))F with F=4a cos(rho)+3epsilon-2epsilon cos(rho)^2, hence lambda_sync=-2 Re(lambda_splay) exactly. Solving F=0 gives the stated c_* and the condition 0<epsilon<4a places the relevant root in (-1,0). The record correctly limits the conclusion to the retained O(epsilon^2) phase model and local sync/splay stability, not the full finite-coupling physical system.

## Originality — PASS

PASS, qualified. Muolo–Nakao–Bick derive the same emergent and physical motif harmonics, but their displayed simple design takes all nonzero physical motif weights equal to one, so at eta=epsilon^2/(4a) it cancels the asymmetric harmonic exactly and only half of the symmetric harmonic. I found no statement in that source of the 1:1:2 motif weighting or of the resulting exact identity lambda_sync=-2 Re(lambda_splay). The 2024 Bick–Böhle–Kuehn paper contains second-order synchronization/splay stability analysis but not this source-specific cancellation design. Targeted current searches did not locate the same exact construction. Because the primary source is only days old, unindexed parallel work remains a real priority limitation.

## Scientific value — PASS

PASS. The contribution is narrow but scientifically useful: it resolves the coefficient mismatch left by the source's simplest design using variables already present in that model and turns the engineered cancellation into a strong dynamical consequence—collapse of the local synchronization–splay bistability window to a single shifted transition. The exact symbolic identity is reusable as a design check even though it is restricted to three oscillators and second order.

## Independent checks

- Fresh SymPy derivation reproduced the residual pairwise kernel and verified lambda_sync+2 Re(lambda_splay)=0 identically.
- Coefficient matching was checked separately for all three explicit triplet Fourier modes and cyclic copies.

## Sources checked

- https://arxiv.org/abs/2609.20632 — Muolo, Nakao and Bick (2026), primary source for the second-order emergent motifs and engineered physical nonpairwise coupling.
- https://doi.org/10.1007/s00332-024-10053-3 — Bick, Böhle and Kuehn (2024), prior higher-order phase-reduction and stability context.
- https://doi.org/10.1063/5.0307452 — Namura, Muolo and Nakao (2026), general interaction-function design context.

## Limitations

- The theorem is exact only for the retained mixed-order phase truncation through O(epsilon^2); O(epsilon^3) and finite-coupling effects are outside the audit claim.
- The stability conclusion concerns synchrony and the three-oscillator splay state locally; it does not exclude other attractors.
- Originality remains qualified against very recent or unindexed work around arXiv:2609.20632.

## Audit conclusion

All three audit axes pass. No substantive research-file correction is required. This audit updates only the independent-audit verification channel; the Lean and expert-attestation channels are preserved exactly. GitHub was used only as read-only evidence during this audit.
