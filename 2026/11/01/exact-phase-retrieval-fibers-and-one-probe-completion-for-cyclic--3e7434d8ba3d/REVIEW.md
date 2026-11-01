# Review of the geometric-window phase-retrieval theorem

## Correctness

The closed geometric-sum formula is exact for every positive ratio different from one. Its zeros occur only at the half translation with odd modulation in even cyclic order. The standard Weyl diagonalization identifies every Hermitian kernel entry; a connectivity argument then recovers every nonexceptional signal phase, and the additional scalar extracts the missing imaginary cross term. All quantifiers, supports and degeneracies are treated explicitly. The standalone checker passed 690 finite consistency assertions.

## Originality

The finite ambiguity diagonalization and nonzero-ambiguity sufficiency criterion belong to Bojarovska–Flinth (2015). The comparison with Grohs–Liehr–Shafkulovska (2022) concerns different continuous-domain sampling assumptions. Li (2026) treats a complex geometric seed and lifted stability rather than complete nonlinear fibers for the real geometric window. The essential new claim is the exact all-support fiber classification and universal one-probe completion for this specific window family. A residual priority risk is an equivalent result in older finite-STFT reconstruction literature.

## Mathematical value

The theorem distinguishes zero-free lifted tomography from exact phaseless reconstruction: an even-dimensional lifted operator has a kernel of real dimension half the signal length, yet phase retrieval fails only on an explicitly classified two-sparse stratum, and one scalar removes all ambiguity. This explains where a nonzero-ambiguity criterion loses information and supplies a minimal deterministic measurement repair for a natural one-parameter window family. No noise robustness is asserted.

## Limitations and relevant work

The proof uses all labelled Gabor intensities, complex signals, positive real geometric windows with ratio different from one, and exact measurements. The separate additional measurement is not itself an original-window Gabor atom. Closest sources: arXiv:1503.05800, arXiv:2211.05687, arXiv:2609.09614. Historical-priority risk remains.

Self-review: passed. Independent audit: not yet performed.
